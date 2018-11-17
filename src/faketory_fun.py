# Author : Milo Sobral
# Main script to check an article from an url
from extension/webscraper import . as ws
import extension/webscraper as webscraper
import spellcheck/spellchecker as spellcheck
import


# TODO
# - Get URL from javascript extension
# - Request and parse with webscraper
# - treat
# - return score

# where to output json file

def get_url() :
    url = # Get url from javascript extension
    return url


def get_json_file(url) :
    file_to_evaluate = webscraper.main(url)
    return file_to_evaluate


def get_spell_checker_score (file_to_evaluate) :
    spellcheck_score = spellcheck.main(file_to_evaluate)
    return spellcheck_score


def get_reliability_score (file_to_evaluate) :
    #reliability_score =
    return reliability_score


def get_bias_score (file_to_evaluate) :
    #bias_score =
    return bias_score


def get_URL_recognizer_score (file_to_evaluate) :
    #URL_recognizer_score =
    return URL_recognizer_score


def get_final_score (spell_check_score, reliability_score, bias_score, URL_recognizer_score) :
    #final_score = spell_check_score * weight1 + reliability_score * weight2 + bias_score * weight3 + URL_recognizer_score * weight 4
    return final_score


def output_score_to_extension (score) :
    #output score to extension 


def main () :
    file_to_evaluate = get_json_file(get_url())
    #make model with words
    #evaluate the json file that we are testing
    score = get_final_score (get_spell_check_score(file_to_evaluate), get_reliability_score(file_to_evaluate), get_bias_score(file_to_evaluate), get_URL_recognizer_score(file_to_evaluate))
    #output score
    output_score_to_extension(score)
