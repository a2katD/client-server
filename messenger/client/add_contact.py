import logging

from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

logger = logging.getLogger('client_dist')


class AddContactDialog(QDialog):
    """Окно добавления пользователя в список контактов"""

    def __init__(self, transport, database):
        super().__init__()
        self.transport = transport
        self.database = database

        self.setFixedSize(300, 120)
        self.setWindowTitle('ICQ - Добавление контакта')
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(True)

        self.selector_label = QLabel('Выберите контакт для добавления:', self)
        self.selector_label.setFixedSize(200, 20)
        self.selector_label.move(10, 0)

        self.selector = QComboBox(self)
        self.selector.setEditable(True)
        self.selector.setFixedSize(200, 20)
        self.selector.move(10, 30)

        self.btn_refresh = QPushButton(self)
        btn_icon = QIcon('common/refresh_icon.png')
        self.btn_refresh.setIcon(btn_icon)
        self.btn_refresh.setIconSize(QSize(48, 48))
        self.btn_refresh.setFixedSize(50, 50)
        self.btn_refresh.move(230, 20)

        self.btn_ok = QPushButton('Добавить', self)
        self.btn_ok.setFixedSize(90, 30)
        self.btn_ok.move(10, 60)

        self.btn_cancel = QPushButton('Отмена', self)
        self.btn_cancel.setFixedSize(90, 30)
        self.btn_cancel.move(120, 60)
        self.btn_cancel.clicked.connect(self.close)

        # Заполняем список возможных контактов
        self.possible_contacts_update()
        # Назначаем действие на кнопку обновить
        self.btn_refresh.clicked.connect(self.update_possible_contacts)

    def possible_contacts_update(self):
        """Функция заполняем список возможных контактов
        за исключением уже добавленных
        """
        self.selector.clear()
        # множества всех контактов и контактов клиента
        contacts_list = set(self.database.get_contacts())
        users_list = set(self.database.get_users())
        # Удалим сами себя из списка пользователей, чтобы нельзя было добавить самого себя
        users_list.remove(self.transport.username)
        # Добавляем список возможных контактов
        self.selector.addItems(users_list - contacts_list)

    def update_possible_contacts(self):
        """Функция обновляет таблицу известных пользователей"""
        try:
            self.transport.user_list_update()
        except OSError:
            pass
        else:
            logger.debug('Обновление списка пользователей с сервера выполнено')
            self.possible_contacts_update()
