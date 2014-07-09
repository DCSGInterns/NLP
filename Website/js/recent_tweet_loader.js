var jsonObj;

function displayJSON(jsonObj)
{
    var x = document.getElementById("tweets");
    x.innerHTML = "";
    for (i = 0; i < jsonObj.length; i++) {
        if (jsonObj[i].sentiment <= -0.5)
            style = "style=\"background-color:#FF3333;\"";
        else if (jsonObj[i].sentiment > -0.5 && jsonObj[i].sentiment <= 0.0)
            style = "style=\"background-color:#FFB84D;\"";
        else if (jsonObj[i].sentiment > 0.0 && jsonObj[i].sentiment <= 0.5)
            style = "style=\"background-color:#8AE62E\"";
        else
            style = "style=\"background-color:#66C266;\"";

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

function loadJSON(){
    var x = document.getElementById("tweets");
    x.innerHTML = "<img src=\"img/loading.gif\" style=\"width:600px;position:relative;left:30%;\">";
    var data_file = "tweet_caller.php"
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
            window.jsonObj = JSON.parse(http_request.responseText);
            displayJSON(jsonObj);
        }
    }

    http_request.open("GET",data_file,true);
    http_request.send();
}