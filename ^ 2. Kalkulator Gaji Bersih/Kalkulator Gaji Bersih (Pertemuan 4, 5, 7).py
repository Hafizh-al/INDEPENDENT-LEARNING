""" Relevan banget untuk mengatur keuangan pribadi atau usaha. """
# Kalkulator Gaji Bersih
def hitung_gaji_bersih(gaji_pokok, pajak_persen, bonus):
    pajak = gaji_pokok * (pajak_persen / 100)
    gaji_bersih = gaji_pokok - pajak + bonus
    return gaji_bersih

# Input data gaji
gaji_pokok = float(input("Masukkan gaji pokok: Rp "))
pajak_persen = float(input("Masukkan persentase pajak (%): "))
bonus = float(input("Masukkan bonus: Rp "))
gaji_bersih = hitung_gaji_bersih(gaji_pokok, pajak_persen, bonus)
print(f"Gaji bersih Anda: Rp {gaji_bersih}")

# Kalkulator Gaji Bersih
"""Relevansi: Penting untuk perencanaan keuangan pribadi atau bisnis."""