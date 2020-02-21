#-*- coding: utf8 -*-
#ya maap kodingam we berantakan :)>

import requests,random,time,os,sys
req=requests.Session()

r='\033[91m'
c='\033[96m'
w='\033[0m'

__banner__ = ('''
  spam kita.bisa gan :V
%s ###############################
 # %scode : Maoundis             %s#
 # %stype : wa/email             %s#
 # %steam : xiuz.sec             %s#
 ###############################%s
    ''' % (c,w,c,w,c,w,c,w))


class Mate_lampu():
        def __init__(self):
            self.ua=open('ua.txt').read().splitlines()
            self.sok_aelu()

        def sok_aelu(self):
            type = str(sys.argv[1])
            if type=='wa':
                self.tolol = 'phone_number'
                self.goblok=str(sys.argv[2])
            elif type=='email':
                self.tolol = 'email'
                self.goblok=str(sys.argv[2])
            else:
                Mate_lampu()
            self.spam_kuy()

        def spam_kuy(self):
            saapa=int(sys.argv[3])
            print('[!] delay 4 menit :V')
            for i in range(1,saapa+1):
                req.headers.update({'user-agent':random.choice(self.ua)});ceko = req.post('https://core.ktbs.io/v2/user/registration/temp', json = {'full_name':'Maoundis','user_id':self.goblok,'user_id_type':self.tolol})
                if ceko.status_code == 200:
                    print('  [%d] pesan: suskes nyepam gan hehe :"c ' % (i))
                else:
                    print('  [%d] pesan: %s' % (i,ceko.json()['errors'][0]['details']['id']))
                time.sleep(240)
                continue
            quit('[#] selsai ,,,,')







# -----main -------

#try:
sys.exit(Mate_lampu())
#except Exception as _er:
#    quit('%serror: %s' % (r,_er))
