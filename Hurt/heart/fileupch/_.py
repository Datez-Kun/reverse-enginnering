#!/bin/usr/python2.7.x

import os, re, urllib2

def main():
	ip = raw_input(" Target IP : ")
	check(ip)

def check(ip):
	try:
		print "Loading Check File Uploader...."
		print 58*"-"
		page = 1
		while page <= 21:
			bing = "http://www.bing.com/search?q=ip%3A" + \
			ip + "+upload&count=50&first=" + str(page)
			openbing = urllib2.urlopen(bing)
			readbing = openbing.read()
			findwebs = re.findall('<h2><a href="(.*?)"', readbing)
			sites = findwebs
			for i in sites:
				try:
					response = urllib2.urlopen(i).read()
					checksqli(i)
				except urllib2.HTTPError, e:
					str(sites).strip(i)
			page = page + 10
	except:
		pass

def checksqli(sqli):
    responsetwo = urllib2.urlopen(sqli).read()
    find = re.findall('type="file"', responsetwo)
    if find:
        print(" Found ---> " + sqli)
					
main()