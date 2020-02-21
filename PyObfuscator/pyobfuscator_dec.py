#!/usr/bin/python
# -*- coding: utf-8 -*-
import random, sys

def Obfuscate(body):
	obfuscated = ""
	for i in range(0, len(body)):
		if obfuscated == "":
			obfuscated += expr(ord(body[i]))
		else:
			obfuscated += "+" + expr(ord(body[i]))
	return obfuscated

def expr(char):
	range = random.randrange(1,10001)
	exp = random.randrange(0,3)
	if exp == 0:
		print "\x1b[0;37mConverting char %s =>\x1b[32;1m %s" % (str(char), str((range+char)) + "-" + str(range))
		return "chr(" + str((range+char)) + "-" + str(range) + ")"
	elif exp == 1:
		print "\x1b[0;37mConverting char %s =>\x1b[32;1m %s" % (str(char), str((char-range)) + "+" + str(range))
		return "chr(" + str((char-range)) + "+" + str(range) + ")"
	elif exp == 2:
		print "\x1b[0;37mConverting char %s =>\x1b[32;1m %s" % (str(char), str((char*range)) + "/" + str(range))
		return "chr(" + str((char*range)) + "/" + str(range) + ")"
try:
	print ("""\x1b[30;1m╔═══════════════════════════════════════════════════════════════╗
║\x1b[31;1m ____         ___  _      __                     _             \x1b[30;1m║
║\x1b[31;1m|  _ \ _   _ / _ \| |__  / _|_   _ ___  ___ __ _| |_ ___  _ __ \x1b[30;1m║
║\x1b[31;1m| |_) | | | | | | | '_ \| |_| | | / __|/ __/ _` | __/ _ \| '__|\x1b[30;1m║
║\x1b[0;37m|  __/| |_| | |_| | |_) |  _| |_| \__ \ (_| (_| | || (_) | |   \x1b[30;1m║
║\x1b[0;37m|_|    \__, |\___/|_.__/|_|  \__,_|___/\___\__,_|\__\___/|_|   \x1b[30;1m║
║\x1b[0;37m       |___/                                                   \x1b[30;1m║
╠═══════════════════════════════════════════════════════════════╣\033[30;1m
║\x1b[0;37m➢ \x1b[34;1mAuthor : \x1b[0;37mFebry [ xNot_Found ]                                \x1b[30;1m║
║\x1b[0;37m➣ \x1b[34;1mContact: \x1b[0;37m+62823-8637-2115                                    \x1b[30;1m║
║\x1b[0;37m➢ \x1b[34;1mEmail  : \x1b[0;37mfebryafriansyah@programmer.net                      \x1b[30;1m║
║\x1b[0;37m➣ \x1b[34;1mWebsite: \x1b[0;37mhttp://hatakecnk.ueuo.com                           \x1b[30;1m║
║\x1b[0;37m➢ \x1b[34;1mGithub : \x1b[0;37mhttps://github.com/hatakecnk                        \x1b[30;1m║
╚═══════════════════════════════════════════════════════════════╝\x1b[0;37m""")
	a = raw_input('\033[0;37m┌─[\033[31;1m Input Your File Path (\x1b[32;1mex: /sdcard/ex.py\x1b[31;1m) \033[0;37m]\n\033[0;37m└─[\033[31;1m$\033[0;37m]> \033[33;1m')
	print ('')
	b = open(a).read()
	z = a.replace('.py', '-obfuscated.py')
	m = open(z, 'w')
	m.write("x=("+Obfuscate(b)+");exec(x)")
	print '\n\x1b[31;1m[\x1b[0;37m+\x1b[31;1m]\x1b[0;37m File saved as\x1b[32;1m %s' % z
except KeyboardInterrupt:
	print ('\n\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m ctrl+c detected')
	print ('\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m exit from program')
	sys.exit()
except EOFError:
	print ('\n\n\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m ctrl+d detected')
	print ('\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m exit from program')
	sys.exit()
except IOError:
	print ('\n\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m file not found')
	print ('\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m exit from program')
	sys.exit()
except:
	print ('\n\x1b[31;1m[\x1b[0;37m!\x1b[31;1m]\x1b[0;37m Exit')
	sys.exit()
