# UTS Sistem Informasi Geografis
Aplikasi sistem informasi geografis berbasis web. Aplikasi ini memungkinkan pengguna menambahkan penanda pada suatu lokasi dipeta.

## Database setting
Gunakan aplikasi XAMPP lalu jalankan MySQL untuk membuat database dan menyimpan informasi penanda. Nama skema atau database bisa diubah pada file konfig_db.py jika terdapat duplikasi.

## Setup environment
Buka terminal sesuai path clone dan jalankan kode berikut:
```
pip install virtualenv
virtualenv [env_name]
[env_name]\Scripts\activate
pip install -r requirements.txt
```

## Run the app
Jalankan aplikasi dengan memanggil app.py menggunakan python
```
python app.py
```

## Default localhost
```
http://127.0.0.1:5000/
```
