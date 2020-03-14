# -*- coding: utf-8 -*-
# coding=utf-8
import time,os,sys, requests
import auto
import v2
import v4
import v4b
import v5
import v6
import v7
import v8
import vp
import vip
import get
import new1, new2
W = '\033[1;37m' #Putih
N = '\033[0m' # Tutup
R = '\033[1;37m\033[31m'  #Merah
G = '\033[1;32m' #Ijo
B = '\033[1;37m\033[34m' # biru
O = '\033[33m' # Kuning
C = '\033[36m' #Biru laut
K = '\x1b[1;93m' #Kuning

gr = "\x1b[00m═══════════════════════════════════"

def user():
    import requests as r
try:
    open('/data/data/com.termux/files/usr/lib/.1.txt')
    tambah = False
except:
    open('/data/data/com.termux/files/usr/lib/.1.txt', 'w').write('')
    tambah = True
    
if tambah:
    requests.get('http://Sereware56.000webhostapp.com/hitung.php?command=t')

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)

def exit():
	slowprint('\x1b[91m[!]\x1b[00m Exiting Program !')
	os.system('xdg-open https://youtube.com/saydog-official')
	os.system('exit')

logo = """
\x1b[1;32m
    ·▄▄▄ ▄▄▄·  ▄▄· ▄▄▄ .▄▄▄▄▄            ▄▄▌
    ▐▄▄·▐█ ▀█ ▐█ ▌▪▀▄.▀·•██  ▪     ▪     ██•
    ██▪ ▄█▀▀█ ██ ▄▄▐▀▀▪▄ ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪
    ██▌.▐█ ▪▐▌▐███▌▐█▄▄▌ ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌
    ▀▀▀  ▀  ▀ ·▀▀▀  ▀▀▀  ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀
           \x1b[91mFACEBOOK HACKING TOOLS\x1b[00m \033[041m PRO \033[00m
"""
def header():
	os.system('clear')
	user()
	os.system('xdg-open https://www.youtube.com/channel/UCLU9H65QrIC6u2UetU6476w')
	slowprint(logo)
	print('\x1b[1;32m   + ----=[\x1b[00m     Coded By \x1b[33mIqbalmh18\x1b[1;32m     ]=---- +')
	print('\x1b[1;32m   + ----=[\x1b[00m      Author By \x1b[33mMr.XsZ\x1b[1;32m      ]=---- +')
	print('\x1b[00m')
	slowprint('Welcome to Facebook Hacking Tools')
	slowprint('For support the Author please subscribe YouTube Channel')
	slowprint('YouTube : \x1b[1;32m\033[041m SAYDOG \033[00m')
	slowprint('YouTube : \x1b[91m\033[042m Mr.XsZ \033[00m')
	print('\x1b[00m')
	slowprint('USAGE THIS TOOLS')
	slowprint('Use command : \x1b[33mhelp')
	print('')
	main()

def main():
	bal = raw_input('\x1b[00mFace®tool \x1b[91m> \x1b[1;32m')
	if bal == '' in bal:
		main()
	elif bal == 'exit' in bal:
		exit()
	elif bal == 'token' in bal:
		tok = raw_input('\x1b[00mPaste Your Token Here : \x1b[1;32m')
		os.system('print "'+tok+'" > login.txt;cat login.txt > data/login.txt')
		os.system('sleep 2')
		slowprint('\x1b[00mSaved as \x1b[33mlogin.txt')
		slowprint('\x1b[00mBack to menu, please wait ...')
		os.system('sleep 3')
		header()
	elif bal == 'logout' in bal:
		os.system('rm login.txt;rm data/login.txt')
		slowprint('\x1b[00mLogout Session Token : \x1b[33m Success\x1b[00m')
		slowprint('\x1b[00mBack to menu, please wait ...')
		os.system('sleep 3')
		header()
	elif bal == 'update' in bal:
		print '[%s#%s] Updating  ...' % (G, N)
		os.system('git pull')
		print '%s[%s**%s]%s  was updated. \xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf' % (G, R, G, N)
		sys.exit()
	elif bal == 'help' in bal:
		print('\x1b[00m')
		print('\x1b[1;32m HELP MENU\x1b[00m')
		print'%s' % gr
		print('  %s[%s+%s] Jumlah User :%s ' + requests.get('http://Sereware56.000webhostapp.com/hitung.php').text) % (W,O,W,G)
		print('\x1b[00m╔═════════════════════════════════╗')
		print('\x1b[00m║ Command             Description ║')
		print('\x1b[00m╠═════════════════════════════════╣')
		print('\x1b[00m║ show             \x1b[91mShow all tools\x1b[00m ║')
		print('\x1b[00m║ token            \x1b[91mLogin token fb\x1b[00m ║')
		print('\x1b[00m║ logout          \x1b[91mLogout token fb\x1b[00m ║')
		print('\x1b[00m║ get                   \x1b[91mGet Token\x1b[00m ║')
		print('\x1b[00m║ update            \x1b[91mUpdate Script\x1b[00m ║')
		print('\x1b[00m║ exit               \x1b[91mExit program\x1b[00m ║')
		print('\x1b[00m╚═════════════════════════════════╝')
		print('')
		main()
	elif bal == 'get' in bal:
		get.tokenz()
	elif bal == 'show' in bal:
		print('\x1b[00m')
		os.system('xdg-open https://www.instagram.com/4N9GA')
		slowprint('Welcome to Tools Menu')
		slowprint('Choose number for running the tools')
		print'%s' % gr
		print('\x1b[1;32m 0.\x1b[1;91m Back')
		print'%s' % gr
		print('%s 1%s DarkFb %sV 1.2' % (G,W,K))
		print'%s' % gr
		print('%s 2%s DarkFb %sV 1.4' % (G,W,K))
		print'%s' % gr
		print('%s 3%s DarkFb %sV 1.4 %s (Beta)' % (G,W,K,W))
		print'%s' % gr
		print('%s 4%s DarkFb %sV 1.5' % (G,W,K))
		print'%s' % gr
		print('%s 5%s DarkFb %sV 1.6' % (G,W,K))
		print'%s' % gr
		print('%s 6%s DarkFb %sV 1.7' % (G,W,K))
		print'%s' % gr
		print('%s 7%s DarkFb %sV 1.8' % (G,W,K))
		print'%s' % gr
		print('%s 8%s DarkFb %sV 1.7 %s Premium' % (G,W,K,W))
		print'%s' % gr
		print('%s 9%s DarkFb %sV 1.7 %s Vip' % (G,W,K,W))
		print'%s' % gr
		print('%s 10%s Auto Cark ' % (G,W))
		print'%s' % gr
		print('%s 11%s Auto Brute Force %sV 0.1 %s New' % (G,W,K,W))
		print'%s' % gr
		print('%s 12%s Auto Brute Force %sV 0.2 %s New' % (G,W,K,W))
		print'%s' % gr
		print('%s 13%s Auto Hack  ' % (G,W))
		print'%s' % gr
		print('\x1b[00m')
		a = raw_input('\x1b[91m[\x1b[00mCHOOSE\x1b[91m] Number : \x1b[1;32m')
		if a == '' in a:
			header()
		if a == '0' in a:
			header()
		elif a == '1' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('sleep 2')
			os.system('xdg-open https://youtu.be/27J0GqAL78w')
			v2.login()
			header()
		elif a == '2' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('xdg-open https://youtu.be/vfbRPJn1fPE')
			os.system('sleep 2')
			v4.login()
			header()
		elif a == '3' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('xdg-open https://youtu.be/vfbRPJn1fPE')
			os.system('sleep 2')
			v4b.login()
			header()
		elif a == '4' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('sleep 2')
			os.system('xdg-open https://youtu.be/sfmLO1e6MUA')
			v5.login()
			header()
		elif a == '5' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('sleep 2')
			os.system('xdg-open https://youtu.be/sfmLO1e6MUA')
			v6.login()
			header()
		elif a == '6' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('sleep 2')
			os.system('xdg-open https://youtu.be/27J0GqAL78w')
			print "%s [%s!%s]  Akun Anda Tidak Premium " % (W,R,W)
			sys.exit()
		elif a == '7' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('sleep 2')
			os.system('xdg-open https://youtu.be/vfbRPJn1fPE')
			print "%s [%s!%s]  Akun Anda Tidak Premium " % (W,R,W)
			sys.exit()
		elif a == '8' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('sleep 2')
			os.system('xdg-open https://youtu.be/27J0GqAL78w')
			print "%s [%s!%s]  Akun Anda Tidak Premium " % (W,R,W)
			sys.exit()
		elif a == '9' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('sleep 2')
			os.system('xdg-open https://youtu.be/27J0GqAL78w')
			print "%s [%s!%s]  Akun Anda Tidak Premium " % (W,R,W)
			sys.exit()
		elif a == '10' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('sleep 2')
			os.system('xdg-open https://youtu.be/ntb_JmvtXzo')
			auto.autoBrute()
			header()
		elif a == '11' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('sleep 2')
			print "%s [%s!%s]  Akun Anda Tidak Premium " % (W,R,W)
			sys.exit()
			os.system('xdg-open https://youtu.be/ntb_JmvtXzo')
		elif a == '12' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('sleep 2')
			print "%s [%s!%s]  Akun Anda Tidak Premium " % (W,R,W)
			sys.exit()
			os.system('xdg-open https://youtu.be/ntb_JmvtXzo')
		elif a == '13' in a:
			print('\x1b[00m')
			slowprint('\033[041m RUNNING THE TOOLS \033[00m')
			slowprint('\x1b[00m Please Wait ... ')
			os.system('sleep 2')
			print "%s [%s!%s]  Akun Anda Tidak Premium " % (W,R,W)
			sys.exit()
			os.system('xdg-open https://youtu.be/ntb_JmvtXzo')
		else:
			header()
	else:
		print('\x1b[91m[!]\x1b[00m Unknown Command !')
		main()

#header()