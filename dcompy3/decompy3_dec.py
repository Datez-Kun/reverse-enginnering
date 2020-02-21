import marshal,random,os

try:
    import uncompyle6
except:
    os.system("pip install uncompyle6")
    try:
        import uncompyle6
    except:
        os.system("clear")
        exit("\033[1;91mOopps terjadi error\ncoba jalankan ulang\033[0m")

def echo(text):
    w = "mhkbucp"
    for c in w:
        text = text.replace(",%s"%(c),"\033[1;%dm"%(91+w.index(c)))
    text += "\033[0m"
    print(text)

n = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm')for _ in range(4))
nb = n+"-enc.py"
class fuck:
    def uncom(fl):
        try:
            files = open(fl,"r").read()
        except:
            echo(",mfile %s tidak ada"%(fl))
            exit()
        files = files.replace("import","import uncompyle6,")
        files = files.replace("exec(","uncompyle6.main.decompile(3.7,")
        files = files.replace("))","),open(\"pfft.py\",\"w\"))")
        try:
            exec(files)
        except:
            echo(",mdecompile gagal,p")
            exit()
        os.rename("pfft.py",nb)
        echo(",hhasil decompile => ,p%s"%(nb))

    def run():
        os.system("clear")
        echo(''',h
:::::::-.    .,-:::::     ...     .        :::::::::::..-:.     ::-. .::.
 ;;,   `';,,;;;'````'  .;;;;;;;.  ;;,.    ;;;`;;;```.;;;';;.   ;;;;';'`';;,
 `[[     [[[[[        ,[[     \[[,[[[[, ,[[[[,`]]nnn]]'   '[[,[[['     .n[[
  $$,    $$$$$        $$$,     $$$$$$$$$$$"$$$ $$$""        c$$"      ``"$$$.
  888_,o8P'`88bo,__,o,"888,_ _,88P888 Y88" 888o888o       ,8P"`       ,,o888"
  MMMMP"`    "YUMMMMMP" "YMMMMMP" MMM  M'  "MMMYMMMb     mM"          YMMP"
==============================================================================
			,hcoded by: ,pZhu Bai Lee
			,hTeam    : ,pBLACK CODER CRUSH''')
        try:
            fl = input("\033[1;92mfile: \033[0m")
            if len(fl) == 0:
                exit()
        except:
            exit("")
        return fuck.uncom(fl)

fuck.run()