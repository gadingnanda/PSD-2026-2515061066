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
