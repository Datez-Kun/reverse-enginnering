# Source Generated With Decompyle++
# File : temp.pyc (Python 2.7)

import os
import sys
os.system('clear')
ie = ImportError

try:
    import requests
except ie:
    os.system('python2 -m pip install requests')
    import requests


try:
    from bs4 import BeautifulSoup as soup
except ie:
    os.system('python2 -m pip install bs4')
    from bs4 import BeautifulSoup as soup


class LRC:
    
    def __init__(self):
        self.logo = '\n\x1b[1;91mSIMPLE \x1b[1;93m\xe2\x95\xa6  \xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\n       \x1b[1;93m\xe2\x95\x91  \xe2\x95\xa0\xe2\x95\xa6\xe2\x95\x9d\xe2\x95\x91\n       \x1b[1;93m\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \x1b[1;92mDOWNLOADER \x1b[1;97mv0.1\n\x1b[1;94mAuthor \x1b[1;97m: \x1b[1;92mNanta ID\x1b[1;97m\n'
        self.url = 'https://syair.info{}'
        self.main()

    
    def main(self):
        get_link = ''
        print self.logo
        print '       [ Maaf jika kurang akurat ]       '
        print '[ Saya hanya scrap bagian atas nya saja ]'
        
        try:
            query = raw_input('^^> Cari lirik lagu: ').replace(' ', '+')
        except:
            exit('[!] Error!')

        data = requests.get(self.url.format('/search?q=' + query)).content
        if 'div class="menu"' in data:
            exit("[*] Tidak ada hasil dengan pencarian '" + query + "'")
        data = soup(data, 'html.parser')
        top = data.find('div', class_ = 'li').find('a')
        link = self.url.format(top['href'])
        size = data.find_all('span')[-3].text.split(' ')
        size = size[0] + ' ' + size[1]
        print 'Nama File : ' + top.text
        print 'Ukuran    : ' + size
        print 'Link      : ' + link
        get_link += link
        cus = raw_input('Download [y/n] ')
        if cus.lower() == 'y':
            rdl = ''
            data = requests.get(get_link).content
            data = soup(data, 'html.parser')
            dl_link = data.find_all('a', target = '_blank')
            rdl = self.url.format(dl_link[-1]['href'])
            with open(top.text.replace(' ', '_'), 'w') as guud:
                guud.write(requests.get(rdl).content)
            print '[*] Disimpan. File: ' + top.text.replace(' ', '_')
        else:
            exit()


LRC()
