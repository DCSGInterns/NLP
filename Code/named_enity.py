'''NOTE: All these manage sentences ..We have to manage clauses and this is highly non-optimized ..
Tagging does not work properly ...Tokenizer  -> make clauses and phrases in seperate arrays ''' 
import nltk

test_sentence = '''Sibi Malayil, whose movies although good, is a horrible person.''' 


#Tokenizing , Tagging and Parsing 
from stat_parser import Parser
parser = Parser()
chunked = parser.parse(test_sentence)
#print chunked

'''for chunk in chunked:
    #print chunk '''
'''
#introducing the sentiment and priority - #have to make changes
#negation - not working  

regexp_not = "(?:^(?:never|no|nothing|nowhere|noone|none|not|havent|hasnt|hadnt|cant|couldnt|shouldnt|wont|wouldnt|dont|doesnt|didnt|isnt|arent|aint)$)|n't"
regexp_clause = "^[.:;!?]$"

import re

for chunked_sent in chunked:
    for chunk in chunked_sent:
        flag = 1;
        
        chunk = (chunk[0], 1);
        word = chunk[0]
        if re.search(regexp_not, word):
            flag = (flag + 1) % 2;
        chunk = chunk + (flag,);
               
        print chunk
        
print chunked   
'''
        
#output - array  - <(extracting NP) , (adjectives)>
#Trying to make a list of matching words ... Pretty lame function -> have to try improving it using regular expression
def match(pattern , tree):
    word = str(tree[0])
    #print word
    if(pattern == 'NOUN'):
        if(word == 'NP' or word[0:2] == 'NN' or word == 'PP' or word == 'PP$' or word == 'PRP'):
            return 1
        else:
            if(word == 'NP+NNP' or word == 'NP+NNS' or word == 'NP+NNPS'):
                return 1
            else:
                return 0
    if(pattern == 'ADJ'):
        if(word == 'ADJP' or word == 'JJ' or word == 'JJR' or word == 'JJS'):
            return 1
        else:
            if(word == 'ADJP+JJ' or word == 'ADJP+JJS' or word == 'ADJP+JJR'):
                return 1
            else:
                return 0
    if(pattern == 'VERB'):
        if(word[0:2] == 'VB'):
                return 1
    else:
        return 0                
    
import re


def dfs(tree, check, avoid_list):
    global t;
    
    #print avoid_list
    if(tree in avoid_list):
        return 0;
    else:
        #print tree[0]
        #print check
        if (match(check, tree) == 1):
            
        #if(tree[0] == check):
            t=tree;
            return t ;
        if(len(tree) == 1):
            return t;       
        for value in tree:
            if(t == -1):
                dfs(value, check, avoid_list);
            else:
                break   
        return t;

#re_np = r'N(N|P)(P|S)?(\+N(N|P)(P|S)?)*'
#re_adjp = r'(ADJP)|(JJ(R|S)?)(\+(ADJP)|(JJ(R|S)?))*'
re_np = 'NOUN'
re_adjp = 'ADJ'
re_verb = 'VERB'
Total_Array = []
for chunked_sent in chunked:
    NP_array = []
    ADJ_array = []
    VERB_array = []
    done_list = []
    t=-1    
    NP_word = dfs(chunked_sent, re_np, done_list);
    while(t != -1):
        NP_array.append(NP_word);
        done_list.append(NP_word);
        #print done_list
        t=-1    
        NP_word = dfs(chunked_sent, re_np, done_list)
        
        #print NP_word
    
    t=-1
    done_list = []
    ADJ_word = dfs(chunked_sent, re_adjp, done_list)
    while(t != -1):
        ADJ_array.append(ADJ_word);
        done_list.append(ADJ_word);                            
        t=-1    
        count = 0
        ADJ_word = dfs(chunked_sent, re_adjp, done_list)

    t=-1
    done_list = []
    VERB_word = dfs(chunked_sent, re_verb, done_list)
    while(t != -1):
        
        VERB_array.append(VERB_word);
        done_list.append(VERB_word);                            
        t=-1    
        count = 0
        VERB_word = dfs(chunked_sent, re_verb, done_list)  
    Total_Array.append((NP_array, ADJ_array, VERB_array))
print Total_Array 
    
