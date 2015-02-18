#Importing modules
from copy import deepcopy

# List to store all dates of the pull request
prDateList = []
# List to store all dates of the lines of code 
locDateList = []

# Copy the dates from the output files from extractDate.py and loc_formatter.py to list
with open("backbone.txt", "r") as f1, open ("backbone.output", "r") as f2:
	for line1 in f1:
		prDateList.append(line1.rsplit()[0])
	for line2 in f2:
		locDateList.append(line2)

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
with open("backbone-result.txt", "w") as outFile:
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
