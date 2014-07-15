function filter_JSON() {
    
    var max_sentiment = document.forms["myForm"]["max_sentiment"].value;
    var min_sentiment = document.forms["myForm"]["min_sentiment"].value;
    var date_diff = document.forms["myForm"]["data_of"].value;

 
    if (max_sentiment == "")
        max_sentiment = 1 ;
    if (min_sentiment == "")
        min_sentiment = -1 ;
    if (date_diff == "")
        date_diff = 180;

    var barrier_date = new Date();
    barrier_date.setDate(barrier_date.getDate() - date_diff);

    jsonObj = jsonObj_main;
    var jsonObj_temp=[];

    i = 0;k = 0;
    while (i < jsonObj.length) {
        var year = parseInt(jsonObj[i].date.slice(0, 4));
        var month = parseInt(jsonObj[i].date.slice(4, 6)) - 1;
        var day = parseInt(jsonObj[i].date.slice(6, 8));

        var json_date = new Date(year, month, day);

        if (jsonObj[i].sentiment >= min_sentiment && jsonObj[i].sentiment <= max_sentiment && json_date > barrier_date)
        { jsonObj_temp[k] = jsonObj[i]; k++; }
        i++;
    }
    jsonObj = jsonObj_temp;
    displayJSON(jsonObj);
    
}