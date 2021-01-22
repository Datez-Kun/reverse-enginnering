# Filename : dg
# Python Bytecode : 2.7
# Time Succses Decompiled : Sat Aug 29 01:49:16 2020
import os, sys, time, random, threading, random, socket, select, datetime, os, sys, random, socket, select, threading, datetime
lock = threading.RLock()
os.system('cls' if os.name == 'nt' else 'clear')
ARYA = '127.0.0.1'
BLITAR = '8080'
JANDA = 'iflix-video-s3.akamaized.net:443'
def real_path(file_name):
    return os.path.dirname(os.path.abspath(__file__)) + file_name


def filter_array(array):
    for i in range(len(array)):
        array[i] = array[i].strip()
        if array[i].startswith('#'):
            array[i] = ''

    return [ x for x in array if x ]


def colors(value):
    patterns = {'R1': '\x1b[31;1m', 'R2': '\x1b[31;2m', 
       'G1': '\x1b[32;1m', 'Y1': '\x1b[33;1m', 
       'P1': '\x1b[35;1m', 'CC': '\x1b[1;34m', 
       'B1': '\x1b[34;1m', 'L1': '\x1b[36;1m'}
    for code in patterns:
        value = value.replace(('[{}]').format(code), patterns[code])

    return value


def log(value, status='', color='[Y1]'):
    value = colors(('{color}[B1][L1]{color}{status} [Y1]{color}{value}[CC]').format(time=datetime.datetime.now().strftime(''), value=value, color=color, status=status))
    with lock:
        print value


def log_replace(value, status='MANTAP', color='[R1]'):
    value = colors(('{}{} ({})        [CC]\r').format(color, status, value))
    with lock:
        sys.stdout.write(value)
        sys.stdout.flush()


class inject(object):

    def __init__(self, inject_host, inject_port):
        super(inject, self).__init__()
        self.inject_host = str(inject_host)
        self.inject_port = int(inject_port)

    def log(self, value, color='[Y1]'):
        log(value, color=color)

    def start(self):
        try:
            socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_server.bind((self.inject_host, self.inject_port))
            socket_server.listen(1)
            frontend_domains = [('{}').format(JANDA)]
            frontend_domains = filter_array(frontend_domains)
            if len(frontend_domains) == 0:
                self.log('Aryatsel', color='[P1]')
                return
            self.log((' \n    \x1b[1;37m \xf0\x9f\x99\x8c\x1aQPYTHON BERHASIL \xf0\x9f\x98\x82\x1a\n ').format(self.inject_host, self.inject_port), color='[R1]')
            while True:
                socket_client, _ = socket_server.accept()
                socket_client.recv(65535)
                domain_fronting(socket_client, frontend_domains).start()

        except Exception as exception:
            self.log(('\x1b[1;31m Gagal.. hpus data apk python mulai lagi').format(self.inject_host, self.inject_port), color='[P1]')


class domain_fronting(threading.Thread):

    def __init__(self, socket_client, frontend_domains):
        super(domain_fronting, self).__init__()
        self.frontend_domains = frontend_domains
        self.socket_tunnel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client = socket_client
        self.buffer_size = 65535
        self.daemon = True

    def log(self, value, status=' ', color='[Y1]'):
        log(value, status=status, color=color)

    def handler(self, socket_tunnel, socket_client, buffer_size):
        sockets = [
         socket_tunnel, socket_client]
        timeout = 0
        while True:
            timeout += 1
            socket_io, _, errors = select.select(sockets, [], sockets, 3)
            if errors:
                break
            if socket_io:
                for sock in socket_io:
                    try:
                        data = sock.recv(buffer_size)
                        if not data:
                            break
                        elif sock is socket_client:
                            socket_tunnel.sendall(data)
                        elif sock is socket_tunnel:
                            socket_client.sendall(data)
                        timeout = 0
                    except:
                        break

            if timeout == 30:
                break

    def run(self):
        try:
            self.proxy_host_port = random.choice(self.frontend_domains).split(':')
            self.proxy_host = self.proxy_host_port[0]
            self.proxy_port = self.proxy_host_port[1] if len(self.proxy_host_port) >= 2 and self.proxy_host_port[1] else '80'
            self.log('\x1b[1;37m \xf0\x9f\x91\x89 PYTHON \x1b[1;33mMENGHUBUNGKAN \x1b[1;31m_______')
            self.socket_tunnel.connect((str(self.proxy_host), int(self.proxy_port)))
            self.socket_client.sendall('HTTP/1.1 200 OK\r\n\r\n')
            self.handler(self.socket_tunnel, self.socket_client, self.buffer_size)
            self.socket_client.close()
            self.socket_tunnel.close()
            self.log(('\x1b[1;37m \xf0\x9f\x94\x92 PYTHON \x1b[1;36mMENGHUBUNGKAN \x1b[1;32mCONNECT ').format(self.proxy_host, self.proxy_port), color='[CC]')
        except OSError:
            self.log('Ada yang Eror', color='[P1]')
        except TimeoutError:
            self.log(('{} not responding').format(self.proxy_host), color='[R1]')


R = '\x1b[31;1m'
Y = '\x1b[33;1m'
G = '\x1b[32;1m'
P = '\x1b[35;1m'
B = '\x1b[34;1m'
L = '\x1b[36;1m'
W = '\x1b[37;1m'
print B + ' '
print G + ' \x1a\xf0\x9f\x94\xa5 HALLO WHATSAPP GUYS ....!! \xf0\x9f\x9a\x80 '
print W + ' '

def spin():
    try:
        L = '\\/-\\/-\\|'
        for q in range(450):
            time.sleep(0.02)
            sys.stdout.write('\r  (' + L[(q % len(L))] + ')')
            sys.stdout.flush()

    except:
        exit()


spin()

def load():
    load = [
     '     \x1b[1;31mTUNGGU DULU \x1b[1;32m>---------10%', '     \x1b[1;33mTUNGGU DULU \x1b[1;34m>>-------- 20%', '     \x1b[1;35mTUNGGU DULU \x1b[1;36m>>>------- 30%', '     \x1b[1;37mTUNGGU DULU \x1b[1;31m>>>>------ 40%', '     \x1b[1;32mTUNGGU DULU \x1b[1;33m>>>>>----- 50%', '     \x1b[1;34mTUNGGU DULU \x1b[1;35m>>>>>>---- 60%', '     \x1b[1;36mTUNGGU DULU \x1b[1;37m>>>>>>>--- 70%', '     \x1b[1;31mTUNGGU DULU \x1b[1;32m>>>>>>>>-- 80%', '     \x1b[1;33mTUNGGU DULU \x1b[1;34m>>>>>>>>>- 90%', '        \x1b[1;37m\xf0\x9f\x92\x91 AKU SAYANG KAMU 100% \xf0\x9f\x92\x96\n        \xe2\x9e\x96\xe2\x9e\x96\xe2\x9e\x96\xe2\x9e\x96\xe2\x9e\x96\xe2\x9e\x96\xe2\x9e\x96\xe2\x9e\x96\xe2\x9e\x96\xe2\x9e\x96\xe2\x9e\x96\xe2\x9e\x96\xe2\x9e\x96']
    for o in load:
        print '\r' + o,
        sys.stdout.flush()
        time.sleep(0.99)


load()

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)


print '\x1b[0;95m'
mengetik(' ')
mengetik(' \x1b[1;37m              _       _ ')
mengetik(' ___  ___ _ __(_)_ __ | |_ ')
mengetik('/ __|/ __|  __| |  _ \\| __| ')
mengetik('\\__ \\ (__| |  | | |_) | |_ ')
mengetik('|___/\\___|_|  |_| .__/ \\__| ')
mengetik('                |_| ')
mengetik(' \x1b[1;34m  __ ___  _(_)___ ')
mengetik('  / _  \\ \\/ / / __| ')
mengetik(' | (_| |>  <| \\__ \\ ')
mengetik('  \\__,_/_/\\_\\_|___/ ')
mengetik(' \x1b[1;36m ____                 _ ')
mengetik(' / ___| __ _ _ __ ___ (_)_ __   __ _ ')
mengetik('| |  _ / _  |  _   _ \\| |  _ \\ / _  | ')
mengetik('| |_| | (_| | | | | | | | | | | (_| | ')
mengetik(' \\____|\\__,_|_| |_| |_|_|_| |_|\\__, | ')
mengetik('                                |___/ ')
mengetik('\x1b[1;32m ___       _                       _ ')
mengetik('|_ _|_ __ | |_ ___ _ __ _ __   ___| |_ ')
mengetik(' | ||  _ \\| __/ _ \\  __|  _ \\ / _ \\ __| ')
mengetik(' | || | | | ||  __/ |  | | | |  __/ |_ ')
mengetik('|___|_| |_|\\__\\___|_|  |_| |_|\\___|\\__| ')
mengetik('\x1b[1;31m  ____           _   _ ')
mengetik(' / ___|_ __ __ _| |_(_)___ ')
mengetik('| |  _|  __/ _  | __| / __| ')
mengetik('| |_| | | | (_| | |_| \\__ \\ ')
mengetik(' \\____|_|  \\__,_|\\__|_|___/ \n')

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.0)


mengetik('\x1b[1;32m \xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97 ')
mengetik(' \x1b[1;32m\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3\xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3 \xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x9d ')
mengetik(' \x1b[1;32m\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\xa9 \xe2\x95\xa9 \xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\xa9  \xe2\x95\xa9  \n')
mengetik(' \x1b[1;34m \xf0\x9f\x92\x96 BY GRUP BLITAR CANTIK \xf0\x9f\x92\x9d \n')
mengetik(' \x1b[1;37m  UPLOAD BY ARIS STYA CHANNEL ')
mengetik('   \x1b[1;34m=\x1b[1;35m=\x1b[1;36m=\x1b[1;37m=\x1b[1;32m=\x1b[1;31m=\x1b[1;34m=\x1b[1;33m=\x1b[1;36m=\x1b[1;35m=\x1b[1;37m=\x1b[1;31m=\x1b[1;32m=\x1b[1;34m=\x1b[1;35m=\x1b[1;36m=\x1b[1;37m=\x1b[1;31m=\x1b[1;32m=\x1b[1;33m=\x1b[1;34m=\x1b[1;35m=\x1b[1;36m=\x1b[1;37m=\x1b[1;31m=\x1b[1;32m=\x1b[1;33m= \n')
mengetik(' \x1b[1;37m \xf0\x9f\x91\x89 Psiphon to :\x1b[1;36m 127.0.0.1 :8080 \n')

def main():
    inject(ARYA, BLITAR).start()


if __name__ == '__main__':
    main()
