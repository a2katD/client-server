import json
import sys
import os
from common.variables import MAX_PACKEGE_LENGTH, ENCODING

sys.path.append(os.path.join(os.getcwd(), '..'))

from errors import *
from log_decor import log


@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKEGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        if isinstance(json_response, str):
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            else:
                raise IncorrectDataRecivedError
    raise IncorrectDataRecivedError


@log
def send_message(sock, message):
    if isinstance(message, dict):
        json_message = json.dumps(message)
        encoded_message = json_message.encode(ENCODING)
        sock.send(encoded_message)
    else:
        raise NonDictInputError
