#'Google has better customer service than Dell' -> how to do negation of sentiment

#input to this is sentence in which that word to find is there
#output - overall sentiment to that sentence


#problem now - latitude has a sentiment - give 0 sentiments to dell products ..

from SWNReader import *

def sentiment_finding(noun , adjective, verb):
        #print adjective
        score = 0
        for part in adjective:
                #print part
                if type(part) is list:
                        t = get_scores('SentiWordNet.txt',part[1])
                        part = [part[0], part[1], t]
                        #print part
                        score = score + t;
        for part in verb:
                #print part
                if (type(part) is list and len(part) != 3) :
                        t = get_scores('SentiWordNet.txt',part[1])
                        part = [part[0], part[1], t]
                        #print part
                        score = score + t;
        return score
