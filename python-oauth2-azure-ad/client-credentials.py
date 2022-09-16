import requests, json

tenant = "<tenant-id>"
client_id = "<client-id>"
client_secret = "<client-secret>"

url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
body = {'client_id': client_id, 'scope': 'https://management.azure.com//.default', 'client_secret': client_secret, 'grant_type': 'client_credentials'}
r = requests.post(url, data=body)
json_text = r.text
j = json.loads(json_text)
access_token = j['access_token']
print(access_token)

params = {'api-version': '2020-01-01'}
headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'}
url = 'https://management.azure.com/' + 'tenants'
r = requests.get(url, headers=headers, params=params)
print(json.dumps(r.json(), indent=4, separators=(',', ': ')))