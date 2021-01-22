# FileName : <zen_ezz>
# Python Bytecode : 3.8
# Time Succses Decompiled : Mon Aug 24 02:50:09 2020
# Timestamp In Code: 2020-06-25 21:39:46

if not os.path.exists('.password'):
    os.makedirs('.password')
pw = 'wonderwoman'
if not os.path.exists('.password/visit_password.txt'):
    f = open('.password/visit_password.txt', 'w+')
    f.write('file_ready')
    f.close()
for i in range(99):
    f = open('.password/visit_password.txt', 'r')
    if f.readlines()[0] == pw:
        break
    pwin = input('\x1b[1;35mLINK PASSWORD         \x1b[1;36m: https://bit.ly/3bx56wQ\n\x1b[1;35mINPUT PASSWORD        \x1b[1;36m: ')
    if pwin == pw:
        f = open('.password/visit_password.txt', 'w+')
        f.write(pwin)
        f.close()
        print('\x1b[1;35mSTATUS                \x1b[1;36m: Correct Password')
        break
    else:
        print('\x1b[1;35mSTATUS                \x1b[1;36m: Wrong Password\n')
        sys.exit()


