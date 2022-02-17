import json
import sys
from common.utils import get_message, send_message
from common.variables import *
from socket import socket, AF_INET, SOCK_STREAM


def process_client_message(message):
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
            raise ValueError
    except ValueError:
        print('Неверно указан параметр порт')
        sys.exit(1)
    except IndexError:
        print('После параметра "-p" должен быть указан порт')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_arrd = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_arrd = ''
    except IndexError:
        print('После параметра "-a" должен быть указан адрес')
        sys.exit(1)

    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((listen_arrd, listen_port))
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_addr = transport.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('При некоретное сообщение')
            client.close()


if __name__ == '__main__':
    main()
