# py2 only
import marshal,sys,os

def Useles(py_,limit):
	with open(py_) as f:
		komtol = f.read()
	for cek in range(int(limit)):
		try:
			coms = (lambda ok: compile('foo = False\nif(foo):\n    bar = 0/0\n    bar = 0/0\n' + ok,'<module>','exec'))
			pico = (lambda pi: pi.replace('\x15Z\x02\x00d\x00\x00d\x00\x00','\x15Z\x02\x00\x84\x15\x00\x84\x01\x00'))
			with open('out.pyc','wb') as f:
				f.write(
					'\x03\xf3\r\n\xb0\xaa]_' +
					marshal.dumps(coms(komtol))
					)
			source = open('out.pyc').read()
			with open('out.pyc','wb') as f:
				f.write(pico(source))
			with open('out.py','wb') as f:
				f.write(
					"import marshal\nexec(marshal.loads(" +
					repr(open('out.pyc').read()[8:]) +
					"))"
					)
			komtol = open('out.py').read()
			print ' compiling at %s ' % (cek + 1)
		except Exception as e:
			sys.exit(str(e))
	print ' all done, saved to ``out.py``!'
	os.remove('out.pyc')

if __name__=="__main__":
	if len(sys.argv) < 2:
		sys.exit('usage : kompel.py [ file ] [ limit ]')
	else:
		Useles(sys.argv[1],sys.argv[2])
