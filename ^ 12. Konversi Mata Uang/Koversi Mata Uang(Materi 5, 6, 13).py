# Globalisasi dan Kerja Remote
# Konversi Mata Uang

def konversi_mata_uang(jumlah, dari, ke):
    rates = {
        "USD": 1.0,        # Dolar AS
        "EUR": 0.85,       # Euro
        "IDR": 14000.0,    # Rupiah Indonesia
        "JPY": 110.0,      # Yen Jepang
        "GBP": 0.75,       # Poundsterling Inggris
        "SAUD": 3.75,      # Riyal Saudi
        "KWD": 0.30,       # Dinar Kuwait
        "CNY": 6.5,        # Yuan Tiongkok
        "KRW": 1200.0,     # Won Korea Selatan
        "VND": 23000.0,    # Dong Vietnam
        "QAR": 3.64,       # Riyal Qatar
        "UND": 0.000025,   # Dinar Uni Emirat Arab
        "RUB": 75.0,       # Rubel Rusia
        "YER": 250.0,      # Rial Yaman
        "INR": 75.0,       # Rupee India
        "OMR": 0.38,       # Rial Oman
        "AED": 3.67,       # Dirham Uni Emirat Arab
        "SGD": 1.35,       # Dolar Singapura
        "MYR": 4.15,       # Ringgit Malaysia
        "HKD": 7.8,        # Dolar Hong Kong
        "JOD": 0.71,       # Dinar Yordania
        "XAU": 0.00058,    # Emas (per troy ounce)
        "CAD": 1.25,       # Dolar Kanada
        "AUD": 1.30,       # Dolar Australia
        "CHF": 0.92,       # Franc Swiss
        "XAG": 0.035,      # Perak (per troy ounce)
        "EGP": 15.7,       # Pound Mesir
        "TRY": 8.5,        # Lira Turki
        "BRL": 5.2,        # Real Brasil
        "OTHR": 1.0,       # Mata uang lain (placeholder)
        "SEK": 8.6,        # Krona Swedia
        "NOK": 8.9,        # Krone Norwegia
        "DKK": 6.3,        # Krone Denmark
        "ZAR": 14.5,       # Rand Afrika Selatan
        "MXN": 20.0,       # Peso Meksiko
        "NZD": 1.4,        # Dolar Selandia Baru
        "MOP": 8.0,        # Pataca Makau
        "THB": 33.0,       # Baht Thailand
        "PHP": 50.0,       # Peso Filipina
        "CLP": 750.0       # Peso Chili
    }
    
    if dari not in rates or ke not in rates:
        raise ValueError("Mata uang tidak didukung.")
    
    # Konversi ke USD dulu, lalu ke mata uang tujuan
    jumlah_usd = jumlah / rates[dari]
    jumlah_tujuan = jumlah_usd * rates[ke]
    
    return jumlah_tujuan


# Contoh penggunaan
try:
    jumlah = float(input("Masukkan jumlah uang: "))
    dari = input("Dari mata uang (USD, EUR, IDR, JPY, GBP, SAUD, KWD, CNY, KRW, VND, QAR): ").upper()
    ke = input("Ke mata uang (USD, EUR, IDR, JPY, GBP, SAUD, KWD, CNY, KRW, VND, QAR): ").upper()
    
    hasil = konversi_mata_uang(jumlah, dari, ke)
    print(f"{jumlah} {dari} = {hasil:.2f} {ke}")
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Terjadi kesalahan:", e)
""" Bisa dikembangkan dengan fitur simpan ke file, variasi mata uang, dll. """
# Relevansi: Berguna untuk bisnis internasional, kerja remote.
# Bisa dipakai di e-commerce, aplikasi keuangan, dll.
# Konversi mata uang penting untuk transaksi lintas negara.
# Bisa dikembangkan dengan fitur simpan ke file, variasi mata uang, dll.
