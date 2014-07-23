from SWNReader import *
from nltk.corpus import stopwords
stopset = set(stopwords.words('english'))

import re

regexp_clause = "[.:;!?]"

def get_text_lexicon(current_word, tag, previous_word_inc_val):
    s = get_scores('SentiWordNet.txt',current_word, tag)
    t = previous_word_inc_val
    if t != 0:
        s = t*s
    if current_word.isupper():
        s = s*2   
    return s 



def get_inc_value(word):
    f = open('Incremetors.txt')
    for line in f:
        cols = split_line(line)
        if word == cols[0]:
            #print word
            #Sprint cols[1]
            return float(cols[1])
        else:
            return 0

def get_tag(pos_tag):
    regexp_noun = r'NN(S|P|PS)?|PRP\$?'
    if re.match(regexp_noun, pos_tag):
        return 'n'
    
    regexp_verb = r'VB(D|G|N|P|Z)?'
    if re.match(regexp_verb, pos_tag):
        return 'v'

    regexp_adj = r'JJ(R|S)?'
    if re.match(regexp_adj,pos_tag):
        return 'a'

    regexp_adverb = r'RB(R|S)?'
    if re.match(regexp_adverb, pos_tag):
        return 'r'               

    if pos_tag == 'FW':
        return 'FW'

def negation(chunked):
    regexp_not = "(?:^(?:never|no|nothing|nowhere|noone|none|not|havent|hasnt|hadnt|cant|couldnt|shouldnt|wont|wouldnt|dont|doesnt|didnt|isnt|arent|aint)$)|n't"
    

    neg_sent = []
    prev_word = None
    flag = 1;
    prev_inc_val = 0
    text_count = 0

    for current_word_tuple in chunked:
        current_word = current_word_tuple[0]
        current_word_tag = current_word_tuple[1]
        current_word_tag = get_tag(current_word_tag)

        global stopset
        if current_word not in stopset:   
            t = flag;
            if t==0:
                t = -1 
            t = t * get_text_lexicon(current_word, current_word_tag, prev_inc_val)
            if t != 0:
                text_count += 1
        else:
            t = 0
        neg_sent.append((current_word , t))
        if re.search(regexp_not, current_word): 
            flag = (flag + 1) % 2;
        prev_word = current_word
        prev_inc_val = get_inc_value(prev_word)  
    
    #print neg_sent
    return [neg_sent, text_count] 

