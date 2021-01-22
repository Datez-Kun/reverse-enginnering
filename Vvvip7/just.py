# Just Get code object and return save to bytecode
# © Datez-Kun 2020
# (love-love) is kyun-kyun （´ω｀♡%）
import types
import sys
import marshal

def JustObj(bytecode):
	sis = marshal.loads(open(bytecode,'rb').read()[16:])
	for pico in sis.co_consts:
		if type(pico) == types.CodeType:
			file = str(pico).split()[2]
			open(f'{file}.pyc','wb').write(b'U\r\r\n\x00\x00\x00\x002\xb7\xf4^\xfa\x03\x0c\x00' + marshal.dumps(pico))
			print(f'[^] Object {file} Saved to {file}.pyc')
		else:
			continue

if __name__=="__main__":
	JustObj(sys.argv[1])
