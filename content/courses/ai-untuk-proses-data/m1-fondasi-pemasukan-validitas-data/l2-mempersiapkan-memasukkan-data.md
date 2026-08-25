---
title: Mempersiapkan & Memasukkan Data Nasabah
course: ai-untuk-proses-data
module: 1
module_title: Fondasi Pemasukan & Validitas Data
lesson: 2
slug: l2-mempersiapkan-memasukkan-data
unit_kompetensi:
  - kode: J.63OPR00.014.2
    nama: Melakukan Pemasukan Data
    elemen: 'Elemen 1-2: Mempersiapkan data & Memasukkan data dengan perangkat komputer'
level: Foundational — Competency
kategori: Competency
bloom_level: Remember/Understand
durasi_menit: 30
durasi_baca_menit: 15
durasi_latihan_menit: 15
bahasa: Indonesia
duration_minutes: 30
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Di akhir lesson ini, kamu akan mampu:
- Mempersiapkan data sebelum dimasukkan sesuai jenis aplikasi yang digunakan
- Memeriksa kelengkapan jumlah dan jenis data pada tiap isian borang
- Memasukkan data ke aplikasi komputer dengan lengkap, termasuk memindai dokumen fisik menjadi format elektronis
- Mencatat pekerjaan pemasukan data pada logbook sesuai standar organisasi

---

## Hook: Data yang Tertukar Bertahun-Tahun Tanpa Diketahui

Sebelum SLIK OJK (Sistem Layanan Informasi Keuangan) seperti yang kita kenal sekarang, sistem pelaporan riwayat kredit di Indonesia bernama **Sistem Informasi Debitur (SID)**, yang saat itu dikelola Bank Indonesia. Setiap bank dan lembaga pembiayaan wajib melaporkan data debiturnya ke SID secara berkala — mirip dengan apa yang akan kamu lakukan setiap hari sebagai petugas pemasukan data.

Namun, sebuah laporan investigasi menemukan pola kesalahan yang mengkhawatirkan dalam praktiknya: **data debitur yang tertukar antar nasabah**, kesalahan pencatatan status kolektabilitas (penilaian kelancaran pembayaran kredit), dan data yang dipakai tanpa persetujuan nasabah yang bersangkutan. Yang membuat kasus ini lebih meresahkan bukan cuma kesalahannya — tapi **berapa lama kesalahan itu berlangsung sebelum ketahuan**. Korban baru menyadari data mereka tertukar setelah mengalami dampaknya sendiri, seperti pengajuan kredit yang ditolak tanpa alasan jelas, tanpa tahu sejak kapan kesalahan itu terjadi atau bagaimana penyelesaiannya.

Ini bukan kegagalan model AI yang canggih, bukan juga serangan siber. Ini adalah kesalahan yang dimulai dari titik paling dasar: **proses pemasukan dan pencatatan data** — persis apa yang akan kamu pelajari di lesson ini.

Sistem informasi kredit di Indonesia sejak itu telah berevolusi (SID kini sepenuhnya digantikan SLIK yang dikelola OJK, sejak 1 Januari 2018, dengan cakupan dan mekanisme kontrol yang lebih ketat) — tapi prinsip dasarnya tidak berubah: **siapa pun yang memasukkan data ke sistem, memegang tanggung jawab yang berdampak nyata pada kehidupan orang lain.**

---

## Kerangka Konseptual: Dua Elemen Kompetensi Melakukan Pemasukan Data

Unit kompetensi **Melakukan Pemasukan Data (J.63OPR00.014.2)** terdiri dari tiga elemen. Lesson ini fokus ke dua elemen pertama:

### Elemen 1: Mempersiapkan Data yang Akan Dimasukkan

Sebelum data benar-benar diketik atau diinput, ada tahap persiapan yang sering dilewati padahal krusial:

- **Perlakuan persiapan data disesuaikan dengan aplikasi yang digunakan** — data untuk SPKO (Sistem Penilaian Kredit Otomatis) mungkin butuh format berbeda dibanding sistem pelaporan ke SLIK, meski sumber datanya sama.
- **Jumlah data diperiksa kelengkapannya sesuai borang** — sebelum diinput, hitung dulu apakah semua kolom di formulir pengajuan kredit sudah terisi.
- **Jenis data pada tiap isian diperiksa sesuai borang** — pastikan kolom "penghasilan bulanan" memang diisi angka, bukan teks; kolom "nomor identitas" memang diisi format yang sesuai.

### Elemen 2: Memasukkan Data dengan Perangkat Komputer

Setelah persiapan selesai, proses input dilakukan dengan disiplin berikut:

- Data dimasukkan menggunakan aplikasi yang ditentukan organisasi (bukan aplikasi pengganti yang "kebetulan lebih familiar")
- Data disimpan pada lokasi penyimpanan yang sesuai — bukan sekadar tersimpan, tapi tersimpan di tempat yang benar
- **Seluruh data wajib dimasukkan secara lengkap** — kolom kosong yang seharusnya wajib diisi adalah risiko, bukan detail kecil
- Dokumen fisik (seperti formulir pengajuan kredit dan salinan KTP nasabah) dipindai menjadi format elektronis sesuai dokumen aslinya — bukan diringkas atau ditulis ulang, tapi direproduksi persis
- Setiap pekerjaan pemasukan data dicatat pada logbook sesuai standar organisasi — ini bukan formalitas administratif, tapi jejak audit (audit trail) yang memungkinkan kesalahan ditelusuri kembali

<!-- VISUAL PLACEHOLDER: Diagram alur horizontal 5 langkah: Terima Dokumen Fisik → Periksa Kelengkapan & Jenis Data → Input ke Aplikasi → Pindai Dokumen → Catat di Logbook, dengan ikon berbeda tiap langkah -->

**Mengapa logbook penting?** Ingat kasus SID di atas — salah satu alasan kesalahan itu berlangsung lama sebelum ketahuan adalah sulitnya menelusuri kapan dan oleh siapa data dimasukkan atau diubah. Logbook yang konsisten adalah pertahanan pertama terhadap masalah semacam ini.

### Kenapa Ini Berbeda untuk Solusi AI, Bukan Sekadar Sistem Biasa

Data yang kamu masukkan di sini bukan cuma "tersimpan di database" — ia menjadi **fitur (feature)** yang secara langsung dibaca dan diproses oleh model AI di SPKO untuk menghasilkan skor kelayakan kredit. Ini beda dengan sistem pencatatan biasa yang mungkin hanya menampilkan data apa adanya ke petugas.

Kalau kolom "penghasilan bulanan" salah ketik jadi 10 kali lipat dari yang seharusnya, sistem pencatatan manual mungkin akan terlihat "aneh" oleh mata manusia yang membacanya — tapi model AI **tidak punya insting untuk curiga**. Ia akan memproses angka yang salah itu sebagai fakta, menghasilkan skor kredit yang keliru, tanpa ada tanda peringatan apa pun kecuali kamu secara eksplisit memvalidasi data sebelum masuk ke model. Inilah yang disebut prinsip **"data masuk sampah, keputusan yang keluar juga sampah"** (*garbage in, garbage out*) — dan prinsip ini jauh lebih berbahaya pada sistem AI dibanding sistem pencatatan manual, karena AI mengambil keputusan secara otomatis tanpa pengecekan akal sehat manusia di setiap baris data.

---

## Konteks SPKO: Data Pengajuan Kredit Nasabah

Di lingkungan latihan SPKO milik Bank Nusantara Sejahtera, data yang kamu proses di lesson ini mencakup field berikut:

| Field | Jenis Data | Catatan Persiapan |
|---|---|---|
| Nomor identitas nasabah (KTP) | Angka (16 digit) | Periksa jumlah digit sebelum input |
| Nama lengkap | Teks | Sesuaikan dengan ejaan di KTP |
| Penghasilan bulanan | Angka | Tidak boleh bernilai negatif atau kosong |
| Riwayat kredit (skor internal) | Angka | Diisi dari hasil pengecekan SLIK |
| Status pekerjaan | Teks/kategori | Field wajib, tidak boleh kosong |

Dokumen fisik yang perlu dipindai: **formulir pengajuan kredit** dan **salinan KTP nasabah**.

---

## Quick Check
**(Target: 2 menit)**

**Seorang petugas menerima formulir pengajuan kredit dengan kolom "status pekerjaan" kosong. Formulir itu sudah ditandatangani nasabah dan tampak lengkap secara visual. Apa yang seharusnya dilakukan petugas SEBELUM memasukkan data ini ke SPKO? Jawab dalam 1-2 kalimat.**

<details>
<summary>Lihat jawaban</summary>

Petugas harus memeriksa kelengkapan jenis data pada tiap isian borang (Elemen 1, KUK 1.3) SEBELUM data dimasukkan — bukan menginput dulu lalu memperbaiki nanti. Karena "status pekerjaan" adalah field wajib di SPKO, formulir ini harus dikembalikan atau dikonfirmasi ulang ke nasabah/petugas front office untuk dilengkapi, bukan diinput dengan kolom kosong atau diisi dengan asumsi. Tanda tangan nasabah tidak menggantikan kelengkapan data — keduanya adalah hal yang berbeda.
</details>

---

## Latihan Terstruktur (Simulasi Singkat)
**(Target: 10 menit — format ini meniru demonstrasi/simulasi di Tempat Uji Kompetensi)**

**Skenario:** Kamu menerima 3 formulir pengajuan kredit SPKO berikut untuk diproses. Untuk setiap formulir, tentukan: (a) apakah data SIAP diinput atau perlu diperbaiki dulu, (b) elemen KUK mana yang relevan (1.1/1.2/1.3), dan (c) tindakan konkret yang harus diambil.

| Formulir | Kondisi Data |
|---|---|
| A | Nomor KTP terisi 15 digit (seharusnya 16), semua field lain lengkap |
| B | Semua field lengkap dan sesuai format, dokumen fisik sudah dipindai dengan jelas |
| C | Penghasilan bulanan diisi "-500000" (nilai negatif) |

**Instruksi pengerjaan:**
1. Kerjakan dalam tabel yang sama — isi 3 kolom tambahan: Siap/Tidak, Elemen KUK, Tindakan
2. Batasi diri pada 10 menit — di uji kompetensi sesungguhnya, kamu tidak akan diberi waktu tanpa batas
3. Setelah selesai, buka kunci jawaban untuk membandingkan

<details>
<summary>Lihat kunci jawaban</summary>

| Formulir | Siap/Tidak | Elemen KUK | Tindakan |
|---|---|---|---|
| A | Tidak siap | 1.3 (jenis data pada tiap isian) | Kembalikan untuk verifikasi nomor KTP — periksa apakah salah ketik atau dokumen fisik memang tidak standar, jangan asumsikan salah satu digit boleh dihilangkan |
| B | Siap | — | Lanjutkan ke Elemen 2 (memasukkan data dengan perangkat komputer) |
| C | Tidak siap | 1.3 (jenis data pada tiap isian, nilai tidak valid) | Kembalikan ke sumber data — penghasilan tidak boleh bernilai negatif; kemungkinan kesalahan input di sumber atau kesalahan format (mis. tanda minus tidak sengaja masuk) |

**Poin penilaian mandiri:** Jika kamu menandai Formulir B sebagai "tidak siap" atau salah mengidentifikasi elemen KUK di A/C, ulangi kerangka konseptual Elemen 1 sebelum lanjut ke L3.
</details>

---

## Analisis Kasus: Kembali ke SID

Kasus kesalahan pencatatan data debitur di SID menunjukkan sesuatu yang penting: kesalahan itu bukan disebabkan oleh satu kejadian besar, melainkan oleh akumulasi kelalaian kecil dalam proses pemasukan dan pencatatan data — persis dua elemen kompetensi yang baru saja kamu pelajari. Data yang tertukar antar nasabah kemungkinan besar berakar dari kegagalan memeriksa kelengkapan dan kesesuaian jenis data sebelum data itu masuk ke sistem, serta lemahnya jejak pencatatan (logbook) yang membuat kesalahan sulit ditelusuri.

Ini mengafirmasi mengapa KUK unit ini menuntut ketelitian di level yang tampak "sepele" — memeriksa jumlah kolom, jenis data, dan mencatat logbook — karena di skala operasional bank yang menangani ribuan nasabah, kelalaian kecil yang konsisten berubah menjadi masalah sistemik.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Kecepatan proses pemasukan data tidak boleh dikorbankan demi throughput semata. Setiap kebijakan yang menekan petugas untuk "input cepat, cek belakangan" berisiko mereproduksi pola kesalahan seperti kasus SID di atas.

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Antarmuka input data sebaiknya memvalidasi jenis data secara otomatis saat diketik (misalnya menolak huruf pada field yang seharusnya angka), sehingga kesalahan Elemen 1 (jenis data tidak sesuai) tertangkap sistem, bukan hanya bergantung pada ketelitian petugas.

**Bagi pengembang/petugas teknis (developer/engineer):**
Logbook pemasukan data idealnya tidak dicatat manual terpisah, tapi terintegrasi otomatis sebagai bagian dari sistem input — setiap input tercatat timestamp dan ID petugas secara otomatis, mengurangi risiko logbook yang tidak konsisten.

---

## Pertanyaan Refleksi

1. Di lingkungan kerjamu, apakah ada tahap "persiapan data" yang eksplisit sebelum data dimasukkan, atau langsung diketik begitu dokumen diterima? Apa risikonya dari masing-masing pendekatan?
2. Kasus SID melibatkan kesalahan yang baru diketahui setelah bertahun-tahun. Menurutmu, kontrol apa yang paling murah namun paling efektif untuk mendeteksi kesalahan pemasukan data lebih cepat?

---

## Ringkasan Lesson

- Elemen 1 (mempersiapkan data) dan Elemen 2 (memasukkan data) dari unit Melakukan Pemasukan Data menuntut ketelitian di setiap tahap: memeriksa kelengkapan jumlah dan jenis data sebelum input, memasukkan data secara lengkap ke aplikasi yang tepat, memindai dokumen fisik secara akurat, dan mencatat logbook secara konsisten.
- Kasus nyata kesalahan pencatatan data debitur di SID (kini digantikan SLIK OJK sejak 2018) menunjukkan bagaimana kelalaian kecil di tahap ini bisa berdampak nyata dan berlangsung lama sebelum terdeteksi.
- Logbook bukan formalitas administratif — ia adalah jejak audit yang memungkinkan kesalahan ditelusuri dan diperbaiki.

---

## Referensi

- Artikel investigasi mengenai kesalahan pencatatan data debitur pada Sistem Informasi Debitur (SID), simadanews.com, 2021.
- Surat Edaran OJK Nomor 50/SEOJK.03/2017 tentang Pelaporan dan Permintaan Informasi Debitur.
- OJK Indonesia — pengalihan penuh Sistem Informasi Debitur (SID) ke Sistem Layanan Informasi Keuangan (SLIK), efektif 1 Januari 2018.

---

## Navigasi

**[← M1-L1: Mengenal SPKO](l1-mengenal-spko)** | **[M1-L3: Mengimpor Data dari Sumber Elektronis →](l3-mengimpor-data-elektronis)**
