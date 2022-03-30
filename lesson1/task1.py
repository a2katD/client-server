from subprocess import Popen, PIPE
import chardet
import platform
import socket
from ipaddress import ip_address, ip_network, ip_interface

ip_list = [
    '87.250.250.242',
    'yandex.ru',
    '74.125.131.136',
    'google.com',
    '192.168.99.99',
    '192.168.3.99',
]


def host_ping(ip_list):
    key = '-n' if platform.system().lower() == 'windows' else '-c'

    for ip in ip_list:
        try:
            IPV4 = ip_address(ip)
        except ValueError:
            IPV4 = ip_address(socket.gethostbyname(ip))
        command = ['ping', key, '2', '-w', '1', str(IPV4)]
        process = Popen(command, stdout=PIPE)
        if process.wait() == 0:
            print(f'Узел {IPV4} доступен')
        else:
            print(f'Узел {IPV4} недоступен')

host_ping(ip_list)
