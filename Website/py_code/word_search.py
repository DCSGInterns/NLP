from textblob import TextBlob
import sys
import datetime
import json
import MySQLdb

def keyword_sentiment():

    ## take in tht input
    word = sys.argv[1]
    date_diff = int(sys.argv[2])
    
    ## create a sentence_tokenizer
    from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
    punkt_param = PunktParameters()
    punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    sent_tokenizer = PunktSentenceTokenizer(punkt_param)
    
    ## caluclate the barrier date
    DD = datetime.timedelta(days=date_diff)
    barrier_date = datetime.datetime.now()- DD

    ## make connection to db and fetch tweets (and respective sentiment) above the barrier_date
    db = MySQLdb.connect(host="localhost",user="InsightsUls0k",passwd="{2qGq(22+5iU",db="Insights")
    cur = db.cursor()
    sql = "SELECT Phrase,Sentiment FROM Phrases WHERE `Date`>'"+str(barrier_date)+"';"
    cur.execute(sql)

    total_sentiment = 0
    total_count = 0
    ## locate tweets which contain keyword, tokenize them into sentences
    for row in cur.fetchall():
        if(row[0].lower().find(word.lower())!=-1):
            sentences = sent_tokenizer.tokenize(row[0])
            
    ## if a single sentence then just take the sentiment from db
            if len(sentences) == 1:
                total_sentiment = total_sentiment + float(row[1])
                total_count = total_count+1
                
    ## else add together sentiment of sentence and keep the count
            else:
                for sentence in sentences:
                        blob = TextBlob(sentence)
                        total_sentiment= total_sentiment + int(blob.sentiment.polarity*1000)/1000.0
                        if(sentence.lower().find(word.lower())!=-1):
                            total_count = total_count+1
                            
    ## json the total_sentiment/count and count
    if(total_count!=0):
        json_array = json_array = [{"sentiment": int(total_sentiment/total_count*1000)/1000.0, "count": total_count}]
    else:
        json_array = json_array = [{"sentiment": 0, "count": 0}]
    ## close the connection to the db
    db.close()
    ## print the json
    print(json.dumps(json_array))
    
keyword_sentiment()

'''
    data_str = ""
    for line in file:
        content_dictionary = json.loads(line)
        if((content_dictionary["text"].lower()).find(word.lower())!=-1):
            if(datetime.datetime.strptime(content_dictionary["date"],"%Y%m%d")>barrier_date):
                data_str = data_str+content_dictionary["text"].lower()
    blob = TextBlob(data_str)
    json_array = [{"sentiment": blob.sentiment.polarity, "count": blob.word_counts[word.lower()]}]
    file.close()
    print json.dumps(json_array)
'''
