# Filenames : <tahm1d>
# Python bytecode : 2.7
# Time decompiled : Fri Sep 11 20:05:16 2020
# Selector <module> in line 3 file <tahm1d>
# Timestamp in code: 2020-09-02 17:33:14

import os, re, sys, time

def decompile(file):
    os.system('rm -rf .tmp .htr')
    htr = '\n# Python Auto Dis Parser 1.1.0\n# Author : HTR-TECH | TAHMID RAYAT\n# https://linktr.ee/tahmid.rayat\n# https://fb.me/tahmid.rayat.official\n# ------------------------------------------\n# Embedded File   : %s\n# Python Bytecode : %s (62211)\n# Decompiled at   : %s\n# ------------------------------------------\n' % (sys.argv[1], sys.version_info[0] + sys.version_info[1] / 10.0, time.ctime())
    try:
        h1 = open(file).read()
    except IOError:
        sys.exit('[!] File Not Found [!]')

    h2 = h1.replace('exec', 'print')
    h3 = open('.tmp', 'w')
    h3.write(h2)
    h3.close()
    h4 = open('.htr', 'w')
    h4.write(htr + '\n')
    h4.close()
    os.system('python2 .tmp >> .htr')
    os.system('cat .htr')
    time.sleep(0.75)
    sys.stdout.write('\n# Okay Decompiling ' + sys.argv[1] + '\n')
    os.system('rm -rf .tmp .htr')


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        decompile(sys.argv[1])
    else:
        print '\n# Python Auto Dis Parser 1.1.0'
        print '# Author : HTR-TECH | TAHMID RAYAT'
        print '# https://linktr.ee/tahmid.rayat'
        print '# https://fb.me/tahmid.rayat.official'
        print ''
        sys.exit('[-] Usage : ' + __file__ + ' input > output\n')