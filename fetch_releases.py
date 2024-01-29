import requests
import json
from urllib.request import urlretrieve
from pathlib import Path

gh_api = "http://api.github.com/repos/AgastyaPatel/github-releases-playground/"

# headers
headers = {'Accept': 'application/vnd.github+json'}

# parameters
parameters = {'per_page': 5}

r = requests.get(gh_api + 'releases', headers= headers)

dictObj = json.loads(r.text)
jsonObj = json.dumps(dictObj, indent= 2)
print(jsonObj)

for obj in dictObj:
    print(obj['tag_name'], obj['name'], obj['assets_url'])


# Downloading asset

r = requests.get(gh_api + 'releases/assets/148439117', headers= headers)
file = json.loads(r.text)
print(file['name'], file['browser_download_url'])
u = urlretrieve(file['browser_download_url'], file['name'])
print(u)