#Decompiled At:Thu Mar 12 20:18:42 2020 

import re, os, sys, json, bs4, time, urllib, random, requests, subprocess, requests, sys, hashlib, json, banner
from data.color import *

class tokenz:

    def __init__(self):
        self.count = 0
        self.menu()

    def back(self):
        raw_input('press enter to menu...')
        banner.header()

    def menu(self):
        print '\n\t[ Select Action ]\n'
        print '  {%s01%s} Generate Single Access Token' % (G, N)
        print '  {%s02%s} Generate Mass Access Token' % (G, N)
        print '  {%s03%s} Back To Menu Option\n' % (R, N)
        self.choice()

    def choice(self):
        c = raw_input('%s[%s*%s]%s Actions>> ' % (G, R, G, N))
        if c == '1' or c == '01':
            e = raw_input('%s[?]%s Email: ' % (G, N))
            p = raw_input('%s[?]%s Passs: ' % (G, N))
            f = self.create('%s|%s' % (e, p))
            if f is None:
                print '%s[!]%s Failed.' % (R, N)
                self.back()
            print '%s[*]%s Success..' % (G, N)
            self.sing(f)
        elif c == '2' or c == '02':
            self.a()
        elif c == '3' or c == '03':
            self.back()
        else:
            print '%s[!]%s invalid options.' % (R, N)
            self.choice()
        return

    def a(self):
        try:
            self.s = open(raw_input('%s[?]%s account list: ' % (
             G, N))).read().splitlines()
        except Exception as e:
            print '%s[!]%s %s' % (R, N, e)
            self.a()

        self.lst()

    def lst(self):
        try:
            self.f = raw_input('%s[?]%s result filename: ' % (G, N))
            open(self.f, 'w').close()
        except Exception as e:
            print '%s[!]%s %s' % (R, N, e)
            self.lst()

        print '%s[*]%s Output: %s' % (G, N, self.f)
        for x in self.s:
            p = self.create(x)
            if p is None:
                self.count += 1
            else:
                open(self.f, 'a').write(p + '\n')
                print '\r%s[*]%s Generating Token %s/%s fail-:%s' % (
                 G, N, len(open(self.f).read().splitlines()),
                 len(self.s), self.count),
                sys.stdout.flush()

        print '\n[*] finished.'
        self.back()
        return

    def sing(self, a):
        f = raw_input('%s[?]%s [P]rint/[S]ave to file [P]/[S]> ' % (
         R, N)).lower()
        if f == 's':
            try:
                filename = raw_input('%s[?]%s Filename: ' % (G, N))
                if filename == '':
                    self.sing(a)
                open(filename, 'w').write(a + '\n')
                print '%s[*]%s Output: %s' % (G, N, filename)
                self.back()
            except Exception as e:
                print '%s[!]%s %s' % (R, N, e)
                self.sing(a)

        print a
        self.back()

    def create(self, a):
        f = a.split('|')
        API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
        data = {'api_key': '882a8490361da98702bf97a021ddc14d', 
           'credentials_type': 'password', 
           'email': f[0], 
           'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 
           'locale': 'en_US', 
           'method': 'auth.login', 'password': f[(-1)], 
           'return_ssl_resources': '0', 'v': '1.0'}
        sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + f[0] + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + f[(-1)] + 'return_ssl_resources=0v=1.0' + API_SECRET
        x = hashlib.new('md5')
        x.update(sig)
        data.update({'sig': x.hexdigest()})
        try:
            return requests.get('https://api.facebook.com/restserver.php', params=data).json()['access_token']
        except:
            pass


