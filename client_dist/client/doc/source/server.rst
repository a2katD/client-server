Server module
=================================================

Мессенджер ICQ.
Серверная часть месенджера для обмена сообщениями.

Аргементы командной стороки:
1. -p - Порт на котором принимаются соединения
2. -a - Адрес с которого принимаются соединения.
3. --no_gui Запуск только основных функций, без графической оболочки.

server.py
~~~~~~~~~

Запускаемый модуль,содержит парсер аргументов командной строки и функционал инициализации приложения.

server. **arg_parser** ()
    Парсер аргументов командной строки, возвращает кортеж из 2 элементов:
	* Прослушиваемый адрес
	* Прослушиваемый порт

server. **config_load** ()
    Пармер конфигурации файла инициализации

server. **main** ()
    Основная логика сервера

core.py
~~~~~~~~~~~

.. autoclass:: server.core.MessageProcessor
	:members:

database.py
~~~~~~~~~~~

.. autoclass:: server.database.ServerStorage
	:members:

main_window.py
~~~~~~~~~~~~~~

.. autoclass:: server.main_window.MainWindow
	:members:

add_user.py
~~~~~~~~~~~

.. autoclass:: server.add_user.RegisterUser
	:members:

remove_user.py
~~~~~~~~~~~~~~

.. autoclass:: server.remove_user.DelUserDialog
	:members:

config_window.py
~~~~~~~~~~~~~~~~

.. autoclass:: server.config_window.ConfigWindow
	:members:

stat_window.py
~~~~~~~~~~~~~~~~

.. autoclass:: server.stat_window.StatWindow
	:members: