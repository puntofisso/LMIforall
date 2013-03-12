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
$url="http://api.lmiforall.org.uk/api/onet/skills";
$a = parseJSON($url);

foreach ($a as $elem) {
	$shortname = $elem['shortname'];
	$description = $elem['description'];
	$query = "INSERT INTO onetskills values ('$shortname', '$description');";
	$res = mySQLquery($query);
	print $res;
}

// Enter socs_onetskills

?>
