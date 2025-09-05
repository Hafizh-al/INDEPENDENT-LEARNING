# Relevansi: Analisis dokumen, caption, deskripsi produk, dll.

teks = input("Masukkan teks: ").lower()  # .lower() → supaya hitung kata tidak peduli huruf besar/kecil.
kata_list = teks.split()  # .split() → pisah teks jadi list kata-kata.
jumlah_kata = len(kata_list)  # len() → hitung jumlah item di list.
print(f"Jumlah kata: {jumlah_kata}")

# Hitung frekuensi tiap kata
frekuensi = {}
for kata in kata_list:
    if kata in frekuensi:
        frekuensi[kata] += 1
    else:
        frekuensi[kata] = 1
print("\nFrekuensi kata:")
for kata, freq in frekuensi.items():
    print(f"{kata}: {freq}")
""" Bisa ditambah fitur simpan hasil ke file, analisis lebih lanjut, dll. """