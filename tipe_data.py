# a = 10, a adalah variabel dengan nilai 10

# tipe data: angka satuan yang gak ada 
# komanya (integer)
data_integer = 1
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "ucup"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# tipe data: biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

# tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))



# episode operator bitwise

a = 8
b = 3

print("a =", a, "->", bin(a))
print("a =", b, "->", bin(b))


print("a & b =", a & b, "->", bin(a & b))  # AND
print("a | b =", a | b, "->", bin(a | b))  # OR
print("a ^ b =", a ^ b, "->", bin(a ^ b))  # XOR
print("~0 =", ~0, "->", bin(~0))           # NOT
print("a << 1 =", 7 << 2, "->", bin(7 << 1)) # LEFT SHIFT
print("a >> 1 =", a >> 1, "->", bin(a >> 1)) # RIGHT SHIFT

# operasi yang adpat dilakukan dengan penyingkatn
# operasi ditambah dengan assignment

a = 5 # adalah assignment
print("nilai a =",a)

a += 1 # artinya a = a + 1
print("nilai a += 1, nilai a menjadi",a)

a -= 2 # artinya adalah a = a -2
print("nilai a -= 2, nilai a menjadi",a)

a *= 5 # artinya adalah a = a * 5
print("nilai a *= 5, nilai a menjadi",a)

a /= 2 # artinya adalah a = a /2
print("nilai a /= 2, nilai a menjadi",a)

b = 10
print("/nnilai b =",b)

b //= 3
print("nilai b //= 3, nilai b menjadi",b)

a = 5
print("nilai a =",a)
a **= 3
print("nilai a **= 3, nilai a menjadi",a)


# operasi bitwise
# OR
c = False
print("/nnilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)

# And
c = True
print("/nnilai c =",c)
c &= True
print("nilai c &= False, nilai c menjadi",c)

# XOR
c = True
print("/nnilai c =",c)
c ^= True
print("nilai c ^= False, nilai c menjadi",c)

data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
   1. dengan menggunakan single quote '...'
   2. dengan menggunakan double quote
'''

data = 'menggunakan single quote'
print(data)

data = 'menggunakan double quote'
print(data)

print('"Halo, apa kabar?"')
print("ini adalah hari jum'at")

# 2. Menggunakan tanda /

# membuat tanda / menjadi string
print('mari sholat jum\'at')

# backslash

print("C;\\user\\Ucup")

# tab

print("ucup\t\t\totong, semakin jauhan")

#backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua") # line feed -> unix , macos , linux
print("baris pertama.\rbaris kedua") # carriage return->
print("baris pertama.\r\nbaris kedua") # line feed carriage return


# 3 string literal atau aw



# TUGAS PEKANAN PEKAN 1

# Proyek Kasir Cerdas Sederhana

print("="*43)
print("SELAMAT DATANG DI PROGRAM KASIR CERDAS!")
print("="*43)

# Input Barang 1
print("--- Masukkan Detail Barang 1 ---")
nama_barang_1 = input("Nama Barang: ")
harga_1 = float(input("Harga Satuan: Rp "))
jumlah_1 = int(input("Jumlah: "))

# Input Barang 2
print("\n--- Masukkan Detail Barang 2 ---")
nama_barang_2 = input("Nama Barang: ")
harga_2 = float(input("Harga Satuan: Rp "))
jumlah_2 = int(input("Jumlah: "))

# Kalkulasi
total_1 = harga_1 * jumlah_1
total_2 = harga_2 * jumlah_2
subtotal = total_1 + total_2

# Logika Diskon
diskon_persen = 0
if subtotal > 200000:
    diskon_persen = 10
elif subtotal > 100000:
    diskon_persen = 5

jumlah_diskon = subtotal * (diskon_persen / 100)
total_setelah_diskon = subtotal - jumlah_diskon

# Bonus: Tambahkan PPN 11%
ppn = total_setelah_diskon * 0.11
total_final = total_setelah_diskon + ppn

# Bonus: Uang kembalian
uang_bayar = float(input("\nMasukkan jumlah uang yang dibayarkan: Rp "))
kembalian = uang_bayar - total_final

# Cetak Struk
print("\n" + "="*43)
print("STRUK PEMBELIAN ANDA")
print("="*43)
print("Detail Belanja:")
print(f"1. {nama_barang_1} ({jumlah_1} x Rp {harga_1}) = Rp {total_1}")
print(f"2. {nama_barang_2} ({jumlah_2} x Rp {harga_2}) = Rp {total_2}")
print("-"*43)
print(f"Subtotal            : Rp {subtotal}")
print(f"Diskon ({diskon_persen}%)      : - Rp {jumlah_diskon}")
print(f"PPN (11%)           : + Rp {ppn}")
print("-"*43)
print(f"Total yang dibayar  : Rp {total_final}")
print(f"Uang dibayarkan     : Rp {uang_bayar}")
print(f"Kembalian           : Rp {kembalian}")
print("="*43)
print("TERIMA KASIH TELAH BERBELANJA!")
print("="*43)
