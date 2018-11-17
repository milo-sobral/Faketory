#  Generate a dataset
#  Authors
#  - Milo Sobral
#  - Zoe Lapomme

#  TODO
#  - for each json file in data
#  - get reliability
#  - take all text and concatenate into one string
#  - Remove capitalization, punctuation...
#  - tokenize
#  - count tokens
#  - output dict with each word

import os
import json
from os import listdir
from os.path import isfile, join
import data_labeler as dl
import ngrams as ng

def get_data_file() :
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(current_dir, "../..", "data")
    return filename

def get_string(data):
    data = data['articles']
    txt = ""
    for art in data :
        try :
            txt += art['title']
            txt += art['description']
            txt += art['content']
        except :
            continue
    return txt

def main():
    path = get_data_file() + "/"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    listRel = [
        dict(string = '', ngrams = dict(), rel = 0),
        dict(string = '', ngrams = dict(), rel = 1),
        dict(string = '', ngrams = dict(), rel = 2),
        dict(string = '', ngrams = dict(), rel = 3),
        dict(string = '', ngrams = dict(), rel = 4),
        dict(string = '', ngrams = dict(), rel = 5),
        dict(string = '', ngrams = dict(), rel = 6),
        dict(string = '', ngrams = dict(), rel = 7),
        dict(string = '', ngrams = dict(), rel = 8),
        dict(string = '', ngrams = dict(), rel = 9)
    ]
    dictRel = dl.getReliability(files)
    for file in files :
        with open(os.path.join(path, file)) as f:
            data = json.load(f)
        data = get_string(data)
        rel = dictRel[file]
        listRel[rel]['string'] += data
    for d in listRel :
        d['ngrams'] = ng.count_ngrams(d['string'], min_length=2, max_length=5)
        array = ng.return_most_frequent(d['ngrams'], 10)


if __name__ == "__main__" :
    main()
