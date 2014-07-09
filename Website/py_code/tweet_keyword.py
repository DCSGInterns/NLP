def keyword_sentiment():
    from textblob import TextBlob
    import sys
    word = sys.argv[1]
    import json
    file = open("py_code/filtered.txt","r");
    data_str = ""
    for line in file:
        if(line.lower().find(word.lower())!=-1):
            data_str = data_str+line.lower()
    blob = TextBlob(data_str)
    json_array = [{"sentiment": blob.sentiment.polarity, "count": blob.word_counts[word.lower()]}]
    print json.dumps(json_array)

keyword_sentiment()
