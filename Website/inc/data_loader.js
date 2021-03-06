var jsonObj = "";

function displayJSON(jsonObj) { 
    var x = document.getElementById("tweet_content");
            x.innerHTML = "";
            var row_content = "";

            for (i = 0; i < Math.floor(jsonObj.length / 4); i++) {
                row_content = "";
                for (j = 0; j < 3; j++) {
                    if(jsonObj[i * 4 + j].sentiment < -0.5)
                        style = "style=\"background-color:#FF3333;\"";
                    else if(jsonObj[i * 4 + j].sentiment > -0.5 && jsonObj[i * 4 + j].sentiment<0.0)
                        style = "style=\"background-color:#FFB84D;\"";
                    else if(jsonObj[i * 4 + j].sentiment > 0.0 && jsonObj[i * 4 + j].sentiment < 0.5)
                        style = "style=\"background-color:#8AE62E\"";
                    else
                        style = "style=\"background-color:#66C266;\"";

                    row_content = row_content + "<div class=\"col-lg-3 col-md-3 col-sm-3 col-xs-3\"" +style+">" + jsonObj[i * 4 + j].noun + "<br/>" + jsonObj[i * 4 + j].sentiment + "<br/>" + jsonObj[i * 4 + j].count + "</div>"
                }
                if(jsonObj[i * 4 + j].sentiment < -0.5)
                        style = "style=\"background-color:#FF3333;\"";
                    else if(jsonObj[i * 4 + j].sentiment > -0.5 && jsonObj[i * 4 + j].sentiment<0.0)
                        style = "style=\"background-color:#FFB84D;\"";
                    else if(jsonObj[i * 4 + j].sentiment > 0.0 && jsonObj[i * 4 + j].sentiment < 0.5)
                        style = "style=\"background-color:#8AE62E\"";
                    else
                        style = "style=\"background-color:#66C266;\"";


                row_content = row_content + "<div class=\"col-lg-2 col-md-2 col-sm-2 col-xs-2\"" +style+">" + jsonObj[i * 4 + j].noun + "<br/>" + jsonObj[i * 4 + j].sentiment + "<br/>" + jsonObj[i * 4 + j].count + "</div>"
                row_content = "<div class=\"row\">" + row_content + "</div>"
                x.innerHTML = x.innerHTML + row_content;
            }
            row_content = "";
            for (j = 0; j < jsonObj.length % 4; j++) {
                if(jsonObj[i * 4 + j].sentiment < -0.5)
                        style = "style=\"background-color:#FF3333;\"";
                    else if(jsonObj[i * 4 + j].sentiment > -0.5 && jsonObj[i * 4 + j].sentiment<0.0)
                        style = "style=\"background-color:#FFB84D;\"";
                    else if(jsonObj[i * 4 + j].sentiment > 0.0 && jsonObj[i * 4 + j].sentiment < 0.5)
                        style = "style=\"background-color:#8AE62E\"";
                    else
                        style = "style=\"background-color:#66C266;\"";


                row_content = row_content + "<div class=\"col-lg-3 col-md-3 col-sm-3 col-xs-3\"" +style+">" + jsonObj[i * 4 + j].noun + "<br/>" + jsonObj[i * 4 + j].sentiment + "<br/>" + jsonObj[i * 4 + j].count + "</div>"
            }
            row_content = "<div class=\"row\">" + row_content + "</div>"
            x.innerHTML = x.innerHTML + row_content;
}

function sort_ascending_count(jsonObj)
{
    var i = 0,j = 0;
   //insertion sorting
    var n = jsonObj.length;
    for (i = 1; i < n; i++)
    { 
        var key = jsonObj[i];
        j = i - 1;
        while(j>=0 && jsonObj[j].count > key.count)
        {
            jsonObj[j+1] = jsonObj[j];
            j--;
        }
        jsonObj[j + 1] = key;
    }
  
    displayJSON(jsonObj);
}

function sort_descending_count(jsonObj)
{ 
     var i = 0,j = 0;
   //insertion sorting
    var n = jsonObj.length;
    for (i = 1; i < n; i++)
    { 
        var key = jsonObj[i];
        j = i - 1;
        while(j>=0 && jsonObj[j].count < key.count)
        {
            jsonObj[j+1] = jsonObj[j];
            j--;
        }
        jsonObj[j + 1] = key;
    }

    displayJSON(jsonObj);
}
function sort_ascending_sentiment(jsonObj)
{ 
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



function loadJSON(param){
    var x = document.getElementById("tweet_content");
    x.innerHTML = "<img src=\"img/loading.gif\" style=\"width:600px;position:relative;left:30%;\">";
    var data_file = "python_caller.php";
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
        if (http_request.readyState == 4) {
            // Javascript function JSON.parse to parse JSON data
            jsonObj = JSON.parse(http_request.responseText);
            if(param == 1)
               displayJSON(jsonObj);
            else if(param == 2)     //most frequent
                sort_descending_count(jsonObj);
            else if(param == 3)     //least frequent
                sort_ascending_count(jsonObj);
            else if(param == 4)     //most positive
                sort_descending_sentiment(jsonObj);
            else if(param == 5)     //least positive
                sort_ascending_sentiment(jsonObj);

        }

    }
    http_request.open("GET",data_file,true);
    http_request.send();
}
