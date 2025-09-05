"""Relevansi: Dunia kerja butuh mencatat rapat, ide, atau progress."""
# Catatan Harian (File I/O)
with open("catatan_harian.txt", "a") as file:  # buka file untuk ditulis (append)
    teks = input("Tulis catatan hari ini: ")
    file.write(teks + "\n")  # tulis catatan ke file
print("Catatan tersimpan di 'catatan_harian.txt'.")    

# Membaca catatan
with open("catatan_harian.txt", "r") as file:  # buka file untuk dibaca
    print("\nIsi Catatan Harian:")
    print(file.read())  # baca dan tampilkan isi file