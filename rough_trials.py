import pickle
import random

userData = pickle.load(open('userData.pkl', 'rb'))

playlist = userData["slow"]
print(playlist[random.randint(0, len(playlist))][1]['id'])