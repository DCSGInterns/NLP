def para_senti_score(sentence,senti_word):
    
    import tokenizer
    tokenized_sent = tokenizer.word_tokenizer(sentence)


    import emoticon_detection
    senti = emoticon_detection.get_score(tokenized_sent)
    count = emoticon_detection.get_count()
    tokenized_sent = emoticon_detection.remove_emoticons()
    

    if count == 0:
        
        import slang_word
        tokenized_sent = slang_word.replace(tokenized_sent)

        import word_sentiment
        senti_array = word_sentiment.negation(tokenized_sent)
        #print senti_array

        import sentiment_finding
        sentiment_finding.get_array(senti_array[0]);
        score = sentiment_finding.sentiment_finding(senti_array[1])
        

    else:
        score = senti/count

    return score



