import os
class uncom:
    def unmarszlib():
        try:
            files = input("nama file: ")
        except:
            exit("")
        if len(files) == 0:
            exit("")
        try:
            bk = open(files,"r").read()
        except IOError:
            print("file tidak ada")
            exit()
        bk = bk.replace("import","import uncompyle6,")
        bk = bk.replace("exec(","uncompyle6.main.decompile(3.7,")
        bk = bk.replace(")))",")),open(\"hasil.py\",\"w\"))")
        try:
            exec(bk)
        except:
            exit("decompile gagal")
    def run():
        os.system("clear")
        logo = '''\033[1;92m
...    :::    .        :   :::::::::
 ;;     ;;;    ;;,.    ;;;  '`````;;;
[['     [[[    [[[[, ,[[[[,     .n[['
$$      $$$    $$$$$$$$"$$$   ,$$P"
88    .d888    888 Y88" 888o,888bo,_
 "YmmMMMM""    MMM  M'  "MMM `""*UMM
++++++++++++++++++++++++++++++++++++++++++++
+	 tools   : Uncompile Marshal Zlib  +
+	 coded by: ZHU BAI LEE             +
+	 team    : BLACK CODER CRUSH       +
++++++++++++++++++++++++++++++++++++++++++++'''
        print(logo)
        uncom.unmarszlib()

uncom.run()
