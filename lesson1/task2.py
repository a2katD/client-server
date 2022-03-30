import socket
from task1 import host_ping
from ipaddress import ip_address


def host_range_ping():
    while True:
        ip = input('Введите начальный ip адрес: ')
        try:
            IPV4 = ip_address(socket.gethostbyname(ip))
        except:
            print('Некорректный ip адрес')
            continue
        quantity = input('Введите сколько адресов проверить: ')
        if not quantity.isdigit() or int(quantity) <= 0:
            print('Неверное значение, введите положительное число')
            continue
        break

    for i in range(int(quantity)):
        host_ping([IPV4 + i])


if __name__ == '__main__':
    host_range_ping()
