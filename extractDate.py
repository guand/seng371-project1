#Importing modules
import json
from pprint import pprint

JSON_FILE_PATH = "data/backbone.json"
OUTPUT_FILE_PATH = "data/backbone.txt"

# open the json file from parse.py's output
json_data=open(JSON_FILE_PATH)

data = json.load(json_data)
json_data.close()

dates = []

# get all the pull request's "closed_at" date
for closeDate in data:
	dates.append((closeDate["closed_at"].split("T"))[0] + "\n")

# sorts the date
dates.sort();

# write the dates out to a result file 
with open(OUTPUT_FILE_PATH, "w") as f:
	for date in dates:
		f.write(date)