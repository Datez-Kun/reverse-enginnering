# Python bytecode 2.7
import requests, os, random, sys, time, subprocess as sp
from bs4 import BeautifulSoup as bs
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
    for i in range(6):
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
        logo()
    except requests.exceptions.ConnectionError:
        print '%s[%sx%s] %sTidak ada koneksi' % (W1, R1, W1, W0)
        time.sleep(1)
        metu()


def enc(hash, tp, tipe):
    spin()
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    dat = {'mbutt': hash, 'ope': tp, 'submit': tipe}
    a = requests.post('http://tools-ixid.ga/enc-dec.php', headers={'User-Agent': '{acak}'}, data=dat)
    b = bs(a.content, 'html.parser')
    c = b.find_all('textarea')[1]
    d = c.text
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult : ' + d
    print
    raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mTekan enter untuk back')
    main()


def dec(hash, tp, tipe):
    spin()
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    dat = {'mbutt': hash, 'ope': tp, 'crack': tipe}
    a = requests.post('http://tools-ixid.ga/enc-dec.php', headers={'User-Agent': '{acak}'}, data=dat)
    b = bs(a.content, 'html.parser')
    c = b.find_all('textarea')[1]
    d = c.text
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult : ' + d
    print
    raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mTekan enter untuk back')
    main()


def e1():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e1()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e1()
        tp = 'urlencode'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e1()
        tp = 'urlencode'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e1()


def e2():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e2()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e2()
        tp = 'base64'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e2()
        tp = 'base64'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e2()


def e3():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e3()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e3()
        tp = 'ur'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e3()
        tp = 'ur'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e3()


def e4():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e4()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e4()
        tp = 'json'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e4()
        tp = 'json'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e4()


def e5():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e5()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e5()
        tp = 'gzinflates'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e5()
        tp = 'gzinflates'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e5()


def e6():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e6()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e6()
        tp = 'str2'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e6()
        tp = 'str2'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e6()


def e7():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e7()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e7()
        tp = 'gzinflate'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e7()
        tp = 'gzinflate'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e7()


def e8():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e8()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e8()
        tp = 'gzinflater'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e8()
        tp = 'gzinflater'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e8()


def e9():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e9()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e9()
        tp = 'gzinflatex'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e9()
        tp = 'gzinflatesx'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e9()


def e10():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e10()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e10()
        tp = 'gzinflatew'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e10()
        tp = 'gzinflatew'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e10()


def e11():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e11()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e11()
        tp = 'str'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e11()
        tp = 'str'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e11()


def e12():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e12()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e12()
        tp = 'url'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e12()
        tp = 'url'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e12()


def e13():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e13()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e13()
        tp = 'hexencode'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e13()
        tp = 'hexencode'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e13()


def e14():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e14()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e14()
        tp = 'md5'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e14()
        tp = 'md5'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e14()


def e15():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e15()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e15()
        tp = 'sha1'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e15()
        tp = 'sha1'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e15()


def e16():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e16()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e16()
        tp = 'str_rot13'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e16()
        tp = 'str_rot13'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e16()


def e17():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e17()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e17()
        tp = 'strlen'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e17()
        tp = 'strlen'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e17()


def e18():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e18()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e18()
        tp = 'xxx'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e18()
        tp = 'xxx'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e18()


def e19():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e19()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e19()
        tp = 'bbb'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e19()
        tp = 'bbb'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e19()


def e20():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e20()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e20()
        tp = 'aaa'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e20()
        tp = 'aaa'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e20()


def e21():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e21()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e21()
        tp = 'www'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e21()
        tp = 'www'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e21()


def e22():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e22()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e22()
        tp = 'sss'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e22()
        tp = 'sss'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e22()


def e23():
    logo()
    print ''
    print '%s[%s#%s] %sEncrypt/Decrypt\n%s[%s!%s] %sPilih tipe cok\n   %s[%s1%s] %sEncrypt\n   %s[%s2%s] %sDecrypt' % (G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1, G1, Y1, G1, W1)
    pil = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mPilih: ')
    if pil == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        e23()
    elif pil == '1':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e23()
        tp = 'eee'
        tipe = 'ENCODE'
        enc(hash, tp, tipe)
    elif pil == '2':
        hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
        if hash == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            e23()
        tp = 'eee'
        tipe = 'DECODE'
        dec(hash, tp, tipe)
    else:
        print '%s[%s!%s] %sPilihan anda salah' % (G1, R1, G1, W0)
        e23()


def auto():
    logo()
    hash = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mMasukkan kode mu: ')
    if hash == '':
        print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
        time.sleep(0.8)
        auto()
    a = requests.get('https://md5calc.com/hash/md2/' + hash)
    b = bs(a.content, 'html.parser')
    c = b.find_all('td', style='white-space:normal;word-break:break-all;')[1]
    d = b.find_all('td', style='white-space:normal;word-break:break-all;')[2]
    e = b.find_all('td', style='white-space:normal;word-break:break-all;')[3]
    f = b.find_all('td', style='white-space:normal;word-break:break-all;')[4]
    g = b.find_all('td', style='white-space:normal;word-break:break-all;')[5]
    h = b.find_all('td', style='white-space:normal;word-break:break-all;')[6]
    i = b.find_all('td', style='white-space:normal;word-break:break-all;')[7]
    j = b.find_all('td', style='white-space:normal;word-break:break-all;')[8]
    k = b.find_all('td', style='white-space:normal;word-break:break-all;')[9]
    l = b.find_all('td', style='white-space:normal;word-break:break-all;')[10]
    m = b.find_all('td', style='white-space:normal;word-break:break-all;')[11]
    n = b.find_all('td', style='white-space:normal;word-break:break-all;')[12]
    o = b.find_all('td', style='white-space:normal;word-break:break-all;')[13]
    p = b.find_all('td', style='white-space:normal;word-break:break-all;')[14]
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult MD2: ', c.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult MD4 : ', d.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult MD5 : ', e.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult SHA1 : ', f.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult SHA224 : ', g.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult SHA256 : ', h.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult SHA384 : ', i.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult SHA512/224 : ', j.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult SHA512/256 : ', k.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult SHA512 : ', l.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult SHA3-224 : ', m.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult SHA3-256 : ', n.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult SHA3-384 : ', o.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult SHA3-512 : ', p.text.replace(' ', '').replace('\n', '')
    print
    raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[1;37mTekan enter untuk back')
    main()


def logo():
    os.system('clear')
    ketik('%s _____%s              __    %s _______               %s__\n%s|     \\%s.---.-.----.|  |--.%s|   |   |%s.---.-.-----.|  |--.\n%s|  --  %s|  _  |   _||    < %s|       |%s|  _  |__ --||     |\n%s|_____/%s|___._|__|  |__|__|%s|___|___|%s|___._|_____||__|__|\n Powered by http://tools-ixid.ga\n' % (G1, W1, G1, W1, G1, W1, G1, W1, G1, W1, G1, W1, G1, W1, G1, W1))


def menu():
    print '%s{%s01%s} %sURL\n%s{%s02%s} %sBASE64\n%s{%s03%s} %sCONVERT_UU\n%s{%s04%s} %sJSON\n%s{%s05%s} %sGZINFLATE - BASE64\n%s{%s06%s} %sSTR_ROT13 - BASE64\n%s{%s07%s} %sSTR_ROT13 - GZINFLATE - BASE64\n%s{%s08%s} %sGZINFLATE - STR_ROT13 - BASE64\n%s{%s09%s} %sGZINFLATE - STR_ROT13 - GZINFLATE - BASE64\n%s{%s10%s} %sSTR_ROT13 - CONVERT_UU - URL - GZINFLATE -\n     STR_ROT13 - BASE64 - CONVERT_UU - GZINFLATE - URL -\n     STR_ROT13 - GZINFLATE - BASE64\n%s{%s11%s} %sSTR_ROT13 - GZINFLATE - STR_ROT13 - BASE64\n%s{%s12%s} %sBASE64 - GZINFLATE - STR_ROT13 - CONVERT_UU -\n     GZINFLATE - BASE64\n%s{%s13%s} %sHEX ENCODE-DECODE\n%s{%s14%s} %sMD5 HASH\n%s{%s15%s} %sSHA1 HASH\n%s{%s16%s} %sROT13 HASH\n%s{%s17%s} %sSTRLEN\n%s{%s18%s} %sUNESCAPE\n%s{%s19%s} %sCHAR AT\n%s{%s20%s} %sCHR - BIN2HEX - SUBSTR\n%s{%s21%s} %sCHR\n%s{%s22%s} %sHTMLSPECIALCHARS\n%s{%s23%s} %sESCAPE\n%s{%s24%s} %sAUTO HASH\n%s{%s99%s} %sContact ( Whatsapp)\n%s{%s00%s} %sExit' % (W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, R1, W1, W0, W1, R1, W1, W0)


def main():
    try:
        os.system('git pull')
        logo()
        menu()
        no = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0', '00', '99']
        pilih = raw_input('\n%s\xe2\x95\x94%s[%sD4RK5H4D0W5%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))
        while pilih not in no:
            logo()
            menu()
            print '\n%s[%sx%s] %sPilihan Anda salah' % (W0, R1, W0, R0)
            pilih = raw_input('%s\xe2\x95\x94%s[%sD4RK5H4D0W5%s]\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s[%sPilih%s]> %s' % (C1, W1, P1, W1, C1, W1, P1, W1, W0))

        if pilih == '1' or pilih == '01':
            e1()
        elif pilih == '2' or pilih == '02':
            e2()
        elif pilih == '3' or pilih == '03':
            e3()
        elif pilih == '4' or pilih == '04':
            e4()
        elif pilih == '5' or pilih == '05':
            e5()
        elif pilih == '6' or pilih == '06':
            e6()
        elif pilih == '7' or pilih == '07':
            e7()
        elif pilih == '8' or pilih == '08':
            e8()
        elif pilih == '9' or pilih == '09':
            e9()
        elif pilih == '10':
            e10()
        elif pilih == '11':
            e11()
        elif pilih == '12':
            e12()
        elif pilih == '13':
            e13()
        elif pilih == '14':
            e14()
        elif pilih == '15':
            e15()
        elif pilih == '16':
            e16()
        elif pilih == '17':
            e17()
        elif pilih == '18':
            e18()
        elif pilih == '19':
            e19()
        elif pilih == '20':
            e20()
        elif pilih == '21':
            e21()
        elif pilih == '22':
            e22()
        elif pilih == '23':
            e23()
        elif pilih == '24':
            auto()
        elif pilih == '99':
            koneksi()
            print
            chat = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mIsi pesan mu : ')
            chat.replace(' ', '%20')
            spin()
            sp.check_output(['am', 'start', 'https://api.whatsapp.com/send?phone=628996604524&text=Report : ' + chat + ''])
            main()
        elif pilih == '0' or pilih == '00':
            metu()
    except requests.exceptions.ConnectionError:
        print '%s[%sx%s] %sTidak ada koneksi' % (W1, R1, W1, W0)
        time.sleep(1)
        metu()


if __name__ == '__main__':
    main()


# Decompiled At : Wed Apr  1 13:29:41 2020 
