# Sangat relevan untuk manajemen waktu di dunia kerja.

tugas_harian = []

while True:
    tugas = input("Masukkan tugas harian (atau 'ok' untuk berhenti): ")
    if tugas.lower() == "ok":
        break
    tugas_harian.append(tugas)    # append() → tambah item ke list.
print("\nTugas Harian Anda:")     
for i, tugas in enumerate(tugas_harian, 1):     # enumerate() → beri nomor otomatis.
    print(f"{i}. {tugas}")
""" Bisa dikembangkan dengan fitur prioritas, deadline, simpan ke file, dll. """

