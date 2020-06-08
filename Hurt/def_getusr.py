# Time Succses Parser : Mon Jun  8 17:00:47 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun
II = requests.get(friend, cookies=(self.Cookie)).content
getid = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>', str(II))
for L in getid:
    if 'profile' in L[0]:
        id.append(L[1] + '|' + re.findall('=(\\d*)?', str(L[0]))[0])
    if 'friends' in L:
        pass
    else:
        id.append(L[1] + '|' + L[0].split('/')[1].split('?')[0])
        print(('\r• Total ID --> ' + str(len(id))), end='')

if 'Lihat Teman Lain' in str(II):
    getid('https://mbasic.facebook.com{}'.format(cantik(II, 'html.parser').find('a', string='Lihat Teman Lain')['href']))
return id
