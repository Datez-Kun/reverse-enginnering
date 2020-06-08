import sys , os , socket
from platform import system

try:
	subdoms = ['webmail' , 'ftp' , 'direct' , 'cpanel']
	site = sys.argv[1]
	# Cleaning the sh*t
	if 'http://' in site:
		site = site.replace('http://' , '')
	if 'www' in site :
		site  = site.replace('www' ,'')
	if site[-1] == '/':
		site[-1] = ''
		
	ip = socket.gethostbyname(site)
	
	for subdom in subdoms:
		doo = subdom + '.' + site
		try:
			ddd = socket.gethostbyname(doo)
			if ip != ddd:
				print ' Found ---> %s\n'%(ddd)
			else :
				print ' Fail 404 Not Found <---'
		except:
			pass
	
	
	
except IndexError:
	sys.exit()
