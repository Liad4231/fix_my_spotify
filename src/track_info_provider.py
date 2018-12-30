import spotipy
from dotmap import DotMap
from user_token import AUTH_TOKEN

_ = '''
{'album': {'album_type': 'single',
  'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q'},
    'href': 'https://api.spotify.com/v1/artists/53XhwfbYqKCa1cC15pYq2q',
    'id': '53XhwfbYqKCa1cC15pYq2q',
    'name': 'Imagine Dragons',
    'type': 'artist',
    'uri': 'spotify:artist:53XhwfbYqKCa1cC15pYq2q'}],
  'available_markets': [],
  'external_urls': {'spotify': 'https://open.spotify.com/album/3rar7GKCodqR9GIIiNe75H'},
  'href': 'https://api.spotify.com/v1/albums/3rar7GKCodqR9GIIiNe75H',
  'id': '3rar7GKCodqR9GIIiNe75H',
  'images': [{'height': 640,
    'url': 'https://i.scdn.co/image/ba84e8818dff75f6901f951c54d39a543be6f357',
    'width': 640},
   {'height': 300,
    'url': 'https://i.scdn.co/image/557fcc38125bea3383b6521ad13bdf40ddda966e',
    'width': 300},
   {'height': 64,
    'url': 'https://i.scdn.co/image/1855bb69df2edb93431a9e7a262f37ba2ec88453',
    'width': 64}],
  'name': 'Natural',
  'release_date': '2018-07-17',
  'release_date_precision': 'day',
  'total_tracks': 1,
  'type': 'album',
  'uri': 'spotify:album:3rar7GKCodqR9GIIiNe75H'},
 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q'},
   'href': 'https://api.spotify.com/v1/artists/53XhwfbYqKCa1cC15pYq2q',
   'id': '53XhwfbYqKCa1cC15pYq2q',
   'name': 'Imagine Dragons',
   'type': 'artist',
   'uri': 'spotify:artist:53XhwfbYqKCa1cC15pYq2q'}],
 'available_markets': [],
 'disc_number': 1,
 'duration_ms': 189466,
 'explicit': False,
 'external_ids': {'isrc': 'USUM71806694'},
 'external_urls': {'spotify': 'https://open.spotify.com/track/4zIO3ilp5HvTeK3HJHxhMP'},
 'href': 'https://api.spotify.com/v1/tracks/4zIO3ilp5HvTeK3HJHxhMP',
 'id': '4zIO3ilp5HvTeK3HJHxhMP',
 'is_local': False,
 'name': 'Natural',
 'popularity': 76,
 'preview_url': None,
 'track_number': 1,
 'type': 'track',
 'uri': 'spotify:track:4zIO3ilp5HvTeK3HJHxhMP'}
 '''
SEP = '\t|\t'


def by_id(track_id):
    sp = spotipy.Spotify(auth=AUTH_TOKEN)
    track = DotMap(sp.track(track_id))
    return SEP.join([track.name, track.artists[0].name, track.album.name, track.uri])
