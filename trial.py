import spotipy
import spotipy.util as util

scope = 'user-modify-playback-state'
username = 'bm3vd1jidrsxrrhco9vukoe6p'
token = util.prompt_for_user_token(username, scope, client_id='acd89ea2ad144fcb9569c4605e8d9a6d', client_secret='61c7190fe8b24b6b947a24c6d8e250c8',redirect_uri ='http://localhost/' )

print(token)