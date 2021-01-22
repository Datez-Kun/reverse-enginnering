#!/../usr/bin/python2
# find password script in disassembly
import re

data = []
foko = ''
normal = []
revesr = []
fix = open('dp.dis','r').readlines()
for peko in fix:
	if 'LOAD_CONST' in peko:
		try:
			cuk = int(''.join(re.findall('LOAD_CONST.*?\((\d.+)\)',peko)))
			data.append(cuk)
		except:
			continue
	elif 'ROT_TWO' in peko:
		lesn = ''.join(chr(i) for i in data)
		normal.append(lesn)
		revesr.append(lesn[::-1])
		del data[:]
		continue
print ''.join(normal)
print '\n'
print ''.join(revesr)
