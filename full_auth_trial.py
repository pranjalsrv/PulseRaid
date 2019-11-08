import requests
import base64
import json
payload = "c4b9f033dae343ff96a75305672a4a31" + ":" + "6b5e8a364475498c920cce8bb6bfaf46"

encodedPayload = base64.b64encode(payload.encode('utf-8'))

body = "grant_type=client_credentials&scope=playlist-modify-public playlist-modify-private"
headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + str(encodedPayload)
    }

r = requests.post("https://accounts.spotify.com/api/token", data=body, headers=headers)

print('Status Code: ', r.status_code, r.content)
