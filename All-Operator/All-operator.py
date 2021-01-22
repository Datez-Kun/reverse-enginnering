# Filename : dg
# Python Bytecode : 2.7
# Time Succses Decompiled : Sun Sep  6 10:22:33 2020
# Timestamp In Code : 2020-04-09 09:07:32
TselOpok = [
 '118.97.159.51:443']
Ilmupedia = ['118.98.95.99:443']
Gamemax = ['118.98.95.120:443']
TselRguru = ['video-cdn.quipper.com:443', 'rg-video.ruangguru.com:443']
TselMaxtream = ['118.98.93.91:443', '118.98.93.65:443']
Isat_Edu = ['video-cdn.quipper.com:443 ', 'rg-video.ruangguru.com:443']
Xl3apk = ['127.0.0.1:9090']
Xlrguru = ['video-cdn.quipper.com:443']
Xlunliturubo = ['iflix-videocdn-p1.akamaized.net', 'iflix-videocdn-p2.akamaized.net', 'iflix-videocdn-p3.akamaized.net', 'iflix-videocdn-p6.akamaized.net', 'iflix-videocdn-p7.akamaized.net', 'iflix-videocdn-p8.akamaized.net', 'video.iflix.com:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
XlIflix = ['iflix-videocdn-p1.akamaized.net', 'iflix-videocdn-p2.akamaized.net', 'iflix-videocdn-p3.akamaized.net', 'iflix-videocdn-p6.akamaized.net', 'iflix-videocdn-p7.akamaized.net', 'iflix-videocdn-p8.akamaized.net', 'video.iflix.com:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Axis3apk = ['127.0.0.1:9090']
AxisRg = ['video-cdn.quipper.com:443', 'rg-video.ruangguru.com:443']
AxisGaming = ['cdn2-prod-cfn.akamaized.net:443']
AxiGame2 = ['iflix-videocdn-p1.akamaized.net']
AxisSosmed = ['23.45.116.48:443', '23.219.184.41:443', '202.111.47.99:443']
Smart = ['video-cdn.quipper.com:443', 'rg-video.ruangguru.com:443']
import itertools, urllib2, os, sys, time, random, socket, select, datetime, threading
from os import system, name
os.system('clear')
version = '2.2.4 '
expired = ['15', '09', '2020']
buffer_size = 99999
logo = ' \x1b[1;31m\xf0\x9f\x98\xad SCRIPT UDAH KADALUWARSA MBAH.. \n \x1b[1;36m\xf0\x9f\x99\x8f TUNGGU UPDATENYA SELANJUTNYA \xf0\x9f\x91\x8d \n \x1b[1;33m\xf0\x9f\x91\x89 JANGAN LUPA DUKUNG TERUS \xf0\x9f\x92\xaa \n \x1b[1;32m\xf0\x9f\x94\xb4 YOUTUBE ARIS STYA CHANNEL \xe2\x9e\xb0 \n \x1b[1;35m\xf0\x9f\x94\xa5 SALAM SEJAHTERA \xf0\x9f\x9a\xa9\xf0\x9f\x9a\xa9 \n\n'
host = '127.0.0.1'
port = '8080'

def connecting():
    while True:
        waktu = datetime.datetime.now().strftime('%H:%M:%S')
        try:
            time.sleep(0.01)
            sys.stdout.write('\r\x1b[37;1m[' + waktu + ']\x1b[35;1m\xe2\x96\xb6SCRIPT \x1b[33;1mMENGHUBUNGKAN \x1b[31;1m_________ ')
            sys.stdout.flush()
            break
        except:
            sys.exit()


def connected():
    while True:
        waktu = datetime.datetime.now().strftime('%H:%M:%S')
        try:
            time.sleep(0.01)
            sys.stdout.write('\r\x1b[36;1m[' + waktu + ']\x1b[37;1m\xe2\x96\xb6SCRIPT \x1b[31;1mMENGHUBUNGKAN \x1b[32;1mCONNECTED ')
            sys.stdout.flush()
            break
        except:
            sys.exit()


def connection_error():
    while True:
        waktu = datetime.datetime.now().strftime('%H:%M:%S')
        try:
            time.sleep(0.02)
            sys.stdout.write('\r\x1b[35;1m[' + waktu + ']\x1b[31;1m CONNECTION \x1b[33;1mLAGI \x1b[37;1mEROR\x1b[0m')
            sys.stdout.flush()
            break
        except:
            sys.exit()


def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.006)


def spin():
    try:
        L = '/-\\-/\\|'
        for q in range(400):
            time.sleep(0.01)
            sys.stdout.write('\r\n\x1b[1;36m \xf0\x9f\x99\x8f HALLO SUHU \xf0\x9f\x92\xaa\x1b[1;37m(' + L[(q % len(L))] + ') ')
            sys.stdout.flush()

    except:
        exit()


spin()

def mengetik_pelan(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.0)


def load():
    load = [
     '\x1b[1;31mTUNGGU DULU \x1b[1;32m>---------10%', '\x1b[1;33mTUNGGU DULU \x1b[1;34m>>-------- 20%', '\x1b[1;35mTUNGGU DULU \x1b[1;36m>>>------- 30%', '\x1b[1;37mTUNGGU DULU \x1b[1;31m>>>>------ 40%', '\x1b[1;32mTUNGGU DULU \x1b[1;33m>>>>>----- 50%', '\x1b[1;34mTUNGGU DULU \x1b[1;35m>>>>>>---- 60%', '\x1b[1;36mTUNGGU DULU \x1b[1;37m>>>>>>>--- 70%', '\x1b[1;31mTUNGGU DULU \x1b[1;32m>>>>>>>>-- 80%', '\x1b[1;33mTUNGGU DULU \x1b[1;34m>>>>>>>>>- 90%', '\x1b[1;32m\xf0\x9f\x92\x91 AKU SAYANG KAMU 100% \n\n']
    for o in load:
        print '\r\t' + o,
        sys.stdout.flush()
        time.sleep(0.05)


def loader():
    loader = [
     '\x1b[94m ']
    for o in loader:
        print '\r\t' + o,
        sys.stdout.flush()
        time.sleep(0.009)


def login():
    os.system('clear')
    from datetime import datetime
    saat_ini = datetime.now()
    tgl = saat_ini.strftime('%d')
    bln = saat_ini.strftime('%m')
    thn = saat_ini.strftime('%Y')
    tanggal = thn + bln + tgl
    exp = expired[2] + expired[1] + expired[0]
    if tanggal >= exp:
        print colors(('\n').join(['' + logo + '']))
        print colors(('\n').join(['\x1b[1;37m\xf0\x9f\x94\xb6 SILAHKAN CEK YT ARIS SETYA CHANNEL \xf0\x9f\x91\x88 ']))
        sys.exit()
    else:
        main()


def header():
    os.system('clear')
    mengetik(colors(('\n').join([
     ' '])))


def headerx():
    os.system('clear')
    mengetik(colors(('\n').join([
     ' '])))


def isi():
    mengetik(colors(('\n').join(['',
     '\x1b[1;37m \xf0\x9f\x94\xa5 SCRIP ALL OPERATOR EXP 15-09-2020 \xf0\x9f\x9a\xa9',
     '\x1b[1;36m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90 \n',
     '\x1b[1;33m \xf0\x9f\x91\x89 TRIAL DULU POPONYA YA.. \xf0\x9f\x92\xaa',
     '\x1b[1;34m \xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac \n',
     ' \x1b[1;31m\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x84\xe2\x96\x80 \xe2\x96\x84\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x84\xe2\x96\x91\xe2\x96\x84\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\x1b[1;31m\xe3\x85\xa4\x1b[1;31m\xe3\x85\xa4',
     ' \x1b[1;37m\xe2\x96\x88\xe2\x96\x91\xe2\x96\x88\xe2\x96\x91\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x91 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x88\xe2\x96\x91\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\x1b[1;31m\xe3\x85\xa4\x1b[1;31m\xe3\x85\xa4',
     ' \x1b[1;37m\xe2\x96\x91\xe2\x96\x80\xe2\x96\x91\xe2\x96\x80\xe2\x96\x91 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x91\xe2\x96\x80 \xe2\x96\x91\xe2\x96\x80\xe2\x96\x91 \xe2\x96\x80\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\x1b[1;31m\xe3\x85\xa4\x1b[1;31m\xe3\x85\xa4',
     '\x1b[1;32m  \xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97',
     '  \xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3\xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3 \xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x9d',
     '  \xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\xa9 \xe2\x95\xa9 \xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\xa9  \xe2\x95\xa9  ',
     '\x1b[1;35m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m01\x1b[1;31m] \x1b[1;37mTELKOMSEL OPOK        \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m02\x1b[1;31m] \x1b[1;37mTELKOMSEL IP/BELAJAR  \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m03\x1b[1;31m] \x1b[1;37mTELKOMSEL GAMEMAX     \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m04\x1b[1;31m] \x1b[1;37mTELKOMSEL RUANGGURU   \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m05\x1b[1;31m] \x1b[1;37mTELKOMSEL MAXTREAM    \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m06\x1b[1;31m] \x1b[1;37mINDOSAT EDUKASI M3    \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m07\x1b[1;31m] \x1b[1;37mXL RG 3APK            \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m08\x1b[1;31m] \x1b[1;37mXL RUANGGURU          \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m09\x1b[1;31m] \x1b[1;37mXL UNLI TURBO         \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m10\x1b[1;31m] \x1b[1;37mXL IFLIX              \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m11\x1b[1;31m] \x1b[1;37mAXIS EDUKASI 3APK     \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m12\x1b[1;31m] \x1b[1;37mAXIS EDUKASI RG       \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m13\x1b[1;31m] \x1b[1;37mAXIS GAMING           \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m14\x1b[1;31m] \x1b[1;37mAXIS GAMING V.2       \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m15\x1b[1;31m] \x1b[1;37mAXIS SOSMED           \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m15\x1b[1;31m] \x1b[1;37mSMART BELAJAR         \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;31m[\x1b[1;32m00\x1b[1;31m] \x1b[1;31mKLUAR                 \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n',
     '\x1b[1;31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\x1b[1;37m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;36m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;35m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;33m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;33m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;37m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;31m\xe2\x95\x97',
     '\x1b[1;37m\xe2\x95\x91 \xf0\x9f\x91\x86 PILIH SAWER PAKETNYA : \x1b[1;36m\xe2\x95\x91',
     '\x1b[1;33m\xe2\x95\x91                           \xe2\x95\x91',
     '\x1b[1;34m\xe2\x95\x91 \xe2\x96\xb6\x1b[1;37m SETING PSIPHONYA \xf0\x9f\x91\x87     \x1b[1;35m\xe2\x95\x91',
     '\x1b[1;35m\xe2\x95\x91\x1b[1;36m\xe3\x80\x98 \x1b[1;37mHOST \x1b[1;35m\xe2\x96\xa3 \x1b[1;32m127.0.0.1 \x1b[1;36m\xe3\x80\x99     \x1b[1;32m\xe2\x95\x91',
     '\x1b[1;36m\xe2\x95\x91\x1b[1;36m\xe3\x80\x98 \x1b[1;37mPORT \x1b[1;35m\xe2\x96\xa3 \x1b[1;32m8080      \x1b[1;36m\xe3\x80\x99     \x1b[1;33m\xe2\x95\x91',
     '\x1b[1;37m\xe2\x95\x9a\xe2\x95\x90\x1b[1;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;35m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;36m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;33m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;37m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;32m\xe2\x95\x90\xe2\x95\x90\x1b[1;31m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;36m\xe2\x95\x9d\n',
     '\x1b[1;33m \xe2\x9c\xac \x1b[1;37mUPLOAD BY ARIS STYA CHANNEL \x1b[1;33m\xe2\x9c\xac ',
     '\x1b[1;31m \xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac'])))


def main():
    os.system('clear')
    from datetime import datetime
    saat_ini = datetime.now()
    tgl = saat_ini.strftime('%d')
    bln = saat_ini.strftime('%m')
    thn = saat_ini.strftime('%Y')
    tanggal = thn + bln + tgl
    exp = expired[2] + expired[1] + expired[0]
    if float(tanggal) + 1 == float(exp):
        headerx()
    else:
        header()
    load()
    loader()
    isi()
    inject(host, port).start()


def real_path(file_name):
    return os.path.dirname(os.path.abspath(__file__)) + file_name


def filter_array(array):
    for i in range(len(array)):
        array[i] = array[i].strip()
        if array[i].startswith('#'):
            array[i] = ''

    return [ x for x in array if x ]


def colors(value):
    patterns = {'R1': '\x1b[31;1m', 'R2': '\x1b[31;2m', 'G1': '\x1b[32;1m', 'Y1': '\x1b[33;1m', 
       'P1': '\x1b[35;1m', 'CC': '\x1b[1;34m', 
       'B1': '\x1b[34;1m', 'L1': '\x1b[36;1m'}
    for code in patterns:
        value = value.replace(('[{}]').format(code), patterns[code])

    return value


lock = threading.RLock()
os.system('cls' if os.name == 'nt' else 'clear')

class inject(object):

    def __init__(self, inject_host, inject_port):
        super(inject, self).__init__()
        self.inject_host = str(inject_host)
        self.inject_port = int(inject_port)

    def start(self):
        try:
            print '\x1b[1;37m '
            pilih = raw_input('\xf0\x9f\x91\x89 NOMER PAKET TULIS SINI : \x1b[1;36m')
            if pilih == '0' or pilih == '00':
                print colors(('\n').join(['\t\n\x1b[1;33m\xf0\x9f\x91\x8b Selamat jalan']))
                sys.exit()
            elif pilih == '' or pilih == '':
                frontend_domains = abc
            elif pilih == '000' or pilih == '000':
                frontend_domains = abcd
            elif pilih == '222' or pilih == '002':
                frontend_domains = abc
            elif pilih == '851' or pilih == '0851':
                frontend_domains = abcd
            else:
                if pilih == '864' or pilih == '864':
                    frontend_domains = abc
                elif pilih == '753' or pilih == '964':
                    frontend_domains = abcd
                elif pilih == '847' or pilih == '963':
                    frontend_domains = abc
                elif pilih == '1' or pilih == '01':
                    frontend_domains = TselOpok
                elif pilih == '2' or pilih == '02':
                    frontend_domains = Ilmupedia
                else:
                    if pilih == '3' or pilih == '03':
                        frontend_domains = Gamemax
                    elif pilih == '4' or pilih == '04':
                        frontend_domains = TselRguru
                    elif pilih == '5' or pilih == '05':
                        frontend_domains = TselMaxtream
                    elif pilih == '6' or pilih == '06':
                        frontend_domains = Isat_Edu
                    elif pilih == '7' or pilih == '07':
                        frontend_domains = Xl3apk
                    else:
                        if pilih == '8' or pilih == '08':
                            frontend_domains = Xlrguru
                        elif pilih == '9' or pilih == '09':
                            frontend_domains = Xlunliturubo
                        elif pilih == '10':
                            frontend_domains = XlIflix
                        elif pilih == '11':
                            frontend_domains = Axis3apk
                        elif pilih == '12':
                            frontend_domains = AxisRg
                        elif pilih == '13':
                            frontend_domains = AxisGaming
                        elif pilih == '14':
                            frontend_domains = AxiGame2
                        elif pilih == '15':
                            frontend_domains = AxisSosmed
                        elif pilih == '16':
                            frontend_domains = AxisSosmed
                        elif pilih == '17':
                            frontend_domains = Smart
                            try:
                                frontend_domains = open(real_path('/bug.ini')).readlines()
                            except IOError as err:
                                make_file = open('/sdcard/qpython/scripts/bug.ini', 'w')
                                make_file.write('')
                                print ('\x1b[31;1meror: {}').format(err)
                                print '\x1b[32;1mdown'
                                sys.exit()

                        else:
                            print colors(('\n').join(['\n\x1b[1;37m\xf0\x9f\x98\x88 PILIHAN SALAH YANK']))
                            sys.exit()
                            frontend_domains = filter_array(frontend_domains)
                        if len(frontend_domains) == 0:
                            return
                    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket_server.bind((self.inject_host, self.inject_port))
                    socket_server.listen(1)
                    while True:
                        waktu = datetime.datetime.now().strftime('%H:%M:%S')
                        try:
                            time.sleep(0.1)
                            sys.stdout.write('\r ')
                            sys.stdout.write('\r\n\n \x1b[37;1m \xf0\x9f\x99\x8c START PSIPHONYA \xf0\x9f\x98\x81\n \x1b[32;1m \xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\n\n')
                            sys.stdout.flush()
                            break
                        except:
                            sys.exit()

                while True:
                    socket_client, _ = socket_server.accept()
                    socket_client.recv(buffer_size)
                    domain_fronting(socket_client, frontend_domains).start()

        except Exception as exception:
            print '\n \x1b[31;1m\xf0\x9f\x99\x85 Hpus data apk lalu masuk lgi ya !! '


class domain_fronting(threading.Thread):

    def __init__(self, socket_client, frontend_domains):
        super(domain_fronting, self).__init__()
        self.frontend_domains = frontend_domains
        self.socket_tunnel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client = socket_client
        self.buffer_size = buffer_size
        self.daemon = True

    def handler(self, socket_tunnel, socket_client, buffer_size):
        sockets = [
         socket_tunnel, socket_client]
        timeout = 0
        while True:
            timeout += 1
            socket_io, _, errors = select.select(sockets, [], sockets, 3)
            if errors:
                break
            if socket_io:
                for sock in socket_io:
                    try:
                        data = sock.recv(buffer_size)
                        if not data:
                            break
                        elif sock is socket_client:
                            socket_tunnel.sendall(data)
                        elif sock is socket_tunnel:
                            socket_client.sendall(data)
                        timeout = 0
                    except:
                        break

            if timeout == 30:
                break

    def run(self):
        try:
            self.proxy_host_port = random.choice(self.frontend_domains).split(':')
            self.proxy_host = self.proxy_host_port[0]
            self.proxy_port = self.proxy_host_port[1] if len(self.proxy_host_port) >= 2 and self.proxy_host_port[1] else '80'
            connecting()
            self.socket_tunnel.connect((str(self.proxy_host), int(self.proxy_port)))
            self.socket_client.sendall('HTTP/1.1 200 OK\r\n\r\n')
            self.handler(self.socket_tunnel, self.socket_client, self.buffer_size)
            self.socket_client.close()
            self.socket_tunnel.close()
            connected()
        except:
            connection_error()


if __name__ == '__main__':
    login()
