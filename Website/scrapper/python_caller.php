<?php
//exec("TwitConsole.exe");

if(is_null( $_GET["date_diff"]))
    $argument = 180;
else
    $argument = $_GET["date_diff"];

$command = "python ../py_code/sentiment.py ".$argument." 2>&1";
$pid = popen( $command,"r");
$jsonObj = "";
while( !feof( $pid ) )  {
    $jsonObj = $jsonObj.fread($pid, 256);
}
ob_flush();
echo $jsonObj;
pclose($pid);
?>