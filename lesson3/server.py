import argparse
import json
import sys
import logging

from select import select
from errors import *
from common.utils import get_message, send_message
from common.variables import *
from socket import socket, AF_INET, SOCK_STREAM
from log_decor import log
from time import time

SERVER_LOGGER = logging.getLogger('serverlog')


@log
def process_client_message(message, messages_list, client):
    SERVER_LOGGER.debug(f'Разбор сообщения от клиента: {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        send_message(client, {RESPONSE: 200})
        return
    elif ACTION in message and message[ACTION] == MESSAGE and TIME in message \
            and MESSAGE_TEXT in message:
        messages_list.append((message[ACCOUNT_NAME], message[MESSAGE_TEXT]))
    else:
        send_message(client, {RESPONSE: 400, ERROR: 'Bad request'})
        return


@log
def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    listen_addr = namespace.a
    listen_port = namespace.p

    if not 1023 < listen_port < 65536:
        SERVER_LOGGER.critical(
            f'Попытка запуска сервера с указанием неподходящего порта '
            f'{listen_port}. Доступные порты с 1024 по 65535')
        sys.exit(1)

    return listen_addr, listen_port


def main():
    listen_addr, listen_port = arg_parser()

    SERVER_LOGGER.info(f'Запущен сервер, порт для подключения: {listen_port}, '
                       f'Адрес с которого принимаются подключения: {listen_addr if listen_addr else "Все адреса"}')

    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((listen_addr, listen_port))
    transport.settimeout(1)
    transport.listen(MAX_CONNECTIONS)

    clients = []
    messages = []

    while True:
        try:
            client, client_addr = transport.accept()
        except OSError as err:
            if err.errno:
                print(err.errno)
        else:
            SERVER_LOGGER.info(f'Установлено соединение с {client_addr}')
            clients.append(client)

        recv_data_list = []
        send_data_list = []
        err_list = []

        try:
            if clients:
                recv_data_list, send_data_list, err_list = select(clients, clients, err_list, 0)
        except OSError:
            pass
        if recv_data_list:
            for client_with_message in recv_data_list:
                try:
                    process_client_message(get_message(client_with_message),
                                           messages, client_with_message)
                except:
                    SERVER_LOGGER.info(f'Клиент {client_with_message.getpeername()} '
                                       f'отключился от сервера.')
        if messages and send_data_list:
            message = {
                ACTION: MESSAGE,
                SENDER: messages[0][0],
                TIME: time(),
                MESSAGE_TEXT: messages[0][1]
            }
            del messages[0]
            for waiting_client in send_data_list:
                try:
                    send_message(waiting_client, message)
                except:
                    SERVER_LOGGER.info(f'Клиент {waiting_client.getpeername()} отключился от сервера.')
                    waiting_client.close()
                    clients.remove(waiting_client)


if __name__ == '__main__':
    main()
