# Filenames : pycompyle.py
# Python bytecode : 2.7
# Time decompiled : Fri Sep 11 00:04:59 2020
# Selector <module> in line 1 file pycompyle.py
# Timestamp in code: 2020-09-10 17:43:30

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import base64, imp, os, StringIO, zlib
__all__ = []
__version__ = '1.0.0'
__date__ = '2020/09/02'
__doc__ = 'PyCompyle\n\tScript to make pyc anti-decompiler.\nUsage : python2 -m pycompyle file'
__FILES = {}
__os_path_exists = os.path.exists
__builtin_open = open
___ = lambda x, y: ('').join([ chr(ord(x[i]) ^ ord(y[(lambda x, y: x % y if x % y >= 0 else y)(i, len(y))])) for i in range(len(x)) ])
__b64d = base64.decodestring
__zlibd = zlib.decompress

def __comb_open(filename, *args, **kwargs):
    if filename in __FILES:
        return StringIO.StringIO(__FILES[filename])
    else:
        return __builtin_open(filename, *args, **kwargs)


def __comb_exists(filename, *args, **kwargs):
    if filename in __FILES:
        return True
    else:
        return __os_path_exists(filename, *args, **kwargs)


open = __comb_open
os.path.exists = __comb_exists
sys.path[0:0] = ['.SELF/']
__FILES['.SELF/pycompyle/__init__.py'] = __zlibd(__b64d('\\eJzjUlZIzS0oqVRIy8xJ5QIAHdMERw=='))
sys.modules['pycompyle'] = imp.new_module('pycompyle')
sys.modules['pycompyle'].open = __comb_open
exec __FILES['.SELF/pycompyle/__init__.py'] in sys.modules['pycompyle'].__dict__
__FILES['.SELF/pycompyle/__main__.py'] = ___(__zlibd(__b64d('\\eJzFlOtv4kYQwP91J9V5YxGtm+NyTbk8Kh5ClcmHU9RIyZWrvSbGeAOmYY0VYpucgUDcw4jkUhlI\nQtfgXEiPfu1J/jCzO955/Wb2h0RB3WAoJGCVKbc1x8U4N06vVOSJak3BkJxcuLjhloZkv3hlSqMa\ndDXn6Vb2DLuloCdVCjjHqylP6qlHcD6eXpFxH0Qvp0yTSMUuAu/3oQDgI8FdZAdBuS1jGsC1Yvsb\niYyMe6rmk8aoIn7mufvC1aX+rmAkemvisXdRsm23fN4bnHwyH0p6Im8oB3bz+HHrSH+XP0X5L1Yr\nvjVqltOvlY89qxu//t2YHia45MxdvyIOAs2r6f/lK/jzQTLfjv9yDurupBo/ZMAKoD9avom8Aiay\nPlXgYZQXM0Bh2EHNckulFGM/fGlPnKZvmuPPzn0inoNp6lEIhgTEBaxfnWgeqGeB+R5wOa7Qroip\n+3LLYNuGlmreuWMgjGAoO3epF8bsLYgJDnQlOBd+S8APAHcJFhyQ5ItZgPwSewNBHQJBkkagKFRE\nwdA7Ik5h3OHrSXg7z/2+0mgBaYLEpxasCswkB6FHYH9nFmr42e0zq4eGYU1o2BIzQvqAnxfh5RXN\ni78IEPKJTQrSgL52ogdo6w9O80PVnhrFjsi+zKWeaq7OwkaedjpQ4G0M3uzAG6B3ZNjTrZQTO3q9\nlQSvhCYbXq2tzFSa1PqvMXi8+fPBxvbx5k95CEIbIj0aZX9Gziy8UGifFPxCgzaXBKePFTStiCRg\neqo8qSCfX4g/BifOsE8PYzCH6n4hwiM6pNmpdsbUpzrzSS12+IjqjFwclfQrxEZmcPWrWWAit4Zv\na2ybMBOl0eJCQjqK7PPOTaBS7JPw7sMY/gK4jGn2IqjO3ZoiqA5t33Mw1dNvOqJmqhZ9PLWsvLm/\np9rVQAthm785g5w7H1UaPj8k8zEMhinG8kpaW+OSXLmlFnuIrS5l2J4jREKEeO6yv6utndPZyQIq\n76Sf5b0FeXtukxyDeQ3DT9NHRPEwMziTJ/xzX7JAfbaRmD6+CHR28SRA+JLfzYLdxcN7ozhFLN05\nGRFPA9kTiz0+8hWoFyM6lWFB6FT+i23rmgEZA3ty5CKo6aPasC2pAQoJ6VJjqdiRhwOl4UHamnCO\nlnrxSxpR1T7BUwrGAnWZ8HeW0PJ+fSe2dKuwXUW+lnUhhP9NxDYEL0fDFBRxAMKFcLO6/XEDCOvw\nlg+v0mszVbWEV+tZsHf049v85t7R7lYSLi3CAuRctLVS4aiqLs0iXF//75zGYFgfA0+wTqP6XiVa\ntvrOKR6CYgvSm28GZ6GG8x1u4OmZ1QHsAgk/CKThGY1Ihel/AONaaaA=')), __b64d((lambda x, y: x(x, y))(lambda x, y: y and chr(y % 256) + x(x, y // 256) or '', 1278621296)))
sys.modules['pycompyle.__main__'] = imp.new_module('pycompyle.__main__')
sys.modules['pycompyle.__main__'].open = __comb_open
sys.modules['pycompyle'].__main__ = sys.modules['pycompyle.__main__']
exec __FILES['.SELF/pycompyle/__main__.py'] in sys.modules['pycompyle.__main__'].__dict__
from pycompyle.__main__ import compile

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    rv = 0
    for filename in args:
        try:
            rv = compile(filename)
        except Exception as err:
            rv = 1
            return str(err)

    return hex(rv)


if __name__ == '__main__':
    sys.exit(main())

