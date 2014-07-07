function loadJSON(){
    
    var data_file = "../py_code/filtered.txt"
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
            var jsonObj = JSON.parse(http_request.responseText);
            var x = document.getElementById("tweet_content");
            for (i=0;i<jsonObj.length;i++) {
                x.innerHTML = x.innerHTML + "<div class=\"row\"><div class=\"col-lg-11 col-md-11 col-sm-11 col-xs-11\">" + jsonObj[i].text + "</div></div>";
            }
            // jsonObj variable now contains the data structure and can
            // be accessed as jsonObj.name and jsonObj.country.
        }
    }

    http_request.open("GET",data_file,true);
    http_request.send();
}

loadJSON();

