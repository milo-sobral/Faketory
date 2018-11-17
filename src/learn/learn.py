# Author :
#  - Milo Sobral
#  - Zoe Lapomme

import sys
sys.path.insert(0, '../create_data')
import gen_dataset as gd

def is_in_features(ngram, features):
    counter = 0
    if not features :
        return -1
    for f in features :
        # print()
        if f['gram'] == ngram :
            return counter
    return -1


def get_features(listF, type):
    features = []
    for d in listF :
        invRel = 1/(d[type]+1)
        # print(len(d['ngrams']))
        for ngram in d['ngrams'] :
            index = is_in_features(ngram, features)
            if index > -1 :
                count = features[index]['countSoFar']
                factor = features[index]['factor']
                features[index]['countSoFar'] += ngram[1]
                features[index]['factor'] += ngram[1] * invRel
            else :
                features.append(dict(
                    n = len(ngram[0]),
                    gram = ngram[0],
                    countSoFar = ngram[1],
                    factor = invRel * ngram[1]
                ))
    for f in features :
        total = f['countSoFar']
        fact = f['factor']
        f['factor'] = fact / total
    return features

def train() :
    dict1 = gd.get_ngrams_bias(True)
    f1 = get_features(dict1, 'bias')
    dict2 = gd.get_ngrams_rel(True)
    f2 = get_features(dict2, 'rel')
    print(len(f2))
    return f1, f2

if __name__ == "__main__" :
    train()
