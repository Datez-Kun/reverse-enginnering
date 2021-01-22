# Filenames : <tahm1d>
# Python bytecode : 2.7
# Time decompiled : Fri Sep 11 20:14:51 2020
# Selector <module> in line 1 file <tahm1d>
# Timestamp in code: 2020-09-02 17:33:14

import os, sys, fileinput
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'
logo = "\n \x1b[1;33m _____                             _            \n \x1b[1;33m|  __ \\    \x1b[1;36mBash File\x1b[1;33m              | |           \n \x1b[1;33m| |  | | ___  ___ _ __ _   _ _ __ | |_ ___ _ __ \n \x1b[1;33m| |  | |/ _ \\/ __| '__| | | | '_ \\| __/ _ \\ '__|\n \x1b[1;33m| |__| |  __/ (__| |  | |_| | |_) | ||  __/ |   \n \x1b[1;33m|_____/ \\___|\\___|_|   \\__, | .__/ \\__\\___|_|   \n \x1b[1;33m                        __/ | |                 \n \x1b[1;33m                       |___/|_|                 \n \x1b[1;33m\n \x1b[1;36m    [\x1b[1;37m+\x1b[1;36m]\x1b[1;32m CREATED BY HTR-TECH (TAHMID RAYAT)\n"
banner = ('\n {}[{}01{}]{} Decrypt Bash File\n \n {}[{}02{}]{} More Tools from us\n \n').format(C, W, C, Y, C, W, C, Y)
os.system('clear')
print logo
print banner

def decr():
    try:
        print ''
        scname = raw_input(G + ' Name of the Script to Decrypt' + C + ' > ' + Y)
        o = open(scname, 'r')
        filedata = o.read()
        o.close()
        new_dat = filedata.replace('eval', 'echo')
        print ''
        output = raw_input(G + ' Name of the Decrypted Script' + C + ' > ' + Y)
        f = open(output, 'w')
        S = output
        f.write(new_dat)
        f.close()
        os.system('touch dummy.sh')
        os.system('bash ' + output + ' > dummy.sh')
        os.remove(output)
        os.system('mv -f dummy.sh ' + output)
        print ''
        print G + ' Decryption Succeed...'
        print ''
        print Y + ' Decrypted Script Name' + C + ' > ' + G + S + W
        print ''
    except KeyboardInterrupt():
        print R + ' !' + Y + ' Tool Stopped ' + R + '!' + W
        print ''
    except IOError:
        print R + ' !' + Y + ' File not Found ' + R + '!' + W
        print ''


maintool = raw_input(G + ' Select an option' + C + ' > ' + Y)
if maintool == '1' or maintool == '01':
    decr()
elif maintool == '2' or maintool == '02':
    os.system('xdg-open https://github.com/htr-tech/')
else:
    print W + ''
    print C + ' [' + R + '!' + C + ']' + Y + ' Invalid input ' + C + '[' + R + '!' + C + ']'

