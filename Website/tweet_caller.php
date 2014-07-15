<?php
$argument = $_GET["keyword"];
$max_sentiment = $_GET["max_sentiment"];
$min_sentiment = $_GET["min_sentiment"];
$command = "python py_code/tweet_sentiment.py ".$argument." ".$max_sentiment." ".$min_sentiment." 2>&1";
$pid = popen( $command,"r");
$jsonObj = "";
while( !feof( $pid ) )  {
    $jsonObj = $jsonObj.fread($pid, 256);
}
ob_flush();
echo $jsonObj;
pclose($pid);
?>