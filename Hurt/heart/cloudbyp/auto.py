# coding=utf-8
import os
import marshal
import zlib
import base64
import time
import sys
from time import sleep as waktu

m='\033[0;31m'
a='\033[1;30m'
k='\033[1;33m'
h='\033[0;32m'
bm='\033[0;36m'
bt='\033[0;34m'
p='\033[1;37m'

def mars():
		try:
			file = open(raw_input(bt+'╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n┃'+bt+'['+p+'➸'+bt+']'+p+'File Path '+bt+'» '+p)).read().splitlines()
			met = raw_input(bt+'┃['+p+'➸'+bt+']'+p+'File Outp '+bt+'» '+p)
			oh = raw_input(bt+'┃['+p+'➸'+bt+']'+p+'Count Dec'+bt+'» '+p)
			jumlah = int(oh)
			angka = 1
			for var in range(jumlah):
				if 'marshal.loads' in ''.join(file):
					file = filter(lambda x: "exec" in x and "(" in x, file)[0].replace('exec', 'x = ')
				else:
					file = open(met).read()
				sc = """from sys import stdout
import marshal, base64, zlib
from decompyle3.main import decompile
""" + file + """
try:
	decompile (3.8,x,stdout)
except:
	print(x)"""
				open('out.py', 'w').write(sc)
				os.system('python out.py > ' + met)
#				os.system('cat '+met)
				file = open(met).read().splitlines()
				print bt+'┃['+p+'➸'+bt+']'+p+'Decompile At \033[0;37m\xe2\x9e\xa4\033[1;33m ' + str(angka)
				if angka == jumlah:
					os.system('cat ' + met)
					print bt+'\n┃['+p+'➸'+bt+']'+p+'File Saved As \033[0;37m\xe2\x9e\xa4\xe2\x9e\xa4 \033[1;30m[\033[1;37m\xc2\xbb\033[1;32m%s\033[1;37m\xc2\xab\033[1;30m]\033[1;37m!' % met
					os.remove('out.py')
					ask = raw_input(bt+'┃['+p+'➸'+bt+']'+p+'Decompile Again Gan? [y/t] '+bt+'\n╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━➤')
					if ask == 'y' or ask == 'Y':
						waktu(0.2)
						mars()
					elif ask == 't' or ask == 'T':
						waktu(0.2)
						sys.exit()
					else:
						print(bt+'╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗'+bt+'\n┃['+p+'➸'+bt+']'+p+'Wrong Input.....'+m+'!!!                     '+bt+'┃')
						ask = raw_input(bt+'┃['+p+'➸'+bt+']'+p+'Press Enter To Back....'+m+'!!!              '+bt+'┃'+bt+'\n╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝')
						waktu(0.2)
						sys.exit()
					break
				angka += 1
		except IOError:
			print(bt+'┃['+p+'➸'+bt+']'+p+'File Not Found..........'+m+'!!!')
			ask = raw_input(bt+'┃['+p+'➸'+bt+']'+p+'Press Enter To Back ...!!\n'+bt+'╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝')
			waktu(0.2)
			exit()
		except EOFError:
			sys.exit()
		except ValueError:
			print (bt+'┃['+p+'➸'+bt+']'+p+'Jumlah Dec Harus Berupa Angka '+bt+'!!!!')
			raw_input(bt+'┃['+p+'➸'+bt+']'+p+'Press Enter To Back ...!!\n'+bt+'╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝')
			waktu(0.5)
			exit()


if __name__ == '__main__':
	mars()
