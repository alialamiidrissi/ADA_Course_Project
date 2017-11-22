import os


for file in os.listdir('.'):
	if not file[:6] == 'recipe':
		continue

	args = {}
	for arg in file[8:].split('&'):
		if len(arg.split('=')) > 1:
			args[arg.split('=')[0]] = arg.split('=')[1]

	new_file_name = './data/results_Main Dishes_'+args['allowedCuisine[]'].replace('cuisine%5Ecuisine-','')+'.json'
	os.system('mv -f "./{}" "{}"'.format(file, new_file_name))
	