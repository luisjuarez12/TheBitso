import requests
import pymongo
from pymongo import MongoClient
bit = MongoClient('localhost')
db = bit.bitso
bitso = db.bitso

if __name__=='__main__':
	url = 'https://api.bitso.com/v3/ticker/'
	args = 'btc_mx'
	response = requests.get(url, args)
	print(response.url)

	if response.status_code == 200:
		response_json1 = response.json()
		db.bitso.insert(response_json1)
		print(db.bitso.count())
