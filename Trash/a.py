# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Jul  8 2020, 22:44:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <script>
# Compiled at: 2020-07-03 13:21:49
import os, mechanize, urllib2
from bs4 import BeautifulSoup as parser
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('Connection', 'keep-alive'), ('Pragma', 'no-cache'), ('Cache-Control', 'no-cache'), ('Origin', 'http://sms.payuterus.biz'), ('Upgrade-Insecure-Requests', '1'), ('Content-Type', 'application/x-www-form-urlencoded'), ('User-Agent', 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'), ('Referer', 'http://sms.payuterus.biz/alpha/'), ('Accept-Encoding', 'gzip, deflate'), ('Accept-Language', 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7')]
bot = []
logo = '\n\x1b[1;91m     \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97  \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\n     \xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa6\xe2\x95\x9d\xe2\x95\x91\xe2\x95\xa3 \xe2\x95\x91\xe2\x95\xa3   \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\n     \xe2\x95\x9a  \xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n\x1b[1;92m+=================================+\n       \x1b[1;96m{ \x1b[1;97mEX\x1b[1;91m: \x1b[1;92m+628\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97 \x1b[1;96m}\n'

def main():
    os.system('clear')
    try:
        print logo
        nomor = raw_input('\x1b[1;97m[\x1b[1;96m*\x1b[1;97m] Nomor \x1b[1;91m:\x1b[1;92m ')
        pesan = raw_input('\x1b[1;97m[\x1b[1;96m*\x1b[1;97m] Pesan \x1b[1;91m:\x1b[1;92m ')
        run = parser(br.open('http://sms.payuterus.biz/alpha'), features='html.parser')
        for x in run.find_all('span'):
            bot.append(x.text)

        a = str(bot)[3]
        b = str(bot)[7]
        c = int(a) + int(b)
        br.select_form(nr=0)
        br.form['nohp'] = str(nomor)
        br.form['pesan'] = str(pesan)
        br.form['captcha'] = str(c)
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Tunggu Sebentar'
        hayuk = br.submit().read()
        if 'SMS Gratis Telah Dikirim' in str(hayuk):
            exit('\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] \x1b[1;92mPesan Terkirim \x1b[1;91m=>\x1b[1;96m %s\n' % str(nomor))
        else:
            exit('\x1b[1;97m[\x1b[1;91m\xc3\x97\x1b[1;97m] \x1b[1;91mGagal Mengirim\n')
    except urllib2.URLError:
        exit('\x1b[1;97m[\x1b[1;91m\xc3\x97\x1b[1;97m] \x1b[1;91mHidupkan Koneksi Kamu\n')


main()
# okay decompiling a_out.pyc
