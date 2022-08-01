import requests
import json

searchTerm = 'gremio'
startIndex = '1'
key = ''
cx = ''
searchUrl = "https://www.googleapis.com/customsearch/v1?q=" + \
            searchTerm + "&start=" + startIndex + "&key=" + key + "&cx=" + cx + \
            "&searchType=image"
r = requests.get(searchUrl)
response = r.content.decode('utf-8')
result = json.loads(response)
print(searchUrl)
print(r)
print(result)