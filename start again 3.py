# Hitung upah + lembur
try:
    jam = float(input("Masukkan jumlah jam kerja: "))
    tarif = float(input("Masukkan tarif per jam"))

    if jam > 40:
        jam_lembur = jam - 40
        upah = (40 * tarif) + (jam_lembur * tarif * 1.5)
    else:
        upah = jam * tarif

    print("Total upah mingguan Anda: Rp", upah)

except:
    print("Error: Input harus berupa angka! Coba lagi ya.")

# Program Penilaian Lengkap (Grade)

try:
    skor = float(input("Masukkan nilai (0.0-1.0): "))

    if skor > 1.0 or skor < 0.0:
        print("Nilai kelewatan batas.")
    elif skor >= 0.9:
        print("Grade: A")
    elif skor >= 0.8:
        print("Grade: B")  
    elif skor >= 0.7:
        print("Grade: C") 
    elif skor >= 0.6:
        print("Grade: D") 
    else:
        print("Grade: F")                
except:
    print("Input tidak valid! Masukkan angka desimal (misal 0.85).")

tinggi = int(input("Masukkan tinggi badan (cm): "))
usia = int(input("Masukkan usia: "))
didampingi = input("Apakah didampingi ortu? (ya/tidak): ").lower()

if tinggi >= 150 and (usia> 12 or didampingi == "ya"):
    print("Anda boleh masuk wahana")
else:
    print("Maaf , Anda belum memenuhi syarat.") 
       
# Lat Sandbox 1
nilai = 10
nama = "Ahmad"       
int("10")  # hasil: 10  # CASTING
float(5)   # hasil: 5.0
bool(0)    # hasil: False
nama = input("Masukkan nama: ")
harga = int(input("Masukkan harga: "))
a = 4
b = 2
print(a>b)
print(a==b)
name = "Ucup"
umur = 17
print(f"Nama: {name}, Umur: {umur}")

import datetime
hari_ini = datetime.date.today()
print(hari_ini)
selisih = hari_ini - datetime.date(2025, 4, 30)
print(selisih.days)