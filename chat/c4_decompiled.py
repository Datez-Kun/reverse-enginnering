import requests,os,json,time

"""
def logs():
	global nam
	nam = raw_input("  Nama : ")
	send()

def send():
	os.system("clear")
	global name
	pesan = requests.get("https://sereware56.000webhostapp.com/chats/chat.txt").text
	print 40 * '\x1b[1;97m\xe2\x95\x90' 
	print (pesan)
	print 40 * '\x1b[1;97m\xe2\x95\x90' 
	pes = raw_input("  Pesan : " )
	requests.post("https://sereware56.000webhostapp.com/chats/index.php",data={"nam":nam, "pes":pes}).text
	send()
"""

print
class chat:
    def __init__(self):
        self.bulan={
            "1":"januari","2":"februari",
            "3":"maret","4":"april","5":"mei",
            "6":"juni","7":"juli","8":"agustus",
            "9":"september","10":"oktober",
            "11":"november","12":"desember"}
        self.path=".config.txt"
        self.server="https://sereware56.000webhostapp.com/chats/{}"
        if os.path.exists(self.path):
            if os.path.getsize(self.path) !=0:
                self.config=json.loads(open(self.path).read())
                self.send()
            else:
                self.regis()
        else:self.regis()
        
    def regis(self):
        print "	[ Create Chatroom account ]\n"
        self.name=raw_input("[?] name: ")
        if self.name =="":self.regis()
        else:
            open(self.path,"w").write(json.dumps({"name":self.name}))
            print("[+] success")
            self.config=json.loads(open(self.path).read())
            os.system("clear")
            print ("[+] opening chatroom...")
            self.send()
            
    def send(self):
        os.system("clear")
        pesan = requests.get("https://sereware56.000webhostapp.com/chats/chat.txt").text
        print 40 * '\x1b[1;97m\xe2\x95\x90' 
        print (pesan)
        print 40 * '\x1b[1;97m\xe2\x95\x90' 
        pes = raw_input("  Pesan : " )
        global name
        requests.post("https://sereware56.000webhostapp.com/chats/index.php",data={"name":self.config["name"], "pes":pes}).text
        self.send()





chat()
