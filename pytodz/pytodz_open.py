# Filenames : xSODx
# python bytecode : 2.7
# Time Succses Parser : Fri Jul 24 14:09:24 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

#!/usr/bin/python2
# -*- coding:utf-8 -*-
import os, sys, re, time
import binascii, base64, marshal, zlib
from py_compile import compile as _compile
try:
	import uncompyle6
except ImportError:
	os.system('pip2 install uncompyle6')
_0o0oO_ = u'S\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8m\x8e$S\xd8s)\x80\xa0\xcd\xc8\xc7?\xca\x9a\x80.\xc7/\xd1\xca\xcd%\x80\xeb`/\xc2/>/\x8e$S\xd8s)\x80\xeb\xc4\xca\xd1\xf8\xc8\x9a\x80\xe4?_\xf8\xd1%\xc1\x80\x17\x80\xe0\xc1\xc4?_\xf8\xd1%\xc1\x80\xf8`\xc8\xc7?>\x16\x8e$S\xd8s)\x80\xe5\xd1\xc8\xc7\xcd\xc2\x9a\x80\xc7\xc8\xc8\xf8\xcb\x9a\x07\x07\xc5\xd1\xc8\xc7\xcd\xc2\x06\xc4?_\x07\xcc\xeb!\xe0\xcc\x91\x91\x8eS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8mS\xd8m'
tod = []


def save_file(outfile, value):
	open(outfile, 'w').write(value[0])
	del value[::]
	main_menu('[√] File Saved '+outfile)

class Compile:
	def __init__(self, file):
		try:
			self.code = open(file).read()
			self.outfile = str('enc_'+file)
			self.filename = str(file)
		except Exception as exception:
			main_menu(exception)

	def marshal(self):
		tod.append('import marshal\nexec marshal.loads({code})'.format(code=repr(marshal.dumps(compile(self.code, self.filename, 'exec')))))
		save_file(self.outfile, tod)

	def pyc(self):
		_compile(self.filename)
		main_menu('[√] File Saved '+self.filename+'c')

	def zlib(self):
		tod.append('import zlib\nexec zlib.decompress({code})'.format(code=repr(zlib.compress(self.code))))
		save_file(self.outfile, tod)

	def base16(self):
		tod.append('import base64\nexec base64.b16decode("{code}")'.format(code=base64.b16encode(self.code)))
		save_file(self.outfile, tod)

	def base32(self):
		tod.append('import base64\nexec base64.b32decode("{code}")'.format(code=base64.b32encode(self.code)))
		save_file(self.outfile, tod)

	def base64(self):
		tod.append('import base64\nexec base64.b64decode("{code}")'.format(code=base64.b64encode(self.code)))
		save_file(self.outfile, tod)

	def hex(self):
		tod.append('import binascii\nexec binascii.unhexlify("%x" % int("{code}", 0))'.format(code=hex(int(binascii.hexlify(self.code),16))))
		save_file(self.outfile, tod)

	def bin(self):
		tod.append('import binascii\nexec binascii.unhexlify("%x" % int("{code}", 0))'.format(code=bin(int(binascii.hexlify(self.code),16))))
		save_file(self.outfile, tod)


class Decompile:
	def __init__(self, file):
		try:
			self.code = open(file).read()
			self.outfile = str('dec_'+file)
			self.filename = str(file)
		except Exception as exception:
			main_menu(exception)

	def marshal(self):
		if 'marshal.loads' in self.code:
			if 'c\\x00' in self.code:
				if ')))' in self.code:
					code = re.search('marshal.loads(.+)', self.code).group()[:-2]
				elif '(marshal.loads(' in self.code:
					code = re.search(r'[(]marshal.loads(.+)', self.code).group()[1:][:-1]
				else:
					code = re.search(r'marshal.loads(.+)', self.code).group()
			else:
				main_menu('[!] File not supported')
		else:
			main_menu('[!] File not supported')
		open('_oOoOo_', 'w').write('import marshal, sys\n__import__("uncompyle6").main.decompile(2.7, {code}, sys.stdout)'.format(outfile=self.outfile, code=str(code)))
		os.system('python2 _oOoOo_ > {hasil}'.format(hasil=self.outfile))
		os.remove('_oOoOo_')
		main_menu('[√] File saved '+self.outfile)

	def pyc(self):
		os.system('uncompyle6 {filename} > {hasil}'.format(filename=self.filename, hasil=self.filename[:-4]+'_dec.py'))
		main_menu('[√] File saved '+self.filename[:-4]+'_dec.py')

	def zlib(self):
		if 'zlib.decompress' in self.code:
			if ')))' in self.code:
				code = re.search(r'zlib.decompress(.+)', self.code).group()[:-2]
			elif '(zlib.decompress(' in self.code:
				code = re.search(r'[(]zlib.decompress(.+)', self.code).group()[1:][:-1]
			else:
				code = re.search(r'zlib.decompress(.+)', self.code).group()
		else:
			main_menu('[!] File not supported')
		exec 'print >> open("{hasil}", "w"), {code}'.format(hasil=self.outfile, code=str(code))
		main_menu('[√] File saved '+self.outfile)

	def base16(self):
		if 'base64.b16decode' in self.code:
			if ')))' in self.code:
				code = re.search(r'base64.b16decode(.+)', self.code).group()[:-2]
			elif '(base64.b16decode(' in self.code:
				code = re.search(r'[(]base64.b16decode(.+)', self.code).group()[1:][:-1]
			else:
				code = re.search(r'base64.b16decode(.+)', self.code).group()
		else:
			main_menu('[!] File not supported')
		exec 'print >> open("{hasil}", "w"), {code}'.format(code=str(code), hasil=self.outfile)
		main_menu('[√] File saved '+self.outfile)

	def base32(self):
		if 'base64.b32decode' in self.code:
			if ')))' in self.code:
				code = re.search(r'base64.b32decode(.+)', self.code).group()[:-2]
			elif '(base64.b32decode(' in self.code:
				code = re.search(r'[(]base64.b32decode(.+)', self.code).group()[1:][:-1]
			else:
				code = re.search(r'base64.b32decode(.+)', self.code).group()
		else:
			main_menu('[!] File not supported')
		exec 'print >> open("{hasil}", "w"), {code}'.format(code=str(code), hasil=self.outfile)
		main_menu('[√] File saved '+self.outfile)

	def base64(self):
		if 'base64.b64decode' in self.code:
			if ')))' in self.code:
				code = re.search(r'base64.b64decode(.+)', self.code).group()[:-2]
			elif '(base64.b64decode(' in self.code:
				code = re.search(r'[(]base64.b64decode(.+)', self.code).group()[1:][:-1]
			else:
				code = re.search(r'base64.b64decode(.+)', self.code).group()
		else:
			main_menu('[!] File not supported')
		exec 'print >> open("{hasil}", "w"), {code}'.format(code=str(code), hasil=self.outfile)
		main_menu('[√] File saved '+self.outfile)

	def hex(self):
		if 'binascii.unhexlify' in self.code:
			if '))))' in self.code:
				code = re.search(r'binascii.unhexlify(.+)', self.code).group()[:-2]
			elif '(binascii.unhexlify(' in self.code:
				code = re.search(r'[(]binascii.unhexlify(.+)', self.code).group()[1:][:-1]
			else:
				code = re.search(r'binascii.unhexlify(.+)', self.code).group()
		else:
			main_menu('[!] File not supported')
		exec 'print >> open("{outfile}", "w"), {code}'.format(outfile=self.outfile, code=str(code))
		main_menu('[√] File saved '+self.outfile)

	def bin(self):
		if 'binascii.unhexlify' in self.code:
			if '))))' in self.code:
				code = re.search(r'binascii.unhexlify(.+)', self.code).group()[:-2]
			elif '(binascii.unhexlify(' in self.code:
				code = re.search(r'[(]binascii.unhexlify(.+)', self.code).group()[1:][:-1]
			else:
				code = re.search(r'binascii.unhexlify(.+)', self.code).group()
		else:
			main_menu('[!] File not supported')
		exec 'print >> open("{outfile}", "w"), {code}'.format(outfile=self.outfile, code=str(code))
		main_menu('[√] File saved '+self.outfile)


def main_menu(text=None):
	if text is not None:
		print text
		time.sleep(1.5)
	else:pass

	os.system('clear')
	print _0o0oO_.encode('cp500')
	print ('[1] Compile {0}\n[2] Decompile {0}\n[3] Exit').format('Menu')
	print '—'*48

	try:
		choose = raw_input('[•] Choose: ')
	except (EOFError, KeyboardInterrupt):pass

	if choose in ('1', '2', '3'):
		choose = int(choose)
		if choose == 1:
			compile_menu()
		elif choose == 2:
			decompile_menu()
		elif choose == 3:
			sys.exit('[!] Exit')
	else:
		main_menu('[!] Wrong Input')
	return


def compile_menu():
	os.system('clear')
	print _0o0oO_.encode('cp500')
	print ('[1] {0} marshal\n[2] {0} pyc\n[3] {0} zlib\n[4] {0} base16\n[5] {0} base32\n[6] {0} base64\n[7] {0} hex\n[8] {0} bin\n[B] Back').format('Compile')
	print '—'*48

	try:
		choose = raw_input('[•] Choose: ')
	except (EOFError, KeyboardInterrupt):pass

	if choose in ('1', '2', '3', '4', '5', '6', '7', '8'):
		try:
			file = raw_input('[•] Input File: ')
		except Exception as exception:
			main_menu(exception)
		choose = int(choose)
		if choose == 1:
			Compile(file).marshal()
		elif choose == 2:
			Compile(file).pyc()
		elif choose == 3:
			Compile(file).zlib()
		elif choose == 4:
			Compile(file).base16()
		elif choose == 5:
			Compile(file).base32()
		elif choose == 6:
			Compile(file).base64()
		elif choose == 7:
			Compile(file).hex()
		elif choose == 8:
			Compile(file).bin()
	elif choose in ['b', 'B']:
		main_menu()
	else:
		main_menu('[!] Wrong Input')
	return


def decompile_menu():
	os.system('clear')
	print _0o0oO_.encode('cp500')
	print ('[1] {0} marshal\n[2] {0} pyc\n[3] {0} zlib\n[4] {0} base16\n[5] {0} base32\n[6] {0} base64\n[7] {0} hex\n[8] {0} bin\n[B] Back').format('Decompile')
	print '—'*48

	try:
		choose = raw_input('[•] Choose: ')
	except (EOFError, KeyboardInterrupt):pass

	if choose in ('1', '2', '3', '4', '5', '6', '7', '8'):
		try:
			file = raw_input('[•] Input File: ')
		except Exception as exception:
			main_menu(exception)
		choose = int(choose)
		if choose == 1:
			Decompile(file).marshal()
		elif choose == 2:
			Decompile(file).pyc()
		elif choose == 3:
			Decompile(file).zlib()
		elif choose == 4:
			Decompile(file).base16()
		elif choose == 5:
			Decompile(file).base32()
		elif choose == 6:
			Decompile(file).base64()
		elif choose == 7:
			Decompile(file).hex()
		elif choose == 8:
			Decompile(file).bin()
	elif choose in ['b', 'B']:
		main_menu()
	else:
		main_menu('[!] Wrong Input')
	return


if __name__ == '__main__':
	main_menu()

