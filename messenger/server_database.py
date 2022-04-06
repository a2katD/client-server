from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from common.variables import SERVER_DATABASE


class ServerStorage:
    Base = declarative_base()

    class AllUsers(Base):
        """Класс отображает таблицы всех пользователй"""

        __tablename__ = 'Users'
        id = Column(Integer, primary_key=True)
        name = Column(String, unique=True)
        last_login = Column(DateTime)

        def __init__(self, username):
            self.name = username
            self.last_login = datetime.now()

    class ActiveUsers(Base):
        """Класс отображает таблицы активных пользователей"""

        __tablename__ = 'Active_users'
        id = Column(Integer, primary_key=True)
        user = Column(String, ForeignKey('Users.id'), unique=True)
        ip = Column(String)
        port = Column(Integer)
        login_time = Column(DateTime)

        def __init__(self, user_id, ip, port, login_time):
            self.user = user_id
            self.ip = ip
            self.port = port
            self.login_time = login_time

    class LoginHistory(Base):
        """Класс отображает истории входов"""

        __tablename__ = 'Login_history'
        id = Column(Integer, primary_key=True)
        name = Column(String, ForeignKey('Users.id'))
        ip = Column(String)
        port = Column(Integer)
        last_conn = Column(DateTime)

        def __init__(self, name, last_conn, ip, port):
            self.name = name
            self.last_conn = last_conn
            self.ip = ip
            self.port = port

    def __init__(self):
        self.database_engine = create_engine(SERVER_DATABASE, echo=False, pool_recycle=7200)
        self.Base.metadata.create_all(self.database_engine)
        Session = sessionmaker(bind=self.database_engine)
        self.session = Session()

        self.session.query(self.ActiveUsers).delete()
        self.session.commit()

    def user_login(self, username, ip, port):
        """Обрабатываем вход пользователя, записывая его в таблицу активных юзеров,
        и в историю входов"""

        rez = self.session.query(self.AllUsers).filter_by(name=username)
        if rez.count():
            user = rez.first()
            user.last_login = datetime.now()
        else:
            user = self.AllUsers(username)
            self.session.add(user)
            self.session.commit()

        new_active_user = self.ActiveUsers(user.id, ip, port, datetime.now())
        self.session.add(new_active_user)
        history = self.LoginHistory(user.id, datetime.now(), ip, port)
        self.session.add(history)

        self.session.commit()

    def user_logout(self, username):
        """После выхода удаляем пользователя из активных"""

        user = self.session.query(self.AllUsers).filter_by(name=username).first()
        self.session.query(self.ActiveUsers).filter_by(user=user.id).delete()
        self.session.commit()

    def users_list(self):
        """Возвращаем список всех зарегистрированных пользователей"""

        query = self.session.query(
            self.AllUsers.name,
            self.AllUsers.last_login
        )
        return query.all()

    def active_users_list(self):
        """Возвращаем список всех активных пользователей"""

        query = self.session.query(
            self.AllUsers.name,
            self.ActiveUsers.ip,
            self.ActiveUsers.port,
            self.ActiveUsers.login_time
        ).join(self.AllUsers)
        return query.all()

    def login_history(self, username=None):
        """Возвращаем историю последних входов пользователей
        username: фильтрует по имени пользователя"""
        query = self.session.query(self.AllUsers.name,
                                   self.LoginHistory.ip,
                                   self.LoginHistory.port,
                                   self.LoginHistory.last_conn
                                   ).join(self.AllUsers)
        if username:
            query = query.filter(self.AllUsers.name == username)
        return query.all()


if __name__ == '__main__':
    db = ServerStorage()
    db.user_login('client_1', '192.168.1.4', 8888)
    db.user_login('client_2', '192.168.1.5', 7777)

    print(' ---- Список пользователей ----')
    print(db.active_users_list())

    db.user_logout('client_1')
    print(' ---- Выполняем логаут client_1 ----')
    print(db.active_users_list())

    print(' ---- История входов пользователя client_1 ----')
    print(db.login_history('client_1'))

    print(' ---- Список всех зарегистрированных пользователей ----')
    print(db.users_list())
