# DICTIONARY (Pertemuan 15–16) — Kamus: akses data pakai nama bukan indeks

kontak = { }
kontak["Peace"] = "0877777"
kontak["Aisy"]  = "0899999"
print(kontak.get("Peace", "Tidak ada")) # gunakan get agar tidak error
print(kontak["Aisy"])

# Histogram huruf (menghitung frekuensi)

kata = "banana"
count = {}
for ch in kata:
    count[ch] = count.get(ch, 0) + 1
print(count)    

# Iterasi .items() dan nested dict

db = {
    "s1": {"nama":"Peace","nilai":99},
    "s2": {"nama":"Aisy","nilai":97}
}
for id, data in db.items():
    print(id, "-", data["nama"], "->", data["nilai"])

# TUPLE (Pertemuan 17) — Rak kaku: tidak bisa berubah, cocok untuk constant    

# Membuat tuple, unpacking

number = (10,20)
a, b = number
print(a, b)

# Menukar nilai variabel dengan satu baris (idiom Python)

a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5
