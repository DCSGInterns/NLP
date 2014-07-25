var jsonObj = "";
var jsonObj_main = "";

function displayJSON(jsonObj)
{
    var x = document.getElementById("tweets");
    x.innerHTML = "";
    if (jsonObj.length == 0) {
        
        x.innerHTML = "<div style=\"position:relative;top:50px;width:200px;margin:0px auto;font-family:'Open Sans';color:grey\"> No Results to display </div>";
        return;
    }

   
    for (i = 0; i < jsonObj.length; i++) {

        if(jsonObj[i].sentiment <= -0.75)
                style = "style=\"background-color:#f75739;\"";
            else if(jsonObj[i].sentiment > -0.75 && jsonObj[i].sentiment <= -0.5)
                style = "style=\"background-color:#db6c51;\"";
            else if(jsonObj[i].sentiment > -0.5 && jsonObj[i].sentiment <= -0.25)
                style = "style=\"background-color:#fc963a;\"";
            else if(jsonObj[i].sentiment > -0.25 && jsonObj[i].sentiment <= 0)
                style = "style=\"background-color:#ebbf48;\"";
            else if(jsonObj[i].sentiment >= 0 && jsonObj[i].sentiment< 0.25)
                style = "style=\"background-color:#b4ea1c;\"";
            else if(jsonObj[i].sentiment >= 0.25 && jsonObj[i].sentiment< 0.5)
                style = "style=\"background-color:#70ef4d;\"";
            else if(jsonObj[i].sentiment >= 0.5 && jsonObj[i].sentiment< 0.75)
                style = "style=\"background-color:#4ce85a;\"";
            else if(jsonObj[i].sentiment >= 0.75 && jsonObj[i].sentiment<= 1)
                style = "style=\"background-color:#30f17c;\"";
            
        x.innerHTML = x.innerHTML + "<div class=\"row\"><div class=\"col-lg-11 col-md-11 col-sm-11 col-xs-11\"" + style + ">" + jsonObj[i].text + "</div></div>";
    }

}


function sort_ascending_sentiment(jsonObj)
{ 
   var x = document.getElementById("tweets");
    x.innerHTML = "<img src=\"img/loading.gif\" style=\"width:600px;position:relative;left:30%;\">";
    var i = 0,j = 0;
   //insertion sorting
    var n = jsonObj.length;
    for (i = 1; i < n; i++)
    { 
        var key = jsonObj[i];
        j = i - 1;
        while(j>=0 && jsonObj[j].sentiment > key.sentiment)
        {
            jsonObj[j+1] = jsonObj[j];
            j--;
        }
        jsonObj[j + 1] = key;
    }
 
    displayJSON(jsonObj);   
}

function sort_descending_sentiment(jsonObj)
{ 
     var x = document.getElementById("tweets");
    x.innerHTML = "<img src=\"img/loading.gif\" style=\"width:600px;position:relative;left:30%;\">";
    var i = 0,j = 0;
   //insertion sorting
    var n = jsonObj.length;
    for (i = 1; i < n; i++)
    { 
        var key = jsonObj[i];
        j = i - 1;
        while(j>=0 && jsonObj[j].sentiment < key.sentiment)
        {
            jsonObj[j+1] = jsonObj[j];
            j--;
        }
        jsonObj[j + 1] = key;
    }
  
    displayJSON(jsonObj);     
}

function loadJSON(keyword,max_sentiment_val,min_sentiment_val,date_diff){
    var x = document.getElementById("tweets");
    x.innerHTML = "<img src=\"img/loading.gif\" style=\"width:600px;position:relative;left:30%;\">";
    var data_file = "tweet_caller.php?keyword="+keyword+"&max_sentiment="+max_sentiment_val+"&min_sentiment="+min_sentiment_val+"&date_diff="+date_diff;
    var http_request = new XMLHttpRequest();
    try
    {
        // Opera 8.0+, Firefox, Chrome, Safari
        http_request= new XMLHttpRequest();
    }
    catch(e)
    {
    // Internet Explorer Browsers
        try
        {
            http_request= new ActiveXObject("Msxml2.XMLHTTP");
        }
        catch(e)
        {
            try
            {
                http_request= new ActiveXObject("Microsoft.XMLHTTP");
            }
            catch(e)
            {
                // Something went wrong
                return false;
            }
        }
    }

    http_request.onreadystatechange = function () {
        if (http_request.readyState == 4) {   // Javascript function JSON.parse to parse JSON data
            window.jsonObj_main = JSON.parse(http_request.responseText);
            window.jsonObj = window.jsonObj_main;
            displayJSON(jsonObj);
        }
    }

    http_request.open("GET",data_file,true);
    http_request.send();
}

