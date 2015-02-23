# SENG 371 - Project 1
Software evolution research on an open-source project.
Jian Guan, Paul Moon, Jonathan Lam

### 1.0 Project question
How does the rate of feature additions change as a project grows in size?

### 2.0 Methodology (including the tools you expect to use)
#### 2.1  Codebases/Systems you will analyze
We will analyze three codebases:
- [Backbone](https://github.com/jashkenas/backbone)
- [Bootstrap](https://github.com/twbs/bootstrap)
- [Homebrew](https://github.com/Homebrew/homebrew)

These codebases were chosen primarily because they practice good use of labeling on issues and pull requests. This will be important as we assume that new features will have a label like "new feature" or "feature".

#### 2.2  Methodology
We used the following tools:
- [GitHub API](https://developer.github.com/v3/): Using a URL like `https://api.github.com/repos/twbs/bootstrap/issues?labels=feature&state=closed`, a list of closed issues with the `feature` label was obtained. Because we want a list of pull requests that were actually merged into master (since the list of feature issues could contain feature requests that were never worked on), the list of pull requests merged into master were obtained from another URL: `https://api.github.com/repos/twbs/bootstrap/pulls?state=closed`. The two lists were merged with a Python script ([parser.py](https://github.com/guand/seng371-project1/blob/master/parse.py)).
- [Gitstats](http://gitstats.sourceforge.net/): Gitstats was used to get the lines of code from a GitHub repository. Because Gitstats returns the data in a `epochTime linesOfCode` format, another Python script was used to convert the epoch time to a YYYY-MM-DD format ([loc_formatter.py](https://github.com/guand/seng371-project1/blob/master/loc_formatter.py)).

After gathering the data, the final step was to merge the two data sets, because the LOC had more data points than the number of merged feature pull requests, and the date data had to be merged to plot a graph. Google Spreadsheets was used to generate the final graphs.

### 3.0 Quick Start
#### 3.1 Requirements
- Python 2.7+ 
- Access Token for Git API: To get Token follow these steps Profile -> Settings -> Applications -> Personal Access Token -> Generate Token

#### 3.2  Obtaining pull request/issues from GitHub.
Edit the following configurations in `parse.py`:
- ACCESS_TOKEN: This should be your GitHub API token.
- REPO_PATH: Repository path e.g. twbs/bootstrap or Homebrew/homebrew
- REPO_NAME: Repository name e.g. homebrew
- LABEL: The label for an issue that will be matched with pull requests that got merged into master. This is different for each repo, so be aware.

Then run it: `python parse.py`. It should output a JSON file of pull requests that were merged into master AND issues that had your label.

#### 3.3  Gitstats
- `git clone https://github.com/hoxu/gitstats.git`
- Rename `gitstats` into `gitstats.py`
- `python gitstats.py ../path/to/repo output`

#### 3.4  Formatting epoch time to YYYY-MM-DD (loc_formatter.py)
Go into the output directory from the previous step, and look for `lines_of_code.dat`.
- Edit `loc_formatter.py` so that `files` contains tuples of (output_file_name, /relative/path/to/lines_of_code.dat).
- `python loc_formatter.py ../path/to/lines_of_code.dat` from this repo's directory.

Formatted files will reside in data/ directory.

#### 3.5  Merging the data sets.
Edit the following configurations in `construct_data.py`:
- JSON_FILE_PATH: This should be the path to your results from 'parse.py'
- LOC_FORMAT_OUTPUT: This should be the path to your results from 'loc_formatter.py'
- OUTPUT_FILE_PATH: This is the path where the result output file will be saved e.g. data/bootstrap-result.txt, where bootstrap-result.txt is the output file that will be created after you run 'construct_data.py'

Then run it: `python construct_data.py`. It should output a .txt file containing the data to construct your table and graph.
Lastly, copy the data in the result file to a Google Spreadsheet and graph!

### 4.0 Results & Analysis
#### 4.1  Graphs
- Backbone:

![Backbone result](https://cloud.githubusercontent.com/assets/5192167/6324839/8bb51596-baf4-11e4-8001-6b35f8692dcf.png)

- Bootstrap:

![Bootstrap result](https://cloud.githubusercontent.com/assets/5192167/6324837/880d2dca-baf4-11e4-9e8a-09fc7334cf3c.png)

- Homebrew:

![Homebrew result](https://cloud.githubusercontent.com/assets/5192167/6324840/8e296ee4-baf4-11e4-91f8-e45325d61dc5.png)

#### 4.2  Analysis




### 5.0 Project Management Information
#### 5.1  Milestones
##### Milestone 1 - January 27
- Create project question
- Pick repositories
- Describe the methodology for testing question

##### Milestone 2 - February 3
- Create a hypothesis for the project based on the project question
- Collect data from the repositories chosen

##### Milestone 3 - February 17
- Analyze the collected data
- Provide an assertion based on the data

##### Milestone 4 - February 23
- Thoroughly analyze the three repositories using statistics and graphs

#### 5.2  Project Members
- Jian Guan @guand
- Paul Moon @paulmoon
- Jonathan Lam @lamj1234
