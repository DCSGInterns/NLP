'''the inputs data file and a word... attach the sentiment
call named_entity
normalize the score
count total number of times word has come
output - sentiment score and count '''

#(ei - Emin)/Emax -Emin

#steps : clean up named_entity file then work here taking data splitting each tweet and all
test_word = 'Dell'

import nltk
from named_entity import para_senti_score

key_word = test_word

#take in data file
with open("data_file.txt", 'r') as data_file:
    for line in data_file:
        if key_word in line:
            print line
            print para_senti_score(line,key_word);



#data - word relation 
#noun-verb relation 


'''
SLOW CASES : 
Dell Latitude D630 Laptop, 1.80 GHz, Intel Core 2 Duo, 2 GB, DVDRW http:\/\/t.co\/MmlZtlHnwB #notebook #laptop #netbook #computer
\u7b2c1\u4f4d18999\u5186\u4e2d\u53e4\u30d1\u30bd\u30b3\u30f3 DELL Latitude D530 \u3010 \u7121\u7ddaLAN \u3011\u3010 Celeron 540 2\n#\u30ce\u30fc\u30c8\u30d1\u30bd\u30b3\u30f3 #\u30d1\u30bd\u30b3\u30f3 #notepc #pasokon http:\/\/t.co\/Fd1NFr2uGW http:\/\/t.co\/XrDpvR1FOp
'''
