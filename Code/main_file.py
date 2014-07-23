

import nltk
from named_entity import para_senti_score

def custom_SA(key_word,sentence):
    ''' Find the sentiment of input sentence. Output is the sentiment rounded upto 3 decimal places'''

	t = para_senti_score(sentence,key_word)
	t = round(t, 3)
	return t

#print custom_SA('Dell', "I got a promotion.");
