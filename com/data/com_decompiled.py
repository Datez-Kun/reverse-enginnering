# uncompyle6 version 3.6.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <Angga>
import re, os, bs4, sys, time, json, random, requests, subprocess
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'

class regis(object):

    def __init__(self):
        self.kent = 'https://sereware56.000webhostapp.com'
        self.checkSession()

    def akin(self):
        os.system('python2 .data/main.py')

    def checkSession(self):
        self.dt = '/data/data/com.termux/files/usr/lib/'
        if os.path.exists(self.dt):
            if os.path.exists('%s/com.txt' % self.dt):
                if os.path.getsize('%s/com.txt' % self.dt) != 0:
                    id = open('%s/com.txt' % self.dt).read().replace('\n', '')
                    self.id = json.loads(id)
                    try:
                        z = requests.get('%s/%s' % (self.kent,
                         'registered.txt')).text
                    except:
                        sys.exit(h + '[' + m + '!' + h + ']' + p + ' Check your internet connection ')

                    if len(re.findall(self.id['sessionID'], z)) != 0:
                        self.akin()
                    else:
                        try:
                            z = requests.get('%s/%s' % (self.kent,
                             'ip.txt')).text
                        except:
                            sys.exit(h + '[' + m + '!' + h + ']' + p + ' Check your internet connection ')

                        if len(re.findall(self.id['sessionID'], z)) != 0:
                            print h + '[' + m + '!' + h + ']' + p + ' Nama anda sudah diregistrasi'
                            print h + '[' + m + '!' + h + ']' + p + ' silahkan meminta konfirmasi Angga'
                            print h + '[' + k + '#' + h + ']' + p + ' Username Anda: %s' % self.id['username']
                            raw_input(h + '[' + k + '^' + h + ']' + p + ' tekan enter untuk menghubungi Angga via WhatsApp...')
                            subprocess.check_output([
                             'am', 'start',
                             'https://api.whatsapp.com/send?phone=6282211661007&text=konfirm%20saya%20dengan%20username:%20' + self.id['username'].replace(' ', '%20') + ''])
                        else:
                            self.generateSession()
                else:
                    self.generateSession()
            else:
                self.generateSession()
        else:
            os.mkdir(self.dt)
            self.generateSession()

    def generateSession(self):
        self.ab = list('abcdefghijklmnopqrstuvwxyz1234567890')
        self.gen = [
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper()]
        self.ok = ('').join(self.gen)
        self.p = requests.get('%s/%s' % (self.kent, 'ip.txt')).text
        if len(re.findall(self.ok, self.p)) != 0:
            print '[!] ID Exists: %s' % self.ok
            self.generateSession()
        else:
            self.username()

    def username(self):
        print h + '[' + k + '#' + h + ']' + p + ' Dark ID : %s' % self.ok
        print h + '[' + m + '*' + h + ']' + p + ' Membuat Nama'
        self.cre()

    def cre(self):
        self.user = raw_input(h + '[' + k + '?' + h + ']' + p + ' Nama Kamu: ')
        if self.user == '':
            self.cre()
        else:
            print requests.post('%s/new.php' % self.kent, data={'ip': self.ok, 'nama': '%s ----> Dark V.1.8' % self.user}).text
            f = json.dumps({'sessionID': self.ok, 'username': self.user})
            open('%s/com.txt' % self.dt, 'w').write(f)
            print h + '[' + k + '#' + h + ']' + p + ' silahkan meminta konfirmasi kepada Angga'
            raw_input(h + '[' + k + '^' + h + ']' + p + ' Tekan Enter Untuk Menghubungi Angga via WhatsApp...')
            subprocess.check_output([
             'am', 'start',
             'https://api.whatsapp.com/send?phone=6282211661007&text=konfirm%20saya%20dengan%20username:%20' + self.user.replace(' ', '%20') + ''])


if int(sys.version[0]) != 2:
    sys.stdout.write(h + '[' + m + '!' + h + ']' + p + "It's Python2 Script \n use python2 ")
    sys.exit()
elif __name__ == '__main__':
    regis()