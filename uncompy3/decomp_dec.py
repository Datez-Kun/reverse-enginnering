# MENTOL 
# At:Sun Nov 24 15:04:31 2019 
if len(bytecode) == 0:
    print('\x1b[1;93mbyte code kosong\nharap masukkan bytecodenya\x1b[0m')
    exit()

import marshal, sys, os, random, string, time
try:
    from uncompyle6.main import decompile
except:
    os.system('pip install uncompyle6')
    from uncompyle6.main import decompile

def echo(text):
    w = 'mhkbucp'
    for z in w:
        text = text.replace('+%s' % z, '\x1b[%d;1m' % (91 + w.index(z)))

    text += '\x1b[0m'
    text = text.replace('+0', '\x1b[0m')
    print(text)


def run(text):
    try:
        w = 'mhkbucp'
        for z in w:
            text = text.replace('+%s' % z, '\x1b[%d;1m' % (91 + w.index(z)))

        text += '\x1b[0m'
        text = text.replace('+0', '\x1b[0m')
        for i in text + '\n':
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.01)

    except (KeyboardInterrupt, EOFError):
        exit('')


n = ''.join((random.choice(string.ascii_lowercase) for _ in range(4)))
fl = n + '-dec.py'
logo = '\n+m     888                                                           +h,8,"88b,\n+m e88 888  ,e e,   e88\'888  e88 88e  888 888 8e  +p888 88e  Y8b Y888P +h " ,88P\'\n+md888 888 d88 88b d888  \'8 d888 888b 888 888 88b +p888 888b  Y8b Y8P  +h   C8K\n+mY888 888 888   , Y888   , Y888 888P 888 888 888 +p888 888P   Y8b Y   +h e `88b,\n+m "88 888  "YeeP"  "88,e8\'  "88 88"  888 888 888 +p888 88"     888    +h"8",88P\'\n                                                +p888         888\n                                                +p888         888+p\n\t\t+ccoded by: +pZhu Bai Lee AKA AnonyMass\n\t\t+cteam    : +pBlack Coder Crush'

def decom():
    try:
        os.system('clear')
        echo(logo)
        x = decompile(3.7, marshal.loads(bytecode), open(fl, 'w'))
        run('\t\t\t+hdecompile sukses :)+p')
        run('\t\t\t+hfile disimpan: +p' + fl)
        exit()
    except Exception as e:
        try:
            os.system('clear')
            echo(logo)
            echo('+mdecompile gagal+p')
            exit()
        finally:
            e = None
            del e


decom()
