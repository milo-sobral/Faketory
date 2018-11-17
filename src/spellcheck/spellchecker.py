# Author : Milo Sobral
# spell checker for an article
from spellchecker import SpellChecker

spell = SpellChecker()
# get the words from json file
# split them in a list
# get the number of them that are misspelled
#get the total nomber of words
def get_words_from_json(json):
    words = json['paragraph']
    words = words.split(' ')
    return words

def main (json) :
    words = get_words_from_json(json)
    a_length = len(words)
    m_lentgh = spell.unknown(words)
    return int((a_length / m_length) * 100)

if __name__ == '__main__' :
    main()
