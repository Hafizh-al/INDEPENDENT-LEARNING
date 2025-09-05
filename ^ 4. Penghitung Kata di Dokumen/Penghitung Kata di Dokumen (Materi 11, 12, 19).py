import re

nama_file = "artikel.txt"  # buat file ini dan isi dengan teks
with open(nama_file, "r") as f:
    teks = f.read().lower()

# Bersihkan teks dari simbol
bersih = re.sub(r'[^a-z0-9\s]', '', teks)
kata = bersih.split()

print(f"Total kata: {len(kata)}")
