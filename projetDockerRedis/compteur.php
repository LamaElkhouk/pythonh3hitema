<?php session_start();
require 'vendor/autoload.php';

Predis\Autoloader::register();

$redis = new Predis\Client();

if( isset($_SESSION['compteur']) ) {
	$_SESSION['compteur']++;
} else {
	$_SESSION['compteur'] = 1;
}
$redis->set("cpt",$_SESSION['compteur']);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>test docker et redis</title>
</head>
<p>Compteur de nombre de chargement dans une page : <?php echo $_SESSION['compteur'];?></p>
<p>reponse redis : <?= $redis->get("cpt");?></p>
<body>
    
</body>
</html>