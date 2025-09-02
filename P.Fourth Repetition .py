# Tantangan — fungsi hitung diskon dengan docstring
def hitung_diskon(harga, persen=15):
    """
    Hitung harga akhir setelah diskon.
    Args: harga (float), persen (int, default 10)
    Returns: harga_akhir (float)
    """
    diskon = harga * persen / 100
    return harga - diskon

print(hitung_diskon(25000))

# safe_int(s) dengan try/except (praktik penanganan error)

def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None
    
print(safe_int("10"))
print(safe_int("abcc"))    # None (artinya gagal konversi)

# WHILE LOOP (Pertemuan 7) — Komputer mengulang sampai kondisi berubah

# Countdown (sederhana)

n = 99
while n > 0:
    print(n)
    n -= 2        # bayangkan hitungan kertas kue berkurang tiap diambil.
print("selesei!")    
    
# Tebak angka dengan batas percobaan (pakai break)

rahasia = "berusaha terus"
kesempatan = 2
while kesempatan > 0:
    guess = str(input("Tebakan: "))
    if guess == rahasia:
        print("Bener!")
        break
    else:
        print("Bukan, coba lagi!")
    kesempatan -= 1
else:
    print("Kesempatanmu habis")        

# Baca input angka sampai ketik "done", hitung rata-rata (error handling)

total = 0
count = 0
while True:
    s = input("Masukkan angka (ketik dah untuk keluar): ")
    if s.lower() == "dah":
        break
    try:
        x = float(s)
    except:
        print("Input buka angka. coba lagi")    
        continue
    total += x
    count += 1

if count:
    print("Rata-rata:", total / count)
else:
    print("Tidak ada angka.")        

# For Loop, range, nested (Pertemuan 8) — Pengulangan yang lebih rapi
# Cetak kelipatan 7 sampai 70
for i in range(0,71,7):      # range(start, stop, step) → mulai di 0, berhenti sebelum 71, lompat 7 tiap langkah.
    print(i)

# Balik string pakai for

s = "Aku"
a = ""
for g in s:
    a = g + a   
print(a)    
 
# Nested loop: tabel perkalian

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()    

