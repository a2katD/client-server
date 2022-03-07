import argparse
import sys
import logging

from select import select
from common.utils import get_message, send_message
from common.variables import *
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from log_decor import log

SERVER_LOGGER = logging.getLogger('serverlog')


@log
def process_client_message(message, messages_list, client, clients, names):
    SERVER_LOGGER.debug(f'Разбор сообщения от клиента: {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message:
        if message[USER][ACCOUNT_NAME] not in names.keys():
            names[message[USER][ACCOUNT_NAME]] = client
            send_message(client, {RESPONSE: 200})
        else:
            send_message(client, {RESPONSE: 400, ERROR: 'Имя пользователя занято'})
            clients.remove(client)
            client.close()
        return
    elif ACTION in message and message[ACTION] == MESSAGE and TIME in message \
            and MESSAGE_TEXT in message and DESTINATION in message \
            and SENDER in message:
        messages_list.append(message)
        return
    elif ACTION in message and message[ACTION] == EXIT and ACCOUNT_NAME in message:
        clients.remove(names[message[ACCOUNT_NAME]])
        names[message[ACCOUNT_NAME]].close()
        del names[message[ACCOUNT_NAME]]
        return
    else:
        send_message(client, {RESPONSE: 400, ERROR: 'Bad request'})
        return


def process_message(message, names, listen_socks):
    if message[DESTINATION] in names and names[message[DESTINATION]] in listen_socks:
        send_message(names[message[DESTINATION]], message)
        SERVER_LOGGER.info(f'Отправлено сообщение пользователю {message[DESTINATION]} '
                           f'от пользователя {message[SENDER]}.')
    elif message[DESTINATION] in names and names[message[DESTINATION]] not in listen_socks:
        raise ConnectionError
    else:
        SERVER_LOGGER.error(
            f'Пользователь {message[DESTINATION]} не зарегистрирован на сервере, '
            f'отправка сообщения невозможна.')


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
    transport.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    transport.bind((listen_addr, listen_port))
    transport.settimeout(1)

    clients = []
    messages = []
    names = dict()

    transport.listen(MAX_CONNECTIONS)
    print('Сервер запущен и находится в режиме прослушивания')
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
                    process_client_message(
                        get_message(client_with_message),
                        messages, client_with_message, clients, names)
                except Exception:
                    SERVER_LOGGER.info(
                        f'Клиент {client_with_message.getpeername()} '
                        f'отключился от сервера.')
        for msg in messages:
            try:
                process_message(msg, names, send_data_list)
            except Exception:
                SERVER_LOGGER.info(f'Связь с клиентом с именем '
                                   f'{msg[DESTINATION]} была потеряна')
                clients.remove(names[msg[DESTINATION]])
                del names[msg[DESTINATION]]
        messages.clear()


if __name__ == '__main__':
    main()
