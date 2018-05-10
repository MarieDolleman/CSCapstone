<?php

$con = mysql_connect("localhost", "lexidela_caps", "password123");
if(!$con)
{
    die('Could not connect: ' . mysql_error()); //tells error
}


mysql_select_db("lexidela_iditarod", $con);

$points = mysql_query("SELECT t.id as id, m1.tot_points AS m1points, m2.tot_points AS m2points, m3.tot_points AS m3points, m4.tot_points AS m4points, m5.tot_points AS m5points
FROM
((SELECT team_id AS id FROM team) t

LEFT JOIN
(SELECT team.team_id AS id, stats.tot_points FROM team JOIN stats WHERE team.mush_id1 = stats.mush_id) m1
ON
t.id = m1.id

LEFT JOIN
(SELECT team.team_id AS id, stats.tot_points FROM team JOIN stats WHERE team.mush_id2 = stats.mush_id) m2
ON
m1.id = m2.id

LEFT JOIN
(SELECT team.team_id AS id, stats.tot_points FROM team JOIN stats WHERE team.mush_id3 = stats.mush_id) m3
ON
m2.id = m3.id

LEFT JOIN
(SELECT team.team_id AS id, stats.tot_points FROM team JOIN stats WHERE team.mush_id4 = stats.mush_id) m4
ON
m3.id = m4.id

LEFT JOIN
(SELECT team.team_id AS id, stats.tot_points FROM team JOIN stats WHERE team.mush_id5 = stats.mush_id) m5
ON
m4.id = m5.id)");

while($row = mysql_fetch_array($points)) {
    $total = $row['m1points'] + $row['m2points'] + $row['m3points'] + $row['m4points'] + $row['m5points'];
    $sql = " UPDATE team SET tot_points = $total WHERE team_id = $row[id] ";
    mysql_query($sql);
}



echo '<!DOCTYPE html>

<html>

<head>
    <link href="style.css" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="UTF-8">
    <title>Fantasy Iditarod</title>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

</head>

<body>
    <div class="main-content">
        <div class="header">
            <!-- Logo -->
            <a href="index.php"><img src="Images/logo2.png" /></a>
        </div>
        <div class="nav-bar">
            <ul>
                <li><a href="teams.php">Team List</a></li>
                <li><a href="mushers.php">Mushers</a></li>
                <li><a href="rules.php">Rules</a></li>
                <li><a href="create-team.php">Create Team</a></li>
                <li><a href="about.php">About</a></li>
            </ul>
        </div>'
?>