from subprocess import Popen, CREATE_NEW_CONSOLE
from common.variables import CLIENTS_LISTEN_COUNT, CLIENTS_SENDER_COUNT

P_LIST = []

while True:
    command = input(f'Запустить {CLIENTS_LISTEN_COUNT} слушающих клиентов "l"\n'
                    f'Запустить {CLIENTS_SENDER_COUNT} отправляющих клиентов "s"\n'
                    f'Закрыть всех клиентов "x" / Выйти "q"\n'
                    f'Введите команду: ')

    if command == 'q':
        break
    elif command == 'l':
        for _ in range(CLIENTS_LISTEN_COUNT):
            P_LIST.append(Popen('python client.py -m listen', creationflags=CREATE_NEW_CONSOLE))
        print(f"Запущено {CLIENTS_LISTEN_COUNT} клиентов")
    elif command == 's':
        for _ in range(CLIENTS_SENDER_COUNT):
            P_LIST.append(Popen('python client.py -m send', creationflags=CREATE_NEW_CONSOLE))
        print(f"Запущено {CLIENTS_SENDER_COUNT} клиентов")
    elif command == 'x':
        for p in P_LIST:
            p.kill()
        P_LIST.clear()
    else:
        print('Неизвестная команда, выберите из предложенных')
