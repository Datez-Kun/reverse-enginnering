import requests as r, random, os, time
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

def gen(tipe, list):
    jml = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[0;37mJumlah > ')
    agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
    acak = random.choice(agent)
    a = r.post('https://nabil.my.id/Tools/Other-Tools/Email-Random-Generator/apiv1.php', headers={'user-agent': '{acak}'}, data={'tipe': tipe, 'symbol': '_', 'jumlah': jml, 'listnama': list}, cookies={'PHPSESSID': '57834435742510a801a31b4c5909f0ae'})
    if '<!DOCTYPE HTML>' in a.text:
        print '%s[%s!%s] %sAnda tidak beruntung cok :v Web ada cloudflare\n%s[%s!%s] %sCoba lagi nanti' % (W1, R1, W1, W0, W1, R1, W1, W0)
        exit()
    print '%s[%s>%s] %sResult: ' % (G1, Y1, G1, W0)
    print
    print a.text
    print '%s[%s>%s] %sHasil tersimpan di hasil.txt' % (G1, Y1, G1, W0)
    open('hasil.txt', 'a+').write(a.text + '\n')


def main():
    os.system('git pull;clear')
    print '%s\n\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84 .       \xe2\x96\x84\xe2\x96\x84 \xe2\x80\xa2 \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84 . \xe2\x96\x90 \xe2\x96\x84\n\xe2\x96\x80\xe2\x96\x84.\xe2\x96\x80\xc2\xb7      \xe2\x96\x90\xe2\x96\x88 \xe2\x96\x80 \xe2\x96\xaa\xe2\x96\x80\xe2\x96\x84.\xe2\x96\x80\xc2\xb7\xe2\x80\xa2\xe2\x96\x88\xe2\x96\x8c\xe2\x96\x90\xe2\x96\x88\n\xe2\x96\x90\xe2\x96\x80\xe2\x96\x80\xe2\x96\xaa\xe2\x96\x84      \xe2\x96\x84\xe2\x96\x88 \xe2\x96\x80\xe2\x96\x88\xe2\x96\x84\xe2\x96\x90\xe2\x96\x80\xe2\x96\x80\xe2\x96\xaa\xe2\x96\x84\xe2\x96\x90\xe2\x96\x88\xe2\x96\x90\xe2\x96\x90\xe2\x96\x8c\n\xe2\x96\x90\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x8cmail  \xe2\x96\x90\xe2\x96\x88\xe2\x96\x84\xe2\x96\xaa\xe2\x96\x90\xe2\x96\x88\xe2\x96\x90\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x8c\xe2\x96\x88\xe2\x96\x88\xe2\x96\x90\xe2\x96\x88\xe2\x96\x8c\n \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80       \xc2\xb7\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80  \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80 \xe2\x96\x88\xe2\x96\xaa\n' % G1
    print '%s[%s>%s] %sPowered by https://nabil.my.id\n%s[%s>%s] %sAuthor D4RKSH4D0WS\n\n   %s{%s01%s} %sGmail    [indonesia]\n   %s{%s02%s} %sYahoo    [indonesia]\n   %s{%s03%s} %sHotmail  [indonesia]\n   %s{%s04%s} %sGmail    [campuran]\n   %s{%s05%s} %sYahoo    [campuran]\n   %s{%s06%s} %sHotmail  [campuran]\n   %s{%s07%s} %sReport   (Whatsapp)\n   %s{%s00%s} %sExit\n' % (G1, Y1, G1, W0, G1, Y1, G1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, G1, W1, W0, W1, R1, W1, R0)
    chc = raw_input('\x1b[1;32m[\x1b[1;33m?\x1b[1;32m] \x1b[0;37mPilih > ')
    if chc == '':
        print '[!] Input yg bener cok'
        time.sleep(0.8)
        main()
    else:
        if chc == '1' or chc == '01':
            tipe = 'gmail.com'
            list = 'indonesia'
            gen(tipe, list)
        else:
            if chc == '2' or chc == '02':
                tipe = 'yahoo.com'
                list = 'indonesia'
                gen(tipe, list)
            else:
                if chc == '3' or chc == '03':
                    tipe = 'hotmail.com'
                    list = 'indonesia'
                    gen(tipe, list)
                else:
                    if chc == '4' or chc == '04':
                        tipe = 'gmail.com'
                        list = 'campuran'
                        gen(tipe, list)
                    else:
                        if chc == '5' or chc == '05':
                            tipe = 'yahoo.com'
                            list = 'campuran'
                            gen(tipe, list)
                        else:
                            if chc == '6' or chc == '06':
                                tipe = 'hotmail.com'
                                list = 'campuran'
                                gen(tipe, list)
                            else:
                                if chc == '7' or chc == '07':
                                    print
                                    chat = raw_input('\x1b[1;32m[\x1b[1;33m#\x1b[1;32m] \x1b[0;37mIsi pesan mu : ')
                                    chat.replace(' ', '%20')
                                    sp.check_output(['am', 'start', 'https://api.whatsapp.com/send?phone=628996604524&text=Report : ' + chat + ''])
                                    exit()
                                else:
                                    if chc == '0' or chc == '00':
                                        exit('Bye')
                                    else:
                                        exit('Bye goblok !')


if __name__ == '__main__':
    main()
