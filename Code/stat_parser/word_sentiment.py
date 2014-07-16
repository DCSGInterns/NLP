from SWNReader import *


import re
regexp_not = "(?:^(?:never|no|nothing|nowhere|noone|none|not|havent|hasnt|hadnt|cant|couldnt|shouldnt|wont|wouldnt|dont|doesnt|didnt|isnt|arent|aint)$)|n't"
regexp_clause = "[.:;!?]"

def word_senti(current_word, previous_word_inc_val):

    s = get_scores('SentiWordNet.txt',current_word)
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
            
def negation(chunked):
    
    neg_track = []


    for chunked_sent in chunked:
        neg_sent = []
        prev_word = None
        flag = 1;
        prev_inc_val = 0

        for current_word in chunked_sent:
            t = flag;
            if t==0:
                t = -1
            t = t * word_senti(current_word, prev_inc_val)
            neg_sent.append((current_word , t))
            if re.search(regexp_not, current_word): #some problem here
                flag = (flag + 1) % 2;
            prev_word = current_word
            prev_inc_val = get_inc_value(prev_word)  
        neg_track.append(neg_sent)
    #print neg_track
    return neg_track 