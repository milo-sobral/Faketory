# create dataset for source labelling
from newsapi import NewsApiClient
import json
import os

def get_data_file() :
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(current_dir, "../..", "data")
    return filename

def get_data() :
    # Init
    newsapi = NewsApiClient(api_key='279f7ab6ee464ec38f52a95f14f79c5d')

    # /v2/sources
    sources = newsapi.get_sources(country='us')

    sources = sources['sources']
    arraySources = []
    arrayURL = []
    for source in sources :
        arraySources.append(source['id'])
        arrayURL.append(source['url'])
    dataPath = get_data_file()
    counter = 0
    for s in arraySources :
        print("Getting articles for source : {}".format(counter))
        counter += 1
        jsonSource = newsapi.get_everything(sources = s, sort_by = 'relevancy')
        url = dataPath + "/"+ s + '.json'
        with open(url, 'w') as outfile:
            json.dump(jsonSource, outfile)

get_data()
