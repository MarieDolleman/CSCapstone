<?php
function whichDay() {
    $d = new DateTime('');
   
    $regStart = new DateTime("2018-01-21 08:00:00");
    $raceStart = new DateTime("2018-03-04 00:00:01");
    $postSeason = new DateTime("2018-03-20");
    if ($d > $regStart and $d < $raceStart) {
        //registration period
        return 0;
    }
    else if ($d > $raceStart and $d < $postSeason) {
        //race period
        return 1;    
    }
    else {
        //post season
        return 2;
    }
}


?>