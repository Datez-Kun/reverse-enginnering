# Time Succses Parser : Mon Jun  8 21:19:08 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

raw = requests.get(url, cookies=kuki).content
getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>', str(raw))
for x in getuser:
    if 'profile' in x[0]:
        id.append(x[1] + '|' + re.findall('=(\\d*)?', str(x[0]))[0])
    if 'friends' in x:
        pass
    else:
        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
        print(('\r• Get ID : ' + str(len(id))), end='')

if 'Lihat Teman Lain' in str(raw):
    getid(mbasic.format(parser(raw, 'html.parser').find('a', string='Lihat Teman Lain')['href']))
return id