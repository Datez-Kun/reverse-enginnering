# Python bytecode 2.7
try:
    import requests, os, json, sys, time, random
except:
    print '%s[%s!%s] %sModule belum terinstall' % (W1, R1, W1, W0)
    spin()
    os.system('pkg install wget;pip2 install requests')
    print '%s[%s!%s] %sInstalasi selesai' % (W1, R1, W1, W0)
    print '%s[%s!%s] %sRun again' % (W1, R1, W1, W0)
    print '%s[%s!%s] %spython2 darkquote.py' % (W1, R1, W1, W0)

G0 = '\x1b[0;32m'
G1 = '\x1b[1;32m'
C0 = '\x1b[0;36m'
C1 = '\x1b[1;36m'
P0 = '\x1b[0;35m'
P1 = '\x1b[1;35m'
W0 = '\x1b[0;37m'
W1 = '\x1b[1;37m'
B0 = '\x1b[0;34m'
B1 = '\x1b[1;34m'
R0 = '\x1b[0;31m'
R1 = '\x1b[1;31m'
Y1 = '\x1b[1;33m'
Y0 = '\x1b[0;33m'
BG = '\x1b[1;97;41m'
RE = '\x1b[0m'
r = '\x1b[91m'
c = '\x1b[96m'
w = '\x1b[0m'

def wait(t):
    for x in range(t):
        t -= 1
        sys.stdout.write('\r' + '\x1b[1;37m[\x1b[1;31m!\x1b[1;37m]\x1b[0;37m Tunggu ' + str(t) + 's')
        sys.stdout.flush()
        time.sleep(1)


def spin():
    try:
        L = '\\|/-'
        for q in range(10):
            time.sleep(0.1)
            sys.stdout.write('\r\x1b[1;32m[\x1b[1;33m' + L[(q % len(L))] + '\x1b[1;32m]\x1b[0;37m Loading please wait...')
            sys.stdout.flush()

    except:
        exit()


def ketik(teks):
    for i in teks + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.001)


def load(word):
    lix = ['/', '-', '\xe2\x95\xb2', '|']
    for i in range(6):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.2)
            sys.stdout.flush()


def metu():
    print '%s[%sx%s] %sExiting Program' % (W1, R1, W1, R0)
    exit(1)


def koneksi():
    logo()
    try:
        rq = requests.get('http://github.com')
        spin()
        print '\n%s[%s#%s] %sKoneksi bagus' % (G1, Y1, G1, W0)
        time.sleep(2)
    except requests.exceptions.ConnectionError:
        print '%s[%sx%s] %sTidak ada koneksi' % (W1, R1, W1, W0)
        time.sleep(1)
        metu()


def logo():
    os.system('clear')
    ketik("\n %s_____             %s_          %s_____%s         _\n%s|     |%s___ ___ ___| |_ ___   %s|     |%s_ _ ___| |_ ___ ___\n%s|   --|%s  _| -_| .'|  _| -_|  %s|  |  |%s | | . |  _| -_|_ -|\n%s|_____|%s_| |___|__,|_| |___|  %s|__  _|%s___|___|_| |___|___|\n                                %s|__|  %sthx to azisek\n" % (G1, W1, G1, W1, G1, W1, G1, W1, G1, W1, G1, W1, G1, W1, G1, W1, G1, W1))


def main():
    os.system('termux-setup-storage;git pull')
    try:
        logo()
        quote = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mQuote : ')
        if quote == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            main()
        name = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[1;37mName : ')
        if name == '':
            print '%s[%s!%s] %sJangan kosong' % (G1, R1, G1, W0)
            time.sleep(0.8)
            main()
        r = requests.Session()
        agent = r.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
        acak = random.choice(agent)
        hd = {'User-Agent': '{acak}'}
        a = r.get('http://apimybot.000webhostapp.com/quote/?quote=' + quote + '&name=' + name + '&bg=random', headers=hd).text
        b = json.loads(a)
        c = b['image']
        d = c.replace('https://apimybot.000webhostapp.com/quote/', '')
        e = r.get('%s' % c)
        f = '%s' % d
        spin()
        with open(f, 'wb') as (code):
            code.write(e.content)
        os.system('mv %s /sdcard' % f)
        print '%s[%s#%s] %sDownload selesai' % (G1, Y1, G1, W1)
        print '%s[%s#%s] %sSilahkan cek penyimpanan internal anda' % (G1, Y1, G1, W1)
        print '%s[%s#%s] %sTerima kasih bro :)' % (G1, Y1, G1, W1)
        exit()
    except requests.exceptions.ConnectionError:
        print '%s[%sx%s] %sTidak ada koneksi' % (W1, R1, W1, W0)
        time.sleep(1)
        metu()


if __name__ == '__main__':
    koneksi()
    main()

# Decompiled At : Wed Apr  1 13:32:00 2020 
