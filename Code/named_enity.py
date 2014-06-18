import nltk

test_sentence = ''' The idea is to find out all the ways in
which our sentence not tokenizer wouldn't fail -
1. Hey!!!, What are you doing??
2. THIS IS PRIVATE PROPERTY. HANDS OFFF!!!!!
3. I don't know WHAT your problem is???
4. Come on, COME ON
4. Phone No : +91-94465-00359, 0484-2203982.
5. Emoticons : :) :( :P.
6. Ellipssis : .......
7. Leinghter Text : SHHHHIITIIIIIITTTTTT!!!!!!''' 

chunked = [];

#Tokenizing , Tagging and Parsing 
from stat_parser import Parser
parser = Parser()
print parser.parse(test_sentence)


#introducing the sentiment - #have to make changes
#negation
'''
regexp_not = "(?:^(?:never|no|nothing|nowhere|noone|none|not|havent|hasnt|hadnt|cant|couldnt|shouldnt|wont|wouldnt|dont|doesnt|didnt|isnt|arent|aint)$)|n't"
regexp_clause = "^[.:;!?]$"

import re

for chunked_sent in chunked:
    for chunk in chunked_sent:
        flag = 1;
        count = 0;
        for word in chunk :
            print word
            chunk[count] = word + (1,);     
            if re.search(regexp_not, word[0]):
                flag = (flag + 1) % 2;
            if flag == 0:
                chunk[count] = (word[0], word[1]) + (flag,);
            count+=1;   
        #print chunk[count - 1]
        
print chunked   

#from pprint import pprint
#pprint(chunked)
'''
         
#output - array  - <(extracting NP) , (adjectives)>

