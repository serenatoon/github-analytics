import requests
import sys


def main(username, password):
    endpoint = "https://api.github.com/repos/serenatoon/spacelords/traffic/views"

    req = requests.get(endpoint, auth=(username, password))
    print req.json()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Script usage: analytics.py USERNAME PASSWORD"
    else:
        main(sys.argv[1], sys.argv[2])
