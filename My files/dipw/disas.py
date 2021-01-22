import dis,types,sys,marshal,re,time

def read_file(file):
	cons = open(file).read()
	byte = marshal.loads(cons[8:])
	show_all(byte)
	
def show_all(code):
	print('\n# Disassemble At : %s\n# Method Name : %s \n# File Name : %s\n'%(time.ctime(),re.search(r'<code object (.*?) at ',repr(code)).group(1),sys.argv[1]))
	dis.disassemble(code)
	for const in code.co_consts:
		if type(const) == types.CodeType:
			show_all(const)
		else:
			pass

if __name__=="__main__":
	if len(sys.argv) < 2:
		exit('usage : disas.py <file.pyc>')
	else:
		read_file(sys.argv[1])
