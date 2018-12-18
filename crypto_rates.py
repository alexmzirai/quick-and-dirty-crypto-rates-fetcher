import requests
import json


# base url = http://api.coinlayer.com/api

access_key = '82200a3abce6307108133289310bbe2c'

api_url_base = 'http://api.coinlayer.com/api/'

headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(access_key)}

# code to actually fetch the 2 endpoints

print('==================================')

# "live" endpoint - request the most recent cryptocurrency rates
def get_live_list():
	api_url = '{0}live'.format(api_url_base)
	response = requests.get(api_url, headers=headers)

	if response.status_code == 200:
		print("working fine for live list")
		data = json.loads(response.content.decode('utf-8'))	# convert content into python dict for easy reading
		
		for k, v in data.items():
			print('{0}:{1}'.format(k, v))
	else:
		#return None
		print ("bummer!")

print('==================================')

# "list" endpoint - request a JSON list containing all supported crypto and fiat currencies
def get_json_list():
	api_url = '{0}list'.format(api_url_base)
	response = requests.get(api_url, headers=headers)

	if response.status_code == 200:
		print("working fine for json list")
		data = json.loads(response.content.decode('utf-8'))
		
		for k, v  in data.items:
			print('{0}:{1}'.format(k, v))
	else:
		#return None
		print("bummer!")

"""
info = get_live_list()	# sets info variable to whatever came back from the call to get_live_list
if info is not None:
	print("Here's your info..")
	for k, v in response.items():
		print('{0}:{1}'.format(k, v))
else:
	print("[!]Request for live rates failed.")

# error handling for 2nd request
info2 = get_json_list()
if info2 is not None:
	print("Here's your info..")
	for k, v in info2['list'].items():
		print('{0}:{1}'.format(k, v))
else:
	print("[!]Request for list of rates failed.")
"""












