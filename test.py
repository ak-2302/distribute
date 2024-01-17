import requests
import json
with open("header.json") as f:
    header = json.load(f)
res = requests.get("https://raw.githubusercontent.com/ak-2302/distribute/main/README.md?token=GHSAT0AAAAAACL5X7WSXHQHBT2MSQJCUWTCZNGHUHA",headers=header)
print(res.text)