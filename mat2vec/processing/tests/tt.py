# importing the requests library
import requests
import json

# api-endpoint
URL = "https://api.elsevier.com/content/search/scopus"

# location given here
query = "retina"
api = "65d692e390d6d327fe0d0406d30257f7"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'query': query,
          'apiKey': api,
          'view': "COMPLETE",
          'cursor': '*',
          'count': 25}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)
data = r.json()
print(json.dumps(data, indent=4))