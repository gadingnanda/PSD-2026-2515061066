produk = ["Laptop", "Mouse", "Keyboard", "Monitor", "Speaker"]
keranjang = []

def tampilkan_produk():
    print("Daftar Produk:")
    for i, p in enumerate(produk, start=1):
        print(f"{i}. {p}")

def tambah_ke_keranjang():
    tampilkan_produk()
    try:
        index = int(input("Masukkan nomor produk: ")) - 1
        if 0 <= index < len(produk):
            keranjang.append(produk[index])
            print("Produk ditambahkan ke keranjang.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus angka.")

def hapus_dari_keranjang():
    if not keranjang:
        print("Keranjang kosong.")
        return
    
    print("\nIsi Keranjang:")
    for i, p in enumerate(keranjang, start=1):
        print(f"{i}. {p}")
    
    try:
        index = int(input("Pilih nomor yang ingin dihapus: ")) - 1
        if 0 <= index < len(keranjang):
            removed = keranjang.pop(index)
            print(f"{removed} dihapus dari keranjang.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus angka.")

def tampilkan_keranjang():
    if not keranjang:
        print("Keranjang kosong.")
    else:
        print("Isi Keranjang:")
        for i, p in enumerate(keranjang, start=1):
            print(f"{i}. {p}")

def menu():
    while True:
        print(" MENU :")
        print("1. Lihat Produk")
        print("2. Tambah ke Keranjang")
        print("3. Hapus dari Keranjang")
        print("4. Lihat Keranjang")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_produk()
        elif pilihan == "2":
            tambah_ke_keranjang()
        elif pilihan == "3":
            hapus_dari_keranjang()
        elif pilihan == "4":
            tampilkan_keranjang()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Menu tidak valid.")

menu()