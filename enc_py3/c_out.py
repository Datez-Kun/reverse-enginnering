# Time Succses Parser : Mon Jun 29 00:05:53 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

import base64
kun = input('# file: ')
ups = open(kun, 'rb').read()
ui = base64.b64encode(ups)
ex = kun.replace('.py', 'e.py')
cok = open(ex, 'w').write('# Encrypt by Sumarr ID\n# RECODE_BERKELAS\nimport base64\nexec(base64.b64decode(' + str(ui) + '))')
print('# hasil: ' + ex)
