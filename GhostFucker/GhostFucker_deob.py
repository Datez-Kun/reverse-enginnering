# Source generated with python 2.7
# Decompile at : Mon Apr  6 14:44:25 WIB 2020

import threading
from multiprocessing.dummy import Pool
import os, sys, time
from bs4 import BeautifulSoup
from platform import system
import random, datetime, cookielib, os, re
from colorama import Fore
from colorama import Style
from colorama import init
import requests, re, os, base64, urllib, httplib, urllib2
from multiprocessing.dummy import Pool as ThreadPool
try:
    os.system('clear||cls')
except:
    pass

def banner_logo():
    print "\x1b[1;95m\n   _____ _               _     ______          _             \n  / ____| |  \x1b[1;97mBCA \x1b[1;95m/ \x1b[1;97m7GT  \x1b[1;95m| |   |  ____|        | |            \n | |  __| |__   ___  ___| |_  | |__ _   _  ___| | _____ _ __ \n | | |_ | '_ \\ / _ \\/ __| __| |  __| | | |/ __| |/ / _ \\ '__|\n | |__| | | | | (_) \\__ \\ |_  | |  | |_| | (__|   <  __/ |   \n  \\_____|_| |_|\\___/|___/\\__| |_|   \\__,_|\\___|_|\\_\\___|_|   \n\x1b[1;97m\n     GHOST FUCKER BING DORKERS WITH 1337 CODERS BY JHON\n            \x1b[1;95m-- \x1b[1;97mPRIVATE7 CODE AND PRIVATE7 BOT \x1b[1;95m--\n\x1b[1;97m"


banner_logo()
now = datetime.datetime.now()
print '           \x1b[1;95mSTARTED AT: ' + str(now)
print '\x1b[1;95m\n  SELECT MENU:\n  \x1b[1;95m[\x1b[1;97m1\x1b[1;95m] \x1b[1;97mBING DORKER FROM DORKLIST\n  \x1b[1;95m[\x1b[1;97m2\x1b[1;95m] \x1b[1;97mBING GRABBER FROM IPLIST\n  \x1b[1;95m[\x1b[1;97m3\x1b[1;95m] \x1b[1;97mRANGE IP FROM IPLIST\n'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0'}
ghost = raw_input('   \x1b[1;97mSELECT NUMBER \x1b[1;95m> \x1b[1;97m')
if str(os.path.exists('result')) == 'False':
    os.system('mkdir result')
if ghost == '1' or ghost == '01':
    dorks = raw_input('\n   \x1b[1;97mYOUR HELL DORK LIST \x1b[1;95m> \x1b[1;97m')
    os.system('clear||cls')
    banner_logo()
    print ' '
    dorks = open(dorks, 'r')
    for fucker in dorks:
        ch = []
        page = 1
        while page < 2000:
            bing = 'http://www.bing.com/search?q=' + fucker + '+&count=50&first=' + str(page)
            select = requests.get(bing, verify=False, headers=headers)
            fwd = select.content
            doork = re.findall('<h2><a href="(.*?)"', fwd)
            for i in doork:
                o = i.split('/')
                if o[0] + '//' + o[2] in ch:
                    print '\n \x1b[1;95m[\x1b[1;92m+\x1b[1;95m] \x1b[1;97mDORK \x1b[1;95m->\x1b[1;97m', fucker
                else:
                    ch.append(o[0] + '//' + o[2])
                    print ' \x1b[1;92m', o[0] + '//' + o[2]
                    with open('result/1bing_dorker.txt', 'a') as (s):
                        s.writelines(o[0] + '//' + o[2] + '\n')

            page = page + 50

if ghost == '2' or ghost == '02':
    ips = raw_input('\n   \x1b[1;97mYOUR HELL IP LIST \x1b[1;95m> \x1b[1;97m')
    os.system('clear||cls')
    banner_logo()
    print ' '
    ips = open(ips, 'r')
    for fucker in ips:
        ch = []
        page = 1
        while page < 2000:
            bing = 'http://www.bing.com/search?q=' + fucker + '+&count=50&first=' + str(page)
            select = requests.get(bing, verify=False, headers=headers)
            fwd = select.content
            ip = re.findall('<h2><a href="(.*?)"', fwd)
            for i in ip:
                o = i.split('/')
                if o[0] + '//' + o[2] in ch:
                    print '\n \x1b[1;95m[\x1b[1;92m+\x1b[1;95m] \x1b[1;97mIPs \x1b[1;95m->\x1b[1;97m', fucker
                else:
                    ch.append(o[0] + '//' + o[2])
                    print ' \x1b[1;92m', o[0] + '//' + o[2]
                    with open('result/2bing_grabber.txt', 'a') as (s):
                        s.writelines(o[0] + '//' + o[2] + '\n')

            page = page + 50

if ghost == '3' or ghost == '03':
    ips = raw_input('\n   \x1b[1;97mYOUR HELL IP LIST TO RANGE \x1b[1;95m> \x1b[1;97m')
    ips = open(ips, 'r')
    for site in ips:
        ur = site.rstrip()
        ch = site.split('\n')[0].split('.')
        ip1 = ch[0]
        ip2 = ch[1]
        fucker = str(ip1) + '.' + str(ip2) + '.'
        i = 0
        while i <= 255:
            i += 1
            c = 0

        while c <= 255:
            c += 1
            print '\n \x1b[1;95m[\x1b[1;92m+\x1b[1;95m] \x1b[1;97mIP RANGE \x1b[1;95m-> \x1b[1;97m' + str(fucker) + str(c) + '.' + str(i)
            open('result/3range_ip.txt', 'a').write(str(fucker) + str(c) + '.' + str(i) + '\n')
