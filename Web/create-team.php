    <?php
    include 'header.php';
        
    ?>
    <?
        $con = mysql_connect("localhost","lexidela_caps","password123");
            
            //check connecti
            if(!$con)
            {
                die('could not connect: '.mysql_error());//tells us the error
            }
            
            //select our database
            mysql_select_db("lexidela_iditarod",$con);        
       
    ?>
        <div class="content">
            <h1 class="create-team">Create Your Fantasy Iditarod Team</h1>
            <form>
                <table class="create-info">
                    <tr>
                        <td>Name</td>
                    </tr>
                    <tr>
                        <td><input type="text" id="fname" name="fname" placeholder="First Name" required="Required"/></td>
                        <td><input type="text" id="lname" name="lname" placeholder="Last Name" required="Required"/></td>
                    </tr>
                    <tr>
                        <td>Team Name</td>
                    </tr> 
                    <tr> 
                        <td><input type="text" name="teamName" id="teamname" placeholder="Choose a name" required="Required"/></td>
                        <td><span id="user-result"></span></td>
                    </tr>
                    <tr>
                        <td>Email</td>
                    </tr>
                    <tr>
                        <td><input type="email" id="email" name="email" placeholder="email@email.com" required="Required"/></td>
                    </tr>
                </table>

                    <h2>Choose your mushers:</h2>
                    <p>
                        Your team should have: </br>
                        <ul>
                            <li>Exactly 5 mushers</li>
                            <li> Only 1 <Span style = "background-color: #f90000a3"> Past Winner</span></li>
                            <li>At least 1 <span style = "background-color: #ffef69cf"> Rookie</span></li>
                            <li>At least 1 female (F)</li>
                        </ul>
                        
                    </p>
                    <br>
                    
                        <?php
                            echo"<div class='musher-container'>";

                            $mushers1 = mysql_query("SELECT * FROM musher WHERE past_winner = 1 ORDER BY gender, first_name;");
                            while($row=mysql_fetch_array($mushers1)) {
                                if($row['gender']=='0'){
                                    $gender = 'M';
                                }
                                else if($row['gender']=='1'){
                                    $gender = 'F';
                                }
                                else{
                                    echo "Error";
                                }
                                echo '<div class = "past-winner musher"> ';
                                echo ' <input type="checkbox" class="musher-check" name ="musher[]" value = "' . $row['mush_id'] . '" /> ';
                                echo $row['first_name'] . " " . $row['last_name'] . " (" . $gender . ")";
                                echo ' </div>';
                            }
                                
                            $mushers2 = mysql_query("SELECT * FROM musher WHERE rookie = 1 ORDER BY gender, first_name;");
                            while($row=mysql_fetch_array($mushers2)) {
                                if($row['gender']=='0'){
                                    $gender = 'M';
                                }
                                else if($row['gender']=='1'){
                                    $gender = 'F';
                                }
                                else{
                                    echo "Error";
                                }
                                echo '<div class = "rookie musher">';
                                echo ' <input type="checkbox" class="musher-check" name ="musher[]" value = "' . $row['mush_id'] . '" /> ';
                                echo $row['first_name'] . " " . $row['last_name'] . " (" . $gender . ")";
                                echo ' </div>';
                            }
                            
                            $mushers3 = mysql_query("SELECT * FROM musher WHERE rookie=0 AND past_winner = 0 ORDER BY first_name;");
                            while($row=mysql_fetch_array($mushers3)){
                                if($row['gender']=='0'){
                                    $gender = 'M';
                                }
                                else if($row['gender']=='1'){
                                    $gender = 'F';
                                }
                                else{
                                    echo "Error";
                                }
                                echo '<div class = "veteran musher">';
                                echo ' <input type="checkbox" class="musher-check" name ="musher[]" value = "' . $row['mush_id'] . '" /> ';
                                echo $row['first_name'] . " " . $row['last_name'] . " (" . $gender . ")";
                                echo ' </div>';
                            }
                            
                            echo ' </div> ';


                        mysql_close($con);
                        ?>
                    
                    <br>
                    <button class="create-submit">Submit</button>
                    <span class="error-message"></span>
                    
        </div>     
    </div>
<script type="text/javascript">

    var available;
    var filled;

    //submit team
    $('.create-submit').on('click', function (e) {
        e.preventDefault(); //so it doesn't submit automatically
        //If team is available, run ajax
        if (($("#fname").val()=='') || ($("#lname").val()=='') || ($("#email").val()=='')){
            filled = false;
        }
        else{
            filled = true;
        }
        

        if(available && filled)
        {
            $.ajax({
            type: "POST",
            url: "teamSubmit.php",
            data: $('form').serialize(),
            success: function(msg) {
            if(msg.result == "true") {
                //redirects to their team page
                var url = "teams.php?id=" + msg.id;
            window.location.href = url;
            }
            if(msg.result == "false") {
                    
                    $('.error-message').html("Error:" + msg.reason); 
                }
            }
        });}
        else if(!available){
            $('.error-message').html("Error: name is not available");
        }
        else{
            $('.error-message').html("Error: please fill in all fields");
        }

    }); //end submit

    //verify team name
    $('#teamname').keyup(function() {
        var potentialName = $('#teamname').val();
        var nameRegEx = /^[A-Za-z0-9\s]+$/.test(potentialName);
        console.log(nameRegEx);
        if(nameRegEx == 0){
            $("#user-result").html('<img src="Images/not-available.png" height = "10" width = "10" /><font size = "2" color = "red"> Username may not contain special characters</font>');
            available = false;
        }
        else{
            $.ajax({
            type: "POST",
            url: "teamNameChecker.php",
            data: { data: potentialName},
            success: function(msg) {
                console.log(msg.result);
            if(msg.result == "0") { 
                available = true;
                console.log("name is available");
                //displays checkmark and text when the name is available
                $("#user-result").html('<img src="Images/available.png" height= "10" width = "10" /><font size = "2" color = "green">  Available</font>');
                }

            else{ 
                available = false;
                console.log("name is taken");
                //displays red x and text when not available
                $("#user-result").html('<img src="Images/not-available.png" height = "10" width = "10" /><font size = "2" color = "red">  Taken</font>');
                }
            }    
            });
        }
        
    }); //end verify

    //Other code as needed
    $(".musher").click(function() {
        $(this).toggleClass("checked");
        var input = $(this).children();
        
        if (input[0].checked) {
            input[0].checked = false;
        }
        else {
            input[0].checked = true;
        }
        console.log(input[0].checked);
        
    }); //end musher click
$(".create-submit").hover(function() {
    $(this).addClass("hover");
}, function() {
    $(this).removeClass("hover");
});



    </script>
</body>
</html>