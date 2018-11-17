# Author :
#  - Milo Sobral
#  - Zoe Lapomme
import re
import nltk
from sklearn.feature_extraction.text
import TfidfVectorizer from sklearn.metrics
import classification_report
from sklearn import svm

# Removing Noise words
def remove_noise(input_text, noise_list):
    words = input_text.split()
    noise_free_words = [word for word in words if word not in noise_list]
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text

#  Removing special patterns
def remove_regex(input_text):
    regex_pattern = "#[\w]*"
    urls = re.finditer(regex_pattern, input_text)
    for i in urls:
        input_text = re.sub(i.group().strip(), '', input_text)
    return input_text

def lemmatize() :
    # Lemmatization and stemming
    from nltk.stem.wordnet import WordNetLemmatizer
    lem = WordNetLemmatizer()

    from nltk.stem.porter import PorterStemmer
    stem = PorterStemmer()

    word = "multiplying"
    lem.lemmatize(word, "v")

# Remove all slang and fake words
def lookup_words(input_text, lookup_dict):
    words = input_text.split()
    new_words = []
    for word in words:
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]
        new_words.append(word) new_text = " ".join(new_words)
        return new_text

#  Generate n grams
def generate_ngrams(text, n):
    words = text.split()
    output = []
    for i in range(len(words)-n+1):
        output.append(words[i:i+n])
    return output

def create_dataset() :
    # Create dataset vectors
    training_corpus = []
    test_corpus = [("a = 23, b = 34", '3')]

# Naive bayes using SKlearn
def train() :
    # preparing data for SVM model (using the same training_corpus, test_corpus from naive bayes example)
    train_data = []
    train_labels = []
    for row in training_corpus:
        train_data.append(row[0])
        train_labels.append(row[1])

    test_data = []
    test_labels = []
    for row in test_corpus:
        test_data.append(row[0])
        test_labels.append(row[1])

    # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=4, max_df=0.9)
    # Train the feature vectors
    train_vectors = vectorizer.fit_transform(train_data)
    # Apply model on test data
    test_vectors = vectorizer.transform(test_data)

    # Perform classification with SVM, kernel=linear
    model = svm.SVC(kernel='linear')
    model.fit(train_vectors, train_labels)
    prediction = model.predict(test_vectors)


def main() :
    noise_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    # lookup_dict = {'rt':'Retweet', 'dm':'direct message', "awsm" : "awesome", "luv" :"love", "..."}

if __name__ == "__main__" :
    main()
