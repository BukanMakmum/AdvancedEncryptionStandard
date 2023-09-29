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

<p style="text-align: justify;">Advanced Encryption Standard (AES) adalah algoritma kriptografi yang menjadi standar algoritma enkripsi kunci simetris pada saat ini. Dalam algoritma kriptografi AES 128, 1 blok plainteks berukuran 128 bit terlebih dahulu dikonversi menjadi matriks heksadesimal berukuran 4x4 yang disebut state. Setiap elemen state berukuran 1 byte. Proses enkripsi pada AES merupakan transformasi terhadap state secara berulang dalam 10 ronde. Setiap ronde AES membutuhkan satu kunci hasil dari generasi kunci yang menggunakan 2 transformasi yaitu substitusi dan transformasi. Pada proses enkripsi AES menggunakan 4 transformasi dasar dengan urutan transformasi subbytes, shiftrows, mixcolumns, dan addroundkey. Sedangkan pada proses dekripsi menggunakan invers semua transformasi dasar pada algoritma AES kecuali addroundkey dengan urutan transformasi invshiftrows, invsubbytes, addroundkey, dan invmixcolumns. Advanced Encryption Standard (AES) Education merupakan implementasi sederhana dari AES dalam Python untuk tujuan pendidikan dan demonstrasi.</p>

## Fitur

- Enkripsi dan Dekripsi menggunakan AES 128 bit;
- Input berupa 32 digit Heksadesimal (128 bit);
- Output berupa 32 digit Heksadesimal (128 bit);
- Validasi input key dan plaintext/ciphertext;
- Menampilkan dan simpan hasil Debug Result Enkripsi dan Dekripsi (Khusus v2.0.beta setelahnya)
- Reset input; dan
- Tampilan modern menggunakan tkinter/antarmuka grafis yang ramah pengguna.
  
- Contoh Input dan Output
  ```bash
  Plaintext:   00112233445566778899aabbccddeeff
  Key:         000102030405060708090a0b0c0d0e0f
  Ciphertext:  69c4e0d86a7b0430d8cdb78070b4c55a

  Plaintext:   0123456789ABCDEF1123456789ABCDEF
  Key:         6281377383082ABCDEF2204205010010
  Ciphertext:  0507E8860F3C843C1F1291C65E984986

  Plaintext:   0123456789abcdeffedcba9876543210 
  Key:         0f1571c947d9e8590cb7add6af7f6798
  Ciphertext:  FF0B844A0853BF7C6934AB4364148FB9
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

2. Masukkan 32 digit heksadesimal (128 bit) Plaintext/Ciphertext dan kunci.

3. Klik tombol "Enkripsi" atau "Dekripsi" sesuai kebutuhan.

4. Hasil akan ditampilkan di bidang "Hasil/Output".

## Tangkapan Layar

![hasil](https://github.com/BukanMakmum/AdvancedEncryptionStandard/assets/32379649/82ae22ac-3e7f-4df9-9378-39433aa1e754)

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat berkas [LICENSE](LICENSE) untuk detailnya.

## Kontak

Untuk pertanyaan atau umpan balik, silakan hubungi pengembang:
- Nama: [Bukan Makmum]
- Email: [imamsyt22@mhs.usk.ac.id]

© 2023 BukanMakmum.
