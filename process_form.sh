#!/bin/bash

# Menerima data form dari input POST
read -r name
read -r address
read -r email
read -r phone

# Menampilkan hasil input
echo "<h1>Hasil Form</h1>"
echo "<p>Nama: $name</p>"
echo "<p>Alamat: $address</p>"
echo "<p>Email: $email</p>"
echo "<p>Nomor Telepon: $phone</p>"
