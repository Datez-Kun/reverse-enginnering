# Time Succses Parser : Sun Jun 14 21:33:53 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

import random, sys, time, os, getpass
angka = 0
reach = [56, 67, 78, 89, 100]

def fk(text, speed=0.01):
    for i in text + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(speed)


def bot_choice(angka):
    global reach
    for i in reach:
        if angka >= i:
            reach.remove(i)

    asu = reach[0] - angka
    if asu <= 10:
        return asu
    else:
        return random.randint(1, 10)


os.system('clear')
print 'Welcome To This Game\nYou can beat me if you smart enough\nSo,be prepared'
time.sleep(2)
print '\n\n'
fk('Cara Bermain')
fk('[1] . Ada sebuah angka yang berjumlah 0')
fk('[2] . Angka tersebut akan ditambahkan oleh pemain secara bergantian')
fk('[3] . Jika angka tersebut mencapai angka 100,Maka game berakhir')
fk('[4] . Pemain yang membuat angka tersebut menjadi 100 adalah pemenangnya')
fk('[5] . Jika pemain membuat angka tersebut lebih dari 100,Dia di anggap kalah')
fk('[6] . Pemain hanya boleh menambahkan angka dari 1 sampai 10')
print '\n\n'
while True:
    aska = raw_input('Sudah Mengerti? (y/n) : ').lower()
    if aska == 'n':
        fk('Jika cara bermainnya saja tidak mengerti,Berarti anda bodoh!')
        sys.exit()
    elif aska == 'y':
        fk('Get ready to lose :)')
        fk('Game is starting...')
        time.sleep(2)
        break
    else:
        fk('Jangan melanggar peraturan!')

gps = '[+] Press anything to continue'
os.system('clear')
kiminonawa = raw_input('Your name ? : ')
turn = random.choice([1, 2])
while angka < 100:
    while turn == 1:
        os.system('clear')
        print 'Bot-kun Turn'
        print ('Angka : {}').format(angka)
        jwb = bot_choice(angka)
        angka -= -jwb
        print ('BOT : {}').format(jwb)
        print ('Total Angka : {}\n\n').format(angka)
        turn = 2
        getpass.getpass(gps)
        break

    if angka >= 100:
        continue
    while turn == 2:
        os.system('clear')
        print ('{}-chan Turn').format(kiminonawa)
        print ('Angka : {}').format(angka)
        try:
            jwb = int(raw_input(('{}-chan : ').format(kiminonawa)))
        except:
            print 'Only number is allowed'
            continue

        if jwb > 10 or jwb < 1:
            print 'Only 1-10 is allowed'
            continue
        angka -= -jwb
        print ('Total Angka : {}\n\n').format(angka)
        turn = 1
        getpass.getpass(gps)

if angka > 100:
    if turn == 2:
        print ('{}-chan WIN :(').format(kiminonawa)
    elif turn == 1:
        print 'Bot-kun WIN :)'
if angka == 100:
    if turn == 1:
        print ('{}-chan WIN :(').format(kiminonawa)
    elif turn == 2:
        print 'Bot-kun WIN :)'
# okay decompiling meki.pyc
