# Filenames : 
# Python bytecode : 3.8
# Time succses decompiled Sat Sep 26 13:17:38 2020
# Selector <module> in line 1 file 
# Timestamp in code : 2020-06-27 04:07:18

import requests
ses = requests.Session()
from bs4 import BeautifulSoup as parser

class browser:

    def __init__(self, kuki):
        self._browser__kuki = {'cookie': kuki}

    def get(self, link):
        return parser(ses.get(('https://mbasic.facebook.com' + link), headers=(self._browser__kuki)).content, 'html.parser')


