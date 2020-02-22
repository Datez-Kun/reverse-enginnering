import os, sys, marshal, __builtin__ as pp, time
from base64 import *

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
logo = R+"""

 ____    ____                     __________ 
|_   \  /   _|                    \______   \\
  |   \/   |                       |    |  _/
  | |\  /| |  """+C+""" ____ ____ ____ _  _ """+R+"""|    |   \ """+C+""" _______ _______ _______"""+R+"""
 _| |_\/_| |_ """+C+""" |__| |__/ [__  |__|"""+R+""" |______  / """+C+""" |_____| |______ |______"""+R+"""
|_____||_____|"""+C+""" |  | |  \ ___] |  |"""+R+"""        \/ """+C+"""  |     | ______| |______
"""+Y+"""["""+C+"""AUTHOR """+Y+"""]"""+G+""" Bl4ck Dr460n
"""+Y+"""["""+C+""" TEAM  """+Y+"""]"""+G+""" Woll Cyber Team
"""+Y+"""["""+C+"""VERSION"""+Y+"""]"""+G+""" 1.0
"""+Y+"""["""+C+"""THANKS """+Y+"""]"""+G+""" All Member Woll Cyber Team"""


sukses = G+"\n[!] Success"
gagal = R+"\n[!] Failed"

def run(b):
	for t in b+"\n":
		sys.stdout.write(t)
		sys.stdout.flush()
		time.sleep(0.1)

def muat():
	m = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100"]
	print
	for b in m:
		sys.stdout.write(W+"\r[#] Compile "+C+b+"%")
		sys.stdout.flush()
		time.sleep(0.1)
	time.sleep(4)

def marsh():
	sc = raw_input(Y+"[?] Script > "+G)
	try:
		op = open(sc,'r').read()
	except IOError:
		print R+"[!] Script Not Found"
		sys.exit()
	ou = raw_input(Y+"[?] Output > "+G)
	muat()
	try:
		r = op.replace('\r\n', '\n')
	        r = r.replace('\r', 'n')
	        if r and r[(-1)] != '\n':
	            r = r + '\n'
	        com = pp.compile(r, '<r>', 'exec')
	        dump = marshal.dumps(com)
		sv = open(ou,"w")
		sv.write("#compile by bl4ck dr460n\n#github : https://github.com/Bl4ckDr460n\nimport marshal\nexec(marshal.loads("+repr(dump)+"))")
		sv.close()
		print sukses
	except:
		print gagal

def base():
	sc = raw_input(Y+"[?] Script > "+G)
	try:
		op = open(sc,'r').read()
	except IOError:
		print R+"[!] Script Not Found"
		sys.exit()
	ou = raw_input(Y+"[?] Output > "+G)
	muat()
	try:
		enc = b64encode(op)
		sv = open(ou,'w')
		sv.write("#compile by bl4ck dr460n\n#github : https://github.com/Bl4ckDr460n\nimport base64\nexec(base64.b64decode('''"+enc+"'''))")
		sv.close()
		print sukses
	except:
		print gagal


def mb():
	global sc
	sc = raw_input(Y+"[?] Script > "+G)
        try:
                op = open(sc,'r').read()
        except IOError:
                print R+"[!] Script Not Found"
                sys.exit()
        ou = raw_input(Y+"[?] Output > "+G)
        muat()
        try:
                r = op.replace('\r\n', '\n')
                r = r.replace('\r', 'n')
                if r and r[(-1)] != '\n':
                    r = r + '\n'
                com = pp.compile(r, '<r>', 'exec')
                dump = marshal.dumps(com)
                sv = open(ou,"w")
                sv.write("#compile by bl4ck dr460n\n#github : https://github.com/Bl4ckDr460n\nimport marshal\nexec(marshal.loads("+repr(dump)+"))")
                sv.close()
                base2()
        except:
                print gagal

def base2():
        try:
                op = open(sc,'r').read()
        except IOError:
                print R+"[!] Script Not Found"
                sys.exit()
        ou = raw_input(Y+"[?] Output > "+G)
        muat()
        try:
                enc = b64encode(op)
                sv = open(ou,'w')
                sv.write("#compile by bl4ck dr460n\n#github : https://github.com/Bl4ckDr460n\nimport base64\nexec(base64.b64decode('''"+enc+"'''))")
                sv.close()
                print sukses
        except:
                print gagal
def menu():
	os.system('clear')
	print logo
	print
	print W+"[1].Compile Marshal"
	print W+"[2].Compile Base64"
	print W+"[3].Compile Marshal ==> Base64"
	print W+"[0].Exit"
	print

if __name__ == '__main__':
	menu()
	p = raw_input(Y+"[?] Choose : "+G)
	if p == '':
		print R+"[!] Wrong Input"
		sys.exit()
	elif p == '1':
		marsh()
	elif p == '2':
		base()
	elif p == '3':
		mb()
	elif p == '0':
		print R+"Exit"
		sys.exit()
	else:
		print R+"[!] Wrong Input"
		sys.exit()

