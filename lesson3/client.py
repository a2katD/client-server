import argparse
import json
import sys
import logging
import threading

from errors import *
from time import time, sleep
from common.utils import send_message, get_message
from common.variables import *
from socket import socket, AF_INET, SOCK_STREAM
from log_decor import log

CLIENT_LOGGER = logging.getLogger('clientlog')


@log
def create_exit_message(account_name):
    return {
        ACTION: EXIT,
        TIME: time(),
        ACCOUNT_NAME: account_name
    }


@log
def message_from_server(sock, my_message):
    while True:
        try:
            message = get_message(sock)
            if ACTION in message and message[ACTION] == MESSAGE and \
                    SENDER in message and MESSAGE_TEXT in message and \
                    DESTINATION in message and message[DESTINATION] == my_message:
                print(f'\nПолучено сообщение от пользователя {message[SENDER]}:'
                      f'\n{message[MESSAGE_TEXT]}')
                CLIENT_LOGGER.info(f'Получено сообщение от пользователя {message[SENDER]}:'
                                   f'\n{message[MESSAGE_TEXT]}')
            else:
                CLIENT_LOGGER.error(f'Получено некорректное сообщение от сервера {message}')
        except IncorrectDataRecivedError:
            CLIENT_LOGGER.error(f'Не удалось декодировать полученное сообщение.')
        except (OSError, ConnectionError, ConnectionAbortedError,
                ConnectionResetError, json.JSONDecodeError):
            CLIENT_LOGGER.critical(f'Потеряно соединение с сервером.')
            break


@log
def create_message(sock, account_name='Guest'):
    to_user = input('Введите получателя сообщения: ')
    message = input('Введите сообщение для отправки: ')

    message_dict = {
        ACTION: MESSAGE,
        SENDER: account_name,
        DESTINATION: to_user,
        TIME: time(),
        MESSAGE_TEXT: message
    }
    CLIENT_LOGGER.debug(f'Сформирован словарь сообщения: {message_dict}')
    try:
        send_message(sock, message_dict)
        CLIENT_LOGGER.info(f'От пользователся {account_name} отправлено сообщение для {to_user}')
    except Exception as e:
        print(e)
        CLIENT_LOGGER.critical(f'Возникла ошибка {e} Потеряно соединение с сервером.')
        sys.exit(1)


@log
def user_interactive(sock, username):
    print_help()
    while True:
        command = input('Введите команду: ')
        if command == 'message':
            create_message(sock, username)
        elif command == 'help':
            print_help()
        elif command == 'exit':
            send_message(sock, create_exit_message(username))
            print('Завершение соединения.')
            CLIENT_LOGGER.info('Завершение работы по команде пользователя.')
            sleep(1)
            break
        else:
            print('Команда не распознана, попробойте снова. help - вывести поддерживаемые команды.')


def print_help():
    print('Поддерживаемые команды:')
    print('message - отправить сообщение. Кому и текст будет запрошены отдельно.')
    print('help - вывести подсказки по командам')
    print('exit - выход из программы')


@log
def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    CLIENT_LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out


@log
def process_ans(meassage):
    CLIENT_LOGGER.debug(f'Разбор сообщения от сервера: {meassage}')
    if RESPONSE in meassage:
        if meassage[RESPONSE] == 200:
            return "200: OK"
        CLIENT_LOGGER.error(f'неожиданный ответ сервера '
                            f'{meassage[RESPONSE]}: {meassage[ERROR]}')
        raise ServerError(f'{meassage[RESPONSE]}: {meassage[ERROR]}')
    CLIENT_LOGGER.error(f"Сообщение не содержит {RESPONSE}")
    raise ReqFieldMissingError(RESPONSE)


@log
def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_ADDR, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-n', '--name', default=None, nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port
    client_name = namespace.name

    if not 1023 < server_port < 65536:
        CLIENT_LOGGER.critical(
            f'Попытка запуска клиента с указанием неподоходящего порта {server_port}'
            f'Доступные порты с 1024 по 65535')
        sys.exit(1)
    return server_address, server_port, client_name


def main():
    server_address, server_port, client_name = arg_parser()

    print(f'Добро пожаловать в консольный менеджер. Имя пользователя: {client_name}')
    if not client_name:
        client_name = input('Введите имя пользователя: ')
    CLIENT_LOGGER.info(f"Запущен клиент с параметрами: имя пользователя: {client_name},"
                       f'адрес сервера:{server_address}, порт: {server_port}')

    try:
        transport = socket(AF_INET, SOCK_STREAM)
        transport.connect((server_address, server_port))
        massage_to_server = create_presence(client_name)
        send_message(transport, massage_to_server)
        answer = process_ans(get_message(transport))
        CLIENT_LOGGER.info(f'Установлено соединение с сервером. Ответ сервера: {answer}')
        print(f'Установлено соединение с сервером.')
    except json.JSONDecodeError:
        CLIENT_LOGGER.error(f'Не удалось декодировать Json строку')
        sys.exit(1)
    except ReqFieldMissingError as missing_error:
        CLIENT_LOGGER.error(f'В ответе сервера отсутствует необходимое поле'
                            f'{missing_error.missing_field}')
        sys.exit(1)
    except (ConnectionRefusedError, ConnectionError):
        CLIENT_LOGGER.critical(
            f'Не удалось подключиться к серверу {server_address}:{server_port}'
            f'Сервер отверг запрос на подключение')
        sys.exit(1)
    except ServerError as error:
        CLIENT_LOGGER.error(f'При установке соединения сервер вернул ошибку: {error.text}')
        sys.exit(1)
    else:
        receiver = threading.Thread(target=message_from_server, args=(transport, client_name))
        receiver.daemon = True
        receiver.start()

        user_interface = threading.Thread(target=user_interactive, args=(transport, client_name))
        user_interface.daemon = True
        user_interface.start()
        CLIENT_LOGGER.debug('Запущены процессы')

        while True:
            sleep(1)
            if receiver.is_alive() and user_interface.is_alive():
                continue
            break


if __name__ == '__main__':
    main()
