import socket
from task1 import host_ping
from ipaddress import ip_address


def host_range_ping(tabulate=False):
    while True:
        ip = input('Введите начальный ip адрес: ')
        try:
            IPV4 = ip_address(socket.gethostbyname(ip))
            last_oct = int(str(IPV4).split('.')[3])
        except:
            print('Некорректный ip адрес')
            continue
        quantity = input('Введите сколько адресов проверить: ')
        if not quantity.isdigit() or int(quantity) <= 0:
            print('Неверное значение, введите положительное число')
            continue
        if (last_oct + int(quantity)) > 256:
            print(f'По условию можно менять только последний октет.'
                  f'т.е. максимальное число хостов {256 - last_oct}')
        break

    host_list = [str(IPV4 + i) for i in range(int(quantity))]
    return host_ping(host_list, tabulate)


if __name__ == '__main__':
    host_range_ping()
