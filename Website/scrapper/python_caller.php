<?php
#exec("TwitConsole.exe");
$command = "python ../py_code/sentiment.py 180 2>&1";
$pid = popen( $command,"r");
$jsonObj = "";
while( !feof( $pid ) )  {
    $jsonObj = $jsonObj.fread($pid, 256);
}
ob_flush();
echo $jsonObj;
pclose($pid);
?>