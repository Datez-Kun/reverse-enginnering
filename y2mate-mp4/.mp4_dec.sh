#Decode At : 03-03-2020,- 14-48-56
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
downloads(){
        iklan=$(curl -s -i "http:/${1}${2}" | grep -c "200OK")
        if [[ iklan == "1" ]]; then
            printf "."
        fi
        url=$(echo "$data2" | grep -Eo "http:.*.y2mate.com.*\" rel=" | cut -d '\' -f3)
        file=$(echo "$data2" | grep -Eo "http:.*.y2mate.com.*\" rel=" | cut -d '\' -f4)
        
        download=$(termux-open-url "http:/${url}${file}")
        printf "."
        printf "$download"

        sleep 0.5
}

url_data(){
	 clear
	 echo -e "\t${p}__________________________"
	 echo -e "\t${h}  DOWNLOADER MP4 YOUTUBE"
	 echo -e "\t${p}       { No Iklan }"
	 echo -e "\t${p}    Author${m}: ${x}Mr.Tr3v!0n"
	 echo -e "\t${p} Team${m}: ${p,}Black Coder Crush"
	 echo -e "\t${p}__________________________"
	 echo -e "\t${m}    { ${x}Private Tools ${m}} \n"
	 
     printf "\t${b}╔════════════════════════╗ \n"
     printf "\t${b}║${p}LINK YOUTUBE${m}:${pu} " url
     read url;
     printf "\t${b}╚════════════════════════╝\n"    
	 if [[ $url =~ "https://youtu.be" ]];then
    	
    	if [[ ${url:16:100} =~ "/" ]];then
    		url="$url"
    	fi
    	
     else
    	echo -e "\n${p}[${m}!${p}] Url Wrong ${m}!!"
    	echo -e "${p}[${m}!${p}] Example: https://youtu.be/${m}xxxxxxx !!\n"
    	exit
     fi
    header=$(curl -s -L -i https://www.y2mate.com)
    cfduid=$(echo $header | grep -Eo "__cfduid.*" | cut -d ";" -f1)
    PHPSESSID=$(echo $header | grep -Eo "PHPSESSID.*;" | cut -d ";" -f1)

    server=$(echo "$header" | grep -Eo "mate([0-9]{1,2}).y2mate.com")
    
    data=$(curl -s "https://${server}/en10/analyze/ajax" --user-agent "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48" \
        -H "cookie:${cfduid}" \
        -H "cookie:${PHPSESSID}" \
        -d "url=${url}&ajax=1" | tr "/" "\n")
    
	judul=$(echo -e "$data" | grep -Eo "title.*" | tr ";" "\n" | sed -n "1p" | tr '"#' '\n' | sed -n "2p" | tr -d '\\')
	echo -e "\n${p}[${m}*${p}]Judul Vedio${m}:${h} $judul\n"
	
    _id=$(echo "${data}" | grep -a "data:" | grep -Eo "_id.*', v_id" | cut -d "'" -f2)
    echo -e "${p}╔════╦══════════╦════════════════╗"
    echo -e "${p}║ ${h}NO ${p}║  ${h}Ukuran ${p} ║ ${h}Qualitas Vedio ${p}║"
    echo -e "${p}╠════╬══════════╩════════════════╝"
    quality=$(echo "${data}" | grep -Eo "([0-9]{1,4})p.*\(.mp4\)")
    size_quality=$(echo "${data}" | grep -Eo "([0-9]{1,4}).[0-9] MB")
    
    count_quality=$(printf "$quality" | grep -Eo "([0-9]{1,4})p.*\(.mp4\)" | wc -l)

    for (( a = 1; a <= ${count_quality}; a++ )); do
        loop1=$(printf "$quality" | sed -n "$a p")
        loop2=$(printf "$size_quality" | sed -n "$a p")
        printf "${p}║ ${h}$a. ${p}║  ${k}${loop2}   ${p} ${loop1}\n"
    
    done
		echo -e "${p}╚════╩═══════════════════════════╝"
    printf "${p}[${h}•${p}]PILIH NOMOR${m}: ${h}" 
    read v_quality

    printf "${p}[${k}?${p}]Converting${h}."
    v_id=$(echo "$data" | grep -Eo "var data_vid =.*\\\"; var da" | cut -d '"' -f2 | cut -d '\' -f1)
    s_quality=$(echo "${data}" | grep -Eo "([0-9]{1,4})p.*\(.mp4\)" | grep -Eo "([0-9]{1,4})p" | sed -n "$v_quality p")

    printf "."
    data2=$(curl -s "https://${server}/convert" \
        --user-agent "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48" \
        -H "cookie:${cfduid}" \
        -H "cookie:${PHPSESSID}" \
        -d "type=youtube&_id=${_id}&v_id=${v_id}&ajax=1&ftype=mp4&fquality=$s_quality")
    
    check1=$(echo "$data2" | grep -Ec "http:.*.y2mate.com.*\" rel=" )

    printf "."
    sleep 0.5

    if [[ $check1 == 0 ]]; then
        printf "."
        sleep 0.5
        check_error=$(echo "$data2" | grep -co "Error:")

        if [[ $check_error == 1 ]]; then
            s_quality=$(echo "$s_quality" | grep  -Eo "([0-9]{1,4})")
            data2=$(curl -s "https://${server}/convert" \
                --user-agent "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48" \
                -H "cookie:${cfduid}" \
                -H "cookie:${PHPSESSID}" \
                -d "type=youtube&_id=${_id}&v_id=${v_id}&ajax=1&ftype=mp4&fquality=$s_quality")
                check="success"
        fi

    else
        check="success"
    fi

    while (true); do
        printf "."
        sleep 3

        file_ready=$(echo "$data2" | grep -c "<a href=")
        if [[ $file_ready == 0 ]]; then
            sleep 2
            data2=$(curl -s "https://${server}/convert" \
                --user-agent "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48" \
                -H "cookie:${cfduid}" \
                -H "cookie:${PHPSESSID}" \
                -d "type=youtube&_id=${_id}&v_id=${v_id}&ajax=1&ftype=mp4&fquality=$s_quality")

        elif [[ $file_ready != 0 ]]; then
            check="success"
            break;
        fi
    done

    printf "."
    printf "."
    sleep 0.5
    printf "."
    sleep 1

    if [[ $check == "success" ]]; then
        printf "\n${p}[${c}√${p}]${h}Converted Success\n"
	printf "${p}[${h}•${p}]${k}Download Vedio${m}[${k}Y${c}/${p}T${m}]${pu}: " down
	read down;
	
	if [[ $down =~ "Y" ]] || [[ $down =~ "y" ]];then
		type=$( curl -s "https://www.y2mate.com/youtube/$url" | grep -Eo "url.*" | sed -n "3p" | tr "'" "\n" | sed -n "2p" | cut -d "/" -f3)
		id=$(curl -s "https://$type/id/mp3/ajax" -d "url=https://www.youtube.com/watch?v=$url&ajax=1" | grep -Eo "_id.*" | tr "," "\n" | sed -n "1p" | cut -d "'" -f2)
		file=$( curl -s "https://$type/mp3Convert?hl=id" -d "type=youtube&_id=$id&v_id=$url&mp3_type=128" | grep -Eo "href.*" | tr '"' '\n' | sed -n "2p" | tr -d '\\')
		sleep 1
		echo -e "${p}[${h}•${p}]Buka Browser Nya"
		sleep 1
		downloads
		exit
	
	elif [[ $down =~ "T" ]] || [[ $down =~ "t" ]];then
		echo -e "${p}[${h}•${p}] Makasih *_*"
		exit
		
	else 
		echo -e "\n${p}[${m}!${p}] Wrong Input ${m}!!"
		sleep 2
		url_data
	fi

        if [[ $nama_file == "" ]]; then
            printf "."
            nama=$(echo "$data" | grep -Eo "var data_vtitle =.*\"; <")
            font_check=$(echo "$nama" | grep -Eo "var data_vtitle =.*\"; <" | grep -o "\"" | wc -l)

            if [[ $font_check == 4 ]]; then
                nama_depan=$(echo "$nama" | grep -Eo "var data_vtitle =.*\"; <" | cut -d '"' -f3)
                nama_belakang$(echo "$nama" | grep -Eo "var data_vtitle =.*\"; <" | cut -d '"' -f4 | cut -d '\' -f1)
                nama_file="${nama_depan}${nama_belakang}"
            else
                nama_file=$(echo "$nama" | grep -Eo "var data_vtitle =.*\"; <" | cut -d '"' -f2 | cut -d '\' -f1)
            fi
        fi
		
    else
        printf "${p}[${m}!${p}]${m}Comverted Failed!!"
        exit 1
    fi

}

trap ctrl_c INT

function ctrl_c (){
    clear
    exit 1
}

url_data