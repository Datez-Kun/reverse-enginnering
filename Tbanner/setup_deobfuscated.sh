!/usr/bin/bash
clear
printf """\e[0m\e[1;93m
	 _______   _
	|__   __| | |
	   | |    | |__   __ _ _ __  _ __   ___ _ __
	   | |    |  _ \ / _  |  _ \|  _ \ / _ \  __|
	   | |    | |_) | (_| | | | | | | |  __/ |
	   |_|    |____/ \__,_|_| |_|_| |_|\___|_|
	
	   \e[0m\e[1;93mCreated By HTR-TECH \e[0m\e[1;96m( \e[0m\e[1;93mTahmid Rayat \e[0m\e[1;96m)"""
printf "
"
echo
read -p $' \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Input Your Name : \e[0m\e[1;96m\en' option
echo
printf " \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Initializing ...\e[0m
"
sleep 2
apt update
apt install figlet -y
cp .1 .bashrc
echo "echo -e '\e[0m\e[1;93m'" >> .bashrc
echo "  figlet $option" >> .bashrc
printf "echo -e '\e[0m\e[1;32m'
date
echo -e '\e[0m'
" >> .bashrc
mv .bashrc ~
echo
printf " \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Binding Packets ...\e[0m
"
sleep 2
echo
echo
printf " \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Done !!\e[0m
"
sleep 1
echo
printf " \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Now Restart Termux App\e[0m
"
printf "\e[0m
"
