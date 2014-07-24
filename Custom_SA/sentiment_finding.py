#summing everything up 
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

# Normalization is done using purity - http://www.ryanmcd.com/papers/local_service_summ.pdf

def sentiment_finding(text_count):
        raw_score = 0
        absolute_score = 0 
        
        for part in senti_array:
                raw_score = raw_score + part[1]
                absolute_score = absolute_score + abs(part[1])
        
        if absolute_score != 0 :
                purity = raw_score / absolute_score

        if raw_score > 1 :
                return 1                
        #print purity        
        return raw_score