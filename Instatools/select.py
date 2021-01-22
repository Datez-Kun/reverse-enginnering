# Filenames : 
# Python bytecode : 3.8
# Time succses decompiled Sat Sep 19 17:02:28 2020
# Selector select in line 93 file 
# Timestamp in code : 2020-07-16 04:45:22

for _ in range(3):
    try:
        choice = input('   >>> ')
        if choice == '':
            break
        elif not choice.isdigit():
            break
        else:
            if int(choice) < min:
                pass
            if int(choice) > max:
                pass
            return choice
    except Exception:
        POSITION()

else:
    info('Refresh', POSITION)


#Instruction context error:
#   
# L. 102        54  POP_BLOCK        
#->                56  JUMP_BACK             8  'to 8'
#                  58  JUMP_FORWARD         88  'to 88'
#                60_0  COME_FROM            52  '52'
