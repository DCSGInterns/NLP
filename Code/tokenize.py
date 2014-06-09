##to improve preformace of sentence tokenizing
import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

##this is to do tokenizing based on RE
from nltk.tokenize import RegexpTokenizer

##to store the array of arrays
data_store=[]

para = '''We're going to create a set of all English stopwords, then use
it to filter stopwords from a sentence. 550% 200,000 2.23 22/7
>>> from nltk.corpus import stopwords
>>> english_stops = set(stopwords.words('english'))
>>> words = ["Can't", 'is', 'a', 'contraction']
>>> [word for word in words if word not in english_stops]
Soln : ["Can't", 'contraction']'''

sent_result = tokenizer.tokenize(para)
#print sent_result

emoticons = "[<>]?[:;=8][\-o\*\']?[\)\]\(\[dDpP/\:\}\{@\|]"
real_numbers = "[+\-]?\d+[,/\.:-]*\d+%?"
hashtags = "\#[\w_]+[\w\'_\-]*\w+"
normal_words = "[\w'\-_]*\w[\w'\-_]*"
line_endings = "[\.:;!?]+"

reg_string = emoticons+"|"+real_numbers+"|"+hashtags+"|"+normal_words+"|"+line_endings
tokenizer = RegexpTokenizer(reg_string)

for sent in sent_result :
    word_result = tokenizer.tokenize(sent)
    data_store.append(word_result)
    
print data_store
