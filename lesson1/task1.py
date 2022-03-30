from subprocess import Popen, PIPE
import chardet
import platform
import socket
from ipaddress import ip_address


def host_ping(ip_list, tabulate=False):
    key = '-n' if platform.system().lower() == 'windows' else '-c'
    result = {'Reachable': "", 'Unreachable': ""}
    for ip in ip_list:
        try:
            IPV4 = ip_address(ip)
        except ValueError:
            try:
                IPV4 = ip_address(socket.gethostbyname(ip))
            except:
                print(f'Узел {ip} недоступен')
                continue
        command = ['ping', key, '1', '-w', '1', str(IPV4)]
        process = Popen(command, stdout=PIPE)
        if tabulate == False:
            if process.wait() == 0:
                print(f'Узел {IPV4} доступен')
            else:
                print(f'Узел {IPV4} недоступен')
        else:
            if process.wait() == 0:
                result['Reachable'] += f'{IPV4}\n'
            else:
                result['Unreachable'] += f'{IPV4}\n'
    return result


if __name__ == '__main__':
    ip_list = [
        '87.250.250.242',
        'yandex.ru',
        '192.168.99.99',
        '192.168.3.99',
        'sdfgksjdnfgsdngj.ru'
    ]
    host_ping(ip_list)
