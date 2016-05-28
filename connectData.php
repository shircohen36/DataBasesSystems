<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

$conn = new mysqli("localhost","root","","music");

$result = $conn->query("SELECT name 
FROM musicgenre
");

$outp = "[";
while($rs = $result->fetch_array(MYSQLI_ASSOC)) {
    if ($outp != "[") {$outp .= ",";}
    $outp .= '{"name":"'  . $rs["name"] . '"}';
   
}
$outp .="]";

$conn->close();

echo($outp);
?>