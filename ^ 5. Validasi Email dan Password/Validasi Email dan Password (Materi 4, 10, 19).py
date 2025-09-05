import re
email = input("Masukkan email: ")
password = input("Masukkan password: ")

# Cek email pake regex sederhana
if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    print("Email valid")
else:
    print("Email tidak valid")

# Cek password minimal 8 karakter, ada huruf besar, huruf kecil, dan angka        
if (len(password) >= 8 and
    re.search(r'[A-Z]', password) and
    re.search(r'[a-z]', password) and
    re.search(r'\d', password)):
    print("Password kuat & aman")
else:
    print("Password lemah, harus ada huruf besar, huruf kecil, angka, dan minimal 8 karakter")   

""" Penting untuk keamanan akun (basic cyber security)."""
