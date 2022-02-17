import json
import sys

from time import time
from common.utils import send_message, get_message
from common.variables import *
from socket import socket, AF_INET, SOCK_STREAM


def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(meassage):
    if RESPONSE in meassage:
        if meassage[RESPONSE] == 200:
            return "200: OK"
        return f'{meassage[RESPONSE]}: meassage[ERROR]'
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
                raise ValueError
        else:
            server_port = DEFAULT_PORT
    except ValueError:
        print('Неверно указан параметр порт')
        sys.exit(1)

    transport = socket(AF_INET, SOCK_STREAM)
    transport.connect((server_address, server_port))
    massage_to_server = create_presence()
    send_message(transport, massage_to_server)
    try:
        answer = process_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print("Не удалось декодировать сообщение с сервера")


if __name__ == '__main__':
    main()
