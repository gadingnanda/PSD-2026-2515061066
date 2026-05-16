Judul : Sistem antrian pelanggan <br>
<br>
<br>
Deskripsi : <br>
Program ini meruoakan simulasi antrian pelanggan menggunakan struktur data queue berbasis array. 
Program memiliki fitur untuk menambahkan pelanggan ke antrian (enqueue), melayani pelanggan (dequeue), melihat pelanggan terdepan (peek), dan menampilkan seluruh isi antrian. 
Selain itu, program juga menghitung estimasi waktu tunggu berdasarkan jumlah pelanggan dalam antrian. 
Pengguna dapat mengoperasikan program melalui menu interaktif yang berjalan terus hingga memilih keluar dari program. <br>
<br>
<br>

<img width="1176" height="863" alt="Screenshot 2026-05-15 151342" src="https://github.com/user-attachments/assets/9ff75365-e626-4f73-b499-025076f8e5b4" /><br>
class QueueArray merupakan sebuah class dalam Python yang digunakan untuk membuat struktur data queue menggunakan array atau list. 
Queue bekerja dengan konsep FIFO (First In First Out), artinya data yang pertama masuk akan menjadi data pertama yang keluar. <br>
Fungsi __init__() digunakan sebagai awalan untuk menginisialisasi queue atau antrian. 
Pada fungsi ini, program menentukan ukuran maksimum queue (MAXN), membuat list kosong sesuai kapasitas, serta mengatur posisi awal front_idx dan rear_idx menjadi -1 yang menandakan queue masih kosong. <br>
Fungsi is_empty() berfungsi untuk memeriksa apakah queue kosong atau tidak. 
Jika nilai front_idx sama dengan -1, maka fungsi akan mengembalikan nilai True yang berarti antrian masih kosong.<br>
Fungsi is_full() digunakan untuk mengecek apakah queue sudah penuh. 
Kondisi penuh terjadi ketika posisi belakang (rear_idx) ditambah satu lalu dimoduluskan dengan kapasitas maksimum sama dengan posisi depan (front_idx).<br>
Fungsi enqueue(x) berfungsi untuk menambahkan data atau pelanggan baru ke dalam antrian. 
Jika queue penuh, program akan menampilkan pesan “Queue penuh”. 
Jika queue masih kosong, maka indeks depan dan belakang diatur ke 0. Jika tidak kosong, posisi belakang akan bergeser ke indeks berikutnya.
Setelah data berhasil ditambahkan, program menampilkan jumlah pelanggan dalam antrean dan estimasi waktu tunggu berdasarkan posisi antrean. <br>
Fungsi dequeue() digunakan untuk menghapus atau melayani data yang berada di bagian depan antrian. 
Jika queue kosong, program akan menampilkan pesan “Antrian kosong”. 
Jika terdapat data, maka program menampilkan nama antrean yang sedang dilayani. 
Setelah itu, jika hanya ada satu data dalam queue, indeks depan dan belakang akan dikembalikan menjadi -1. 
Namun jika masih ada data lain, posisi depan akan maju ke indeks berikutnya. <br>
<br>
<br>

<img width="777" height="451" alt="Screenshot 2026-05-15 151527" src="https://github.com/user-attachments/assets/702c036f-cb59-45a6-be45-b5fab9bb6838" /> <br>
Fungsi peek() digunakan untuk melihat elemen atau data yang berada di bagian depan antrian tanpa menghapusnya dari queue. 
Fungsi ini terlebih dahulu memeriksa apakah queue kosong menggunakan is_empty(). 
Jika kosong, program akan menampilkan pesan “Antrian kosong”. 
Namun jika queue memiliki data, maka program akan menampilkan elemen yang berada pada posisi front_idx sebagai elemen terdepan dalam antrian.<br>
Fungsi display() digunakan untuk menampilkan seluruh isi antrian yang ada di dalam queue. 
Program akan terlebih dahulu memeriksa apakah queue kosong. Jika kosong, maka akan muncul pesan “Antrian kosong”. 
Jika terdapat data, program akan menampilkan semua elemen antrean mulai dari posisi depan hingga belakang. <br>
<br>
<br>

<img width="538" height="792" alt="Screenshot 2026-05-15 150119" src="https://github.com/user-attachments/assets/7ae6183d-74b4-4d83-8edd-98f2b3ec687c" /> <br>
Fungsi main() digunakan sebagai program utama untuk menjalankan sistem antrian pelanggan.
Pada awal fungsi, program membuat objek queue dari class QueueArray dan variabel pilih untuk menyimpan pilihan menu pengguna. 
Selanjutnya, program menjalankan perulangan while selama pengguna belum memilih menu keluar. 
Di dalam perulangan, program menampilkan beberapa menu, yaitu menambahkan antrean, melayani pelanggan, melihat pelanggan terdepan, menampilkan seluruh antrean, dan keluar dari program.<br>
Program kemudian meminta pengguna memasukkan pilihan menu menggunakan input().
Jika pengguna memilih menu 1, program meminta nama pelanggan lalu menambahkannya ke dalam antrean menggunakan fungsi enqueue(). 
Jika memilih menu 2, program akan melayani dan menghapus pelanggan terdepan menggunakan dequeue(). 
Pilihan 3 digunakan untuk melihat pelanggan paling depan dengan fungsi peek(), 
sedangkan pilihan 4 digunakan untuk menampilkan seluruh isi antrean melalui fungsi display(). 
Jika pengguna memilih 5, program akan berhenti dan menampilkan pesan “Program selesai”. <br>
<br>
<br>

<img width="282" height="66" alt="Screenshot 2026-05-15 150126" src="https://github.com/user-attachments/assets/5a050eb8-c95e-48a8-8533-79cf18115bac" /><br>
Pada kode if __name__ == "__main__": digunakan untuk memastikan bahwa fungsi main() hanya dijalankan ketika file Python tersebut dieksekusi secara langsung, bukan saat file digunakan atau diimpor ke program lain sebagai module. 
Jika kondisi tersebut bernilai benar, maka program akan memanggil fungsi main() sehingga seluruh sistem antrian dapat dijalankan.<br>
<br>
<br>

<img width="776" height="876" alt="Screenshot 2026-05-16 174423" src="https://github.com/user-attachments/assets/38c7448f-293f-4550-bbb9-631b1876500d" /><br>
Output program ini pada awalnya akan menampilkan menu utama yang berisi beberapa pilihan, seperti menambahkan antrean, melayani pelanggan, melihat pelanggan terdepan, menampilkan antrean, dan keluar dari program. 
Pengguna pertama memilih menu 1 untuk menambahkan pelanggan bernama Agus ke dalam antrean. Program kemudian menampilkan bahwa Agus berhasil ditambahkan dengan posisi antrean pertama sehingga estimasi waktu tunggunya 0 menit.<br>
Berikutnya ketika pengguna kembali memilih menu 1 dan menambahkan pelanggan bernama Arif. 
Karena Arif berada di belakang Agus, program menampilkan bahwa jumlah pelanggan yang sedang dilayani adalah 1 dan estimasi waktu tunggunya 5 menit. 
Setelah itu, pengguna memilih menu 4 untuk menampilkan seluruh isi antrean, sehingga program menampilkan urutan antrean yaitu “Agus Arif”. Terakhir, pengguna memilih menu 3 untuk melihat pelanggan terdepan, dan program menampilkan bahwa elemen atau pelanggan paling depan dalam antrean adalah Agus.<br>
<br>
<br>
Link video : <br>
https://youtu.be/vcnkNYGgG8s


