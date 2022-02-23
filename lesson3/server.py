import json
import sys
import logging
import logs.config_server_log

from errors import *
from common.utils import get_message, send_message
from common.variables import *
from socket import socket, AF_INET, SOCK_STREAM

SERVER_LOGGER = logging.getLogger('serverlog')


def process_client_message(message):
    SERVER_LOGGER.debug(f'Разбор сообщения от клиента: {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message and message[USER][
        ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad request'
    }


def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if 1024 > listen_port > 65535:
            SERVER_LOGGER.error(
                f'Попытка запуска сервера с указанием неподоходящего порта {listen_port}. Доступные порты с 1024 по 65535')
            raise ValueError
    except ValueError:
        SERVER_LOGGER.error('Неверно указан параметр порт')
        sys.exit(1)
    except IndexError:
        SERVER_LOGGER.error('После параметра "-p" не указан порт')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_arrd = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_arrd = ''
    except IndexError:
        SERVER_LOGGER.error('После параметра "-a" не указан адрес')
        sys.exit(1)

    SERVER_LOGGER.info(f'Запущен сервер, порт для подключения: {listen_port}, '
                       f'Адрес с которого принимаются подключения: {listen_arrd if listen_arrd else "Все адреса"}')

    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((listen_arrd, listen_port))
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_addr = transport.accept()
        SERVER_LOGGER.info(f'Установлено соединение с {client_addr}')
        try:
            message_from_client = get_message(client)
            SERVER_LOGGER.debug(f'Получено сообщение {message_from_client}')
            response = process_client_message(message_from_client)
            SERVER_LOGGER.info(f'Сформирован ответ клиенту {response}')
            send_message(client, response)
            SERVER_LOGGER.debug(f'Соединение с клиентом {client_addr} закрывается')
            client.close()
        except json.JSONDecodeError:
            SERVER_LOGGER.error(f'Не удалось декодировать Json строку полученную от {client_addr}, закрытие соединения')
            client.close()
        except IncorrectDataRecivedError:
            SERVER_LOGGER.error(f'От клиента {client_addr} приняты некорректные данные, закрытие соединения')
            client.close()


if __name__ == '__main__':
    main()
