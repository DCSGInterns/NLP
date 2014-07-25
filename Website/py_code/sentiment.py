import time
start_time =  time.clock()

import json
import re
import datetime
import sys
import os
import MySQLdb
from textblob import TextBlob

def gather_input():

    #gather input
    for file in os.listdir("../scrapper/"):
        if file.endswith(".txt"):
            inputFile = file
    file = open("../scrapper/"+inputFile,"r")
    input = file.read()
    file.close()

    #os.remove("../scrapper/"+inputFile)

    #extract text
    reg_string=ur"\"text\":\"(.+?)[^\\]\""
    data_array=re.findall(reg_string,input)
    
    #extract location of tweet
    reg_string=ur"\"location\":\"(.*?)\""
    location_array=re.findall(reg_string,input)
        
    #extract whether retweeted or not
    reg_string = ur"\"retweeted\":(.+?),"
    retweet_bool=re.findall(reg_string,input)
    
    #today's date in YYYYMMDD format
    date = datetime.datetime.now()
    date = date.date()
    #date = date.strftime("%Y%m%d")

    ## calcualte the barrier date
    date_diff = int(sys.argv[1])
    DD = datetime.timedelta(days=date_diff)
    barrier_date = (datetime.datetime.now()- DD).date()

    ## load the whitelist and create array of arrays as - [noun,sentiment,count]
    file = open("../py_code/white_list.txt","r")
    white_list = []
    line = file.readline()
    while line:
        white_list.append([line.rstrip(),0,0])
        line = file.readline()
    file.close()

    ## create a sentence_tokenizer
    from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
    punkt_param = PunktParameters()
    punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    sent_tokenizer = PunktSentenceTokenizer(punkt_param)
    
    ## next step is to inject into the database
    db = MySQLdb.connect(host="localhost",user="InsightsUls0k",passwd="{2qGq(22+5iU",db="Insights")
    cur = db.cursor()
    
    ##filter out those tweet which have prices in them - usually sales, or retweets
    i=0
    for text in data_array:
        if retweet_bool[i]!="false":
            pass
        else:        
            ##filter text as many users dont put space after full stop - which is essential to use sentence tokenizer
            data_array[i] = re.sub(r'([\.\?\!])(\w)', r'\1 \2', data_array[i])
            
            blob = TextBlob(data_array[i])
            blob_sentiment = int(blob.sentiment.polarity*1000)/1000.0
            sql = "INSERT INTO Phrases(Phrase,Sentiment,Location,Date) VALUES (\""+data_array[i]+"\", "+str(blob_sentiment)+", \""+location_array[i]+"\", \""+str(date)+"\")"
            cur.execute(sql)

            ## tokenize the tweets, for sentiment analysis
            sentences = sent_tokenizer.tokenize(data_array[i])

            if len(sentences) == 1:
                ##run through the whiteList array, for each find count, add count, sentiment to array
                for word in white_list:
                    if((sentences[0].lower()).find(word[0])!=-1):
                        word[1]=word[1]+blob_sentiment
                        word[2]=word[2]+1

                        
            else:
                for sentence in sentences:
                    ##run through the whiteList array, for each find count and sentiment, add count, sentiment to array
                    for word in white_list:
                        if((sentence.lower()).find(word[0])!=-1):
                            blob = TextBlob(sentence)
                            word[1]=word[1]+int(blob.sentiment.polarity*1000)/1000.0
                            word[2]=word[2]+1
                            
                           
        i=i+1
    db.commit()

    ### now integerate these into Sentiment db, if there is no entry for today insert phrase and create one
    sql = "SELECT * FROM Sentiment WHERE `Date` ='"+str(date)+"' LIMIT 1;"
    cur.execute(sql)
    if(cur.rowcount==0):
        for word in white_list:
            if(word[2]!=0):
                sql = "INSERT INTO Sentiment VALUES ('"+str(date)+"','"+word[0]+"','"+str(word[1])+"','"+str(word[2])+"');"
                cur.execute(sql)
                
    ### else get the entry in the table, add sentiment and count, store back
    else:
        for word in white_list:
            if(word[2]!=0):
                sql = "SELECT Sentiment,Count FROM Sentiment WHERE `Date` ='"+str(date)+"'AND `Phrase`='"+word[0]+"';"
                cur.execute(sql)
                for row in cur.fetchall():
                    new_sentiment = float(row[0])+word[1]
                    new_count = row[1]+word[2]
                sql = "UPDATE Sentiment SET `Sentiment`="+str(new_sentiment)+",`Count`="+str(new_count)+" WHERE `Date` ='"+str(date)+"'AND `Phrase`='"+word[0]+"';"
                cur.execute(sql)
    db.commit()
    
    ### now add all the sentiment and count for all phrases in the white list in the Sentiment db above the barrier_date, add to json those whose count is not zero
    total_sentiment = 0;
    total_count = 0;
    json_array = [];
    for word in white_list:
        sql = "SELECT Sentiment,Count FROM Sentiment WHERE `Date` >'"+str(barrier_date)+"'AND `Phrase`='"+word[0]+"';"
        cur.execute(sql)
        if(cur.rowcount!=0):
            for row in cur.fetchall():
                total_sentiment = total_sentiment+float(row[0])
                total_count = total_count+int(row[1])
            json_array.append({"noun": word[0], "sentiment": int(total_sentiment/total_count*1000)/1000.0, "count": total_count})
            total_sentiment = 0;
            total_count = 0;
    
    db.close()   
    print(json.dumps(json_array))
    
gather_input()
       

'''  
    ## load the whitelist and create array of arrays as - [noun,sentiment,count]
    file = open("white_list.txt","r")
    white_list = []
    line = file.readline()
    while line:
        white_list.append([line.rstrip(),0,0])
        line = file.readline()
    file.close()

    ## create a sentence_tokenizer
    from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
    punkt_param = PunktParameters()
    punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    sent_tokenizer = PunktSentenceTokenizer(punkt_param)
        
    ## take a tweet, tokenize it, textblob to each token, if only one token take sentiment from db, else textblob sentiment to each token
    sql = "SELECT Phrase,Sentiment From Phrases WHERE `Date` >='"+str(date)+"';"
    cur.execute(sql)
    for row in cur.fetchall() :
        #if row[2] >=barrier_date:
            sentences = sent_tokenizer.tokenize(row[0])

            if len(sentences) == 1:
                ##run through the whiteList array, for each find count, add count, sentiment to array
                for word in white_list:
                    if((sentences[0].lower()).find(word[0])!=-1):
                        word[1]=word[1]+row[1]
                        word[2]=word[2]+1
            else:
                for sentence in sentences:
                    ##run through the whiteList array, for each find count and sentiment, add count, sentiment to array
                    for word in white_list:
                        if((sentence.lower()).find(word[0])!=-1):
                            blob = TextBlob(sentence)
                            word[1]=word[1]+int(blob.sentiment.polarity*1000)/1000.0
                            word[2]=word[2]+1

    json_array = []
    for word in white_list:
        ### only consider those whose count in not zero
        if word[2]!=0:
            ## create the json_obj
            json_array.append({"noun": word[0], "sentiment": int(word[1]/word[2]*1000)/1000.0, "count": word[2]})
    
    ## check if database has an entry for today, if not create one and insert these values
    sql = "SELECT * FROM Sentiment WHERE `Date` ='"+str(date)+"' LIMIT 1;"
    cur.execute(sql)
    if(cur.rowcount==0):
        for word in json_array:
            sql = "INSERT INTO Sentiment VALUES ('"+str(date)+"','"+word["noun"]+"','"+str(word["sentiment"])+"','"+str(word["count"])+"');"
            cur.execute(sql)
    ##else obtain the sentiment/count in the database currently, and update it with the now calculated sentiment and count
    else:
        for word in json_array:
            sql = "SELECT Sentiment,Count FROM Sentiment WHERE `Date` ='"+str(date)+"'AND `Phrase`='"+word["noun"]+"';"
            cur.execute(sql)
            for row in cur.fetchall():
                new_sentiment = float(row[0])+word["sentiment"]
                new_count = row[1]+word["count"]
            print new_sentiment/new_count
            print new_count
    
    ## et the value of sentiment/count for the words whose count!=0 as the new combined ones, DONT FORGET TO COMMIT!!

       
    ## commit all the changes always and close the database
    db.commit() 
    db.close()
    ## return the json_object as noun,sentiment,count
    print json_array
'''
