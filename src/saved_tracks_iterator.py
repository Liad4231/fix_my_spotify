# -*- coding: utf-8 -*-
from track_info_provider import by_id
import json
from pprint import pprint
from dotmap import DotMap

TRACK_JSON = r"products\saved_tracks.json"
with open(TRACK_JSON, "r") as f:
    tracks = json.load(f)["saved"]
output_file = open(r"products\saved_tracks_info.txt", "ab")
for i, track in enumerate(tracks):
    try:
        track = DotMap(track)
        line = ""
        line += str(i)
        line += '\t|\t'
        line += by_id(track.uri)
        line += '\n'
        line = line.encode("utf8")
        print(line)
        output_file.write(line)
    except TimeoutError as timeout:
        print("Timeout exception occured, continuing...")
        by_id(track.uri)
output_file.close()