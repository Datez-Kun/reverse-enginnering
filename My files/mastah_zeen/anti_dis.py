# Disassemble At : Sun Aug 16 19:02:51 2020
# Method Name : <module> 
# File Name : anti.pyc

  1           0 JUMP_ABSOLUTE            6
              3 LOAD_CONST           34457 

        >>    6 LOAD_CONST               0 (-1)
              9 LOAD_CONST               1 (None)
             12 IMPORT_NAME              0 (time)
             15 STORE_NAME               0 (time)
             18 LOAD_CONST               0 (-1)
             21 LOAD_CONST               1 (None)
             24 IMPORT_NAME              1 (sys)
             27 STORE_NAME               1 (sys)

  3          30 LOAD_CONST               2 ('EzzKun')
             33 LOAD_CONST               4 (())
             36 LOAD_CONST               3 (<code object EzzKun at 0xaaaa5f50, file "tes.py", line 3>)
             39 MAKE_FUNCTION            0
             42 CALL_FUNCTION            0
             45 BUILD_CLASS         
             46 STORE_NAME               2 (EzzKun)

 14          49 SETUP_EXCEPT            11 (to 63)

 15          52 LOAD_NAME                2 (EzzKun)
             55 CALL_FUNCTION            0
             58 POP_TOP             
             59 POP_BLOCK           
             60 JUMP_FORWARD            17 (to 80)

 16     >>   63 DUP_TOP             
             64 LOAD_NAME                3 (EOFError)
             67 COMPARE_OP              10 (exception match)
             70 POP_JUMP_IF_FALSE       79
             73 POP_TOP             
             74 POP_TOP             
             75 POP_TOP             

 17          76 JUMP_FORWARD             1 (to 80)
        >>   79 END_FINALLY         
        >>   80 LOAD_CONST               1 (None)
             83 RETURN_VALUE        

# Disassemble At : Sun Aug 16 19:02:51 2020
# Method Name : EzzKun 
# File Name : anti.pyc

  3           0 LOAD_NAME                0 (__name__)
              3 STORE_NAME               1 (__module__)

  4           6 JUMP_ABSOLUTE           12
              9 LOAD_CONST           34460 

        >>   12 LOAD_CONST               0 (<code object __init__ at 0xaaaa5f08, file "tes.py", line 4>)
             15 MAKE_FUNCTION            0
             18 STORE_NAME               2 (__init__)
             21 LOAD_LOCALS         
             22 RETURN_VALUE        

# Disassemble At : Sun Aug 16 19:02:51 2020
# Method Name : __init__ 
# File Name : anti.pyc

  5           0 LOAD_CONST               1 (10)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (angka)

  6           9 LOAD_CONST               2 (0)
             12 LOAD_FAST                0 (self)
             15 STORE_ATTR               1 (apes)

  7          18 SETUP_LOOP              99 (to 120)
             21 LOAD_GLOBAL              2 (range)
             24 LOAD_FAST                0 (self)
             27 LOAD_ATTR                0 (angka)
             30 CALL_FUNCTION            1
             33 GET_ITER            
        >>   34 FOR_ITER                82 (to 119)
             37 STORE_FAST               1 (i)

  8          40 LOAD_GLOBAL              3 (time)
             43 LOAD_ATTR                4 (sleep)
             46 LOAD_CONST               3 (0.5)
             49 CALL_FUNCTION            1
             52 POP_TOP             

  9          53 LOAD_FAST                0 (self)
             56 DUP_TOP             
             57 LOAD_ATTR                1 (apes)
             60 LOAD_CONST               4 (1)
             63 INPLACE_ADD         
             64 ROT_TWO             
             65 STORE_ATTR               1 (apes)

 10          68 JUMP_ABSOLUTE           74
             71 LOAD_CONST           34470 

        >>   74 LOAD_GLOBAL              5 (sys)
             77 LOAD_ATTR                6 (stdout)
             80 LOAD_ATTR                7 (write)
             83 LOAD_CONST               5 ('\r\x1b[1;34m[\x1b[1;37m*\x1b[1;34m]\x1b[1;37m Tunggu Sampai ')
             86 LOAD_GLOBAL              8 (str)
             89 LOAD_FAST                0 (self)
             92 LOAD_ATTR                1 (apes)
             95 CALL_FUNCTION            1
             98 BINARY_ADD          
             99 CALL_FUNCTION            1
            102 POP_TOP             

 11         103 LOAD_GLOBAL              5 (sys)
            106 LOAD_ATTR                6 (stdout)
            109 LOAD_ATTR                9 (flush)
            112 CALL_FUNCTION            0
            115 POP_TOP             
            116 JUMP_ABSOLUTE           34
        >>  119 POP_BLOCK           

 12     >>  120 LOAD_CONST               6 ('\n\x1b[1;34m[\x1b[1;37m*\x1b[1;34m]\x1b[1;37m INI ISINYA !!!')
            123 PRINT_ITEM          
            124 PRINT_NEWLINE       
            125 LOAD_CONST               0 (None)
            128 RETURN_VALUE        
