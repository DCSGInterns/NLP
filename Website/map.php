<!--
You are free to copy and use this sample in accordance with the terms of the
Apache license (http://www.apache.org/licenses/LICENSE-2.0.html)
-->

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
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
  <link href="css/map.css" rel="stylesheet"  type="text/css">

  <script src="js/data_loader.js" type="text/javascript"></script>
  <script src="js/filter.js" type="text/javascript"></script>
</head>

<body>
<div id="header_wrapper">
	<div id="header" class="container">
		<div id="header_links" class="row">
			<div class="col-lg-1 col-md-1 col-sm-1 col-xs-1" id="home"><a href="index.php">Home</a></div>
            <div class="col-lg-1 col-md-1 col-sm-1 col-xs-1" id="recent_tweets"><a href="tweets.php">Tweets</a></div>
            <div class="col-lg-1 col-md-1 col-sm-1 col-xs-1" id="search"><a href="search.php">Search</a></div>
            <div class="col-lg-1 col-md-1 col-sm-1 col-xs-1" id="search"><a href="graph.php">Plots</a></div>
            <div class="col-lg-1 col-md-1 col-sm-1 col-xs-1" id="search"><a href="map.php">Heat Map</a></div>
            <div class="col-lg-2 col-md-2 col-sm-2 col-xs-2" id="search"></div>
			<div class="col-lg-4 col-md-4 col-sm-4 col-xs-4" id="title">
				<img src="img/dell_bg.jpg" id="dell_logo"  alt="Dell Logo">
                <span>Insights</span>
			</div>
		</div>
	</div>
</div>

<!--
<div id="loading">
    <img alt="loading" src="img/loading.gif">
</div>
-->

<div id="visualization">
    <script type="text/javascript">
      google.load('visualization', '1', { packages: ['geochart'] });
      function drawVisualization() {
          var data = google.visualization.arrayToDataTable([
          ['Country', 'Sentiment'],
          ['United States', 0.6],
          ['Canada', -0.4],
          ['France', 0.3],
          ['India',-0.8],
          ['Russia',0.1]
        ]);

          var options = {
              colorAxis: { minValue: -1, maxValue: 1, colors: ['red', 'green'] },
              backgroundColor: '#d2fbf5',
              magnifyingGlass: { enable: true, zoomFactor: 7.5 }
          };

          var geochart = new google.visualization.GeoChart(
            document.getElementById('visualization'));
          geochart.draw(data, options);
      }
      google.setOnLoadCallback(drawVisualization);
  </script>
</div>

<div id="disclaimer">
    <p>The location of a tweet may not always be available. It depends on the privacy settings of the user. So the sentiment represented here may not involve all
    the tweets used on the home page. This is based on tweets whose loaction could be resolved.</p>
</div>

</body>
</html>