# Time Succses Parser : Sun Jun 28 23:16:47 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

import os, sys, py_compile, marshal
print '==========================================\n# ENCRYPT PYTHON\n# ANTI UNCOMPYLE6\n\n# author : Sumarr ID\n# gitlab : https://gitlab.com/Sumarr-ID\n=========================================='
print 'contoh : /sdcard/Download/sc.py'
a = raw_input('# file: ')
b = open(a).read()
y = open('au.py', 'w')
y.write('astaghfirullah=(\n')
for i in range(62431):
    y.write('"astaghfirullah","astaghfirullah","astaghfirullah","astaghfirullah",\n')

y.write(')\n')
a = compile(b, 'Sumarr', 'exec')
m = marshal.dumps(a)
s = repr(m)
y.write('# Encrypt by Sumarr ID\n# RECODE_BERKELAS\nimport marshal\nexec(marshal.loads(' + s + '))')
y.close()
py_compile.compile('au.py', 'ok.pyc')
os.system('rm au.py')
print '# hasil: ok.pyc'
