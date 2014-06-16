import nltk
from classifier import classifier
from nltk.chunk import ne_chunk
from nltk.tag import pos_tag


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

tokenized = classifier(test_sentence);
tagged_para = pos_tag(tokenized[0])
#print tagged_para;

#for tagged_sent in tagged_para :;
tagged_sent = tagged_para
chunked_sent = ne_chunk(tagged_sent, binary=True);
chunked.append(chunked_sent)
#print chunked

#introducing the sentiment
#negation
'''
regexp_not = "(?:^(?:never|no|nothing|nowhere|noone|none|not|havent|hasnt|hadnt|cant|couldnt|shouldnt|wont|wouldnt|dont|doesnt|didnt|isnt|arent|aint)$)|n't"
regexp_clause = "^[.:;!?]$"

import re

for chunk in chunked:
	flag = 1;
	count = 0;
	for word in chunk :
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
#dependency tree 
from pprint import pprint

try:
    from nltk import Tree
    
    def nltk_tree(t):
        return Tree(t[0], [c if isinstance(c, basestring) else nltk_tree(c) for c in t[1:]])
    
    nltk_is_available = True

except ImportError:
    nltk_is_available = False

from collections import defaultdict

def argmax(lst):
    return max(lst) if lst else (0.0, None)


def backtrace(back, bp):
    # Extract the tree from the backpointers
    if not back: return None
    if len(back) == 6:
        (X, Y, Z, i, s, j) = back
        return [X, backtrace(bp[i  , s, Y], bp),
                   backtrace(bp[s+1, j, Z], bp)]
    else:
        (X, Y, i, i) = back
        return [X, Y]

def CKY(pcfg, norm_words):
    x, n = [("", "")] + norm_words, len(norm_words)
    
    # Charts
    pi = defaultdict(float)
    bp = defaultdict(tuple)
    for i in range(1, n+1):
        for X in pcfg.N:
            norm, word = x[i]
            if (X, norm) in pcfg.q1:
                pi[i, i, X] = pcfg.q1[X, norm]
                bp[i, i, X] = (X, word, i, i)
    
    # Dynamic program
    for l in range(1, n):
        for i in range(1, n-l+1):
            j = i+l
            for X in pcfg.N:
                # Note that we only check rules that exist in training
                # and have non-zero probability
                score, back = argmax([(
                        pcfg.q2[X, Y, Z] * pi[i, s, Y] * pi[s+1, j, Z],
                        (X, Y, Z, i, s, j)
                    ) for s in range(i, j)
                        for Y, Z in pcfg.binary_rules[X]
                            if pi[i  , s, Y] > 0.0
                            if pi[s+1, j, Z] > 0.0
                ])
                
                if score > 0.0:
                    bp[i, j, X], pi[i, j, X] = back, score
    
    _, top = max([(pi[1, n, X], bp[1, n, X]) for X in pcfg.N])
    return backtrace(top, bp)

class Parser:
    def __init__(self, pcfg=None):
        if pcfg is None:
            pcfg = build_model()
        
        self.pcfg = pcfg

    def norm_parse(self, sentence):
        words = chunked;
        if is_cap_word(words[0]):
            words[0] = words[0].lower()
        
        norm_words = []
        for word in words:
            if isinstance(word, tuple):
                # This is already a word normalized to the Treebank conventions
                norm_words.append(word)
            else:
                # rare words normalization
                norm_words.append((self.pcfg.norm_word(word), word))
        return CKY(self.pcfg, norm_words)        

    def raw_parse(self, sentence):
        tree = self.norm_parse(sentence)
        un_chomsky_normal_form(tree)
        return tree

    def display_tree(tree):
        if nltk_is_available:
            tree.draw()
        else:
            pprint(tree)
   

         
#output - array  - <(extracting NP) , (adjectives)>

