# Cocok untuk membiasakan pakai list dan loop.

# Daftar Belanja Pintar (Materi 7–13)
"""Relevansi: Di dunia nyata, orang sering buat daftar belanja."""

daftar_belanja = []  # list kosong untuk simpan barang
while True:          # while True → tanya terus sampai ketik "done".
    barang = input("Masukkan barang (ketik 'dah' untuk selesai): ")
    if barang.lower() == "dah":
        break
    daftar_belanja.append(barang)  # tambahkan barang ke list
print("\nDaftar Belanja Kamu:")
for i, barang in enumerate(daftar_belanja, start=1):
    print(f"{i}. {barang}")  # tampilkan dengan nomor urut