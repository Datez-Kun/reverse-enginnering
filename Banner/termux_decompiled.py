# uncompyle6 version 3.6.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
import os, sys, time
w = '\x1b[90;1m'
m = '\x1b[91;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
p = '\x1b[95;1m'
a = '\x1b[96;1m'
s = '\x1b[97;1m'

def iqbalz(x):
    w = {'w': 90, 'm': 31, 'h': 32, 'k': 33, 'b': 34, 'p': 35, 'a': 96, 's': 97}
    for i in w:
        x = x.replace('\r%s' % i, '\x1b[%s;1m' % w[i])

    x += '\x1b[0m'
    x = x.replace('\r0', '\x1b[0m')
    print x


def runntxt(lolz):
    for noobs in lolz:
        sys.stdout.write(noobs)
        sys.stdout.flush()
        time.sleep(10.0 / 100)


def banner():
    os.system('clear')
    os.system('cowsay -f eyes "Mr.XsZ" | lolcat')
    iqbalz('\rp          TOOLS EDIT TERMUX KEREN')
    print s + '+---------------------------------------------+'
    iqbalz('\ra|  Author:\rh Mr-XsZ')
    iqbalz('\ra|  Fb    :\rh https://www.facebook.com/2angga315')
    iqbalz('\ra|  github:\rh https://www.github.com/Mr-XsZ')
    print s + '|   +-----------------------------------------+'
    iqbalz('\rm|   | \rm[\rs1\rm]\rk  Ubah termux kamu sekarang          |')
    iqbalz('\rm|   | \rm[\rs2\rm]\rk  Cara Mengedit                      |')
    iqbalz('\rm|   | \rm[\rs3\rm]\rh  Install paketnya dulu bos....      |')
    print s + '+---+-----------------------------------------+'
    print m + '    4. Exit '


def main():
    banner()
    print a + ',~~~~~', h + '[', s + ' Pilih Opsinya ', h + ']'
    iqbalz_noobs = input("\x1b[96m'~~~~~>   ")
    if iqbalz_noobs == 1:
        pertama()
        runntxt(w + '...................')
        print ' '
        os.system('cowsay -f eyes "termux" | lolcat')
        os.system('toilet -f standard "termux" -F gay')
        runntxt(h + '         S u c c s e s s ...')
        print '  '
        runntxt(a + ' Silahkan buka jendela termux baru')
        print ' '
        print ' '
    elif iqbalz_noobs == 2:
        print w + 'sedang proses.......'
        time.sleep(1)
        noobs()
    elif iqbalz_noobs == 3:
        install()
    elif iqbalz_noobs == 4:
        keluar()
    else:
        main()


def pertama():
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('cp -f bash.bashrc $HOME/../usr/etc')
    os.system('clear')
    print w + 'sedang proses.....'


def install():
    os.system('pkg install ruby cowsay toilet figlet')
    os.system('gem install lolcat')
    main()


def keluar():
    sys.exit()


def noobs():
    print a + '\n  CARA EDIT SCRIPT BASH.BASHRC\n\x1b[97m\n\n   Ganti string yg bertuliskan \n"\x1b[91mtermux\x1b[97m" dengan nama kamu\natau dengan kata-kata lain yang kamu inginkan\njangan ubah string selain yg bertuliskan "\x1b[91mtermux\x1b[97m",\ndikhawatirkan program menjadi error...\njika sudah di edit, tinggal save dengan cara tekan \ntombol \x1b[95mCTRL + X + Y + ENTER                \n\x1b[90m\n                 Powered by: Mr.XsZ\n'
    lol = raw_input('\x1b[92;1m  E D I T  S E K A R A N G ?\x1b[91m  [ Y / N ]: ')
    if lol == 'y' or lol == 'Y':
        os.system('pkg install nano')
        os.system('nano bash.bashrc')
        main()
    else:
        main()


if __name__ == '__main__':
    main()