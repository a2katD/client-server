import sys

from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QApplication, QLabel, qApp
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QPixmap

sys.path.append('../')

# Стартовый диалог с выбором имени пользователя
class UserNameDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ok_pressed = False

        self.setWindowTitle('ICQ')
        self.setFixedSize(175, 260)

        self.icon = QLabel(self)
        pixmap = QPixmap('common/icon128.png')
        self.icon.setPixmap(pixmap)
        self.icon.move(20, 10)
        self.icon.setFixedSize(128, 128)

        self.label = QLabel('Добро пожаловать в ICQ\nВведите имя пользователя:', self)
        self.label.move(15, 138)
        self.label.setFixedSize(150, 40)

        self.client_name = QLineEdit(self)
        self.client_name.setFixedSize(154, 20)
        self.client_name.move(10, 188)

        self.btn_ok = QPushButton('Начать', self)
        self.btn_ok.move(10, 218)
        self.btn_ok.clicked.connect(self.click)

        self.btn_cancel = QPushButton('Выход', self)
        self.btn_cancel.move(90, 218)
        self.btn_cancel.clicked.connect(qApp.exit)

        self.show()

    # Обработчик кнопки ОК, если поле ввода не пустое, ставим флаг и завершаем приложение.
    def click(self):
        if self.client_name.text():
            self.ok_pressed = True
            qApp.exit()


if __name__ == '__main__':
    app = QApplication([])
    dial = UserNameDialog()
    app.exec_()
