# Cara Membuat List
# Dengan []
# Dengan range()
# Dengan list comprehension: [i**2 for i in range(5)]
# Apa Itu Dictionary?
# Struktur data yang menyimpan data dalam pasangan kunci & nilai:
dict_negara = {'id': 'Indonesia', 'my': 'Malaysia'}
data_mahasiswa = {
   'MAH001': {'nama': 'Ahmad', 'nim': 'ARN221', 'halaqoh': 6}
}

# Mengelola data menggunakan list
# Menerapkan operasi tambah, ubah, hapus, dan cari
# Langkah-langkah:
# Buat list awal
list_nama = ["Ahmad", "Abdullah", "Umar"]
print("List awal:", list_nama)

# akses data di list
print("Nama pertama:", list_nama[0])
print("Nama terakhir:", list_nama[-1])

# Tambah data
list_nama.append("Abu Bakr")
list_nama.append("Ali")    # Tambah di akhir
list_nama.insert(1, "Utsman") # Tambah di index 1
print("All setelah tambah:", list_nama)

# ubah data
list_nama[0] = "Muhammad"
print("All setelah ubah:", list_nama)

# Hapus data
list_nama.remove("Abdullah")
list_nama.pop()
print("All setelah dihapus:", list_nama)

# Urutkan dan balik urutan
list_nama.sort()
print("Urutkan A-Z:", list_nama)
list_nama.reverse()
print("Urutkan Z-A:", list_nama)

# Latihan Copy List dan Nested list
# Copy biasa
a = [1, 2, 3]
b = a
b[0] = 99
print("a:", a)
print("b:", b)

# Copy independen
a = [1, 2, 3]
b = a.copy()
b[0] = 99
print("a:", a)
print("b:", b)

# Nested list & deepcopy
from copy import deepcopy

nested_a = [[1, 2], [3, 4]]
nested_b = deepcopy(nested_a)
nested_b[0][0] = 99

print("nested_a:", nested_a)
print("nested_b;", nested_b)

# latihan dictionary
# buat dictionary
dict_negara = {"id": "Indonesia", "my": "Malaysia", "sg": "Singapura"}
print(dict_negara)

# akses data
print("Kode 'id' adalah:", dict_negara["id"])
print("Kode 'th' (pakai get):", dict_negara.get("th", "Tidak ditemukan"))

# tambah dan ubah data
dict_negara["th"] = "Thailand"             # Tambah
dict_negara.update({"sg":  "Singapore"}) # Ubah
print(dict_negara)

# Hapus data
del dict_negara["th"]
print("setelah hapus:", dict_negara)

# Loop dictionary
for key, value in dict_negara.items():
    print(f"{key} --> {value}")
    