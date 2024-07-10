#!/usr/bin/python3
"""
Lists 10 commits (from most recent to oldest) of a repository by a user.
Usage: ./100-github_commits.py <repository name> <owner name>
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    r = requests.get(url)
    commits = r.json()

    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
