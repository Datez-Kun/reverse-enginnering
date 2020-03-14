import requests,os,json,time, sys, subprocess
from getpass import getpass as click
import requests as r

from data import banner
from data import prem

#Warna
W = '\033[1;37m' #Putih
N = '\033[0m' # Tutup
R = '\033[1;37m\033[31m'  #Merah
G = '\033[1;32m' #Ijo
B = '\033[1;37m\033[34m' # biru
O = '\033[33m' # Kuning
C = '\033[36m' #Biru laut
K = '\x1b[1;93m' #Kuning

notic  = "{}{}[*]{} ".format(N,B,N)
warning = "{}[-]{} ".format(R,N)
wa = "{}[{}-{}] ".format(W,R,W)
was = "{}[{}!{}] ".format(W,R,W)
good    = "{}[!]{} ".format(G,N)
warn    = "{}[!]{} ".format(O,N)
gris = "\xe2\x95\x91".format(W,N)
pan = "{}\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90".format(W)
q = 'q'


class allq:
	def __init__(self):
		self.user()
		self.menu()
	
	def menu(self):
		os.system('clear')
		print ""
		print('  %s[%s+%s] Jumlah User :%s ' + requests.get('http://Sereware56.000webhostapp.com/hitung.php').text) % (W,O,W,G)
		print "\n"
		print "     %s{%s01%s} Daftar " % (W,G,W)
		print "     {%s02%s} Login " % (G,W)
		print "     {%s03%s} Remove Account " % (G,W)
		print "     {%s04%s} Wa " % (G,W)
		print "     {%s05%s} Update " % (G,W)
		print "     {%s00%s} Exit " % (R,W)
		print ""
		mane = raw_input('    %s%s > ' % (pan,G))
		if mane == '':
			self.menu()
		elif mane in ('1', '01'):
			self.daftar()
		elif mane in ('2', '02'):
			self.fele()
		elif mane in ('3', '03'):
			self.remov()
		elif mane in ('4', '04'):
			self.wa()
		elif mane in ('5', '05'):
			self.up()
		elif mane in ('0', '00'):
			print "%s[%s!%s] Exit " % (W,R,W)
			sys.exit()
		#self.fele()
	
	def up(self):
		print '[%s#%s] Updating  ...' % (G, N)
		os.system('git pull')
		print '%s[%s**%s]%s  was updated. \xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf' % (G, R, G, N)
	
	def wa(self):
		print ""
		print '   %s[ %sReport %s] ' % (W,G,W)
		print '\n%sReport Bug Via WhatsApp' % wa
		bug = raw_input('%sEnter your message : ' % was)
		print 42 * '\x1b[1;97m\xe2\x95\x90'
		subprocess.check_output([
		'am', 'start',
		'https://api.whatsapp.com/send?phone=6282211661007&text=Masalah : ' + bug + ''])
	
	def remov(self):
		os.system("rm .config.txt")
		print "%s[%s+%s] Account Remove " % (W,R,W)
	
	def daftar(self):
		q = raw_input('  \n%s[%s+%s] Username :%s ' % (W,G,W,G))
		z = raw_input('%s[%s~%s] Password :%s ' % (W,G,W,G))
		url = 'http://betzxs.000webhostapp.com/tai/daftar.php?user=%s&pass=%s' % (q,z)
		cek = eval(requests.get(url).text)
		print("\n%s%s" + cek['msg']) % (wa,W)
		print ""
		print '%s[%s#%s] %sSilahkan Meminta konfirmasi kepada Angga' % (G,K,G,W)
		raw_input('%s[%s^%s] %sTekan Enter Untuk Menghubungi Angga via WhatsApp...' % (G,K,G,W))
		subprocess.check_output([
		'am', 'start',
		'https://api.whatsapp.com/send?phone=6282211661007&text=konfirm%20saya%20dengan%20username : %20' + q.replace(' ', '%20') + ''])
	
	def fele(self):
		self.path=".config.txt"
		if os.path.exists(self.path):
			if os.path.getsize(self.path) !=0:
				self.config=json.loads(open(self.path).read())
				self.login()
			else:
				self.saveq()
		else:
			self.saveq()
			
	def user(self):
		import requests as r
		try:
			open('/data/data/com.termux/files/usr/lib/.1.txt')
			tambah = False
		except:
			open('/data/data/com.termux/files/usr/lib/.1.txt', 'w').write('')
			tambah = True
			
		if tambah:
			requests.get('http://Sereware56.000webhostapp.com/hitung.php?command=t')
			
			
	def regis(self):
		open(self.path,"w").write(json.dumps({"name":self.name, "pas":self.pas}))
		print("[+] success")
		self.config=json.loads(open(self.path).read())
		os.system("clear")
		print ("[+] Sedang Masuk")
		self.login()
			
	def saveq(self):
		self.name=raw_input('  \n%s[%s+%s] Username :%s ' % (W,G,W,G))
		self.pas=raw_input('%s[%s~%s] Password :%s ' % (W,G,W,G))
		save = raw_input("\n%s[%s?%s] Save Info Login ? (Y/N) "%(W,B,W))
		if save == "y" or save == "Y":
			print("Device Saved!")
			self.regis()
		elif save == "n" or save == "N":
			print("Device Not Saved!")
			data = r.get('http://betzxs.000webhostapp.com/tai/login.php?user=' + self.name + '&pass=' + self.pas).text
			#data = requests.get("http://betzxs.000webhostapp.com/tai/login.php",data={"name":self.name, "pas":self.pas}).text
			try:
				data_ = eval(data)
				print "\n" + data_['akses']
				if data_['akses'] == 'username belum disetujui':
					print(data_['akses'])
				else:
					print "\n%s[%s~%s] Akun Anda Premium" % (W,G,W) 
					click('\n[ Tekan Enter ]')
					prem.header()
			except:
				if '{' in data:
					print "\n" + data_['msg']
				else:
					print "\n%s[%s~%s] Akun Anda Tidak Premium" % (W,G,W)
					click('\n[ Tekan Enter ]')
					banner.header()
	
	def login(self):
		data = r.get('http://betzxs.000webhostapp.com/tai/login.php?user=' + self.config["name"] + '&pass=' + self.config["pas"]).text
		#data = requests.get("http://betzxs.000webhostapp.com/tai/login.php",data={"name":self.config["name"], "pas":self.config["pas"]}).text
		try:
			data_ = eval(data)
			print "\n" + data_['akses']
			if data_['akses'] == 'username belum disetujui':
				print(data_['akses'])
			else:
				print "\n%s[%s~%s] Akun Anda Premium" % (W,G,W) 
				click('\n[ Tekan Enter ]')
				prem.header()
		except:
			if '{' in data:
				print "\n" + data_['msg']
			else:
				print "\n%s[%s~%s] Akun Anda Tidak Premium" % (W,G,W)
				click('\n[ Tekan Enter ]')
				banner.header()
				
				
