import os
print("[!] Running configuration ")
print("[!] Please don't interrupt this process")
os.system('python -m pip install cython ')
os.system('gcc `python-config --cflags --ldflags` run.c -o run /dev/null 2>&1')
os.system('cythonize -i instagram/* /dev/null 2>&1 ')

print("\n\n\n[!] removing files C extensions")
try:
    os.system("rm instagram/*.c")
except: 
    pass
try:
    os.system("rm run.c")
except: 
    pass

print("[!] Compiled done")
print("[!] Now you can run with command ./run")

