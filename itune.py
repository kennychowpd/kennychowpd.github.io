import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&attribute=allArtistTerm&limit=50&term=" + sys.argv[1])
print(response)

print(json.dumps(response.json(), indent=2))

this_json = response.json()
for result in this_json["results"]:
    print(result["trackName"])