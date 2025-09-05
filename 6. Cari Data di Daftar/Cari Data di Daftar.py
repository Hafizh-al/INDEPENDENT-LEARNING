# Relevansi: Berguna untuk cek apakah barang ada di stok, atau pelanggan ada di database.

data_list = ["apel", "pisang", "jeruk", "mangga", "anggur"]
cari = input("Mau cari apa? : ").lower()  # .lower() → supaya perbandingan tidak peduli huruf besar/kecil.

if cari.lower() in data_list:
    print(f"{cari} tersedia.")
else:
    print(f"{cari} stok habis.")
""" Bisa dikembangkan dengan fitur input data, hapus data, simpan ke file, dll. """
