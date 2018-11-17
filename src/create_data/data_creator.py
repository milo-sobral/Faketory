# create dataset for source labelling
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='')

# /v2/everything
all_articles = newsapi.get_everything(sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      language='en',
                                      sort_by='relevancy')

# /v2/sources
sources = newsapi.get_sources(country='us')
