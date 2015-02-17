import os
import time

files = [('backbone.output', 'data/gitstats/backbone/lines_of_code.dat'),
		 ('bootstrap.output', 'data/gitstats/bootstrap/lines_of_code.dat'),
		 ('homebrew.output', 'data/gitstats/homebrew/lines_of_code.dat')]

def get_formatted_time(loc_file):
	for line in loc_file.readlines():
		current_date, loc = line.split()
		formatted_time = time.strftime('%Y-%m-%d', time.localtime(int(current_date)))
		yield "{} {}\n".format(formatted_time, loc)

for name, path in files:
	with open(path, "r") as loc_file:

		if not os.path.exists(os.getcwd() + '/' + path):
			os.makedirs(os.getcwd() + '/' + path)

		with open('/'.join([os.getcwd(), 'data/gitstats', name]), 'w+') as output_file:
			for line in get_formatted_time(loc_file):
				output_file.write(line)
