# SENG 371 - Project 1
Software evolution research on an open-source project.
Jian Guan, Paul Moon, Jonathan Lam

### 1.0 Project Question
*How does the rate of feature additions change as a project grows in size?*

We think that the rate of feature additions is important because for a project, it shows the relationship between the number of features added and the size of the project. Developers may be interested in this to see if they are continuing to add features to improve user satisfaction rather than only fixing bugs.

### 2.0 Methodology
#### 2.1  Codebases chosen for analysis
We will analyze three codebases:
- [Backbone](https://github.com/jashkenas/backbone)
- [Bootstrap](https://github.com/twbs/bootstrap)
- [Homebrew](https://github.com/Homebrew/homebrew)

These codebases were chosen primarily because they practice good use of labeling on issues and pull requests. This will be important as we assume that new features will have a label like "new feature" or "feature".

#### 2.2  Methodology
We used the following tools:
- [GitHub API](https://developer.github.com/v3/): Using a URL like `https://api.github.com/repos/twbs/bootstrap/issues?labels=feature&state=closed`, a list of closed issues with the `feature` label was obtained. Because we want a list of pull requests that were actually merged into master (since the list of feature issues could contain feature requests that were never worked on), the list of pull requests merged into master were obtained from another URL: `https://api.github.com/repos/twbs/bootstrap/pulls?state=closed`. The two lists were merged with a Python script ([parser.py](https://github.com/guand/seng371-project1/blob/master/parse.py)).
- [Gitstats](http://gitstats.sourceforge.net/): Gitstats was used to get the lines of code from a GitHub repository. Because Gitstats returns the data in a `epochTime linesOfCode` format, another Python script was used to convert the epoch time to a YYYY-MM-DD format ([loc_formatter.py](https://github.com/guand/seng371-project1/blob/master/loc_formatter.py)).
- [Google Sheets](http://www.google.ca/sheets/about/): Google Sheets was used to plot the graphs.
- The scripts used for gathering and parsing the data were written in Python.

After gathering the data, the final step was to merge the two data sets, because the LOC had more data points than the number of merged feature pull requests, and the date data had to be merged to plot a graph. Google Spreadsheets was used to generate the final graphs.

##### Metrics Gathered
- List of issues with label 'feature' or 'new feature' (name can be different for each repo) that are closed. We gathered this data to obtain only the issues which were considered as features, as opposed to styling changes, bug fixes, documentation etc. Only closed issues were obtained because we do not want to analyze open issues that are still waiting to be worked on.
- List of pull requests that are closed. Only the closed pull requests were obtained because we considered only the pull requests which were actually merged into the repo.
- Lines of code from GitHub repositories over time. This will approximate the project size over time, which is necessary because we are analyzing how the rate of feature additions change **as the project grows**.

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
Lastly, copy the data in the result file to a Google Sheet file, and graph it!

### 4.0 Results & Analysis
#### 4.1  Results

The raw results can be found in `data` directory (here)[https://github.com/guand/seng371-project1/tree/master/data]. Below are the graphs showing the relationship between feature additions and LOC over time for each of our repositories.

- Backbone:

![Backbone result](https://cloud.githubusercontent.com/assets/5192167/6324839/8bb51596-baf4-11e4-8001-6b35f8692dcf.png)

- Bootstrap:

![Bootstrap result](https://cloud.githubusercontent.com/assets/5192167/6324837/880d2dca-baf4-11e4-9e8a-09fc7334cf3c.png)

- Homebrew:

![Homebrew result](https://cloud.githubusercontent.com/assets/5192167/6324840/8e296ee4-baf4-11e4-91f8-e45325d61dc5.png)

#### 4.2  Analysis
Our hypothesis was that the rate of feature additions will be inversely proportional to the project size i.e. LOC.

##### 4.2.1 Backbone
The graph shows that the slopes for both LOC and enhancement pull requests were both positive and relatively unchanging. This shows that as the project grew in size, the rate at which feature pull requests were merged into master was not affected. 

##### 4.2.2 Bootstrap
The Bootstrap repo graph shows that from the beginning of the project to around 01/01/2013, not many features were added to the repo while the LOC grew and shrunk. After 01/01/2013, the rate at which features were added exploded. This may be explained by the growing popularity of Bootstrap as shown by the Google Search Trends below. The slope of the feature additions line is unchanging as the project size grows, which suggests that there is no significant causal relationship between them, contrary to our hypothesis. 

![Bootstrap searchtrends](https://cloud.githubusercontent.com/assets/1689157/6340764/96f03444-bb77-11e4-939e-205745bd6e6a.png)

##### 4.2.3 Homebrew
The Homebrew graph shows that no feature pull requests were added to the repo except between December 2012 and August 2013, during which a total of 8 features were added. The project size grew consistently but the rate of feature addition was relatively unchanging. This could be because the maintainers stopped using the labels or incorrectly use the labels (e.g. documentation was labeled as a feature).

##### 4.2.4 Overall Analysis
Based on our analysis, our hypothesis was proven wrong. The Backbone and Bootstrap repos showed that the rate of feature addition (slope) was consistent with the rate of project growth. The Homebrew data was not considered to be significant for our analysis, because there was not enough feature pull requests to be statistically significant (only 8 feature additions over 6 years)

###### Threats to validity
- Not all features will be labeled diligently by the maintainers. Similarly, not all features labeled as features may not actually be features. Our analysis does not take human error into account.
- If the project suddently becomes popular, there may be an increase in feature requests, and consequently feature additions to the repo. We did not take this into account in our analysis, but this can play a big role in feature additions (see popularity of Bootstrap in Section 4.2.2).
- Analyzing only three repos out of thousands is not considered as statistically significant.

###### Future work
- Analyze more repos.
- Come up with a better, more consistent way of classifying pull requests as feature additions.
- Improve the scripts for reusability e.g. take repo names from a file input, or use Google Sheet API for automatically generating graphs.

### 5.0 Project Management Information
#### 5.1  Milestones
##### Milestone 1 - January 27
- Come up with a project question
- Pick repositories
- Describe the methodology for the project question

##### Milestone 2 - February 3
- Create a hypothesis for the project based on the project question
- Collect data from the repositories chosen

##### Milestone 3 - February 17
- Analyze the collected data
- Provide an assertion based on the data

##### Milestone 4 - February 23
- Thoroughly analyze the three repositories using statistics and graphs
- Finish the project report

#### 5.2  Project Members
- Jian Guan @guand: Developer
- Paul Moon @paulmoon: Developer
- Jonathan Lam @lamj1234: Developer
