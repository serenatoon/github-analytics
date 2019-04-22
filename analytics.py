import requests

endpoint = "https://api.github.com/repos/serenatoon/spacelords/traffic/views"
auth = "serenatoon"

req = requests.get(endpoint, auth=('serenatoon', ''))
print req.json()