<?php include 'header.php'; ?>

<div class="content">
            
            
<?php
    $con = mysql_connect("localhost", "lexidela_caps", "password123");
    if(!$con)
    {
        die('Could not connect: ' . mysql_error()); //tells error
    }
            
    mysql_select_db("lexidela_iditarod", $con);

           
    ?>

        <h1>Welcome to Fantasy Iditarod!</h1>
        <p>Fantasy Iditarod is a league for Iditarod lovers to create their own teams of mushers and compete to see who can create the team that accumulates the most points. To see a breakdown of how points are calculated, check out the <a href="rules.php">rules page</a>.</p>
        <p></p>
        <h2>Top 10 Teams</h2>
        <table class="team-table">
            <tr>
                <th>Rank</th>
                <th>Points</th>
                <th>Team Name</th>
                <th style="width: 45%">Mushers</th>
            </tr>

            <?php
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
                //add order by
                $counter = 1;
               while($row = mysql_fetch_array($leaderboard))
               {
                   if($counter <= 10) {
                        echo "<tr class='musher-row' data-id=" . $row['id'] . " >";
                        //echo "<tr>";
                        echo "<td>" . $counter . "</td>";
                        echo "<td>" . $row['points'] . "</td>";
                        echo "<td>" . $row['teamName'] . "</td>";
                        echo "<td>" . $row['musher1'] . ", " . $row['musher2'] . ", " . $row['musher3'] . ", " . $row['musher4'] . ", " . $row['musher5'] . "</td>";
                        echo "</tr>";
                        $counter ++;
                   }
               }
               
               //close connection
            mysql_close($con);

            ?>
        </table>

        <a class="cta-link" href="create-team.php"><div class="cta-button">Create Your Team</div></a>


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