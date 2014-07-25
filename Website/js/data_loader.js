var jsonObj = "";
var jsonObj_main = "";

var sort_s_a = 0;
var sort_s_d = 0;

var sort_c_a = 0;
var sort_c_d = 0;


function displayJSON(jsonObj) { 
    var x = document.getElementById("tweet_content");
    x.innerHTML = "";
    var row_content = "";

    if (jsonObj.length == 0) {
        x.innerHTML = "<div style=\"position:relative;top:50px;width:200px;margin:0px auto;font-family:'Open Sans';color:grey\"> No Results to display </div>";
        return;
    }

    for (i = 0; i < Math.floor(jsonObj.length / 4); i++) {
        row_content = "";
        for (j = 0; j < 3; j++) {

            javascript = "onclick=\"redirect(\'"+jsonObj[i * 4 + j].noun+"\')\"";

            if(jsonObj[i * 4 + j].sentiment <= -0.75)
                style = "style=\"background-color:#f75739;\"";
            else if(jsonObj[i * 4 + j].sentiment > -0.75 && jsonObj[i * 4 + j].sentiment <= -0.5)
                style = "style=\"background-color:#db6c51;\"";
            else if(jsonObj[i * 4 + j].sentiment > -0.5 && jsonObj[i * 4 + j].sentiment <= -0.25)
                style = "style=\"background-color:#fc963a;\"";
            else if(jsonObj[i * 4 + j].sentiment > -0.25 && jsonObj[i * 4 + j].sentiment < 0)
                style = "style=\"background-color:#ebbf48;\"";
            else if(jsonObj[i * 4 + j].sentiment >= 0 && jsonObj[i * 4 + j].sentiment< 0.25)
                style = "style=\"background-color:#b4ea1c;\"";
            else if(jsonObj[i * 4 + j].sentiment >= 0.25 && jsonObj[i * 4 + j].sentiment< 0.5)
                style = "style=\"background-color:#70ef4d;\"";
            else if(jsonObj[i * 4 + j].sentiment >= 0.5 && jsonObj[i * 4 + j].sentiment< 0.75)
                style = "style=\"background-color:#4ce85a;\"";
            else if(jsonObj[i * 4 + j].sentiment >= 0.75 && jsonObj[i * 4 + j].sentiment<= 1)
                style = "style=\"background-color:#30f17c;\"";

            row_content = row_content + "<div class=\"col-lg-3 col-md-3 col-sm-3 col-xs-3\"" +style+javascript+">" + jsonObj[i * 4 + j].noun + "<br/>S : " + jsonObj[i * 4 + j].sentiment + "<br/>C : " + jsonObj[i * 4 + j].count + "</div>"
        }
        if(jsonObj[i * 4 + j].sentiment <= -0.75)
                style = "style=\"background-color:#f75739;\"";
            else if(jsonObj[i * 4 + j].sentiment > -0.75 && jsonObj[i * 4 + j].sentiment <= -0.5)
                style = "style=\"background-color:#db6c51;\"";
            else if(jsonObj[i * 4 + j].sentiment > -0.5 && jsonObj[i * 4 + j].sentiment <= -0.25)
                style = "style=\"background-color:#fc963a;\"";
            else if(jsonObj[i * 4 + j].sentiment > -0.25 && jsonObj[i * 4 + j].sentiment <= 0)
                style = "style=\"background-color:#ebbf48;\"";
            else if(jsonObj[i * 4 + j].sentiment >= 0 && jsonObj[i * 4 + j].sentiment< 0.25)
                style = "style=\"background-color:#b4ea1c;\"";
            else if(jsonObj[i * 4 + j].sentiment >= 0.25 && jsonObj[i * 4 + j].sentiment< 0.5)
                style = "style=\"background-color:#70ef4d;\"";
            else if(jsonObj[i * 4 + j].sentiment >= 0.5 && jsonObj[i * 4 + j].sentiment< 0.75)
                style = "style=\"background-color:#4ce85a;\"";
            else if(jsonObj[i * 4 + j].sentiment >= 0.75 && jsonObj[i * 4 + j].sentiment<= 1)
                style = "style=\"background-color:#30f17c;\"";

        javascript = "onclick=\"redirect(\'"+jsonObj[i * 4 + j].noun+"\')\"";

        row_content = row_content + "<div class=\"col-lg-2 col-md-2 col-sm-2 col-xs-2\"" +style+javascript+">" + jsonObj[i * 4 + j].noun + "<br/>S : " + jsonObj[i * 4 + j].sentiment + "<br/>C : " + jsonObj[i * 4 + j].count + "</div>"
        row_content = "<div class=\"row\">" + row_content + "</div>"
        x.innerHTML = x.innerHTML + row_content;
    }
    row_content = "";
    for (j = 0; j < jsonObj.length % 4; j++) {

        javascript = "onclick=\"redirect(\'"+jsonObj[i * 4 + j].noun+"\')\"";

        if(jsonObj[i * 4 + j].sentiment <= -0.75)
                style = "style=\"background-color:#f75739;\"";
            else if(jsonObj[i * 4 + j].sentiment > -0.75 && jsonObj[i * 4 + j].sentiment <= -0.5)
                style = "style=\"background-color:#db6c51;\"";
            else if(jsonObj[i * 4 + j].sentiment > -0.5 && jsonObj[i * 4 + j].sentiment <= -0.25)
                style = "style=\"background-color:#fc963a;\"";
            else if(jsonObj[i * 4 + j].sentiment > -0.25 && jsonObj[i * 4 + j].sentiment <= 0)
                style = "style=\"background-color:#ebbf48;\"";
            else if(jsonObj[i * 4 + j].sentiment >= 0 && jsonObj[i * 4 + j].sentiment< 0.25)
                style = "style=\"background-color:#b4ea1c;\"";
            else if(jsonObj[i * 4 + j].sentiment >= 0.25 && jsonObj[i * 4 + j].sentiment< 0.5)
                style = "style=\"background-color:#70ef4d;\"";
            else if(jsonObj[i * 4 + j].sentiment >= 0.5 && jsonObj[i * 4 + j].sentiment< 0.75)
                style = "style=\"background-color:#4ce85a;\"";
            else if(jsonObj[i * 4 + j].sentiment >= 0.75 && jsonObj[i * 4 + j].sentiment<= 1)
                style = "style=\"background-color:#30f17c;\"";


        row_content = row_content + "<div class=\"col-lg-3 col-md-3 col-sm-3 col-xs-3\"" +style+javascript+">" + jsonObj[i * 4 + j].noun + "<br/>S : " + jsonObj[i * 4 + j].sentiment + "<br/>C : " + jsonObj[i * 4 + j].count + "</div>"
    }
    row_content = "<div class=\"row\">" + row_content + "</div>"
    x.innerHTML = x.innerHTML + row_content;
}

function sort_ascending_count(jsonObj)
{
    var x = document.getElementById("tweet_content");
    x.innerHTML = "<img src=\"img/loading.gif\" style=\"width:600px;position:relative;left:30%;\">";
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
  
    window.sort_c_a = 1;
    window.sort_c_d = 0;

    displayJSON(jsonObj);

   
}

function sort_descending_count(jsonObj)
{ 
     var x = document.getElementById("tweet_content");
    x.innerHTML = "<img src=\"img/loading.gif\" style=\"width:600px;position:relative;left:30%;\">";
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
    window.sort_c_a = 0;
    window.sort_c_d = 1;

    displayJSON(jsonObj);

   
}

function sort_ascending_sentiment(jsonObj)
{ 
     var x = document.getElementById("tweet_content");
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
    window.sort_s_a = 1;
    window.sort_s_d = 0;
 
    displayJSON(jsonObj);   

    
}

function sort_descending_sentiment(jsonObj)
{ 
     var x = document.getElementById("tweet_content");
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
    window.sort_s_a = 0;
    window.sort_s_d = 1;

    displayJSON(jsonObj);     
}



function loadJSON(value){
    var x = document.getElementById("tweet_content");
    x.innerHTML = "<img src=\"img/loading.gif\" style=\"width:600px;position:relative;left:30%;\">";
    var data_file = "scrapper/python_caller.php?date_diff="+value;
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
            window.jsonObj_main = JSON.parse(http_request.responseText);
            window.jsonObj = jsonObj_main;
            filter_JSON()
        }

    }
    http_request.open("GET",data_file,true);
    http_request.send();
}

setInterval(function () {
    var arg = document.forms['myForm']['data_of'].value;

    loadJSON(arg);
    filter_JSON();

    if (sort_c_a == 1)
        sort_ascending_count(jsonObj);
    if (sort_c_d == 1)
        sort_descending_count(jsonObj);
    if (sort_s_a == 1)
        sort_ascending_sentiment(jsonObj);
    if (sort_s_d == 1)
        sort_descending_sentiment(jsonObj);

}, 600000);

/*
function filter_byDate_JSON(){
    var date_diff = document.forms["myForm"]["data_of"].value;
    var param = "date_diff="+date_diff;

    var x = document.getElementById("tweet_content");

    x.innerHTML = "<img src=\"img/loading.gif\" style=\"width:600px;position:relative;left:30%;\">";
    var data_file = "scrapper/filter.php";
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
            window.jsonObj_main = JSON.parse(http_request.responseText);
            window.jsonObj = jsonObj_main;
               displayJSON(jsonObj);
        }

    }
    http_request.open("GET",data_file+"?"+param,true);
    http_request.send();

}
*/

