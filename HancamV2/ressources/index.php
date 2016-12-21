<?php

	 $user = "root";
    $pass = "";
    $host = "localhost";
    $db_name = "test";

     $id = mysql_connect($host, $user, $pass);
	  if($id){
       //Connexion à la base
       mysql_select_db($db_name, $id);
      //Requete
      $req = "SELECT * FROM etudiants";

      $result = mysql_query($req);
?>

<html>
	<head>
	   <meta charset="UTF-8">
	   <meta name="viewport" content="width=device-width, initial-scale=1">
		<title>HaniCam</title>
		<link rel="stylesheet" type="text/css" href="bootstrap.css"></link>
	</head>
	
	<body>
		<h1>WELCOME</h1>
		
		<table class="table">
			<thead>
				<tr>
					<td>ID</td>
					<td>NOM ETUDIANT</td>
					<td>ABSCENCE</td>
				</tr>
			</thead>
			
			<tbody>
				<?php while($row = mysql_fetch_array($result)){  ?>
				<tr class="danger">
					<td><?php echo $row['id']; ?></td>
					<td><?php echo $row['nom']; ?></td>
					<td><?php echo $row['absence']; ?></td>
				</tr>
				<?php } ?>
				
			</tbody>
		</table>
		
		<fieldset id="d">
			<legend>Data</legend>
		</fieldset>
		
		<script src="http://code.jquery.com/jquery-latest.min.js"></script>
 	   <script src="/socket.io/socket.io.js"></script>
		<script>
		jQuery(function($)
		{
 	 	   var socket = io();
  			var $field = $('#d');
			
 		   socket.emit('log', "I am now Connected Server");
		 
  			socket.on('data', function(info)
  			{
    			$field.append(info.donne + "<br/>");
			});

		});
		</script>
  </body>	
</html>
