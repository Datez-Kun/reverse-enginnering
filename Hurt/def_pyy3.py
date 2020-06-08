# Time Succses Parser : Mon Jun  8 17:06:19 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

print('\npyc\t\t\tDeobfuscate pyc to py\nother\n\t\t')
while True:
    try:
        self.py3command = input(' hurt(pythondeob/py3) > ')
        if self.py3command in ('pyc', ):
            try:
                os.mkdir('Python-Deobfuscate')
            except:
                pass
            else:
                try:
                    self.File = input('\n File : ')
                    self.op = open(self.File).read()
                    os.system('uncompyle6 %s >> Python-Deobfuscate/Result_pyc.py')
                    print(' Result : Python-Deobfuscate/Result_pyc.py')
                except IOError:
                    print(' File not Found')

        elif self.py3command in ('other', ):
            print(' You can Deobfuscate with Online or Manual Decompile')
        else:
            print(' Hurt err : not Found')
    except (KeyboardInterrupt, EOFError):
        Exit()
