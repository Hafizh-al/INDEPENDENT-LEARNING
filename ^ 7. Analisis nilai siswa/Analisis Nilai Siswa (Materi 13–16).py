# Dipakai untuk guru, mentor, atau evaluasi tim.

nilai_siswa = {}

while True:
    nama = input("Nama siswa (ketik 'done' untuk berhenti): ")
    if nama.lower() == "done":
        break
    skor = float(input(f"Masukkan nilai {nama}: "))
    nilai_siswa[nama] = skor

# Hitung rata-rata
rata_rata = sum(nilai_siswa.values()) / len(nilai_siswa) if nilai_siswa else 0
print(f"\nRata-rata nilai: {rata_rata:.2f}")
# Tampilkan nilai tertinggi dan terendah
tertinggi = max(nilai_siswa.values()) if nilai_siswa else None
terendah = min(nilai_siswa.values()) if nilai_siswa else None
if tertinggi is not None and terendah is not None:
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
# Tampilkan semua nilai
print("\nDaftar Nilai Siswa:")
for nama, skor in nilai_siswa.items():
    print(f"{nama}: {skor}")

""" Bisa ditambah fitur simpan ke file, grafik, dll. """

