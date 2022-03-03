import sys
import logging
import logs.config_server_log
import logs.config_client_log

if sys.argv[0].find('client.py') == -1:
    LOGGER = logging.getLogger('serverlog')
else:
    LOGGER = logging.getLogger('clientlog')


def log(func):
    def wrap(*args, **kwargs):
        res = func(*args, **kwargs)
        LOGGER.debug(f'функция {func.__name__} с аргументами {args}, {kwargs} вызвана из функции {func.__module__}')
        return res

    return wrap
