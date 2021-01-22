# Filenames : tes.py
# Python bytecode : 2.7
# Time decompiled : Sun Sep 13 09:58:38 2020
# Selector <module> in line 1 file tes.py
# Timestamp in code: 2020-06-10 22:04:47

import time, sys

class EzzKun:

    def __init__(self):
        self.angka = 10
        self.apes = 0
        for i in range(self.angka):
            time.sleep(0.5)
            self.apes += 1
            sys.stdout.write('\r\x1b[1;34m[\x1b[1;37m*\x1b[1;34m]\x1b[1;37m Tunggu Sampai ' + str(self.apes))
            sys.stdout.flush()

        print '\n\x1b[1;34m[\x1b[1;37m*\x1b[1;34m]\x1b[1;37m INI ISINYA !!!'


try:
    EzzKun()
except EOFError:
    pass