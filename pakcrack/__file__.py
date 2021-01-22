# Filenames : <tahm1d>
# Python bytecode : 2.7
# Time decompiled : Thu Sep 10 23:27:42 2020
# Selector <module> in line 4 file <tahm1d>
# Timestamp in code: 2020-09-02 17:33:14

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

