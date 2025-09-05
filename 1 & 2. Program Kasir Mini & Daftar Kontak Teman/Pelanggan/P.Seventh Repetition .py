# 1. Program Kasir Mini (Hitung Total Belanja)
"""Relevansi: Dipakai di toko, warung, minimarket — menghitung total belanja."""
# Kasir Mini
total = 0 
while True:
    harga = input("Masukkan harga barang (atau 'selesai'): ")
    if harga.lower() == "selesai":
        break
    try:
        harga = float(harga) # ubah ke angka
        total += harga    # tambahkan ke total
    except:
        print("Input tidak valid, coba lagi.") 
print(f"Total belanja: Rp {total}")        

# 2. Daftar Kontak Teman / Pelanggan
""" Relevansi: Di pekerjaan, menyimpan data pelanggan/klien adalah hal penting. """
kontak = {}  # tempat simpan kontak

while True:
    nama = input("Nama (ketik 'stop' untuk keluar): ")
    if nama.lower() == "stop":
        break
    no_hp = input("Nomor HP: ")
    kontak[nama] = no_hp

print("Daftar Kontak:")
for nama, no_hp in kontak.items():
    print(f"{nama} -> {no_hp}")
