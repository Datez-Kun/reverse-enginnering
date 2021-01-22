# Filenames : <tahm1d>
# Python bytecode : 2.7
# Time decompiled : Thu Sep 10 23:29:38 2020
# Selector <module> in line 4 file <tahm1d>
# Timestamp in code: 2020-09-02 17:33:14

import os, sys, time
from os import system
from time import sleep

def htrprint(s):
    for t in s + '\n':
        sys.stdout.write(t)
        sys.stdout.flush()
        sleep(0.01)


def menu():
    system('rm -rf *.pyc *.dis')
    htrprint(' \x1b[1;96mHello Bro !!')
    htrprint('\n \x1b[1;96mExcute \x1b[1;92mpython2 crack.py \x1b[1;96mto run this tool !\x1b[1;97m')
    sleep(1)


if __name__ == '__main__':
    menu()

