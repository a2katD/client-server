Client module
=================================================

ICQ - современное клиентское приложение для обмена сообщениями.
Сохраняет сообщения в базу данных SQLite.
Обмен сообщениями происходит в зашифрованном виде.

Аргументы коммандной строки:
1. {имя сервера} - адрес сервера сообщений.
2. {порт} - порт по которому принимаются подключения
3. -n или --name - имя пользователя с которым произойдёт вход в систему.
4. -p или --password - пароль пользователя.

client.py
~~~~~~~~~

Запускаемый модуль,содержит парсер аргументов командной строки и функционал инициализации приложения.

client. **arg_parser** ()
    Парсер аргументов командной строки, возвращает кортеж из 4 элементов:
    
	* адрес сервера
	* порт
	* имя пользователя
	* пароль
	
    Выполняет проверку на корректность номера порта.


database.py
~~~~~~~~~~~~~~

.. autoclass:: client.database.ClientDatabase
	:members:
	
transport.py
~~~~~~~~~~~~~~

.. autoclass:: client.transport.ClientTransport
	:members:

main_window.py
~~~~~~~~~~~~~~

.. autoclass:: client.main_window.ClientMainWindow
	:members:

start_dialog.py
~~~~~~~~~~~~~~~

.. autoclass:: client.start_dialog.UserNameDialog
	:members:


add_contact.py
~~~~~~~~~~~~~~

.. autoclass:: client.add_contact.AddContactDialog
	:members:
	
	
del_contact.py
~~~~~~~~~~~~~~

.. autoclass:: client.del_contact.DelContactDialog
	:members: