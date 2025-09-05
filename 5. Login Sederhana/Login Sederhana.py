# Login Sederhana
"""Relevansi: Banyak/semua aplikasi butuh login untuk keamanan."""

username = "admin"
password = "bismillah"

for i in range(3):  # coba 3 kali
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")
    if input_username == username and input_password == password:
        print("Login berhasil!")
        break
    else:
        print("Login gagal. Coba lagi.")
else:
    print("Akun terkunci. Hubungi admin.")   

"""sistem login mini."""
    