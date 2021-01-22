# Source Generated With Python 2.7
# Decompile At : Mon Apr  6 14:45:52 WIB 2020
# CODED BY : JHON
# CODENAME : E-XPLOIT1337 & MR-X666X
# TEAM WORK: BLACK CODERS ANONYMOUS & SEVEN GHOST TEAM
# TOOLS NM : PRIV8 SUPER FAST CMS DETECTORS

# SPECIAL THANKS TO MY BIG FAMILY :
# MAURITANIA ATTACKER, ANON GHOST TEAM, GHOST SQUAD HACKER
# ./K1TSUN3-6H057, SEA-GHOST, BROSE666, ./K4IZ3N-6H05T
# Z3R0H1D3N, K4TSUY4-GH05T, L4ZYXPL0I7, TAMPANSKY-ID

# HOW TO USE ON TERMUX?
# python2 1337.py

# THREADS POOL CAN BE CHANGED AGAIN
# THREADS POOL IS ON THE LINE 187

# INSTALL MODULE ON TERMUX :
# pip2 install -r requirements.txt

# !/usr/bin/python2.x
# -*- coding: utf-8 -*-

import datetime

import requests, threading

from multiprocessing.dummy import Pool

import os, sys, time

if os.name == "nt":

	os.system("cls")

else:

	os.system("clear")

def banner_logo():

    print ("""\033[1;95m
   _____ _               _     ______          _             
  / ____| |  \033[1;97mBCA \033[1;95m/ \033[1;97m7GT  \033[1;95m| |   |  ____|        | |            
 | |  __| |__   ___  ___| |_  | |__ _   _  ___| | _____ _ __ 
 | | |_ | '_ \ / _ \/ __| __| |  __| | | |/ __| |/ / _ \ '__|
 | |__| | | | | (_) \__ \ |_  | |  | |_| | (__|   <  __/ |   
  \_____|_| |_|\___/|___/\__| |_|   \__,_|\___|_|\_\___|_|   
\033[1;97m
     GHOST FUCKER VERY FAST CMS DETECTOR CODERS BY JHON
            \033[1;95m-- \033[1;97mPRIVATE7 CODE AND PRIVATE7 BOT \033[1;95m--
\033[1;97m """)

banner_logo()

now = datetime.datetime.now()

print("           \033[1;95mSTARTED AT: " + str(now))

def scan(site):

	try:

		if "http" in site:

			url = site

		else:

			url = "http://" + site

		r = requests.get(url,timeout=20)

		# 1. CMS WORDPRESS
		if "/wp-content/" in r.text or "/wp-login.php" in r.text or "/wp-admin/" in r.text or "/license.txt" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mWORDPRESS \033[1;95m...............\033[1;97m " + url)

			with open("cms_result/wordpress.txt","a") as f:

				f.write(url + "\n")

		# 2. CMS JOOMLA
		elif "/Joomla!" in r.text or "/index.php?option=com_" in r.text or "/administrator/index.php" in r.text or "/administrator/" in r.text or "/administrator/manifests/files/joomla.xml" in r.text or "/<version>(.*?)<\/version>" in r.text or "/language/en-GB/en-GB.xml" in r.text or "<version>(.*?)<\/version>" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mJOOMLA \033[1;95m..................\033[1;97m " + url)

			with open("cms_result/joomla.txt","a") as f:

				f.write(url + "\n")

		# 3. CMS OPENCART
		elif "/index.php?route=common/home" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mOPENCART \033[1;95m................\033[1;97m " + url)

			with open("cms_result/opencart.txt","a") as f:

				f.write(url + "\n")

		# 4. CMS DRUPAL
		elif "/sites/default" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mDRUPAL \033[1;95m..................\033[1;97m " + url)

			with open("cms_result/drupal.txt","a") as f:

				f.write(url + "\n")

		# 5. CMS PRESTASHOP
		elif "/prestashop" in r.text or "/PrestaShop" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mPRESTASHOP \033[1;95m..............\033[1;97m " + url)

			with open("cms_result/prestashop.txt","a") as f:

				f.write(url + "\n")

		# 6. CMS OSCOMMERCE
		elif "/osCommerce" in r.text or "/admin/login.php" in r.text or "/admin/images/cal_date_over.gif" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mOSCOMMERCE \033[1;95m..............\033[1;97m " + url)

			with open("cms_result/oscommerce.txt","a") as f:

				f.write(url + "\n")

		# 7. CMS VBULLETIN
		elif "/osCommerce" in r.text or "/admin/login.php" in r.text or "/admin/images/cal_date_over.gif" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mVBULLETIN \033[1;95m...............\033[1;97m " + url)

			with open("cms_result/vbulletin.txt","a") as f:

				f.write(url + "\n")

		# 8. CMS MAGENTO
		elif "/Mage.Cookies" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mMAGENTO \033[1;95m.................\033[1;97m " + url)

			with open("cms_result/magento.txt","a") as f:

				f.write(url + "\n")

		# 9. CMS ZENCART
		elif "/application/configs/application.ini" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mZENCART \033[1;95m.................\033[1;97m " + url)

			with open("cms_result/zencart.txt","a") as f:

				f.write(url + "\n")

                # 10. CMS SHOPIFY
		elif "/collections/all/Powered by Shopify/cdn.shopify.com/" in r.text or "/all/" in r.text or "/collections/all" in r.text or "/Powered by Shopify/" in r.text or "/cdn.shopify.com" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mSHOPIFY \033[1;95m.................\033[1;97m " + url)

			with open("cms_result/shopify.txt","a") as f:

				f.write(url + "\n")

                # 11. CMS LARAVEL PHP UNIT
		elif "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mLARAVEL PHPUNIT \033[1;95m.........\033[1;97m " + url)

			with open("cms_result/laravel_phpunit.txt","a") as f:

				f.write(url + "\n")

		# 12. CMS SITEFINITY
		elif "/Sitefinity" in r.text or "/sitefinity/UserControls/Dialogs/DocumentEditorDialog.aspx" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mSITEFINITY \033[1;95m..............\033[1;97m " + url)

			with open("cms_result/sitefinity.txt","a") as f:

				f.write(url + "\n")

		# 13. CMS MYBB
		elif "/jscripts/general.js?ver=" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mMYBB \033[1;95m....................\033[1;97m " + url)

			with open("cms_result/mybb.txt","a") as f:

				f.write(url + "\n")

		# 14. CMS UBERCART
		elif "/uc_cart" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mUBERCART \033[1;95m................\033[1;97m " + url)

			with open("cms_result/ubercart.txt","a") as f:

				f.write(url + "\n")

		# 15. CMS PROTOTYPE
		elif "/sites/default" in r.text or "/prototype.js" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mPROTOTYPE \033[1;95m...............\033[1;97m " + url)

			with open("cms_result/prototype.txt","a") as f:

				f.write(url + "\n")

		# 16. CMS JQUERY FILE UPLOAD
		elif "/assets/global/plugins/jquery-file-upload/server/php/" in r.text or "/jQuery/server/php" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mJQUERY FILE UPLOAD \033[1;95m......\033[1;97m " + url)

			with open("cms_result/jquery_file_upload.txt","a") as f:

				f.write(url + "\n")

		# 17. CMS JALIOS JCMS
		elif "/Jalios JCMS/" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mJALIOS JCMS \033[1;95m.............\033[1;97m " + url)

			with open("cms_result/jalios_jcms.txt","a") as f:

				f.write(url + "\n")

		# 18. CMS SHAREPOINT
		elif "/SharePoint/" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mSHAREPOINT \033[1;95m..............\033[1;97m " + url)

			with open("cms_result/sharepoint.txt","a") as f:

				f.write(url + "\n")

		# 19. CMS BIGACE

		elif "/BIGACE/" in r.text:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mBIGACE \033[1;95m..................\033[1;97m " + url)

			with open("cms_result/bigace.txt","a") as f:

				f.write(url + "\n")

		# 20. CMS ZENPHOTO
		elif "/zp-core/js/" in r.text:
			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mZENPHOTO \033[1;95m................\033[1;97m " + url)
			with open("cms_result/zenphoto.txt","a") as f:
				f.write(url + "\n")

		# 00. CMS NOT FOUND / NOT WORKING
		else:

			print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mNOT FOUND \033[1;95m...............\033[1;97m " + url)

			with open("cms_result/othercms.txt","a") as f:

				f.write(url + "\n")
	except:

		print("    \033[1;95m[\033[1;92m+\033[1;95m] \033[1;97mNOT WORKING \033[1;95m.............\033[1;97m " + site)

sitelist = raw_input("\n   \033[1;97mSITE LIST SEND TO HELL \033[1;95m> \033[1;97m")

print("")

try:

	sites = open(sitelist,"r").read().splitlines()

	pp = Pool(100)

	pr = pp.map(scan, sites)

except:

	print("   \033[1;95mWEBSITE LIST FILE NOT FOUND !!!\033[1;97m")

	sys.exit()

