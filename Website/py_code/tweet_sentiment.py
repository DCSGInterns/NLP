def tweet_sentiment():
    import sys
    keyword = sys.argv[1]
    max_sentiment = float(sys.argv[2])
    min_sentiment = float(sys.argv[3])
    from textblob import TextBlob
    import json
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
tweet_sentiment()

