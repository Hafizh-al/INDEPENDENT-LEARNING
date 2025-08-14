# IF ELSE
nilai = 74
if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")

# IF — ELIF — ELSE
nilai = 69
if nilai >= 85:
    print("Sangat Baik")
elif nilai >= 70:
    print("Baik")
else:
    print("Kurang")        

# FOR LOOP
# Digunakan untuk mengulang sebanyak data yang dimiliki.
buah = ["apel", "pisang", "mangga"]
for b in buah:
    print(b)

# WHILE LOOP
# Terus mengulang selama kondisi bernilai True.
i = 1
while i <= 5:
    print(i)
    i += 1

list_angka = [1, 2, 3, 4, 5]   # LIST (mutable → bisa diubah) 
tuple_angka = (1, 2, 3, 4, 5)  # TUPLE (immutable → tidak bisa diubah)
set_angka = {6, 7, 8, 9, 10}   # SET (unik, tanpa urutan)

# Mengakses Data (di list)
list_nama = ['Ahmad','Budi','Santoso']
print(list_nama[0])   # 'Ahmad'
print(list_nama[-1])  # 'Santoso'

# Menambah Data
# insert(index, value) – menambah di posisi tertentu.
# append(value) – menambah di akhir.
# extend(list2) – gabungkan list.

# Mengubah & Menghapus Data
list_nama[1] = "Rudi"
list_nama.remove("Ahmad")
list_nama.pop()  # hapus item terakhir

# Cara Membuat List secara Dinamis
# Dengan range():
list_angka = list(range(0, 10, 2))
# hasil: [0, 2, 4, 6, 8]

# Dengan List Comprehension:
list_kuadrat = [i**2 for i in range(10)]
list_genap = [i for i in range(10) if i%2 == 0]