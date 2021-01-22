# Filenames : <tahm1d>
# Python bytecode : 2.7
# Time decompiled : Fri Sep 11 19:57:32 2020
# Selector <module> in line 3 file <tahm1d>
# Timestamp in code: 2020-09-02 17:33:14

import os, re, sys, time, zlib, base64, marshal, subprocess
try:
    from uncompyle6.main import decompile
except Exception:
    e = None
    subprocess.call('pip2 install uncompyle6', shell=True, stderr=subprocess.STDOUT)

def decompile(file):
    os.system('rm -rf .tmp .htr')
    htr = '\n# Python Auto Dis Parser 1.0.1\n# Author : HTR-TECH | TAHMID RAYAT\n# https://linktr.ee/tahmid.rayat\n# https://fb.me/tahmid.rayat.official\n# ------------------------------------------'
    try:
        h1 = open(file).read()
    except IOError:
        sys.exit('[!] File Not Found [!]')

    h2 = h1.replace('exec', 'hax = ')
    h3 = open('.tmp', 'w')
    h3.write(h2 + '\nimport marshal,zlib,base64\nfrom sys import stdout\nfrom uncompyle6.main import decompile\ndecompile(2.7,hax,stdout)')
    h3.close()
    h4 = open('.htr', 'w')
    h4.write(htr + '\n')
    h4.close()
    os.system('python2 .tmp >> .htr')
    os.system('cat .htr')
    sys.stdout.write('\n')
    os.system('rm -rf .tmp .htr')


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        decompile(sys.argv[1])
    else:
        print '\n# Python Auto Dis Parser 1.0.1'
        print '# Author : HTR-TECH | TAHMID RAYAT'
        print '# https://linktr.ee/tahmid.rayat'
        print '# https://fb.me/tahmid.rayat.official'
        print ''
        sys.exit('[-] Usage : ' + __file__ + ' input > output\n')

