Judul : Sistem nomor antrian
<br>
<br>
Deskripsi : <br>
Kode Python ini merupakan sebuah program implementasi sederhana untuk mengelola nomor antrian menggunakan struktur data Binary Search Tree (BST). 
Program ini menampilkan tampilan menu yang dapat digunakan oleh pengguna agar dapat memilih operasi yang diinginkan seperti menambah nomor antrian, menghapus nomor tertentu, mencari nomor antrian, serta menampilkan nomor antrian berikutnya dan sebelumnya.
Setiap data disimpan dalam bentuk node yang memiliki cabang kiri dan kanan sesuai aturan BST, sehingga proses pencarian dan pengelolaan data menjadi lebih terstruktur dan efisien.
<br>
<br>

<img width="292" height="120" alt="Screenshot 2026-05-21 191307" src="https://github.com/user-attachments/assets/1b70a475-7c47-4549-b2e0-558b3faf2dea" /><br>
Pada bagian ini program akan membuat kelas Node yang berfungsi sebagai tempat penyimpanan data pada struktur Binary Search Tree (BST). 
Setiap node memiliki atribut key untuk menyimpan nilai nomor antrian, serta left dan right yang digunakan untuk menunjuk node di sebelah kiri dan kanan.<br>
<br>
<br>

<img width="663" height="517" alt="Screenshot 2026-05-21 191502" src="https://github.com/user-attachments/assets/1b5c6aaa-f991-47ce-a100-0ba8cbead32c" /><br>
Class BSTLanjut adalah program utama yang berfungsi untuk mengelola serta mengatur seluruh operasi BST.
Fungsi __init__() digunakan untuk membuat root awal bernilai None. 
Fungsi insert_node() digunakan untuk menambahkan data baru ke dalam pohon sesuai aturan BST, yaitu nilai yang lebih kecil dari root akan ditempatkan di kiri dan nilai yang lebih besar di kanan, 
Fungsi insert() digunakan sebagai pemanggil utama agar pengguna lebih mudah menambahkan data.
Fungsi find_min_node() digunakan untuk mencari nilai terkecil dalam subtree dengan cara terus bergerak ke node paling kiri.<br>
<br>
<br>

<img width="750" height="744" alt="Screenshot 2026-05-22 172615" src="https://github.com/user-attachments/assets/4d7c3440-14b5-4831-a3c5-3a1ef95ec509" /><br>
Fungsi delete_node() digunakan untuk menghapus data dari BST dengan tiga kondisi utama, yaitu ketika node tidak memiliki anak, memiliki satu anak, atau memiliki dua anak. 
Jika node memiliki dua anak, maka program akan mencari pengganti menggunakan node terkecil dari subtree kanan.
Fungsi delete() berfungsi untuk memanggil fungsi delete_node() dari root utama.
Fungsi search_node() digunakan untuk mencari apakah suatu nomor antrian ada di dalam BST dengan teknik rekursif. 
Jika data ditemukan maka fungsi mengembalikan nilai True, sedangkan jika tidak ada akan mengembalikan False.
<br>
<br>

<img width="790" height="807" alt="Screenshot 2026-05-22 173035" src="https://github.com/user-attachments/assets/5fdd5f07-4766-447e-bd82-6050be327fae" /><br>
Fungsi search() berguna agar proses pencarian dapat dilakukan langsung dari root utama. 
Fungsi count_nodes() yang digunakan untuk menghitung jumlah seluruh node dalam BST secara rekursif, serta fungsi inorder() yang menampilkan isi BST secara terurut dari kecil ke besar menggunakan traversal inorder.
Fungsi find_successor() yang berfungsi mencari nomor antrian berikutnya dari suatu nilai tertentu, fungsi ini bekerja dengan mencari node yang memiliki nilai lebih besar terdekat.
<br>
<br>

<img width="534" height="534" alt="Screenshot 2026-05-22 173331" src="https://github.com/user-attachments/assets/6cdc7b12-9d30-41f6-80bb-d9406968cdfe" /><br>
Fungsi find_predecessor() digunakan untuk mencari nomor antrian sebelumnya, yaitu nilai yang lebih kecil terdekat dari data yang dicari.
<br>
<br>

<img width="422" height="230" alt="Screenshot 2026-05-22 173539" src="https://github.com/user-attachments/assets/c96cad59-800c-442c-bf87-bec3503cec27" /><br>
Fungsi main() berguna untuk menjalankan semua program. 
Di dalamnya terdapat menu yang dapat dipilih oleh pengguna dengan pilihan untuk memasukkan nomor antrian, menghapus nomor, mengecek nomor, dan keluar dari program.
<br>
<br>

<img width="282" height="66" alt="Screenshot 2026-05-15 150126" src="https://github.com/user-attachments/assets/ec71152c-03e6-4c76-8ad2-ceffa7d45ddf" /><br>
Kode if name == "main": digunakan untuk memastikan bahwa fungsi main() hanya dijalankan ketika file Python tersebut dieksekusi secara langsung, bukan saat file digunakan atau diimpor ke program lain sebagai module. 
Jika kondisi tersebut bernilai benar, maka program akan memanggil fungsi main() sehingga seluruh sistem antrian dapat dijalankan.
<br>
<br>

<img width="395" height="838" alt="Screenshot 2026-05-22 174725" src="https://github.com/user-attachments/assets/a591f3de-18c2-4df7-86b8-e8c86b5d37b6" /><br>
Output program ini menunjukkan proses pengelolaan nomor antrian menggunakan struktur data Binary Search Tree (BST). 
Awalnya pengguna memilih menu tambah nomor dan memasukkan angka 5, sehingga program menampilkan bahwa nomor berhasil dimasukkan dan isi antrian menjadi 5. 
Selanjutnya pengguna kembali menambahkan angka 2, lalu BST secara otomatis menyusun data sehingga urutan antrian menjadi 2 5 karena traversal inorder menampilkan data dari kecil ke besar. 
Setelah itu pengguna memasukkan angka 10 dan antrian berubah menjadi 2 5 10. 
Kemudian pengguna memilih menu hapus nomor dan menghapus angka 2. 
Program berhasil menghapus data tersebut, menampilkan jumlah nomor antrian yang tersisa sebanyak 2, serta menunjukkan isi antrian terbaru yaitu 5 10.
<br>
<br>

Link video : <br>
https://youtu.be/1IPA5gyegSk
