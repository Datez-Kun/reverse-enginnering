import os
import sys
import time
import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

logo = """
\033[1;32m  ______    _         \033[1;33m  __  __       _ _           
\033[1;32m |  ____|  | |        \033[1;33m |  \/  |     (_) |          
\033[1;32m | |__ __ _| | _____  \033[1;33m | \  / | __ _ _| | ___ _ __ 
\033[1;32m |  __/ _  | |/ / _ \ \033[1;33m | |\/| |/ _  | | |/ _ \  __|
\033[1;32m | | | (_| |   <  __/ \033[1;33m | |  | | (_| | | |  __/ |   
\033[1;32m |_|  \__,_|_|\_\___| \033[1;33m |_|  |_|\__,_|_|_|\___|_|   

\033[1;36m [\033[1;37m+\033[1;36m]\033[1;32m CREATED BY HTR-TECH \033[1;31m(\033[1;33mTAHMID RAYAT\033[1;31m)
"""

os.system("clear")
print (logo)
print ("")
slowprint(G + ' Launching Fake Mailer ...')
time.sleep(2)
print ("")
to = raw_input(G + " Send Mail To" + C + " : " + Y)
print ("")
subject = raw_input(G + " Input Mail Subject" + C + " : " + Y)
print ("")
msg = raw_input(G + " Input Mail Content" + C + " : " + Y)
print ("")
user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
mailsession = requests.Session()
email_sender = mailsession.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
	'Host': 'anonymouse.org',
	'User-Agent': user_agent,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://anonymouse.org/anonemail.html',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded'
}, data={
	'to': to,
	'subject': subject,
	'text': msg
})

if 'The e-mail has been sent' in email_sender.text:
    slowprint(G + " Sending Email >>>>>>>>>>")
    print ("")
    time.sleep(5)
    slowprint(C + " Mail Successfully Sent !!")
    print ("")
    time.sleep(3)
    slowprint(W + " Process can take some time !!")
    print ("")
    print (Y + " Visit www.github.com/htr-tech for More Tools" + W)
    print ("")

