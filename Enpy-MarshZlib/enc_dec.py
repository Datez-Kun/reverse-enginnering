# -*- coding: utf-8 -*-
import marshal, zlib, sys, os
B = '\x1b[34;1m'
R = '\x1b[31;1m'
G = '\x1b[32;1m'
W = '\x1b[0m'
Y = '\x1b[33;1m'
counter = 0
def banner():
    print """ \x1b[31;5m┏━┳━┓░░░░░░░┏━┓┏┓░░░░░░░░────┏━━┓░░░┏┓┏┓░
 ┃┃┃┃┃┏━┓░┏┳┓┃━┫┃┗┓┏━┓░┏┓░╔══╗┣━━┃┏┓░┣┫┃┗┓     
 \x1b[39;5m┃┃┃┃┃┃╋┗┓┃┏┛┣━┃┃┃┃┃╋┗┓┃┗┓╚══╝┃━━┫┃┗┓┃┃┃╋┃
 ┗┻━┻┛┗━━┛┗┛░┗━┛┗┻┛┗━━┛┗━┛────┗━━┛┗━┛┗┛┗━┛    
╔═════════════════════════════════════════╗
 \x1b[31;5mAuthor : \x1b[39;3mFebry [ xNot_Found ]\x1b[0;37m
 \x1b[31;5mGithub : \x1b[39;3mhttps://github.com/hatakecnk\x1b[0;37m\x1b[39;5m
╚═════════════════════════════════════════╝"""
try:
    banner()
    file = raw_input('\033[0;37m┌─[\033[31;1m Input Your File Path (\x1b[39;5m/sdcard/ex.py\x1b[31;1m) \033[0;37m]\n\033[0;37m└─[\033[31;1m$\033[0;37m]> \033[36;1m')
    count = int(raw_input('\033[0;37m┌─[\033[31;1m Count Encrypt (\x1b[39;5mmax 400\x1b[31;1m) \033[0;37m]\n\033[0;37m└─[\033[31;1m$\033[0;37m]> \033[36;1m'))
except IndexError:
    print R + '\n[' + W + '!' + R + '] ' + W + 'there is an error'
    sys.exit()
except KeyboardInterrupt:
    print R + '\n[' + W + '!' + R + '] ' + W + 'ctrl+c detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
    sys.exit()
except EOFError:
	print R + '\n\n[' + W + '!' + R + '] ' + W + 'ctrl+d detected'
	print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
	sys.exit()
except ValueError:
	print R + '\n[' + W + '!' + R + '] ' + W + 'input count!'
	print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
	sys.exit()
	
if count < 400:
	try:
	    fileopen = open(file).read()
	except IOError:
	    banner()
	    print R + '\n[' + W + '!' + R + '] ' + W + 'file not exist'
	    sys.exit()
	try:
	    a = compile(fileopen, 'dg', 'exec')
	    b = marshal.dumps(a)
	    c = zlib.compress(b)
	except Exception as f:
	    banner()
	    print R + '[' + W + '!' + R + '] ' + W + f
	    sys.exit()
	d = ('#Encrypted By xNot_Found\n#Github : https://github.com/hatakecnk/\n#Do Not Edit The Script To Avoid Errors\nimport marshal, zlib\nexec(marshal.loads(zlib.decompress('+repr(c) +')))')
	e = file.replace('.py', '_enc.py')
	f = open(e, 'w')
	f.write(d)
	f.close()
	while True:
		if count >= counter:
			try:
				fileopen = open(e).read()
			except IOError:
				banner()
				print R + '\n[' + W + '!' + R + '] ' + W + 'file not exist'
				sys.exit()
			try:
				a = compile(fileopen, 'dg', 'exec')
				b = marshal.dumps(a)
				c = zlib.compress(b)
			except Exception as f:
				banner()
				print R + '[' + W + '!' + R + '] ' + W + f
				sys.exit()
			d = ('#Encrypted By xNot_Found\n#Github : https://github.com/hatakecnk/\n#Do Not Edit The Script To Avoid Errors\nimport marshal, zlib\nexec(marshal.loads(zlib.decompress('+repr(c) +')))')
			e = file.replace('.py', '_enc.py')
			f = open(e, 'w')
			f.write(d)
			f.close()
			counter += 1
		else:
			break
banner()
print B + '\n[' + W + '+' + B + '] ' + G + 'file saved : \x1b[39;5m' + e
