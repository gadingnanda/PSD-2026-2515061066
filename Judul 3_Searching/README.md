Judul : Pencarian Nomor Telepon Berdasarkan Nama <br>

<br>
Deskripsi : <br>
Program ini berfungsi untuk mencari nama di dalam sebuah array menggunakan metode sequential search atau pencarian berurutan. 
Program mencari nama dalam sebuah array secara berurutan, kemudian menampilkan nomor telepon jika nama ditemukan. 
Input pengguna juga divalidasi agar tidak berupa angka. Jika nama tidak ada dalam data, program akan menampilkan pesan bahwa nama tidak ditemukan. <br>

<br>
<br>
<br>
<img width="407" height="208" alt="Screenshot 2026-05-08 131830" src="https://github.com/user-attachments/assets/e581c779-9f3a-46de-b82b-41f0fe14b061" /> <br>
Fungsi ini merupakan fungsi sequential_search yang digunakan untuk mencari dan menghitung jumlah kemunculan suatu nilai target dalam sebuah list atau data. 
Fungsi bekerja dengan melakukan pencarian secara berurutan menggunakan perulangan while dari indeks pertama hingga terakhir. 
Jika elemen data sama dengan target, maka variabel counter akan bertambah satu. 
Setelah semua data diperiksa, fungsi mengembalikan jumlah kemunculan target yang ditemukan. <br>

<br>
<br>
<br>
<img width="702" height="750" alt="Screenshot 2026-05-08 131841" src="https://github.com/user-attachments/assets/e611c97a-58e1-43f0-b07b-684fd19634d9" />
Fungsi ini merupakan fungsi main() yang digunakan untuk menjalankan program pencarian nama dan nomor telepon. 
Program terlebih dahulu membuat daftar nama dalam sebuah array, kemudian menampilkan data tersebut kepada pengguna. 
Selanjutnya, program meminta input nama yang ingin dicari dan melakukan validasi agar input tidak berupa angka menggunakan try dan except. 
Setelah input valid, fungsi sequential_search() dipanggil untuk mengecek apakah nama tersebut ada di dalam data. 
Jika nama ditemukan, program akan menampilkan nomor telepon yang sesuai berdasarkan nama yang dipilih. 
Namun, jika nama tidak ditemukan, program akan menampilkan pesan bahwa nama tersebut tidak ada dalam data.<br>

<br>
<br>
<br>
<img width="517" height="72" alt="Screenshot 2026-05-08 133634" src="https://github.com/user-attachments/assets/12712d4d-1b46-428c-b3b6-44fca88bfa81" /><br>
Output program ini menunjukkan bahwa program berhasil menampilkan daftar nama yang tersedia di dalam array, yaitu Angga, Daffa, Riski, Nanda, dan Bima. 
Setelah itu, pengguna memasukkan nama Daffa pada bagian input pencarian. 
Program kemudian melakukan proses pencarian menggunakan fungsi sequential_search() dan menemukan bahwa nama tersebut ada di dalam data. 
Karena nama ditemukan, program menampilkan pesan bahwa nama Daffa berhasil ditemukan beserta nomor telepon yang sesuai, yaitu 082345678901.<br>
