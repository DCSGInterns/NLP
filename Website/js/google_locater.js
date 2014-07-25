var geocoder;
var map;

function codeAddress() {
    var address = "";
    geocoder.geocode( { 'address': address}, function(results, status) {
            //position: results[0].geometry.location
    });
}

google.maps.event.addDomListener(window, 'load', initialize);

function country_finder() { 
     //the json_obj is retrieved
    for (i = 0; i < json_location.length; i++)
    { 
        
    }
}

//return the json object from the database - ["id":***,"location":"*****"]
function loadLocation(){
    var data_file = "location_caller.php";
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

    http_request.open("GET",data_file,true);
    http_request.send();
    json_location = JSON.parse(http_request.responseText);
    country_finder();
}