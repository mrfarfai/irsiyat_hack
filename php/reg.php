<?php 
	require 'config.php';
	if(isset($_POST["reg_btn"])) {
		$name = trim($_POST["name"]);
		$surname = trim($_POST["surname"]);
		$nikname = trim($_POST["nikname"]);
		$phone = trim($_POST["phone"]);
		$email = trim($_POST["email"]);

		mysqli_query($conn, "INSERT INTO `user` (`name`, `surname`, `nikname`, `phone`, `email`, `reg_date`) VALUES ('$name', '$surname', '$nikname', '$phone', '$email', NOW());");

		$res = mysqli_fetch_assoc(mysqli_query($conn, "SELECT `id` from `user` WHERE
			`name` = '$name' and
			`surname` = '$surname' and
			`nikname` = '$nikname' and
			`phone` = '$phone' and
			`email` = '$email'
			ORDER BY `id` DESC LIMIT 1;
			"));

		move_uploaded_file($_FILES['photo']['tmp_name'], '../templets/img/user/'.$res["id"].'.png');

		shell_exec("action.py ".$res['id']." 1");
		
		header('location: /templets/register.php.');
	}
?>