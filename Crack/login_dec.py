# Decompile At :  Thu Mar  5 23:59:04 2020
import os, time
os.system('clear')
print "Login Script"

import getpass, os

CorrectUsername = "me"
CorrectPassword = "hacker" 

loop = 'true'
while (loop == 'true'):

    username = raw_input("Please enter your username: ")

    if (username == CorrectUsername):
        loop1 = 'true'
        while (loop1 == 'true'):
            password = getpass.getpass("Please enter your password: ")
            if (password == CorrectPassword):
                print "Logged in successfully as " + username + password
                loop = 'false'
                loop1 = 'false'
                time.sleep(2)
                os.system('sh v2.sh')
            else:
                print "Password incorrect!"

    else:
        print "Username incorrect!"