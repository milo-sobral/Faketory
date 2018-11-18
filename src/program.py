# Author : Milo Sobral
#  Zoe Lapomme
# Main script to check an article from an url
import sys
sys.path.insert(0, './create_data')
sys.path.insert(0, './extension')
sys.path.insert(0, './learn')
sys.path.insert(0, './spellcheck')
sys.path.insert(0, './to_send')
import webscraper as ws
# import spellcheck as sc
import calc_f as c
#import URL_check as urlcheck

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
#    spellcheck_score = urlcheck.main(file_to_evaluate)
    return 0.01
    #spellcheck_score

def get_scores(file) :
    return c.calc(file)

#def get_URL_recognizer_score (url) :
#    arr = urlcheck.main(url)
#    return arr

# def get_final_score (rel_score, bias_score, URL_recognizer_score) :
#     #final_score = spell_check_score * weight1 + reliability_score * weight2 + bias_score * weight3 + URL_recognizer_score * weight 4
#     # spell = spell * 100
#     if rel_score == 0 :
#         return 1000
#     if URL_recognizer_score[0] == -1:
#         final_score = (1/rel_score) * (bias_score)
#         return final_score
#     rel_score = rel_score*0.75 + URL_recognizer_score[0]*0.25
#     bias_score = bias_score*0.75 + URL_recognizer_score[1]*0.25
#     final_score = (1/rel_score) * (bias_score)
#     return final_score
# (1/spell) *
# def output_score_to_extension (score) :
    #output score to extension


def get_final_score (spell_check_score, reliability_score, bias_score):
    #URL_recognizer_score
    #if URL_recognizer_score[0] == -1 :
    final_score = (spell_check_score*100)**(0.4) * (10 - reliability_score)**(0.3) * (bias_score * 2.5)**(0.3)
    #else :
    #    final_score =(spell_check_score * 100)^(0.4) * ((10 - reliability_score)*0.7+(10 - URL_recognizer_score[0])*0.3)^(0.3) * ((bias_score * 2.5) * 0.7 + (URL_recognizer_score[1] * 2.5) * 0.3)^(0.3)
    return final_score

#in main
#final_score = get_final_score (get_spell_check_score(file_to_evaluate), get_reliability_score(file_to_evaluate), get_bias_score(file_to_evaluate), get_URL_recognizer_score(file_to_evaluate))
#final_score = get_final_score (0.1, 6, 4, ([-1],[-1])
##if final_score >= 8 :
#    score_evaluation= "not a reliable source"
#elif final_score > 5 :
#    score_evaluation= "probably not a reliable source"
#elif final_score >= 2 :
#    score_evaluation= "probably a reliable souce"
#else :
#    score_evaluation = "reliable source"
#return final_score or score_evaluation
#print (final_score)
#print (score_evaluation)


def calc(url) :
    #url = get_url()
    file_to_evaluate = get_json_file(url)
    spell = get_spell_checker_score(file_to_evaluate)
    array = get_scores(file_to_evaluate)
    bias_score = array[0]
    rel_score = array[1]
    print(array[0])
    print(array[1])
    #url_score = get_URL_recognizer_score(url)
    final = get_final_score(spell, rel_score, bias_score) #url_score
    return final

print(calc("https://www.usnews.com/news/politics/articles/2018-11-17/house-in-part-of-major-realignment-in-southern-california"))

#if __name__ == "__main__" :
#    calc()
