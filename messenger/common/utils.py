import json
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append('../')
from common.errors import *
from common.log_decor import log
from common.variables import *


@log
def get_message(client):
    encoded_response = client.recv(1024)
    json_response = encoded_response.decode(ENCODING)
    response = json.loads(json_response)
    if isinstance(response, dict):
        return response
    else:
        raise TypeError


@log
def send_message(sock, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
