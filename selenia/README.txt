BAHASA SCRIPT : PYTHON
MODUL YANG DIPERLUKAN : CLOUDSCRAPER, REQUESTS
LANGKAH INSTALLASI
- DOWNLOAD TERMUX DI PLAYSTORE
- BUKA TERMUXNYA
- KETIKAN PERINTAH INSTALLASI BERIKUT SECARA BERGANTIAN :
"apt update && apt upgrade -y" #Berfungsi untuk update dan upgrade Termux Kalian
"apt install python / khusus vps: apt install python3" #Berfungsi untuk menginstall bahasa script yang diperlukan
"pip install --upgrade pip / khusus vps : pip3 install --upgrade pip" #Berfungsi untuk media install modul script yang diperlukan
"pip install cloudscraper" #Berfungsi menginstall modul cloudscraper || Instal modul di python3 gunakan pip3
"pip install requests" #Berfungsi menginstall modul requests || Instal modul di python3 gunakan pip3
"apt install git" #Berfungsi untuk menginstall git untuk mengambil script dari github tanpa mendownload dari browser
"termux-setup-storage"
- JIKA SUDAH MELAKUKAN INSTALLASI SEKARANG KITA DOWNLOAD SCRIPT MENGGUNAKAN PERINTAH GIT TADI
- SILAKAN ARAHKAN DULU TEMPAT MENYIMPAN SCRIPTNYA KETIKAN:
"cd /sdcard/namafolder_kalian_tempat_menyimpan_script" #Berfungsi Mengakses Memori Internal Kalian
"git clone http://github.com/layscape/selenia" #Berfungsi untuk mendownload script dari github
"cd selenia" #berfungsi untuk mengakses folder script
- SELANJUTNYA KITA RUN CONFIG DENGAN MENGETIKAN
"python bot.py"
- LAKUKAN REGISTRASI TERLEBIH DAHULU
- JIKA SUDAH KITA EDIT FILE CONFIG MENGGUNAKAN TEXT EDITOR APA SAJA (SAYA MENGGUNAKAN QUICK EDIT/NOTEPAD)
- JIKA SUDAH MENGISI CONFIG DENGAN MENYETING TRADESET,AKUN DAN LICENSE(JIKA ADA) SILAKAN RUN ULANG SCRIPTNYA
"python bot.py"
- DAN SCRIPT BISA DIGUNAKAN


1. PENJELASAN SETTING TRADESET
	"BaseTrade": INI UNTUK BASE MODAL YANG KITA MAINKAN
	"C1": INI UNTUK MENGATUR KESEMPATAN MENANG TRADING KITA NILAINYA DARI 5-95
	"C2": INI UNTUK MENGATUR KESEMPATAN MENANG TRADING KITA NILAINYA DARI 5-95
	"TradeCount": INI UNTUK MENGATUR JUMLAH TRADING YANG DILAKUKAN DALAM SATU WAKTU
	"MultiplyOnWin": INI UNTUK MENGATUR PERKALIAN TRADING JIKA MENANG > Aturan Pengisiannya adalah : 0.5 = 50%(1.5x), 1 = 100%(double atau 2x), 2 = 200% (triple atau 3x), 3 = 300% (quad atau 4x)
	"MultiplyOnLose": INI UNTUK MENGATUR PERKALIAN TRADING JIKA KALAH > Aturan Pengisiannya adalah : 0.5 = 50%(1.5x), 1 = 100%(double atau 2x), 2 = 200% (triple atau 3x), 3 = 300% (quad atau 4x)
	"MaxBaseTrade": INI UNTUK MENGATUR MAKSIMAL BASETRADE YANG MASUK SAAT TRADING
	"ClientSeed": INI UNTUK MENGATUR SEED PERHITUNGAN SAAT TRADING
2. PENJELASAN SETTING TOOLS
	"ResetOnLoseMaxTrade": INI UNTUK MENGATUR JIKA BASETRADE SUDAH MAKSIMAL MAKA AKAN DIRESET KE BASETRADE AWAL
	"StopOnLoseMaxTrade": INI UNTUK MENGATUR JIKA BASETRADE SUDAH MAKSIMAL MAKA TRADING AKAN STOP
	"TargetProfit": INI UNTUK MENGATUR JIKA TARGET PROFIT TERCAPAI TRADING AKAN STOP
	"RecoveryMultiplier": INI UNTUK MENGATUR PERKALIAN TRADING JIKA KALAH DALAM 1 SESI TRADING
	"RecoveryIncrease": INI UNTUK MENGATUR PERTAMBAHAN TRADING JIKA KALAH DALAM 1 SESI TRADING
	"AddDelayTrade": MEMBERIKAN DELAY PERTRADINGNYA DALAM HITUNGAN DETIK
	"AddDelayTradeWin": MEMBERIKAN DELAY TRADING JIKA WIN DALAM HITUNGAN DETIK
	"AddDelayTradeLose": MEMBERIKAN DELAY TRADING JIKA LOSE DALAM HITUNGAN DETIK
	"ForceTC1AfterLose": MENGUBAH TRADECOUNT MENJADI 1 KETIKA LOSE DAN BALIK SEPERTI SEMULA KETIKA WIN
	"ChangeTCAfterLose": MENGUBAH TRADECOUNT MENJADI SESUAI YANG KITA MAU KETIKA LOSE DAN BALIK SEPERTI SEMULA KETIKA WIN
	"SmartRecovery": RECOVERY AKAN TERUS MENINGKAT SAMPAI PROFIT KEMBALI SEPERTI SEMULA

ERROR YANG SERING TERJADI KETIKA MENJALANKAN SCRIPT
Error 'Payouts'/'PayIns', konsultasikan saja ke creator, ini hanya masalah salah setting config
Error 'ses', sebelum melakukan trading harap login terlebih dahulu
Error 'cloudscraper', silakan baca ulang langkah installasi
