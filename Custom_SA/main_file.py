
from named_entity import para_senti_score

def custom_SA(key_word,sentence):
	''' Find the sentiment of input sentence. Output is the sentiment rounded upto 3 decimal places'''
	t = para_senti_score(sentence,key_word)
	if t!= None :
		t = round(t, 3)
	return t

user_input1 = raw_input("Sentence: ")
user_input2 = raw_input("keyword: ")

print custom_SA(user_input2, user_input1)