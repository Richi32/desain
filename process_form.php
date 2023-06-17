<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Menerima data form dari input POST
    $name = $_POST["name"];
    $address = $_POST["address"];
    $email = $_POST["email"];
    $phone = $_POST["phone"];

    // Menjalankan shell script untuk memproses data
    $output = shell_exec("bash process_form.sh '$name' '$address' '$email' '$phone'");

    // Menampilkan hasil output dari shell script
    echo "<h1>Hasil Form</h1>";
    echo $output;
}
?>
