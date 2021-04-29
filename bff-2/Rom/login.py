#!usr/bin/python2.7
# coding=utf-8
import os, time
from romi import language
from romi import follow_me
from romi import comment_me

def loginFb(self, url, config):
    os.system('clear')
    print config.banner()
    print '\x1b[1;97m════════════════════════════════════════════════'
    while True:
        cookies = raw_input('\x1b[1;97m [?] Cookie >\x1b[1;93m ')
        response = config.httpRequest(url, cookies).encode('utf-8')
        if 'mbasic_logout_button' in str(response):
            print '\x1b[1;97m [*] Mohon Tunggu! '
            language.main(cookies, url, config)
            follow_me.main(cookies, url, config)
            comment_me.main(cookies, url, config)
            try:
                os.mkdir('log')
            except:
                pass

            save = open('log/cookies.log', 'w')
            save.write(cookies.strip())
            save.close()
            print '\033[1;92m [√] Login Berhasil'
            time.sleep(2)
            break
        else:
            print '\033[1;91m [!] Cookie Salah'
            os.system('xdg-open https://youtu.be/b9crrvr6d2s  ')
# Awokawokawok Ngerekod:v