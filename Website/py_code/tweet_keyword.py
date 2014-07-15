def keyword_sentiment():
    from textblob import TextBlob
    import sys
    word = sys.argv[1]
    date_diff = int(sys.argv[2])

    import datetime
    DD = datetime.timedelta(days=date_diff)
    barrier_date = datetime.datetime.now()- DD

    import json
    file = open("py_code/JSON.txt","r");
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

keyword_sentiment()
