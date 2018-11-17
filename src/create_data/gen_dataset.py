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
import io
import os
import json
from os import listdir
from os.path import isfile, join
import data_labeler as dl
import ngrams as ng

MAX_NGRAMS = 10

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

noise_list = ['headlines', 'todays', 'ap', 'email', 'subscribe', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def remove_noise(input_text):
    input_text = input_text.lower()
    words = input_text.split()
    noise_free_words = [word for word in words if word not in noise_list]
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text

def get_ngrams_rel(filter):
    path = get_data_file() + "/"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    listRel = [
        dict(string = '', ngrams = [], rel = 0),
        dict(string = '', ngrams = [], rel = 1),
        dict(string = '', ngrams = [], rel = 2),
        dict(string = '', ngrams = [], rel = 3),
        dict(string = '', ngrams = [], rel = 4),
        dict(string = '', ngrams = [], rel = 5),
        dict(string = '', ngrams = [], rel = 6),
        dict(string = '', ngrams = [], rel = 7),
        dict(string = '', ngrams = [], rel = 8),
        dict(string = '', ngrams = [], rel = 9)
    ]
    dictRel = dl.getReliability(files)
    for file in files :
        with open(os.path.join(path, file)) as f:
            data = json.load(f)
        data = get_string(data)
        if filter :
            data = remove_noise(data)
        rel = dictRel[file]
        listRel[rel]['string'] += data
    for d in listRel :
        d['ngrams'] = ng.return_most_frequent((ng.count_ngrams(io.StringIO(d['string']), min_length=2, max_length=7)), MAX_NGRAMS)

    if "string" in listRel:
        del listRel["string"]

    return listRel

def get_ngrams_bias(filter) :
    path = get_data_file() + "/"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    listBias = [
        dict(string = '', ngrams = [], bias = 0),
        dict(string = '', ngrams = [], bias = 1),
        dict(string = '', ngrams = [], bias = 2),
        dict(string = '', ngrams = [], bias = 3),
        dict(string = '', ngrams = [], bias = 4),
    ]
    dictBias = dl.getBias(files)
    for file in files :
        with open(os.path.join(path, file)) as f:
            data = json.load(f)
        data = get_string(data)
        if filter :
            data = remove_noise(data)
        bias = dictBias[file]
        if bias == 0:
            continue
        listBias[bias]['string'] += data
    for d in listBias :
        d['ngrams'] = ng.return_most_frequent((ng.count_ngrams(io.StringIO(d['string']), min_length=2, max_length=7)), MAX_NGRAMS)

    if "string" in listBias:
        del listBias["string"]

    return listBias

def main() :
    rel = get_ngrams_rel(True)
    bias = get_ngrams_bias(True)
    print(rel)
    print(bias)

if __name__ == "__main__" :
    main()
