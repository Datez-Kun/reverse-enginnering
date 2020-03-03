set +x
declare -f loading
loading() {
declare -a colors
colors=( '[91m' '[92m' '[93m' '[94m' '[95m' '[96m' )
local text num rand i t oldText endText
w='[97m'
b=${colors[3]}
r=${colors[0]}
text="$1"
num=0
OFIS=$IFS
IFS=$'
	'
local spinstr='|/-\'
while [[ $num < 1 ]]; do
i=0
rand=${colors[$(shuf -n 1 -i 0-$(( ${#colors[@]} - 1)) )]}
for letter in $(echo ${text} | fold -w 1); do
if (( $i == 0 )); then
local temp="${spinstr#?}"
tput civis
printf "${w}%s${rand}%s  ${b}[${r}%c${b}]" "${letter~~}" "${text:1}" $spinstr
local spinstr=$temp${spinstr%"$temp"}
((i++))
elif (( $i == 1 )); then
oldText=${text:0:1}
local temp="${spinstr#?}"
tput civis
printf "${rand}%s${w}%s${rand}%s  ${b}[${r}%c${b}]" "${oldText}" "${letter~~}" "${text:2}" $spinstr
local spinstr=$temp${spinstr%"$temp"}
((i++))
elif (( $i == $i )); then
oldText=${text:0:$i}
endText="${text:$(( i + 1 )):${#text}}"
local temp="${spinstr#?}"
tput civis
printf "${rand}%s${w}%s${rand}%s  ${b}[${r}%c${b}]" "${oldText}" "${letter~~}" "${endText}" $spinstr
local spinstr=$temp${spinstr%"$temp"}
((i++))
fi
sleep 0.1
done
((num++))
done
tput cnorm
return 0
}
for((;n++<=1;)) { loading "$1";}
