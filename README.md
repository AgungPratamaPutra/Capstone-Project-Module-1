Sistem Data Pasien Rumah Sakit

Sistem ini adalah aplikasi sederhana berbasis Python yang digunakan untuk mengelola data pasien di rumah sakit. Aplikasi ini memungkinkan pengguna untuk melihat, menambah, mengupdate, dan menghapus data pasien dengan antarmuka yang sederhana. Program ini dibuat sebagai bagian dari tugas akhir module 1 dari program Job Connector Data Science Purwadhika Digital School. 

Sebelum menjalankan aplikasi ini, pastikan Anda telah menginstal:

    Python 3.x
    Library berikut:
        colorama
        tabulate

Fitur Tambahan 

1. Fitur GetPass
Program ini menggunakan fitur getpass untuk membedakan jenis user yaitu admin dan visitor.
Admin Features:
        Mengakses menu admin dengan memasukkan password.
        Melihat data pasien
        Menambah data pasien baru.
        Memperbaharui data pasien yang ada.
        Menghapus data pasien.
Visitor Features:
        Melihat data pasien

2. Fitur Validate
Program ini menggunakan fitur validasi untuk memastikan jenis kelamin dan golongan darah yang dimasukkan sesuai dengan format yang ditentukan.

Fitur Utama

1. Fitur Read
Fitur Read adalah fitur yang digunakan untuk melihat data pasien. Dalam program ini, fitur read dapat diakses oleh semua user(admin dan visitor).
Lihat Data Pasien:
     Melihat semua data pasien.
     Mencari data pasien berdasarkan ID.

2. Fitur Create
Fitur Create adalah fitur yang digunakan untuk menambahkan pasien. Dalam program ini, fitur create hanya dapat diakses oleh admin. Untuk menambah pasien, masukkan ID baru, nama, umur, jenis kelamin (M/F), dan golongan darah (A, B, AB, O).

3. Fitur Update
Fitur Update adalah fitur yang digunakan untuk memperbaharui data pasien. Dalam program ini, fitur update hanya dapat diakses oleh admin. Data yang dapat diperbaharui berupa nama, umur, jenis kelamin (M/F), dan golongan darah (A, B, AB, O). 

4. Fitur Delete
Fitur Delete adalah fitur yang digunakan untuk menghapus data pasien. Dalam program ini, fitur delete hanya dapat diakses oleh admin. Untuk menghapus data pasien dalam program dapat dilakukan dengan memasukkan ID pasien yang ingin dihapus dalam database pasien.

Catatan:
    Password default untuk admin adalah admin123. Anda dapat menggantinya sesuai kebutuhan.
    

Lisensi
Program ini bersifat open-source. Silakan gunakan dan modifikasi sesuai kebutuhan Anda.
