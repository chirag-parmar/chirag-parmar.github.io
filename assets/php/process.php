<?php
if($_POST){
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];

//send email
    mail("chiragparmar12209@gmail.com", "This is an email from:" .$email, $message);
}
?>
