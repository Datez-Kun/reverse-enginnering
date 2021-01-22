# Filenames : <tahm1d>
# Python bytecode : 2.7
# Time decompiled : Sat Sep 12 02:39:37 2020
# Selector <module> in line 5 file <tahm1d>
# Timestamp in code: 2020-08-19 16:29:47

import os, base64, codecs
from sys import argv
from os import system
from time import ctime
note = '\n# Obfuscated By TAHMID RAYAT | HTR-TECH\n# Github    : https://www.github.com/htr-tech\n# Instagram : https://instagr.am/tahmid.rayat\n'
flag1 = ctime()
flag2 = os.uname()
flag3 = '# Time      : ' + flag1 + '\n'
flag4 = '# Platform  : ' + flag2[0] + ' ' + flag2[4] + '\n'
flag0 = '# --------------------------------------------\n'
obf_note = note + flag0 + flag3 + flag4 + flag0

def main(file):
    try:
        htr1 = open(file).read()
    except IOError:
        os.sys.exit('[!] File Not Found [!]')

    htr2 = file.replace('.py', '_enc.py')
    htr3 = base64.b64encode(htr1)
    h1 = []
    h2 = []
    h3 = []
    h4 = ''
    h5 = ''
    for x in htr3:
        h1.append(ord(x))

    z = 0
    while 1:
        h2.append(h1[z])
        if z >= len(h1) / 2:
            break
        z += 1

    v = len(h1) / 2 + 1
    try:
        while 1:
            h3.append(h1[v])
            v += 1

    except IndexError:
        pass

    for s in h3:
        h4 += chr(s)

    htr4 = codecs.encode(h4, 'rot_13')
    h6 = open(htr2, 'w')
    h6.write(obf_note + '\nimport codecs,base64\n' + 'htr = ' + str(h2) + '\t\t\n' + "tahmid = '" + str(htr4) + "'\t\t\n")
    h6.write("pizza = '\\x72\\x6f\\x74\\x5f\\x31\\x33'\t\t\n")
    h6.write("mobile = codecs.decode(eval('\\x74\\x61\\x68\\x6d\\x69\\x64'), eval('\\x70\\x69\\x7a\\x7a\\x61'))\t\t\n")
    h6.write("burger = base64.b64decode(''.join([chr(tech) for tech in htr])+eval('\\x6d\\x6f\\x62\\x69\\x6c\\x65'))\t\t\n")
    h6.write('eval(compile(eval("\\x62\\x75\\x72\\x67\\x65\\x72"),"<tahm1d>","exec"))\t\t\n')
    h6.close()
    print '[-] SuccessFully Encrypted ' + htr2


if __name__ == '__main__':
    if len(argv) >= 2:
        main(argv[1])
    else:
        os.sys.exit('[-] Type : ' + __file__ + ' <script>')

