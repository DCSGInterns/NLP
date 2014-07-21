from textblob import TextBlob
import json
import sys
import MySQLdb
import datetime

def tweet_sentiment():
    
    keyword = sys.argv[1]
    max_sentiment = float(sys.argv[2])
    min_sentiment = float(sys.argv[3])
    date_diff = int(sys.argv[4])

    ## calcualte the barrier date
    DD = datetime.timedelta(days=date_diff)
    barrier_date = (datetime.datetime.now()- DD).date()
    
    ##fetch sentiment according to the values entered
    db = MySQLdb.connect(host="localhost",user="InsightsUls0k",passwd="{2qGq(22+5iU",db="Insights")
    cur = db.cursor()
    sql = "SELECT `Phrase`,`Sentiment`,`Date` FROM Phrases WHERE `Date`>'"+str(barrier_date)+"' AND `Sentiment`>="+str(min_sentiment)+" AND Sentiment<="+str(max_sentiment)+" ORDER BY `Date` DESC LIMIT 100;"
    cur.execute(sql)

    json_array = []
    
    if(keyword=="default"):
        for row in cur.fetchall():
            json_array.append({"text":row[0], "sentiment": int(row[1]*1000)/1000.0,"date":str(row[2])})
    else:
        for row in cur.fetchall():
            if(row[0].lower().find(keyword.lower())!=-1):
                json_array.append({"text":row[0], "sentiment": int(row[1]*1000)/1000.0,"date":str(row[2])})

    print(json.dumps(json_array))

tweet_sentiment()
    
'''
    file = open("py_code/JSON.txt","r")
    json_array = []
    line = file.readline()
    while line:
        content_dictionary = json.loads(line)
        content = content_dictionary["text"]
        if(content_dictionary["sentiment"]==2):
            blob = TextBlob(content)
            json_array.append({"text":content, "sentiment": int(blob.sentiment.polarity*1000)/1000.0,"date":content_dictionary['date']})
        else:
            json_array.append({"text":content, "sentiment": content_dictionary["sentiment"],"date":content_dictionary['date']})
        line = file.readline()
    file.close()
    file = open('py_code/JSON.txt','w')
    i=0
    while i<len(json_array):
        file.write(json.dumps(json_array[i]))
        file.write("\n")
        i=i+1
    file.close()
    

    if(keyword=="default"):
        print(json.dumps(json_array))
    else:
        json_temp = []
        i=0
        k=0;
        while i<len(json_array):
            if((json_array[i]["text"]).lower().find(keyword)>=0):
                if(json_array[i]["sentiment"] >= min_sentiment):
                    if(json_array[i]["sentiment"] <= max_sentiment):
                        json_temp.append(json_array[i])
                        k=k+1
            i=i+1    
        print(json.dumps(json_temp))

'''
    

