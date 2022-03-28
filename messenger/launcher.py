from subprocess import Popen, CREATE_NEW_CONSOLE
from common.variables import CLIENTS_COUNT

PROCESSES = []

while True:
    command = input(f'Запустить {CLIENTS_COUNT} клиентов "s"\n'
                    f'Закрыть всех клиентов "x" / Выйти "q"\n'
                    f'Введите команду: ')

    if command == 'q':
        break
    elif command == 's':
        PROCESSES.append(Popen('python server.py', creationflags=CREATE_NEW_CONSOLE))
        PROCESSES.extend([Popen(f'python client.py -n user{x + 1}', creationflags=CREATE_NEW_CONSOLE)
                          for x in range(CLIENTS_COUNT)])
        print(f"Запущено {CLIENTS_COUNT} клиентов")
    elif command == 'x':
        for p in PROCESSES:
            p.kill()
        PROCESSES.clear()
    else:
        print('Неизвестная команда, выберите из предложенных')
