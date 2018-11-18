# Sklearn script using naive bayes
from sklearn.feature_extraction.text import CountVectorizer
import json
import os
import sys
sys.path.insert(0, '../create_data')
sys.path.insert(0, '../extension')
import data_labeler as dl
from os import listdir
import ngrams as ng
from nltk import ngrams
from collections import Counter

def tokenize_string(text) :
    text = text.lower()
    text = text.split()
    text = remove_noise(text)
    ngram_counts = Counter(ngrams(text,7))
    return (ngram_counts.most_common(200))

def get_data_file() :
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(current_dir, "../..", "data3")
    return filename

def create_count_vectorizer(string):
    string = [string]
    count_vect = CountVectorizer(ngram_range = (4, 4))
    count_vect.fit(string)
    return count_vect

def get_text(dir) :
    text = ''
    files = [f for f in listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    for f in files :
        path = os.path.join(get_data_file(), dir, f)
        with open(path) as json_data:
            d = json.load(json_data)
        text += d['id']
        text += d['paragraph']
    return text

def get_data():
    lib_path = get_data_file()
    onlydirs = [x[0] for x in os.walk(lib_path)]
    file_array = []
    for file in onlydirs :
        file_array.append(file + '.json')
    file_array2 = [os.path.basename(x) for x in file_array]
    fileRel = dl.getReliability(file_array2)
    fileBias = dl.getBias(file_array2)
    stringsRel = ['', '', '', '', '', '', '', '', '', '']
    stringsBias = ['', '', '', '', '']
    onlydirs = onlydirs[1:]
    for i in range(0, 9) :
        for dir in onlydirs :
            if fileRel[os.path.basename(dir) + '.json'] == i :
                stringsRel[i] += get_text(dir)
    for i in range(0, 4) :
        for dir in onlydirs :
            if fileBias[os.path.basename(dir) + '.json'] == i :
                stringsBias[i] += get_text(dir)
    return stringsRel, stringsBias

noise_list = ['headlines', 'todays', 'ap', 'email', 'subscribe', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def remove_noise(input_text):
    noise_free_words = [word for word in input_text if word not in noise_list]
    return noise_free_words

def main() :
    dataRel, dataBias = get_data()
    # vectorsRel = [create_count_vectorizer(x) for x in dataRel if x != '']
    # vectorsBias = [create_count_vectorizer(x) for x in dataBias if x != '']
    vectorsRel = [tokenize_string(x) for x in dataRel]
    vectorsBias = [tokenize_string(x) for x in dataBias]
    d = dict(
        vectorsRel = vectorsRel,
        vectorsBias = vectorsBias
    )
    output_json(d)

# puts the dictionnary in a json file and create a file
def output_json(d):
    j = json.dumps(d)
    with open('features.json', 'w') as fp:
        json.dump(d, fp)

main()
