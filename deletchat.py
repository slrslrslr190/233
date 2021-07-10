import requests , time
from json import dumps
r = requests.session()
import os
os.system("clear ;rm -rf deletchat.py")
os.system("figlet Del-Chat")
joker = 1
print(' Enter Insta User And Pass\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
time.sleep(1)
user = input("\n User : ")
pess = input(" Pass : ")
def chatMS():
	def aco():
		global go , foCH , foCU
		sis = go.cookies['sessionid']
		urA = 'https://i.instagram.com/api/v1/direct_v2/threads/{}/hide/'.format(foCH)
		
		hedA = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-length': '0',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; ds_user_id=46165248972; shbid=13126; shbts=1616804137.1316793; rur=PRN; csrftoken=mnnbqhStTDAfu10DkI2VrW5VoCg9InFk; sessionid='+sis,
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
			'x-csrftoken': 'mnnbqhStTDAfu10DkI2VrW5VoCg9InFk',
			'x-ig-app-id': '1217981644879628',
			'x-ig-www-claim': 'hmac.AR24Fkd2DvunQ5ELQD_I_6FoVMTbIdkiDD08ZF2jyPhpEmIg',
			'x-instagram-ajax': '753ce878cd6d'}
		
		g = r.post(urA,headers=hedA)
		
		if '"status":"ok"' in g.text:
			print(f'[+] The chat has been deleted -> {foCU}')
		
		else:
			print('[-] You have been banned ! ')
	aco()
	def idCHT():
		global go , foCH , foCU , slp
		sis = go.cookies['sessionid']
		while True:
			urCH = 'https://i.instagram.com/api/v1/direct_v2/inbox/?persistentBadging=true&cursor='
			
			hedCH = {
				'accept': '*/*',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
				'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; ds_user_id=46165248972; shbid=13126; shbts=1616804137.1316793; rur=PRN; csrftoken=mnnbqhStTDAfu10DkI2VrW5VoCg9InFk; sessionid='+sis,
				'origin': 'https://www.instagram.com',
				'referer': 'https://www.instagram.com/',
				'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
				'sec-ch-ua-mobile': '?0',
				'sec-fetch-dest': 'empty',
				'sec-fetch-mode': 'cors',
				'sec-fetch-site': 'same-site',
				'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
				'x-ig-app-id': '936619743392459',
				'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'}
			time.sleep(slp)
			j=r.get(urCH,headers=hedCH)
			
			try:
				foCH = str(j.json()['inbox']['threads'][0]['thread_id'])
				
				foCU = str(j.json()['inbox']['threads'][0]['users'][0]['username'])
				aco()
			except IndexError:
				print('\nThere are no messages to delete !')
				exit()
	idCHT()
def sc():
	global headLG , go , datLG , slp
	st = go.json()['checkpoint_url']
	coke = go.cookies
	urSC= 'https://www.instagram.com' + st
	g=r.post(urSC,data=datLG,headers=headLG,cookies=coke)
	if ("phone_number") in g.text:
		print("\n 0 >> Phone \n")
	if ("email") in g.text:
		print("\n 1 >> Email \n")
	snd = input('Enter the type of send : ')
	datSC = {
		"choice": snd}
	go1 = r.post(urSC,data=datSC,headers=headLG,cookies=coke)
	if ("security_code") in go1.text:
		code = input('\n Enter the security code : ')
		datCO = {
			"security_code": code}
		go = requests.post(urSC,data=datCO,headers=headLG,cookies=coke)
		if ("ok") in go.text:
			print(f'\n\tHello {user} | Done login\n')
			if joker == '54525243431':
				slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
				print('')
				chatMS()
		elif joker == '1':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			chatMS()
		elif joker == '325354234':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			post()
		elif joker == '25352454':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			chatMS()
		else:
			print('\n The security code is invalid !')
def ta():
	global headLG , go ,slp
	datTA = {
		'username': user,
		'verificationCode': cod,
		'identifier': st,
		'queryParams': '{"next":"/"}'}
	
	go = r.post('https://www.instagram.com/accounts/login/ajax/two_factor/', headers=headLG,data=datTA,cookies=coke)
	
	if ("userId") in go.text:
		print(f'\n\tHello {user} | Done login\n')
		if joker == '1':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			chatMS()
	if joker == '1':
		slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
		print('')
		chatMS()
		elif joker == '3':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			chatMS()
		elif joker == '4':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			chatMS()
	elif ("checkpoint_url")  in go.text:
		sc()
	else:
		print('\n The security code is invalid !')

def login():
	global headLG , go , datLG , slp 
	urLG = "https://www.instagram.com/accounts/login/ajax/"
	headLG = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'content-length': '272',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; shbid=6144; shbts=1614374582.8963153',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/accounts/login/',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': '0',
		'x-instagram-ajax': '790551e77c76',
		'x-requested-with': 'XMLHttpRequest'}
	
	datLG = {
		"username": user,
		"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{pess}",
		"queryParams": "{}",
		"optIntoOneTap": "false"}
	
	go = r.post(urLG,headers=headLG,data=datLG)
	
	if ("userId") in go.text:
		print(f'\n\tHello {user} | Done login\n')
		if joker == '1634765':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			chatMS()
		elif joker == '1':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			chatMS()
		elif joker == '7643':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			chatMS()
		elif joker == '474':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			chatMS()
	elif ("two_factor") in go.text:
		print('\n Binary verification \n')
		ta()
	elif ("checkpoint_url")  in go.text:
		print('\n Account Secure \n')
		sc()
	else:
		print('\nThe username or password is wrong ! \n')
login()
ta()

