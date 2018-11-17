# Author :
#  - Milo Sobral
#  - Zoe Lapomme
# import re
# import nltk
# from sklearn.feature_extraction.text
# import TfidfVectorizer from sklearn.metrics
# import classification_report
# from sklearn import svm
# import ../create_data/gen_dataset as gd
import sys
sys.path.insert(0, '../create_data')
import gen_dataset as gd

def get_features_bias(dict):
    features = []
    for d in dict :
        tCount = 0
        invRel = 1/(d['bias']+1)
        

def get_features_rel() :
    return 0

def main() :
    dict = gd.get_ngrams_bias(True)
    get_features_bias(dict)
    get_features_rel()

if __name__ == "__main__" :
    main()

# Removing Noise words
# def remove_noise(input_text, noise_list):
#     words = input_text.split()
#     noise_free_words = [word for word in words if word not in noise_list]
#     noise_free_text = " ".join(noise_free_words)
#     return noise_free_text
#
# #  Removing special patterns
# def remove_regex(input_text):
#     regex_pattern = "#[\w]*"
#     urls = re.finditer(regex_pattern, input_text)
#     for i in urls:
#         input_text = re.sub(i.group().strip(), '', input_text)
#     return input_text
#
# def lemmatize() :
#     # Lemmatization and stemming
#     from nltk.stem.wordnet import WordNetLemmatizer
#     lem = WordNetLemmatizer()
#
#     from nltk.stem.porter import PorterStemmer
#     stem = PorterStemmer()
#
#     word = "multiplying"
#     lem.lemmatize(word, "v")
#
# # Remove all slang and fake words
# def lookup_words(input_text, lookup_dict):
#     words = input_text.split()
#     new_words = []
#     for word in words:
#         if word.lower() in lookup_dict:
#             word = lookup_dict[word.lower()]
#         new_words.append(word) new_text = " ".join(new_words)
#         return new_text
#
# #  Generate n grams
# def generate_ngrams(text, n):
#     words = text.split()
#     output = []
#     for i in range(len(words)-n+1):
#         output.append(words[i:i+n])
#     return output
#
# def create_dataset() :
#     # Create dataset vectors
#     training_corpus = []
#     test_corpus = [("a = 23, b = 34", '3')]
#
# # Naive bayes using SKlearn
# def train() :
#     # preparing data for SVM model (using the same training_corpus, test_corpus from naive bayes example)
#     train_data = []
#     train_labels = []
#     for row in training_corpus:
#         train_data.append(row[0])
#         train_labels.append(row[1])
#
#     test_data = []
#     test_labels = []
#     for row in test_corpus:
#         test_data.append(row[0])
#         test_labels.append(row[1])
#
#     # Create feature vectors
#     vectorizer = TfidfVectorizer(min_df=4, max_df=0.9)
#     # Train the feature vectors
#     train_vectors = vectorizer.fit_transform(train_data)
#     # Apply model on test data
#     test_vectors = vectorizer.transform(test_data)
#
#     # Perform classification with SVM, kernel=linear
#     model = svm.SVC(kernel='linear')
#     model.fit(train_vectors, train_labels)
#     prediction = model.predict(test_vectors)
