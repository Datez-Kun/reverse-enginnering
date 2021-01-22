# Filename : ex.py
# Python Bytecode : 2.7
# Time Succses Decompiled : Sat Aug 15 18:31:53 2020
# Timestamp In Code : 2020-06-10 22:04:47
# Source Generated With Decompyle++
# File : analyze.pyc (Python 2.7)

import time
import sys
from random import choice as ch
__po__ = [
    '\x1b[1;31m',
    '\x1b[1;32m',
    '\x1b[1;33m',
    '\x1b[1;34m']

class ClAss:
#Segmentation fault

	def __init__(self):
	    self.time = 0.7
	    self.ReturN()


	def DaTez_Kun(self, teks):
	    for o in teks + '\n':
	        sys.stdout.write(o)
	        sys.stdout.flush()
	        time.sleep(10.0 / 100)


	def ReturN(self):
	    _ = 0
	    for _ in range(10):
	        _ += 1
	        sys.stdout.write('\r%s[%s*%s]%s Wait A Second ! %s %s ' % (ch(__po__), ch(__po__), ch(__po__), ch(__po__), ch(__po__), str(_)))
	        sys.stdout.flush()
	        time.sleep(self.time)

	    self.DaTez_Kun('\n%s[%s*%s]%s Thanks For Waiting' % (ch(__po__), ch(__po__), ch(__po__), ch(__po__)))

if __name__=="__main__":
	ClAss()
