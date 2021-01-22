# Filenames : <EzzKun>
# Python bytecode : 3.8
# Time : Mon Sep 21 15:47:16 2020
# Selector <module> in line 1 file <EzzKun>
# Timestamp in code : 2020-09-18 02:01:53

#Instruction context:
#   
# L. 551       964  POP_EXCEPT       
#                 966  BREAK_LOOP          970  'to 970'
#->               968  END_FINALLY      
#               970_0  COME_FROM           966  '966'
#               970_1  COME_FROM           956  '956'
import cloudscraper, sys, os, time, random, requests
from datetime import datetime
from config import *
headers = {'user-agent':'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.93 Mobile Safari/537.36', 
 'content-type':'application/x-www-form-urlencoded', 
 'accept':'/', 
 'x-requested-with':'com.reland.relandicebot', 
 'sec-fetch-site':'cross-site', 
 'sec-fetch-mode':'cors', 
 'accept-encoding':'gzip, deflate', 
 'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
 'cookie':'lang=id'}
scr = cloudscraper.create_scraper()
url = 'https://www.999doge.com/api/web.aspx'
birutua = '\x1b[0;34m'
putih = '\x1b[0m'
kuning = '\x1b[1;33m'
hijau = '\x1b[1;32m'
merah = '\x1b[1;31m'
biru = '\x1b[0;36m'
ungu = '\x1b[1;35m'
bghijau_white = '\x1b[5;37;42m'
bgmerah_black = '\x1b[5;37;41m'
num_format = '{:.8f}'.format
num_PayIn = '{:0>1.0f}'.format
Username = account['Username']
Password = account['Password']
BaseTrade = float(tradeset['BaseTrade'])
C1 = float(tradeset['C1'])
C2 = float(tradeset['C2'])
TC1 = int(tradeset['TradeCount_1'])
TC2 = int(tradeset['TradeCount_2'])
if TC1 > 200 or (TC2 > 200):
    print('Number Of Trade Out of Limit')
    sys.exit()
IncreaseOnWinPercent = str(tradeset['MultiplyOnWin'])
if IncreaseOnWinPercent == '0':
    ResetOnWin = 1
else:
    ResetOnWin = 0
IncreaseOnLosePercent = str(tradeset['MultiplyOnLose'])
if IncreaseOnLosePercent == '0':
    ResetOnLose = 1
else:
    ResetOnLose = 0
MaxBase = tradeset['MaxBaseTrade']['Toogle']
if MaxBase == 'ON':
    MaxBaseTrade = float(tradeset['MaxBaseTrade']['Max']) * 100000000
    if tradeset['MaxBaseTrade']['ResetOnLoseMaxTrade'] == 'ON':
        ResetOnLoseMaxTrade = 1
    else:
        ResetOnLoseMaxTrade = 0
    if tradeset['MaxBaseTrade']['StopOnLoseMaxTrade'] == 'ON':
        StopOnLoseMaxTrade = 1
    else:
        StopOnLoseMaxTrade = 0
elif MaxBase == 'OFF':
    MaxBaseTrade = 0
    ResetOnLoseMaxTrade = 0
    StopOnLoseMaxTrade = 0
ForceTC1AfterLose = tools['ForceTC1AfterLose']
ChangeTCAfterLose = tools['ChangeTCAfterLose']['Toogle']
TargetProfit = float(tools['TargetProfit'])
ClientSeed = int(tradeset['ClientSeed'])
RecoveryMultiplier = float(tools['RecoveryMultiplier'])
RecoveryIncrease = float(tools['RecoveryIncrease'])
AddDelayTrade = float(tools['AddDelayTrade'])
AddDelayTradeWin = float(tools['AddDelayTradeWin'])
AddDelayTradeLose = float(tools['AddDelayTradeLose'])
StopLoseBalance = float(tools['StopLoseBalance'])
ContinueLastBase = tools['ContinueLastBase']
SmartRecovery = tools['SmartRecovery']

def withdraw():
    amt = input('Witdraw Amount (0 = withdraw all) : ')
    Address = input('Wallet : ')
    Amount = int(amt) * 100000000
    otp = input('2FA Code (IF Enabled): ')
    withdraw_data = 'a=Withdraw&s=' + ses + '&Amount=' + str(Amount) + '&Address=' + Address + '&Totp=' + otp + '&Currency=doge'
    withdraw = scr.post(url, data=withdraw_data, headers=headers).json()
    try:
        if withdraw['Pending']:
            print(hijau + 'Success Pending' + putih)
            input('')
    except:
        pass
    try:
        if withdraw['TooSmall']:
            print(hijau + 'Minimum 2 DOGE' + putih)
            input('')
    except:
        pass

def harga_license():
    print('Price List License SELENIA TRADEBOT')
    print(hijau + '~Premium~' + putih)
    print(biru + '[1] 14 Days - 15K IDR SG SERVER - 1 USER - MULTI DEVICE')
    print('[2] 30 Days - 25K - IDR SG SERVER - 1 USER - MULTI DEVICE')
    print(hijau + '~Platinum~' + putih)
    print(biru + '[1] 14 Days - Ì¶2Ì¶5Ì¶K > 15K - SG SERVER - MULTI USER - MULTI DEVICE')
    print('[2] 30 Days - Ì¶3Ì¶5Ì¶K > 20K - SG SERVER - MULTI USER - MULTI DEVICE' + putih)
    print(kuning + 'Price Valid Until 24/09/2020')
    print('Contact Admin :')
    print('Whatsapp/Telegram : +6283153942438')
    print('*Chat Only*')
    input('Enter' + putih)

def post(data):
    req = requests.post(url, data=data, headers=headers).json()
    return req

def login():
    otp = ''
    data = {'username':Username, 
     'password':Password}
    url_get = 'http://layscape.xyz/selenia/getuser.php'
    getid = scr.post(url_get, data=data).json()
    if getid['status'] == 'Berhasil':
        pass
    else:
        print(merah + getid['status'] + putih)
        sys.exit()
    otp = input('2FA Code (If Enabled) : ')
    login = 'a=Login&Key=e46b7c63f6b647e0bed15b38238700d5&Username=' + getid['username'] + '&Password=' + getid['password'] + '&Totp=' + otp
    try:
        post(login)
        ses = req['SessionCookie']
        refer = req['ReferredById']
        dogebalance = req['Doge']['Balance'] / 100000000
        accid = req['AccountId']
        print(hijau + 'Login Success')
        statslogin = 'Online'
        getwalletdoge = 'a=GetDepositAddress&s=' + ses + '&Currency=doge'
        post(getwalletdoge)
        dogewallet = req['Address']
        time.sleep(2)
    except Exception as e:
        try:
            print(e)
            print(merah + 'Check Username or Password')
            sys.exit()
        finally:
            e = None
            del e
    else:
        return getid
# Filenames : <EzzKun>
# Python bytecode : 3.8
# Time : Sun Sep 20 17:46:07 2020
# Selector autobet in line 171 file <EzzKun>
# Timestamp in code : 2020-07-16 04:45:22

def autobet(x):
    win = 0
    lose = 0
    wins = 0
    loses = 0
    delay = 0
    MaxPayIns = 0
    MaxBase = 0
    MaxPayOuts = 0
    TotalProfit = 0
    ProfitSementara = 0
    PayIn = 0
    LProfit = 0
    if BaseTrade >= float(1e-08) and BaseTrade < float(0.0001):
        delay = 2
    elif BaseTrade >= float(0.0001) and BaseTrade < float(0.001):
        delay = 1
    elif BaseTrade >= float(0.001) and BaseTrade < float(0.01):
        delay = 0.5
    elif BaseTrade >= float(0.01):
        delay = 0
    if x > 150:
        print(hijau + 'Please Buy License')
        print(kuning + 'Max Balance For Free Is 150 Doge', putih)
        sys.exit()
    else:
        print(hijau + 'Start Trading' + putih)
        time.sleep(2)
        os.system('clear')
    if BaseTrade > 0:
        PayIn = BaseTrade * int(100000000)
    else:
        PayIn = BaseTrade / int(100000000)
    Profit = 0
    NumberOfTrade = random.randint(TC1, TC2)
    while True:
        try:
            if TotalProfit < TargetProfit:
                time.sleep(AddDelayTrade)
                ch = round(random.uniform(C2, C1), 2)
                Low = int(1000000) - ch * int(10000)
                PlaceAutoBets = {'a':'PlaceAutomatedBets', 
                 's':ses, 
                 'BasePayIn':num_PayIn(int(PayIn)), 
                 'Low':int(Low), 
                 'High':'999999', 
                 'MaxBets':int(NumberOfTrade), 
                 'ResetOnWin':ResetOnWin, 
                 'ResetOnLose':ResetOnLose, 
                 'IncreaseOnWinPercent':str(IncreaseOnWinPercent), 
                 'IncreaseOnLosePercent':str(IncreaseOnLosePercent), 
                 'MaxPayIn':int(MaxBaseTrade), 
                 'ResetOnLoseMaxBet':int(ResetOnLoseMaxTrade), 
                 'StopOnLoseMaxBet':int(StopOnLoseMaxTrade), 
                 'ClientSeed':int(ClientSeed), 
                 'Currency':Currency, 
                 'ProtocolVersion':'2'}
                post(PlaceAutoBets)
                try:
                    if int(req['InsufficientFunds']) == 1:
                        print('\n\nInsufficient Funds')
                        input('Enter')
                    else:
                        pass
                except:
                    print('hello') # my modificated, to skip parserror
                else: # -> this is nothing
                    BetCount = len(req['PayIns']) # -> exception return to this
                    PayIns = sum(req['PayIns'])
                    PayOuts = sum(req['PayOuts'])
                    if MaxPayIns > PayIns:
                        MaxPayIns = PayIns
                    count_profit = PayOuts + PayIns
                    if MaxPayOuts > count_profit:
                        MaxPayOuts = count_profit
                    Profit += count_profit
                    TotalProfit = Profit / 100000000
                    if PayOuts > 0 and count_profit > 0:
                        win += 1
                        lose = 0
                        if wins < win:
                            wins += 1
                        print(bghijau_white + 'TC:', BetCount, 'TradeIn:', num_format(PayIns / -100000000) + ' TradeProfit:', ' ' + num_format(count_profit / 100000000) + putih)
                        print(hijau, 'Profit :', (num_format(Profit / 100000000) + putih), (hijau + '[W]' + str(win) + ':' + str(wins) + merah), ('[L]' + str(lose) + ':' + str(loses) + putih), end='\r')
                        if BaseTrade > 0:
                            PayIn = BaseTrade * int(100000000)
                            NumberOfTrade = random.randint(TC1, TC2)
                        else:
                            PayIn = BaseTrade / int(100000000)
                            NumberOfTrade = random.randint(TC1, TC2)
                        if SmartRecovery == 'ON':
                            LProfit += count_profit
                            if LProfit > 0:
                                LProfit = 0
                                if BaseTrade > 0:
                                    PayIn = BaseTrade * int(100000000)
                                    NumberOfTrade = random.randint(TC1, TC2)
                                else:
                                    LProfit += Profit
                                    PayIn = BaseTrade / int(100000000)
                                    NumberOfTrade = random.randint(TC1, TC2)
                            else:
                                LProfit += count_profit
                                if ContinueLastBase == 'ON':
                                    PayIn = (req['PayIns'][(-1)] + RecoveryIncrease) * RecoveryMultiplier
                                else:
                                    PayIn = (req['PayIns'][0] + RecoveryIncrease) * RecoveryMultiplier
                                if MaxBase == 'ON':
                                    MaxBaseTrade = (MaxBaseTrade + RecoveryIncrease) * RecoveryMultiplier
                                elif MaxBase == 'OFF':
                                    MaxBaseTrade = 0
                                if ForceTC1AfterLose == 'ON':
                                    NumberOfTrade = 1
                                elif ForceTC1AfterLose == 'OFF':
                                    NumberOfTrade = random.randint(TC1, TC2)
                                if ChangeTCAfterLose == 'ON':
                                    NumberOfTrade = tools['ChangeTCAfterLose']['ChangeTo']
                        else:
                            pass
                        if MaxBase == 'ON':
                            MaxBaseTrade = float(tradeset['MaxBaseTrade']['Max']) * 100000000
                        elif MaxBase == 'OFF':
                            MaxBaseTrade = 0
                        time.sleep(AddDelayTradeWin)
                    else:
                        win = 0
                        lose += 1
                        LProfit += count_profit
                        if loses < lose:
                            loses += 1
                        print(bgmerah_black + 'TC:', BetCount, 'TradeIn:', num_format(PayIns / -100000000) + ' TradeProfit:', num_format(count_profit / 100000000) + putih)
                        print(hijau, 'Profit :', (num_format(Profit / 100000000) + putih), (hijau + '[W]' + str(win) + ':' + str(wins) + merah), ('[L]' + str(lose) + ':' + str(loses) + putih), end='\r')
                        if ContinueLastBase == 'ON':
                            PayIn = (req['PayIns'][(-1)] + RecoveryIncrease) * RecoveryMultiplier
                        else:
                            PayIn = (req['PayIns'][0] + RecoveryIncrease) * RecoveryMultiplier
                        if MaxBase == 'ON':
                            MaxBaseTrade = (MaxBaseTrade + RecoveryIncrease) * RecoveryMultiplier
                        elif MaxBase == 'OFF':
                            MaxBaseTrade = 0
                        if ForceTC1AfterLose == 'ON':
                            NumberOfTrade = 1
                        elif ForceTC1AfterLose == 'OFF':
                            NumberOfTrade = random.randint(TC1, TC2)
                        if ChangeTCAfterLose == 'ON':
                            NumberOfTrade = tools['ChangeTCAfterLose']['ChangeTo']
                        else:
                            pass
                        time.sleep(AddDelayTradeLose)
                        time.sleep(delay)
                    if Profit < float(StopLoseBalance):
                        print(merah + '\nStop Lose Tercapai' + putih)
                        sys.exit()

                print('\nTrading Complete\nTrade Summary:')
                print(kuning + 'Profit :', num_format(Profit / 100000000))
                print('Higher TradeIn :', num_format(MaxPayIns / -100000000))
                print('Higher PayOut :', num_format(MaxPayOuts / 100000000))
        except Exception as e:
        	try:
        		print(e)
        		input('Enter')
        	finally:
        		e = None
#Instruction context error:
#-> 
# L. 247       482  POP_EXCEPT       
#                 484  BREAK_LOOP          488  'to 488'
#                 486  END_FINALLY      
#               488_0  COME_FROM           484  '484'
#               488_1  COME_FROM           474  '474'

def ainfo():
    url_login = 'https://www.999doge.com/api/web.aspx'
    dlogin = 'a=Login&Key=258aed99b1924356909fd825d695a9ac&Username=' + getid['username'] + '&Password=' + getid['password'] + '&Totp='
    login = scr.post(url_login, data=dlogin, headers=headers).json()
    seswallet = login['SessionCookie']
    getwalletdoge = 'a=GetDepositAddress&s=' + seswallet + '&Currency=doge'
    pwalletdoge = scr.post(url_login, data=getwalletdoge, headers=headers)
    login = scr.post(url_login, data=dlogin, headers=headers).json()
    dogbal = login['Doge']['Balance'] / 100000000
    depodog = login['Doge']['DepositAddress']
    depoltc = login['LTC']['DepositAddress']
    depoeth = login['ETH']['DepositAddress']
    depobtc = login['DepositAddress']
    accid = login['AccountId']
    print('Account Information:')
    print('ID :', accid)
    print('Username : ' + getid['username'])
    print('Password : ' + getid['password'])
    print('Username & Password For Login 999Doge.com')
    print('Balance :')
    print('-Doge :', num_format(dogbal))
    print('Deposit Address :')
    print('-Doge :', depodog)
    input('Enter')

def verify():
    if refer == 317641596:
        print(hijau + 'Success Verify Account' + putih)
    else:
        print(merah + 'Account Not Registered' + putih)
        print(kuning + 'Please Register')
        sys.exit()

def register():
    print('Creating Account')
    CreateAccount = 'a=CreateAccount&Key=e46b7c63f6b647e0bed15b38238700d5'
    post(CreateAccount)
    AccountCookie = req['AccountCookie']
    BeginSession = 'a=BeginSession&Key=e46b7c63f6b647e0bed15b38238700d5&AccountCookie=' + AccountCookie
    print('Begining Session')
    post(BeginSession)
    Session = req['SessionCookie']
    inpusername = input('Input Username : ')
    inppassword = input('Input Password : ')
    gen = 'ABCDEFGHIJKLMN0PQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789#*&%$'
    grator = lambda lenght: [random.choice(gen) for i in range(lenght)]
    u_id = grator(12)
    p_id = grator(12)
    username_id = ''.join([str(elem) for elem in u_id])
    password_id = ''.join([str(elem) for elem in p_id])
    data = {'username':inpusername, 
     'password':inppassword, 
     'usernameid':username_id, 
     'passwordid':password_id}
    url_create = 'http://layscape.xyz/selenia/create.php'
    create = scr.post(url_create, data=data).json()
    if create['status'] == 'Registered':
        print(hijau + create['status'] + ' to Server')
    else:
        print(merah + create['status'] + ' to Server')
        sys.exit()
    CreateUser = 'a=CreateUser&s=' + Session + '&Username=' + username_id + '&Password=' + password_id
    post(CreateUser)
    try:
        if req['success'] == 1:
            print(hijau + 'Account Registered')
            print('Please Change Login Information In Config')
            input('Enter' + putih)
    except:
        pass
    try:
        if req['AccountHasUser'] == 1:
            print('Account Has User')
            input('Enter')
    except:
        pass
    try:
        if req['UsernameTaken'] == 1:
            print('Username Has Been Taken')
            input('Enter')
    except:
        pass

def check_license():
    if 'PLTM' in license:
        print(merah + 'This License Not For Premium Login')
        sys.exit()
    url_license = 'https://layscape.xyz/selenia/user'
    url_license_add = 'https://layscape.xyz/selenia/adduser'
    data = {'license':license, 
     'username':Username}
    mydatetime = datetime.now()
    date = mydatetime.strftime('%Y-%m-%d')
    try:
        user_premium_add = scr.post(url_license_add, data=data).json()
        if user_premium_add['status'] == 'Added':
            print(kuning + user_premium_add['status'] + putih)
        else:
            print(kuning + user_premium_add['status'] + putih)
    except:
        pass
    else:
        try:
            user_premium = scr.post(url_license, data=data).json()
            userdate = user_premium['date']
            userdate_split = int(''.join([i for i in str(userdate).split('-')]))
            date_split = int(''.join([i for i in str(date).split('-')]))
            Expired = int(userdate_split) - int(date_split)
            if Expired > 30:
                Expired = Expired - 70
                if Expired > 60:
                    Expired = Expired - 70
                print(hijau + 'Sukses Verify License')
                User = 'Granted'
                print(User)
            else:
                if Expired < 0:
                    print(merah + 'License Out of Date' + putih)
                    sys.exit()
        except Exception as e:
            try:
                print(e)
                print(hijau + 'User Not Permited To Use This License')
                print(merah + user_premium['status'] + putih)
                sys.exit()
            finally:
                e = None
                del e

        else:
            return Expired

def check_license_premium():
    if 'STB' in license:
    print(merah + 'This License Not For Platinum Login')
    sys.exit()
    url_license = 'https://layscape.xyz/selenia/user_platinum'
    data = {'license':license, 
     'username':Username}
    mydatetime = datetime.now()
    date = mydatetime.strftime('%Y-%m-%d')
    try:
        user_premium = scr.post(url_license, data=data).json()
        userdate = user_premium['date']
        userdate_split = int(''.join([i for i in str(userdate).split('-')]))
        date_split = int(''.join([i for i in str(date).split('-')]))
        Expired = int(userdate_split) - int(date_split)
        if Expired > 30:
           Expired = Expired - 70
            if Expired > 60:
               Expired = Expired - 70
            print(hijau + 'Sukses Verify License')
            User = 'Granted'
            print(User)
        else:
            if Expired < 0:
               print(merah + 'License Out of Date' + putih)
               sys.exit()
    except Exception as e:
        try:
            print(e)
            print(hijau + 'User Not Permited To Use This License')
            print(merah + user_premium['status'] + putih)
            sys.exit()
        finally:
            e = None
            del e
    else:
        return Expired

def gblnc():
    getbalance = 'a=GetBalance&s=' + ses + '&Currency=doge'
    post(getbalance)
    dogebalance = req['Balance'] / 100000000
    return dogebalance

if StopLoseBalance == '0' or StopLoseBalance == 0:
    StopLoseBalance = -999999999999999999999999999
else:
    if StopLoseBalance != '0' or (StopLoseBalance != 0):
        StopLoseBalance = StopLoseBalance * -100000000
Currency = 'doge'
statslogin = 'Offline'
limit = 0
try:
    os.system('clear')
    srv = scr.get('https://layscape.xyz/selenia/info.php')
    status = srv.status_code
    print('Server Status Code [', status, ']')
    if status == 200:
        print(hijau + 'Alive' + putih)
        info = srv.json()
        version = info['versi']
    else:
        pass
except Exception as e:
    try:
        print(merah + 'Server Down Try Again or Check Latest Version Script' + putih)
        print('Server Status Code [', status, ']')
        print(merah, 'ERROR CONNECTION TRY AGAIN' + putih)
        sys.exit()
    finally:
        e = None
        del e
if status == 200:
    try:
        getbalance = 'a=GetBalance&s=' + ses + '&Currency=doge'
        post(getbalance)
        dogebalance = req['Balance'] / 100000000
    except:
        pass
    else:
        time.sleep(1)
        os.system('clear')
        print('\x1b[1;31m====================================================\x1b[0m')
        print('\x1b[1;32m[+]\x1b[0m             \x1b[0;36mDO WITH YOUR OWN RISK \x1b[0m           \x1b[1;32m[+]\x1b[0m')
        print('\x1b[1;32m[+]\x1b[0m \x1b[1;33mCreator : Layscape\x1b[0m                           \x1b[1;32m[+]\x1b[0m')
        print('\x1b[1;32m[+]\x1b[0m \x1b[1;33mVersi Script  V3.0\x1b[0m                           \x1b[1;32m[+]\x1b[0m')
        print('\x1b[1;32m[+]\x1b[0m \x1b[1;33mJoin Group Whatsapp For News and Update\x1b[0m      \x1b[1;32m[+]\x1b[0m')
        print('\x1b[1;31m====================================================\x1b[0m')
        print("Disclaimer : \nScript Not Working Don't Blame Creator :). \nRead/Watch How to Use As Well")
        print('\x1b[1;31m====================================================\x1b[0m')
        print(kuning + 'Info :' + info['notice5'] + putih)
        print('\x1b[1;31m====================================================\x1b[0m')
        print(hijau + 'Information Script :')
        print('Versi :', info['versi'])
        print('Creator :', info['created'])
        print('Youtube :', info['youtube'])
        print('Script :', info['script'] + putih)
        if '3.0' == version:
            print(hijau + 'New Version' + putih)
        elif  version > '3.0': # -> float required not str
            print(merah + 'New Version ' + version + ' Release' + putih)
            print(merah + 'Please Update' + putih)
            print(hijau + 'Type This Command:\n- git stash\n- git pull' + putih)
            sys.exit()
            print(kuning + 'Notice :\n' + info['notice1'])
            print(info['notice2'])
            print(info['notice3'])
            print(info['notice4'])
            print('- Attention to Your Connection' + putih)
            print('Buy License Here : \nhttps://layscape.xyz/selenia/license')
            print('')
            if statslogin == 'Online':
                print(hijau + 'Re-Login for Refresh', putih)
                try:
                    if Expired <= 0:
                        print(merah + 'License Out of Date' + putih)
                        print(kuning + 'Buy New One' + putih)
                        sys.exit()
                    else:
                        pass
                except:
                    pass
                else:
                    print('Informasi Status Login :', hijau + statslogin + putih)
                    print('Account ID :', accid)
                    print('Username :', Username)
                    print('Doge Balance :', num_format(dogebalance))
                    print('Doge Deposit Wallet :', dogewallet)
                    print('License Type : ', logintype)
                    if logintype == 'Free License':
                        statssrv = 'Offline'
                        print('Expired Date : None')
                        print('SG Server Status :', merah + statssrv + putih)
                        print('Max Balance : 150 DOGE')
                    else:
                        if not logintype == 'Premium License':
                            if logintype == 'Platinum License':
                                pass
                        statssrv = 'Online'
                        mydatetime = datetime.now()
                        print('SG Server Status :', hijau + statssrv + putih)
                        print('Date :', mydatetime.strftime('%Y-%m-%d'))
                        print('Expired Date :', userdate)
                        print('Expired In :', Expired, 'Days')
                        print('Max Balance : Unlimited')
                    print('Currency Available : DOGE')
                    print('Information Status Login :', statslogin)
                    print(hijau + '\nPilih Menu :')
                    print(kuning + '1. Login Premium License')
                    print('2. Login For Free')
                    print('3. Login Platinum License')
                    print('4. Register Account SELENIA')
                    print('5. Price List License')
                    print('0. Keluar')
                    if statslogin == 'Online':
                        print('6. Start Trade')
                        print('7. Withdraw')
                        print('8. Account Information')
                        smenu = input('==>')
                        if smenu == '1':
                            limit = 0
                            logintype = 'Premium License'
                            login()
                            verify()
                            check_license()
                        if smenu == '2':
                            logintype = 'Free License'
                            login()
                            limit = dogebalance
                            verify()
                        if smenu == '3':
                            limit = 0
                            logintype = 'Platinum License'
                            login()
                            verify()
                            check_license_platinum()
                        if smenu == '4':
                            register()
                        if smenu == '6':
                            if statslogin == 'Online':
                                if logintype == 'Free License':
                                    gblnc()
                                    limit = dogebalance
                                else:
                                    pass
                                autobet(limit)
                        if smenu == '5':
                            harga_license()
                        if smenu == '7':
                            if statslogin == 'Online':
                                withdraw()
                        if smenu == '8':
                            if statslogin == 'Online':
                                ainfo()
                        if smenu == '0':
                            sys.exit()
                        print('NO MENU SELECTED')
else:
    pass
