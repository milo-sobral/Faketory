import json
import os
import requests

# https://newsapi.org/v2/everything?sources=abc-news&apiKey=279f7ab6ee464ec38f52a95f14f79c5d



url = ('https://newsapi.org/v2/everything?sources=abc-news-au&apiKey=e74ca84a910749b08b7e34aca0e12ee3')
response = requests.get(url)
print(len(response.json()['articles']))
