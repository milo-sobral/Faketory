# Authors
#  - Milo Sobral
#  - Zoe Lapomme

# create dataset for source labelling
from newsapi import NewsApiClient
import json
import os

def get_data_file() :
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(current_dir, "../..", "data")
    return filename

def get_sources(c) :
    newsapi = NewsApiClient(api_key='e74ca84a910749b08b7e34aca0e12ee3')
    sources = newsapi.get_sources(country = c)
    sources = sources['sources']
    for s in sources :
        aSources.append(s)

def get_data(c) :
    # Init
    newsapi = NewsApiClient(api_key='e74ca84a910749b08b7e34aca0e12ee3')
    # /v2/sources
    sources = newsapi.get_sources(country = c)
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
        jsonSource = newsapi.get_everything(sources = s)
        articles = jsonSource['articles']
        url = dataPath + "/"+ s + '.json'
        with open(url, 'w') as outfile:
            json.dump(jsonSource, outfile)

aSources = []

def main() :
    countries = ['us', 'au', 'ca', 'nz', 'gb']
    for c in countries :
        print("getting data for country : ".format(c))
        # get_data(c)
        get_sources(c)
    return dict(sources = aSources)


if __name__ == "__main__" :
    main()
