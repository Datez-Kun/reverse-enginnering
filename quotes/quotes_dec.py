# Decompiled At : Fri Apr 10 21:02:24 WIB 2020
# File : temp.pyc (Python 2.7)

exec 'import os, sys, requests, json, random, time'
os.system('clear')
b = '\x1b[94;1m'
m = '\x1b[91;1m'
k = '\x1b[93;1m'
h = '\x1b[92;1m'
p = '\x1b[97;1m'
pu = '\x1b[96;1m'
c = '\x1b[95;1m'
bl = '\x1b[90;1m'
bg = '\x1b[7m'
nr = '\x1b[0m'
warna = random.choice([b, m, k, h, p, pu, c])
logo = '%s\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97 %s\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\n%s\xe2\x95\x91\xe2\x95\x90\xe2\x95\xac\xe2\x95\x97%s\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x9c\xe2\x94\xa4 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x90\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a%s\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 \xe2\x94\xb4 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 %sOf The Day%s v0.1\n%s Coded by Nanta ID a.k.a R3DB0T %s\n' % (h, m, h, m, h, m, k, nr, bg, nr)
api = 'trnsl.1.1.20190811T093056Z.c49ad2b84a78db90.3c8791321fcf6ba39a3a12ce331dd5ff7e5271eb'
page = 'https://api.quotable.io/random'

class Quotes:

    def __init__(self):
        self.main(api)

    def main(self, api):
        try:
            print logo
            for x in m + '[' + nr + ' Maaf jika translatenya ngawur:)' + m + ' ]' + nr + '\n':
                sys.stdout.write(x)
                sys.stdout.flush()
                time.sleep(0.1)

            data = json.loads(requests.get(page).text)
            author = data['author']
            quotes = data['content']
            url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=%s&text=%s&lang=id' % (api, quotes)
            conv = json.loads(requests.get(url).text)
            idq = ('').join([ str(q) for q in conv['text'] ])
            print 50 * ('%s\xe2\x95\x90%s' % (m, nr))
            print ('English').center(50)
            print '" ' + warna + quotes + nr + ' "'
            print 50 * ('%s\xe2\x95\x90%s' % (m, nr))
            print ('Indonesian').center(50)
            print '" ' + warna + idq + nr + ' "'
            print 50 * ('%s\xe2\x95\x90%s' % (m, nr))
            print ('Author').center(50)
            print warna + ('~ ' + nr + author).center(53)
            print 50 * ('%s\xe2\x95\x90%s' % (m, nr))
        except Exception as hm:
            print m + '- ERROR_LOG:  ' + str(hm)


Quotes()
