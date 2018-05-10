<!-- name, points, position, checkpoint -->

<?php
    include 'header.php';
    $con = mysql_connect("localhost", "lexidela_caps", "password123");
        if(!$con)
        {
            die('Could not connect: ' . mysql_error()); //tells error
        }
        // else
        // {
        //     print("Connection established" . "<br/>");
        // }
        
        //choose database
        mysql_select_db("lexidela_iditarod", $con);
?>

<!-- <div class="content"> -->

<?php
       
       echo"<br/>";
       echo "<br/>";

       echo '<table class="musher-table">
        <tr>
        <th>Rank</th>
        <th>Musher</th>
        <th>Points</th>
        <th>Checkpoint</th>
        </tr>';
       //size of stats
       //if size > 0

       $numStats = mysql_query("SELECT * FROM stats");
        if(mysql_num_rows($numStats) > 0) {
            $musherInfo = mysql_query("SELECT stats.mush_id, stats.tot_points, stats.checkpoint, concat(musher.first_name, ' ', musher.last_name) AS mush_name
        FROM (stats
        INNER JOIN musher ON
        stats.mush_id = musher.mush_id)
        -- WHERE stats.mush_id IN (" . $mush1 .", " . $mush2 . ", " . $mush3 . ", " . $mush4 . ", " . $mush5 . ")
        ORDER BY stats.tot_points DESC");

        $rank = 1;

        while($row = mysql_fetch_array($musherInfo)) {
            //add info to table
            echo "<tr>";
            echo "<td>" . $rank . "</td>";
            echo "<td><b>" . $row['mush_name'] . "</b></td>" ;
            echo "<td>" . $row['tot_points'] . "</td>";
            echo "<td>" . $row['checkpoint'] . "</td>";
            echo "</tr>";
            $rank = $rank + 1;
        }

        echo '</table>';
        }
        else {
            $nameInfo = mysql_query("SELECT concat(musher.first_name, ' ', musher.last_name) AS mush_name
        FROM musher ");

        while($row = mysql_fetch_array($nameInfo)) {
            echo "<tr>";
            echo "<td> - </td>";
            echo "<td><b>" . $row['mush_name'] . "</b></td>" ;
            echo "<td> 0 </td>";
            echo "<td> Anchorage </td>";
            echo "</tr>";
        }
        }
       
    
    //} //end teamInfo
    
   
    mysql_close($con);


?>
<!-- </div> -->
</div>

</body>
</html>