# Relevansi: Aplikasi nyata sering harus cek format input.

import re    # import modul regex

nomor_telepon = input("Masukkan nomor telepon (contoh: 082314029196): ")

# Regex untuk nomor telepon Indonesia (contoh: 08xxxxxxxxxx atau +628xxxxxxxxxx)
pattern = r'^(?:\+62|0)8\d{8,11}$'      # ^ → awal string, $ → akhir string
if re.match(pattern, nomor_telepon):    # re.match() → cek kecocokan pola
    print("Nomor telepon valid")
else:
    print("Nomor telepon tidak valid")

""" Penting untuk validasi data kontak (basic data validation)."""
# Relevansi: Berguna untuk cek apakah barang ada di stok, atau pelanggan ada di database.
# Bisa dipakai di form pendaftaran, aplikasi kontak, dll.
# Validasi nomor telepon penting untuk memastikan data yang dimasukkan benar.
# Bisa dikembangkan dengan fitur simpan ke file, variasi format nomor, dll.

