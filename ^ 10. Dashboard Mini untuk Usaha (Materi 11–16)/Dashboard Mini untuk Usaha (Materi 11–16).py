# Simulasi sistem kasir sederhana.

produk = {"Nasi Goreng": 25000, "Mie Ayam": 20000, "Es Teh": 5000}
penjualan = []

while True:
    print("\nMenu:")
    for i, (p, h) in enumerate(produk.items(), start=1):
        print(f"{i}. {p} - Rp{h}")
    pilih = input("Pilih produk (done untuk selesai): ")
    if pilih.lower() == "done":
        break
    if pilih in produk:
        penjualan.append(produk[pilih])
        print(f"{pilih} ditambahkan!")
    else:
        print("Produk tidak ada.")

print("\nTotal pendapatan hari ini:", sum(penjualan))

""" Bisa dikembangkan dengan fitur simpan ke file, variasi produk, dll. """   

