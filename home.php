<!DOCTYPE html>

<html>

<head>
    <style type="text/css">
        .main-content {
            width: 100%;
            max-width: 900px;
            background-color: #fffffd;
            height: 1000px;
            margin: 0 auto;
        }
        body {
            background-color: #331800;
        }
        .header {
            width: 100%;
            height: 200px;
        }
        .nav-bar {
            background-color: #1e2e08;
            height: 60px;
            color: white;
        }
        ul {
            text-align: center;
            margin: 0 auto;
            padding: 0;
        }
        li {
            display: inline-block;
            margin: 0 5px;
            
        }
        .nav-bar li a {
            display: block;
            padding: 5px 50px;
            text-decoration: none;
            color: white;
            padding: 21px;
            font-size: 16px;
            font-family: sans-serif;
        }
        .nav-bar a:hover {
            background-color: #aac0c5;
            color: #331800;
        }
        .content {
            width: 90%;
            margin: 0 auto;
        }
        table {
            border-collapse: collapse;
            font-size: 16px;
            width: 90%;
            margin: 0 auto;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
            }

        th {
            background-color: green;
            color: white;
            font-weight: 400;
            font-size: 18px;
            text-transform: uppercase;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        td:nth-child(-n+2) {
            text-align: center;
        }

        tr, td, th {
            border: 1px solid black;
            padding: 10px;
        }
        
    </style>
</head>

<body>
    <div class="main-content">
        <div class="header">
            <!-- Logo -->
        </div>
        <div class="nav-bar">
            <ul>
                <li><a href="#">Team List</a></li>
                <li><a href="#">Rules</a></li>
                <li><a href="#">Create Team</a></li>
                <li><a href="#">About</a></li>
            </ul>
        </div>

        <div class="content">
            <!-- Content goes here! -->
            
            <?php
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
            mysql_select_db("lexidela_iditarod-test", $con);

            
            ?>
    
        <table>
            <tr>
                <th>Rank</th>
                <th>Points</th>
                <th>Team Name</th>
                <th style="width: 45%">Mushers</th>
            </tr>

            <?php
                $leaderboard = mysql_query("SELECT t.tot_points as points, t.name as teamName, t1.name AS musher1, t2.name AS musher2, t3.name AS musher3, t4.name AS musher4, t5.name AS musher5
                FROM
                (SELECT team_id AS id, tot_points, name FROM team) t
                
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
                t4.id = t5.id");
                $counter = 1;
               while($row = mysql_fetch_array($leaderboard))
               {
                    echo "<tr>";
                    echo "<td>" . $counter . "</td>";
                    echo "<td>" . $row['points'] . "</td>";
                    echo "<td>" . $row['teamName'] . "</td>";
                    echo "<td>" . $row['musher1'] . ", " . $row['musher2'] . ", " . $row['musher3'] . ", " . $row['musher4'] . ", " . $row['musher5'] . "</td>";
                    echo "</tr>";
                    $counter ++;
               }
               
               //close connection
            mysql_close($con);

            ?>
        </table>


        </div>
            
    </div>
</body>
</html>