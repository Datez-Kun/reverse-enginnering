import os
import sys
import time
from platform import system

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3.0 / 100)
      
logo = """
\033[1;32m  ______         \033[1;33m _                  _     
\033[1;32m (_____ \        \033[1;33m| |                | |    
\033[1;32m  _____) )   _   \033[1;33m| |      ___   ____| |  _ 
\033[1;32m |  ____/ | | |  \033[1;33m| |     / _ \ / ___) |_/ )
\033[1;32m | |    | |_| |  \033[1;33m| |____| |_| ( (___|  _ ( 
\033[1;32m |_|     \__  |  \033[1;33m|_______)___/ \____)_| \_)
\033[1;32m        (____/                             

\033[1;36m [\033[1;37m+\033[1;36m]\033[1;32m CREATED BY HTR-TECH (TAHMID RAYAT)
"""
banner = """
 {}[{}01{}]{} Encrypt Python
 
 {}[{}02{}]{} Encrypt Python2
 
 {}[{}03{}]{} More Tools from us
 
""".format(C,W,C,Y,C,W,C,Y,C,W,C,Y)

os.system("clear")
print logo
slowprint (banner)

mainmenu = raw_input(G + " Select an option" + C + " > " + Y)

if mainmenu == "1" or mainmenu == "01":
    print ("")
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ("")
    py_one = raw_input(G + " Name of the Script to Encrypt (without .py)" + C + " > " + Y)
    print ("")
    by_one = raw_input(G + " Encrypted Script Name (without .py)" + C + " > " + Y)
    py_dato = ("__pycache__/"+str(py_one)+".cpython-38.opt-2.pyc")
    print ("")
    slowprint (G + " Encrypting...")
    os.system('python -OO -m py_compile ' + py_one+'.py')
    print ("")
    os.system("mv "+str(py_dato)+" "+str(by_one)+".py")
    os.system('rm -rf __pycache__')
    time.sleep(3)
    slowprint(G + " Encryption Completed...")
    time.sleep(3)
    print ("")
    slowprint(G + ' Encrypted File Name '+str(by_one)+".py")
    print ("")
    print (W)
    
elif mainmenu == "2" or mainmenu == "02":
    print ("")
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ("")
    py_two = raw_input(G + " Name of the Script to Encrypt (without .py)" + C + " > " + Y)
    print ("")
    by_two = raw_input(G + " Encrypted Script Name (without .py)" + C + " > " + Y)
    py_datt = (str(py_two)+".pyo")
    print ("")
    slowprint (G + " Encrypting...")
    os.system('python2 -OO -m py_compile ' + py_two+'.py')
    print ("")
    os.system("mv "+str(py_datt)+" "+str(by_two)+".py")
    time.sleep(3)
    slowprint(G + " Encryption Completed...")
    time.sleep(3)
    print ("")
    slowprint(G + ' Encrypted File Name '+str(by_two)+".py")
    print ("")
    print (W)
    
elif mainmenu == "3" or mainmenu == "03":
    print ("")
    slowprint(G + "  You are being Redirectrd to Github")
    time.sleep(1)
    os.system("termux-open-url https://github.com/htr-tech/")
    print ("")
    print (W)
else:
   print (W + "")
   print (C + "[" + R + " !" + C + "]" + Y + " Invalid input " + C + "[" + R + "!" + C + "]")

