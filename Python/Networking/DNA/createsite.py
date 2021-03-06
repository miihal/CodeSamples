import requests
import json

################ LOGIN ######################
url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

user = 'devnetuser'
pw = 'Cisco123!'

response = requests.post(url, auth=(user, pw)).json()
# print(response)
token = response['Token']

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/site"

payload = {}
headers = {
    'x-auth-token': token,
    'Accept': 'application/json'
}

my_site = {
    "type": "area",
    "site": {
        "area": {
            "name": "Baton Rouge",
            "parentName": "Global/USA"
        }
    }
}

response = requests.post(url, data=my_site, headers=headers).json()

print(json.dumps(response, indent=2))
