class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=15):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nIsi Hash Table:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"({self.table[i].key},{self.table[i].value})")


def main():
    hashmap = HashMapOpenAddressing()
    pilih = 0
    while pilih != 10:
        print("\n=== Menu ===")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                key = int(input("Masukkan key: "))
                value = input("Masukkan value: ")
                hashmap.insert(key, value)
                print(f"Data ({key}, {value}) berhasil dimasukkan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                x = int(input("Cari nilai key: "))
                hasil = hashmap.search(x)
                if hasil is not None:
                    print(f"\nKey {x} ditemukan, value = {hasil.value}")
                else:
                    print(f"\nKey {x} tidak ditemukan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            try:
                key = int(input("Masukkan nilai key barang : "))
                if hashmap.remove_key(key):
                    print(f"Key {key} berhasil dihapus")
                else:
                    print(f"Key {key} tidak ditemukan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 4:
            print("Display: ", end="")
            hashmap.display()
            print()
        elif pilih == 5:
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
