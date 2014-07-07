'''the inputs are two files, word file and data file... attach the sentiment
call named_entity
normalize the score
count total number of times word has come
output - sentiment score and count '''

#steps : clean up named_entity file then work here taking data splitting each tweet and all
test_sentence = '''Dell does not have BEST customer service. I liked a @YouTube video http:\/\/t.co\/byGg9a0yTu Dell latitude e6500 review.'''

import nltk

from named_entity import para_senti_score

print para_senti_score(test_sentence);


