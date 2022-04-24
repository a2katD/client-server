import argparse
import sys
import logging
import os

from PyQt5.QtWidgets import QApplication, QMessageBox
from Cryptodome.PublicKey import RSA

from common.errors import *
from common.variables import *
from common.log_decor import log
from client.database import ClientDatabase
from client.transport import ClientTransport
from client.main_window import ClientMainWindow
from client.start_dialog import UserNameDialog

CLIENT_LOGGER = logging.getLogger('clientlog')


@log
def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_ADDR, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-n', '--name', default=None, nargs='?')
    parser.add_argument('-p', '--password', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port
    client_name = namespace.name
    client_passwd = namespace.password

    if not 1023 < server_port < 65536:
        CLIENT_LOGGER.critical(
            f'Попытка запуска клиента с неподходящим номером порта: {server_port}. Допустимы адреса с 1024 до 65535. Клиент завершается.')
        sys.exit(1)

    return server_address, server_port, client_name, client_passwd


# @log
# def contacts_list_request(sock, name):
#     """Запрос контакт листа"""
#     CLIENT_LOGGER.debug(f'Запрос контакт листа для пользователя {name}')
#     req = {
#         ACTION: GET_CONTACTS,
#         TIME: time(),
#         USER: name
#     }
#     CLIENT_LOGGER.debug(f'Сформирован запрос {req}')
#     send_message(sock, req)
#     ans = get_message(sock)
#     CLIENT_LOGGER.debug(f'Получен ответ {ans}')
#     if RESPONSE in ans and ans[RESPONSE] == 202:
#         return ans[LIST_INFO]
#     else:
#         raise ServerError
#
#
# @log
# def add_contact(sock, username, contact):
#     """Добавление пользователя в контакты"""
#     CLIENT_LOGGER.debug(f'Создание контакта {contact}')
#     req = {
#         ACTION: ADD_CONTACT,
#         TIME: time(),
#         USER: username,
#         ACCOUNT_NAME: contact
#     }
#     send_message(sock, req)
#     ans = get_message(sock)
#     if RESPONSE in ans and ans[RESPONSE] == 200:
#         pass
#     else:
#         raise ServerError('Ошибка создания контакта')
#     print('Удачное создание контакта.')
#
#
# @log
# def user_list_request(sock, username):
#     """Запрашиваем известных контактов пользователей"""
#     CLIENT_LOGGER.debug(f'Запрос списка известных пользователей {username}')
#     req = {
#         ACTION: USERS_REQUEST,
#         TIME: time(),
#         ACCOUNT_NAME: username
#     }
#     send_message(sock, req)
#     ans = get_message(sock)
#     if RESPONSE in ans and ans[RESPONSE] == 202:
#         return ans[LIST_INFO]
#     else:
#         raise ServerError
#
#
# @log
# def remove_contact(sock, username, contact):
#     """Удаляем пользователей из списки контактов"""
#     CLIENT_LOGGER.debug(f'Создание контакта {contact}')
#     req = {
#         ACTION: REMOVE_CONTACT,
#         TIME: time(),
#         USER: username,
#         ACCOUNT_NAME: contact
#     }
#     send_message(sock, req)
#     ans = get_message(sock)
#     if RESPONSE in ans and ans[RESPONSE] == 200:
#         pass
#     else:
#         raise ServerError('Ошибка удаления клиента')
#     print('Удачное удаление')
#
#
# @log
# def database_load(sock, database, username):
#     """Инициализация базы данных"""
#     try:
#         users_list = user_list_request(sock, username)
#     except ServerError:
#         CLIENT_LOGGER.error('Ошибка запроса списка известных пользователей.')
#     else:
#         database.add_users(users_list)
#     try:
#         contacts_list = contacts_list_request(sock, username)
#     except ServerError:
#         CLIENT_LOGGER.error('Ошибка запроса списка контактов.')
#     else:
#         for contact in contacts_list:
#             database.add_contact(contact)


if __name__ == '__main__':
    # Загружаем параметы коммандной строки
    server_address, server_port, client_name, client_passwd = arg_parser()

    # Создаём клиентокое приложение
    client_app = QApplication(sys.argv)

    # Если имя пользователя не было указано в командной строке, то запросим его
    start_dialog = UserNameDialog()
    if not client_name or not client_passwd:
        client_app.exec_()
        # Если пользователь ввёл имя и нажал ОК, то сохраняем ведённое и удаляем объект.
        # Иначе - выходим
        if start_dialog.ok_pressed:
            client_name = start_dialog.client_name.text()
            client_passwd = start_dialog.client_passwd.text()
        else:
            exit(0)

    # Записываем логи
    CLIENT_LOGGER.info(
        f'Запущен клиент с парамертами: адрес сервера: {server_address} , '
        f'порт: {server_port}, имя пользователя: {client_name}')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    key_file = os.path.join(dir_path, f'{client_name}.key')
    if not os.path.exists(key_file):
        keys = RSA.generate(2048, os.urandom)
        with open(key_file, 'wb') as key:
            key.write(keys.export_key())
    else:
        with open(key_file, 'rb') as key:
            keys = RSA.import_key(key.read())
    CLIENT_LOGGER.debug("Keys successfully loaded.")

    database = ClientDatabase(client_name)

    # Создаём объект - транспорт и запускаем транспортный поток
    try:
        transport = ClientTransport(server_port,
                                    server_address,
                                    database,
                                    client_name,
                                    client_passwd,
                                    keys)
    except ServerError as error:
        message = QMessageBox()
        message.critical(start_dialog, 'Ошибка сервера', error.text)
        exit(1)
    transport.setDaemon(True)
    transport.start()
    del start_dialog

    # Создаём GUI
    main_window = ClientMainWindow(database, transport, keys)
    main_window.make_connection(transport)
    main_window.setWindowTitle(f'ICQ - {client_name}')
    client_app.exec_()

    # Раз графическая оболочка закрылась, закрываем транспорт
    transport.transport_shutdown()
    transport.join()
