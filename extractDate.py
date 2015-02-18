#Importing modules
import json
from pprint import pprint

# open the json file from parse.py's output
json_data=open("backbone.json")

data = json.load(json_data)
json_data.close()

dates = []

# get all the pull request's "closed_at" date
for closeDate in data:
	dates.append((closeDate["closed_at"].split("T"))[0] + "\n")

# sorts the date
dates.sort();

# write the dates out to a result file 
with open("backbone.txt", "w") as f:
	for date in dates:
		f.write(date)