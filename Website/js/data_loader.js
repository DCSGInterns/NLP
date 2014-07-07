function displayJSON(jsonObj) { 
    var x = document.getElementById("tweet_content");
            x.innerHTML = "";
            var row_content = "";

            for (i = 0; i < Math.floor(jsonObj.length / 4); i++) {
                row_content = "";
                for (j = 0; j < 3; j++) {
                    row_content = row_content + "<div class=\"col-lg-3 col-md-3 col-sm-3 col-xs-3\">" + jsonObj[i * 4 + j].noun + "<br/>" + jsonObj[i * 4 + j].sentiment + "<br/>" + jsonObj[i * 4 + j].count + "</div>"
                }
                row_content = row_content + "<div class=\"col-lg-2 col-md-2 col-sm-2 col-xs-2\">" + jsonObj[i * 4 + j].noun + "<br/>" + jsonObj[i * 4 + j].sentiment + "<br/>" + jsonObj[i * 4 + j].count + "</div>"
                row_content = "<div class=\"row\">" + row_content + "</div>"
                x.innerHTML = x.innerHTML + row_content;
            }
            row_content = "";
            for (j = 0; j < jsonObj.length % 4; j++) {
                row_content = row_content + "<div class=\"col-lg-3 col-md-3 col-sm-3 col-xs-3\">" + jsonObj[i * 4 + j].noun + "<br/>" + jsonObj[i * 4 + j].sentiment + "<br/>" + jsonObj[i * 4 + j].count + "</div>"
            }
            row_content = "<div class=\"row\">" + row_content + "</div>"
            x.innerHTML = x.innerHTML + row_content;
}

function sort_ascending_count(jsonObj)
{

    displayJSON(jsonObj);
}
function sort_descending_count(jsonObj)
{ 
    
    displayJSON(jsonObj);
}
function sort_ascending_sentiment(jsonObj)
{ 
    
    displayJSON(jsonObj);     
}
function sort_descending_sentiment(jsonObj)
{ 
    
    displayJSON(jsonObj);
}



function loadJSON(param){
    var flag = 1;
    var data_file = "../py_code/data.txt";
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

setInterval(loadJSON(1),600000);