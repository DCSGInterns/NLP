import json
import re
import datetime
import sys
import os
import MySQLdb
from textblob import TextBlob

def calculate_sentiment():
    #today's date in YYYYMMDD format
    date_time= datetime.datetime.now()
    date = date_time.date()
    
    ## next step is to inject into the database
    db = MySQLdb.connect(host="localhost",user="InsightsUls0k",passwd="{2qGq(22+5iU",db="Insights")
    cur = db.cursor()

    json_array = []
    sql = "SELECT `Phrase`,`Sentiment` FROM Phrases WHERE `Date`='"+str(date)+"'"
    cur.execute(sql)
    while cur.rowcount!=0:
        total_sentiment = 0
        total_count = 0
        for row in cur.fetchall():
            total_sentiment = total_sentiment + float(row[1])
            total_count = total_count+1
        json_array.append({"sentiment":str(int(total_sentiment/total_count*1000)/1000.0),"date":str(date)})

        DD = datetime.timedelta(days=1)
        date_time = (date_time- DD)
        date = date_time.date()
        
        sql = "SELECT `Phrase`,`Sentiment` FROM Phrases WHERE `Date`='"+str(date)+"'"
        cur.execute(sql)
    print json.dumps(json_array)
    
calculate_sentiment()
