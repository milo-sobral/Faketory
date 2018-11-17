import json

def get_array_URL_checked () :
  arrayURL = []
  for source in create_data/sources :
    arrayURL.append(source['url'])
  return arrayURL

arrayURLS = get_array_URL_checked
print (arrayURLS)
