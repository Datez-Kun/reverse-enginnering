# uncompyle6 version 3.6.2
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <default>
import os, sys, time
normal = '\x1b[0;39m'
logo = "\n\x1b[92m  ___ ___       __                                 __       \n\x1b[92m |   Y   .-----|  |--.   .-----.---.-.-----.---.-.|__.--.--.\n\x1b[92m |.  1   |  -__|    <    |     |  _  |__ --|  _  | __|  |  |\n\x1b[92m |.  _   |_____|__|__|   |__|__|___._|_____|___._||__|\\___/ \n\x1b[92m |:  |   |    \x1b[95mAuthor  \x1b[91m: R3DB0T                           \n\x1b[92m |::.|:. |    \x1b[95mGithub  \x1b[91m: \x1b[4;96mhttps://github.com/R3DB0T\x1b[0;39m\n\x1b[92m `--- ---'    \x1b[95mMessage \x1b[91m: \x1b[95mGunakan \x1b[96mBaik \x1b[94mBaik:v\n"

def mlaku(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def menu():
    os.system('clear')
    print logo + normal
    print 50 * '\x1b[91m=' + normal
    x = raw_input('\x1b[92mMessage\x1b[91m: ' + normal)
    xx = x.replace(' ', '+')
    xxx = xx.replace('/', '%2')
    mlaku('\x1b[92mHacking...' + normal)
    mlaku('\x1b[92mSuccess!' + normal)
    print '\x1b[95mCopy \x1b[91m: \x1b[92mhttps://nasasearch.nasa.gov/search?utf8=%E2%9C%93&affiliate=nasa&sort_by=&query=' + xxx + normal
    os.sys.exit()


menu()