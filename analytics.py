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
    for key in json_data:
        print key['full_name']


def main(username, password):
    get_repos(username)
    # endpoint = "https://api.github.com/repos/serenatoon/spacelords/traffic/views"

    # req = requests.get(endpoint, auth=(username, password))
    # print req.json()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Script usage: analytics.py USERNAME PASSWORD"
    else:
        main(sys.argv[1], sys.argv[2])
