# uncompyle6 version 3.6.2
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <default>
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
web = mechanize.Browser()
web.set_handle_robots(False)
web.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
web.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>')]
norm = '\x1b[0;39m'
info = ' \x1b[1;91m[\x1b[1;92mi\x1b[1;91m]\x1b[1;93mNFO PROFILE ' + norm
infonet = ' \x1b[1;91m[\x1b[1;92mi\x1b[1;91m]\x1b[1;93mNFO ERROR ' + norm
logo = '\n\x1b[1;92m \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xac\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xac\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xac\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xac\xe2\x94\x80\xe2\x94\xac\xe2\x94\x80\xe2\x94\xac\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90 \x1b[1;95m \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x90 \n\x1b[1;92m \xe2\x94\x82   \xe2\x96\x81   \xe2\x94\x82 \xe2\x94\x80\xe2\x94\x80\xe2\x94\xa4 \xe2\x94\x80\xe2\x94\x80\xe2\x94\xa4 \xe2\x94\x80 \xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82   \xe2\x94\x82 \xe2\x94\x94\xe2\x94\x90 \x1b[1;95m\xe2\x94\x82 \x1b[0;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \x1b[1;95m\xe2\x94\x82 \n\x1b[1;92m \xe2\x94\x82\x1b[1;91m.  \x1b[1;92m\xe2\x96\x89   \xe2\x94\x9c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xb4\xe2\x94\x80\xe2\x94\xac\xe2\x94\x80\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xb4\xe2\x94\x80\xe2\x94\xb4\xe2\x94\x80\xe2\x94\xa4 \xe2\x94\x80\xe2\x94\xa4 \x1b[1;95m\xe2\x94\x82 \x1b[0;39m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \x1b[1;95m\xe2\x94\x82 \n\x1b[1;92m \xe2\x94\x82\x1b[1;91m. \x1b[1;92m \xe2\x96\x81   \xe2\x94\x82     \xe2\x94\x94[\x1b[1;91mF\xca\x99\x1b[1;93mC\xca\x9c\xe1\xb4\x87\xe1\xb4\x84\xe1\xb4\x8b\xe1\xb4\x87\xca\x80\x1b[1;92m]\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98 \x1b[1;95m\xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98\n\x1b[1;92m \xe2\x94\x82\x1b[1;91m\xe2\x94\x82 \x1b[1;92m \xe2\x94\x82   \xe2\x94\x9c\xe2\x94\x80\x1b[1;93m\xe2\x96\xb6 \x1b[0;39mN\xe1\xb4\x8f LOGGER\x1b[1;91m,\x1b[0;39m U\xea\x9c\xb1\xe1\xb4\x87\xca\x80 A\xc9\xa2\xe1\xb4\x87\xc9\xb4\xe1\xb4\x9b C\xca\x9c\xca\x80\xe1\xb4\x8f\xe1\xb4\x8d\xe1\xb4\x87\x1b[1;91m,\x1b[0;39m P\xc9\xaa\xe1\xb4\x84\xe1\xb4\x8b T\xe1\xb4\x8f\xe1\xb4\x8b\xe1\xb4\x87\xc9\xb4\n\x1b[1;92m \xe2\x94\x82\x1b[1;91m\xe2\x94\x82\xe2\x94\x82.\x1b[1;92m\xe2\x94\x82\x1b[1;91m\xe2\x94\x82. \x1b[1;92m\xe2\x94\x9c\xe2\x94\x80\x1b[1;93m\xe2\x96\xb6 \x1b[0;39mAuthor \x1b[1;91m:  \x1b[1;93mR3DB0T \x1b[1;97m|\x1b[1;96m./Termux Coding Indonesia\n\x1b[1;92m \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xb4\xe2\x94\x80\x1b[1;93m\xe2\x96\xb6 \x1b[0;39mGithub \x1b[1;91m:  \x1b[1;92m\x1b[4mhttps://github.com/R3DB0T\x1b[0m\x1b[0;39m\n '

def dots():
    thed = [
     '.   ', '..  ', '... ']
    for o in thed:
        print '\r\x1b[1;91m\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mLogin ' + norm + o,
        sys.stdout.flush()
        time.sleep(1)


def tolol(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0001)


def nope(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def out():
    os.sys.exit()


def mainmenu():
    os.system('clear')
    try:
        loginshow = open('.token', 'r').read()
        print logo
        os.system('clear')
        print logo
        print ('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;93mToken still active \x1b[1;95m[\x1b[1;91m\xe2\x97\x80\x1b[1;95m]').center(115)
        time.sleep(1.5)
        os.system('clear')
        print logo
        print info.center(90)
        print 55 * '\xe2\x95\x90'
        bug = requests.get('https://graph.facebook.com/me?access_token=' + loginshow)
        a = json.loads(bug.text)
        name = a['name']
        id = a['id']
        follow = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + loginshow)
        fol = json.loads(follow.text)
        follower = str(fol['summary']['total_count'])
        tolol('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mName      \x1b[1;96m: ' + norm + name)
        tolol('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mID        \x1b[1;96m: ' + norm + id)
        tolol('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mFollowers \x1b[1;96m: ' + norm + follower)
        tolol('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mStatus    \x1b[1;96m: \x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mACTIVE')
        tolol('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mToken     \x1b[1;96m: ' + norm + loginshow)
        print 55 * '\xe2\x95\x90'
        nope('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mTools by\x1b[4;91m R\x1b[4;93m3D\x1b[4;92mB\x1b[4;94m0\x1b[4;95mT ' + norm)
        nope('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mDont Forget to check my Instagram')
        nope('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mhttps://instagram.com/redbot.termux' + norm)
        out()
    except (KeyError, IOError):
        try:
            os.system('clear')
            print logo
            print ('\x1b[1;96m\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;91mToken not found \x1b[1;95m[\x1b[1;91m\xe2\x97\x80\x1b[1;95m]').center(115)
            time.sleep(1.5)
            os.system('clear')
            print logo
            print '\x1b[1;91m\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mLogin Your Facebook Account \x1b[1;95m[\x1b[1;91m\xe2\x97\x80\x1b[1;95m]' + norm
            id = raw_input('\x1b[1;91m\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;36mID\x1b[1;97m/\x1b[1;96mEmail\x1b[1;97m \x1b[1;91m:\x1b[1;92m ')
            password = getpass.getpass('\x1b[1;91m\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
            dots()
        except (KeyboardInterrupt, UnboundLocalError):
            print '\x1b[1;91m\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;91mInterrupt' + norm

        try:
            web.open('https://m.facebook.com')
        except mechanize.URLError:
            print infonet.center(95)
            print 55 * '\xe2\x95\x90'
            print '\x1b[1;91m\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;91mNo Internet Active' + norm
            out()

        web._factory.is_html = True
        web.select_form(nr=0)
        web.form['email'] = id
        web.form['pass'] = password
        web.submit()
        url = web.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + password + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': password, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                oauth = open('.token', 'w')
                oauth.write(z['access_token'])
                oauth.close()
                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin successfully'
                os.system('am start https://www.instagram.com/redbot.termux > /dev/null')
                time.sleep(1.5)
                os.system('clear')
                print logo
                print ('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;93mToken still active \x1b[1;95m[\x1b[1;91m\xe2\x97\x80\x1b[1;95m]').center(115)
                time.sleep(1.5)
                os.system('clear')
                print logo
                print info.center(90)
                print 55 * '\xe2\x95\x90'
                loginshow = open('.token', 'r').read()
                bug = requests.get('https://graph.facebook.com/me?access_token=' + loginshow)
                a = json.loads(bug.text)
                name = a['name']
                id = a['id']
                follow = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + loginshow)
                fol = json.loads(follow.text)
                follower = str(fol['summary']['total_count'])
                tolol('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mName      \x1b[1;96m: ' + norm + name)
                tolol('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mID        \x1b[1;96m: ' + norm + id)
                tolol('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mFollowers \x1b[1;96m: ' + norm + follower)
                tolol('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mStatus    \x1b[1;96m: \x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mACTIVE')
                tolol('\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mToken     \x1b[1;96m: ' + norm + loginshow + '\n')
                out()
            except requests.exceptions.ConnectionError:
                print infonet.center(95)
                print 55 * '\xe2\x95\x90'
                print '\x1b[1;91m\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;91mNo Internet Active' + norm
                out()

        if 'checkpoint' in url:
            os.system('clear')
            print logo
            print ('\x1b[1;96m\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;91mToken has Expired/Account Checkpoint \x1b[1;95m[\x1b[1;91m\xe2\x97\x80\x1b[1;95m]').center(115)
            time.sleep(1.5)
            os.system('clear')
            print logo
            print info.center(90)
            print 55 * '\xe2\x95\x90'
            print '\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mName      \x1b[1;96m: \x1b[1;91m\x1b[1;91mnull'
            print '\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mID        \x1b[1;96m: \x1b[1;91mnull'
            print '\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mFollowers \x1b[1;96m: \x1b[1;91mnull'
            print '\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mStatus    \x1b[1;96m: \x1b[1;91m[\x1b[1;93m\xc3\x97\x1b[1;91m] \x1b[1;93mCHECKPOINT'
            print '\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] \x1b[1;92mToken     \x1b[1;96m: \x1b[1;91mnull'
            os.system('rm -rf .token')
            raw_input('\x1b[1;91m\x1b[1;95m[\x1b[1;91m\xe2\x96\xb6\x1b[1;95m] Enter to exit' + norm)
        else:
            print '\n\x1b[1;91m[!] \x1b[1;93mLogin Failed'
            os.system('rm -rf .token')
            time.sleep(1)
            mainmenu()


mainmenu()