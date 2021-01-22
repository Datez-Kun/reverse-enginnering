# Filenames : 
# Python bytecode : 3.8
# Time succses decompiled Sat Sep 26 04:15:28 2020
# Selector <module> in line 6 file 
# Timestamp in code : 2020-06-27 04:07:18

#Instruction context error:
#   
# L.  40       108  JUMP_BACK            32  'to 32'
#->               110  JUMP_FORWARD        154  'to 154'
#               112_0  COME_FROM           106  '106'
import re
from .session import browser
from .parsing import url_find, parser

class Main:

    def __init__(self, cookie):
        """
        :params
         > cookie: Your cookies

        """
        self.id = []
        self.parser = browser(cookie)

    def friendlist(self,link):
        try:
            raw = self.parser.get(link)
            users = url_find(raw, '?fref', text=True)
            for user in users:
                if 'profile' in str(user['url']):
                    self.id.append({'name':user['text'], 
                     'username':re.findall('=(\\d*)', str(user['url']))[0]})
                else:
                    if 'friend' in str(user):
                        pass
                    else:
                        self.id.append({'name':user['text'], 
                         'username':user['url'].replace('?fref=fr_tab', '').replace('/', '')})
                print(('\r  { ! } %s retrieved' % str(len(self.id))),
                  end='')

            if 'cursor=' in str(raw):
                self.friendlist(url_find(raw, 'cursor='))
            return self.id
        except:
            return self.id

    def likes(self, url):
        """
        params
        url: url who is react in post `type <string>`
        """
        try:
            raw = self.parser.geturl
            users = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(raw))
            for user in users:
                if 'profile' in user[0]:
                    self.id.append({'name':user[1], 
                     'username':re.findall('=(\\d*)',str(user[0]))[0]})
                else:
                    self.id.append({'name':user[1], 
                     'username':user[0].split('/')[1]})
                print(('\r  { ! } %s retrieved' % str(len(self.id))), end='')
            else:
                if 'ids=' in str(raw):
                    self.likesurl_find(raw, 'ids=')

            return self.id
        except:
            return self.id

    def bysearch(self, url):
        """
        params
        url: url by serach link
        """
        try:
            search = self.parser.geturl
            users = re.findall('profile picture".*?<a href="/(.*?)"><div class=".."><div.*?>(.*?)</div>',str(search))
            for user in users:
                if 'profile' in user[0]:
                    self.id.append({'name':user[1], 
                     'username':re.findall('=(\\d*)',str(user[0]))[0]})
                else:
                    self.id.append({'name':user[1], 
                     'username':user[0].split('?')[0]})
                print(('\r  { ! } %s retrieved' % str(len(self.id))), end='')
            else:
                if 'cursor=' in str(search):
                    self.bysearchurl_find(search, 'cursor=').split('.com')[1]

            return self.id
        except:
            return self.id

    def fromGrub(self, url):
        try:
            grab = self.parser.geturl
            users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
            for user in users:
                if 'profile' in user[0]:
                    self.id.append({'name':user[1], 
                     'username':re.findall('id=(\\d*)',str(user[0]))[0]})
                else:
                    self.id.append({'name':user[1], 
                     'username':user[0]})
                print(('\r  { ! } %s retrieved' % str(len(self.id))), end='')
            else:
                if 'cursor=' in str(grab):
                    self.fromGruburl_find(grab, 'cursor=')

            return self.id
        except:
            return self.id

    def hashtag(self, url):
        try:
            grab = self.parser.geturl
            users = re.findall('<a href="/(.*?)__tn__=C">(.*?)</a>',str(grab))
            for user in users:
                if 'profile' in user[0]:
                    self.id.append({'name':user[1], 
                     'username':re.findall('id=(\\d*)',str(user[0]))[0]})
                else:
                    self.id.append({'name':user[1], 
                     'username':user[0].replace('?','')})
                print(('\r  { ! } %s retrieved' % str(len(self.id))), end='')
            else:
                if len(self.id) != 0:
                    if 'cursor=' in str(grab):
                        self.hashtagurl_find(grab, 'cursor=').split('.com')[1]

            return self.id
        except:
            return self.id
