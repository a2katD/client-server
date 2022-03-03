import json
import sys
import logging

from errors import *
from time import time
from common.utils import send_message, get_message
from common.variables import *
from socket import socket, AF_INET, SOCK_STREAM
from log_decor import log

CLIENT_LOGGER = logging.getLogger('clientlog')


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
        return f'{meassage[RESPONSE]}: {meassage[ERROR]}'
    CLIENT_LOGGER.error(f"Сообщение не содержит {RESPONSE}")
    raise ValueError


def main():
    try:
        if len(sys.argv) > 1:
            server_address = sys.argv[1]
        else:
            server_address = DEFAULT_ADDR
        if len(sys.argv) > 2:
            server_port = int(sys.argv[2])
            if 1024 > server_port < 65535:
                CLIENT_LOGGER.error(
                    f'Попытка запуска клиента с указанием неподоходящего порта {server_port}. Доступные порты с 1024 по 65535')
                raise ValueError
        else:
            server_port = DEFAULT_PORT
    except ValueError:
        CLIENT_LOGGER.error("Неверно указан порт")
        sys.exit(1)

    CLIENT_LOGGER.info(f"Запущен клиент с параметрами:"
                       f'адрес сервера:{server_address}, порт: {server_port}')

    try:
        transport = socket(AF_INET, SOCK_STREAM)
        transport.connect((server_address, server_port))
        massage_to_server = create_presence()
        send_message(transport, massage_to_server)
        answer = process_ans(get_message(transport))
        print(answer)
    except json.JSONDecodeError:
        CLIENT_LOGGER.error(f'Не удалось декодировать Json строку')
    except ReqFieldMissingError as missing_error:
        CLIENT_LOGGER.error(f'В ответе сервера отсутствует необходимое поле'
                            f'{missing_error.missing_field}')
    except ConnectionRefusedError:
        CLIENT_LOGGER.critical(f'Не удалось подключиться к серверу {server_address}:{server_port}'
                               f'Сервер отверг запрос на подключение')


if __name__ == '__main__':
    main()
