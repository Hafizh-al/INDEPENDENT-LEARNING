""" Skill analisis data penjualan yang nyata dipakai bisnis. """
# Skill Data Analyst Pemula:
# Relevansi: Berguna untuk analisis penjualan, laporan bisnis.
# Bisa dipakai di usaha kecil, toko online, dll.

penjualan = {
    "Januari": 5000000,
    "Februari": 9500000,
    "Maret": 7000000,
    "April": 12000000,
    "Mei": 8500000,
    "Juni": 11000000
}

total_penjualan = sum(penjualan.values())  # sum() → jumlah total  # .values() → ambil semua nilai (angka)
rata_rata = total_penjualan / len(penjualan)  # len() → jumlah bulan
bulan_tertinggi = max(penjualan, key=penjualan.get)  # max() → bulan dengan penjualan tertinggi
bulan_terendah = min(penjualan, key=penjualan.get)   # min() → bulan dengan penjualan terendah
print(f"Total Penjualan: Rp{total_penjualan}")
print(f"Rata-rata Bulanan: Rp{rata_rata:.2f}")
print(f"Bulan Tertinggi: {bulan_tertinggi} (Rp{penjualan[bulan_tertinggi]})")
print(f"Bulan Terendah: {bulan_terendah} (Rp{penjualan[bulan_terendah]})")

""" Bisa dikembangkan dengan fitur simpan ke file, grafik, dll. """
