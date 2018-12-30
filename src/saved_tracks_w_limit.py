import spotipy
from dotmap import DotMap
from user_token import AUTH_TOKEN
from pprint import pprint

sp = spotipy.Spotify(auth=AUTH_TOKEN)
results = sp.current_user_saved_tracks(limit=1000)
results = DotMap(results)
# pprint(results)
for item in results["items"]:
    track = item.track
    print("\t|\t".join([track.name, track.artists[0].name]))
