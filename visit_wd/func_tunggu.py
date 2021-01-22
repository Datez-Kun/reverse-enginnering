# Filename : <zen_ezz>
# Python Bytecode : 3.8
# Time Succses Decompiled : Mon Aug 24 02:42:28 2020
# Timestamp In Code : 2020-06-25 21:39:46

sys.stdout.write('\r')
sys.stdout.write('                                                               ')
for remaining in range(x, 0, -1):
    sys.stdout.write('\r')
    sys.stdout.write('\x1b[1;35mSTATUS VISIT    : \x1b[1;36mWait \x1b[1;32m{:2d} \x1b[1;36mseconds '.format(remaining))
    sys.stdout.flush()
    sleep(1)


