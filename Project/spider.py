import requests
import json
import pandas as pd
import numpy as np
import time, os
from tqdm import tqdm

def build_query(endpoint, params):
	url = endpoint
	for key in params.keys():
		url += '&'+key+'='+str(params[key])
	print("[Info] Requesting API at {}".format(url))
	return url

time_out = 300
max_results = 500
api_id = 'INSERT_API_ID'
api_key = 'INSERT_API_KEY'
endpoint = 'http://api.yummly.com/v1/api/recipes?_app_id={}&_app_key={}'.format(api_id, api_key)


data = []
cuisines = ['American','Asian','Chinese','Cuban','English','French','German','Greek','Hawaiian','Hungarian','Indian','Irish','Italian','Japanese','Mexican','Moroccan','Portuguese','Spanish','Swedish','Thai']
for cuisine in tqdm(cuisines):
	if os.path.exists(cuisine.lower()+'.json'):
		continue

	params = {'allowedCuisine[]': 'cuisine^cuisine-{}'.format(cuisine),
			  'allowedCourse[]': 'course^course-Main Dishes',
			  'maxResult': max_results}
	r = requests.get(build_query(endpoint, params), timeout=time_out).json()

	print(r.keys())
	print(r['totalMatchCount'])
	print(len(r['matches']))

	with open(cuisine.lower()+'.json', 'w') as jf:
		json.dump(r['matches'], jf)

	time.sleep(300)