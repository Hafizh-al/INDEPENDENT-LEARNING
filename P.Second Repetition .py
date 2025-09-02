# 5 — FUNCTIONS (fungsi): definisi & return
# Kenapa: fungsi membuat kode terorganisir dan dapat dipakai ulang.
# 5.1
def sapa():
    print("Assalamualaikum!")
    print("Semangat terus , belajar terus!!!")
sapa()
sapa()
# 5.2
def hitung_luas_persegi_panjang(p, l):
    return p * l
print(hitung_luas_persegi_panjang(11, 7))
# 5.3
def buat_email(nama, domain="coding.com"):
    return f"{nama.lower()}@{domain}"

print(buat_email("Daffa"))
print(buat_email("Daffa", domain="example.com"))
# 5.4
def safe_int(s):
    try:
        return int(s)
    except:
        return None

print(safe_int("10"), safe_int("abc"))        
# 5.5
kali2 = lambda x: x * 2
print(kali2(5))

# 6 — PERULANGAN WHILE
# Kenapa: untuk tugas berulang yang tidak tahu jumlah iterasi sebelumnya

# 6.1-Countdown
n = 10
while n > 0:
    print(n)
    n -= 1
print("Blastoff!")    
# 6.2-Tebak angka sederhana
secret = 7
while True:
    tebak = int(input("Tebak angka (1-10): "))
    if tebak == secret:
        print("Betul banget!")
        break
    elif tebak < secret:
        print("kurang,kekecilan itu!")
    else:
        print("dah over itu!")    

# 6.3-Terus input sampe done
total = 0
count = 0
while True:
    s = input("Masukkan angka (ketik 'done' untuk berhenti): ")
    if s.lower() == "done":
        break
    try:
        n = float(s)
        total += n
        count += 1
    except:
        print("selain angka, biarin!")
if count > 0:
    print("Rata-rata:", total / count)
else:
    print("ga ada angkanya,mana?!")

# 7 — Perulangan for, range, nested loops
# Kenapa: elegan untuk mengulang di atas iterable.
# 7.1-Range dasar
for i in range(5):
    print(i)
# 7.2-kelipatan 7
for i in range(0, 71, 7):
    print(i)    
# 7.3-abel perkalian 1..9 (nested loop)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}x{j}={i*j}", end="\t")
    print()    
# 7.4-Pattern segitiga
for i in range(1, 6):
    print("*" * i)

