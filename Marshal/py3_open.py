# File Names : <Sanz>
# Python Bytecode : 3.8
# Time Succses Parser : Mon Jul  6 13:53:32 2020
# Auto Parser Dis Version : 1.2.1
# Source : https://www.github.com/Datez-Kun

import marshal, os, time
h = '\x1b[1;92m'
bi = '\x1b[1;96m'
k = '\x1b[1;93m'
u = '\x1b[1;95m'
pu = '\x1b[1;97m'
b = '\x1b[1;94m'
m = '\x1b[1;91m'
hi = '\x1b[1;30m'
hg = '\x1b[4;92m'
p = '\x1b[0m'

def logo():
    os.system('clear')
    print(u + '┬─┐┬ ┬┌┬┐┬ ┬┌─┐┌┐┌  ┬─┐┌─┐┌┬┐┌─┐┬┬  ┌─┐┬─┐\n├─┘└┬┘ │ ├─┤│ ││││  │  │ ││││├─┘││  ├┤ ├┬┘\n┴   ┴  ┴ ┴ ┴└─┘┘└┘  └─┘└─┘┴ ┴┴  ┴┴─┘└─┘┴└─')
    print(hi + '------------------------------------------')
    print(p + '[' + h + '•' + p + '] ' + pu + 'Author ' + m + ': ' + bi + 'Sanz')
    print(p + '[' + h + '•' + p + '] ' + pu + 'Youtube' + m + ': ' + bi + 'SANZ SOEKAMTI')
    print(p + '[' + h + '•' + p + '] ' + pu + 'Github' + m + ': ' + hg + 'https://github.com/B4N954N2-ID' + p)
    print(hi + '------------------------------------------')


def main():
    try:
        logo()
        print(p + '[' + h + '+' + p + '] ' + k + 'Ex ' + m + ': ' + p + '/sdcard/file.py')
        a = input(p + '[' + h + '+' + p + '] ' + pu + 'File ' + m + ': ' + h)
        x = open(a).read()
        b = compile(x, '<Sanz>', 'exec')
        c = a.replace('.py', '_enc.py')
        d = marshal.dumps(b)
        e = open(c, 'w')
        e.write('# Compile by Sanz\n# Youtube : SANZ SOEKAMTI\n# Github  : https://github.com/B4N954N2-ID\n')
        e.write('import marshal\n')
        e.write('exec(marshal.loads(' + repr(d) + '))')
        e.close()
        time.sleep(2)
        print(p + '[' + h + '+' + p + '] ' + pu + 'Files Encrypted ' + m + ': ' + h + c)
        os.system('xdg-open https://youtube.com/SanzSoekamti')
        time.sleep(0.1)
    except IOError:
        print(p + '[' + m + 'x' + p + '] ' + pu + 'File Not Found')
        time.sleep(1)
        main()
    except KeyboardInterrupt:
        out()


def out():
    time.sleep(0.1)
    print(p + '[' + h + '+' + p + '] ' + p + 'Thanks For Using This My Tools')
    os.system('xdg-open https://youtube.com/SanzSoekamti')
    time.sleep(1)
    exit(p + '[' + m + '!' + p + '] ' + p + 'Exit')


try:
    main()
except KeyboardInterrupt:
    out()