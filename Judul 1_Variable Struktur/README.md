Judul Program : Program Barang Belanjaan

Deskripsi : <br>
 Program ini adalah simulasi sederhana tentang keranjang belanja. Pengguna dapat melihat daftar produk, memilih barang untuk dimasukkan ke dalam keranjang, menghapus barang yang tidak jadi dibeli, serta melihat isi keranjang.
 Program ini menggunakan List 1D sebagai inti penyimpanan data, yaitu pada variabel keranjang. Algoritma yang diterapkan adalah linear traversal atau penelusuran berurutan, yaitu menampilkan isi keranjang, serta operasi insert dan delete pada list.

Source code :
<img width="1115" height="929" alt="Screenshot 2026-04-28 160308" src="https://github.com/user-attachments/assets/4b1ee4cb-ffb7-4d5c-947e-c0852cb1a672" />
<img width="1276" height="932" alt="Screenshot 2026-04-29 125305" src="https://github.com/user-attachments/assets/982592c1-801d-4229-adb8-4960610290b3" />

Penjelasan : <br>
baris 1, Membuat list produk yang berisi daftar barang yang tersedia.<br>
Baris 2, Membuat list kosong keranjang untuk menyimpan barang yang dipilih user.<br>
Baris 4, Mendefinisikan fungsi tampilkan_produk.<br>
Baris 5, Menampilkan teks "Daftar Produk:".<br>
Baris 6, Melakukan perulangan pada list produk dengan enumerate untuk mendapatkan nomor.<br>
Baris 7, Menampilkan nomor dan nama produk.<br>
Baris 9, Mendefinisikan fungsi tambah_ke_keranjang.<br>
Baris 10, Memanggil fungsi tampilkan_produk untuk menampilkan daftar produk.<br>
Baris 11, Memulai blok try untuk menangani error input.<br>
Baris 12, Meminta input nomor produk, mengubah ke integer, lalu dikurangi 1.<br>
Baris 13, Mengecek apakah index berada dalam range list produk.<br>
Baris 14, Menambahkan produk ke dalam keranjang.<br>
Baris 15, Menampilkan pesan bahwa produk berhasil ditambahkan.<br>
Baris 16, Menangani kondisi jika input tidak valid.<br>
Baris 17, Menangkap error jika input bukan angka.<br>
Baris 18, Menampilkan pesan error input harus angka.<br>
Baris 21, Mendefinisikan fungsi hapus_dari_keranjang.<br>
Baris 22, Mengecek apakah keranjang kosong.<br>
Baris 23, Menampilkan pesan jika keranjang kosong.<br>
Baris 24, Menghentikan fungsi dengan return.<br>
Baris 26, Menampilkan teks "Isi Keranjang:".<br>
Baris 27, Melakukan perulangan untuk isi keranjang.<br>
Baris 28, Menampilkan nomor dan nama produk dalam keranjang.<br>
Baris 30, Memulai blok try.<br>
Baris 31, Meminta input nomor barang yang akan dihapus.<br>
Baris 32, Mengecek apakah index valid.<br>
Baris 33, Menghapus item dari keranjang menggunakan pop().<br>
Baris 34, Menampilkan pesan item yang dihapus.<br>
Baris 35, Menangani jika pilihan tidak valid.<br>
Baris 36, Menangkap error input.<br>
Baris 37, Menampilkan pesan error.<br>
Baris 40, Mendefinisikan fungsi tampilkan_keranjang.<br>
Baris 41, Mengecek apakah keranjang kosong.<br>
Baris 42, Menampilkan pesan jika kosong<br>
Baris 43, Masuk ke kondisi jika keranjang tidak kosong.<br>
Baris 44, Menampilkan teks "Isi Keranjang:".<br>
Baris 45, Melakukan perulangan isi keranjang.<br>
Baris 46, Menampilkan nomor dan nama produk.<br>
Baris 48, Mendefinisikan fungsi menu.<br>
Baris 49, Memulai perulangan tak terbatas (while True).<br>
Baris 50, Menampilkan judul menu<br>
Baris 51, Menampilkan pilihan menu 1.<br>
Baris 52, Menampilkan pilihan menu 2.<br>
Baris 53, Menampilkan pilihan menu 3<br>
Baris 54, Menampilkan pilihan menu 4.<br>
Baris 55, Menampilkan pilihan menu 5.<br>
Baris 57, Meminta input pilihan menu dari user.<br>
Baris 59, Mengecek jika user memilih menu 1.<br>
Baris 60, Memanggil fungsi tampilkan produk.<br>
Baris 61, Mengecek jika user memilih menu 2.<br>
Baris 62, Memanggil fungsi tambah ke keranjang.<br>
Baris 63, Mengecek jika user memilih menu 3.<br>
Baris 64, Memanggil fungsi hapus dari keranjang.<br>
Baris 65, Mengecek jika user memilih menu 4.<br>
Baris 66, Memanggil fungsi tampilkan keranjang.<br>
Baris 67, Mengecek jika user memilih menu 5.<br>
Baris 68, Menampilkan pesan keluar.<br>
Baris 69, Menghentikan program dengan break.<br>
Baris 70, Menangani jika pilihan tidak valid.<br>
Baris 71, Menampilkan pesan "Menu tidak valid".<br>
Baris 73, Memanggil fungsi menu() untuk menjalankan program.<br>

Output :
<img width="287" height="161" alt="Screenshot 2026-04-28 170421" src="https://github.com/user-attachments/assets/ce7b76f1-875a-4518-bf69-6700310a0d69" />

Penjelasan : <br>
Jika memilih 1, program menampilkan daftar produk.
Jika memilih 2, user bisa menambahkan barang ke keranjang.
Jika memilih 3, user bisa menghapus barang dari keranjang.
Jika memilih 4, program menampilkan isi keranjang.
Jika memilih 5, program akan berhenti.
