banner() {
clear
printf "\e[0m
"
printf "\e[0m\e[1;93m   ____            _      \e[0m\e[1;92m                _  _    \e[0m
"
printf "\e[0m\e[1;93m  |  _ \          | |     \e[0m\e[1;92m               | || |   \e[0m
"
printf "\e[0m\e[1;93m  | |_) | __ _ ___| |__   \e[0m\e[1;92m _ __ ___  _ __| || |_  \e[0m
"
printf "\e[0m\e[1;93m  |  _ < / _  / __|  _ \  \e[0m\e[1;92m|  _   _ \|  _ \__   _| \e[0m
"
printf "\e[0m\e[1;93m  | |_) | (_| \__ \ | | | \e[0m\e[1;92m| | | | | | |_) | | |   \e[0m
"
printf "\e[0m\e[1;93m  |____/ \__,_|___/_| |_| \e[0m\e[1;92m|_| |_| |_| .__/  |_|   \e[0m
"
printf "\e[0m\e[1;93m                          \e[0m\e[1;92m          | |           \e[0m
"
printf "\e[0m\e[1;93m                          \e[0m\e[1;92m          |_|           \e[0m
"
printf "\e[0m
"
printf "\e[0m\e[1;93m    Created By HTR-TECH \e[0m\e[1;91m(\e[0m\e[1;92mTahmid Rayat\e[0m\e[1;91m)\e[0m
"
printf "\e[0m
"
}
banner
printf "\e[0m
"
printf "  \e[0m\e[1;91m[\e[0m\e[1;97m~\e[0m\e[1;91m]\e[0m\e[1;93m Installing Packages...\e[0m
"
printf "\e[0m
"
termux-setup-storage
apt update
clear
pkg install python ffmpeg -y
clear
pip install youtube-dl
clear
termux-setup-storage
clear
sleep 2
banner
printf "\e[0m
"
printf "  \e[0m\e[1;91m[\e[0m\e[1;97m~\e[0m\e[1;91m]\e[0m\e[1;93m Creating Directories...\e[0m
"
printf "\e[0m
"
if [[ -e /sdcard/B2Mp4/Mp4 ]]; then
echo ""
else
mkdir -p /sdcard/B2Mp4/Mp4
fi
if [[ -e /sdcard/B2Mp4/Mp3 ]]; then
echo ""
else
mkdir -p /sdcard/B2Mp4/Mp3
fi
if [[ -e ~/bin ]]; then
echo ""
else
mkdir ~/bin
fi
if [[ -e ~/.config/youtube-dl ]]; then
echo ""
else
mkdir -p ~/.config/youtube-dl
fi
sleep 2
printf "\e[0m
"
printf "  \e[0m\e[1;91m[\e[0m\e[1;97m~\e[0m\e[1;91m]\e[0m\e[1;93m Binding Packets...\e[0m
"
printf "\e[0m
"
cp -f b2mp4 /data/data/com.termux/files/usr/bin/b2mp4
echo 'termux-open-url https://github.com/htr-tech/' > /data/data/com.termux/files/usr/bin/htr-tech
echo 'termux-open-url https://github.com/htr-tech/' > /data/data/com.termux/files/usr/bin/HTR-TECH
echo 'termux-open-url https://www.instagram.com/tahmid.rayat/' > /data/data/com.termux/files/usr/bin/instagram
echo 'termux-open-url https://www.instagram.com/tahmid.rayat/' > /data/data/com.termux/files/usr/bin/Instagram
chmod +x /data/data/com.termux/files/usr/bin/b2mp4
chmod +x /data/data/com.termux/files/usr/bin/htr-tech
chmod +x /data/data/com.termux/files/usr/bin/HTR-TECH
chmod +x /data/data/com.termux/files/usr/bin/instagram
chmod +x /data/data/com.termux/files/usr/bin/Instagram
echo 'youtube-dl $1' > ~/bin/termux-url-opener
sleep 2
printf "\e[0m
"
printf "  \e[0m\e[1;91m[\e[0m\e[1;97m~\e[0m\e[1;91m]\e[0m\e[1;93m Installation Succeed !\e[0m
"
printf "\e[0m
"
sleep 2
printf "\e[0m
"
printf "\e[0m
"
printf "  \e[0m\e[1;93mType b2mp4 to Run the Tool\e[0m
"
printf "\e[0m
"
printf "\e[0m
"
