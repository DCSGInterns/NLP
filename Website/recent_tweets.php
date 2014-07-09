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
</head>

<body onload="loadJSON()">


    <!--The actual page header ------------------------------------------------------------------------------------- -->
	<?php include("inc/header.php")?>>


    <!-- The page body content ---------------------------------------------------------------------------------------->
	<div class="container" id="phrases">
        <div class="row" id="phrase_ctrl">
            <div class="col-lg-3 col-md-3 col-sm-3 col-xs-3" id="most_pos" onclick="sort_descending_sentiment(jsonObj)">MOST POSITIVE</div>
			<div class="col-lg-3 col-md-3 col-sm-3 col-xs-3" id="most_neg" onclick="sort_ascending_sentiment(jsonObj)">MOST NEGATIVE</div>
            <div class="col-lg-3 col-md-3 col-sm-3 col-xs-3" id="data_box">
                 <form class="form-inline" role="form">
                        <select class="selectpicker">
                                <option>Include Data Of</option>
                                <option>Past Hour</option>
                                <option>Past 2 Hours</option>
                                <option>Past 3 Hours</option>
                                <option>Past 4 Hours</option>
                                <option>Past Day</option>
                        </select>
                </form>
            </div>
		</div>
        <div id="tweets">
           
        </div>
	</div>
	
<script src="js/jquery.js" type="text/javascript"> </script>
<script src="js/jquery.min.js" type="text/javascript"> </script>
<script src="js/bootstrap-select.js" type="text/javascript"></script>
<script src="js/bootstrap.min.js" type="text/javascript"></script>
<script type="text/javascript">$('select').selectpicker();</script>
</body>
</html>
