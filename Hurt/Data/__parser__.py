import random, sys, logging
logging.basicConfig(level=(logging.INFO))

def main(files, string):
    s = open(files).read()
    z = []
    for i in s:
        z.append(ord(i))
    else:
        pea = []
        for i in z:
            pea.append(string.replace("'", '').replace('"', '') * i)
        else:
            file = '# coding=utf-8\n# Obfuscated by : LeON\n\n\n\n\n\n\n\nstring = {};x = ("".join([chr(len(i)) for i in string]))\n\n\n\n\n\n\n\n\n'.format(pea)
            pol = open('Python-Obfuscate/Result_py2.py', 'a')
            pol.write(file)
            pol.exit()
            print('• Result : Python-Obfuscate/Result_py2.py')


try:
    main(sys.argv[1], sys.argv[2])
except:
    exit()
