import numpy as np
import os
import json
import requests
from tqdm import tqdm
import time
from random import randint

def get_url(url, retry=True, time_out=3, n=3):
	if n==0:
		return None
	try:
		return requests.get(url, timeout=time_out).json()
	except Exception:
		print("[Error] Raised Exception on {}..".format(url))
		if retry:
			print("[Error] Retrying on {}".format(url))
			return get_url(url, retry, time_out, n=n-1)
		else:
			raise Exception

api_id = 'INSERT_API_ID'
api_key = 'INSERT_API_KEY'
data_folder = './data/lists/'
res_folder = './data/recipes/'

for cuisine_result_filename in os.listdir(data_folder):
	if not cuisine_result_filename.split('.')[-1] == 'json':
		continue
	file_path = os.path.join(data_folder, cuisine_result_filename)
	print('[Info] Reading results from {}'.format(cuisine_result_filename))
	with open(file_path) as jf:
		results = json.load(jf)['matches']

	for result in tqdm(results):
		id_ = result['id']
		url = 'http://api.yummly.com/v1/api/recipe/{}?_app_id={}&_app_key={}'.format(id_, api_id, api_key)
		json_file = os.path.join(res_folder, id_+'.json')
		if os.path.exists(json_file):
			continue
		recipe_info = get_url(url)
		if recipe_info is None:
			continue
		if not os.path.exists(res_folder):
			os.mkdir(res_folder)
		with open(json_file, 'w') as jf:
			json.dump(recipe_info, jf)
		time.sleep(randint(0,3))