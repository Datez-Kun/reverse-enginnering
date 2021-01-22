# Filename : <zen_ezz>
# Python Bytecode : 3.8
# Time Succses Decompiled : Mon Aug 24 02:41:31 2020
# Timestamp In Code : 2020-06-25 21:39:46

for c in itertools.cycle(['|', '/', '-', '\\']):
    if done:
        break
    else:
        sys.stdout.write('\x1b[1;36m\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
else:
    sys.stdout.write('\rDone!     ')


