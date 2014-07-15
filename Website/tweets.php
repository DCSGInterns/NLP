<!DOCTYPE html>
<html>
<head>
	<title>iNSiGHTS</title>
	<link rel="icon" href="img/Dell2.ico" type="image/x-icon">
	
	<meta content="text/html; charset=utf-8" http-equiv="Content-Type">
	<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
	<!-- Bootstrap --> 
    <link href="css/bootstrap-select.css" rel="stylesheet" type="text/css" >
	<link href="css/bootstrap.min.css" rel="stylesheet" type="text/css">
	<!-- Specific Styling -->
	<link href="css/body.css" rel="stylesheet"  type="text/css">
    <link href="css/override.css" rel="stylesheet"  type="text/css">

    <script src="js/recent_tweet_loader.js" type="text/javascript"> </script>
    <script src="js/filter_tweets.js" type="text/javascript"> </script>

    <script type="text/javascript">
        if (window.location.search) {
            var string = window.location.search.substring(1);
            var array = string.split('=');
            var keyword = array[1].split('&')[0];
            /*   
            alert(array[2]);
            alert(array[3]);
            */
            var max_sentiment_val = array[2].split('&')[0];
            var min_sentiment_val = array[3];
        }
        else {
            keyword = 'default';
            var max_sentiment_val = 1;
            var min_sentiment_val = -1;
        }
    </script>

</head>

<body onload="loadJSON(keyword,max_sentiment_val,min_sentiment_val)">

    <!--Modal Information-->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
            <h4 class="modal-title" id="myModalLabel">How To?</h4>
          </div>
          <div class="modal-body">
            <h4>Filters - </h4> <hr/>
              <p>The maximum and minimum sentiment accept float values. The upper and lower limits are +1.0 and -1.0 respectively.
                  They can be increased/decreased with the default functionality in steps of 0.1</p>
              <p>The "Include data of" includes the data of specified number of days starting from today. It accepts whole number.
                  The upper limit is 180.</p><br/>
              <h4>Interpreting Results - </h4> <hr/>
              <p>The data displayed is heatmapped, with dark green representing most positive sentiment and red representig most negative sentiment</p>
          </div>
        </div>
      </div>
    </div>

    <!--The actual page header ------------------------------------------------------------------------------------- -->
	<?php include("inc/header.php")?>


    <!-- The page body content ---------------------------------------------------------------------------------------->
	<div class="container" id="phrases">
        <div class="row" id="properties_ctrl">
            <form class="form-inline" role="form" name="myForm">
                <div class="form-group">
                    <label>Max Sentiment : </label>
                    <input type="number" max="1" min="-1" step="0.1" value="1" class="form-control" name="max_sentiment" id="max_sentiment">
                </div>
                <div class="form-group">
                    <label>Min Sentiment : </label>
                    <input type="number" max="1" min="-1" step="0.1" value="-1" class="form-control" name="min_sentiment" id="min_sentiment">
                </div>
                <div class="form-group">
                    <label>Include Data of : </label>
                    <input type="number" max="180" min="0" value="180" class="form-control" name="data_of"> days
                </div>
                <div class="form-group">
                    <input type="button" class="form-control" value="FILTER" onclick="filter_JSON();">
                </div>
            </form>    
        </div>
        <div class="row" id="phrase_ctrl">
            <div class="col-lg-3 col-md-3 col-sm-3 col-xs-3" id="most_pos" onclick="sort_descending_sentiment(jsonObj)"><span class="glyphicon glyphicon-thumbs-up"></span> BEST SENTIMENT</div>
			<div class="col-lg-3 col-md-3 col-sm-3 col-xs-3" id="most_neg" onclick="sort_ascending_sentiment(jsonObj)"><span class="glyphicon glyphicon-thumbs-down"></span> WORST SENTIMENT</div>
		</div>
        <div id="tweets">
           
        </div>
	</div>
	
<script src="js/jquery.js" type="text/javascript"> </script>
<script src="js/jquery.min.js" type="text/javascript"> </script>
<script src="js/bootstrap-select.js" type="text/javascript"></script>
<script src="js/bootstrap.min.js" type="text/javascript"></script>
<script type="text/javascript">$('select').selectpicker();</script>
<script type="text/javascript">
    document.getElementById("max_sentiment").value = max_sentiment_val;
    document.getElementById("min_sentiment").value = min_sentiment_val;
</script>
</body>
</html>
