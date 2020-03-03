#Decode At : 03-03-2020,- 14-29-23 WIB

b="\033[34;1m"
p="\033[39;1m"
k="\033[33;1m"
m="\033[31;1m"
h="\033[32;1m"
c="\033[35;1m"
pu="\033[36;1m"
x="\033[30;1m"
o="\033[0m"
JAM=`date +%H`
MENIT=`date +%M`
DETIK=`date +%S`
TANGGAL=`date +%d`
BULAN=`date +%m`
TAHUN=`date +%Y`
        
function mulai(){
	clear
	echo -e "\t${p}__________________________"
	echo -e "\t${h}    YOUTUBE DOWNLOADER"
	echo -e "\t${p}   { No Iklan ${m}* ${x}v.2.0 ${p}}"
	echo -e "\t${p}    Author${m}: ${x}Mr.Tr3v!0n"
	echo -e "\t${p} Team${m}: ${p,}Black Coder Crush"
	echo -e "\t${p}__________________________"
	echo -e "\t      ${m}[ ${p}$TANGGAL-$BULAN-$TAHUN ${m}]\n"
	
	echo -e "\n\t ${p}[${h}01${p}] Download ${h}Mp3 ${p}Youtube"
	echo -e "\t ${p}[${h}02${p}] Download ${h}Mp4 ${p}Youtube"
	echo -e "\t ${p}[${h}03${p}] ${k}Channel Telegram"
	echo -e "\t ${p}[${m}00${p}] ${m}Exit\n"
	echo -e "\t${p}__________________________"
	printf "\t ${p}[${k}?${p}] PILIH NO${m}: ${h}" 
	read no;
	
		if [[ $no =~ "01" ]] || [[ $no =~ "1" ]];then
			bash .mp3.sh
		
		elif [[ $no =~ "02" ]] || [[ $no =~ "2" ]];then
			bash .mp4.sh
		
		elif [[ $no =~ "03" ]] || [[ $no =~ "3" ]];then
			sleep 1
			termux-open-url "https://t.me/config_geratis"
			mulai
			
		elif [[ $no =~ "00" ]] || [[ $no =~ "0" ]];then
			echo -e "\t ${p}[${h}•${p}] ${h}Trimakasih ${p}*_*"
			exit 1
			
		else 
			echo -e "\n\t ${p}[${m}!${p}] Wrong Input ${m}!!"
			sleep 2
			mulai
		fi
			
}
mulai
		
		