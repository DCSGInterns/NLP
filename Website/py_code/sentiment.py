def gather_input():
    import json
    import re
    from datetime import datetime
    import sys

    import os
    for file in os.listdir("../scrapper/"):
        if file.endswith(".txt"):
            inputFile = file
    #gather input
    file = open("../scrapper/"+inputFile,"r")
    
    input = file.read()

    file.close()

    #os.remove("../scrapper/"+inputFile)

    #extract text, whether retweeted or not, date of tweet
    reg_string=ur"\"text\":\"(.+?)[^\\]\""
    data_array=re.findall(reg_string,input)
    
    reg_string = ur"\"retweeted\":(.+?),"
    retweet_bool=re.findall(reg_string,input)

    reg_string = ur"},\"created_at\":\"(.+?)\""
    dates=re.findall(reg_string,input)
    filtered_dates = []

    #format date of tweet to yyyymmdd
    for date in dates:
        part=date.split()
        date = part[2]+' '+part[1]+' '+part[5]
        date = datetime.strptime(date,"%d %b %Y")
        date = date.strftime("%Y%m%d")
        filtered_dates.append(date)

    filtered_data = []

    ##filter out those tweet which have prices in them - usually sales, or retweets
    fileJSON=open("../py_code/JSON.txt","a")
    i=0;
    file_array = []
    for text in data_array:
        if re.findall(r'Price [0-9]+\.?[0-9]* ',text):
            #print text, '*************************************'
            pass
        if retweet_bool[i]!="false":
            pass
        else:
            ## concatenate to make a string and write as json to file
            fileJSON.write("{\"text\": \""+text+"\",\"sentiment\": 2, \"date\": \""+filtered_dates[i]+"\"}\n")
        i=i+1

    fileJSON.close()
    tokenize(int(sys.argv[1]))


def tokenize(value):
    import nltk
    import json
    import re
    
    ##### sentence tokenizer
    from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
    punkt_param = PunktParameters()
    punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    sent_tokenizer = PunktSentenceTokenizer(punkt_param)
    #sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    #### deciphering time
    import datetime
    flag=0
    DD = datetime.timedelta(days=value)
    barrier_date = datetime.datetime.now()- DD
    '''
    ##### word/other tokenizer
    from nltk.tokenize import RegexpTokenizer

    emoticons = "[<>]?[:;=8][\-o\*\']?[\)\]\(\[dDpP/\:\}\{@\|]"
    real_numbers = "[+\-]?\d+[0123456789,/.:-]*%?"
    hashtags = "\#[\w_]+[\w\'_\-]*\w+"
    all_words = "[\w'\-_]*\w[\w'\-_]*"
    line_endings = "[.:;,!?]+"

    reg_string = emoticons+"|"+real_numbers+"|"+hashtags+"|"+all_words+"|"+line_endings
    word_tokenizer = RegexpTokenizer(reg_string)
    '''
    from textblob import TextBlob
    required_noun = ['dell','laptop','pc','notebook','desktop','service','order','delievery']
    info_tuple=[]
    data_store=[]
    sentiment_str=''

    reg_string_text=ur"\"text\": \"(.+?)[^\\]\""
    reg_string_date=ur"\"date\": \"(.+?)\""
    
    file=open("../py_code/JSON.txt","r")
    json_array = []
    line = file.readline()
    while line:
        content_dictionary = json.loads(line)
        #content_array=re.findall(reg_string_text,content)
        #date_array = re.findall(reg_string_date,content)
        i=0;
 
        if datetime.datetime.strptime(content_dictionary["date"],"%Y%m%d")>barrier_date:
    
            #Flitering out grammatical errors with line endings
            content = re.sub(r'([\.\?\!])(\w)', r'\1 \2', content_dictionary["text"])

            sentences = sent_tokenizer.tokenize(content)
            for sentence in sentences :
                for noun in required_noun :
                    if (sentence.lower().find(noun)!=-1) :
                        info_tuple=[noun.lower(),sentence.lower()]
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
                sentiment_str = ""
                if(blob.word_counts[noun]>0):
                    json_array.append({"noun": noun, "sentiment": int(blob.sentiment.polarity*1000)/1000.0, "count":blob.word_counts[noun]})
        line = file.readline()
    file.close()
    print(json.dumps(json_array))
        
def noun_phrase(para):
    from textblob import TextBlob
    blob=TextBlob(para)
    list=blob.noun_phrases
    for noun in list:
        print noun, blob.word_counts[noun]

gather_input()

