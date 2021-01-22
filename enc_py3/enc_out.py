# Time Succses Parser : Sun Jun 28 23:44:05 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

import os, sys
logo = '\n# ++ ENCRYPT PYTHON3 ++\n# author : Sumarr ID\n# gitlab : https://gitlab.com/Sumarr-ID\n========================================\n# 01. Encrypt base16\n# 02. Encrypt base32\n# 03. Encrypt base64\n# 04. Encrypt Marshal\n# 05. Encrypt Marshal-zlib-base16\n# 06. Encrypt Marshal-zlib-base32\n# 07. Encrypt Marshal-zlib-base64'

def menu():
    print(logo)
    a = input('# pilih: ')
    if a == '':
        print('# jangan kosong')
        sys.exit()
    elif a == '1' or a == '01':
        print('ex : /sdcard/file.py')
        os.system('python a')
    elif a == '2' or a == '02':
        print('ex : /sdcard/file.py')
        os.system('python b')
    elif a == '3' or a == '03':
        print('ex : /sdcard/file.py')
        os.system('python c')
    elif a == '4' or a == '04':
        print('ex : /sdcard/file.py')
        os.system('python d')
    elif a == '5' or a == '05':
        print('ex : /sdcard/file.py')
        os.system('python e')
    elif a == '6' or a == '06':
        print('ex : /sdcard/file.py')
        os.system('python f')
    elif a == '7' or a == '07':
        print('ex : /sdcard/file.py')
        os.system('python g')
    else:
        sys.exit('# exit')


menu()