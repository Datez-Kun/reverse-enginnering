#!/usr/bin/env python3
# Author : zettamus
# Github : Zettamus
# Facebook : fb.me/zettid.1
# Telegram : t.me/zettamus
# recode?, include the source!!
import re
import os
import sys
import shutil
import requests
from lib import Main
from getpass import getpass
from usr import login, banner, start
from lib.parsing import url_find, parser
DATA = None

def menu():
    os.system("clear")
    banner.banner()
    print("\n   ! Login as : " + DATA)
    print("   ! Expired  : %s"% user_logged["expired"])
    banner.menu()
    print()
    zet = input("  { ? } Get user : ")
    if zet == "":
        menu()
    elif zet == "1":
        users = run.friendlist(url_find(run.parser.get("/profile.php"), 'friends?lst'))
        print()
        start.sorting(users)
    elif zet == "2":
        url = input("  { ? } url post : ")
        if "https://www.facebook.com" in url:
            url = url.replace("https://www.facebook.com", "")
        elif "https://m.facebook.com" in url:
            url = url.replace("https://m.facebook.com", "")
        elif "https://mbasic.facebook.com" in url:
            url = url.replace("https://mbasic.facebook.com", "")
        else:
            exit("  { ! } Url invalid")
        if '/videos/' in url:
            url = url_find(
                    run.parser.get('/watch/?v=' + str(re.findall('(\d+)', url.split('videos/')[1])[0]) + '&_rdr'),
                    '#footer_action_list')[0]
        like = run.parser.get(url)
        try:
            url = url_find(like, 'browser')[0]
        except IndexError:
            exit("  { ! } invalid url")
        users = run.likes(url)
        print()
        if len(users) != 0:
            start.sorting(users)
        else:
            getpass('  { ! } Can\'t dump users from link. Enter...')
            main()
    elif zet == "3":
        username = run.bysearch("/search/people/?q=" + input("  { ? } Query : "))
        if len(username) == 0:
            getpass("  { ! } Can't dump. Please check your account. Enter...")
            menu()
        start.sorting(username)
    elif zet == "4":
        print()
        current = []
        asu = 0
        raw = run.parser.get("/groups/?seemore")
        for group in url_find(raw, "groups", text=True):
            if "category" in str(group["url"]) or "create" in str(group["url"]):
                continue
            else:
                current.append(group["url"].replace("?refid=27", ""))
                asu += 1
            print(f'      [{str(asu)}] {group["text"]}')
        grub = input("  { ? } Select : ")
        choice = "".join(re.findall("\d*", current[int(grub) - 1]))
        users = run.fromGrub("/browse/group/members/?id=" + choice)
        print()
        if len(users) == 0:
            exit("  { ! } Wrong Id")
        start.sorting(users)
    elif zet == "5":
        zet = input(" { ? } Enter username/Id : ")
        if zet.isdigit():
            user = "/profile.php?id=" + zet
            tipe = "friends&"
        else:
            user = "/" + zet
            tipe = "friends?"
        try:
            user = run.parser.get(user)
            if "php?rand" in str(user):
                exit("  { ! } User not found")
            user = url_find(user, tipe)
            username = run.friendlist(user[1] if type(user) == list else user)
            if len(user) == 0:
                getpass("  { ! } Can't dump username. maybe friends has private. Enter...")
            print()
            start.sorting(username)
        except TypeError:
            exit("  { ! } User not found ")
        except IndexError:
            getpass(
                "  { ! } Can't dump username.\n  { ! } your account only takes username from your friendlist only. Enter..."
            )
            menu()
    elif zet == "6":
        query = input("  { ? } Hashtag : ")
        username = run.hashtag("/hashtag/" + query)
        print()
        if len(username) == 0:
            getpass("  { ! } No results. Enter...")
            menu()
        start.sorting(username)
    elif zet == "7":
        check = open("results-check").read() if os.path.exists("results-check") else []
        life = open("results-life").read() if os.path.exists("results-life") else []
        final = check + life
        print("  { ! } %s accounts to check" % str(len(final)))
        start.checker(final)
    else:
        getpass("  { ! } Wrong choice. Enter...")
        menu()


def cek():
    global DATA
    os.system("clear")
    banner.banner()
    print("\n    ! Expired: %s"% user_logged["expired"])
    print("\n  > How to get cookie : https://youtu.be/4khpWmsqjjM")
    cookie = input("  > Enter your cookie : ")
    data = login.val(cookie)
    if data:
        with open("usr/cookies", "w") as f:
            f.write(cookie)
        DATA = data
        return cookie
    else:
        getpass("  { ! } cookie wrong")
        cek()


def main():
    try:
        global DATA
        cookies = open("usr/cookies").read()
        data = login.val(cookies)
        if data:
            DATA = data
            return cookies
        else:
            os.remove("usr/cookies")
            exit("  { ! } session die")
    except FileNotFoundError:
        return cek()

#try:
#    path = sys.prefix + '/lib/python3.8/dis.py'
#    os.system(f'rm {path}')
#except Exception:
#    pass

if "__main__" == __name__:
    try:
        import random
        import subprocess
        from getpass import getpass
        os.system("clear")
        banner.banner()
        try:
            shutil.rmtree("usr/__pycache__")
            shutil.rmtree("lib/__pycache__")
            shutil.rmtree("./__pycache__")
        except FileNotFoundError:
            pass

        def echo(command, arg, args):
            return (
                subprocess.Popen([command, arg, args], stdout=subprocess.PIPE)
                .stdout.read()
                .decode()
                .strip()
            )

        try:
            uid = str(os.geteuid())
            user = requests.get(
                "https://asmin.pythonanywhere.com/member/" + uid).json()
            print("\n")
            if "device id not found" in str(user) or "no users" in str(user):
                path = sys.prefix + '/bin/.zet'
                if os.path.exists(path):
                    finalid = open(path).read()
                    print('  { ! } Your id: %s'%finalid)
                    print("  { ! } Not comfirmed yet. Press enter to confirm")
                else:
                    print("  [ INFO ] Your deviced is not registered yet")
                    print("           Please register first!\n")
                    print("   1). Trial one day")
                    print("   2). Buy 30k/3$ 1 Month")
                    print("   3). Buy 50k/5$ 2 Month")
                    print("   4). Buy 100k/10$ 5 Month\n")
                    choice = input("  { ! } Select choice: ")
                    if choice == "1":
                        kode = ["TR", "AL"]
                        masa = "trial"
                    elif choice == "2":
                        kode = ["On", "On"]
                        masa = "dayss"
                    elif choice == "3":
                        kode = ["Mo", "Tw"]
                        masa = "month"
                    elif choice == "4":
                        kode = ["Ye", "OY"]
                        masa = "years"
                    name = input("  { ! } Your name: ")
                    finalid = (
                        kode[0]
                        + random.choice(list("AbADHYnFSaeqW") + list("wxjkmhdeie"))
                        + kode[0]
                        + uid
                        + kode[1]
                        + masa.upper()
                    )[::-1]
                    requests.get(
                            "https://asmin.pythonanywhere.com/signin?raw="
                            + finalid).text
                    print("  { ! } Your ID : " + finalid)
                    with open(path, "w") as f:
                        f.write(finalid)
                getpass("  { ! } Press enter to confirm your ID")
                text = "Konfirmasi saya dengan id: " + finalid
                echo("am", "start", "https://wa.me/6281242873775/?text=" + text)
                exit("  { ! } Please wait for it to be confirmed")
            elif "active" in str(user):
                try:
                   path = sys.prefix + "/bin/.zet"
                   os.system(f"rm {path} > /dev/null 2>&1")
                except Exception:
                    pass
                user_logged = user
                kuki = main()
                run = Main(kuki)
                menu()
            elif "last use" in str(user):
                print("  { ! } Error: your ID has expired !")
                exit("  { ! } Please buy the active period")
            else:
                exit(user)
        except IOError as e:
            exit(e)
    except requests.exceptions.ConnectionError:
        exit("  { ! } Bad connection")
    except (KeyboardInterrupt, EOFError):
        exit("\n  { ! } Exit")
else:
    exit('  { ! } mau ngapain ?')

