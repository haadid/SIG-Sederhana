# UTS Sistem Informasi Geografis
Pembuatan aplikasi sistem informasi geografis berbasis web. Aplikasi ini memungkinkan pengguna menambahkan penanda pada suatu lokasi dipeta.

<br>

## Database setting
Gunakan aplikasi XAMPP lalu jalankan MySQL. Buka MySQL melalui shell atau aplikasi lainnya. <br>
Untuk membuat database penyimpanan data penanda, <br>
Jalankan query berikut:
```
CREATE DATABASE IF NOT EXISTS gis_database;

USE gis_database;

CREATE TABLE IF NOT EXISTS lokasi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(255) NOT NULL,
    latitude DOUBLE NOT NULL,
    longitude DOUBLE NOT NULL
);
```

<br>

## Setup environment
Buka terminal sesuai path clone dan jalankan kode berikut:
```
virtualenv [env_name]
[env_name]\Scripts\activate
pip install -r requirements.txt
```

<br>

## Run the 
Jalankan aplikasi dengan memanggil app.py menggunakan python
```
python app.py
```

## Default localhost
```
http://127.0.0.1:5000/
```
