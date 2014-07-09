def gather_input():
    import re
    file = open("py_code/input.txt","r")
    input = file.read()
    file.close()
    reg_string = ur"\"text\":\"(.+?)[^\\]\""
    data_array=re.findall(reg_string,input)
    spam_filter(data_array)




def spam_filter(data_array):
    '''
    Filter out all the hastag element and the encoded characters??/
    '''
    import json
    import re
    filtered_array = []
    data_str=''
    file=open("py_code/filtered.txt","w")

    for text in data_array:
        if re.findall(r'Price [0-9]+\.?[0-9]* ',text):
            #print text, '*************************************'
            pass
        else:
            data_str=data_str+text
            file.write(text);
            file.write("\n");

    file.close()
    ########    Flitering out grammatical errors with line endings
    data_str = re.sub(r'([\.\?\!])(\w)', r'\1 \2', data_str)
    ########
    
    tokenize(data_str)




def tokenize(para):
    
    import nltk
    import json
    ##### sentence tokenizer
    from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
    punkt_param = PunktParameters()
    punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    sent_tokenizer = PunktSentenceTokenizer(punkt_param)
    #sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    ##### word/other tokenizer
    from nltk.tokenize import RegexpTokenizer

    emoticons = "[<>]?[:;=8][\-o\*\']?[\)\]\(\[dDpP/\:\}\{@\|]"
    real_numbers = "[+\-]?\d+[0123456789,/.:-]*%?"
    hashtags = "\#[\w_]+[\w\'_\-]*\w+"
    all_words = "[\w'\-_]*\w[\w'\-_]*"
    line_endings = "[.:;,!?]+"

    reg_string = emoticons+"|"+real_numbers+"|"+hashtags+"|"+all_words+"|"+line_endings
    word_tokenizer = RegexpTokenizer(reg_string)

    ############## noun phrase extraction
    from textblob import TextBlob
    required_noun = ['dell','laptop','pc','notebook','desktop','service','order','delievery']
    info_tuple=[]
    data_store=[]
    sentiment_str=''
    
    sentences = sent_tokenizer.tokenize(para)
    for sentence in sentences :
        for noun in required_noun :
            if (sentence.lower().find(noun)!=-1) :
                info_tuple=[noun,sentence.lower()]
                #print sentence
                #print noun
                #print info_tuple
                data_store.append(info_tuple)

    json_array = []
    
    for noun in required_noun:
        for data in data_store:
            if noun in data:
                sentiment_str=sentiment_str+data[1]
        blob = TextBlob(sentiment_str)
        if(blob.word_counts[noun]>0):
            json_array.append({"noun": noun, "sentiment": int(blob.sentiment.polarity*1000)/1000.0, "count":blob.word_counts[noun]})
    print(json.dumps(json_array))
        
def noun_phrase(para):
    from textblob import TextBlob
    blob=TextBlob(para)
    list=blob.noun_phrases
    for noun in list:
        print noun, blob.word_counts[noun]

gather_input()
