# 8 — Kombinasi: fungsi + loop + kondisi (praktik nyata)
# Kenapa: tugas nyata sering gabungkan semuanya.
# 8.1 - sum_range(n)
def sum_range(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(sum_range(10)) # 55   
# 8.2
def palindrom_checker(s):
    s = s.replace(" ", "").lower()
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True    
print(palindrom_checker("kasur rusak")) # True
# 8.3
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

nums = []
while True:
    s = input("Angka (done/enter): ")
    if s.lower() == "done" or s == "":
        break
    try:
        nums.append(float(s))
    except:
        print("Bukan angka, diabaikan.")
if nums:
    print("Min, Max, Avg:", stats(nums))
else:
    print("Tidak ada data.")     

# 9 — Manipulasi String (praktis & berguna)
# Kenapa: data teks umum — nama, pesan, file, URL.
# 9.1
raw = "   ani santoso  "
clean = raw.strip().title()
print(clean) # Ani Santoso

# 9.2 — Validasi email sederhana

email = input("Email: ")
if "@" in email and (email.endswith(".com")or email.endswith(".co.id")):
    print("Sepertinya valid (sederhana).")
else:
    print("Tidak valid.")    

# 9.3 — Hitung frekuensi kata (simple)

text = input("Kalimat: ").lower().strip()
words = text.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)        