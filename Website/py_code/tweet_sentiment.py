def tweet_sentiment():
    from textblob import TextBlob
    import json
    file = open("py_code/filtered.txt","r")
    json_array = []
    line = file.readline()
    while line:
        blob = TextBlob(line)
        json_array.append({"text":line, "sentiment": int(blob.sentiment.polarity*1000)/1000.0})
        line = file.readline()
    print(json.dumps(json_array))

tweet_sentiment()

