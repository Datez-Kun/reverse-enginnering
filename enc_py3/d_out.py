# Time Succses Parser : Mon Jun 29 00:07:16 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

import marshal
kun = input('# file: ')
fileopen = open(kun, 'rb').read()
a = compile(fileopen, 'dg', 'exec')
m = marshal.dumps(a)
s = repr(m)
c = kun.replace('.py', 'e.py')
d = open(c, 'w').write('# Encrypt by Sumarr ID\n# RECODE_BERKELAS\nimport marshal\nexec(marshal.loads(' + s + '))')
print('# hasil: ' + c)