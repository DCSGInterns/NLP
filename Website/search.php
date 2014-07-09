<?php
 include("inc/submit.php");
?>

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
	<link href="css/search.css" rel="stylesheet"  type="text/css">
    <script type="text/javascript" src="js/keyword_loader.js"></script>

    <script type="text/javascript">
        function form_validate() {
            var data_of = document.forms["myForm"]["data_of"].value;
            var keyword = document.forms["myForm"]["keyword"].value;

            if (data_of == "" || keyword == "") {
                alert("Fill In all fields");
                return false;
            }
        }
    </script>
</head>

<body>


    <!--The actual page header ------------------------------------------------------------------------------------- -->
	<?php include("inc/header.php")?>>

    <!-- The page content -->
	<div id="search_panel">
        <div id="content_wrapper_search">
            <form class="form-inline" role="form" action="#" method="post" name="myForm" onsubmit="return form_validate();">
                <div class="form-group" id="search_box">
                    <label>Enter KeyWord</label>
                    <input type="text" class="form-control" name="keyword">
                </div>
                <div id="data_box">
                    <label>Include Data Of</label>
                    <select class="selectpicker" name="data_of">
                            <option>Month</option>
                            <option>3 Months</option>
                            <option>6 Months</option>
                            <option>12 Months</option>
                            <option>ALL</option>
                    </select>
                </div>
                <div class="form-group" id="submit">
                    <input type="Submit" class="form-control" name="submit">
                </div>
            </form>
        </div>
    </div>

   <div id="answer_panel">
        <div id="content_wrapper_answer">
            Sentiment   <br/>
            <span id="sentiment_content"><?php echo $matches_float[0]; ?></span><hr/>
            Count   <br/>
            <span id="count_content"><?php echo $matches_int[0]; ?></span><hr/>
        </div> 
    </div>

<script src="js/jquery.js" type="text/javascript"> </script>
<script src="js/jquery.min.js" type="text/javascript"> </script>

<script src="js/bootstrap-select.js" type="text/javascript"></script>

<script src="js/bootstrap.min.js" type="text/javascript"></script>

<script type="text/javascript">$('select').selectpicker();</script>
</body>
</html>

