# Filenames : 
# Python bytecode : 3.8
# Time succses decompiled Sat Sep 26 13:13:00 2020
# Selector <module> in line 4 file 
# Timestamp in code : 2020-06-27 04:07:18

#Instruction context error:
#   
# L.  46       100  POP_EXCEPT       
#                 102  JUMP_BACK            60  'to 60'
#->               104  POP_EXCEPT       
#                 106  JUMP_BACK            60  'to 60'
#               108_0  COME_FROM            92  '92'
#                 108  END_FINALLY      
#                 110  JUMP_BACK            60  'to 60'
#                 112  JUMP_BACK            18  'to 18'
"""
:Parsing response to many function

"""
import re
from bs4 import BeautifulSoup

def parser(raw):
    """
    Change type response to bs4

    """
    return BeautifulSoup(raw, 'html.parser')


def url_find(raw, string, text=False, **args):
    lisT = []
    for url in raw.find_all('a', args, href=True):
        if not 'zero/toggle' in str(url['href']):
            if 'upsell' in str(url['href']):
                pass
            elif text:
                if string in str(url):
                    lisT.append({'url':url['href'], 
                     'text':url.text})
        elif string in str(url):
            lisT.append(url['href'])
        else:
            if len(lisT) == 1:
                return lisT[0]
            return lisT

# --- fixed ---
def form(raw,string):
    rv = {}
    for x in Parser(raw).find_all('form'):
        if string in str(x['action']):
            rv['action'] = x['action']
            for i in x.find_all('input'):
                try:
                    rv[i['name']] = i['value']
                except Exception:
                    pass

        return rv
