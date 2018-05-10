<?php
header('Content-Type: application/json');

$con = mysqli_connect("localhost","lexidela_caps","password123", "lexidela_iditarod");
            
//check connecti
if(!$con){
    die('could not connect: '.mysqli_error());//tells us the error
}
            

$nametest = $_POST["data"];

$query = "SELECT * FROM `team` WHERE `name` = '$nametest' ";
$result = mysqli_query($con, $query);
    
$count = mysqli_num_rows($result);
    
$validate->result = $count;
    

//encode data and send it
$myJSON = json_encode($validate);
echo $myJSON;



mysqli_close($con);


?>