# Enkripsi dan Dekripsi AES

Implementasi sederhana algoritma Advanced Encryption Standard (AES) menggunakan Python dan pustaka Tkinter untuk antarmuka pengguna grafis. Advanced Encryption Standard (AES) versi Education merupakan skrip yang dikembangkan untuk pembelajaran proses enkripsi dan dekripsi menggunakan AES.


## Daftar Isi

- [Pendahuluan](#pendahuluan)
- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Tangkapan Layar](#tangkapan-layar)
- [Lisensi](#lisensi)
- [Kontak](#kontak)

## Pendahuluan

AES (Advanced Encryption Standard) adalah sebuah algoritma enkripsi kunci simetris yang digunakan secara luas untuk mengamankan data dalam berbagai aplikasi keamanan komputer. AES telah digunakan secara internasional sebagai pengganti algoritma DES (Data Encryption Standard) yang lebih lama. AES mendukung kunci enkripsi dengan panjang 128 bit, 192 bit, atau 256 bit. 
AES mengenkripsi data dalam blok-blok berukuran tetap, di mana panjang blok pesan adalah 128 bit. Pesan yang lebih panjang dibagi menjadi blok-blok 128 bit dan dienkripsi secara terpisah. AES menggunakan serangkaian putaran enkripsi, yang jumlahnya tergantung pada panjang kunci. Pada setiap putaran, data diubah menggunakan subkunci yang dihasilkan dari kunci utama. Operasi-operasi yang melibatkan substitusi, permutasi, dan XOR digunakan pada setiap putaran.
Sebelum putaran pertama dan setelah putaran terakhir, terjadi inisialisasi awal (initial permutation) dan permutasi akhir (final permutation) pada blok pesan. Inisialisasi awal mengatur data awal ke dalam urutan tertentu, sedangkan permutasi akhir mengubahnya kembali ke urutan aslinya. AES dianggap sangat aman dan tahan terhadap serangan-serangan modern, bahkan dengan panjang kunci yang lebih pendek (128 bit).

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
