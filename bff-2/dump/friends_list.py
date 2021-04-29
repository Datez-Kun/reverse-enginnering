#!usr/bin/python2.7
# coding=utf-8
import os, re, sys, json, time,datetime,itertools
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
    id = []
    flist = url + '/friends/center/friends/'
    output = 'dump/friends.json'
    print ''
    while True:
        try:
            response = config.httpRequest(flist, cookie).encode('utf-8')
            html = parser(response, 'html.parser')
            for x in html.find_all(style='vertical-align: middle'):
                find = x.find('a')
                if '+' in str(find) or find == None:
                    continue
                else:
                    full_name = str(find.text.encode('utf-8'))
                    if '/?uid=' in str(find):
                        uid = re.findall('/\\?uid=(.*?)&', find['href'])
                    else:
                        uid = re.findall('/(.*?)\\?fref=', find['href'])
                    if len(uid) == 1:
                        id.append({'uid': uid[0], 'name': full_name})
                    sys.stdout.write('\r\x1b[1;95m•  \r\x1b[1;95m• \x1b[1;97m%s\x1b[1;95m • \x1b[1;97m%s\x1b[1;95m • \x1b[1;97mSedang Dump ' % (
                     datetime.now().strftime('%H:%M:%S'), len(id)))
                    sys.stdout.flush()
                    time.sleep(0.0050)
                                        
            if 'Lihat selengkapnya' in str(html):
                flist = url + html.find('a', string='Lihat selengkapnya')['href']
            else:
                break
        except KeyboardInterrupt:
            print '\n\n \x1b[1;97m[!] Error, Berhenti'
            break

    try:
        for filename in os.listdir('dump'):
            os.remove('dump/' + filename)

    except:
        pass

    print '\n\n\x1b[1;97m [*] Output :\x1b[1;93m ' + output+'\x1b[0;92m '
    save = open(output, 'w')
    save.write(json.dumps(id))
    save.close()
    return
# Awokawokawok Ngerekod:v