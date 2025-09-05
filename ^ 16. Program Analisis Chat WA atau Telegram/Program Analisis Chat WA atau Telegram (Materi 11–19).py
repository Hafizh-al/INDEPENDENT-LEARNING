# Kenapa penting?
""" Analisis percakapan customer atau grup bisnis buat tahu kata-kata yang 
sering muncul (tren, kebutuhan pasar)."""

import re   # regex = regular expression, buat manipulasi teks

# Baca file chat yang sudah kamu export dari WA/Telegram
with open("chat.txt", "r", encoding="utf-8") as f:    # encoding biar support karakter Indonesia #  utf-8 = standar encoding teks
    chat = f.read().lower()  # baca & ubah ke huruf kecil

# Bersihkan teks: buang simbol
bersih = re.sub(r'[^a-z0-9\s]', '', chat)
kata = bersih.split()   # split = pisah teks jadi list

# Hitung frekuensi kata
frekuensi = {}
for k in kata:
    frekuensi[k] = frekuensi.get(k, 0) + 1   # .get = ambil nilai, default 0

# Cari kata paling populer
populer = max(frekuensi, key=frekuensi.get) #.get = ambil nilai
print(f"Kata paling sering: '{populer}' ({frekuensi[populer]} kali)")
