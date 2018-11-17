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

def get_data_file() :
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(current_dir, "../..", "data")
    return filename

#  Generate n grams
def generate_ngrams(text, n):
    words = text.split()
    output = []
    for i in range(len(words)-n+1):
        output.append(words[i:i+n])
    return output

def get_string(data):
    

def main():
    path = get_data_file() + "/"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    dictRel = dict(
        rel0 = [],
        rel1 = [],
        rel2 = [],
        rel3 = [],
        rel4 = [],
        rel5 = [],
        rel6 = [],
        rel7 = [],
        rel8 = [],
        rel9 = []
    )
    for file in files :
        with open(os.path.join(path, file)) as f:
            data = json.load(f)
        data = get_string(data)
        print(type(data))

if __name__ == "__main__" :
    main()
