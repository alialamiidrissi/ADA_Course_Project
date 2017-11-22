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

def build_params(course, cuisine, max_results):
	params = {'allowedCuisine[]': 'cuisine^cuisine-{}'.format(cuisine),
			  'allowedCourse[]': 'course^course-{}'.format(course),
			  'maxResult': max_results}
	return params

def get_search_results(url, retry=True):
	try:
		return requests.get(url, timeout=time_out).json()
	except Exception:
		print("[Error] Raised Exception..")
		if retry:
			print("[Error] Retrying on {}".format(url))
			return get_search_results(url, retry)
		else:
			raise Exception

sample_ratio = 0.3
time_out = 300
max_results = 2
api_id = '97235512'
api_key = '910547f3d9b411971d1318bd99a18460'
endpoint = 'http://api.yummly.com/v1/api/recipes?_app_id={}&_app_key={}'.format(api_id, api_key)
# print('http://api.yummly.com/v1/api/metadata/cuisine?_app_id={}&_app_key={}'.format(api_id, api_key))
# exit()

data = []
courses = ['Main Dishes']
cuisines = ['American','Chinese','Cuban','English','French','German','Greek','Hawaiian','Hungarian','Indian','Irish','Italian','Japanese','Mexican','Moroccan','Portuguese','Spanish','Swedish','Thai']
for course in courses:
	for cuisine in tqdm(cuisines):
		cuisine = cuisine.lower()
		json_file = './data/results_'+cuisine+'_'+course+'.json'
		if os.path.exists(json_file):
			continue

		# params = build_params(course, cuisine, 2)
		# r = get_search_results(build_query(endpoint, params))

		# print("[Info] {} results for {} cuisine".format(r['totalMatchCount'], cuisine))
		# print("'{}': {}".format(cuisine, r['totalMatchCount']))
		
		# max_results = int(max(1500, r['totalMatchCount']*0.3))
		params = build_params(course, cuisine, 1000)
		url = build_query(endpoint, params)
		with open('search_url.txt', 'a') as uf:
			uf.write(url+'\n')

		r = get_search_results(build_query(endpoint, params))

		with open(json_file, 'w') as jf:
			json.dump(r, jf)

		# time.sleep(300)