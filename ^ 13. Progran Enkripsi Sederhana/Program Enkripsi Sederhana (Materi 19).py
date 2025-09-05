# Cyber Security Pemula
# Program Enkripsi Sederhana

pesan = input("Masukkan pesan yang ingin dienkripsi: ")
geser = 3
enkripsi = ""

for huruf in pesan:
    if huruf.isalpha():
        kode = ord(huruf) + geser
        if huruf.islower():
            if kode > ord('z'):
                kode -= 26
        elif huruf.isupper():
            if kode > ord('Z'):      # ord(huruf) → ubah huruf ke angka ASCII.
                kode -= 26
        enkripsi += chr(kode)     
    else:
        enkripsi += huruf

print("Pesan terenkripsi:", enkripsi)
# Enkripsi adalah metode sederhana untuk mengamankan pesan dengan menggeser huruf-hurufnya.
# Relevansi: Dasar dari keamanan data, komunikasi rahasia.