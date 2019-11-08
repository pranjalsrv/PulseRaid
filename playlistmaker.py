import spotipy
import spotipy.util as util
import pickle
from pprint import pprint


scope = 'user-library-read'
username = 'bm3vd1jidrsxrrhco9vukoe6p'
token = util.prompt_for_user_token(username, scope, client_id='acd89ea2ad144fcb9569c4605e8d9a6d', client_secret='61c7190fe8b24b6b947a24c6d8e250c8',redirect_uri ='http://localhost:8000' )

sp = spotipy.Spotify(auth=token)
results = sp.current_user_saved_tracks()
trackuri = []
tracknames = [] 

try:
    while True:
        for i in results['items']:
            #print(i['track']['name'])
            #print(i['track']['uri'])
            trackuri.append(i['track']['uri'])
            tracknames.append(i['track']['name'])
    
        if results['next']:
            results = sp.next(results)
        else:
            break
except spotipy.client.SpotifyException:
    token = util.prompt_for_user_token(username,scope,client_id='acd89ea2ad144fcb9569c4605e8d9a6d',client_secret='6fbdeb9c51f44ad2ad2162c4a9c1baee',redirect_uri ='https://localhost/' )
    sp = spotipy.Spotify(auth=token)

print("Received all music")

index = 0
trackdata = []
for i in trackuri:
    #print(i)
    #print(tracknames[index])
    af = sp.audio_features(i)
    #pprint(af)
    for i in af:
        #print('Danceability: ',i['danceability'],'\n', 'Tempo: ',i['tempo'],'\n','Energy: ', i['energy'],'\n','Valence:', i['valence'], '\n')
        trackdata.append([tracknames[index], {'id': i['id'], 'danceability':i['danceability'], 'tempo':i['tempo'], 'energy': i['energy'],'valence':i['valence']}])
    #print(json.dumps(af, indent=4))
    index += 1

print("Retrieved audio features")
slow = [i for i in trackdata if i[1]['energy']<0.32]
fast = [i for i in trackdata if i[1]['danceability']>0.75]
normal = [i for i in trackdata if i not in slow and i not in fast]

print("Made all playlists")
print("Total songs: ", len(trackdata))
print("Songs in Slow playlists: ", len(slow))
print("Songs in Normal playlists: ", len(normal))
print("Songs in Fast playlists: ", len(fast))

userData = {"slow": slow, "normal": normal, "fast": fast}
pickle.dump(userData, open('userData.pkl', 'wb'))

print("Saved user data")
