

def playSong(token, songID):
    import requests
    import json
    print(songID)
    body = {"uris": ["spotify:track:" + str(songID)], "offset": {"position": 0}, "position_ms": 0}
    headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer " + str(token)}

    #r = requests.put("https://api.spotify.com/v1/me/player/play?device_id=04362e386c7ea723fe958faec3a420fc7b781f2f", data=json.dumps(body), headers=headers)
    r = requests.put("https://api.spotify.com/v1/me/player/play?device_id=04362e386c7ea723fe958faec3a420fc7b781f2f",
                     data=json.dumps(body), headers=headers)

    print('Status Code: ', r.status_code)
    print('Content: ', r.content)

def pauseSong(token):
    import requests
    import json

    headers = {"Accept": "application/json", "Content-Type": "application/json",
               "Authorization": "Bearer " + str(token)}

    #r = requests.put("https://api.spotify.com/v1/me/player/pause?device_id=04362e386c7ea723fe958faec3a420fc7b781f2f", headers=headers)
    r = requests.put("https://api.spotify.com/v1/me/player/pause?device_id=04362e386c7ea723fe958faec3a420fc7b781f2f",
                     headers=headers)

    print('Status Code: ', r.status_code)
    print('Content: ', r.content)
