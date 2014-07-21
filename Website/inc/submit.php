<?php
$submit=@$_POST['submit'];
$data_of = @$_POST['data_of'];
$keyword = htmlspecialchars(@$_POST['keyword']);

$pattern_float = '/[+-]?[0-9]+\.[0-9]+/';
$pattern_int = '/[0-9]+/';
if($submit)
{
    if($data_of && $keyword)
    {
        $command = "python py_code/word_search.py $keyword $data_of 2>&1";
        $pid = popen( $command,"r");
        $jsonObj = "";
        while( !feof( $pid ) )  {
            $jsonObj = $jsonObj.fread($pid, 256);
        }
        preg_match($pattern_int, $jsonObj, $matches_int);
        preg_match($pattern_float, $jsonObj, $matches_float);
        pclose($pid);

    } 
    else
    {
        echo "<span style=\"
			     position:absolute;
			     top:19%;
			     left:32%;
			     font-size:22px;
			     font-weight : bold;
			     font-family:Agency FB
			     \">Fill In Field</span>";
    }
}

?>