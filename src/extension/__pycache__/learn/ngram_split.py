import ngrams as ng
from nltk import ngrams
from collections import Counter



def tokenize_string(text) :
    text = text.lower()
    text = text.split()
    ngram_counts = Counter(ngrams(text,4))
    print (ngram_counts.most_common(10))

tokenize_string("hello my name is zoe and  this is the project we are working on")
