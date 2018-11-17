# Author : Milo Sobral
#  Zoe Lapomme
# Main script to check an article from an url
import sys
sys.path.insert(0, './create_data')
sys.path.insert(0, './extension')
sys.path.insert(0, './learn')
sys.path.insert(0, './spellcheck')
import webscraper as ws
# import spellcheck as sc
import calc as c
import URL_check as urlcheck


# TODO
# - Request and parse with webscraper
# - treat
# - Get URL from javascript extension
# - return score

# where to output json file

def get_url() :
    url = 'https://www.bbc.com/news/world-europe-46233560'# Get url from javascript extension
    return url


def get_json_file(url) :
    file_to_evaluate = ws.main(url)
    return file_to_evaluate

def get_spell_checker_score (file_to_evaluate) :
    spellcheck_score = sc.main(file_to_evaluate)
    return spellcheck_score

def get_scores(file) :
    return c.calc(file)

def get_URL_recognizer_score (url) :
    arr = urlcheck.main(url)
    return arr

def get_final_score (rel_score, bias_score, URL_recognizer_score) :
    #final_score = spell_check_score * weight1 + reliability_score * weight2 + bias_score * weight3 + URL_recognizer_score * weight 4
    # spell = spell * 100
    if rel_score == 0 :
        return 1000
    if URL_recognizer_score[0] == -1:
        final_score = (1/rel_score) * (bias_score)
        return final_score
    rel_score = rel_score*0.75 + URL_recognizer_score[0]*0.25
    bias_score = bias_score*0.75 + URL_recognizer_score[1]*0.25
    final_score = (1/rel_score) * (bias_score)
    return final_score
# (1/spell) *
# def output_score_to_extension (score) :
    #output score to extension


def calc() :
    url = get_url()
    file_to_evaluate = get_json_file(url)
    # spell = get_spell_checker_score(file_to_evaluate)
    array = get_scores(file_to_evaluate)
    bias_score = array[0]
    rel_score = array[1]
    url_score = get_URL_recognizer_score(url)
    final = get_final_score(rel_score, bias_score, url_score)
    print(final)
    return final

if __name__ == "__main__" :
    calc()
