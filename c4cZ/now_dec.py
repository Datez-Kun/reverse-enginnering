# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.2
# At Thu Apr  9 13:47:24 WIB 2020
"""
Recode? Pantek kali kao
"""
module = [
 'os', 'sys', 'random', 'http.cookiejar', 'json', 'time', 'urllib.request', 're']
import os, sys, random, http.cookiejar, json, time, urllib.request, re
for q in module:
    print('Setting up %s' % q)
    time.sleep(0.09)
else:
    red = '\x1b[1;91m'
    green = '\x1b[1;92m'
    yellow = '\x1b[1;93m'
    blue = '\x1b[1;94m'
    magenta = '\x1b[1;95m'
    cyan = '\x1b[1;96m'
    white = '\x1b[1;97m'
    normal = '\x1b[0;39m'
    print('Setting up fake_useragent')
    time.sleep(0.09)
    try:
        from fake_useragent import UserAgent
        user_agent = UserAgent()
    except ImportError:
        os.system('python3 -m pip install fake-useragent')
        from fake_useragent import UserAgent
        user_agent = UserAgent().random
    except Exception:
        exit('%s{%sRestart tool script%s}%s' % (white, green, white, normal))
    else:
        print('Setting up requests')
        time.sleep(0.09)
        try:
            import requests
        except ImportError:
            os.system('python3 -m pip install requests')
            import requests
        else:
            print('Setting up mechanize')
            time.sleep(0.09)
    try:
        import mechanize
    except ImportError:
        os.system('python3 -m pip install mechanize')
        import mechanize
    else:
        print('Setting up bs4')
        time.sleep(0.09)
        try:
            from bs4 import BeautifulSoup as soup
        except ImportError:
            os.system('python3 -m pip install bs4')
            from bs4 import BeautifulSoup as soup
        else:
            os.system('clear')
            end = ''.join(re.findall('[a-z]', 'EIPJCIOBCOUBDIWOVDHIOXJIDVHOFHOnIDOWHOIVCXUSBUBDUIWGCKGEIFVWGIDWIIWDGIXBGUDBIWHDaWOPJDDPOXMDJPFUROVURIBYGEPOQYPGBRVCRMFIOnOXMHEWFXHLREWPRMPQEWFUILEWUIWGPIRUHCFMFBRRVCUFEIWtIOJPWG5IOPGHRUPQFHRMCJROQPMCJRGIRIOaHUISOGHRLCMGCOHUTCGUTHWIGHRQIEPgHRWHIGPWQHTURTMCUGHUTMHUOIMJFEIHEUHLRGIHaHEIWOHQGUP4WHMXHUGMHRInHUEWGHUQOWCHMUQWGHRQUIsIQOFIPHEICFHICHFMXRHGUIHFEPQHN'))
            banner = '\x1b[1;92m╔═╗\x1b[1;91m┌─┐┌─┐┬ ┬\x1b[1;92m╦ ╦╦═╗\x1b[1;91m┬  ┬┌─┐┬┌─┌─┐\n\x1b[1;92m║\x1b[1;91m  ├─┤└─┐├─┤\x1b[1;92m╚═╣║\x1b[1;91m  │  ││  ├┴┐┌─┘\n\x1b[1;92m╚═╝\x1b[1;91m┴ ┴└─┘┴ ┴  \x1b[1;92m╩╩═╝\x1b[1;91m┴─┘┴└─┘┴ ┴└─┘ \x1b[1;92mBotZ\n\x1b[1;96mAuthor\x1b[0;39m : \x1b[1;96mNanta ID\n\x1b[1;96mGithub \x1b[0;39m: \x1b[4;93mgithub.com/R3DB0T\x1b[0;39m\n'

            def cekPass(pwd):
                password_tul = open('/data/data/com.termux/files/usr/share/.cash4clickz.passwordscript', 'r').read()
                if pwd == password_tul:
                    print('%s{%sPASSWORD CORRECT%s}%s' % (white, green, white, normal))
                    time.sleep(1.5)
                else:
                    print('%s{%sPASSWORD INCORRECT%s}%s' % (white, red, white, normal))
                    time.sleep(1.5)
                    menu()


            def add_reff():
                gets = 0
                br = mechanize.Browser()
                user = input('%s{%sInput User%s}> %s' % (white, green, white, normal))
                br.open('https://cash4clickz.com/dashboard/invite.php?invite=' + user)
                try:
                    amount = int(input('%s{%sInput Amount%s}> %s' % (white, green, white, normal)))
                except ValueError:
                    exit('%s{%sAmount must number%s}%s' % (white, red, white, normal))
                else:
                    if amount >= 100000:
                        exit("%s{%sDon't add amount too much%s}%s" % (white, red, white, normal))
                for i in range(amount):
                    try:
                        userag = user_agent.random
                        data = requests.get('https://randomuser.me/api').json()
                        name = data['results'][0]['name']['first'] + ' ' + data['results'][0]['name']['last']
                        user_name = data['results'][0]['login']['username']
                        email = data['results'][0]['email']
                        pswd = data['results'][0]['login']['password'] + '1234567890' if len(data['results'][0]['login']['password']) < 8 else data['results'][0]['login']['password']
                        br.select_form(nr=0)
                        br.form['name'] = name
                        br.form['username'] = user_name
                        br.form['email'] = email
                        br.form['password'] = pswd
                        br.form['password2'] = pswd
                        br.find_control('terms').items[0].selected = True
                        br.submit()
                        respon = requests.get(('https://cash4clickz.com/dashboard/invite.php?invite=' + user), headers={'User-Agents': userag})
                        gets += 1
                    except:
                        pass
                    else:
                        sys.stdout.write('\r%s from %s, %sSuccess%s: %s' % (i + 1, str(amount), green, normal, str(gets)))
                        sys.stdout.flush()
                else:
                    exit('\n%s{%sCompleted%s}%s' % (white, green, white, normal))


            def add_click():
                stat = ''
                ipt = 0
                user = input('%s{%sInput User%s}> %s' % (white, green, white, normal))
                try:
                    amount = int(input('%s{%sInput Amount%s}> %s' % (white, green, white, normal)))
                except ValueError:
                    exit('%s{%sAmount must number%s}%s' % (white, red, white, normal))
                else:
                    if amount >= 100000:
                        exit("%s{%sDon't add amount too much%s}%s" % (white, red, white, normal))
                for i in range(amount):
                    try:
                        userag = user_agent.random
                        component = urllib.request.Request(('https://cash4clickz.com/dashboard/invite.php?invite=' + user),
                          data=None,
                          headers={'User-Agent': userag})
                        hor = urllib.request.urlopen(component)
                        if hor.status != '200':
                            stat = 'OK'
                            ipt += 1
                    except:
                        stat = 'BAD'
                    else:
                        print('User: %s, click status: %s, %s from %s.' % (user, stat, str(ipt), str(amount)))
                else:
                    exit('%s{%sCompleted%s}%s' % (white, green, white, normal))


            def login_acc():
                br = mechanize.Browser()
                br.set_cookiejar(http.cookiejar.LWPCookieJar())
                br.set_handle_equiv(True)
                br.set_handle_gzip(True)
                br.set_handle_redirect(True)
                br.set_handle_referer(True)
                br.set_handle_robots(False)
                br.open('https://cash4clickz.com/dashboard/login.php')
                br.select_form(nr=0)
                br.set_handle_redirect(True)
                br.set_handle_referer(True)
                if os.path.exists('cash4clickz.login'):
                    if os.path.getsize('cash4clickz.login') != 0:
                        usern, user_pass = open('cash4clickz.login', 'r').read().split('?')
                    else:
                        usern = input('%s{%sUsername%s}> %s' % (white, green, white, normal))
                        user_pass = input('%s{%sPassword%s}> %s' % (white, green, white, normal))
                        with open('cash4clickz.login', 'w') as yut:
                            yut.write(usern + '?' + user_pass)
                else:
                    usern = input('%s{%sUsername%s}> %s' % (white, green, white, normal))
                    user_pass = input('%s{%sPassword%s}> %s' % (white, green, white, normal))
                    with open('cash4clickz.login', 'w') as yut:
                        yut.write(usern + '?' + user_pass)
                br.form['username'] = usern
                br.form['password'] = user_pass
                br.submit()
                data = br.open('https://cash4clickz.com/dashboard/index.php')
                data = br.response().read()
                data = soup(data, 'html.parser')
                getz = data.find_all('h1', class_='card-stat-num')
                click = getz[0].text
                refferal = getz[1].text
                tasks = getz[2].text
                earning = getz[3].text
                print('%s[ %sAccount Info %s]%s' % (white, green, white, normal))
                print('%sUser%s: %s%s' % (green, white, normal, usern))
                print('%sClicks%s: %s%s' % (green, white, normal, click))
                print('%sRefferals%s: %s%s' % (green, white, normal, refferal))
                print('%sTasks%s: %s%s' % (green, white, normal, tasks))
                print('%sEarnings%s: %s%s' % (green, white, normal, earning))
                input('\n\nEnter to back ')
                menu()


            def change_acc():
                if os.path.exists('cash4clickz.login'):
                    usern = input('%s{%sUsername%s}> %s' % (white, green, white, normal))
                    user_pass = input('%s{%sPassword%s}> %s' % (white, green, white, normal))
                    with open('cash4clickz.login', 'w') as yut:
                        yut.write(usern + '?' + user_pass)
                    input('%sAccount Changed!\n%s{%sEnter to back%s}> %s' % (green, white, green, white, normal))
                    menu()
                else:
                    input('%sLogin log not found!\n%s{%sEnter to back%s}> %s' % (red, white, green, white, normal))
                    menu()


            def info_script():
                global banner
                os.system('clear')
                print(banner)
                print('%sThanks to%s: %sAll Member Group Chat Python Tutorial%s' % (green, white, cyan, normal))
                print('%sDate%s: %s12 January 2020 on 4:30 p.m%s' % (green, white, cyan, normal))
                print('%sContact WhatsApp%s: %s+6282232906037%s' % (green, white, cyan, normal))
                print('%sTools Version%s: %s1.0%s' % (green, white, cyan, normal))
                print('%sDonate%s: %sOVO +6283132588696%s' % (green, white, cyan, normal))
                input('\n\nPress enter to back')
                menu()


            def menu():
                os.system('clear')
                print(banner)
                print('%s{%s01%s}%s Add Refferal + Click (Premium)' % (white, green, white, normal))
                print('%s{%s02%s}%s Add Click (Premium)' % (white, green, white, normal))
                print('%s{%s03%s}%s Account' % (white, green, white, normal))
                print('%s{%s04%s}%s Change Account' % (white, green, white, normal))
                print('%s{%sII%s}%s Tool Info' % (white, green, white, normal))
                print('%s{%sEX%s}%s For exit, type randomly' % (white, red, white, normal))
                tul = input('%s==%s> %s' % (cyan, green, normal))
                if '1' in tul:
                    confirmation = input('%sinput tool password\n    %s==%s> %s' % (green, cyan, green, normal))
                    cekPass(confirmation)
                    add_reff()
                elif '2' in tul:
                    confirmation = input('%sinput tool password\n    %s==%s> %s' % (green, cyan, green, normal))
                    cekPass(confirmation)
                    add_click()
                elif '3' in tul:
                    login_acc()
                elif '4' in tul:
                    change_acc()
                elif 'I' in tul.upper():
                    info_script()
                else:
                    exit('%s{%sThanks For Using%s}%s' % (white, green, white, normal))


            if __name__ == '__main__':
                try:
                    if os.path.exists('/data/data/com.termux/files/usr/share/.cash4clickz.passwordscript'):
                        if os.path.getsize('/data/data/com.termux/files/usr/share/.cash4clickz.passwordscript') != 0:
                            menu()
                        else:
                            with open('/data/data/com.termux/files/usr/share/.cash4clickz.passwordscript', 'w') as hmz:
                                hmz.write(end)
                            menu()
                    else:
                        with open('/data/data/com.termux/files/usr/share/.cash4clickz.passwordscript', 'w') as hmz:
                            hmz.write(end)
                        menu()
                except KeyboardInterrupt:
                    exit('\n%s{%sInterrupted%s}%s' % (white, red, white, normal))
                except EOFError:
                    exit('\n%s{%sExitted%s}%s' % (white, red, white, normal))
                except Exception as uap:
                    try:
                        exit('%s{%s%s%s}%s' % (white, red, str(uap), white, normal))
                    finally:
                        uap = None
                        del uap
