import json, os

def get_array_URL_checked () :
  arrayURL = []
  data = json.loads(open('create_data/sources.json').read())
  for source in data['sources'] :
    arrayURL.append(source['url'])
  return arrayURL

arrayURL = get_array_URL_checked()
print (arrayURL)
