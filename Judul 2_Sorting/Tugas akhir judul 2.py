def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n -  i - 1):
            if arr[j] > arr[j + 1]:
                tukar(arr, j, j + 1)

def main():
    try:
        n = int(input("Masukkan jumlah buku : "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan harga buku :")
    for i in range(n):
        while True:
            try:
                nilai = int(input())
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
    print("Harga buku sebelum diurutkan :", end=" ")
    for i in arr:
        print(f"Rp{i}", end=" ")
    print()
    bubble_sort(arr, n)
    print("Harga buku setelah diurutkan :", end=" ")
    for i in range(n):
        print(f"Rp{arr[i]}", end=" ")
    print()

main()