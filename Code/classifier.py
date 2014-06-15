## TOKENIZING

#para  = raw_input("Comment Here : ")
para = ''' This is a test paragraph. The idea is to find out all the ways in
which our sentence tokenizer would fail -
1. Hey!!!, What are you doing??
2. THIS IS PRIVATE PROPERTY. HANDS OFFF!!!!!
3. I don't know WHAT your problem is???
4. Come on, COME ON
4. Phone No : +91-94465-00359, 0484-2203982.
5. Emoticons : :) :( :P.
6. Ellipssis : .......
7. Leinghter Text : HECCKKKK NOOOOOOOO!!!!!!''' 

def classifier():
        import nltk
        
        #from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
        #punkt_param = PunktParameters()
        #punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc'])
        #sentence_tokenizer = PunktSentenceTokenizer(punkt_param)
        sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

        sent_result = sent_tokenizer.tokenize(para)
        #for sent in sent_result:
        #    print sent
        #    print "_______________________________"
        
        ##this is to do tokenizing based on RE
        from nltk.tokenize import RegexpTokenizer

        emoticons = "[<>]?[:;=8][\-o\*\']?[\)\]\(\[dDpP/\:\}\{@\|]"
        real_numbers = "[+\-]?\d+[0123456789,/.:-]*%?"
        hashtags = "\#[\w_]+[\w\'_\-]*\w+"
        all_words = "[\w'\-_]*\w[\w'\-_]*"
        line_endings = "[.:;,!?]+"

        reg_string = emoticons+"|"+real_numbers+"|"+hashtags+"|"+all_words+"|"+line_endings
        word_tokenizer = RegexpTokenizer(reg_string)

        ##to store the array of arrays
        data_store=[]

        for sent in sent_result :
                word_result = word_tokenizer.tokenize(sent)
                data_store.append(word_result)
    
        print data_store
	#return data_store
	
''' ISSUES WITH SENTENCE TOKENIZER
** Cannot recognize bullet types eg, 1. Sm text, 2. Some text (Mr. Mrs. Dr. Prof.)  - ITS POSSIBLE TO TRAIN
** Splits multiple exclamation/question marks onto multiple sentences - WHY???
'''

''' ISSUES WITH WORD TOKENIZER
NOT SURE WHAT ALL COULD COME AS all_words - cud be possible that i missed out something >>> 
combination of words/numbers/symbols???
'''

classifier()
