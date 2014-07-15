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
    <link href="css/body.css" rel="stylesheet"  type="text/css">
	<link href="css/search.css" rel="stylesheet"  type="text/css">
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

    <!--Modal Information-->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
            <h4 class="modal-title" id="myModalLabel">How To?</h4>
          </div>
          <div class="modal-body">
            <h4>Search - </h4> <hr/>
              <p>The search carried out is case insenstive. The "Include Data Of" includes the tweets for the number of days entered strating from today
              and counting backwards.</p>
              <h4>Interpreting Results - </h4> <hr/>
              <p>The sentiment values ranges from -1.0 (most negative) to 1.0 (most positive)</p>
              <p>The count field indicates number of occurences of the keyword.</p>

              <p></p>
          </div>
        </div>
      </div>
    </div>

    <!--The actual page header ------------------------------------------------------------------------------------- -->
	<?php include("inc/header.php")?>

    <!-- The page content -->
	<div id="search_panel">
        <div id="content_wrapper_search">
            <form class="form-inline" role="form" action="#" method="post" name="myForm" onsubmit="return form_validate();">
                <div class="form-group">
                    <label>Enter Keyword : </label>
                    <input type="text" class="form-control" name="keyword">
                </div>
                <div class="form-group">
                    <label>Include Data of : </label>
                    <input type="number" max="180" min="0" value="180" class="form-control" name="data_of"> days
                </div>
                <br/>
                <div class="form-group" id="submit">
                    <input type="Submit" class="form-control" name="submit">
                </div>
            </form>
        </div>
    </div>

   <div id="answer_panel">
        <div id="content_wrapper_answer">
            Keyword : <br/> <span id="keyword_content"><?php echo $keyword; ?></span><hr/>
            Sentiment : <br/> <span id="sentiment_content"><?php echo $matches_float[0]; ?></span><hr/>
            Count : <br/> <span id="count_content"><?php echo $matches_int[0]; ?></span><hr/>
        </div> 
    </div>

<script src="js/jquery.js" type="text/javascript"> </script>
<script src="js/jquery.min.js" type="text/javascript"> </script>

<script src="js/bootstrap-select.js" type="text/javascript"></script>

<script src="js/bootstrap.min.js" type="text/javascript"></script>

<script type="text/javascript">$('select').selectpicker();</script>
</body>
</html>

