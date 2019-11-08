from flask import Flask, request
import json
import play_music
import pickle
import random
import pulse_synch



app = Flask(__name__)
 

access_token = ""
userData = pickle.load(open('userData.pkl', 'rb'))
@app.route('/auth', methods=['GET', 'POST'])
def combiner():
    global access_token
    if request.method == 'POST':
        dict = json.loads(request.data.decode())
        #print(dict)
        access_token = dict["access_token"]
        pulse = pulseReceiver()
        print('Average BPM calculated: ', pulse)
        playlist = moodCalculate(pulse)
        print('Mood calculated')

        if playlist == 'Illegal':
            print('User Away from Detector/ User asleep. Music paused.')
            play_music.pauseSong(access_token)
        else:
            songPlayer(playlist) #play_music.playSong(dict["access_token"], song='')
        return "From Flask Server: Received Token: " + dict["access_token"]


def pulseReceiver():
    pulseRate = sum(pulse_synch.bpm()[-10:])/10
    return pulseRate



def moodCalculate(pulse):
    if 55 < pulse <= 60:
        print('Mood: Slow')
        return userData["slow"]
    elif 80 > pulse >= 60:
        print('Mood: Normal')
        return userData["normal"]
    elif pulse >= 80:
        print('Mood: Workout')
        return userData["fast"]
    else:
        return 'Illegal'

def songPlayer(playlist):
    song = playlist[random.randint(0, len(playlist))]
    print("Playing Song: ",song[0])
    play_music.playSong(access_token, song[1]['id'])



if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug=True)
