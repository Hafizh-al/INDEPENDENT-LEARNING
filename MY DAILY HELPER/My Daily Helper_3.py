# my_daily_helper_gui_with_persistence.py
# My Daily Helper - GUI Tkinter + Persistent JSON storage
# Save/load data to data.json automatically.

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import re, random, string, json, os
from datetime import datetime

# -------------------------
# DATA DEFAULT (fallback)
# -------------------------
DATA_FILE = "data.json"

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

# -------------------------
# PERSISTENCE: load & save JSON
# -------------------------
def load_data():
    """Membaca data dari DATA_FILE jika ada; kalau tidak ada, pakai default."""
    global kontak, transaksi, menu_makanan, nilai, faq
    if not os.path.exists(DATA_FILE):
        return
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        # update only if keys exist to preserve defaults
        kontak = data.get("kontak", kontak)
        transaksi = data.get("transaksi", transaksi)
        menu_makanan = data.get("menu_makanan", menu_makanan)
        nilai = data.get("nilai", nilai)
        faq = data.get("faq", faq)
    except Exception as e:
        print("Gagal load data:", e)

def save_data():
    """Tulis data saat ini ke file JSON (data.json)."""
    try:
        data = {
            "kontak": kontak,
            "transaksi": transaksi,
            "menu_makanan": menu_makanan,
            "nilai": nilai,
            "faq": faq,
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Gagal save data:", e)

# muat data saat program mulai
load_data()

# -------------------------
# UTIL helpers
# -------------------------
def center_window(win, w=900, h=650):
    ws = win.winfo_screenwidth(); hs = win.winfo_screenheight()
    x = (ws // 2) - (w // 2); y = (hs // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")

def show_info(msg, title="Info"):
    messagebox.showinfo(title, msg)

def show_error(msg, title="Error"):
    messagebox.showerror(title, msg)

# -------------------------
# MAIN APP
# -------------------------
class MyDailyHelper(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Daily Helper (with Save/Load)")
        center_window(self, 1000, 700)
        self.create_menu()
        self.create_widgets()
        # tangani klik 'x' untuk autosave sebelum keluar
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    # ---------- menu bar (File -> Save/Load/Exit) ----------
    def create_menu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save Data", command=lambda: (save_data(), show_info("Data disimpan.")))
        filemenu.add_command(label="Load Data", command=lambda: (load_data(), self.refresh_all_views(), show_info("Data dimuat ulang.")))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.on_close)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)

    def on_close(self):
        """Autosave sebelum aplikasi ditutup."""
        save_data()
        self.destroy()

    # ---------- buat tab control dan setiap tab ----------
    def create_widgets(self):
        tabControl = ttk.Notebook(self)
        tabControl.pack(expand=1, fill="both", padx=8, pady=8)

        self.tab_kontak = ttk.Frame(tabControl); tabControl.add(self.tab_kontak, text="Kontak")
        self.tab_keuangan = ttk.Frame(tabControl); tabControl.add(self.tab_keuangan, text="Keuangan")
        self.tab_analisis = ttk.Frame(tabControl); tabControl.add(self.tab_analisis, text="Analisis Teks")
        self.tab_menu = ttk.Frame(tabControl); tabControl.add(self.tab_menu, text="Menu & Kasir")
        self.tab_reminder = ttk.Frame(tabControl); tabControl.add(self.tab_reminder, text="Reminder")
        self.tab_chat = ttk.Frame(tabControl); tabControl.add(self.tab_chat, text="Chatbot FAQ")
        self.tab_pass = ttk.Frame(tabControl); tabControl.add(self.tab_pass, text="PasswordGen")
        self.tab_nilai = ttk.Frame(tabControl); tabControl.add(self.tab_nilai, text="Nilai")
        self.tab_encrypt = ttk.Frame(tabControl); tabControl.add(self.tab_encrypt, text="Enkripsi")

        # builder per tab
        self.build_kontak_tab(); self.build_keuangan_tab(); self.build_analisis_tab()
        self.build_menu_tab(); self.build_reminder_tab(); self.build_chat_tab()
        self.build_pass_tab(); self.build_nilai_tab(); self.build_encrypt_tab()

    def refresh_all_views(self):
        """Panggil ini bila data baru dimuat dari file."""
        self.refresh_contacts_list()
        self.refresh_transactions_view()
        self.refresh_menu_list()
        self.refresh_nilai_view()

    # -------------------------
    # TAB Kontak
    # -------------------------
    def build_kontak_tab(self):
        frm = self.tab_kontak
        left = ttk.Frame(frm, padding=10); left.pack(side="left", fill="y")
        right = ttk.Frame(frm, padding=10); right.pack(side="right", expand=1, fill="both")

        ttk.Label(left, text="Nama:").pack(anchor="w")
        self.k_nama = ttk.Entry(left, width=25); self.k_nama.pack()
        ttk.Label(left, text="Nomor:").pack(anchor="w", pady=(6,0))
        self.k_nomor = ttk.Entry(left, width=25); self.k_nomor.pack()
        ttk.Button(left, text="Tambah Kontak", command=self.add_contact).pack(pady=8)
        ttk.Button(left, text="Hapus Kontak Terpilih", command=self.delete_contact).pack(pady=4)
        ttk.Button(left, text="Cari Kontak", command=self.search_contact).pack(pady=4)

        ttk.Label(right, text="Daftar Kontak:").pack(anchor="w")
        self.lst_kontak = tk.Listbox(right)
        self.lst_kontak.pack(expand=1, fill="both")
        self.refresh_contacts_list()

    def add_contact(self):
        nama = self.k_nama.get().strip(); nomor = self.k_nomor.get().strip()
        if not nama or not nomor: show_error("Nama dan nomor harus diisi"); return
        kontak[nama] = nomor
        self.k_nama.delete(0, 'end'); self.k_nomor.delete(0, 'end')
        self.refresh_contacts_list()
        save_data()  # simpan otomatis saat data berubah
        show_info("Kontak ditambahkan")

    def delete_contact(self):
        sel = self.lst_kontak.curselection()
        if not sel: show_error("Pilih kontak di list untuk dihapus"); return
        nama = self.lst_kontak.get(sel[0]).split(" -> ")[0]
        if messagebox.askyesno("Konfirmasi", f"Hapus kontak {nama}?"):
            kontak.pop(nama, None)
            self.refresh_contacts_list()
            save_data()
    
    def search_contact(self):
        q = simpledialog.askstring("Cari", "Masukkan nama yang dicari:")
        if not q: return
        hasil = {k:v for k,v in kontak.items() if q.lower() in k.lower()}
        if not hasil: show_info("Tidak ditemukan"); return
        self.lst_kontak.delete(0, 'end')
        for k, v in hasil.items(): self.lst_kontak.insert('end', f"{k} -> {v}")

    def refresh_contacts_list(self):
        self.lst_kontak.delete(0, 'end')
        for k, v in sorted(kontak.items()): self.lst_kontak.insert('end', f"{k} -> {v}")

    # -------------------------
    # TAB Keuangan
    # -------------------------
    def build_keuangan_tab(self):
        frm = self.tab_keuangan
        top = ttk.Frame(frm, padding=10); top.pack(fill="x")
        bottom = ttk.Frame(frm, padding=10); bottom.pack(expand=1, fill="both")

        ttk.Label(top, text="Deskripsi:").grid(row=0, column=0, sticky="w")
        self.t_desc = ttk.Entry(top, width=30); self.t_desc.grid(row=0, column=1, padx=6)
        ttk.Label(top, text="Nominal (+ masuk, - keluar):").grid(row=1, column=0, sticky="w", pady=(6,0))
        self.t_nom = ttk.Entry(top, width=20); self.t_nom.grid(row=1, column=1, padx=6, pady=(6,0))
        ttk.Button(top, text="Tambah", command=self.add_transaction).grid(row=0, column=2, rowspan=2, padx=8)

        self.txt_trans = tk.Text(bottom, height=12); self.txt_trans.pack(expand=1, fill="both")
        ttk.Button(bottom, text="Hitung Total", command=self.show_total).pack(pady=6)

        self.refresh_transactions_view()

    def add_transaction(self):
        desc = self.t_desc.get().strip()
        try: nom = float(self.t_nom.get().strip())
        except: show_error("Nominal harus angka (pakai titik untuk desimal)."); return
        transaksi.append((desc, nom))
        self.t_desc.delete(0, 'end'); self.t_nom.delete(0, 'end')
        self.refresh_transactions_view(); save_data()
        show_info("Transaksi ditambahkan")

    def refresh_transactions_view(self):
        self.txt_trans.delete('1.0', 'end')
        if not transaksi:
            self.txt_trans.insert('end', "Belum ada transaksi.\n"); return
        for d, n in transaksi: self.txt_trans.insert('end', f"{d}: {n}\n")

    def show_total(self):
        total = sum(n for _, n in transaksi); show_info(f"Total saldo: {total}")

    # -------------------------
    # TAB Analisis Teks
    # -------------------------
    def build_analisis_tab(self):
        frm = self.tab_analisis
        top = ttk.Frame(frm, padding=10); top.pack(fill="x")
        self.ana_file_label = ttk.Label(top, text="(Belum pilih file)")
        self.ana_file_label.pack(side="left")
        ttk.Button(top, text="Pilih File Teks", command=self.pick_text_file).pack(side="right")
        self.txt_ana = tk.Text(frm, height=20); self.txt_ana.pack(expand=1, fill="both", padx=10, pady=8)

    def pick_text_file(self):
        path = filedialog.askopenfilename(title="Pilih file teks", filetypes=[("Text Files","*.txt"),("All files","*.*")])
        if not path: return
        try:
            with open(path, "r", encoding="utf-8") as f: teks = f.read().lower()
        except Exception as e: show_error("Gagal baca file: " + str(e)); return
        self.ana_file_label.config(text=os.path.basename(path))
        bersih = re.sub(r'[^a-z0-9\s]', '', teks); kata = bersih.split()
        frek = {}
        for k in kata: frek[k] = frek.get(k, 0) + 1
        items = sorted(frek.items(), key=lambda x: x[1], reverse=True)[:20]
        self.txt_ana.delete('1.0', 'end')
        self.txt_ana.insert('end', f"Total kata: {len(kata)}\n\nTop kata:\n")
        for w, c in items: self.txt_ana.insert('end', f"{w} -> {c}\n")

    # -------------------------
    # TAB Menu & Kasir
    # -------------------------
    def build_menu_tab(self):
        frm = self.tab_menu
        left = ttk.Frame(frm, padding=10); left.pack(side="left", fill="y")
        right = ttk.Frame(frm, padding=10); right.pack(side="right", expand=1, fill="both")

        ttk.Label(left, text="Menu & Stok:").pack(anchor="w")
        self.lst_menu = tk.Listbox(left, height=10); self.lst_menu.pack()
        ttk.Button(left, text="Refresh Menu", command=self.refresh_menu_list).pack(pady=6)
        ttk.Button(left, text="Tambah Stok (pilih item)", command=self.add_stock_prompt).pack(pady=4)

        ttk.Label(right, text="Kasir - pilih produk lalu 'Tambah'").pack(anchor="w")
        self.combo_produk = ttk.Combobox(right, values=list(menu_makanan.keys())); self.combo_produk.pack(pady=6)
        ttk.Button(right, text="Tambah ke Keranjang", command=self.add_to_cart).pack()
        self.lst_cart = tk.Listbox(right, height=8); self.lst_cart.pack(expand=1, fill="both", pady=6)
        ttk.Button(right, text="Bayar (Checkout)", command=self.checkout).pack(pady=4)

        self.cart = []
        self.refresh_menu_list()

    def refresh_menu_list(self):
        self.lst_menu.delete(0, 'end')
        for m, info in menu_makanan.items(): self.lst_menu.insert('end', f"{m} - Rp{info['harga']} (Stok: {info['stok']})")
        self.combo_produk['values'] = list(menu_makanan.keys())

    def add_stock_prompt(self):
        sel = self.lst_menu.curselection()
        if not sel: show_error("Pilih item pada daftar menu terlebih dahulu"); return
        line = self.lst_menu.get(sel[0]); nama = line.split(" - ")[0]
        try: tambah = int(simpledialog.askstring("Tambah Stok", f"Berapa stok tambahan untuk {nama}?"))
        except: show_error("Masukkan angka valid"); return
        menu_makanan[nama]['stok'] += tambah
        self.refresh_menu_list(); save_data(); show_info("Stok diperbarui")

    def add_to_cart(self):
        nama = self.combo_produk.get()
        if not nama or nama not in menu_makanan: show_error("Pilih produk yang tersedia"); return
        if menu_makanan[nama]['stok'] <= 0: show_error("Stok habis!"); return
        menu_makanan[nama]['stok'] -= 1
        self.cart.append(menu_makanan[nama]['harga'])
        self.lst_cart.insert('end', nama)
        self.refresh_menu_list(); save_data()

    def checkout(self):
        if not self.cart: show_error("Keranjang kosong"); return
        total = sum(self.cart); show_info(f"Total bayar: Rp{total}")
        self.cart.clear(); self.lst_cart.delete(0, 'end')
        save_data()

    # -------------------------
    # TAB Reminder
    # -------------------------
    def build_reminder_tab(self):
        frm = self.tab_reminder
        top = ttk.Frame(frm, padding=10); top.pack(fill="x")
        ttk.Label(top, text="Nama tugas:").grid(row=0, column=0, sticky="w")
        self.r_name = ttk.Entry(top, width=30); self.r_name.grid(row=0, column=1, padx=6)
        ttk.Label(top, text="Deadline (YYYY-MM-DD):").grid(row=1, column=0, sticky="w", pady=(6,0))
        self.r_dead = ttk.Entry(top, width=20); self.r_dead.grid(row=1, column=1, pady=(6,0), padx=6)
        ttk.Button(top, text="Tambah Reminder", command=self.add_reminder).grid(row=0, column=2, rowspan=2, padx=8)
        self.txt_rem = tk.Text(frm, height=15); self.txt_rem.pack(expand=1, fill="both", padx=10, pady=8)

    def add_reminder(self):
        nama = self.r_name.get().strip(); d = self.r_dead.get().strip()
        if not nama or not d: show_error("Isi nama tugas dan deadline"); return
        try: dt = datetime.strptime(d, "%Y-%m-%d")
        except: show_error("Format tanggal harus YYYY-MM-DD"); return
        sisa = (dt - datetime.now()).days
        self.txt_rem.insert('end', f"{nama} - {d} (sisa {sisa} hari)\n")
        self.r_name.delete(0, 'end'); self.r_dead.delete(0, 'end')

    # -------------------------
    # TAB Chatbot
    # -------------------------
    def build_chat_tab(self):
        frm = self.tab_chat
        top = ttk.Frame(frm, padding=10); top.pack(fill="x")
        self.chat_entry = ttk.Entry(top, width=60); self.chat_entry.pack(side="left", padx=6)
        ttk.Button(top, text="Kirim", command=self.chat_send).pack(side="left")
        ttk.Button(top, text="Clear", command=lambda: self.chat_box.delete('1.0','end')).pack(side="left", padx=6)
        self.chat_box = tk.Text(frm, height=20); self.chat_box.pack(expand=1, fill="both", padx=10, pady=8)

    def chat_send(self):
        txt = self.chat_entry.get().strip(); 
        if not txt: return
        self.chat_box.insert('end', "Kamu: " + txt + "\n")
        key = txt.lower(); resp = faq.get(key, "Maaf, saya belum tahu jawabannya.")
        self.chat_box.insert('end', "Bot: " + resp + "\n"); self.chat_entry.delete(0, 'end')

    # -------------------------
    # TAB Password
    # -------------------------
    def build_pass_tab(self):
        frm = self.tab_pass
        ttk.Label(frm, text="Panjang password:").pack(pady=(10,0))
        self.spin_len = tk.Spinbox(frm, from_=6, to=64, width=6); self.spin_len.pack()
        ttk.Button(frm, text="Buat Password", command=self.make_password).pack(pady=6)
        self.pass_box = ttk.Entry(frm, width=50); self.pass_box.pack(pady=6)

    def make_password(self):
        try: ln = int(self.spin_len.get())
        except: show_error("Masukkan panjang valid"); return
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        pw = "".join(random.choice(chars) for _ in range(ln))
        self.pass_box.delete(0,'end'); self.pass_box.insert(0, pw)

    # -------------------------
    # TAB Nilai
    # -------------------------
    def build_nilai_tab(self):
        frm = self.tab_nilai
        top = ttk.Frame(frm, padding=10); top.pack(fill="x")
        ttk.Label(top, text="Nama:").grid(row=0, column=0)
        self.n_name = ttk.Entry(top, width=25); self.n_name.grid(row=0, column=1)
        ttk.Label(top, text="Nilai:").grid(row=1, column=0)
        self.n_score = ttk.Entry(top, width=15); self.n_score.grid(row=1, column=1)
        ttk.Button(top, text="Tambah Nilai", command=self.add_score).grid(row=0, column=2, rowspan=2, padx=8)
        self.txt_nilai = tk.Text(frm, height=12); self.txt_nilai.pack(expand=1, fill="both", padx=10, pady=8)
        self.refresh_nilai_view()

    def add_score(self):
        nama = self.n_name.get().strip()
        try: skor = float(self.n_score.get())
        except: show_error("Nilai harus angka"); return
        if not nama: show_error("Isi nama"); return
        nilai[nama] = skor
        self.n_name.delete(0,'end'); self.n_score.delete(0,'end')
        self.refresh_nilai_view(); save_data()

    def refresh_nilai_view(self):
        self.txt_nilai.delete('1.0','end')
        if not nilai: self.txt_nilai.insert('end', "Belum ada data nilai\n"); return
        for k,v in nilai.items(): self.txt_nilai.insert('end', f"{k}: {v}\n")
        rata = sum(nilai.values())/len(nilai); top = max(nilai, key=nilai.get)
        self.txt_nilai.insert('end', f"\nRata-rata: {rata:.2f}\nTop: {top} ({nilai[top]})\n")

    # -------------------------
    # TAB Enkripsi
    # -------------------------
    def build_encrypt_tab(self):
        frm = self.tab_encrypt
        ttk.Label(frm, text="Masukkan pesan:").pack(pady=(10,0))
        self.e_in = tk.Text(frm, height=5); self.e_in.pack(padx=10, pady=6)
        ttk.Label(frm, text="Geser (angka):").pack()
        self.e_shift = ttk.Entry(frm, width=6); self.e_shift.pack()
        ttk.Button(frm, text="Enkripsi", command=self.do_encrypt).pack(pady=6)
        self.e_out = tk.Text(frm, height=8); self.e_out.pack(expand=1, fill="both", padx=10, pady=6)

    def do_encrypt(self):
        pes = self.e_in.get('1.0','end').strip()
        try: ges = int(self.e_shift.get().strip())
        except: show_error("Masukkan angka untuk geser"); return
        out = ""
        for ch in pes:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                out += chr((ord(ch) - base + ges) % 26 + base)
            else:
                out += ch
        self.e_out.delete('1.0','end'); self.e_out.insert('end', out)

# -------------------------
# RUN APP
# -------------------------
if __name__ == "__main__":
    app = MyDailyHelper()
    app.mainloop()
