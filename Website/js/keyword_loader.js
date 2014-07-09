var jsonObj;

function displayJSON(jsonObj)
{
  
}

function loadJSON(){
    var x = document.getElementById("content_wrapper_answer");
    x.innerHTML = "<img src=\"img/loading.gif\" style=\"width:600px;position:relative;left:30%;\">";
    var data_file = "keyword_caller.php"
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