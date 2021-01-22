# simple disassembly python bytecode
# © Datez-Kun (love-love) is kyun-kyun 
import dis
import types
import sys
import marshal
import re
import time
import datetime
import os
from xdis.cross_dis import format_code_info as format_

class Disassemble(object):
	def __init__(self,file):
		self.file = file
		self.read_file()
	def read_file(self):
		try:
			cons = open(self.file,'rb').read()
		except FileNotFoundError:
			exit(f'-! file {sys.argv[1]} not found ')
		byte = marshal.loads(cons[16:])
		self.show_all(byte)
	def show_all(self,code):
		_stamp = os.stat(self.file).st_mtime
		_value = datetime.datetime.fromtimestamp(_stamp).strftime(" (%Y-%m-%d %H:%M:%S)\n")
		__info__ = (
		f'# FileNames : {code.co_filename}\n'
		f'# Python Bytecode : {sys.version.split()[0]}\n'
		f'# Selector {code.co_name} In Line {code.co_firstlineno} file {self.file}\n'
		f'# Timestamp In Code : {_value}'
		)
		print(__info__)
		print(format_(code,float(sys.version.split()[0][:3])))
		dis.dis(code)
		for const in code.co_consts:
			if type(const) == types.CodeType:
				self.show_all(const)
			else:
				pass

if __name__=="__main__":
	if len(sys.argv) < 2:
		exit('usage : inspek.py <file.pyc>')
	else:
		Disassemble(sys.argv[1])
