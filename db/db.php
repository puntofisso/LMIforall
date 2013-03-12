<?php

function mySQLquery($query) {

	$DB_HOST="lmiforall.alexbilbie.com";
	$DB_USER="data";
	$DB_PASS="Zjtb6QU39Q";
	$DB_NAME="lmiforall";

	mysql_connect($DB_HOST, $DB_USER, $DB_PASS) or die(mysql_error()." | HOST ".$DB_HOST." USER ".$DB_USER." PASS ".$DB_PASS ." NAME ".$DB_NAME." | Error on connect ");
	mysql_select_db($DB_NAME) or die(mysql_error()." | HOST ".$DB_HOST." USER ".$DB_USER." PASS ".$DB_PASS ." NAME ".$DB_NAME." | Error on select db ");

	$result = mysql_query("$query") or die(mysql_error()." | HOST ".$DB_HOST." USER ".$DB_USER." PASS ".$DB_PASS ." NAME ".$DB_NAME. " | Error on query " );  

// keeps getting the next row until there are no more to get
#while($row = mysql_fetch_array( $result )) {
#	// Print out the contents of each row into a table
#}
return $result; 
}


function parseJSON($url) {
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $output = curl_exec($ch);
        curl_close($ch); 
        $arr_ext = json_decode($output,true);


	return $arr_ext;

}

// Enter onetskills
function enter_onetkills() {
$url="http://api.lmiforall.org.uk/api/onet/skills";
$a = parseJSON($url);

foreach ($a as $elem) {
	$shortname = $elem['shortname'];
	$description = $elem['description'];
	$query = "INSERT INTO onetskills values ('$shortname', '$description');";
	$res = mySQLquery($query);
	print $res;
}
}


// Enter socs_onetskills
function enter_socskills() {
	$query = "SELECT code from socs";
	$res = mySQLquery($query);
	$socs = array();
	while($row = mysql_fetch_assoc( $res )) {
		$code = $row['code'];
		$socs[] = $code;
	}

	foreach ($socs as $soc) {
		
		// initial population
		//$querysoc = "REPLACE INTO socs_skills (`code`) VALUES ($soc);";
		//mySQLquery($querysoc);

		// query skills levels
		$levels = parseJSON("http://api.lmiforall.org.uk/api/onet/levels/$soc");
		// query skills importance
		$importance = parseJSON("http://api.lmiforall.org.uk/api/onet/importance/$soc");

		

		$levels_skills = $levels['skills'];	
		$levels_importance = $importance['skills'];



		for ($i=0;$i<10;$i++) {
			$thislevel = $levels_skills[$i];
			$thisimportance = $levels_importance[$i];
			$name = $thislevel['name'];
			$skill_importance = $thisimportance['score'];	
			$skill_importance_rank = $thisimportance['rank'];
			$skill_level = $thislevel['score'];
			$skill_level_rank = $thislevel['rank'];

			$insert = "INSERT INTO socs_skills VALUES('$soc','$name',$skill_importance,$skill_importance_rank,$skill_level,$skill_level_rank);";
			$csv = "'$soc','$name',$skill_importance,$skill_importance_rank,$skill_level,$skill_level_rank\n";
			//mySQLquery($insert);
			print $csv;
		}

	}
}


function create_ess() {
	$query = "SELECT code,title from socs";
        $res = mySQLquery($query);
        $socs = array();
        while($row = mysql_fetch_assoc( $res )) {
                $code = $row['code'];
		$title = $row['title'];
                $socs[$code] = $title;
        }

        foreach ($socs as $soc => $title) {

                // initial population
                //$querysoc = "REPLACE INTO socs_skills (`code`) VALUES ($soc);";
                //mySQLquery($querysoc);

                // query skills levels
                $ess = parseJSON("http://api.lmiforall.org.uk/api/ess/uk/$soc");

		$code = $ess['soc'];
		$percSSV = $ess['percentSSV'];
		$percHTF = $ess['percentHTF'];
		$percHTFSSV = $ess['percentHTFisSSV'];
		$reliability = $ess['reliability'];

		print "$code,\"$title\",$percSSV,$percHTF,$percHTFSSV,$reliability\n";
	}
}
//enter_socskills();
//create_ess();
?>
