<?php
$argument = $_GET["keyword"];
$max_sentiment = $_GET["max_sentiment"];
$min_sentiment = $_GET["min_sentiment"];
$date_diff = $_GET["date_diff"];
$command = "python py_code/tweet.py ".$argument." ".$max_sentiment." ".$min_sentiment." ".$date_diff." 2>&1";
$pid = popen( $command,"r");
$jsonObj = "";
while( !feof( $pid ) )  {
    $jsonObj = $jsonObj.fread($pid, 256);
}
ob_flush();
echo $jsonObj;
pclose($pid);
?>