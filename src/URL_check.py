import json, os
import sys
sys.path.insert(0,'./create_data')
import data_labeler as data_labeler
import os
from os import listdir
from os.path import isfile, join

def get_array_URL_to_compare () :
  arrayURL = []
  data = json.loads(open('create_data/sources1.json').read())
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


def get_array_URL_complete ():
    arrayURL = []
    data = json.loads(open('create_data/sources1.json').read())
    for source in data['sources'] :
        arrayURL.append (source['url'])
    return arrayURL


def check_URL (URL_to_check, arrayURL) :
    i = -1
    for url in arrayURL :
        i += 1
        num = URL_to_check.find(url)
        if num > -1 :
            return i
    return -1


def URLscore (posURL, arrayURL) :
    URLname = arrayURL[posURL]
    name_file_score = ""
    name_file_score_complete = ""
    data = json.loads(open('create_data/sources1.json').read())
    for source in data['sources'] :
        if source['url'] == URLname :
            name_file_score = source['id']
            name_file_score_complete = name_file_score + ".json"
            break
    mypath = data_labeler.get_data_file()
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    #getting the dictionary with all the sources and their reliability and bias scores
    dicReliability = data_labeler.getReliability(files)
    dicBias = data_labeler.getBias(files)

    #first entry of the score array is the reliability score and the second is the bias score
    scoresArray = [-1,-1]
    scoresArray[0] = dicReliability[name_file_score_complete]
    scoresArray[1] = dicBias [name_file_score_complete]

    return scoresArray




#def main ():
arrayURL_comparison = get_array_URL_to_compare()
arrayURL_complete = get_array_URL_complete()
posURL = check_URL ("https://www.foxnews.com/politics/trump-on-cnns-jim-acosta-if-he-misbehaves-well-throw-him-out", arrayURL_comparison)
score = []
if posURL == -1 :
    #return [-1,-1]
    print (-1)
else :
    score = URLscore (posURL, arrayURL_complete)
    #return scoreArray
    print (score)
