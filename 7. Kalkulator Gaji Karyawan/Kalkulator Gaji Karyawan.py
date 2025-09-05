# Relevansi: Dipakai HRD/keuangan untuk hitung gaji.
# Bisa juga untuk freelancer atau pekerja lepas hitung pendapatan.

nama = input("Nama karyawan: ")
jam_kerja = float(input("Jam kerja per hari: "))
tarif_per_jam = float(input("Tarif per jam (Rp): "))
hari_kerja = int(input("Hari kerja dalam sebulan: "))
gaji_pokok = jam_kerja * tarif_per_jam * hari_kerja
potongan = float(input("Potongan (Rp): "))
gaji_bersih = gaji_pokok - potongan
print(f"\nGaji Bersih {nama}: Rp {gaji_bersih:,.2f}")
""" Bisa dikembangkan dengan fitur pajak, bonus, simpan ke file, dll. """