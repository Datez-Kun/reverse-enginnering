# coding=utf-8
# simple disassembly all object bytecode 2.7
# usage : python2 file.pyc > file.dis

import dis
import types
import sys
import marshal
import re
import time
import datetime
import os
from xdis.util import format_code_info as format_

class Disassemble(object):
	def __init__(self,file):
		self.file = file
		self.read_file()
	def read_file(self):
		try:
			cons = open(self.file,'rb').read()
		except FileNotFoundError:
			exit('-! file %s not found'%(sys.argv[1]))
		byte = marshal.loads(cons[8:])
		self.show_all(byte)
	def show_all(self,code):
		try:
			_stamp = os.stat(self.file).st_mtime
			_value = datetime.datetime.fromtimestamp(_stamp).strftime(" (%Y-%m-%d %H:%M:%S)\n")
			__info__ = ('# FileNames : %s\n# Python Bytecode : %s\n# Selector %s In Line %s file %s\n# Timestamp In Code : %s') %(code.co_filename,sys.version.split()[0],code.co_name,code.co_firstlineno,self.file,_value)
			print(__info__)
			print(format_(code,float(sys.version.split()[0][:3])))
			dis.dis(code)
			for const in code.co_consts:
				if type(const) == types.CodeType:
					self.show_all(const)
				else:
					pass
		except:
			pass

if __name__=="__main__":
	if len(sys.argv) < 2:
		exit('usage : inspek.py <file.pyc>')
	else:
		Disassemble(sys.argv[1])
