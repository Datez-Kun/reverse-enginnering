# uncompyle6 version 3.6.2
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <script>
import string, fileinput, os, sys, time

def check():
    dots = [
     '.   ', '..  ', '... ']
    for o in dots:
        print '\r\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mChecking \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


def fix():
    dots = [
     '.   ', '..  ', '... ']
    for o in dots:
        print '\r\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mFixing status \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


logo = '\n\x1b[1;91m  \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90  \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90 \xe2\x94\xac\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\n\x1b[1;93m  \xe2\x94\x94\xe2\x94\x80\xe2\x94\x90\xe2\x94\x82  \xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x82\xe2\x94\x9c\xe2\x94\x80\xe2\x94\x98 \xe2\x94\x82   \xe2\x94\x9c\xe2\x94\xa4 \xe2\x94\x82\xe2\x94\x8c\xe2\x94\xb4\xe2\x94\xac\xe2\x94\x98\xe2\x95\x91\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa6\xe2\x95\x9d\n\x1b[1;92m\xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4\xe2\x94\xb4   \xe2\x94\xb4\xe2\x94\x80  \xe2\x94\x94  \xe2\x94\xb4\xe2\x94\xb4 \xe2\x94\x94\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\x1b[39;101m   Author \x1b[92m: \x1b[39mR3DB0T From TERMUXID3   \x1b[39;49m\n'

def out():
    os.sys.exit()


def error():
    err = [
     'FAILED']
    for o in err:
        print '\r\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mFixing status \x1b[1;91m' + o,
        sys.stdout.flush()
        time.sleep(1)


def fixing():
    suc = [
     'SUCCESS']
    for o in suc:
        print '\r\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mFixing status \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


def menu():
    os.system('clear')
    try:
        print logo
        g = raw_input('\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mSelect file \x1b[1;95m[\x1b[1;96mex\x1b[1;91m:\x1b[1;93mx.py\x1b[1;95m] \x1b[1;91m:\x1b[1;39m ')
        check()
        s = open(g).read()
        if "os.system('clear')" in s:
            print '\n\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mThere is no error'
            raw_input('\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mEnter to exit\x1b[1;39m')
            out()
        else:
            try:
                s = open(g).read()
                if "os.system('reset')" in s:
                    s = open(g).read()
                    fixed = '# FIXED BY R3DB0T\n# GITHUB : https://github.com/R3DB0T\n'
                    s = s.replace('reset', 'clear')
                    f = open('fix.py', 'w')
                    f.write(fixed + s)
                    f.close()
                    fix()
                    fixing()
                    print '\n\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mFile named \x1b[1;91m:\x1b[1;92m fix.py\x1b[1;39m'
                    raw_input('\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mEnter to exit\x1b[1;39m')
                    out()
                else:
                    fix()
                    error()
                    print '\n\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mFirst make the script normal or not compiled'
                    raw_input('\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mEnter to exit\x1b[1;39m')
                    out()
            except KeyboardInterrupt:
                os.sys.exit()
            except IOError:
                print '\n\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mFile\x1b[1;91m not found'
                raw_input('\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mEnter to exit\x1b[1;39m')
                out()

    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        print '\n\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mFile not found'
        raw_input('\x1b[1;91m[\x1b[1;96m*\x1b[1;91m] \x1b[1;92mEnter to exit\x1b[1;39m\x1b[1;39m')
        out()


menu()