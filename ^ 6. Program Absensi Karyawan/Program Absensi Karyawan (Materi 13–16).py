""" Cocok untuk HR atau event organizer. """

absensi = {}
while True:
    nama = input("Masukkan nama karyawan (atau 'exit' untuk keluar): ")
    if nama.lower() == 'exit':
        break
    waktu_masuk = input("Masukkan waktu masuk (HH:MM): ")
    waktu_keluar = input("Masukkan waktu keluar (HH:MM): ")
    absensi[nama] = (waktu_masuk, waktu_keluar)
print("\nRekap Absensi Karyawan:")
for nama, (masuk, keluar) in absensi.items():
    print(f"{nama}: Masuk pukul {masuk}, Keluar pukul {keluar}")

""" Bisa dikembangkan dengan fitur validasi waktu, simpan ke file, dll. """

# Contoh output:
# Masukkan nama karyawan (atau 'exit' untuk keluar): Budi
# Masukkan waktu masuk (HH:MM): 09:00
# Masukkan waktu keluar (HH:MM): 17:00
# Masukkan nama karyawan (atau 'exit' untuk keluar): Siti
# Masukkan waktu masuk (HH:MM): 08:30
# Masukkan waktu keluar (HH:MM): 16:30
# Masukkan nama karyawan (atau 'exit' untuk keluar): exit
# 
# Rekap Absensi Karyawan:
# Budi: Masuk pukul 09:00, Keluar pukul 17:00
# Siti: Masuk pukul 08:30, Keluar pukul 16:30


absensi = {}

while True:
    nama = input("Nama karyawan (ketik 'done' untuk selesai): ")
    if nama.lower() == "done":
        break
    hadir = input("Hadir? (y/n): ").lower()
    absensi[nama] = hadir == "y"

print("\nRekap Absensi:")
for k, v in absensi.items():
    print(f"{k}: {'Hadir' if v else 'Tidak Hadir'}")
