# Closed issues with label "enhancement" "for i in `seq 1 10`; do curl "https://api.github.com/repos/jashkenas/backbone/issues?labels=enhancement&state=closed&page=$i&per_page=100&access_token=<access_token>" >> backbone-issues.json; done;
# Pull requests: "for i in `seq 1 10`; do curl "https://api.github.com/repos/jashkenas/backbone/pulls?state=closed&page=$i&per_page=100&access_token=<access_token>" >> backbone-pr.json; done;

from collections import defaultdict
import json
from pprint import pprint
import requests

ACCESS_TOKEN = "INSERT YOUR GITHUB API TOKEN HERE"
REPO_PATH = "Homebrew/homebrew"
REPO_NAME = "homebrew"
LABEL = "features"

# e.g. https://api.github.com/repos/jashkenas/backbone/issues?labels=enhancement&state=closed&access_token=<access_token>
enhancement_issues_url = "https://api.github.com/repos/{}/issues?labels={}&state=closed&access_token={}".format(REPO_PATH, LABEL, ACCESS_TOKEN)
closed_pull_requests_url = "https://api.github.com/repos/{}/pulls?state=closed&access_token={}".format(REPO_PATH, ACCESS_TOKEN)

def get_json(url):
	page_num = 1
	url += "&page={}&per_page=100".format(page_num)
	results = []
	request_result = requests.get(url).json()

	# Paginate through the issues/PRs
	while request_result:
		print (url)
		results.extend(request_result)
		request_result = requests.get(url).json()
		url = url.replace("&page={}".format(page_num), "&page={}".format(page_num + 1))
		page_num += 1

	return results

def main():
	enhancement_issues = get_json(enhancement_issues_url)
	closed_PRs = get_json(closed_pull_requests_url)

	# Get pull requests that were actually merged into master.
	merged_prs = [x for x in closed_PRs if x["merged_at"]]

	merged_prs_urls = set()
	for pr in merged_prs:
		merged_prs_urls.add(pr["url"])

	# Get enhancement issues that have a corresponding pull request associated with it.
	issues = [x for x in enhancement_issues if "pull_request" in x]
	# Get the pull requests that were merged AND are associated with issues labeled as enhancemenets.
	features = [issue for issue in enhancement_issues if "pull_request" in issue \
				and "url" in issue["pull_request"] and issue["pull_request"]["url"] in merged_prs_urls]
	pprint(features)

	with open("{}.json".format(REPO_NAME), "w+") as output_file:
		json.dump(features, output_file, sort_keys=True, indent=4)

if __name__ == "__main__":
	main()