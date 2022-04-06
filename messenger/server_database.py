import datetime


class SeverStorage:
    class AllUsers:
        """Класс отображает таблицы всех пользователй"""

        def __init__(self, username):
            self.name = username
            self.last_login = datetime.datetime.now()
            self.id = None

    class ActiveUsers:
        """Класс отображает таблицы активных пользователей"""

        def __init__(self, user_id, ip_address, port, login_time):
            self.user = user_id
            self.ip_address = ip_address
            self.port = port
            self.login_time = login_time
            self.id = None

    class LoginHistory:
        """Класс отображает истории входов"""

        def __init__(self, name, date, ip, port):
            self.id = None
            self.name = name
            self.date_time = date
            self.ip = ip
    
    def __init__(self):
        pass
