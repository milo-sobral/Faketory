# Authors
#  - Milo Sobral
#  - Zoe Lapomme

# create dataset for source labelling
from newsapi import NewsApiClient
import json
import os

def get_data_file() :
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(current_dir, "../..", "data2")
    return filename

def get_sources():
    with open('sources1.json') as json_data:
        d = json.load(json_data)
    array = []
    for source in d['sources']:
        array.append(source['id'])
    return array

newsapi = NewsApiClient(api_key='019c4c70f26a468cb615b451b40f6d30')

def get_urls(articles) :
    array = []
    for art in articles :
        array.append(art['url'])
    return array

def get_data(source):
    array = []
    dates = [
        ['2018-10-18', '2018-10-20'],
        ['2018-10-20', '2018-10-24'],
        ['2018-10-25', '2018-10-30'],
        ['2018-10-30', '2018-11-04'],
        ['2018-11-08', '2018-11-12'],
        ['2018-11-13', '2018-11-17']]
    for date in dates :
        articles = newsapi.get_everything(
            sources=source,
            from_param=date[0],
            to=date[1],
            language='en',
        )
        temp = get_urls(articles['articles'])
        for t in temp :
            array.append(t)
    return array

def create_json(data, source) :
    r = dict(source = source, urls = data)
    path = get_data_file()
    with open(os.path.join(path, source + '.json'), 'w') as fp:
        json.dump(r, fp)

def main() :
    sources = get_sources()
    counter = 0
    sources = sources[80:]
    for s in sources :
        array = get_data(s)
        counter += len(array)
        create_json(array, s)
    print("Total number of url's : {}".format(counter))
    # print(sources)


if __name__ == "__main__" :
    main()
