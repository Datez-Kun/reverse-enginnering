#!/bin/bash
clear
bi="\033[1m"
u="\033[4m"
o="\033[30m"
r="\033[31m"
i="\033[32m"
bu="\033[34m"
me="\033[35m"
c="\033[36m"
pu="\033[37m"
endc="\033[0m"
enda="\033[0m"
blue="\033[1;34m"
cy="\033[1;36m"
red="\033[1;31m"
R='\x1b[1;31m'
G='\x1b[1;32m'
B='\x1b[1;34m'
Y='\x1b[1;33m'
C='\x1b[1;36m'
D='\x1b[0m'
endc='\E[0m'
enda=''
echo
echo $me"╭━━━━━━━╮"$cy "╔════════════════════════╗"
echo $me"┃$pu ● ══$me  ┃"$cy "║$bi ELCei Tool Hacking$cy     ║"$me "██████████████"
echo $me"┃$pu███████$me┃"$cy "║$i Gunakan Dengan Bijak$cy   ║"$me "██████████████"
echo $me"┃$pu███████$me┃"$cy "║$me Author Tidak Bertang-$cy  ║"$pu "██████████████"
echo $me"┃$pu███████$me┃"$cy "║$pu gung Jawab Atas Semua$cy  ║"$pu "██████████████"
echo $me"┃$pu███████$me┃"$cy "║$pur Hal Yang Terjadi$cy       ║"
echo $me"┃$pu███████$me┃"$cy "╚════════════════════════╝"$pu "INDONESIAN$me HACKER$pu RULES"
echo $me"┃$pu███████$me┃"
echo $me"┃$pu███████$me┃"$pur "╔════════════════════════╗"
echo $me"┃$pu███████$me┃"$pur "║$pu Create : 2/11/2018 $pur    ║"
echo $me"┃$pu   ○$me   ┃"$pur "║$pu Author : Nubz   $pur       ║"
echo $me"╰━━━━━━━╯"$pur "╚════════════════════════╝"
echo
sleep 3
echo $me"╔════════════════════════╗"$cy "╔════════════════════════╗"
echo $me"║$pu Sebelum login tools$me    ║"$cy "║$me Username & Password$cy    ║"
echo $me"║$pu silahkan download user$me ║"$cy "║$me Tools lama sudah tidak$cy ║"
echo $me"║$pu & pass terlebih dahulu$me ║"$cy "║$me berlaku / sudah di-$cy    ║"
echo $me"║$bi Buat yang baru memakai$me ║"$cy "║$me update.$i Jadi, diharap-$cy ║"
echo $me"║$bi harap instal bahan agar$me║"$cy "║$i kan untuk mendownload$cy  ║"
echo $me"║$bi tidak terjadi error di-$me║"$cy "║$i Username & Password$cy    ║"
echo $me"║$bi saat menjalankan tools$me ║"$cy "║$i yang baru. Thanks. >_<$cy ║"
echo $me"╚════════════════════════╝"$cy "╚════════════════════════╝"
sleep 2
echo $pu"╔═════════════════════╗"
echo $pu"║$i JANGAN LUPA BERIKAN$pu ║"
echo $pu"║$i STAR GITHUB Nubz $pu   ║"
echo $pu"╚═════════════════════╝"
echo
sleep 1
echo $i"╔═══╗"$bi"╔═════════════╗"
echo $i"║$pu 1$i ║"$bi"║$pu Login Tools$bi ║"
echo $i"╚═══╝"$bi"╚═════════════╝"
echo $i"╔═══╗"$bi"╔══════════════════════╗"
echo $i"║$pu 2$i ║"$bi"║$pu Register with facebook$bi ║"
echo $i"╚═══╝"$bi"╚══════════════════════╝"
echo $i"╔═══╗"$bi"╔══════════════════════╗"$i "╔════════════════════════╗"
echo $i"║$pu 3$i ║"$bi"║$pu Register with Gmail $bi ║"$i "║$pu If register facebook checkpoint$i ║"
echo $i"╚═══╝"$bi"╚══════════════════════╝"$i "╚════════════════════════╝"
echo $i"╔═══╗"$bi"╔═══════════════╗"
echo $i"║$pu 4$i ║"$bi"║$pu Install Bahan$bi ║"
echo $i"╚═══╝"$bi"╚═══════════════╝"
echo $i"╔═══╗"$bi"╔════════════════════════╗"
echo $i"║$pu 5$i ║"$bi"║$pu Beri STAR github Nubz $bi ║"
echo $i"╚═══╝"$bi"╚════════════════════════╝"
echo
echo $bi"╔═══$pu Choose$bi ════"
read -p "╚═══════════════➢➢ " pil
if [ $pil = '1' ]
then
python2 login.py
fi
if [ $pil = '2' ]
then
python2 logfb.py
fi
if [ $pil = '3' ]
then
python2 logmail.py
fi
if [ $pil = '4' ]
then
cd install
python2 install.py
fi
if [ $pil = '5' ]
then
echo $i"TERIMAKASIH BANYAK TELAH MELUANGKAN WAKTU UNTUK MEMBERIKAN STAR GITHUB ELCei"
sleep 3
echo $i"SILAHKAN BUKA BROWSER ANDA, LALU TEKAN STAR DI GITHUB ELCei"
sleep 3
xdg-open https://github.com/LightCyberIndo/
fi