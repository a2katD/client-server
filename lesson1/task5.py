from chardet import detect
from subprocess import Popen, PIPE
from platform import system



sites = ['yandex.ru', 'youtube.com', 'google.com']
param = '-n' if system().lower() == 'windows' else '-c'

for site in sites:
    args = ['ping', param, '2', site]
    result = Popen(args, stdout=PIPE)
    for line in result.stdout:
        result = detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'), end='')