import json, os

def get_array_URL_checked () :
  arrayURL = []
  data = json.loads(open('create_data/sources.json').read())
  for source in data['sources'] :
    source_url = source['url']
    string_to_add = ""
    length = len(source_url)
    if source_url[6] == '/' :
        string_to_add = source_url[7:length]
    elif source_url[7] == '/' :
        string_to_add = source_url [8:length]
    else :
        string_to_add = source_url
    arrayURL.append(string_to_add)
  return arrayURL

def check_URL (URL_to_check, arrayURL) :
    URL_to_remember = "a"
    for url in arrayURL :
        num = URL_to_check.find(url)
        if num > -1 :
            return url
    if URL_to_remember == "a" :
        return "no_URL_found"
    else :
        return URL_to_remember

#def URLscore ()


#def main ():
arrayURL = get_array_URL_checked()
URL = check_URL ("foxnews", arrayURL)
score = 0
if URL == "no_URL_found" :
    break
else :
    score = URLscore (URL)

print (URL)
