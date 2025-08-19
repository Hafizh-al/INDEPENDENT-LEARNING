# IMPORT: Menghubungkan Antar File Python
# Contoh:
# import nama_file
# from nama_file import fungsi_tertentu
# Latihan 1: Membuat dan Menggunakan Module
print("_____Latihan 1_____")
# Tugas:
# Buat file bernama math_tools.py
# Di dalamnya buat fungsi: tambah, kali, pangkat
# Panggil modul ini di file main.py
# main.py
# main.py
import math_tools

print(math_tools.tambah(3, 5))
print(math_tools.kali(4, 6))
print(math_tools.pangkat(2, 3))
# Penjelasan:
# math_tools.py adalah module
# import math_tools → memanggil semua isi modul
# math_tools.tambah(3,5) artinya akses fungsi tambah dari modul math_tools

# Latihan 2: Membuat Package Sederhana
print("_____Latihan 2_____")
# Tugas:
# Buat folder mypackage
# Di dalamnya buat file __init__.py dan string_tools.py
# Gunakan di file main.py
from mypackage import string_tools

print(string_tools.kapital("python itu keren"))
print(string_tools.balik("Belajar Python"))
# Penjelasan:
# Package = folder berisi beberapa module
# __init__.py biasanya dikosongkan (cukup jadi penanda folder itu package)
# Dengan from mypackage import string_tools, kita bisa pakai fungsi dari modul string_tools

# Latihan 3: Membaca File Teks
print("_____Latihan 3_____")
# Tugas:
# Buat file data.txt dengan isi:
# Kemudian baca file ini menggunakan Python.
with open("data.txt", "r") as file:
    isi = file.read()

print("Isi file:")
print(isi)    
# Penjelasan:
# Mode "r" → read only
# with open() → otomatis menutup file setelah selesai
# read() → membaca seluruh isi file

# Latihan 4: Menulis & Menambah Data ke File
print("_____Latihan 4_____")
# Tugas:
# Tambahkan teks baru ke file data.txt
# Cek hasilnya
with open("data.txt", "a") as file:
    file.write("\nPython mudah dipelajari!")

print("Data baru berhasil ditambahkan!")
print(isi)  

# Latihan 5: Error Handling dengan Try-Except
print("_____latihan 5_____")
# Tugas:
# Tangani error ketika membuka file yang tidak ada.
try:
    with open("tidak_ada.txt", "r") as file:
        isi = file.read()
except FileNotFoundError:
    print("File tidak ditemukan, pastikan nama file benar!")        
    