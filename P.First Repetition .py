# 1 — DASAR: print() & komentar (mudah, foundation)
# Kenapa: agar kamu bisa menampilkan informasi dan memberi catatan di kode.
# 1.1
print("Selamat datang, calon programmer!")
# 1.2
print("Nama: Muhammad Dff. A. Hfzh")
print("Cita cita: Developer, Teacher, etc")
# 1.3
# Ini komentar single-line: menjelaskan fungsi berikut
"""
Ini komentar multi-line (docstring style).
Bisa dipakai untuk penjelasan panjang.
"""
print("Komentar sudah ditambahkan.")
# 1.4
a, b = 7, 3
# print(a, "+", b, "=", a + b)                     # menggunakan koma -> print menambahkan spasi otomatis
# print(str(a) + " + " + str(b) + " = " + str(a+b)) # menggabung string manual
print(f"{a} + {b} = {a + b}")                    # paling ringkas dan rapi (f-string)

# 2 — OPERATOR & EKSPRESI (praktik penting)
# Kenapa: memahami operator membuatmu bisa melakukan perhitungan & logika.
# 2.1
print("10/3=", 10/3)   # 3.3333... (float)
print("10//3=", 10//3) # 3 (pembulatan ke bawah)
# 2.2
angka = 101
is_genap = (angka % 2 == 0)
print(angka, "genap?", is_genap)
# 2.3
a = float(input("Angka pertama: "))
b = float(input("Angka kedua: "))
op = input("Operator (+ - * /): ")

if op == "+":
    print("Hasil:", a+b)
elif op == "-":
    print("Hasil:", a-b) 
elif op == "*":
    print("Hasil:", a*b)
elif op == "/":
    if b == 0:
        print("Error: ga bisa di bagi nol lah!")
    else: 
        print("Hasil:", a/b)   
else:
    print("operator ga jelas?")       
# 2.4
print("2 + 3 * 4 =", 2 + 3 * 4)      # 14
print("(2 + 3) * 4 =", (2 + 3) * 4)  # 20
      
# 3 — VARIABEL< TIPE DATA & KONVERSI
# Kenapa: variabel adalah “kotak” untuk menyimpan data.
# 3.1
a = 10        # int
b = 3.14      # float
c = "Daffa"   # str
d = True      # bool

print(type(a), type(b), type(c), type(d))
# 3.2
umur = int(input("Masukkan umur: "))
print(f"Anda berumur {umur} tahun")
# 3.3
s = "5"
print("Sebelum konversi:", s * 2)    # "55" (string ulang)
n = int(s)
print("Setelah konversi:", n * 2)     # 10 (numeric)
# 3.4
n1 = float(input("Nilai 1: "))
n2 = float(input("Nilai 2: "))
n3 = float(input("Nilai 3: "))
total = n1 + n2 + n3
rata = total / 3
print(f"Total: {total}, Rata-rata: {rata:.2f}")

# 4 — Percabangan: IF / ELIF / ELSE (praktik keputusan)
# Kenapa: agar program bisa melakukan tindakan berbeda sesuai kondisi.
# 4.1
umur = int(input("umur: "))
if umur >= 17:
    print("Alhamdulillah, dah bole buat SIM ni!")
else:
    print("Sabar. nanti", 17-umur, "tahun lagi.")
# 4.2
try:
    s = float(input("Masukkan skor(0.0-9.9): "))
    if s < 0.0 or s > 9.9:
        print("Skor harus antara 0.0 dan 9.9")
    else:
        if s >= 8.9:
            print("Grade: A")
        elif s >= 7.5:
            print("Grade: B")
        elif s >= 6.5:
            print("Grade: C")   
        else:
            print("Grade: D")
except ValueError:
    print("Et , masukin angka!")
# 4.3
tinggi = int(input("Tinggi (cm): "))
umur = int(input("Umur: "))
dampingi = input("Didampingi orang tua? (ya/tidak): ").lower() == "ya"

if tinggi >= 150 and (umur > 12 or dampingi):
    print("Boleh naik wahana.")
else:
    print("Tidak boleh naik.")
