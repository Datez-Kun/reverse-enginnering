# -*- coding:utf-8 -*-
import os, sys
os.system('clear')

r = '\033[1;31m'
g = '\033[92;1m'
y = '\033[1;33m'
c = '\033[34;1m'
w = '\033[1;37m'
n = '\033[0;00m'
br = '\033[91;7m'
a = '\033[90m'

def logo():
  logo = a+'''
88  88    db     dP""b8 88  dP 888888 88""Yb
88  88   dPYb   dP   `" 88odP  88__   88__dP
888888  dP__Yb  Yb      88"Yb  88""   88"Yb
88  88 dP""""Yb  YboodP 88  Yb 888888 88  Yb
                '''+w+'''All Page Links '''+r+'''Search..........'''

  logo2 = w+'''
</------------'''+br+g+''' CapthaCode404_'''+n+w+''' -------------/>'''
  print logo
  print logo2
def input():
  print
  print w+"ex : www.nasa.gov / nasa.gov ( Do Not Use HTTP / HTTPS )"
  link = raw_input(g+"#"+r+"> "+g)
  print
  output = g+'''['''+a+'''+++++++++++'''+r+'''RESULT'''+a+'''+++++++++++'''+g+''']'''+w
  print output
  os.system('lynx -listonly -dump '+link)
  print
  end = g+'''['''+a+'''+++++++++++'''+r+'''END OUTPUT'''+a+'''+++++++++++'''+g+''']'''+n
  print end
  print
  about = g+'.::['+w+' Tools ini berfungsi sebagai scanner link di website. bisa juga untuk mencari sqli point dan admin finder.'+g+']::.'
  about3 = y+'Developer Security45 - BlackCoderCruh'+n
  print about
  print about3
logo()
input()
