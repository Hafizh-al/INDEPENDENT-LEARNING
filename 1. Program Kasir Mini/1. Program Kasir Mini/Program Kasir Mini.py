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

