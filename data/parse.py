# Closed issues with label "enhancement" "for i in `seq 1 10`; do curl "https://api.github.com/repos/jashkenas/backbone/issues?labels=enhancement&state=closed&page=$i&per_page=100&access_token=<access_token>" >> backbone-issues.json; done;
# Pull requests: "for i in `seq 1 10`; do curl "https://api.github.com/repos/jashkenas/backbone/pulls?state=closed&page=$i&per_page=100&access_token=<access_token>" >> backbone-pr.json; done;

from collections import defaultdict
import json
from pprint import pprint

with open("backbone-pr.json") as pr_file:
	pull_requests = json.load(pr_file)
	merged_prs = [x for x in pull_requests if x["merged_at"]]

	merged_prs_urls = set()
	for pr in merged_prs:
		merged_prs_urls.add(pr["url"])

	with open("backbone-issues.json") as issue_file:
		issues = json.load(issue_file)
		issues = [x for x in issues if "pull_request" in x]

		features = [issue for issue in issues if issue["pull_request"]["url"] in merged_prs_urls]
		pprint(features)
