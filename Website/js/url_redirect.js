function redirect(keyword) { 
    var max_sentiment = document.forms["myForm"]["max_sentiment"].value;
    var min_sentiment = document.forms["myForm"]["min_sentiment"].value;

    location.href = "tweets.php?keyword=" + keyword + "&max_sentiment=" + max_sentiment + "&min_sentiment=" + min_sentiment;
}