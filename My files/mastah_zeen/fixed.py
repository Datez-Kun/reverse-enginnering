# Source Generated With Decompyle++
# File : fixed.pyc (Python 2.7)

import time
import sys

class EzzKun:
    
    def __init__(self):
        self.angka = 10
        self.apes = 0
        for i in range(self.angka):
            time.sleep(0.5)
            self.apes += 1
            sys.stdout.write('\r\x1b[1;34m[\x1b[1;37m*\x1b[1;34m]\x1b[1;37m Tunggu Sampai ' + str(self.apes))
            sys.stdout.flush()
        else:
            print '\n\x1b[1;34m[\x1b[1;37m*\x1b[1;34m]\x1b[1;37m INI ISINYA !!!'
            return None



try:
    EzzKun()
except EOFError:
    pass

