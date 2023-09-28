# Enkripsi dan Dekripsi AES

Implementasi sederhana algoritma Advanced Encryption Standard (AES) menggunakan Python dan pustaka Tkinter untuk antarmuka pengguna grafis.

## Daftar Isi

- [Pendahuluan](#pendahuluan)
- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Tangkapan Layar](#tangkapan-layar)
- [Lisensi](#lisensi)
- [Kontak](#kontak)

## Pendahuluan

Advanced Encryption Standard (AES) adalah algoritma kriptografi yang menjadi standar algoritma enkripsi kunci simetris pada saat ini. Dalam algoritma kriptografi AES 128, 1blok plainteks berukuran 128 bit
terlebih dahulu dikonversi menjadi matriks heksadesimal berukuran 4x4 yang disebut state. Setiap elemen state berukuran 1 byte. Proses enkripsi pada AES merupakan transformasi terhadap state secara berulang dalam 10 ronde. Setiap ronde AES membutuhkan satu  kunci hasil dari generasi kunci yang  menggunakan 2 transformasi yaitu subtitusi dan transformasi. Pada proses enkripsi AES mengunakan 4 transformasi dasar dengan urutan trasformasi subbytes, shiftrows, mixcolumns, dan addroundkey. Sedangkan pada proses dekripsi mengunakan invers semua transformasi dasar pada algoritma AES kecuali addroundkey dengan urutan transformasi invshiftrows, invsubbytes, addroundkey,dan invmixcolumns. Advanced Encryption Standard (AES) Education merupakan implementasi sederhana dari AES dalam Python untuk tujuan pendidikan dan demonstrasi.

## Fitur

- Enkripsi dan Dekripsi menggunakan AES;
- Input berupa 32 digit Heksadesimal;
- Output berupa 32 digit Heksadesimal;
- Validasi input key dan plaintext/ciphertext;
- Menampilkan dan simpan hasil Debug Result Enkripsi dan Dekripsi (Khusus v2.0.beta setelahnya)
- Reset input; dan
- Tampilan modern menggunakan tkinter/antarmuka grafis yang ramah pengguna.
  
- Contoh Input dan Output
  ```bash
  Plaintext:   00112233445566778899aabbccddeeff
  Key:         000102030405060708090a0b0c0d0e0f
  Ciphertext:  69c4e0d86a7b0430d8cdb78070b4c55a
   ```

## Instalasi

1. Clone repositori ini:

   ```bash
   git clone https://github.com/BukanMakmum/AdvancedEncryptionStandard.git
   ```

2. Masuk ke direktori proyek:

   ```bash
   cd AdvancedEncryptionStandard
   ```

3. Instal pustaka yang diperlukan:

   ```bash
   pip install tk
   pip install ttkthemes

   ```

## Penggunaan

1. Jalankan aplikasinya:

   ```bash
   AESvx.x.py atau AESvx.x.exe
   x.x = nomor versi
   ```

2. Masukkan teks biasa/teks sandi dan kunci dalam format heksadesimal.

3. Klik tombol "Enkripsi" atau "Dekripsi" sesuai kebutuhan.

4. Hasil akan ditampilkan di bidang "Hasil/Output".

## Tangkapan Layar



## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat berkas [LICENSE](LICENSE) untuk detailnya.

## Kontak

Untuk pertanyaan atau umpan balik, silakan hubungi pengembang:
- Nama: [Bukan Makmum]
- Email: [imamsyt22@mhs.usk.ac.id]

© 2023 BukanMakmum.
