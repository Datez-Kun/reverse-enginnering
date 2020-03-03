#Decode At : 03-03-2020,- 14-29-03 WIB

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
		fi
		
}
check
function mp3(){
	clear
	echo -e "\t${p}__________________________";c1="type=yo";v1="htt";l1="htt";i1="url=ht";q1="/id/m";t1="/mp3C";echo -e "\t${h}  DOWNLOADER MP3 YOUTUBE";o1="url=ht";v7="4/ana";v2="ps://m";i2="tps://y";o2="tps://ww";echo -e "\t${p}   { No Iklan ${m}* ${x}v.1.0 ${p}}";v8="lyze/a";v3="ate0";i3="outu.be/";o3="w.yout";c3="e&_id=";echo -e "\t${p}    Author${m}: ${x}Mr.Tr3v!0n";c2="utub";v9="jax";v4="1.y2m";l2="ps://w";q2="p3/a";o4="ube.c";echo -e "\t${p} Team${m}: ${p,}Black Coder Crush";v5="ate.c";l3="ww.y2m";l5="om/yo";t2="onv";o5="om/wa";echo -e "\t${p}__________________________";o6="tch?v=";v6="om/id";l4="ate.c";l6="utube/";q3="jax";t3="ert?hl=id";echo -e "\t      ${m}[ ${p}$TANGGAL-$BULAN-$TAHUN ${m}]\n"
	
	printf "\t${b}╔════════════════════════╗ \n"
    printf "\t${b}║${p}LINK YOUTUBE${m}:${pu} " url
    read url;
    printf "\t${b}╚════════════════════════╝\n"    
    
    if [[ $url =~ "https://youtu.be" ]];then
    	
    	if [[ ${url:16:100} =~ "/" ]];then
    		url="${url:17:100}"
    	fi
    	
    else
    	echo -e "\n${p}[${m}!${p}] Url Wrong ${m}!!"
    	echo -e "${p}[${m}!${p}] Example: https://youtu.be/${m}xxxxxxx !!\n"
    	exit
    fi
    
get=$( \
curl \
-s \
"$v1$v2$v3$v4$v5$v6$v7$v8$v9" \
-d \
"$i1$i2$i3$url&ajax=1")
judul=$( \
echo \
-e \
"$get" | \
grep \
-Eo \
"title.*" | \
tr \
";" "\n" | \
sed \
-n \
"1p" | \
tr \
'"#' '\n' | \
sed \
-n \
"2p" | \
tr \
-d \
'\\')
ukuran=$( \
echo \
-e \
"$get" | \
grep \
-Eo \
"Konverter.*" | \
tr \
"><" "\n" | \
sed \
-n \
"51p" | \
tr \
-d \
'()')
size=$( \
echo \
-e "$get" | \
grep \
-Eo \
"Konverter.*" | \
tr \
"><" "\n" | \
sed \
-n \
"57p")

echo -e "\n${p}[${m}*${p}]${k}NAME MP3${m}:${h} $judul"
echo -e "${p}[${m}*${p}]${pu}SIZE MP3${m}: ${k}$size ${m}(${p}$ukuran${m} )\n"

printf "${p}[${h}•${p}] ${h}Download ${m}[${k}Y${c}/${p}T${m}]${pu}: " down
read down;
	
	if \
	[[ \
	$down \
	=~ \
	"Y" \
	]] \
	|| \
	[[ \
	$down \
	=~ \
	"y" \
	]];then
		type=$( \
		curl \
		-s \
		"$l1$l2$l3$l4$l5$l6$url" | \
		grep \
		-Eo \
		"url.*" | \
		sed \
		-n \
		"3p" | \
		tr \
		"'" "\n" | \
		sed \
		-n \
		"2p" | \
		cut \
		-d "/" \
		-f3)
		id=$( \
		curl \
		-s \
		"https://$type$q1$q2$q3" \
		-d \
		"$o1$o2$o3$o4$o5$o6$url&ajax=1" | \
		grep \
		-Eo \
		"_id.*" | \
		tr \
		"," "\n" | \
		sed \
		-n \
		"1p" | \
		cut \
		-d "'" \
		-f2)
		file=$( \
		curl \
		-s \
		"https://$type$t1$t2$t3" \
		-d \
		"$c1$c2$c3$id&v_id=$url&mp3_type=128" | \
		grep \
		-Eo \
		"href.*" | \
		tr \
		'"' '\n' | \
		sed \
		-n \
		"2p" | \
		tr \
		-d \
		'\\')

		echo -e "${p}[${h}•${p}] Buka Browser Nya"
		sleep 2
		termux-open-url "$file"
	
	elif [[ $down =~ "T" ]] || [[ $down =~ "t" ]];then
		echo -e "${p}[${h}•${p}] Makasih *_*"
		exit
		
	else 
		echo -e "\n${p}[${m}!${p}] Wrong Input ${m}!!"
		sleep 2
		mp3
	fi
	
}
mp3
