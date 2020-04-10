# Decompiled At : Fri Apr 10 19:36:05 WIB 2020
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
hijau = '\x1b[32m'
cyan = '\x1b[36m'
kuning = '\x1b[33;1m'
ungu = '\x1b[35m'
putih = '\x1b[37m'
merah = '\x1b[31m'
biru = '\x1b[34m'
tip = '%s          [%sPilih Tipenya%s]\n%s            [%s1%s]%s Encrypt\n%s            [%s2%s]%s Decrypt\n' % (putih, cyan, putih, putih, merah, putih, hijau, putih, merah, putih, hijau)

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
    lix = [
     '/', '-', '\xe2\x95\xb2', '|']
    for i in range(6):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.2)
            sys.stdout.flush()


licen = '\n       %s[%sLICENSE HASHER%s]%sv0.1\n  %s|>%s Tenang Licensenya Gratis kok %s<|\n  %s|> %s[%sA%s] %sTEKAN A UNTUK CHAT ADMIN %s<|\n' % (merah, putih, merah, kuning, merah, cyan, merah, merah, putih, hijau, putih, cyan, merah)

def metu():
    print '%s[%sx%s] %sExiting Program' % (W1, R1, W1, R0)
    exit(1)


def main1():
    print '\x1b[37m==============================================='
    print '\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97  \x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97 \x1b[32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97 \x1b[32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97  \x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97\x1b[32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97\x1b[32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97'
    print '\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91  \x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91  \x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97'
    print '\x1b[32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\x1b[32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\x1b[32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97\x1b[32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\x1b[32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97  \x1b[32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x94\xe2\x95\x9d'
    print '\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97'
    print '\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91  \x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91  \x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\x1b[32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91  \x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91\x1b[32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x97\x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91  \x1b[32m\xe2\x96\x88\xe2\x96\x88\x1b[31m\xe2\x95\x91'
    print '\x1b[31m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d'
    print '           \x1b[31m[\x1b[37mAuthor\x1b[31m]=[ \x1b[36mRizky ID'
    print '           \x1b[31m[\x1b[37mCreate\x1b[31m]=[ \x1b[36m8 April 2020'
    print '           \x1b[31m[\x1b[37mFungsi\x1b[31m]=[ \x1b[36mEncrypt/Decrypt'
    print '\x1b[37m==============================================='


ban = '\n\x1b[37m{\x1b[31m01\x1b[37m} \x1b[32mURL\n\x1b[37m{\x1b[31m02\x1b[37m} \x1b[32mBASE64\n\x1b[37m{\x1b[31m03\x1b[37m} \x1b[32mCONFERT_UU\n\x1b[37m{\x1b[31m04\x1b[37m} \x1b[32mJSON\n\x1b[37m{\x1b[31m05\x1b[37m} \x1b[32mGZINFLATE - BASE64\n\x1b[37m{\x1b[31m06\x1b[37m} \x1b[32mSTR_ROT13 - BASE64\n\x1b[37m{\x1b[31m07\x1b[37m} \x1b[32mSTR_ROT13 - GZINFLATE - BASE64\n\x1b[37m{\x1b[31m08\x1b[37m} \x1b[32mGZINFLATE - STR_ROT13 - BASE64\n\x1b[37m{\x1b[31m09\x1b[37m} \x1b[32mGZINFLATE - STR_ROT13 - GZINFLATE - BASE64\n\x1b[37m{\x1b[31m10\x1b[37m} \x1b[32mSTR_ROT13 - CONVERT_UU - URL - GZINFLATE -\n\x1b[37m     \x1b[32mSTR_ROT13 - BASE64 - CONVERT_UU - GZINFLATE -\n \x1b[37m    \x1b[32mURL - STR_ROT13 - GZINFLATE - BASE64\n\x1b[37m{\x1b[31m11\x1b[37m} \x1b[32mSTR_ROT13 - GZINFLATE - STR_ROT13 - BASE64\n\x1b[37m{\x1b[31m12\x1b[37m} \x1b[32mBASE64 - GZINFLATE - STR_ROT13 - CONVERT_UU -\n \x1b[37m    \x1b[32mGZINFLATE - BASE64\n\x1b[37m{\x1b[31m13\x1b[37m} \x1b[32mHEX ENCODE-DECODE\n\x1b[37m{\x1b[31m14\x1b[37m} \x1b[32mMD5 HASH\n\x1b[37m{\x1b[31m15\x1b[37m} \x1b[32mSHA1 HASH\n\x1b[37m{\x1b[31m16\x1b[37m} \x1b[32mROT13 HASH\n\x1b[37m{\x1b[31m17\x1b[37m} \x1b[32mSTRLEN\n\x1b[37m{\x1b[31m18\x1b[37m} \x1b[32mUNESCAPE\n\x1b[37m{\x1b[31m19\x1b[37m} \x1b[32mCHAR AT\n\x1b[37m{\x1b[31m20\x1b[37m} \x1b[32mCHR - BIN2HEX - SUBSTR\n\x1b[37m{\x1b[31m21\x1b[37m} \x1b[32mCHR\n\x1b[37m{\x1b[31m22\x1b[37m} \x1b[32mHTMLSPECIALCHARS\n\x1b[37m{\x1b[31m23\x1b[37m} \x1b[32mESCAPE\n\x1b[37m{\x1b[31m24\x1b[37m} \x1b[32mAUTO HASH\n\x1b[37m===============================================\n\x1b[31m[\x1b[37mC\x1b[31m]=[ \x1b[35mCHAT ADMIN\n\x1b[31m[\x1b[37mF\x1b[31m]=[ \x1b[35mFOLLOW ADMIN\n\x1b[31m[\x1b[37mE\x1b[31m]=[ \x1b[31mEXIT PROGRAM\n\x1b[37m===============================================\n'

def main():
    os.system('clear')
    main1()
    print ban
    pilih = raw_input('%s    >>>>%s ' % (biru, hijau))
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
    elif pilih == 'C' or pilih == 'c':
        print
        chat = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mIsi pesan mu : ')
        chat.replace(' ', '%20')
        spin()
        sp.check_output(['am', 'start', 'https://api.whatsapp.com/send?phone=6288261764938&text=HASHER : ' + chat + ''])
        main()
    elif pilih == 'F' or pilih == 'f':
        os.system('xdg-open https://www.instagram.com/riski_1504')
        sys.exit()
    elif pilih == 'E' or pilih == 'e':
        print '%s(%s!%s) %sKeluar' % (putih, merah, putih, merah)
        sys.exit()


def muat():
    m = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
    print
    for b in m:
        sys.stdout.write('\r' + putih + '[' + cyan + '#' + putih + ']' + putih + ' Sedang Menghubungkan' + merah + ' [' + hijau + b + putih + '%' + merah + ']')
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)


def pilih():
    os.system('clear')
    print licen
    mana = raw_input('\n%s(%s!%s)%s Masukan License%s :%s ' % (putih, merah, putih, putih, merah, hijau))
    if mana == '':
        print '%s(%s!%s)%s Jangan Kosong' % (putih, merah, putih, merah)
        pilih()
    elif mana in ('mikuna5bq2kuu', 'Abogabegaefi1y3'):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('pinajquaqjuabb', 'macet52aaremkunek'):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('kahwbwbana77ahwg', 'piquennadrakqma147aa'):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('ajagagahahavqgayag', 'jakamwnabagajuquaiw9'):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('aiqiqnabah181jq17', 'hahquw72j18qjq8q'):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('jahafw71816262baha5', 'jajwhqha618191gwgw6j'):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('jauwiw816w5wywhwbwgqu', 'jayayqiqkqbagauqj'):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('quqiaha8172baiq9', 'kauqiqnaba17q9qb'):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('riski_1504instagram', 'rizkyganz1504kahquah'):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('iakwajaahwggwhaa817oqja', 'facebookrizkyid111'):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('===bwjabase64ajaagja', 'baagbav-base64baf=='):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('mueheheheeh525y2qgqh', 'makanyajangangoblokxxx'):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('ahyauqhwha6w8qhagagi', 'aajaba7w52uabw8wh'):
        muat()
        print '\n       %s>>>>>   %sLICENSE OK    %s<<<<<' % (biru, hijau, biru)
        time.sleep(2)
        main()
    elif mana in ('A', 'a'):
        print
        chat = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mIsi pesan mu : ')
        chat.replace(' ', '%20')
        spin()
        sp.check_output(['am', 'start', 'https://api.whatsapp.com/send?phone=6288261764938&text=HASHER : ' + chat + ''])
        main()
    else:
        muat()
        print '\n     %s>>>>>%s License Wrong%s <<<<<' % (biru, merah, biru)
        time.sleep(2)
        pilih()


def enc(hash, tp, tipe):
    spin()
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    dat = {'mbutt': hash, 'ope': tp, 'submit': tipe}
    a = requests.post('http://tools-ixid.ga/enc-dec.php', headers={'User-Agent': '{acak}'}, data=dat)
    b = bs(a.content, 'html.parser')
    c = b.find_all('textarea')[1]
    d = c.text
    print '\n\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult : ' + d
    print
    raw_input('\n\x1b[32m     [ \x1b[31menter to back menu \x1b[32m] ')
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
    print '\n\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult : ' + d
    print
    raw_input('\n\x1b[32m     [ \x1b[31menter to back menu \x1b[32m] ')
    main()


def e1():
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print ''
    print tip
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
    print
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
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult MD2  : ', c.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult MD4  : ', d.text.replace(' ', '').replace('\n', '')
    print '\x1b[1;32m[\x1b[1;33m>\x1b[1;32m] \x1b[1;37mResult MD5  : ', e.text.replace(' ', '').replace('\n', '')
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
    raw_input('\n\x1b[32m     [ \x1b[31menter to back menu \x1b[32m] ')
    main()


if __name__ == '__main__':
    pilih()
