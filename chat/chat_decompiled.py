# uncompyle6 version 3.6.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <Angga>
import os, sys, time
myroom = 'svrsc.xyz/chat/'
logo = '\n\x1b[1;91m\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\x1b[1;97m\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80   \x1b[1;91m\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\x1b[1;97m\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\n \x1b[1;91m\xe2\x95\x91\xe2\x95\x91\x1b[1;97m\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;91m\xe2\x95\xa0\xe2\x95\xa6\xe2\x95\x9d\x1b[1;97m\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\n\x1b[1;91m\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\x1b[1;97m\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4   \x1b[1;91m\xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\x1b[1;97m\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4\n\x1b[1;93m* \x1b[1;97mAuthor  \x1b[1;91m: \x1b[1;96mAngga\x1b[1;97m\n\x1b[1;93m* \x1b[1;97mGitHub  \x1b[1;91m: \x1b[1;92m\x1b[4mhttp://github.com/Mr-XsZ\x1b[0m'

def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mSedang Masuk \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


bergabung = ' \x1b[1;96mBergabung\x1b[1;97m...'

def main():
    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m1. \x1b[1;97mRoom Publik'
    print '\x1b[1;91m2. \x1b[1;97mJoin Room Request'
    print '\x1b[1;91m3. \x1b[1;97mBuat Room'
    print '\x1b[1;91m0. Keluar'
    print
    asu = raw_input('\x1b[1;91m-#\x1b[1;97m ')
    if asu == '1':
        room()
    elif asu == '2':
        send()
    elif asu == '3':
        buat()
    elif asu == '0':
        keluar()
    else:
        keluar()


def room():
    global name
    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    name = raw_input('\x1b[1;91m[+] \x1b[1;92mNama anda \x1b[1;91m:\x1b[1;97m ')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[+] \x1b[1;92mSelamat datang \x1b[1;97m' + name
    tik()
    print '\n\x1b[1;91m[+] \x1b[1;97m' + name + ' \x1b[1;96mBergabung\x1b[1;97m ...'
    zedd = open('config', 'w')
    raw_input('\n\x1b[1;91m[ \x1b[1;97mENTER \x1b[1;91m]')
    zedd.write('\x1b[1;97m' + name + bergabung + '\n')
    zedd.close()
    os.system('curl -X POST -F x=@config http://' + myroom + '/server.php')
    get()


def get():
    os.system('clear')
    os.system('curl http://' + myroom)
    zedd = open('config', 'w')
    pesan = raw_input("\n\x1b[1;91mKetik \x1b[1;97m'zexit' \x1b[1;91mUntuk keluar\x1b[1;97m...\n" + 40 * '\x1b[1;97m\xe2\x95\x90' + '\n\x1b[1;97mSend \x1b[1;91m:\x1b[1;97m ')
    if pesan == 'zexit':
        main()
    zedd.write('\x1b[1;92m[\x1b[1;97m' + name + '\x1b[1;92m] =>\x1b[1;97m ' + pesan + '\n')
    zedd.close()
    os.system('curl -X POST -F x=@config http://' + myroom + '/server.php')
    get()


def send():
    global name
    global server
    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    server = raw_input('\x1b[1;91m[+] \x1b[1;92mAlamat Server \x1b[1;91m=>\x1b[1;97mhttp://')
    name = raw_input('\x1b[1;91m[+] \x1b[1;92mNama anda \x1b[1;91m:\x1b[1;97m ')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[+] \x1b[1;92mSelamat datang \x1b[1;97m' + name
    tik()
    print '\n\x1b[1;91m[+] \x1b[1;97m' + name + ' \x1b[1;96mBergabung\x1b[1;97m ...'
    zedd = open('config', 'w')
    raw_input('\n\x1b[1;91m[ \x1b[1;97mENTER \x1b[1;91m]')
    zedd.write('\x1b[1;97m' + name + bergabung + '\n')
    zedd.close()
    os.system('curl -X POST -F x=@config http://' + server + '/server.php')
    next()


def next():
    os.system('clear')
    os.system('curl http://' + server)
    zedd = open('config', 'w')
    pesan = raw_input("\n\x1b[1;91mKetik \x1b[1;97m'Zexit' \x1b[1;91mUntuk keluar\x1b[1;97m...\n" + 40 * '\x1b[1;97m\xe2\x95\x90' + '\n\x1b[1;97mSend \x1b[1;91m:\x1b[1;97m ')
    if pesan == 'Zexit':
        main()
    zedd.write('\x1b[1;92m[\x1b[1;97m' + name + '\x1b[1;92m] =>\x1b[1;97m ' + pesan + '\n')
    zedd.close()
    os.system('curl -X POST -F x=@config http://' + server + '/server.php')
    next()


def buat():
    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;92mindex.php'
    print '\x1b[1;97m<?php $x=file_get_contents("config");echo $x;?>'
    print
    print '\x1b[1;92mserver.php'
    print '\x1b[1;97m<?php $date=date("d/m/Y");if(file_exists($_FILES["x"]["name"])){$x=file_get_contents($_FILES["x"]["tmp_name"]);$fh=fopen("config","a");fwrite($fh,"[$date] $x");fclose($fh);}else{@copy($_FILES["x"]["tmp_name"],$_FILES["x"]["name"]);}?>'
    print
    print '\x1b[1;91m[!] \x1b[1;92mUnggah file ini ke server website anda'
    done = raw_input('\x1b[1;91m[?] \x1b[1;92mSudah/Belum\x1b[1;97m [s/b]\x1b[1;91m: \x1b[1;97m')
    if done == '':
        keluar()
    elif done == 's':
        send()
    elif done == 'S':
        send()
    elif done == 'b':
        main()
    elif done == 'B':
        main()
    else:
        keluar()


main()