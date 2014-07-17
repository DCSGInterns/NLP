#'Google has better customer service than Dell' -> how to do negation of sentiment

#input to this is sentence in which that word to find is there
#output - overall sentiment to that sentence


#problem now - latitude has a sentiment - give 0 sentiments to dell products ..

#from SWNReader import *

senti_array = []

def get_array(value_array):
        global senti_array
        senti_array = value_array


def get_value(word):
        #print word
        for sent in senti_array:
                for value in sent:
                        if (word == value[0]):
                                return value[1]

'''
def sentiment_finding(noun , adjective, verb):
        #print adjective
        score = 0
        
        for part in adjective:
                if type(part) is list and len(part) == 2:
                        t = get_value(part[1])
                        part = [part[0], part[1], t] 
                        score = score + t;

        for part in noun:
                #print part
                if (type(part) is list and len(part) != 3) :
                        t = get_scores('SentiWordNet.txt',part[1])
                        flag = get_value(part[1])
                        t=t*flag
                        part = [part[0], part[1], t]
                        #print part
                        score = score + t;

        for part in verb:
                #print part
                if (type(part) is list and len(part) != 3) :
                        t = get_scores('SentiWordNet.txt',part[1])
                        flag = get_value(part[1])
                        t=t*flag
                        part = [part[0], part[1], t]
                        #print part
                        score = score + t;
        
        #print senti_array
        for sent in senti_array:
                for part in sent:
                        score = score + part[1]
                        #print score

        return score
'''

def sentiment_finding():
        score = 0
        for sent in senti_array:
                for part in sent:
                        score = score + part[1]
                        #print score

        return score

        
