import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu  # Tambahkan ini untuk mengimpor modul menu
from ttkthemes import ThemedStyle
from tkinter import scrolledtext  # Import the scrolledtext module
from tkinter import filedialog
import webbrowser # Fungsi untuk mengarahkan ke alamat email saat teks hak cipta diklik
from PIL import Image, ImageTk
import os

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

# Function to convert text to a 4x4 byte matrix (128-bit)
def text2matrix(text):
    matrix = []

    for i in range(16):
        byte = (text >> (8 * (15 - i))) & 0xFF
        if i % 4 == 0:
            matrix.append([byte])
        else:
            matrix[i // 4].append(byte)

    # Return the matrix as usual
    return matrix

# Fungsi untuk mengkonversi matriks menjadi teks
def matrix2text(matrix):
    text = 0
    for i in range(4):
        for j in range(4):
            text |= (matrix[i][j] << (8 * (15 - (4 * i + j))))
    return text

class AES:
    def __init__(self, master_key):
        self.change_key(master_key)

    def change_key(self, master_key):
        global debug_results  # Add global variable
        debug_results.append("")  # Debug: Add an empty line as a separator
        debug_results.append("Ekspansi Kunci AES:")
        debug_results.append("Original Key:")
        debug_results.append("{:032X}".format(int(master_key)))

        # Initialize round keys
        self.round_keys = text2matrix(master_key)

        # Generate additional round keys
        for i in range(4, 4 * 11):
            self.round_keys.append([])

            if i % 4 == 0:
                debug_results.append("\nRound {} RotWord:".format(i // 4))  # Debug: Add RotWord() statement
                # RotWord()
                word = [self.round_keys[i - 1][1], self.round_keys[i - 1][2], self.round_keys[i - 1][3], self.round_keys[i - 1][0]]
                debug_results.append("Rotated Word (Hex): {:02X} {:02X} {:02X} {:02X}".format(
                    word[0], word[1], word[2], word[3]))
                debug_results.append("Rotated Word (Binary): {:08b} {:08b} {:08b} {:08b}".format(
                    word[0], word[1], word[2], word[3]))

                # SubWord() using S-Box
                debug_results.append("\nRound {} SubWord:".format(i // 4))  # Debug: Add SubWord() statement
                debug_results.append("Input Word (Hex): {:02X} {:02X} {:02X} {:02X}".format(
                    word[0], word[1], word[2], word[3]))
                debug_results.append("Input Word (Binary): {:08b} {:08b} {:08b} {:08b}".format(
                    word[0], word[1], word[2], word[3]))

                for j in range(4):
                    word[j] = Sbox[word[j]]

                debug_results.append("Output Word (Hex): {:02X} {:02X} {:02X} {:02X}".format(
                    word[0], word[1], word[2], word[3]))
                debug_results.append("Output Word (Binary): {:08b} {:08b} {:08b} {:08b}".format(
                    word[0], word[1], word[2], word[3]))

                # XOR word with Rcon
                debug_results.append("\nRound {} Rcon:".format(i // 4))  # Debug: Add Rcon() statement
                debug_results.append("Rcon Value (Hex): {:02X}".format(Rcon[i // 4]))
                debug_results.append("Rcon Value (Binary): {:08b}".format(Rcon[i // 4]))
                word[0] ^= Rcon[i // 4]
                debug_results.append("Y ⊕ Rcon (Hex): {:02X} {:02X} {:02X} {:02X}".format(
                    word[0], word[1], word[2], word[3]))
                debug_results.append("Y ⊕ Rcon (Binary): {:08b} {:08b} {:08b} {:08b}".format(
                    word[0], word[1], word[2], word[3]))
                word[1] ^= 0x00
                word[2] ^= 0x00
                word[3] ^= 0x00

                # XOR word with the previous key
                self.round_keys[i].append(word[0] ^ self.round_keys[i - 4][0])
                self.round_keys[i].append(word[1] ^ self.round_keys[i - 4][1])
                self.round_keys[i].append(word[2] ^ self.round_keys[i - 4][2])
                self.round_keys[i].append(word[3] ^ self.round_keys[i - 4][3])
            else:
                # Calculate the next round key bytes
                for j in range(4):
                    byte = self.round_keys[i - 4][j] ^ self.round_keys[i - 1][j]
                    self.round_keys[i].append(byte)

        # Debug statements to record round keys for each round (0 to 10)
        for i in range(11):
            debug_text = "\n" + f"Round {i} Key (Hex):\n"
            debug_text += "\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.round_keys[i * 4:i * 4 + 4]])
            debug_results.append(debug_text)  # Use the global variable debug_results

            debug_text_binary = "\n" + f"Round {i} Key (Binary):\n"
            debug_text_binary += "\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.round_keys[i * 4:i * 4 + 4]])
            debug_results.append(debug_text_binary)  # Use the global variable debug_results

    def encrypt(self, plaintext):
        global debug_results  # Tambahkan variabel global
        debug_results.append("\n")  # Baris kosong
        debug_results.append("Encrypt:")
        
        # Debug: Menambahkan plaintext asli ke hasil debug
        original_plaintext = int(plaintext)
        debug_results.append("Original Plaintext:")
        debug_results.append("{:032X}".format(original_plaintext))

        self.plain_state = text2matrix(plaintext)

        # Debug: Menambahkan input state 4x4 (format heksadesimal dan biner) ke hasil debug
        debug_results.append("\n"+"Input State (4x4) Hex:")
        debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.plain_state]))
        debug_results.append("\n"+"Input State (4x4) Binary:")
        debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.plain_state])+"\n")

        self.add_round_key(self.plain_state, self.round_keys[:4])
        
        # Debug: Menambahkan hasil AddRoundKey (format heksadesimal dan biner) ke hasil debug
        debug_results.append("After AddRoundKey Hex:")
        debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.plain_state]))
        debug_results.append("\n"+"After AddRoundKey Binary:")
        debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.plain_state])+"\n")

        for i in range(1, 10):
            debug_results.append(f"\nRound {i} SubBytes:")
            self.sub_bytes(self.plain_state)  # SubBytes sebelum putaran
            debug_results.append(f"Matrix SubBytes round {i}:")
            debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.plain_state])+"\n")
            debug_results.append(f"Binary SubBytes round {i}:")
            debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.plain_state])+"\n")

            debug_results.append(f"\nRound {i} ShiftRows:")
            self.shift_rows(self.plain_state)  # ShiftRows
            debug_results.append(f"Matrix ShiftRows round {i}:")
            debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.plain_state])+"\n")
            debug_results.append(f"Binary ShiftRows round {i}:")
            debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.plain_state])+"\n")

            debug_results.append(f"\nRound {i} MixColumns:")
            self.mix_columns(self.plain_state)  # MixColumns
            debug_results.append(f"Matrix MixColumns round {i}:")
            debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.plain_state])+"\n")
            debug_results.append(f"Binary MixColumns round {i}:")
            debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.plain_state])+"\n")

            debug_results.append(f"\nRound {i} AddRoundKey:")
            self.add_round_key(self.plain_state, self.round_keys[4 * i : 4 * (i + 1)])
            debug_results.append(f"Matrix AddRoundKey round {i}:")
            debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.plain_state])+"\n")
            debug_results.append(f"Binary AddRoundKey round {i}:")
            debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.plain_state])+"\n")

        debug_results.append("\nFinal SubBytes:")
        self.sub_bytes(self.plain_state)  # SubBytes terakhir sebelum Final AddRoundKey
        debug_results.append("Matrix Final SubBytes:")
        debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.plain_state])+"\n")
        debug_results.append("Binary Final SubBytes:")
        debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.plain_state])+"\n")

        debug_results.append("\nFinal ShiftRows:")
        self.shift_rows(self.plain_state)  # ShiftRows terakhir
        debug_results.append("Matrix Final ShiftRows:")
        debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.plain_state])+"\n")
        debug_results.append("Binary Final ShiftRows:")
        debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.plain_state])+"\n")

        debug_results.append("\nFinal AddRoundKey:")
        self.add_round_key(self.plain_state, self.round_keys[40:])
        debug_results.append("Matrix Final AddRoundKey:")
        debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.plain_state])+"\n")
        debug_results.append("Binary Final AddRoundKey:")
        debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.plain_state])+"\n")

        return matrix2text(self.plain_state)

    def decrypt(self, ciphertext):
        global debug_results  # Tambahkan variabel global
        debug_results.append("\n")  # Baris kosong
        debug_results.append("Decrypt:")
        self.cipher_state = text2matrix(ciphertext)

        # Debug: Menambahkan ciphertext asli ke hasil debug
        original_ciphertext = int(ciphertext)
        debug_results.append("Original Ciphertext:")
        debug_results.append("{:032X}".format(original_ciphertext))

        # Debug: Menambahkan input state 4x4 (format heksadesimal dan biner) ke hasil debug
        debug_results.append("\n"+"Input State (4x4) Hex:")
        debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.cipher_state]))
        debug_results.append("\n"+"Input State (4x4) Binary:")
        debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")

        self.add_round_key(self.cipher_state, self.round_keys[40:])
        
        # Debug: Menambahkan hasil AddRoundKey (format heksadesimal dan biner) ke hasil debug
        debug_results.append("After AddRoundKey Hex:")
        debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.cipher_state]))
        debug_results.append("\n"+"After AddRoundKey Binary:")
        debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.cipher_state])+ "\n")

        self.inv_shift_rows(self.cipher_state)
        
        # Debug: Menambahkan hasil InvShiftRows (format heksadesimal dan biner) ke hasil debug
        debug_results.append("\n"+"After InvShiftRows Hex:")
        debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.cipher_state]))
        debug_results.append("\n"+"After InvShiftRows Binary:")
        debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")

        self.inv_sub_bytes(self.cipher_state)
        
        # Debug: Menambahkan hasil InvSubBytes (format heksadesimal dan biner) ke hasil debug
        debug_results.append("\n"+"After InvSubBytes Hex:")
        debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.cipher_state]))
        debug_results.append("\n"+"After InvSubBytes Binary:")
        debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")

        for i in range(9, 0, -1):
            debug_results.append(f"\nRound {9 - i} AddRoundKey (Decrypt):")
            self.add_round_key(self.cipher_state, self.round_keys[4 * i : 4 * (i + 1)])
            debug_results.append(f"Matrix AddRoundKey round {9 - i}:")
            debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")
            debug_results.append(f"Binary AddRoundKey round {9 - i}:")
            debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")

            debug_results.append(f"\nRound {9 - i} InvMixColumns (Decrypt):")
            self.inv_mix_columns(self.cipher_state)
            debug_results.append(f"Matrix InvMixColumns round {9 - i}:")
            debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")
            debug_results.append(f"Binary InvMixColumns round {9 - i}:")
            debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")

            debug_results.append(f"\nRound {9 - i} InvShiftRows (Decrypt):")
            self.inv_shift_rows(self.cipher_state)
            debug_results.append(f"Matrix InvShiftRows round {9 - i}:")
            debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")
            debug_results.append(f"Binary InvShiftRows round {9 - i}:")
            debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")

            debug_results.append(f"\nRound {9 - i} InvSubBytes (Decrypt):")
            self.inv_sub_bytes(self.cipher_state)  # InvSubBytes sebelum putaran dekripsi
            debug_results.append(f"Matrix InvSubBytes round {9 - i}:")
            debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")
            debug_results.append(f"Binary InvSubBytes round {9 - i}:")
            debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")

        debug_results.append("\nRound 10 AddRoundKey (Decrypt):")
        self.add_round_key(self.cipher_state, self.round_keys[:4])
        debug_results.append("\nMatrix Final AddRoundKey:")
        debug_results.append("\n".join([" ".join(["{:02X}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")
        debug_results.append("\nBinary Final AddRoundKey:")
        debug_results.append("\n".join([" ".join(["{:08b}".format(byte) for byte in row]) for row in self.cipher_state])+"\n")

        return matrix2text(self.cipher_state)

    
    def add_round_key(self, plaintext, key):
        global debug_results
        debug_results.append("Add Round Key:")

         # Menampilkan Plaintext asli sebelum operasi Add Round Key
        debug_results.append("Plaintext Asli:")
        for i in range(4):
            for j in range(4):
                plaintext_hex = hex(plaintext[i][j])[2:].zfill(2)  # Format heksadesimal dua digit
                plaintext_bin = format(plaintext[i][j], '08b')  # Konversi ke binary 8-bit
                key_hex = hex(key[i][j])[2:].zfill(2)  # Format heksadesimal dua digit
                key_bin = format(key[i][j], '08b')  # Konversi ke binary 8-bit
                xor_result = plaintext[i][j] ^ key[i][j]  # Hasil XOR
                xor_result_hex = hex(xor_result)[2:].zfill(2)  # Format heksadesimal dua digit
                xor_result_bin = format(xor_result, '08b')  # Konversi ke binary 8-bit
                debug_results.append(f"Plaintext[{i}][{j}]= {plaintext_hex} (Hex), {plaintext_bin} (Binary) \nKey[{i}][{j}]= {key_hex} (Hex), {key_bin} (Binary) \nXOR Result= {xor_result_hex} (Hex), {xor_result_bin} (Binary)\n")

        # Operasi XOR antara plaintext dan key
        for i in range(4):
            for j in range(4):
                plaintext[i][j] ^= key[i][j]

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
        global debug_results
        
        for i in range(4):
            for j in range(4):
                row_index = hex(i)[2:]
                col_index = hex(j)[2:]
                original_byte = s[i][j]
                original_byte_hex = hex(original_byte)[2:].zfill(2)  # Ubah ke heksadesimal dengan panjang 2 karakter
                
                index_baris = original_byte_hex[0]  # Ambil digit pertama
                index_kolom = original_byte_hex[1]  # Ambil digit kedua
                
                sub_byte_hex = hex(Sbox[original_byte])[2:].zfill(2)
                
                debug_results.extend([f"State S{row_index}.{col_index}: {original_byte_hex} \nIndek baris: {index_baris} \nIndek kolom: {index_kolom} \nSubByte: {sub_byte_hex}\n"])
        
                s[i][j] = Sbox[original_byte]
        
        return s

    def inv_sub_bytes(self, s):
        for i in range(4):
            for j in range(4):
                s[i][j] = InvSbox[s[i][j]]

    def shift_rows(self, s):        
        # Implementasi ShiftRows
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
    global encryption_done
     # Hapus hasil debug yang sudah ada
    debug_results.clear()

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
    global encryption_done
     # Hapus hasil debug yang sudah ada
    debug_results.clear()

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

# Global variable to store debug results
global debug_results
debug_results = []

# Initialize the debug_text_widget variable
debug_text_widget = None

# Variabel global untuk melacak apakah enkripsi atau dekripsi telah dilakukan
encryption_done = False

# Inisialisasi global variable
debug_option_enabled = False

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

def open_email(event):
    webbrowser.open("mailto:imamsayuti.usk@gmail.com")

# Fungsi untuk mengaktifkan atau menonaktifkan opsi "Debug Result"
def toggle_debug_option():
    global debug_option_enabled
    debug_option_enabled = not debug_option_enabled
    if debug_option_enabled:
        file_menu.entryconfig("Debug Result", state=tk.NORMAL)
    else:
        file_menu.entryconfig("Debug Result", state=tk.DISABLED)

# Function to open the debug window
def open_debug_result(debug_text):
    global debug_window, debug_text_widget  # Menetapkan variabel global
    debug_window = None  # Inisialisasi variabel debug_window

    if debug_window is not None:
        # Jika jendela debug sudah ada, tutup terlebih dahulu
        debug_window.destroy()

    debug_window = tk.Toplevel(root)
    debug_window.title("Debug Result")  # 

    # Atur ukuran jendela debug (misalnya, 1000x600 piksel)
    debug_window.geometry("600x300")

    # Mendapatkan ukuran layar
    screen_width = debug_window.winfo_screenwidth()
    screen_height = debug_window.winfo_screenheight()

    # Menghitung posisi x dan y untuk memusatkan jendela
    x = (screen_width - 600) // 2
    y = (screen_height - 300) // 2

    # Menetapkan posisi jendela di tengah
    debug_window.geometry(f"600x300+{x}+{y}")

    # Create a scrolled text widget in the debug window
    debug_text_widget = scrolledtext.ScrolledText(debug_window, wrap=tk.WORD)
    debug_text_widget.pack(fill=tk.BOTH, expand=True)  # Mengisi dan memperluas widget ke seluruh jendela

    # Show the debug text in the scrolled text widget
    debug_text_widget.insert(tk.END, debug_text)

    # Create a menu bar for the debug window
    menubar = Menu(debug_window)
    debug_window.config(menu=menubar)

    # Create a "File" menu in the debug window
    file_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)

    # Add a "Save" option to the "File" menu
    file_menu.add_command(label="Save", command=save_debug_text)

    # Add an "Exit" option to the "File" menu that closes the debug window
    file_menu.add_command(label="Exit", command=debug_window.destroy)

# Function to close the debug window
def close_debug_window():
    global debug_text_widget
    if debug_text_widget is not None:
        debug_text_widget.destroy()

# Function to save debug text to a file
def save_debug_text():
    global debug_text_widget
    if debug_text_widget is not None:
        debug_text = debug_text_widget.get("1.0", tk.END)

        # Replace ⊕ with ^ or + or other suitable symbol
        debug_text = debug_text.replace("⊕", "^")  # You can replace with a different symbol if needed

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )

        if file_path:
            with open(file_path, "w") as file:
                file.write(debug_text)

# Fungsi untuk menggabungkan hasil debug dari berbagai bagian fungsi enkripsi
def handle_debug_result():
    global debug_results  # Tambahkan variabel global

    key = master_key_entry.get("1.0", "end-1c")
    if not key:
        messagebox.showerror("Error", "Jalankan Enkripsi atau Dekripsi sebelum mengklik Debug Result.")
        return  # Keluar dari fungsi jika kunci kosong

    # Membuat teks hasil debug
    debug_result = []
    debug_result.append("Hasil Debug:")

    # Tambahkan hasil debug dari berbagai bagian fungsi enkripsi ke dalam daftar debug_result
    for debug_text in debug_results:
        debug_result.append(str(debug_text))  # Ubah hasil debug menjadi string dan tambahkan ke hasil debug

    # Menggabungkan hasil debug menjadi satu string
    debug_text = "\n".join(debug_result)

    # Menampilkan hasil debug di jendela debug
    open_debug_result(debug_text)

# Fungsi saat cursor masuk ke tombol
def on_enter(event):
    event.widget.config(bg=event.widget.highlight_color, fg='white')

# Fungsi saat cursor meninggalkan tombol
def on_leave(event):
    event.widget.config(bg=event.widget.original_color, fg='black')

# Membuat GUI
root = tk.Tk()
root.title("Advanced Encryption Standard")
app_version = "Education 2.0.beta"
root.configure(bg="#2596be")  # Mengatur warna latar belakang jendela utama

# Tentukan ukuran jendela
window_width = 650
window_height = 245
root.geometry(f"{window_width}x{window_height}")

# Mencegah pengguna untuk mengubah ukuran jendela
root.resizable(False, False)

# Dapatkan direktori tempat script ini berada
current_directory = os.path.dirname(__file__) if os.path.dirname(__file__) else '.'


#Gabungkan path direktori dengan nama gambar latar belakang
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
style.set_theme("adapta")

# Membuat objek menu utama
menubar = tk.Menu(root)
root.config(menu=menubar)

# Membuat menu "File" tanpa garis putus-putus
file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu)

# Menambahkan opsi "Debug Result" di menu "File" dan menonaktifkannya saat pertama kali dibuat
file_menu.add_command(label="Debug Result", command=handle_debug_result, state=tk.DISABLED)

# Menambahkan opsi "Exit" di menu "File" tanpa garis pemisah
file_menu.add_command(label="Exit", command=exit_app)

# Menambahkan opsi "About" di menu utama
menubar.add_command(label="About", command=show_about_info)

judul_jendela = root.title()

# Label judul dengan font yang lebih besar
title_label = ttk.Label(root, text=judul_jendela, font=("Helvetica", 14, "bold"), foreground="black", background=root.cget('bg'))
title_label.grid(row=0, column=1, padx=10, pady=2)

# Label versi dengan font yang lebih kecil
version_label = ttk.Label(root, text=f"Versi {app_version}", font=("Helvetica", 10), background=root.cget('bg'))
version_label.grid(row=1, column=1, padx=10, pady=2)

# Agar label versi berada di bawah label judul
title_label.grid(pady=(20, 0))

# Label untuk input plaintext/ciphertext
input_label = ttk.Label(root, text="Plaintext/Ciphertext (Hex):", foreground="black", background=root.cget('bg'))
input_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Text widget untuk input teks plaintext/ciphertext
input_entry = tk.Text(root, height=1, width=40)
input_entry.grid(row=2, column=1, padx=5, pady=5)

# Label untuk input kunci
master_key_label = ttk.Label(root, text="Key (Hex):", foreground="black", background=root.cget('bg'))
master_key_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

# Text widget untuk input kunci
master_key_entry = tk.Text(root, height=1, width=40)
master_key_entry.grid(row=3, column=1, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset", width=6, height=1, command=reset_text)
reset_button.grid(row=4, column=0, padx=(10, 5), pady=10, sticky="e")
# Menetapkan warna latar belakang saat disorot dan warna latar belakang asli
reset_button.highlight_color = 'red'  # Warna latar belakang saat disorot
reset_button.original_color = 'SystemButtonFace'  # Warna latar belakang asli
reset_button.bind("<Enter>", on_enter)
reset_button.bind("<Leave>", on_leave)

decrypt_button = tk.Button(root, text="Decrypt", width=6, height=1, command=decrypt_text)
decrypt_button.grid(row=4, column=1, padx=5, pady=10)
# Menetapkan warna latar belakang saat disorot dan warna latar belakang asli
decrypt_button.highlight_color = 'green'  # Warna latar belakang saat disorot
decrypt_button.original_color = 'SystemButtonFace'  # Warna latar belakang asli
decrypt_button.bind("<Enter>", on_enter)
decrypt_button.bind("<Leave>", on_leave)

encrypt_button = tk.Button(root, text="Encrypt", width=6, height=1, command=encrypt_text)
encrypt_button.grid(row=4, column=2, padx=5, pady=10, sticky="w")
# Menetapkan warna latar belakang saat disorot dan warna latar belakang asli
encrypt_button.highlight_color = 'blue'  # Warna latar belakang saat disorot
encrypt_button.original_color = 'SystemButtonFace'  # Warna latar belakang asli
encrypt_button.bind("<Enter>", on_enter)
encrypt_button.bind("<Leave>", on_leave)

#Hasil/Output
result_label = ttk.Label(root, text="Output (Hex):", foreground="black", background=root.cget('bg'))
result_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
result_entry = tk.Text(root, height=1, width=40, bg="light gray", state='disabled')
result_entry.grid(row=5, column=1, padx=5, pady=5)

# #Dilarang hapus, sesama pengembang/pemrograman/mahasiswa/sarjana harus saling menghargai karya orang lain!
copyright_label = tk.Label(root, text="© 2023 BukanMakmum.", font=("Helvetica", 8, "bold"), foreground="#fbf7f6", cursor="hand2", background=root.cget('bg'))
copyright_label.grid(row=6, column=1, pady=(10, 20), sticky="nsew")
"""
Jika ingin berkontribusi silakan Clone Github berikut https://github.com/BukanMakmum/AdvancedEncryptionStandard.git
#User sangat menghargai kontribusi Anda, dengan menampilkan profil di halaman kontribusi. 

# Mengatur teks hak cipta menjadi rata tengah horizontal
#copyright_label.configure(anchor="center", justify="center")
"""
# Menghubungkan fungsi dengan klik pada teks hak cipta
copyright_label.bind("<Button-1>", open_email)

# Setelah enkripsi selesai, aktifkan opsi "Debug Result"
toggle_debug_option()

# Panggil fungsi untuk menempatkan jendela di tengah
center_window(root)

root.mainloop()