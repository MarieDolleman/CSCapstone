

    <?php
    include 'header.php';
    $con = mysql_connect("localhost", "lexidela_caps", "password123");
                if(!$con)
                {
                    die('Could not connect: ' . mysql_error()); //tells error
                }
                
                //choose database
                mysql_select_db("lexidela_iditarod", $con);
    ?>



        <div class="content">

            <?php
                $teamId = $_GET["id"];
                $teamInfo = mysql_query("SELECT * FROM team WHERE team_id = " . $teamId . ";");
    

                if(mysql_num_rows($teamInfo) == 1) {
                    // display team page
                    teamInfo($teamInfo);
                }
                else {
                    // display leaderboard
                    leaderboard();
                }

                function leaderboard() {
                    
                    echo "<table class='team-table'>
                    <tr>
                        <th>Rank</th>
                        <th>Points</th>
                        <th>Team Name</th>
                        <th style='width: 45%'>Mushers</th>
                    </tr>";
                    $leaderboard = mysql_query("SELECT t.id as id, t.tot_points as points, t.name as teamName, t1.name AS musher1, t2.name AS musher2, t3.name AS musher3, t4.name AS musher4, t5.name AS musher5
                    FROM
                    ((SELECT team_id AS id, tot_points, name FROM team) t
                    
                    LEFT JOIN
                    (SELECT team.team_id AS id, concat(musher.first_name, ' ', musher.last_name) AS name FROM team JOIN musher WHERE team.mush_id1 = musher.mush_id) t1
                    ON
                    t.id = t1.id
                    
                    LEFT JOIN
                    (SELECT team.team_id AS id, concat(musher.first_name, ' ', musher.last_name) AS name FROM team JOIN musher WHERE team.mush_id2 = musher.mush_id) t2
                    ON
                    t1.id = t2.id
                    
                    LEFT JOIN
                    (SELECT team.team_id AS id, concat(musher.first_name, ' ', musher.last_name) AS name FROM team JOIN musher WHERE team.mush_id3 = musher.mush_id) t3
                    ON
                    t2.id = t3.id
                    
                    LEFT JOIN
                    (SELECT team.team_id AS id, concat(musher.first_name, ' ', musher.last_name) AS name FROM team JOIN musher WHERE team.mush_id4 = musher.mush_id) t4
                    ON
                    t3.id = t4.id
                    
                    LEFT JOIN
                    (SELECT team.team_id AS id, concat(musher.first_name, ' ', musher.last_name) AS name FROM team JOIN musher WHERE team.mush_id5 = musher.mush_id) t5
                    ON
                    t4.id = t5.id)
                    ORDER BY t.tot_points DESC");
                    $counter = 1;
                    while($row = mysql_fetch_array($leaderboard))
                    {
                        echo "<tr class='musher-row' data-id=" . $row['id'] . " >";
                        echo "<td>" . $counter . "</td>";
                        echo "<td>" . $row['points'] . "</td>";
                        echo "<td>" . $row['teamName'] . "</td>";
                        echo "<td>" . $row['musher1'] . ", " . $row['musher2'] . ", " . $row['musher3'] . ", " . $row['musher4'] . ", " . $row['musher5'] . "</td>";
                        echo "</tr>";
                        $counter ++;
                    }
                    echo "</table>";
                } //end leaderboard

                function teamInfo($teamInfo) {
                    
                    while($row = mysql_fetch_array($teamInfo)) {
                        $teamName = $row['name'];
                        $teamPoints = $row['tot_points'];
                        $mush1 = $row['mush_id1'];
                        $mush2 = $row['mush_id2'];
                        $mush3 = $row['mush_id3'];
                        $mush4 = $row['mush_id4'];
                        $mush5 = $row['mush_id5'];  
                    }

                    echo "<h1 class='team-name'>" . $teamName . "</h1>";
                    
                    

                    //Add team info to HTML
                    $numStats = mysql_query("SELECT * FROM stats");
                    if(mysql_num_rows($numStats) > 0) {
                        echo "<p class='total-points'>Total points: " . $teamPoints . "</p>";
                    
                    
                    $musherInfo = mysql_query("SELECT stats.mush_id, stats.rank, stats.tot_points, concat(musher.first_name, ' ', musher.last_name) AS mush_name
                    FROM (stats
                    INNER JOIN musher ON
                    stats.mush_id = musher.mush_id)
                    WHERE stats.mush_id IN (" . $mush1 .", " . $mush2 . ", " . $mush3 . ", " . $mush4 . ", " . $mush5 . ")
                    ORDER BY stats.tot_points DESC");

                    echo '<table class="team-table">
                    <tr>
                    <th>Musher</th>
                    <th>Position</th>
                    <th>Points</th>
                    </tr>';
                
                    
                    while($row = mysql_fetch_array($musherInfo)) {
                        //add info to table
                        echo "<tr>";
                        echo "<td>" . $row['mush_name'] . "</td>" ;
                        echo "<td>" . $row['rank'] . "</td>";
                        echo "<td>" . $row['tot_points'] . "</td>";
                        echo "</tr>";
                    }

                    echo '</table>';
                }
                } //end teamInfo
                
               
                mysql_close($con);


            ?>
        </div>
            
    </div>

    <script>
    $(document).ready(function($) {
        $(".musher-row").click(function() {
            var urlID = $(this).data("id");
            window.location = "http://fantasy-iditarod.com/teams.php?id=" + urlID;
        });
    });
    </script>
</body>
</html>