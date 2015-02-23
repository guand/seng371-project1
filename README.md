# SENG 371 - Project 1
Software evolution research on an open-source project.
Jian Guan, Paul Moon, Jonathan Lam

### Project question
How does the rate of feature additions change as a project grows in size?

### Methodology (including the tools you expect to use)
We can use Gource to visualize the additions of features in the system. We can use GitHub API to measure the rate of feature additions based on the labels on pull requests, and also count the lines of code to approximate the size of the project.

### Codebases/Systems you will analyze
Using the methodology above, we will analyze three codebases:
- [Backbone](https://github.com/jashkenas/backbone)
- [Bootstrap](https://github.com/twbs/bootstrap)
- [Homebrew](https://github.com/Homebrew/homebrew)

### Project milestones
#### Milestone 1 - January 27
- Create project question 
- pick repositories 
- figure out the methodology for testing question

#### Milestone 2 - February 03
- Create a hypothesis for the project based on the project question
- Collect Data from the repositories chosen

#### Milestone 3 - February 17
- Using the collected data from the repositories, do an analysis on the data
- Give an assertion based on the data

#### Milestone 4 - February 23
- will have a thorough analysis of these three repos showing Gource videos and statistics for answering the project question.

### Current Issues
- How can we get the lines of code (LOC) over time from the repositories?
- What is a good way of graph LOC to feature additions over time? Google Docs? Excel?

## Installation Guide
### Requirements
- Python 2.6+ 
- Access Token for Git API: To get Token follow these steps Profile->Settings->Applications->Presonal Access Token->Generate Token
- Clone [git-loc](https://github.com/ITikhonov/git-loc)

### Quick Start
##### Edit the following configurations in `parse.py`:
- ACCESS_TOKEN: This should be your GitHub API token.
- REPO_PATH: Repository path e.g. twbs/bootstrap or Homebrew/homebrew
- REPO_NAME: Repository name e.g. homebrew
- LABEL: The label for an issue that will be matched with pull requests that got merged into master. This is different for each repo, so be aware.

Then run it: `python parse.py`. It should output a JSON file of pull requests that were merged into master AND issues that had your label.

##### Edit the following configurations in `extractDate.py`:
- JSON_FILE_PATH: This should be the path to your results from 'parse.py'
- OUTPUT_FILE_PATH: This is the path where the output file will be saved e.g. data/bootstrap.txt, where bootstrap-result.txt is the output file that will be created after you run 'extractDate.py'

Then run it: `python extractDate.py`. It should output a .txt file of the "closed_at" dates of each pull requests.

##### Edit the following configurations in `merge.py`:
- EXTRACT_DATE_OUTPUT: This should be the path to your results from 'extractDate.py'
- LOC_FORMAT_OUTPUT: This should be the path to your results from 'loc_formatter.py'
- OUTPUT_FILE_PATH: This is the path where the result output file will be saved e.g. data/bootstrap-result.txt, where bootstrap-result.txt is the output file that will be created after you run 'merge.py'

Then run it: `python merge.py`. It should output a .txt file containing the data to construct your table and graph.
Lastly, copy the data in the result file to a Google Spreadsheet and graph!

Resulting ouput graph from Google Spreadsheet should look something like:

- Backbone:

![Backbone result](https://cloud.githubusercontent.com/assets/5192167/6324839/8bb51596-baf4-11e4-8001-6b35f8692dcf.png)

- Bootstrap:

![Bootstrap result](https://cloud.githubusercontent.com/assets/5192167/6324837/880d2dca-baf4-11e4-9e8a-09fc7334cf3c.png)

- Homebrew:

![Homebrew result](https://cloud.githubusercontent.com/assets/5192167/6324840/8e296ee4-baf4-11e4-91f8-e45325d61dc5.png)
