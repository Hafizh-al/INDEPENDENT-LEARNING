# Aplikasi Multifungsi Sederhana untuk Belajar & Kerja
# MY DAILY HELPER
# Relevansi: Membantu tugas sehari-hari di rumah dan pekerjaan.

import re
import random
import string
from datetime import datetime

# ===================== DATA SIMPANAN =====================
kontak = {}
transaksi = []
menu_makanan = {
    "Nasi Goreng": {"harga": 20000, "stok": 5},
    "Mie Ayam": {"harga": 15000, "stok": 3},
    "Es Teh": {"harga": 5000, "stok": 10},
}
nilai = {}
faq = {
    "harga": "Harga mulai dari Rp50.000.",
    "buka": "Kami buka setiap hari pukul 08:00 - 20:00.",
    "lokasi": "Kami ada di Jakarta Pusat.",
}

# ===================== FITUR APLIKASI =====================
def manajemen_kontak():
    while True:
        print("\n--- Manajemen Kontak ---")
        print("1. Tambah Kontak\n2. Lihat Kontak\n3. Cari Kontak\n4. Hapus Kontak\n5. Kembali")
        p = input("Pilih: ")
        if p == "1":
            nama = input("Nama: ")
            nomor = input("Nomor: ")
            kontak[nama] = nomor
        elif p == "2":
            for n, t in kontak.items():
                print(f"{n} -> {t}")
        elif p == "3":
            c = input("Nama dicari: ")
            print(kontak.get(c, "Kontak tidak ada"))
        elif p == "4":
            h = input("Nama dihapus: ")
            if h in kontak:
                del kontak[h]
        elif p == "5":
            break

def catatan_keuangan():
    while True:
        print("\n--- Catatan Keuangan ---")
        print("1. Tambah Transaksi\n2. Lihat Transaksi\n3. Hitung Total\n4. Kembali")
        p = input("Pilih: ")
        if p == "1":
            desk = input("Deskripsi: ")
            nominal = float(input("Nominal (+masuk, -keluar): "))
            transaksi.append((desk, nominal))
        elif p == "2":
            for d, n in transaksi:
                print(f"{d}: {n}")
        elif p == "3":
            print("Total saldo:", sum(n for _, n in transaksi))
        elif p == "4":
            break

def analisis_teks():
    nama_file = input("Masukkan nama file teks: ")
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            teks = f.read().lower()
        bersih = re.sub(r'[^a-z0-9\s]', '', teks)
        kata = bersih.split()
        frek = {}
        for k in kata:
            frek[k] = frek.get(k, 0) + 1
        top = max(frek, key=frek.get)
        print(f"Kata paling sering: '{top}' ({frek[top]} kali)")
    except FileNotFoundError:
        print("File tidak ditemukan!")

def rekomendasi_menu():
    while True:
        print("\n--- Menu Makanan ---")
        for m, i in menu_makanan.items():
            print(f"{m} - Rp{i['harga']} (Stok: {i['stok']})")
        pilih = input("Pesan apa? (done untuk selesai): ")
        if pilih.lower() == "done":
            break
        if pilih in menu_makanan and menu_makanan[pilih]["stok"] > 0:
            menu_makanan[pilih]["stok"] -= 1
            print(f"{pilih} dipesan!")
        else:
            print("Menu tidak ada atau stok habis!")

def reminder_tugas():
    tugas = []
    while True:
        nama = input("Nama tugas (done untuk selesai): ")
        if nama.lower() == "done":
            break
        deadline = input("Deadline (YYYY-MM-DD): ")
        tugas.append((nama, deadline))
    for t, d in tugas:
        dt = datetime.strptime(d, "%Y-%m-%d")
        sisa = (dt - datetime.now()).days
        print(f"{t}: {d} (Sisa {sisa} hari)")

def chatbot():
    while True:
        tanya = input("Kamu: ").lower()
        if tanya in ["bye", "exit"]:
            print("Bot: Sampai jumpa!")
            break
        print("Bot:", faq.get(tanya, "Maaf, saya belum tahu jawabannya."))

def password_generator():
    panjang = int(input("Panjang password: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    pw = "".join(random.choice(chars) for _ in range(panjang))
    print("Password aman:", pw)

def pencatat_nilai():
    while True:
        nama = input("Nama (done untuk selesai): ")
        if nama.lower() == "done":
            break
        skor = float(input(f"Nilai {nama}: "))
        nilai[nama] = skor
    rata = sum(nilai.values()) / len(nilai)
    top = max(nilai, key=nilai.get)
    print(f"Rata-rata: {rata:.2f}")
    print(f"Nilai tertinggi: {top} ({nilai[top]})")

def mini_kasir():
    keranjang = []
    while True:
        print("\nMenu:")
        for p, h in menu_makanan.items():
            print(f"{p} - Rp{h['harga']}")
        pilih = input("Pilih produk (done untuk bayar): ")
        if pilih.lower() == "done":
            break
        if pilih in menu_makanan:
            keranjang.append(menu_makanan[pilih]["harga"])
    print(f"Total belanja: Rp{sum(keranjang)}")

def enkripsi_pesan():
    pesan = input("Pesan: ")
    geser = 3
    hasil = ""
    for huruf in pesan:
        if huruf.isalpha():
            kode = ord(huruf) + geser
            hasil += chr(kode)
        else:
            hasil += huruf
    print("Pesan terenkripsi:", hasil)

# ===================== MENU UTAMA =====================
while True:
    print("\n=== MY DAILY HELPER ===")
    print("1. Manajemen Kontak")
    print("2. Catatan Keuangan")
    print("3. Analisis Teks")
    print("4. Rekomendasi Menu Makanan")
    print("5. Reminder Tugas")
    print("6. Chatbot FAQ")
    print("7. Password Generator")
    print("8. Pencatat Nilai")
    print("9. Mini Kasir")
    print("10. Enkripsi Pesan")
    print("11. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1": manajemen_kontak()
    elif pilih == "2": catatan_keuangan()
    elif pilih == "3": analisis_teks()
    elif pilih == "4": rekomendasi_menu()
    elif pilih == "5": reminder_tugas()
    elif pilih == "6": chatbot()
    elif pilih == "7": password_generator()
    elif pilih == "8": pencatat_nilai()
    elif pilih == "9": mini_kasir()
    elif pilih == "10": enkripsi_pesan()
    elif pilih == "11":
        print("Terima kasih telah menggunakan MY DAILY HELPER!")
        break
    else:
        print("Pilihan tidak valid!")
