# uncompyle6 version 3.6.2
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <NantaID>
import os, sys, string, random, time
preman = '    __  __\n   / / / /_  ______ ___  ____ _____\n  / /_/ / / / / __ `__ \\/ __ `/ __ \\\n / __  / /_/ / / / / / / /_/ / / / /\n/_/ /_/\\__,_/_/ /_/ /_/\\__,_/_/ /_/\n    ____                        __\n   / __ \\___  ____  ____  _____/ /_\n  / /_/ / _ \\/ __ \\/ __ \\/ ___/ __/\n / _, _/  __/ /_/ / /_/ / /  / /_\n/_/ |_|\\___/ .___/\\____/_/   \\__/\n          /_/\nAuthor  : Nanta ID / 4N71R\nSupport : TERMUXID3\n'
pahala = 0
dosa = 0
heav = ['Firdaus', 'Adn', "Na'iim", "Ma'wa", 'Darussalam', 'Daarul Muqoomah', 'Maqoomul Amiin', 'Khuldi']
baka = ['Huthamah', 'Hawiyah', 'Jahannam', 'Jahim', 'Saqar', "Sa'ir", 'Wail']
surga = random.choice(heav)
neraka = random.choice(baka)

def darah():
    os.system('clear')
    print preman
    print '[01]   Report'
    print '[02]   Pahala'
    print '[03]   Dosa'
    print '[00]   Exit'
    getih = raw_input('[human_report]> ')
    if getih == '':
        exit('Oops! Gagal Memakai!')
    elif getih in ('01', '1'):
        lapor()
    elif getih in ('02', '2'):
        baik()
    elif getih in ('03', '3'):
        buruk()
    elif getih in ('00', '0'):
        exit()
    else:
        exit('Oops! Pilihanmu tidak ada!')


def lapor():
    print ''
    target = raw_input('Masukkan nama : ')
    alam = raw_input('Surga/Neraka: ')
    if alam == '':
        exit('Jangan kosong!')
    elif alam in ('surga', 'Surga', 'SURGA'):
        alam = 'Surga'
    elif alam in ('neraka', 'Neraka', 'NERAKA'):
        alam = 'Neraka'
    print 'Berhasil mereport ' + target + ' ke ' + alam + '!'
    raw_input('Enter untuk kembali')
    darah()


def baik():
    global pahala
    print ''
    target = raw_input('Masukkan nama : ')
    nilai = raw_input('Masukkan pahala target: ')
    print 'Memilih Surga yang cocok...'
    time.sleep(1)
    print 'Sukses! Surga : ' + surga
    while True:
        pahala += 1
        sys.stdout.write('\rBerhasil mereport ' + target + ' dengan pahala : ' + str(pahala) + ', ke surga : ' + surga)
        sys.stdout.flush()
        time.sleep(0.01)
        if str(pahala) == nilai:
            print '\nSelesai!'
            break
            exit()


def buruk():
    global dosa
    print ''
    target = raw_input('Masukkan nama : ')
    nilai = raw_input('Masukkan dosa target: ')
    print 'Memilih Neraka yang cocok...'
    time.sleep(1)
    print 'Sukses! Neraka : ' + neraka
    while True:
        dosa += 1
        sys.stdout.write('\rBerhasil mereport ' + target + ' dengan dosa : ' + str(dosa) + ', ke neraka : ' + neraka)
        sys.stdout.flush()
        time.sleep(0.1)
        if str(pahala) == nilai:
            print '\nSelesai!'
            break
            exit()


if __name__ == '__main__':
    darah()