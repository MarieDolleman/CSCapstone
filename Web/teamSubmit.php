<?php 

header('Content-Type: application/json'); //needed if dealing with json data



$con = mysql_connect("localhost","lexidela_caps","password123");
            
//check connecti
if(!$con){
    die('could not connect: '.mysql_error());//tells us the error
}
            
//select our database
mysql_select_db("lexidela_iditarod",$con);



$fname = $_POST["fname"];
$lname = $_POST["lname"];
$teamName = $_POST["teamName"];
$email = $_POST["email"];
$mushers = array();

// Add all mushers to an array
foreach($_POST['musher'] as $musher) {
    $mushers[] = $musher;
}


//SQL query to get rookie, woman, and past winner info from database
//For each row, add to count of rookie, past winner, and woman

$women = 0;
$rookies = 0;
$past = 0;

if(count($mushers) != 5) {
    $validate->result = "false";
    if(count($musher) > 5) {
        $validate->reason = "You can only have 5 mushers on your team";
    }
    else {
        $validate->reason = "You need 5 mushers on your team";
    }
    
}
else {
    $musher_info = mysql_query(" SELECT mush_id, gender, past_winner, rookie FROM musher WHERE mush_id IN ($mushers[0], $mushers[1], $mushers[2], $mushers[3], $mushers[4]) ");
    while($row=mysql_fetch_array($musher_info)) {

        if ($row['gender'] == '1') { 
            $women = $women + 1; 
        }
        if ($row['past_winner'] == '1') { 
            $past = $past + 1;
        }
        if ($row['rookie'] == '1') { 
            $rookies = $rookies + 1; 
        }
    }
    if($women > 0 AND $rookies > 0 && $past < 2) {
        $validate->result = "true";
        $sql = "INSERT INTO team(`name`, `email`, `first_name`, `last_name`, `mush_id1`, `mush_id2`, `mush_id3`, `mush_id4`, `mush_id5`) VALUES ('$teamName', '$email', '$fname', '$lname', '$mushers[0]', '$mushers[1]', '$mushers[2]', '$mushers[3]', '$mushers[4]')";
        mysql_query($sql);

        $id = mysql_insert_id();

        $validate->id = $id;

        //Send email here
        $to = $email;
        $subject = "Thank you for creating a team!";
        $message = "Your fantasy team has been successfully created!" . "\r\n" . "Your unique team link is fantasy-iditarod.com/teams.php?id=" . $id;
        $headers = "From: success@fantasy-iditarod.com";
        //send the email using mail function
        mail($to, $subject, $message, $headers);

        
    }
    else {
        $validate->result = "false";
        if($past > 1) {
            $validate->reason = "You can only have 1 past winner on your team";
        }
        else if($women < 1) {
            $validate->reason = "You need at least 1 woman on your team";
        }
        else if($rookies < 1) {
            $validate->reason = "You need at least 1 rookie on your team";
        }
        
         
    }
}




//Return data
$myJSON = json_encode($validate);
echo $myJSON;


mysql_close($con);

?>

