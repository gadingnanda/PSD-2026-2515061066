Judul : Sistem pengelolaan data berbasis Hash Map <br>
<br>
<br>
Deskripsi : <br>
Program ini merupakan implementasi struktur data dari Hash Map atau Hash Table yang menggunakan metode Open Addressing dengan Linear Probing. 
Program ini memungkinkan pengguna untuk menambahkan, mencari, menghapus, dan menampilkan data dalam bentuk pasangan key-value melalui menu utama. 
Untuk mengatasi terjadinya collision atau tabrakan data, program menggunakan teknik pencarian slot berikutnya secara berurutan hingga menemukan posisi yang tersedia. 
Selain itu, setiap slot memiliki status EMPTY, OCCUPIED, atau DELETED untuk memudahkan pengelolaan data dalam hash table.<br>
<br>
<br>
<img width="431" height="281" alt="Screenshot 2026-06-08 153827" src="https://github.com/user-attachments/assets/abf92810-617d-47b3-a1a6-9c878409a63e" /><br>
Class SlotState, digunakan sebagai tempat penyimpanan yang merepresentasikan kondisi setiap slot pada hash table. 
Class ini memiliki tiga status, yaitu EMPTY (slot kosong dan belum pernah digunakan), OCCUPIED (slot sedang menyimpan data), dan DELETED (slot pernah digunakan tetapi datanya telah dihapus).<br>
Class Entry, berfungsi sebagai representasi dari suatu slot dalam hash table. 
Setiap objek Entry menyimpan tiga informasi utama, yaitu key sebagai kunci data, value sebagai nilai yang terkait dengan key tersebut, dan state yang menunjukkan kondisi slot.<br>
<br>
<br>
<img width="696" height="807" alt="Screenshot 2026-06-08 154226" src="https://github.com/user-attachments/assets/95362ddd-7a21-4b6e-8b46-85118aa8c048" /><br>
Class HashMapOpenAddressing, merupakan class utama yang mengimplementasikan struktur data Hash Map menggunakan metode Open Addressing dengan Linear Probing. 
Class ini bertanggung jawab untuk mengelola seluruh operasi pada hash table.<br>
Fungsi __init__(), berfungsi untuk membuat hash table dengan ukuran tertentu, yang secara default berjumlah 15 slot. 
Selain menyimpan ukuran tabel pada variabel SIZE, fungsi ini juga membuat daftar list yang berisi objek-objek Entry sebagai tempat penyimpanan data dalam hash table.<br>
Fungsi hash_function() digunakan untuk menghitung indeks atau posisi penyimpanan data berdasarkan nilai key yang diberikan. 
Perhitungan dilakukan menggunakan operasi modulo terhadap ukuran hash table sehingga indeks yang dihasilkan selalu berada dalam rentang yang valid.<br>
Fungsi insert(), bertugas untuk menambahkan data baru ke dalam hash table. 
Pertama, fungsi akan menghitung indeks menggunakan hash function. 
Jika slot yang dituju sudah terisi oleh data lain, maka program akan melakukan Linear Probing, yaitu mencari slot berikutnya secara berurutan hingga menemukan slot kosong atau slot yang telah dihapus.<br>
<br>
<br>
<img width="864" height="683" alt="Screenshot 2026-06-08 154828" src="https://github.com/user-attachments/assets/169901d8-c839-4c4b-a197-2bc4bc787129" /><br>
Fungsi search(), digunakan untuk mencari data berdasarkan key yang dimasukkan pengguna. 
Pencarian dimulai dari indeks hasil hash function dan dilanjutkan secara berurutan menggunakan Linear Probing.<br>
Fungsi remove_key(), berfungsi untuk menghapus data dari hash table. 
Prosesnya dimulai dengan mencari data menggunakan fungsi search(). Jika data ditemukan, status slot tidak langsung dikosongkan, tetapi diubah menjadi DELETED.<br>
Fungsi display(), digunakan untuk menampilkan seluruh isi hash table ke layar. 
Program akan menampilkan nomor indeks setiap slot beserta statusnya, yaitu EMPTY jika kosong, DELETED jika data telah dihapus, atau isi jika slot berisi data.<br>
<br>
<br>
<img width="806" height="829" alt="Screenshot 2026-06-08 155331" src="https://github.com/user-attachments/assets/3b3c706f-cc68-4470-a5a8-0141659f649d" /><br>
Fungsi main(), merupakan pusat dari program yang mengatur interaksi dengan pengguna melalui menu. 
Di dalam fungsi ini terdapat perulangan yang terus berjalan hingga pengguna memilih keluar dari program. 
Pengguna dapat memilih berbagai operasi seperti menambah data, mencari data, menghapus data, atau menampilkan isi hash table. 
Selain itu, fungsi ini juga menangani kesalahan input menggunakan try-except sehingga program tidak langsung berhenti jika pengguna memasukkan data yang tidak valid.<br>
<br>
<br>
<img width="455" height="718" alt="Screenshot 2026-06-08 155616" src="https://github.com/user-attachments/assets/b4bd32fd-11ed-4d6a-892f-755c5cb5dd94" /><br>
<img width="500" height="814" alt="Screenshot 2026-06-08 155731" src="https://github.com/user-attachments/assets/ced3bea8-a84d-48c0-bde3-b22effef29fc" /><br>
Pada output awal program, pengguna memilih menu Insert (1) dan memasukkan key = 12 serta value = 2550. 
Program kemudian berhasil menyimpan data tersebut ke dalam hash table dan menampilkan pesan "Data (12, 2550) berhasil dimasukkan". 
Setelah itu, pengguna kembali memilih menu Insert (1) untuk menambahkan data kedua dengan key = 1 dan value = anggur. 
Data tersebut juga berhasil disimpan dan ditampilkan pesan konfirmasi bahwa data berhasil dimasukkan.<br>
Selanjutnya, pengguna memilih menu Search (2) dan memasukkan key = 12. 
Program menjalankan fungsi pencarian dengan menghitung indeks hash dari key tersebut dan memeriksa slot yang sesuai pada hash table. 
Karena data ditemukan, program menampilkan pesan "Key 12 ditemukan, value = 2550", yang menunjukkan bahwa pasangan key-value tersebut berhasil ditemukan.
Kemudian pengguna memilih menu Display (4) untuk melihat seluruh isi hash table. 
Hasil yang ditampilkan menunjukkan bahwa sebagian besar slot masih berstatus EMPTY, yang berarti belum berisi data. Pada indeks 1 terdapat data (1, anggur), sedangkan pada indeks 12 terdapat data (12, 2550).
Terakhir, ketika pengguna memilih menu Keluar (5) sehingga program menampilkan pesan "Program selesai." dan proses eksekusi dihentikan.<br>
<br>
<br>
<br>
Link video : <br>




