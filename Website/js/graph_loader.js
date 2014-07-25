window.jsonObj = "";

function loadJSON(){
    var data_file = "graph_caller.php";
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

    /*
    http_request.onreadystatechange = function () {
        if (http_request.readyState == 4) {
            // Javascript function JSON.parse to parse JSON data
            window.jsonObj = JSON.parse(http_request.responseText);
            CreatJSON();
        }

    }
    */
    http_request.open("GET",data_file,false);
    http_request.send();
    window.jsonObj = JSON.parse(http_request.responseText);
}

loadJSON();