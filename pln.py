import os
try:
	import PrettyTable
	import requests
	import json
except ImportError:
	os.system('pip install prettytable')
	os.system('pip install requests')
	os.system('pip install json')
from prettytable import PrettyTable
import requests
import json

def grep():
	os.system('clear')
	print('Build With ♡ kumpul4semut')
	idpln = input("Enter your pln id?")
	print('please waiting')
	req = requests.get('http://174.138.27.250/pln/stimulus.php?idpln='+idpln)
	respon = json.loads(req.content)
	if(respon['status'] == 'error'):
		print(respon['message'])
	else:
		print('Nama: '+respon['nama'])
		for data in respon['result']:
			t = PrettyTable(['Tanggal', 'Kwh', 'token']) 
			t.add_row([data[0], data[6],data[7]])
			print(t)
		option = input('Again y/n??')
		if(option =='y'):
			grep()
		else:
			os.system('exit')

grep()
