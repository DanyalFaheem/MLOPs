import requests
from datetime import datetime, timedelta

# Set up variables for the GitHub API
url = "https://api.github.com/search/repositories"
params = {
    "q": "language:python created:" + (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d") + ".." + datetime.now().strftime("%Y-%m-%d"),
    "sort": "stars",
    "order": "desc",
}

# Send a GET request to the GitHub API
response = requests.get(url, params=params)

# Check for errors
if response.status_code != 200:
    print("Error: Failed to retrieve repositories.")
    exit()

# Parse the JSON response
repositories = response.json()["items"]

# Filter out repositories that have workflows defined
repositories_without_workflows = [repo for repo in repositories if not requests.get(repo["url"] + "/actions/workflows").json()["total_count"]]

# Print the names and URLs of the repositories
for repo in repositories_without_workflows:
    print(f"{repo['name']} - {repo['html_url']}")

