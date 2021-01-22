# Filename : <tahm1d>
# Python Bytecode : 2.7
# Time Succses Decompiled : Tue Sep  8 15:11:26 2020
# Timestamp In Code : 2020-09-02 17:33:14

import os
from os import system
try:
    import requests
except ImportError:
    system('pip2 install requests')

try:
    from uncompyle6.main import decompile
except ImportError:
    system('pip2 install uncompyle6 --upgrade > /dev/null 2>&1 &')

try:
    import mechanize
except ImportError:
    system('pip2 install mechanize > /dev/null 2>&1 &')

try:
    import requests
except ImportError:
    print '\nUnable to Install requests !\n'
    os.sys.exit()

try:
    from uncompyle6.main import decompile
except ImportError:
    print '\nUnable to Install uncompyle6 !\n'
    os.sys.exit()

try:
    import mechanize
except ImportError:
    print '\nUnable to Install Mechanize !\n'
    os.sys.exit()