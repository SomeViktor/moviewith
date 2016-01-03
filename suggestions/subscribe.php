<?php

$firstname = $_POST['firstname'] || '';
$lastname = $_POST['lastname'] || '';
$countries = isset($_POST['countries']) ? $_POST['countries'] : array();

$data = array('firstname' => $_POST['firstname'], 'lastname' => $_POST['lastname']);


?>
<html>
<head>
    <title></title>
</head>
<body>
    <p>Hello <?php echo $data['firstname']; ?> <?php echo $data['lastname'] ?>! <br/>
        You have selected: <?php print_r($countries) ?></p>

</body>
</html>
