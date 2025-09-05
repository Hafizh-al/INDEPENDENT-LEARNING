# Berguna untuk otomasi customer service sederhana.

import re      # import modul regex

while True:
    pesan = input("Anda: ")
    if pesan.lower() in ['exit', 'quit', 'keluar', 'bye', 'sampai jumpa', 'dadah', 'dah']:
        print("Chatbot: Terima kasih! Sampai jumpa lagi.")
        break

    # Respon sederhana berdasarkan kata kunci
    if re.search(r'\b(hai|halo|hello|hi|Assalamualaikum)\b', pesan, re.IGNORECASE):     # \b → batas kata   # re.IGNORECASE → abaikan besar/kecil
        print("Chatbot: Halo/Waalaikumussalam! Ada yang bisa saya bantu?")
    elif re.search(r'\b(bantuan|help|butuh bantuan)\b', pesan, re.IGNORECASE):
        print("Chatbot: Tentu! Silakan jelaskan masalah Anda.")
    elif re.search(r'\b(terima kasih|makasih|thanks)\b', pesan, re.IGNORECASE):
        print("Chatbot: Sama-sama! Senang bisa membantu.")
    else:
        print("Chatbot: Maaf, saya tidak mengerti. Bisa ulangi?")

""" Bisa dikembangkan dengan fitur simpan ke file, variasi respon, dll. """
# Relevansi: Berguna untuk otomasi customer service sederhana.
# bisa dikembangkan jadi AI chatbot yang lebih canggih.
# Bisa dipakai di website, aplikasi, dll.
