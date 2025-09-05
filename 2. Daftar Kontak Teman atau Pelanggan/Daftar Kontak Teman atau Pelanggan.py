# 2. Daftar Kontak Teman / Pelanggan
""" Relevansi: Di pekerjaan, menyimpan data pelanggan/klien adalah hal penting. """
kontak = {}  # tempat simpan kontak

while True:
    nama = input("Nama (ketik 'stop' untuk keluar): ")
    if nama.lower() == "stop":
        break
    no_hp = input("Nomor HP: ")
    kontak[nama] = no_hp

print("Daftar Kontak:")
for nama, no_hp in kontak.items():
    print(f"{nama} -> {no_hp}")
