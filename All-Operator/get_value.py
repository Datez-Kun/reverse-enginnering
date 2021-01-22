import re

with open('2.dis') as f:
	print ''.join(chr(len(i)) for i in re.findall(r"LOAD_CONST.*?\('(.*?)'\)",f.read())[:-1])
