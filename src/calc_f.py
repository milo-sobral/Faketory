# Calc all words

# import sys
# sys.path.insert(0, './learn')
import learner as l

source = 'features.json'
with open(source) as json_data:
    d = json.load(json_data)
ngrams_rel = d['vectorsRel']
ngrams_bias = d['vectorsBias']

def find_reliability(sent_article) :
    ngrams = l.tokenize_string(sent_article)
    counter0 = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    counter6 = 0
    counter7 = 0
    counter8 = 0
    counter9 = 0
    for i in ngrams :
        for j in ngrams_rel[0] :
            if j == i :
                counter0 += ngrams_rel0[j][1]
        for j in ngrams_rel[1] :
            if j == i :
                counter1 += ngrams_rel1[j][1]
        for j in ngrams_rel[2] :
            if j == i :
                counter2 += ngrams_rel2[j][1]
        for j in ngrams_rel[3] :
            if j == i :
                counter3 += ngrams_rel3[j][1]
        for j in ngrams_rel[4] :
            if j == i :
                counter4 += ngrams_rel4[j][1]
        for j in ngrams_rel[5] :
            if j == i :
                counter5 += ngrams_rel5[j][1]
        for j in ngrams_rel[6] :
            if j == i :
                counter6 += ngrams_rel6[j][1]
        for j in ngrams_rel[7] :
            if j == i :
                counter7 += ngrams_rel7[j][1]
        for j in ngrams_rel[8] :
            if j == i :
                counter8 += ngrams_rel8[j][1]
        for j in ngrams_rel[9] :
            if j == i :
                counter9 += ngrams_rel9[j][1]
    sum_recurrence = counter0 + counter1 + counter2 + counter3 + counter4 + counter5 + counter6 + counter7 + counter8 + counter9
    reliability = (counter1 + counter2 * 2 + counter3 * 3 + counter4 * 4 + counter5 * 5 + counter6 * 6 + counter7 * 7 + counter8 * 8 + counter9 * 9)/sum_recurrence
    return reliability

def find_bias (sent_article) :
    ngrams = tokenize(sent_article)
    counter0 = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    for i in ngrams :
        for j in ngrams_bias[0] :
            if j == i :
                counter0 += ngrams_bias0[j][1]
        for j in ngrams_bias[1] :
            if j == i :
                counter1 += ngrams_bias1[j][1]
        for j in ngrams_bias[2] :
            if j == i :
                counter2 += ngrams_bias2[j][1]
        for j in ngrams_bias[3] :
            if j == i :
                counter3 += ngrams_bias3[j][1]
        for j in ngrams_bias[4] :
            if j == i :
                counter4 += ngrams_bias4[j][1]
    sum_recurrence = counter0 + counter1 + counter2 + counter3 + counter4
    bias = (counter1 + counter2 * 2 + counter3 * 3 + counter4 * 4) / sum_recurrence
    return bias
