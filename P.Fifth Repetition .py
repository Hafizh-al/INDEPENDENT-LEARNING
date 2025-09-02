# File I/O (Membaca / Menulis / Append / os) (Pertemuan 11–12) — Simpan data supaya tidak 

nama_file = "siswa.txt"
try: 
    with open(nama_file, 'r') as f:
        for baris in f:
            print("Nama:", baris.strip())
except FileNotFoundError:
    print("File tidak ditemukan, buat dulu 'siswa.txt'.") 

# Tulis daftar belanja (mode 'w')

items = ["Apel", "Roti", "Susu", "Pisang"]
with open("belanja.txt", "w") as f:
    for i, it in enumerate(items, start=1):
        f.write(f"{i}. {it}\n")

# Tambah log (mode 'a')

with open("log.txt", "a") as f:
    f.write("Login user: Daffa\n")
    
# Baca angka dari file lalu hitung rata-rata (gabungan read + konversi + try/except)# 

total = 0
count = 0
with open("nilai.txt","r") as f:
    for line in f:
        s = line.strip()
        try:
            n = float(s)
            total += n
            count += 1
        except:
            print("Lewati:", s)
if count:
    print("Rata rata:", total/count)
else:
    print("Tidak ada angka valid.") 


# LIST (Pertemuan 13–14) — Rak untuk banyak barang: ubah tambah hapus

# Buat list, append, insert, remove, pop

buah = ["Apel", "Jeruk"]
buah.append("Mangga")        # tambahkan di akhir                       
buah.insert(1, "Pisang")     # sisipkan di indeks 1
print(buah)
buah.remove("Jeruk")         # hapus berdasar nilai (pertama ditemukan)
terhapus = buah.pop()        #  hapus & kembalikan elemen terakhir
print("Setelah hapus:", buah, "dihapus:", terhapus)

# .append() menambah 1 item di akhir.

# .insert(i, x) sisipkan di posisi i.

# .remove(val) hapus item pertama yang cocok.

# .pop() hapus & kembalikan elemen (berguna kalau butuh nilai yang dihapus).

# Slicing dan loop modifikasi

nums = [1,2,3,4,5]
for i in range(len(nums)):      # Gunakan range(len(nums)) bila ingin mengubah list di tempat.
    nums[i] = nums[i] * 2
print(nums)   

# Sorting dan penggunaan sorted() vs .sort()
names = ["ani" , "Budi" , "cika"]
print(sorted(names))    # mengembalikan list baru terurut tanpa ubah asli
names.sort(key=str.lower) # ubah list asli jadi terurut case-insensitive
print(names)      # sorted() mengembalikan hasil baru; .sort() mengubah list asli.


