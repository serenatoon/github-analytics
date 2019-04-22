import requests
import sys
import json

GITHUB_ENDPOINT = "https://api.github.com/"

def get_repos(username):
    global GITHUB_ENDPOINT
    endpoint = GITHUB_ENDPOINT + "users/" + username + "/repos"
    print endpoint
    req = requests.get(endpoint)
    json_data = req.json()
    return json_data


def get_views(repo, username, password):
    global GITHUB_ENDPOINT
    endpoint = GITHUB_ENDPOINT + "repos/" + repo + "/traffic/views"

    req = requests.get(endpoint, auth=(username, password))
    print req.text


def get_clones(repo, username, password):
    global GITHUB_ENDPOINT
    endpoint = GITHUB_ENDPOINT + "repos/" + repo + "/traffic/clones"

    req = requests.get(endpoint, auth=(username, password))
    print req.text


def main(username, password):
    repos = get_repos(username)
    for key in repos:
        repo = key['full_name']
        print repo
        get_views(repo, username, password)
        get_clones(repo, username, password)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Script usage: analytics.py USERNAME PASSWORD"
    else:
        main(sys.argv[1], sys.argv[2])
