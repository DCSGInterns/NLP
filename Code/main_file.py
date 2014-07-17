#import datetime
#a = datetime.datetime.now()

'''the inputs data file and a word... attach the sentiment
call named_entity
normalize the score
count total number of times word has come
output - sentiment score and count 
'''
#(ei - Emin)/Emax -Emin

test_word = 'Dell'

import nltk
from named_entity import para_senti_score
'''
import json

key_word = test_word
Smax = 0
Smin = 10000000

#take in data file
with open("data_file.txt", 'r') as data_file:
    for line in data_file:
        line_encoded = json.loads(line)
        #print line_encoded
        data = line_encoded['text']
        if key_word in data:
            print data
            print para_senti_score(data,key_word);

#b = datetime.datetime.now()
#c = b-a
#print c
'''

def custom_SA(key_word,tokenized_sentence):
	t = para_senti_score(tokenized_sentence,key_word)
	#print t
	return t
#custom_SA('Dell', 'Dell is very BAD');
