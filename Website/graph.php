<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>iNSiGHTS</title>
    <link rel="icon" href="img/Dell2.ico" type="image/x-icon">

    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Calling GOOGLE API -->
    <script type="text/javascript" src="//www.google.com/jsapi"></script>

    <!-- Bootstrap --> 
    <link href="css/bootstrap-select.css" rel="stylesheet" type="text/css" >
    <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css">
    <!-- Specific Styling -->
    <link href="css/header.css" rel="stylesheet"  type="text/css">
    <link href="css/graph.css" rel="stylesheet"  type="text/css">

    <script type="text/javascript" src="js/graph_loader.js"></script>
    <script type="text/javascript">
        json_array = [['Date', 'Sentiment']];
        for (i = 0; i < jsonObj.length; i++) {
            json_array.push([jsonObj[i].date, parseFloat(jsonObj[i].sentiment)]);
        }
        google.load("visualization", "1", { packages: ["corechart"] });
        google.setOnLoadCallback(drawChart);
        function drawChart() {
            var data = google.visualization.arrayToDataTable(json_array);

            var options = {
                title: 'Company Performance',
                hAxis: { title: 'Date', titleTextStyle: { color: '#333'} },
                vAxis: { minValue: -1, maxValue: 1 }
            };

            var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
            chart.draw(data, options);
        }
    </script>
    </script>
</head>

<body>
<div id="header_wrapper">
	<div id="header" class="container">
		<div id="header_links" class="row">
			<div class="col-lg-1 col-md-1 col-sm-1 col-xs-1" id="home"><a href="index.php">Home</a></div>
            <div class="col-lg-1 col-md-1 col-sm-1 col-xs-1" id="recent_tweets"><a href="tweets.php">Tweets</a></div>
            <div class="col-lg-1 col-md-1 col-sm-1 col-xs-1" id="search"><a href="search.php">Search</a></div>
            <div class="col-lg-1 col-md-1 col-sm-1 col-xs-1" id="search"><a href="">Plots</a></div>
            <div class="col-lg-1 col-md-1 col-sm-1 col-xs-1" id="search"><a href="map.php">Heat Map</a></div>
            <div class="col-lg-2 col-md-2 col-sm-2 col-xs-2" id="search"></div>
			<div class="col-lg-4 col-md-4 col-sm-4 col-xs-4" id="title">
				<img src="img/dell_bg.jpg" id="dell_logo"  alt="Dell Logo">
                <span>Insights</span>
			</div>
		</div>
	</div>
</div>

<div id="chart_div">
</div>

</body>
</html>
