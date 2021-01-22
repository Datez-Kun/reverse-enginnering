import marshal,dis

co = marshal.loads(open('Script-http-socks4.pyc').read()[8:])
dis.dis(marshal.loads(co.co_consts[-1]))
#open('1.pyc','wb').write('\x03\xf3\r\nd\x83\x8e^' + co.co_consts[-1])
