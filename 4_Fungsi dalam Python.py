# def nama_fingsi(parameter):
    # isi fungsi
#    return hasil


# Fungsi tanpa argumen
def ucap_salam():
    print ("Assalamualikum warahmatullahi wabarakatuh")
# panggil fungsi
ucap_salam()
ucap_salam()
ucap_salam()

# Fungsi dengan argumen
def sapa(nama):
    print(f"Assalamualaikum, Ya {nama}!")
sapa("Muhammad")
sapa("Abdillah")

# Fungsi dengan return
def tambah(a, b):
    return a + b
hasil = tambah(11, 5)
print("Hasil =", hasil)

# Default argument
def bagi(a, b=1):
    return a / b
print(bagi(10, 2)) # 10 / 2 = 5.0
print(bagi(10))    # 10 / 1 = 10.0

# Multiple return
def operasi(a, b):
    return a+b, a-b, a*b, a/b

tambah, kurang, kali, bagi = operasi(11, 5)
print("Tambah =", tambah)
print("Kurang =", kurang)
print("Kali   =", kali)
print("Bagi   =", bagi)

# Type hints
def tambah(a: int, b: int) -> int:
    return a + b
print(tambah(7, 3))

# *Args
def total(*angka):
    return sum(angka)
print(total(1, 2, 3, 4, 5))  # 15
print(total(10, 20))         # 30

# **Kwargs
def operasi_matematika(*args, **kwargs):
    hasil = 0
    if kwargs['operasi'] == 'tambah':
        for angka in args:
            hasil += angka
    elif kwargs['operasi'] == 'kurang':
        for angka in args:
            hasil -= angka
    else:
        hasil = None
    return hasil

print(operasi_matematika(1,2,3,4,5, operasi="tambah"))  # 15
print(operasi_matematika(10,2,1, operasi="kurang"))     # -13

# Lambda function
kuadrat = lambda x: x**2
pangkat = lambda num, pow: num**pow

print(kuadrat(5))      # 25
print(pangkat(2, 3))   # 8

# Anonymous/currying
def pangkat(n):
    return lambda angka: angka ** n

pangkat2 = pangkat(2)
print(pangkat2(5))    # 25

print(pangkat(3)(2))  # 8

# Global vs Local variable
x = 10  # variabel global

def ubah():
    x = 5  # variabel lokal
    print("Di dalam fungsi:", x)

ubah()
print("Di luar fungsi :", x)
