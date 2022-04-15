import argparse
# import json
import sys
import logging

from messenger.common.errors import *
from time import time
from common.utils import send_message, get_message
from common.variables import *
# from socket import socket, AF_INET, SOCK_STREAM
from log_decor import log
# from metaclasses import ClientVerifier
from PyQt5.QtWidgets import QApplication
from client.database import ClientDatabase
from client.transport import ClientTransport
from client.main_window import ClientMainWindow
from client.start_dialog import UserNameDialog

CLIENT_LOGGER = logging.getLogger('clientlog')

# sock_lock = threading.Lock()
# database_lock = threading.Lock()
#
#
# class ClientSender(threading.Thread, metaclass=ClientVerifier):
#     def __init__(self, account_name, sock, database):
#         self.account_name = account_name
#         self.sock = sock
#         self.database = database
#         super().__init__()
#
#     def create_exit_message(self):
#         return {
#             ACTION: EXIT,
#             TIME: time(),
#             ACCOUNT_NAME: self.account_name
#         }
#
#     def create_message(self):
#         to_user = input('Введите получателя сообщения: ')
#         message = input('Введите сообщение для отправки: ')
#
#         with database_lock:
#             if not self.database.check_user(to_user):
#                 CLIENT_LOGGER.error(f'Попытка отправить сообщение '
#                                     f'незарегистрированому получателю: {to_user}')
#                 return
#
#         message_dict = {
#             ACTION: MESSAGE,
#             SENDER: self.account_name,
#             DESTINATION: to_user,
#             TIME: time(),
#             MESSAGE_TEXT: message
#         }
#         CLIENT_LOGGER.debug(f'Сформирован словарь сообщения: {message_dict}')
#
#         with database_lock:
#             self.database.save_message(self.account_name, to_user, message)
#
#         with sock_lock:
#             try:
#                 send_message(self.sock, message_dict)
#                 CLIENT_LOGGER.info(f'От пользователся {self.account_name} отправлено сообщение для {to_user}')
#             except Exception as e:
#                 CLIENT_LOGGER.critical(f'Возникла ошибка {e} Потеряно соединение с сервером.')
#                 sys.exit(1)
#
#     def run(self):
#         self.print_help()
#         while True:
#             command = input('Введите команду: ')
#             if command == 'message':
#                 self.create_message()
#             elif command == 'help':
#                 self.print_help()
#             elif command == 'exit':
#                 try:
#                     send_message(self.sock, self.create_exit_message())
#                 except:
#                     pass
#                 print('Завершение соединения.')
#                 CLIENT_LOGGER.info('Завершение работы по команде пользователя.')
#                 sleep(1)
#                 break
#             elif command == 'contacts':
#                 with database_lock:
#                     contacts_list = self.database.get_contacts()
#                 for contact in contacts_list:
#                     print(contact)
#             elif command == 'edit':
#                 self.edit_contacts()
#             elif command == 'history':
#                 self.print_history()
#             else:
#                 print('Команда не распознана, попробойте снова. help - вывести поддерживаемые команды.')
#
#     def print_help(self):
#         print('Поддерживаемые команды:')
#         print('message - отправить сообщение. Кому и текст будет запрошены отдельно.')
#         print('history - история сообщений')
#         print('contacts - список контактов')
#         print('edit - редактирование списка контактов')
#         print('help - вывести подсказки по командам')
#         print('exit - выход из программы')
#
#     def print_history(self):
#         ask = input('Показать входящие сообщения - in, исходящие - out, все - просто Enter: ')
#         with database_lock:
#             if ask == 'in':
#                 history_list = self.database.get_history(to_who=self.account_name)
#                 for message in history_list:
#                     print(f'\nСообщение от пользователя: {message[0]} '
#                           f'от {message[3]}:\n{message[2]}')
#             elif ask == 'out':
#                 history_list = self.database.get_history(from_who=self.account_name)
#                 for message in history_list:
#                     print(f'\nСообщение пользователю: {message[1]} '
#                           f'от {message[3]}:\n{message[2]}')
#             else:
#                 history_list = self.database.get_history()
#                 for message in history_list:
#                     print(f'\nСообщение от пользователя: {message[0]},'
#                           f' пользователю {message[1]} '
#                           f'от {message[3]}\n{message[2]}')
#
#     def edit_contacts(self):
#         ans = input('Для удаления введите del, для добавления add: ')
#         if ans == 'del':
#             edit = input('Введите имя удаляемного контакта: ')
#             with database_lock:
#                 if self.database.check_contact(edit):
#                     self.database.del_contact(edit)
#                 else:
#                     CLIENT_LOGGER.error('Попытка удаления несуществующего контакта.')
#         elif ans == 'add':
#             edit = input('Введите имя создаваемого контакта: ')
#             if self.database.check_user(edit):
#                 with database_lock:
#                     self.database.add_contact(edit)
#                 with sock_lock:
#                     try:
#                         add_contact(self.sock, self.account_name, edit)
#                     except ServerError:
#                         CLIENT_LOGGER.error('Не удалось отправить информацию на сервер.')
#
#
# class ClientReader(threading.Thread, metaclass=ClientVerifier):
#     def __init__(self, account_name, sock, database):
#         self.account_name = account_name
#         self.sock = sock
#         self.database = database
#         super().__init__()
#
#     def run(self):
#         while True:
#             sleep(1)
#             with sock_lock:
#                 try:
#                     message = get_message(self.sock)
#                 except IncorrectDataRecivedError:
#                     CLIENT_LOGGER.error(f'Не удалось декодировать полученное сообщение.')
#                 except OSError as err:
#                     if err.errno:
#                         CLIENT_LOGGER.critical(f'Потеряно соединение с сервером.')
#                         break
#                 except (ConnectionError,
#                         ConnectionAbortedError,
#                         ConnectionResetError,
#                         json.JSONDecodeError):
#                     CLIENT_LOGGER.critical(f'Потеряно соединение с сервером.')
#                     break
#                 else:
#                     if ACTION in message and message[ACTION] == MESSAGE and SENDER in message and DESTINATION in message \
#                             and MESSAGE_TEXT in message and message[DESTINATION] == self.account_name:
#                         print(f'\nПолучено сообщение от пользователя {message[SENDER]}:\n{message[MESSAGE_TEXT]}')
#
#                         with database_lock:
#                             try:
#                                 self.database.save_message(message[SENDER],
#                                                            self.account_name,
#                                                            message[MESSAGE_TEXT])
#                             except Exception as e:
#                                 print(e)
#                                 CLIENT_LOGGER.error('Ошибка взаимодействия с базой данных')
#                         CLIENT_LOGGER.info(
#                             f'Получено сообщение от пользователя {message[SENDER]}:\n{message[MESSAGE_TEXT]}')
#                     else:
#                         CLIENT_LOGGER.error(f'Получено некорректное сообщение с сервера: {message}')
#
#
# @log
# def create_presence(account_name):
#     out = {
#         ACTION: PRESENCE,
#         TIME: time(),
#         USER: {
#             ACCOUNT_NAME: account_name
#         }
#     }
#     CLIENT_LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
#     return out
#
#
# @log
# def process_response_ans(message):
#     CLIENT_LOGGER.debug(f'Разбор приветственного сообщения от сервера: {message}')
#     if RESPONSE in message:
#         if message[RESPONSE] == 200:
#             return "200: OK"
#         CLIENT_LOGGER.error(f'неожиданный ответ сервера '
#                             f'{message[RESPONSE]}: {message[ERROR]}')
#         raise ServerError(f'{message[RESPONSE]}: {message[ERROR]}')
#     CLIENT_LOGGER.error(f"Сообщение не содержит {RESPONSE}")
#     raise ReqFieldMissingError(RESPONSE)


@log
def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_ADDR, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-n', '--name', default=None, nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port
    client_name = namespace.name

    if not 1023 < server_port < 65536:
        CLIENT_LOGGER.critical(
            f'Попытка запуска клиента с неподходящим номером порта: {server_port}. Допустимы адреса с 1024 до 65535. Клиент завершается.')
        sys.exit(1)

    return server_address, server_port, client_name


@log
def contacts_list_request(sock, name):
    """Запрос контакт листа"""
    CLIENT_LOGGER.debug(f'Запрос контакт листа для пользователя {name}')
    req = {
        ACTION: GET_CONTACTS,
        TIME: time(),
        USER: name
    }
    CLIENT_LOGGER.debug(f'Сформирован запрос {req}')
    send_message(sock, req)
    ans = get_message(sock)
    CLIENT_LOGGER.debug(f'Получен ответ {ans}')
    if RESPONSE in ans and ans[RESPONSE] == 202:
        return ans[LIST_INFO]
    else:
        raise ServerError


@log
def add_contact(sock, username, contact):
    """Добавление пользователя в контакты"""
    CLIENT_LOGGER.debug(f'Создание контакта {contact}')
    req = {
        ACTION: ADD_CONTACT,
        TIME: time(),
        USER: username,
        ACCOUNT_NAME: contact
    }
    send_message(sock, req)
    ans = get_message(sock)
    if RESPONSE in ans and ans[RESPONSE] == 200:
        pass
    else:
        raise ServerError('Ошибка создания контакта')
    print('Удачное создание контакта.')


@log
def user_list_request(sock, username):
    """Запрашиваем известных контактов пользователей"""
    CLIENT_LOGGER.debug(f'Запрос списка известных пользователей {username}')
    req = {
        ACTION: USERS_REQUEST,
        TIME: time(),
        ACCOUNT_NAME: username
    }
    send_message(sock, req)
    ans = get_message(sock)
    if RESPONSE in ans and ans[RESPONSE] == 202:
        return ans[LIST_INFO]
    else:
        raise ServerError


@log
def remove_contact(sock, username, contact):
    """Удаляем пользователей из списки контактов"""
    CLIENT_LOGGER.debug(f'Создание контакта {contact}')
    req = {
        ACTION: REMOVE_CONTACT,
        TIME: time(),
        USER: username,
        ACCOUNT_NAME: contact
    }
    send_message(sock, req)
    ans = get_message(sock)
    if RESPONSE in ans and ans[RESPONSE] == 200:
        pass
    else:
        raise ServerError('Ошибка удаления клиента')
    print('Удачное удаление')


@log
def database_load(sock, database, username):
    """Инициализация базы данных"""
    try:
        users_list = user_list_request(sock, username)
    except ServerError:
        CLIENT_LOGGER.error('Ошибка запроса списка известных пользователей.')
    else:
        database.add_users(users_list)
    try:
        contacts_list = contacts_list_request(sock, username)
    except ServerError:
        CLIENT_LOGGER.error('Ошибка запроса списка контактов.')
    else:
        for contact in contacts_list:
            database.add_contact(contact)


# def main():
#     print('Консольный месседжер. Клиентский модуль.')
#     server_address, server_port, client_name = arg_parser()
#
#     if not client_name:
#         client_name = input('Введите имя пользователя: ')
#     else:
#         print(f'Клиентский модуль запущен с именем: {client_name}')
#
#     CLIENT_LOGGER.info(f"Запущен клиент с параметрами: имя пользователя: {client_name},"
#                        f'адрес сервера:{server_address}, порт: {server_port}')
#
#     try:
#         transport = socket(AF_INET, SOCK_STREAM)
#         transport.settimeout(1)
#         transport.connect((server_address, server_port))
#         send_message(transport, create_presence(client_name))
#         answer = process_response_ans(get_message(transport))
#         CLIENT_LOGGER.info(f'Установлено соединение с сервером. Ответ сервера: {answer}')
#         print(f'Установлено соединение с сервером.')
#     except json.JSONDecodeError:
#         CLIENT_LOGGER.error('Не удалось декодировать полученную Json строку.')
#         exit(1)
#     except ServerError as error:
#         CLIENT_LOGGER.error(f'При установке соединения сервер вернул ошибку: {error.text}')
#         exit(1)
#     except ReqFieldMissingError as missing_error:
#         CLIENT_LOGGER.error(f'В ответе сервера отсутствует необходимое поле {missing_error.missing_field}')
#         exit(1)
#     except (ConnectionRefusedError, ConnectionError):
#         CLIENT_LOGGER.critical(
#             f'Не удалось подключиться к серверу {server_address}:{server_port}, '
#             f'конечный компьютер отверг запрос на подключение.')
#         exit(1)
#     else:
#         database = ClientDatabase(client_name)
#         database_load(transport, database, client_name)
#
#         module_reciver = ClientReader(client_name, transport, database)
#         module_reciver.daemon = True
#         module_reciver.start()
#
#         module_sender = ClientSender(client_name, transport, database)
#         module_sender.daemon = True
#         module_sender.start()
#         CLIENT_LOGGER.debug('Запущены процессы')
#
#         while True:
#             sleep(1)
#             if module_reciver.is_alive() and module_sender.is_alive():
#                 continue
#             break


if __name__ == '__main__':
    # Загружаем параметы коммандной строки
    server_address, server_port, client_name = arg_parser()

    # Создаём клиентокое приложение
    client_app = QApplication(sys.argv)

    # Если имя пользователя не было указано в командной строке, то запросим его
    if not client_name:
        start_dialog = UserNameDialog()
        client_app.exec_()
        # Если пользователь ввёл имя и нажал ОК, то сохраняем ведённое и удаляем объект.
        # Иначе - выходим
        if start_dialog.ok_pressed:
            client_name = start_dialog.client_name.text()
            del start_dialog
        else:
            exit(0)

    # Записываем логи
    CLIENT_LOGGER.info(
        f'Запущен клиент с парамертами: адрес сервера: {server_address} , '
        f'порт: {server_port}, имя пользователя: {client_name}')

    # Создаём объект базы данных
    database = ClientDatabase(client_name)

    # Создаём объект - транспорт и запускаем транспортный поток
    try:
        transport = ClientTransport(server_port, server_address, database, client_name)
    except ServerError as error:
        print(error.text)
        exit(1)
    transport.setDaemon(True)
    transport.start()

    # Создаём GUI
    main_window = ClientMainWindow(database, transport)
    main_window.make_connection(transport)
    main_window.setWindowTitle(f'Чат Программа alpha release - {client_name}')
    client_app.exec_()

    # Раз графическая оболочка закрылась, закрываем транспорт
    transport.transport_shutdown()
    transport.join()
