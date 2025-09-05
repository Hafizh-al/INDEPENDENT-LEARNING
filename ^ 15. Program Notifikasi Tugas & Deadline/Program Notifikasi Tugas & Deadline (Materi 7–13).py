# Kenapa penting?
"""Biar nggak lupa kerjaan, bikin alert tugas dengan hitung sisa hari."""

from datetime import datetime

tugas = []  # tempat simpan tugas

while True:
    nama = input("Nama tugas (ketik 'done' untuk selesai): ")   
    if nama.lower() == "done":  
        break 
    deadline = input("Deadline (YYYY-MM-DD): ")    
    tugas.append((nama, deadline))   # simpan tugas 
    
print("\nDaftar Tugas & Deadline:")
for t, d in tugas:
    deadline_dt = datetime.strptime(d, "%Y-%m-%d")  # ubah ke objek tanggal  # .strptime = ubah teks ke tanggal.
    sisa = (deadline_dt - datetime.now()).days      # hitung sisa hari  # .now() = waktu sekarang
    print(f"{t}: {d} (Sisa {sisa} hari)")     # tampilkan tugas & sisa hari

"""  Berguna untuk manajemen proyek, sekolah, kerja tim. Bisa ditambah fitur notifikasi, simpan ke file, dll. """
# Relevansi: Notifikasi tugas & deadline penting untuk manajemen waktu.
# Bisa dipakai di aplikasi produktivitas, manajemen proyek, atau pengingat pribadi.
# Contoh tugas: kerjaan kantor, tugas sekolah, proyek tim, acara keluarga.
# Bisa juga untuk melacak deadline tagihan, perpanjangan langganan, atau janji dokter.
# Bisa dikembangkan dengan fitur notifikasi via email, SMS, atau aplikasi.
# Bisa juga ditambahkan fitur sinkronisasi dengan kalender digital seperti Google Calendar atau Outlook.
# Bisa juga ditambahkan fitur pengulangan tugas untuk tugas rutin.
# Bisa juga ditambahkan fitur prioritas tugas (tinggi, sedang, rendah).
# Bisa juga ditambahkan fitur kategori tugas (kerja, sekolah, pribadi).