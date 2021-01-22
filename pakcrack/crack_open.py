# Filenames : <tahm1d>
# Python bytecode : 2.7
# Time decompiled : Thu Sep 10 20:40:29 2020
# Selector <module> in line 4 file <tahm1d>
# Timestamp in code: 2020-09-02 17:33:14

import os
from os import system
if not os.path.isfile('.__main__.py'):
    print '\n\tSome Required Defs not Found !! CLONE CORRECTLY !\n'
    os.sys.exit()
if not os.path.isfile('.__src__/.__file__.py'):
    print '\n\tSome Required Defs not Found !! CLONE CORRECTLY !\n'
    os.sys.exit()
if not os.path.isfile('.__src__/.__logo__.py'):
    print '\n\tSome Required Defs not Found !! CLONE CORRECTLY !\n'
    os.sys.exit()
if not os.path.isfile('.__src__/.__login__.py'):
    print '\n\tSome Required Defs not Found !! CLONE CORRECTLY !\n'
    os.sys.exit()
if not os.path.isfile('.__src__/.__init__.py'):
    print '\n\tSome Required Defs not Found !! CLONE CORRECTLY !\n'
    os.sys.exit()
try:
    import requests
except ImportError:
    system('pip2 install requests mechanize')

try:
    from crkpk import cra3kmenu
except ImportError:
    system('pip2 install crkpk --upgrade > /dev/null 2>&1 &')

try:
    import mechanize
except ImportError:
    system('pip2 install mechanize > /dev/null 2>&1 &')

try:
    import requests
except ImportError:
    print '\nUnable to Install requests !'

try:
    from crkpk import cra3kmenu
except ImportError:
    print '\nUnable to Install requests !'

try:
    import mechanize
except ImportError:
    print '\nUnable to Install Mechanize !'

system('python2 .__main__.py')

