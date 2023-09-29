import tkinter as tk  # Import library tkinter untuk GUI
from tkinter import ttk, messagebox  # Import komponen-komponen dari tkinter dan messagebox
from ttkthemes import ThemedStyle  # Import tema ttk
import webbrowser  # Import library untuk mengarahkan ke alamat email saat teks hak cipta diklik
from PIL import Image, ImageTk
import os  # Import modul os untuk manajemen file dan direktori

# Tabel S-box yang digunakan dalam enkripsi
Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

# Tabel invers S-box yang digunakan dalam dekripsi
InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
)

# Tabel putaran konstan
Rcon = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)

# Fungsi untuk mengalikan byte dengan xtime
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

# Fungsi untuk mengonversi teks menjadi matriks byte
def text2matrix(text):
    matrix = []
    for i in range(16):
        byte = (text >> (8 * (15 - i))) & 0xFF
        if i % 4 == 0:
            matrix.append([byte])
        else:
            matrix[i // 4].append(byte)
    return matrix

# Fungsi untuk mengkonversi matriks menjadi teks
def matrix2text(matrix):
    text = 0
    for i in range(4):
        for j in range(4):
            text |= (matrix[i][j] << (8 * (15 - (4 * i + j))))
    return text

# Kelas AES yang digunakan untuk enkripsi dan dekripsi
class AES:
    def __init__(self, master_key):
        self.change_key(master_key)

    def change_key(self, master_key):
        # Inisialisasi kunci putaran
        self.round_keys = text2matrix(master_key)
        
        # Menghasilkan kunci putaran tambahan
        for i in range(4, 4 * 11):
            self.round_keys.append([])
            if i % 4 == 0:
                byte = self.round_keys[i - 4][0]        \
                     ^ Sbox[self.round_keys[i - 1][1]]  \
                     ^ Rcon[i // 4]
                self.round_keys[i].append(byte)

                for j in range(1, 4):
                    byte = self.round_keys[i - 4][j]    \
                         ^ Sbox[self.round_keys[i - 1][(j + 1) % 4]]
                    self.round_keys[i].append(byte)
            else:
                for j in range(4):
                    byte = self.round_keys[i - 4][j]    \
                         ^ self.round_keys[i - 1][j]
                    self.round_keys[i].append(byte)

    def encrypt(self, plaintext):
        self.plain_state = text2matrix(plaintext)

        self.add_round_key(self.plain_state, self.round_keys[:4])

        for i in range(1, 10):
            self.round_encrypt(self.plain_state, self.round_keys[4 * i : 4 * (i + 1)])

        self.sub_bytes(self.plain_state)
        self.shift_rows(self.plain_state)
        self.add_round_key(self.plain_state, self.round_keys[40:])

        return matrix2text(self.plain_state)

    def decrypt(self, ciphertext):
        self.cipher_state = text2matrix(ciphertext)

        self.add_round_key(self.cipher_state, self.round_keys[40:])
        self.inv_shift_rows(self.cipher_state)
        self.inv_sub_bytes(self.cipher_state)

        for i in range(9, 0, -1):
            self.round_decrypt(self.cipher_state, self.round_keys[4 * i : 4 * (i + 1)])

        self.add_round_key(self.cipher_state, self.round_keys[:4])

        return matrix2text(self.cipher_state)
    def add_round_key(self, s, k):
        for i in range(4):
            for j in range(4):
                s[i][j] ^= k[i][j]


    def round_encrypt(self, state_matrix, key_matrix):
        self.sub_bytes(state_matrix)
        self.shift_rows(state_matrix)
        self.mix_columns(state_matrix)
        self.add_round_key(state_matrix, key_matrix)


    def round_decrypt(self, state_matrix, key_matrix):
        self.add_round_key(state_matrix, key_matrix)
        self.inv_mix_columns(state_matrix)
        self.inv_shift_rows(state_matrix)
        self.inv_sub_bytes(state_matrix)

    def sub_bytes(self, s):
        for i in range(4):
            for j in range(4):
                s[i][j] = Sbox[s[i][j]]


    def inv_sub_bytes(self, s):
        for i in range(4):
            for j in range(4):
                s[i][j] = InvSbox[s[i][j]]


    def shift_rows(self, s):
        s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
        s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]


    def inv_shift_rows(self, s):
        s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
        s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]

    def mix_single_column(self, a):
        # please see Sec 4.1.2 in The Design of Rijndael
        t = a[0] ^ a[1] ^ a[2] ^ a[3]
        u = a[0]
        a[0] ^= t ^ xtime(a[0] ^ a[1])
        a[1] ^= t ^ xtime(a[1] ^ a[2])
        a[2] ^= t ^ xtime(a[2] ^ a[3])
        a[3] ^= t ^ xtime(a[3] ^ u)


    def mix_columns(self, s):
        for i in range(4):
            self.mix_single_column(s[i])


    def inv_mix_columns(self, s):
        # see Sec 4.1.3 in The Design of Rijndael
        for i in range(4):
            u = xtime(xtime(s[i][0] ^ s[i][2]))
            v = xtime(xtime(s[i][1] ^ s[i][3]))
            s[i][0] ^= u
            s[i][1] ^= v
            s[i][2] ^= u
            s[i][3] ^= v

        self.mix_columns(s)

# Fungsi untuk mengenkripsi teks
def encrypt_text():
    try:
        master_key_hex = master_key_entry.get("1.0", "end-1c")
        plaintext_hex = input_entry.get("1.0", "end-1c")  # Mengambil nilai dari input_entry

        # Konversi kunci dan plaintext dari heksadesimal ke bilangan bulat 128-bit
        master_key = int(master_key_hex, 16)
        plaintext = int(plaintext_hex, 16)

        # Pastikan panjang kunci adalah 128 bit (16 byte)
        if len(master_key_hex) != 32:
            messagebox.showerror("Error", "Panjang kunci harus 128 bit (32 karakter heksadesimal).")
            return

        # Padding plaintext menjadi kelipatan 128 bit
        while len(plaintext_hex) % 32 != 0:
            plaintext_hex = "0" + plaintext_hex

        aes = AES(master_key)
        ciphertext = aes.encrypt(plaintext)

        # Konversi hasil enkripsi ke format heksadesimal dan tampilkan di output
        result_entry.config(state='normal')  # Aktifkan mode tulis
        result_entry.delete("1.0", tk.END)
        result_entry.insert("1.0", hex(ciphertext)[2:].zfill(32).upper())
        result_entry.config(state='disabled')  # Nonaktifkan mode tulis
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid. Silakan masukkan nilai heksadesimal yang valid.")

# Fungsi untuk mengdekripsi teks
def decrypt_text():
    try:
        master_key_hex = master_key_entry.get("1.0", "end-1c")
        ciphertext_hex = input_entry.get("1.0", "end-1c")  # Mengambil nilai dari input_entry

        # Konversi kunci dari heksadesimal ke bilangan bulat 128-bit
        master_key = int(master_key_hex, 16)

        # Pastikan panjang kunci adalah 128 bit (16 byte)
        if len(master_key_hex) != 32:
            messagebox.showerror("Error", "Panjang kunci harus 128 bit (32 karakter heksadesimal).")
            return

        # Konversi ciphertext dari heksadesimal ke bilangan bulat 128-bit
        ciphertext = int(ciphertext_hex, 16)

        aes = AES(master_key)
        plaintext = aes.decrypt(ciphertext)

        # Konversi hasil dekripsi ke format heksadesimal dan tampilkan di output
        result_entry.config(state='normal')  # Aktifkan mode tulis
        result_entry.delete("1.0", tk.END)
        result_entry.insert("1.0", hex(plaintext)[2:].zfill(32).upper())
        result_entry.config(state='disabled')  # Nonaktifkan mode tulis
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid. Silakan masukkan nilai heksadesimal yang valid.")

def reset_text():
    input_entry.delete("1.0", tk.END)
    master_key_entry.delete("1.0", tk.END)
    result_entry.config(state='normal')
    result_entry.delete("1.0", tk.END)
    result_entry.config(state='disabled')

# Fungsi untuk menempatkan jendela di tengah
def center_window(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")

# Fungsi untuk keluar dari aplikasi
def exit_app():
    root.quit()

def show_about_info():
    # Gunakan teks judul jendela dan versi aplikasi untuk mengatur teks keterangan
    root_title = root.title()
    email = "imamsyt22@mhs.usk.ac.id"  # Ganti dengan alamat email Anda
    about_info = f"{root_title}\nVersi {app_version}\n\nDikembangkan oleh [Bukan Makmum]\nEmail: {email}"
    result = messagebox.showinfo("About", about_info, icon=messagebox.INFO)
    if result:
        open_github()

def open_github():
    webbrowser.open("https://github.com/BukanMakmum/AdvancedEncryptionStandard.git")  # Ganti dengan URL repositori GitHub Anda

# Membuat GUI
root = tk.Tk()
root.title("Advanced Encryption Standard")
app_version = "Education 1.0.beta"

# Tetapkan ukuran jendela (misalnya, 800x600)
root.geometry("650x245")

# Mencegah pengguna untuk mengubah ukuran jendela
root.resizable(False, False)

# Dapatkan direktori tempat script ini berada
current_directory = os.path.dirname(__file__) if os.path.dirname(__file__) else '.'

# Gabungkan path direktori dengan nama gambar latar belakang
#image_path = os.path.join(current_directory, "background.jpg")  # Ganti "background.jpg" dengan nama gambar Anda

# Baca gambar latar belakang
#background_image = Image.open(image_path)
#background_photo = ImageTk.PhotoImage(background_image)

# Tambahkan gambar sebagai latar belakang jendela utama
#background_label = tk.Label(root, image=background_photo)
#background_label.place(relwidth=1, relheight=1)

# Gabungkan direktori saat ini dengan nama file ikon favicon
favicon_path = os.path.join(current_directory, "favicon.ico")

# Atur favicon
root.iconbitmap(default=favicon_path)

style = ThemedStyle(root)
style.set_theme("arc")

# Membuat objek menu utama
menubar = tk.Menu(root)
root.config(menu=menubar)

# Membuat menu "File" tanpa garis putus-putus
file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu)

# Menambahkan opsi "Debug Result" di menu "File" dan menonaktifkannya saat pertama kali dibuat
file_menu.add_command(label="Debug Result", command="", state=tk.DISABLED)

# Menambahkan opsi "Exit" di menu "File" tanpa garis pemisah
file_menu.add_command(label="Exit", command=exit_app)

# Menambahkan opsi "About" di menu utama
menubar.add_command(label="About", command=show_about_info)

# Mengambil teks judul dari jendela
judul_jendela = root.title()

# Label judul dengan font yang lebih besar
title_label = ttk.Label(root, text=judul_jendela, font=("Helvetica", 14, "bold"), foreground="black")
title_label.grid(row=0, column=1, padx=10, pady=2)

# Label versi dengan font yang lebih kecil
version_label = ttk.Label(root, text=f"Versi {app_version}", font=("Helvetica", 10))
version_label.grid(row=1, column=1, padx=10, pady=2)

# Agar label versi berada di bawah label judul
title_label.grid(pady=(20, 0))

# Label untuk input plaintext/ciphertext
input_label = ttk.Label(root, text="Plaintext/Ciphertext (Hex):")
input_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Text widget untuk input teks plaintext/ciphertext
input_entry = tk.Text(root, height=1, width=40)
input_entry.grid(row=2, column=1, padx=10, pady=5)

# Label untuk input kunci
master_key_label = ttk.Label(root, text="Key (Hex):")
master_key_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Text widget untuk input kunci
master_key_entry = tk.Text(root, height=1, width=40)
master_key_entry.grid(row=3, column=1, padx=10, pady=5)

#Tombol Reset
reset_button = ttk.Button(root, text="Reset", command=reset_text)
reset_button.grid(row=4, column=0, padx=10, pady=10)

#Tombol Dekripsi
decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=4, column=1, padx=10, pady=10)

#Tombol Enkripsi
encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=4, column=2, padx=10, pady=10)

#Hasil/Output
result_label = ttk.Label(root, text="Output (Hex):")
result_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
result_entry = tk.Text(root, height=1, width=40, state='disabled')
result_entry.grid(row=5, column=1, padx=10, pady=5)

# #Dilarang hapus, sesama pengembang/pemrograman/mahasiswa/sarjana harus saling menghargai karya orang lain!
copyright_label = tk.Label(root, text="© 2023 BukanMakmum.", font=("Helvetica", 8, "bold"), foreground="grey", cursor="hand2")
copyright_label.grid(row=6, column=1, pady=(10, 20), sticky="nsew")
#Jika ingin berkontribusi silakan Clone Github berikut https://github.com/BukanMakmum/AdvancedEncryptionStandard.git
#User sangat menghargai kontribusi Anda, dengan menampilkan profil di halaman kontribusi. 

# Mengatur teks hak cipta menjadi rata tengah horizontal
#copyright_label.configure(anchor="center", justify="center")

def open_email(event):
    webbrowser.open("mailto:imamsayuti.usk@gmail.com")

# Menghubungkan fungsi dengan klik pada teks hak cipta
copyright_label.bind("<Button-1>", open_email)
# Panggil fungsi untuk menempatkan jendela di tengah
center_window(root)
root.mainloop()
