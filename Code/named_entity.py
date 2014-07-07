'''NOTE: this is highly non-optimized ..
Relating np to vp what refers to what ...
use anaphora from nltk then u have to search for sentiment for those words only.
'''

'''Apply conjuction rules given in the paper - bookmarked'''

#count number of times word has come 

t = -1
import re

def parsing(test_sentence):
    '''Input - plain para 
    Output - [[Sentence] , [[NP , (tag,word), (tag, word)]]] 
    Parsing done with the the help of Pystat Parser - https://github.com/emilmont/pyStatParser '''

    from stat_parser import Parser
    parser = Parser()
    chunked = parser.parse(test_sentence)

    return chunked

#Trying to make a list of matching words ... Pretty lame function -> have to try improving it using regular expression
def match(pattern , tree):
    '''Input  - Pattern to be matched with tag of the tree eg.NP and the tree itself
    Output - boolean true or false
    '''
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


def dfs(tree, check, avoid_list):
    ''' Do a dfs search ...to check whether word is Noun ,  Adjective or Verb 
    avoid_list is for not repeating the word '''

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

def differentiate_clauses(chunked_sent):
    '''Seperate cluses in a sentence ..have a look at conjuction rules '''
    if(chunked_sent[0] == 'S'):
        return [chunked_sent];
    else:
        return [chunked_sent[1], chunked_sent[2]]  



def phrasing(chunked):
    '''Input -  Chunked (parsed) sentences 
    Output -   array  - <(extracting NP) , (adjectives), (verbs)>
    '''

    global t
    chunked_delta = []
    for chunked_sent in chunked:
        for part in differentiate_clauses(chunked_sent):
            chunked_delta.append(part)
            
    chunked = chunked_delta


    #re_np = r'N(N|P)(P|S)?(\+N(N|P)(P|S)?)*'
    #re_adjp = r'(ADJP)|(JJ(R|S)?)(\+(ADJP)|(JJ(R|S)?))*'
    re_np = 'NOUN'
    re_adjp = 'ADJ'
    re_verb = 'VERB'
    Total_Array = []     

    for chunked_sent in chunked: #Optimize this part
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
    return Total_Array    

def para_senti_score(para):
    '''Input - Plain para
    Output - The sentiment score of that para'''
    parsed  = parsing(para);
    Tuple_array = phrasing(parsed[0])
    neg_array = parsed[1]

    import sentiment_finding
    score = 0
    count = 0

    sentiment_finding.get_array(neg_array);

    for sentence in Tuple_array:
        score = score + sentiment_finding.sentiment_finding(*sentence);
        count += 1
    
    return score

'''from nltk.sem.drt import resolve_anaphora
print resolve_anaphora(test_sentence); '''

