def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = ['Angga', 'Daffa', 'Riski', 'Nanda', 'Bima']
    n = len(data)
    print(f"Data array: {data}")
    while True:
        try:
            target = input("Masukkan Nomor yang ingin dicari: ")
            if target.isdigit():
                raise ValueError
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan Huruf!")
    counter = sequential_search(data, n, target)
    if counter > 0:
        if target == "Angga":
            nomor = "081234567890"
        elif target == "Daffa":
            nomor = "082345678901"
        elif target == "Risk":
            nomor = "083456789012"
        elif target == 'Nanda':
            nomor = '089514061188' 
        elif target == 'Bima':
            nomor = '085856283197'
        else:
            nomor = "Nomor tidak tersedia"
        print(f"Nama {target} ditemukan, Nomornya adalah : {nomor}.")
    else:
        print(f"Nama {target} tidak ditemukan.")

main()