import nltk
from nltk.corpus import wordnet as wn

list = ['too'', 'very', 'barely'', 'little']

wordnet = nltk.corpus.wordnet
Synset = nltk.corpus.wordnet.synset
Lemma = nltk.corpus.wordnet.lemma
# Part of speech constants
VERB, NOUN, ADJ, ADV = wordnet.VERB, wordnet.NOUN, wordnet.ADJ, wordnet.ADV

