# Estimating the reliability and bias of one article based on the features in learn.py
# TODO:
#  - Get one article
#  - Convert it to string
#  - Tokenize it (ngrams.py)
#  - calculate its rating based on the features we have
import sys
sys.path.insert(0, '../create_data')
sys.path.insert(0, '../extension')
import gen_dataset as gd
import ngrams as ng
import learn as l
import webscraper as ws
import json
import io

MAX_NGRAMS = 10

def get_string(dict):
    txt = ''
    txt += dict['id']
    txt += dict['paragraph']
    return txt

def tokenize(string) :
    text = gd.remove_noise(string)
    ngrams = ng.return_most_frequent((ng.count_ngrams(io.StringIO(text), min_length=2, max_length=7)), MAX_NGRAMS)
    return ngrams

def find_match(features, ngram) :
    for f in features :
        if f['gram'] == ngram :
            return features['factor']
    return 0

def calculate (features, ngrams) :
    sum = 0
    for ngram in ngrams :
        sum += find_match(features, ngram)
    return sum / len(ngrams)

def get_bias_score(ngrams):
    dict = gd.get_ngrams_bias(True)
    f = l.get_features(dict, 'bias')
    return calculate(f, ngrams)

def get_rel_score(ngrams):
    dict = gd.get_ngrams_rel(True)
    f = l.get_features(dict, 'rel')
    return calculate(f, ngrams)

def calc(dict):
    string = get_string(dict)
    tokens = tokenize(string)
    score_bias = get_bias_score(tokens)
    score_rel = get_rel_score(tokens)
    return [score_bias, score_rel]

if __name__ == "__main__" :
    calc()
