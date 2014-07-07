"""
CKY algorithm from the "Natural Language Processing" course by Michael Collins
https://class.coursera.org/nlangp-001/class
"""

#introduce the prority

from collections import defaultdict
from pprint import pprint

try:
    from nltk import Tree
    
    def nltk_tree(t):
        return Tree(t[0], [c if isinstance(c, basestring) else nltk_tree(c) for c in t[1:]])
    
    nltk_is_available = True

except ImportError:
    nltk_is_available = False

from stat_parser.learn import build_model
from stat_parser.tokenizer import Tokenizer
from stat_parser.treebanks.normalize import un_chomsky_normal_form
from stat_parser.word_classes import is_cap_word


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

def negation(chunked):
    regexp_not = "(?:^(?:never|no|nothing|nowhere|noone|none|not|havent|hasnt|hadnt|cant|couldnt|shouldnt|wont|wouldnt|dont|doesnt|didnt|isnt|arent|aint)$)|n't"
    regexp_clause = "^[.:;!?]$"

    neg_track = []

    import re

    for chunked_sent in chunked:
        neg_sent = []
        flag = 1;
        for chunk in chunked_sent:
            word = chunk
            t = flag;
            if t==0:
                t = -1
            if word.isupper():
                t = t*2
                word = word.lower()    
            neg_sent.append((word , t))
            if re.search(regexp_not, word): #some problem here
                flag = (flag + 1) % 2;
               
        neg_track.append(neg_sent)
    #print neg_track
    return neg_track 

class Parser:
    def __init__(self, pcfg=None):
        if pcfg is None:
            pcfg = build_model()
        
        self.pcfg = pcfg
        self.tokenizer = Tokenizer()
        
        if nltk_is_available:
            self.parse = self.nltk_parse
        else:
            self.parse = self.raw_parse
    
    def norm_parse(self, paragraph):
        para = self.tokenizer.tokenize(paragraph)
        array = negation(para)
        #print para
        tree_list = []
       
        for sentence in para:        
            norm_words = []
            for word in sentence:
                if isinstance(word, tuple):
                    # This is already a word normalized to the Treebank conventions
                    norm_words.append(word)
                else:
                    #print word
                    # rare words normalization
                    norm_words.append((self.pcfg.norm_word(word), word))
                #print norm_words
            #print "end of sentence" 

            tree_list.append(CKY(self.pcfg, norm_words))
        
        return (tree_list , array )
    
    def raw_parse(self, sentence):
        tree = self.norm_parse(sentence)
        tree_list = []
        for sent in tree[0]:
            un_chomsky_normal_form(sent)
            tree_list.append(sent)
            
            #print tree[0]
        return (tree_list , tree[1])
    
    def nltk_parse(self, sentence):
        tree = self.raw_parse(sentence)
        #print tree
        return tree

def display_tree(tree):
    if nltk_is_available:
        tree.draw()
    else:
        pprint(tree)
