# Decompiled At : Fri Apr 10 19:58:27 WIB 2020
# File : Python 3.7
#!usr/bin/python3.7
#Author: DulLah ©2019
# FB : fb.me/dulahz
#Telegram : t.me/unikers
#github: github.com/dz-id
'''
Sudah Berhasil Dec? Yaudah Pake Sendiri Jangan Disebarin
Apalagi diRecode
'''
import os, re, sys, requests
from data import cekKuki
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
from http.cookiejar import LWPCookieJar as kuki
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style

global W, G, R
if sys.platform in ['linux','linux2']:
	W = '\033[0m'
	G = '\033[1;92m'
	R = '\033[1;91m'
else:
	W = ''
	G = ''
	R = ''

class Report:
	def __init__(self):
		self.loop = 0
		cekKuki.cek(self)
		self.link = []
		self.true = []
		self.false = []
		self.url = 'https://mbasic.facebook.com{}'
		self.HD = {'User-Agent' : open('UserAgent/ua.txt').read()}
		self.req = requests.Session()
		s = self.req
		s.cookies = kuki('log/kuki')
		s.cookies.load()
		self.Main()
	
	def Support_Inbox(self,anu):
		try:
			a = self.req.get(anu)
			b = parser(a.content, 'html.parser')
			
			for i in b.find_all('span'):
				if 'Anda secara anonim melaporkan' in str(i):
					p = i.find('a')
					if '/story.php?' in str(p):
						
						try:
							ids = re.findall(r'/?story_fbid=(.*?)&id=',p['href'])[0]
							print(W +'-' * 50)
							print(W + '[' + G + '•' + W + '] '+ R + i.text)
							print(W + '[' + G + '•' + W + '] url : ' + G + 'facebook.com/' + str(ids))
						except:
							try:
								ids = re.findall(r'/?story_fbid=(.*?)&amp;id=',p['href'])[0]
								print(W +'-' * 50)
								print(W + '[' + G + '•' + W + '] '+ R + i.text)
								print(W + '[' + G + '•' + W + '] url : ' + G + 'facebook.com/' + str(ids))
							except:pass
							
					elif '/photo.php?' in str(p):
						try:
							ids = re.findall(r'/?fbid=(.*?)&id=',p['href'])[0]
							print(W +'-' * 50)
							print(W + '[' + G + '•' + W + '] '+ R + i.text)
							print(W + '[' + G + '•' + W + '] url : ' + G + 'facebook.com/' + str(ids))
						except:
							try:
								ids = re.findall(r'/?fbid=(.*?)&amp;id=',p['href'])[0]
								print(W +'-' * 50)
								print(W + '[' + G + '•' + W + '] '+ R + i.text)
								print(W + '[' + G + '•' + W + '] url : ' + G + 'facebook.com/' + str(ids))
							except:pass
							
					elif 'profile.php?' in str(p):
						try:
							ids = p['href'].replace('/profile.php?id=','')
							print(W +'-' * 50)
							print(W + '[' + G + '•' + W + '] '+ R + i.text)
							print(W + '[' + G + '•' + W + '] url : ' + G + 'facebook.com/' + str(ids))
						except: pass
					
					elif '/groups/' in str(p):
						try:
							print(W +'-' * 50)
							print(W + '[' + G + '•' + W + '] '+ R + i.text)
							print(W + '[' + G + '•' + W + '] url : ' + G + 'facebook.com' + str(p['href']))
						except: pass
						
					else:
						try:
							print(W +'-' * 50)
							print(W + '[' + G + '•' + W + '] '+ R + i.text)
							print(W + '[' + G + '•' + W + '] url : ' + G + 'facebook.com' + str(p['href']))
						except: pass
						
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
	
	def Excute1(self,postid):
			try:
				data1 = []
				s = self.req.get(postid, headers = self.HD)
				b1 = parser(s.content, 'html.parser')
						
				for i in b1('form'):
					data1.append(i['action'])
				for i in b1('input'):
					try:
						if 'fb_dtsg' in i['name']:
							data1.append(i['value'])
						if 'jazoest' in i['name']:
							data1.append(i['value'])
							break
					except : pass
							
				if len(data1) == 3:
					data2 = []
					url = self.url.format(data1[0])
					form = {'fb_dtsg' : data1[1], 'jazoest' : data1[2], 'tag' : 'harassment'}
					p = self.req.post(url, data = form, headers = self.HD)
					b2 = parser(p.content, 'html.parser')
							
					for i in b2('form'):
						data2.append(i['action'])
					for i in b2('input'):
						try:
							if 'fb_dtsg' in i['name']:
								data2.append(i['value'])
							if 'jazoest' in i['name']:
								data2.append(i['value'])
							if 'RESOLVE_PROBLEM_REDIRECT' in i['value'] or 'FRX_PROFILE_REPORT_CONFIRMATION' in i['value']:
								data2.append(i['value'])
								break
						except: pass
							
					if len(data2) == 4:
						if 'RESOLVE_PROBLEM_REDIRECT' in data2[3]:
									
							data3 = []
							url = self.url.format(data2[0])
							form = {'fb_dtsg' : data2[1], 'jazoest' : data2[2], 'action_key' : data2[3]}
							p = self.req.post(url, data = form, headers = self.HD)
							b3 = parser(p.content, 'html.parser')
									
							for i in b3('form'):
								data3.append(i['action'])
							for i in b3('input'):
								try:
									if 'fb_dtsg' in i['name']:
										data3.append(i['value'])
									if 'jazoest' in i['name']:
										data3.append(i['value'])
										break
								except: pass
									
							if len(data3) == 3:
								data4 = []
								url = self.url.format(data3[0])
								form = {'fb_dtsg' : data3[1], 'jazoest' : data3[2], 'answer' : 'offensive'}
								w = self.req.post(url, data = form, headers = self.HD)
								b4 = parser(w.content, 'html.parser')
									
								for i in b4('form'):
									data4.append(i['action'])
								for i in b4('input'):
									try:
										if 'fb_dtsg' in i['name']:
											data4.append(i['value'])
										if 'jazoest' in i['name']:
											data4.append(i['value'])
											break
									except: pass
										
								if len(data4) == 3:
									data5 = []
									if 'Apa yang salah dengan foto ini?' in str(b4):
												
										url = self.url.format(data4[0])
										form = {'fb_dtsg' : data4[1], 'jazoest' : data4[2], 'answer' : 'other'}
										o = self.req.post(url, data = form, headers = self.HD)
										b5 = parser(o.content, 'html.parser')
												
										for i in b5('form'):
											data5.append(i['action'])
										for i in b5('input'):
											try:
												if 'fb_dtsg' in i['name']:
													data5.append(i['value'])
												if 'jazoest' in i['name']:
													data5.append(i['value'])
													break
											except: pass
												
										if len(data5) == 3:
											data6 = []
											url = self.url.format(data5[0])
											form = {'fb_dtsg' : data5[1], 'jazoest' : data5[2], 'answer' : 'hate'}
											u = self.req.post(url, data = form, headers = self.HD)
											b6 = parser(u.content, 'html.parser')
													
											for i in b6('form'):
												data6.append(i['action'])
											for i in b6('input'):
												try:
													if 'fb_dtsg' in i['name']:
														data6.append(i['value'])
													if 'jazoest' in i['name']:
														data6.append(i['value'])
													if 'REPORT_CONTENT' in i['value']:
														data6.append(i['value'])
														break
												except: pass
													
											if len(data6) == 4:
												url = self.url.format(data6[0])
												form = {'fb_dtsg' : data6[1], 'jazoest' : data6[2], 'action_key' : data6[3]}
												m = self.req.post(url, data = form, headers = self.HD)
												if 'Dikirimkan ke Facebook untuk Ditinjau' in str(m.text):
													self.true.append(postid)
												else: self.false.append(postid)
											else: self.false.append(postid)
										else: self.false.append(postid)
													
									elif 'Apa yang salah dengan kiriman ini?' in str(b4):
												
										url = self.url.format(data4[0])
										form = {'fb_dtsg' : data4[1], 'jazoest' : data4[2], 'answer' : 'hatespeech'}
										o = self.req.post(url, data = form, headers = self.HD)
										b5 = parser(o.content, 'html.parser')
												
										for i in b5('form'):
											data5.append(i['action'])
										for i in b5('input'):
											try:
												if 'fb_dtsg' in i['name']:
													data5.append(i['value'])
												if 'jazoest' in i['name']:
													data5.append(i['value'])
													break
											except: pass
												
										if len(data5) == 3:
											data6 = []
											url = self.url.format(data5[0])
											form = {'fb_dtsg' : data5[1], 'jazoest' : data5[2], 'answer' : 'individual'}
											u = self.req.post(url, data = form, headers = self.HD)
											b6 = parser(u.content, 'html.parser')
													
											for i in b6('form'):
												data6.append(i['action'])
											for i in b6('input'):
												try:
													if 'fb_dtsg' in i['name']:
														data6.append(i['value'])
													if 'jazoest' in i['name']:
														data6.append(i['value'])
														break
												except: pass
													
											if len(data6) == 3:
												data7 = []
												url = self.url.format(data6[0])
												form = {'fb_dtsg' : data6[1], 'jazoest' : data6[2], 'answer' : 'harassing_someone_else'}
												m = self.req.post(url, data = form, headers = self.HD)
												b7 = parser(m.content, 'html.parser')
														
												for i in b7('form'):
													data7.append(i['action'])
												for i in b7('input'):
													try:
														if 'fb_dtsg' in i['name']:
															data7.append(i['value'])
														if 'jazoest' in i['name']:
															data7.append(i['value'])
														if 'REPORT_CONTENT' in i['value']:
															data7.append(i['value'])
															break
													except: pass
														
												if len(data7) == 4:
													url = self.url.format(data7[0])
													form = {'fb_dtsg' : data7[1], 'jazoest' : data7[2], 'action_key' : data7[3]}
													c = self.req.post(url, data = form, headers = self.HD)
													if 'Dikirimkan ke Facebook untuk Ditinjau' in str(c.text):
														self.true.append(postid)
													else: self.false.append(postid)
												else: self.false.append(postid)
											else: self.false.append(postid)
										else: self.false.append(postid)
												
									elif 'Apa yang salah dengan postingan ini?' in str(b4):
												
										url = self.url.format(data4[0])
										form = {'fb_dtsg' : data4[1], 'jazoest' : data4[2], 'answer' : 'againstbelief'}
										o = self.req.post(url, data = form, headers = self.HD)
										b5 = parser(o.content, 'html.parser')
												
										for i in b5('form'):
											data5.append(i['action'])
										for i in b5('input'):
											try:
												if 'fb_dtsg' in i['name']:
													data5.append(i['value'])
												if 'jazoest' in i['name']:
													data5.append(i['value'])
												if 'REPORT_CONTENT' in i['value']:
													data5.append(i['value'])
													break
											except: pass
												
										if len(data5) == 4:
											url = self.url.format(data5[0])
											form = {'fb_dtsg' : data5[1], 'jazoest' : data5[2], 'action_key' : data5[3]}
											u = self.req.post(url, data = form, headers = self.HD)
											if 'Dikirimkan ke Facebook untuk Ditinjau' in str(u.text):
												self.true.append(postid)
											else: self.false.append(postid)
										else: self.false.append(postid)
									else: self.false.append(postid)
								else: self.false.append(postid)
											
						elif 'FRX_PROFILE_REPORT_CONFIRMATION' in data2[3]:
							data3 = []
							url = self.url.format(data2[0])
							form = {'fb_dtsg' : data2[1], 'jazoest' : data2[2], 'action_key' : data2[3]}
							p = self.req.post(url, data = form, headers = self.HD)
							b3 = parser(p.content, 'html.parser')
									
							for i in b3('form'):
								data3.append(i['action'])
							for i in b3('input'):
								try:
									if 'fb_dtsg' in i['name']:
										data3.append(i['value'])
									if 'jazoest' in i['name']:
										data3.append(i['value'])
										break
								except: pass
									
							if len(data3) == 3:
								url = self.url.format(data3[0])
								form = {'fb_dtsg' : data3[1], 'jazoest' : data3[2], 'checked' : 'yes', 'action' : 'Laporkan'}
								w = self.req.post(url, data = form, headers = self.HD)
								if 'Dikirimkan ke Facebook untuk Ditinjau' in str(w.text):
									self.true.append(postid)
								else: self.false.append(postid)
							else: self.false.append(postid)
						else: self.false.append(postid)
					else: self.false.append(postid)
				else: self.false.append(postid)
				
			except: self.false.append(postid)
			self.loop += 1
			sys.stdout.write(W +'\r[' + R + str(len(self.false)) + W + '] process '+str(self.loop)+'/'+str(self.t)+ ' {:.2f}'.format(self.loop/self.t*100)+'% success :-' + G + str(len(self.true)) + ' ')
			sys.stdout.flush()
		
	def Excute2(self,postid):
			try:
				data1 = []
				s = self.req.get(postid, headers = self.HD)
				b1 = parser(s.content, 'html.parser')
						
				for i in b1('form'):
					data1.append(i['action'])
				for i in b1('input'):
					try:
						if 'fb_dtsg' in i['name']:
							data1.append(i['value'])
						if 'jazoest' in i['name']:
							data1.append(i['value'])
							break
					except : pass
				
				if len(data1) == 3:
					data2 = []
					url = self.url.format(data1[0])
					form = {'fb_dtsg' : data1[1], 'jazoest' : data1[2], 'tag' : 'hate_speech'}
					p = self.req.post(url, data = form, headers = self.HD)
					b2 = parser(p.content, 'html.parser')
							
					for i in b2('form'):
						data2.append(i['action'])
					for i in b2('input'):
						try:
							if 'fb_dtsg' in i['name']:
								data2.append(i['value'])
							if 'jazoest' in i['name']:
								data2.append(i['value'])
							if 'hate_speech_something_else' in i['value']:
								data2.append(i['value'])
								break
						except: pass
					
					if len(data2) == 4:
						data3 = []
						url = self.url.format(data2[0])
						form = {'fb_dtsg' : data2[1], 'jazoest' : data2[2], 'tag' : data2[3]}
						p = self.req.post(url, data = form, headers = self.HD)
						b3 = parser(p.content, 'html.parser')
									
						for i in b3('form'):
							data3.append(i['action'])
						for i in b3('input'):
							try:
								if 'fb_dtsg' in i['name']:
									data3.append(i['value'])
								if 'jazoest' in i['name']:
									data3.append(i['value'])
									break
							except: pass
						
						if len(data3) == 3:
							data4 = []
							url = self.url.format(data3[0])
							form = {'fb_dtsg' : data3[1], 'jazoest' : data3[2], 'action_key' : 'RESOLVE_PROBLEM_REDIRECT'}
							p = self.req.post(url, data = form, headers = self.HD)
							b4 = parser(p.content, 'html.parser')
									
							for i in b4('form'):
								data4.append(i['action'])
							for i in b4('input'):
								try:
									if 'fb_dtsg' in i['name']:
										data4.append(i['value'])
									if 'jazoest' in i['name']:
										data4.append(i['value'])
										break
								except: pass
							
							if len(data4) == 3:
								data5 = []
								url = self.url.format(data4[0])
								form = {'fb_dtsg' : data4[1], 'jazoest' : data4[2], 'answer' : 'offensive'}
								p = self.req.post(url, data = form, headers = self.HD)
								b5 = parser(p.content, 'html.parser')
								
								for i in b5('form'):
									data5.append(i['action'])
								for i in b5('input'):
									try:
										if 'fb_dtsg' in i['name']:
											data5.append(i['value'])
										if 'jazoest' in i['name']:
											data5.append(i['value'])
											break
									except: pass
								
								if len(data5) == 3:
									data6 = []
									if 'Apa yang salah dengan foto ini?' in str(b5) or 'Apa yang salah dengan kiriman ini?' in str(b5) or 'Apa yang salah dengan postingan ini?' in str(bs5):
										
										url = self.url.format(data5[0])
										form = {'fb_dtsg' : data5[1], 'jazoest' : data5[2], 'answer' : 'pornography'}
										o = self.req.post(url, data = form, headers = self.HD)
										b6 = parser(o.content, 'html.parser')
										
										for i in b6('form'):
											data6.append(i['action'])
										for i in b6('input'):
											try:
												if 'fb_dtsg' in i['name']:
													data6.append(i['value'])
												if 'jazoest' in i['name']:
													data6.append(i['value'])
												if 'REPORT_CONTENT' in i['value']:
													data6.append(i['value'])
													break
											except: pass
												
										if len(data6) == 4:
											url = self.url.format(data6[0])
											form = {'fb_dtsg' : data6[1], 'jazoest' : data6[2], 'action_key' : data6[3]}
											u = self.req.post(url, data = form, headers = self.HD)
											if 'Dikirimkan ke Facebook untuk Ditinjau' in str(u.text):
												self.true.append(postid)
											else: self.false.append(postid)
										else: self.false.append(postid)
									else: self.false.append(postid)
								else: self.false.append(postid)
							else: self.false.append(postid)
						else: self.false.append(postid)
					else: self.false.append(postid)
				else: self.false.append(postid)
				
			except: self.false.append(postid)
			self.loop += 1
			sys.stdout.write(W +'\r[' + R + str(len(self.false)) + W + '] process '+str(self.loop)+'/'+str(self.t)+ ' {:.2f}'.format(self.loop/self.t*100)+'% success :-' + G + str(len(self.true)) + ' ')
			sys.stdout.flush()
	
	def Excute3(self,postid):
			try:
				data1 = []
				s = self.req.get(postid, headers = self.HD)
				b1 = parser(s.content, 'html.parser')
						
				for i in b1('form'):
					data1.append(i['action'])
				for i in b1('input'):
					try:
						if 'fb_dtsg' in i['name']:
							data1.append(i['value'])
						if 'jazoest' in i['name']:
							data1.append(i['value'])
						if 'RESOLVE_PROBLEM' in i['value']:
							data1.append(i['value'])
							break
					except : pass
				
				if len(data1) == 4:
					if 'RESOLVE_PROBLEM' in data1[3]:
						
						data2 = []
						url = self.url.format(data1[0])
						form = {'fb_dtsg' : data1[1], 'jazoest' : data1[2], 'action_key' : data1[3]}
						p = self.req.post(url, data = form, headers = self.HD)
						b2 = parser(p.content, 'html.parser')
									
						for i in b2('form'):
								data2.append(i['action'])
						for i in b2('input'):
							try:
								if 'fb_dtsg' in i['name']:
									data2.append(i['value'])
								if 'jazoest' in i['name']:
									data2.append(i['value'])
									break
							except: pass
									
						if len(data2) == 3:
							data3 = []
							url = self.url.format(data2[0])
							form = {'fb_dtsg' : data2[1], 'jazoest' : data2[2], 'tag' : 'hate_speech'}
							w = self.req.post(url, data = form, headers = self.HD)
							b3 = parser(w.content, 'html.parser')
									
							for i in b3('form'):
								data3.append(i['action'])
							for i in b3('input'):
								try:
									if 'fb_dtsg' in i['name']:
										data3.append(i['value'])
									if 'jazoest' in i['name']:
										data3.append(i['value'])
										break
								except: pass
							
							if len(data3) == 3:
								data4 = []
								url = self.url.format(data3[0])
								form = {'fb_dtsg' : data3[1], 'jazoest' : data3[2], 'tag' : 'hate_speech_something_else'}
								w = self.req.post(url, data = form, headers = self.HD)
								b4 = parser(w.content, 'html.parser')
								
								for i in b4('form'):
									data4.append(i['action'])
								for i in b4('input'):
									try:
										if 'fb_dtsg' in i['name']:
											data4.append(i['value'])
										if 'jazoest' in i['name']:
											data4.append(i['value'])
										if 'RESOLVE_PROBLEM_REDIRECT' in i['value'] or 'FRX_PROFILE_REPORT_CONFIRMATION' in i['value']:
											data4.append(i['value'])
											break
									except: pass
								
								if len(data4) == 4:
									if 'RESOLVE_PROBLEM_REDIRECT' in data4[3]:
										
										data5 = []
										url = self.url.format(data4[0])
										form = {'fb_dtsg' : data4[1], 'jazoest' : data4[2], 'action_key' : data4[3]}
										w = self.req.post(url, data = form, headers = self.HD)
										b5 = parser(w.content, 'html.parser')
										
										for i in b5('form'):
											data5.append(i['action'])
										for i in b5('input'):
											try:
												if 'fb_dtsg' in i['name']:
													data5.append(i['value'])
												if 'jazoest' in i['name']:
													data5.append(i['value'])
													break
											except: pass
										
										if len(data5) == 3:
											data6 = []
											url = self.url.format(data5[0])
											form = {'fb_dtsg' : data5[1], 'jazoest' : data5[2], 'answer' : 'offensive'}
											w = self.req.post(url, data = form, headers = self.HD)
											b6 = parser(w.content, 'html.parser')
											
											for i in b6('form'):
												data6.append(i['action'])
											for i in b6('input'):
												try:
													if 'fb_dtsg' in i['name']:
														data6.append(i['value'])
													if 'jazoest' in i['name']:
														data6.append(i['value'])
														break
												except: pass
											
											if len(data6) == 3:
												data7 = []
												if 'Apa yang salah dengan foto ini?' in str(b6):
													
													url = self.url.format(data6[0])
													form = {'fb_dtsg' : data6[1], 'jazoest' : data6[2], 'answer' : 'annoying'}
													w = self.req.post(url, data = form, headers = self.HD)
													b7 = parser(w.content, 'html.parser')
													
													for i in b7('form'):
														data7.append(i['action'])
													for i in b7('input'):
														try:
															if 'fb_dtsg' in i['name']:
																data7.append(i['value'])
															if 'jazoest' in i['name']:
																data7.append(i['value'])
															if 'REPORT_CONTENT' in i['value']:
																data7.append(i['value'])
																break
														except: pass
													
													if len(data7) == 4:
														url = self.url.format(data7[0])
														form = {'fb_dtsg' : data7[1], 'jazoest' : data7[2], 'action_key' : data7[3]}
														w = self.req.post(url, data = form, headers = self.HD)
														if 'Dikirimkan ke Facebook untuk Ditinjau' in str(w.text):
															self.true.append(postid)
														else: self.false.append(postid)
													else: self.false.append(postid)
												
												elif 'Apa yang salah dengan kiriman ini?' in str(b6):
													
													url = self.url.format(data6[0])
													form = {'fb_dtsg' : data6[1], 'jazoest' : data6[2], 'answer' : 'hatespeech'}
													w = self.req.post(url, data = form, headers = self.HD)
													b7 = parser(w.content, 'html.parser')
													
													for i in b7('form'):
														data7.append(i['action'])
													for i in b7('input'):
														try:
															if 'fb_dtsg' in i['name']:
																data7.append(i['value'])
															if 'jazoest' in i['name']:
																data7.append(i['value'])
																break
														except: pass
													
													if len(data7) == 3:
														data8 = []
														url = self.url.format(data7[0])
														form = {'fb_dtsg' : data7[1], 'jazoest' : data7[2], 'answer' : 'individual'}
														w = self.req.post(url, data = form, headers = self.HD)
														b8 = parser(w.content, 'html.parser')
														
														for i in b8('form'):
															data8.append(i['action'])
														for i in b8('input'):
															try:
																if 'fb_dtsg' in i['name']:
																	data8.append(i['value'])
																if 'jazoest' in i['name']:
																	data8.append(i['value'])
																if 'harassing_someone_else' in i['value']:
																	data8.append(i['value'])
																	break
															except: pass
														
														if len(data8) == 4:
															data9 = []
															url = self.url.format(data8[0])
															form = {'fb_dtsg' : data8[1], 'jazoest' : data8[2], 'answer' : data8[3]}
															w = self.req.post(url, data = form, headers = self.HD)
															b9 = parser(w.content, 'html.parser')
															
															for i in b9('form'):
																data9.append(i['value'])
															for i in b9('input'):
																try:
																	if 'fb_dtsg' in i['name']:
																		data9.append(i['value'])
																	if 'jazoest' in i['name']:
																		data9.append(i['value'])
																	if 'REPORT_CONTENT' in i['value']:
																		data9.append(i['value'])
																		break
																except: pass
															
															if len(data9) == 4:
																url = self.url.format(data9[0])
																form = {'fb_dtsg' : data9[1], 'jazoest' : data9[2], 'action_key' : data9[3]}
																w = self.req.post(url, data = form, headers = self.HD)
																if 'Dikirimkan ke Facebook untuk Ditinjau' in str(w.text):
																	self.true.append(postid)
																else: self.false.append(postid)
															else: self.false.append(postid)
														else: self.false.append(postid)
													else: self.false.append(postid)
												
												elif 'Apa yang salah dengan postingan ini?' in str(b6):
													
													data7 = []
													url = self.url.format(data6[0])
													form = {'fb_dtsg' : data6[1], 'jazoest' : data6[2], 'answer' : 'hatespeech'}
													w = self.req.post(url, data = form, headers = self.HD)
													b7 = parser(w.content, 'html.parser')
													
													for i in b7('form'):
														data7.append(i['action'])
													for i in b7('input'):
														try:
															if 'fb_dtsg' in i['name']:
																data7.append(i['value'])
															if 'jazoest' in i['name']:
																data7.append(i['value'])
															if 'REPORT_CONTENT' in i['value']:
																data7.append(i['value'])
																break
														except: pass
														
													if len(data7) == 4:
														url = self.url.format(data7[0])
														form = {'fb_dtsg' : data7[1], 'jazoest' : data7[2], 'action_key' : data7[3]}
														w = self.req.post(url, data = form, headers = self.HD)
														if 'Dikirimkan ke Facebook untuk Ditinjau' in str(w.text):
															self.true.append(postid)
														else: self.false.append(postid)
													else: self.false.append(postid)
												else: self.false.append(postid)
											else: self.false.append(postid)
										else: self.false.append(postid)

									elif 'FRX_PROFILE_REPORT_CONFIRMATION' in data4[3]:
										
										data5 = []
										url = self.url.format(data4[0])
										form = {'fb_dtsg' : data4[1], 'jazoest' : data4[2], 'action_key' : data4[3]}
										w = self.req.post(url, data = form, headers = self.HD)
										b5 = parser(w.content, 'html.parser')
										
										for i in b5('form'):
											data5.append(i['action'])
										for i in b5('input'):
											try:
												if 'fb_dtsg' in i['name']:
													data5.append(i['value'])
												if 'jazoest' in i['name']:
													data5.append(i['value'])
													break
											except: pass
										
										if len(data5) == 3:
											url = self.url.format(data5[0])
											form = {'fb_dtsg' : data5[1], 'jazoest' : data5[2], 'checked' : 'yes', 'action' : 'Laporkan'}
											w = self.req.post(url, data = form, headers = self.HD)
											if 'Dikirimkan ke Facebook untuk Ditinjau' in str(w.text):
												self.true.append(postid)
											else: self.false.append(postid)
										else: self.false.append(postid)
									else: self.false.append(postid)
								else: self.false.append(postid)
							else: self.false.append(postid)
						else: self.false.append(postid)
					else: self.false.append(postid)
				else: self.false.append(postid)
				
			except: self.false.append(postid)
			self.loop += 1
			sys.stdout.write(W +'\r[' + R + str(len(self.false)) + W + '] process '+str(self.loop)+'/'+str(self.t)+ ' {:.2f}'.format(self.loop/self.t*100)+'% success :-' + G + str(len(self.true)) + ' ')
			sys.stdout.flush()
				
	def Rpt(self,tip,links):
		try:
			if tip == 'profile':
				
				a = self.req.get(links,headers = self.HD)
				b = parser(a.content, 'html.parser')
				
				if 'Cari Dukungan atau Laporkan Postingan' in str(b):
					for i in b.find_all('a', string = 'Cari Dukungan atau Laporkan Postingan'):
						self.link.append(self.url.format(i['href']))
						print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.link)) + W + '] GET posts url... ',end='');sys.stdout.flush()
					
					if 'Lihat Berita Lain' in str(b):
						href = self.url.format(b.find('a', string = 'Lihat Berita Lain')['href'])
						self.Rpt(tip,href)
						
				data1 = []
				r = self.req.get(self.url.format('/'+str(self.id)),headers = self.HD)
				b1 = parser(r.content, 'html.parser')
				if 'Konten Tidak Ditemukan' in str(b1) or 'Halaman Tidak Ditemukan' in str(b1):
					print(W + '[' + R + '!' + W + '] ' + R + 'profile not found!')
					sys.exit()
				print(W + '\n[' + G + '*' + W + '] report profile ' + G + str(b1.title.text))
				if 'Lainnya' in str(b1):
					f = self.url.format(b1.find('a', string = 'Lainnya')['href'])
					
					y = self.req.get(f,headers = self.HD)
					b2 = parser(y.content, 'html.parser')
							
					if 'Cari Dukungan atau Laporkan Profil' in str(b2):
						href = b2.find('a', string = 'Cari Dukungan atau Laporkan Profil')['href']
						s = self.req.get(self.url.format(href),headers = self.HD)
						b3 = parser(s.content, 'html.parser')
								
						for i in b3('form'):
							data1.append(i['action'])
						for i in b3('input'):
							try:
								if 'fb_dtsg' in i['name']:
									data1.append(i['value'])
								if 'jazoest' in i['name']:
									data1.append(i['value'])
									break
							except: pass
									
						if len(data1) == 3:
							data2 = []
							url = self.url.format(data1[0])
							form = {'fb_dtsg' : data1[1], 'jazoest' : data1[2], 'tag' : 'profile_fake_name'}
							q = self.req.post(url, data = form, headers = self.HD)
							b4 = parser(q.content, 'html.parser')
							
							for i in b4('form'):
								data2.append(i['action'])
							for i in b4('input'):
								try:
									if 'fb_dtsg' in i['name']:
										data2.append(i['value'])
									if 'jazoest' in i['name']:
										data2.append(i['value'])
										break
								except: pass
							
							if len(data2) == 3:
								data3 = []
								url = self.url.format(data2[0])
								form = {'fb_dtsg' : data2[1], 'jazoest' : data2[2], 'action_key' : 'FRX_PROFILE_REPORT_CONFIRMATION'}
								q = self.req.post(url, data = form, headers = self.HD)
								b5 = parser(q.content, 'html.parser')
								
								for i in b5('form'):
									data3.append(i['action'])
								for i in b5('input'):
									try:
										if 'fb_dtsg' in i['name']:
											data3.append(i['value'])
										if 'jazoest' in i['name']:
											data3.append(i['value'])
											break
									except: pass
								
								if len(data3) == 3:
									url = self.url.format(data3[0])
									form = {'fb_dtsg' : data3[1], 'jazoest' : data3[2], 'checked' : 'yes', 'action' : 'Laporkan'}
									q = self.req.post(url, data = form, headers = self.HD)
									#//
									
				if len(self.link) !=0:
					self.t = len(self.link)
					m = ThreadPool(10)
					m.map(self.Excute1,self.link)
					print(W +'\n[' + G + '•' + W + '] done!')
					print(W +'[' + G + '*' + W + '] ' + str(len(self.true)) + ' posts successfully reported:)*')
					y = input(W + '[' + G + '?' + W + '] check support inbox [y/n] : ' + G)
					if y.lower() == 'y':
						print('')
						self.Support_Inbox(self.url.format('/support/'))
						exit()
					else: exit()
				else: exit(W + '[' + R + '!' + W + '] ' + R + 'no posts found!')
			
			elif tip == 'page':
				
				a = self.req.get(links,headers = self.HD)
				b = parser(a.content, 'html.parser')
				
				if 'Cari Dukungan atau Laporkan Postingan' in str(b):
					for i in b.find_all('a', string = 'Cari Dukungan atau Laporkan Postingan'):
						self.link.append(self.url.format(i['href']))
						print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.link)) + W + '] GET posts url... ',end='');sys.stdout.flush()
					
				if 'Cari Dukungan atau Laporkan Video' in str(b):
					for p in b.find_all('a', string = 'Cari Dukungan atau Laporkan Video'):
						self.link.append(self.url.format(p['href']))
						print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.link)) + W + '] GET posts url... ',end='');sys.stdout.flush()
				
				if 'Tampilkan lainnya' in str(b):
					href = self.url.format(b.find('a', string = 'Tampilkan lainnya')['href'])
					self.Rpt(tip,href)
						
				data1 = []
				r = self.req.get(self.url.format('/'+str(self.id)),headers = self.HD)
				b1 = parser(r.content, 'html.parser')
				if 'Konten Tidak Ditemukan' in str(b1) or 'Halaman Tidak Ditemukan' in str(b1):
					print(W + '[' + R + '!' + W + '] ' + R + 'page not found!')
					sys.exit()
				print(W + '\n[' + G + '*' + W + '] report page ' + G + str(b1.title.text))
				if 'Lainnya' in str(b1):
					for f in b1.find_all('a'):
						if '/pages/more/' in str(f):
							data1.append(f['href'])
							break
							
				if len(data1) !=0:
					data2 = []
					y = self.req.get(self.url.format(data1[0]),headers = self.HD)
					b2 = parser(y.content, 'html.parser')
							
					if 'Cari Dukungan atau Laporkan Halaman' in str(b2):
						href = b2.find('a', string = 'Cari Dukungan atau Laporkan Halaman')['href']
						s = self.req.get(self.url.format(href),headers = self.HD)
						b3 = parser(s.content, 'html.parser')
								
						for i in b3('form'):
							data2.append(i['action'])
						for i in b3('input'):
							try:
								if 'fb_dtsg' in i['name']:
									data2.append(i['value'])
								if 'jazoest' in i['name']:
									data2.append(i['value'])
									break
							except: pass
									
						if len(data2) == 3:
							data3 = []
							url = self.url.format(data2[0])
							form = {'fb_dtsg' : data2[1], 'jazoest' : data2[2], 'answer' : 'offensive'}
							q = self.req.post(url, data = form, headers = self.HD)
							b4 = parser(q.content, 'html.parser')
							
							for i in b4('form'):
								data3.append(i['action'])
							for i in b4('input'):
								try:
									if 'fb_dtsg' in i['name']:
										data3.append(i['value'])
									if 'jazoest' in i['name']:
										data3.append(i['value'])
										break
								except: pass
							
							if len(data3) == 3:
								data4 = []
								url = self.url.format(data3[0])
								form = {'fb_dtsg' : data3[1], 'jazoest' : data3[2], 'answer' : 'pornographic'}
								p = self.req.post(url, data = form, headers = self.HD)
								b5 = parser(p.content, 'html.parser')
								
								for i in b5('form'):
									data4.append(i['action'])
								for i in b5('input'):
									try:
										if 'fb_dtsg' in i['name']:
											data4.append(i['value'])
										if 'jazoest' in i['name']:
											data4.append(i['value'])
											break
									except: pass
								
								if len(data4) == 3:
									url = self.url.format(data4[0])
									form = {'fb_dtsg' : data4[1], 'jazoest' : data4[2], 'action_key' : 'REPORT_CONTENT'}
									q = self.req.post(url, data = form, headers = self.HD)
									#//
									
				if len(self.link) !=0:
					self.t = len(self.link)
					m = ThreadPool(10)
					m.map(self.Excute2,self.link)
					print(W +'\n[' + G + '•' + W + '] done!')
					print(W +'[' + G + '*' + W + '] ' + str(len(self.true)) + ' posts successfully reported:)*')
					y = input(W + '[' + G + '?' + W + '] check support inbox [y/n] : ' + G)
					if y.lower() == 'y':
						print('')
						self.Support_Inbox(self.url.format('/support/'))
						exit()
					else: exit()
				else: exit(W + '[' + R + '!' + W + '] ' + R + 'no posts found!')
			
			elif tip == 'groups':
				
				a = self.req.get(links,headers = self.HD)
				b = parser(a.content, 'html.parser')
				
				if 'Lainnya' in str(b):
					for i in b.find_all('a', string = 'Lainnya'):
						self.link.append(self.url.format(i['href']))
						print(W + '\r[' + G + '*' + W + '] [' + R + str(len(self.link)) + W + '] GET posts url... ',end='');sys.stdout.flush()
					
				if 'Lihat Postingan Lainnya' in str(b):
					href = self.url.format(b.find('a', string = 'Lihat Postingan Lainnya')['href'])
					self.Rpt(tip,href)
						
				data1 = []
				r = self.req.get(self.url.format('/groups/'+str(self.id)+'?view=info'),headers = self.HD)
				b1 = parser(r.content, 'html.parser')
				if 'Konten Tidak Ditemukan' in str(b1) or 'Halaman Tidak Ditemukan' in str(b1):
					print(W + '[' + R + '!' + W + '] ' + R + 'page not found!')
					sys.exit()
				print(W + '\n[' + G + '*' + W + '] report groups ' + G + str(b1.title.text))
				if 'Laporkan Grup' in str(b1):
					f = self.url.format(b1.find('a', string = 'Laporkan Grup')['href'])
					
					y = self.req.get(f,headers = self.HD)
					b2 = parser(y.content, 'html.parser')
					
					for i in b2.find_all('a'):
						if '/rapid_report/?' in str(i):
							data1.append(i['href'])
							break
							
					if len(data1) !=0:
						data2 = []
						s = self.req.get(self.url.format(data1[0]),headers = self.HD)
						b3 = parser(s.content, 'html.parser')
							
						for i in b3('form'):
							data2.append(i['action'])
						for i in b3('input'):
							try:
								if 'fb_dtsg' in i['name']:
									data2.append(i['value'])
								if 'jazoest' in i['name']:
									data2.append(i['value'])
									break
							except: pass
						
						if len(data2) == 3:
							data3 = []
							url = self.url.format(data2[0])
							form = {'fb_dtsg' : data2[1], 'jazoest' : data2[2], 'tag' : 'hate_speech'}
							s = self.req.post(url, data = form, headers = self.HD)
							b4 = parser(s.content, 'html.parser')
							
							for i in b4('form'):
								data3.append(i['action'])
							for i in b4('input'):
								try:
									if 'fb_dtsg' in i['name']:
										data3.append(i['value'])
									if 'jazoest' in i['name']:
										data3.append(i['value'])
									if 'REPORT_CONTENT' in i['value']:
										data3.append(i['value'])
										break
								except: pass
							
							if len(data3) == 4:
								url = self.url.format(data3[0])
								form = {'fb_dtsg' : data3[1], 'jazoest' : data3[2], 'action_key' : data3[3]}
								s = self.req.post(url, data = form, headers = self.HD)
								#//
								
				if len(self.link) !=0:
					self.t = len(self.link)
					m = ThreadPool(10)
					m.map(self.Excute3,self.link)
					print(W +'\n[' + G + '•' + W + '] done!')
					print(W +'[' + G + '*' + W + '] ' + str(len(self.true)) + ' posts successfully reported:)*')
					y = input(W + '[' + G + '?' + W + '] check support inbox [y/n] : ' + G)
					if y.lower() == 'y':
						print('')
						self.Support_Inbox(self.url.format('/support/'))
						exit()
					else: exit()
				else: exit(W + '[' + R + '!' + W + '] ' + R + 'no posts found!')
				
		except requests.exceptions.ConnectionError:
			print(W + '\n[' + R + '!' + W + '] ' + R + 'connections error!')
			sys.exit()
		except KeyboardInterrupt: pass
	
	def Main(self):
		
		print(G + '\n    01' + W + '. Report Profile  ',G + '02' + W + '. Report Page')
		print(G + '    03' + W + '. Report Group    ',R + '00' + W + '. Back')
		
		cek = input(W + '\n[ ' + R + 'Dz' + W +' ]•> ' + G)
		
		if cek in ['1','01']:
			self.id = input(W + '\n[' + G + '?' + W + '] enter target id : ' + G)
			if self.id.lower() in ["","dulahz","100005584243934","dulahz/","100005584243934/"]:
				exit(W + '[' + R + '!' + W + '] ' + R + 'STUPPID!')
			else:
				tip = 'profile'
				print(W + '[' + R + '!' + W + '] CTRL+c for skip')
				target = self.url.format('/'+str(self.id)+'?v=timeline')
				self.Rpt(tip,target)
		elif cek in ['2','02']:
			self.id = input(W + '\n[' + G + '?' + W + '] enter page id : ' + G)
			tip = 'page'
			print(W + '[' + R + '!' + W + '] CTRL+c for skip')
			target = self.url.format('/'+str(self.id))
			self.Rpt(tip,target)
		elif cek in ['3','03']:
			print(W + '\n[' + G + '!' + W + '] ' + R + 'Info akun anda harus bergabung dengan grup target!')
			self.id = input(W + '[' + G + '?' + W + '] enter groups id : ' + G)
			tip = 'groups'
			print(W + '[' + R + '!' + W + '] CTRL+c for skip')
			target = self.url.format('/'+str(self.id))
			self.Rpt(tip,target)
		elif cek in ['0','00']:
			os.system('python Fb.py')
		else:
			exit(W + '[' + R + '!' + W + '] ' + R + 'you stuppid!')
try:
	print('')
	style = Style.from_dict({'': '#00FF00','1': '#FFFFFF','2': '#00FF00','3': '#FFFFFF','4': '#FFFFFF'})
	msg = [('class:1', '['),('class:2', '•'),('class:3', ']'),('class:4', ' this feature requires a key. input key : ')]
	
	key = prompt(msg,style=style,is_password=True)
	if key == str(requests.get('https://pastebin.com/raw/Lr2zdFEF').text):
		print(W + '[' + G +'*' + W + '] true!')
		Report()
	else:
		print(W + '[' + R + '!' + W + '] ' + R + 'wrong key!')
		y = input(W + '[' + G + '?' + W + '] contact author [y/n] : ' + G)
		if y.lower() == 'y':
			os.system('xdg-open http://dulah-z.ga')
		else:
			exit(W + '[' + R + '!' + W + '] canceling')
except requests.exceptions.ConnectionError:
	print(W + '[' + R + '!' + W + '] ' + R + 'connections error!')
	sys.exit()
