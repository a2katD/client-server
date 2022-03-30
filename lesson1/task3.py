from task2 import host_range_ping
from tabulate import tabulate


def host_range_ping_tab():
    result = host_range_ping(True)
    print(tabulate([result], headers='keys', tablefmt='pipe'))


if __name__ == '__main__':
    host_range_ping_tab()
