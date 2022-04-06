DEFAULT_PORT = 7777
DEFAULT_ADDR = 'localhost'
MAX_CONNECTIONS = 5
MAX_PACKEGE_LENGTH = 1024
ENCODING = 'utf-8'
CLIENTS_COUNT = 2
SERVER_DATABASE = 'sqlite:///server_base.db3'

ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'from'
DESTINATION = 'to'

PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'
EXIT = 'exit'

RESPONSE_200 = {RESPONSE: 200}
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}
