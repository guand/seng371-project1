#Importing modules
import json
from pprint import pprint
from copy import deepcopy

JSON_FILE_PATH = "data/backbone.json"
LOC_FORMAT_OUTPUT = "data/gitstats/backbone.output"
OUTPUT_FILE_PATH = "data/backbone-result.txt"

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

# List to store all dates of the pull request
prDateList = []

# removes '\n' from each date. e.g. '2014-02-28\n'
for date in dates:
	prDateList.append(date.rsplit()[0])

# List to store all dates of the lines of code 
locDateList = []

# Copy the dates from the output files from extractDate.py and loc_formatter.py to list
with open (LOC_FORMAT_OUTPUT, "r") as f2:
	for line in f2:
		locDateList.append(line)

# Merge prDateList with locDateList since there may be 
# some dates in prDateList that are not in locDateList
prDateListCpy = deepcopy(prDateList);
for date in locDateList:
	if date.split()[0] in prDateListCpy:
		prDateListCpy.remove(date.split()[0])
locDateList += prDateListCpy
locDateList.sort()

# Adding the lines of code to the new elements that was 
# added from prDateList by grabbing the lines of code 
# from the previous element.
counter = 0
for date in locDateList:
	index = locDateList.index(date)
	if len(date.split()) == 1:		
		if counter == 0:
			# if first element does not have line number, it means
			# there the pull request was closed before any code were
			# added to the repository.
			locDateList[index] += " 0"
		else:
			locDateList[index] += " " + locDateList[index - 1].split()[1] 
	
	# removing "\n" at the end of every element		
	locDateList[index] = locDateList[index].rsplit("\n")[0]

	# replace whitespaces with a \t, so when copying result to
	# Google Spreadsheet or Excel, the data will be in correct cells
	locDateList[index] = locDateList[index].replace(" ", "\t")
	counter = counter + 1

# Write all the dates and the current number of 
# pull request at that time to a result file. 
pullRequestCount = 0
with open(OUTPUT_FILE_PATH, "w") as outFile:
	for locDate in locDateList:
		index = locDateList.index(locDate)
		if locDate.split()[0] in prDateList:
			pullRequestCount = pullRequestCount + 1;
			prDateList.remove(locDate.split()[0])

		# the \t is for properly copying data to correct cells when 
		# copying result file to Google Spreadsheet or Excel
		appendingString = "\t " + str(pullRequestCount) + "\n"
		locDateList[index] += appendingString
		outFile.write(locDateList[index])
