# MENTOL 
# At:Thu Mar 12 20:16:21 2020 

"""
     Rebuild Copyright Can't make u real programmer
"""
import sys
if 'linux' in sys.platform.lower():
    W = '\x1b[1;37m'
    N = '\x1b[0m'
    R = '\x1b[1;37m\x1b[31m'
    B = '\x1b[1;37m\x1b[34m'
    G = '\x1b[1;32m'
    O = '\x1b[33m'
    C = '\x1b[36m'
    notice = ('{}{}[*]{} ').format(N, B, N)
    warning = ('{}[-]{} ').format(R, N)
    good = ('{}[!]{} ').format(G, N)
    warn = ('{}[!]{} ').format(O, N)
else:
    W = ''
    N = ''
    R = ''
    B = ''
    G = ''
    O = ''
    C = ''
    notice = ''
    warning = ''
    good = ''
    warn = ''
