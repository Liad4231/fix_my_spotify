import sys
import spotipy
import spotipy.util as util
import pprint

scope = 'user-library-read'

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print "Usage: %s username" % (sys.argv[0],)
#     sys.exit()

username = "liad4231@gmail.com"
# token = util.prompt_for_user_token(username, scope)

if 1:
    sp = spotipy.Spotify(
        auth=r"BQD3z8CHC9ys82WusWzElEX4SlFMqW8VYV6Nb0F0dGw-MouCzQy535Hf6arNaFK9XhfnvRZc9c2BSnPthdM-_bh77kTm8jiMevBtuT-9nCyiW9FMgp-SAehQhOOTQo-Hp124QZRwG2wzqcU-z0kS4AxREXZ2EjkQLSdDvuUn0MKcdUA42yrg")
    results = sp.current_user_saved_tracks()
    pprint.pprint(results)
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)
