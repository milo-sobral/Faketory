import json, os

def get_array_URL_checked () :
  arrayURL = []
  data = json.loads(open('create_data/sources.json').read())
  for source in data['sources'] :
    #string_to_add = source['url']
    #if (source_url[6] == '/')
    arrayURL.append(source['url'])
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
URL = check_URL ("http://www.nytimes.com/", arrayURL)
print (URL)
