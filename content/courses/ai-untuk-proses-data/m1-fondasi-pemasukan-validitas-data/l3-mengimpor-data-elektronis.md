---
title: Mengimpor Data dari Sumber Elektronis
course: ai-untuk-proses-data
module: 1
module_title: Fondasi Pemasukan & Validitas Data
lesson: 3
slug: l3-mengimpor-data-elektronis
unit_kompetensi:
  - kode: J.63OPR00.014.2
    nama: Melakukan Pemasukan Data
    elemen: 'Elemen 3: Meng-import data dari sumber elektronis'
level: Foundational — Competency
kategori: Competency
bloom_level: Understand/Apply
durasi_menit: 28
durasi_baca_menit: 15
durasi_latihan_menit: 13
bahasa: Indonesia
duration_minutes: 15
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Di akhir lesson ini, kamu akan mampu:
- Mengidentifikasi jenis file dengan tepat sesuai aplikasi yang dapat membacanya
- Menyimpan file dengan format yang sesuai aplikasi yang akan menggunakannya
- Memastikan berkas yang diimpor terbaca sesuai dengan berkas aslinya
- Mencatat pekerjaan pengimportan data pada logbook

---

## Hook: Migrasi Data yang Direncanakan Berminggu-Minggu, Bukan Semalam

Ketika sebuah bank mengganti sistem core banking-nya — proses yang cukup umum terjadi di industri perbankan Indonesia seiring transformasi digital — memindahkan data nasabah dari sistem lama ke sistem baru bukan sekadar "salin-tempel" yang bisa selesai dalam semalam.

Proses migrasi semacam ini pada praktiknya mencakup beberapa tahap yang direncanakan secara sistematis: **pemetaan struktur database** (data mapping), **pembersihan data** (data cleansing) untuk memastikan tidak ada data usang atau tidak konsisten yang ikut terbawa, hingga **uji operasional paralel** (parallel run) — menjalankan sistem lama dan baru secara bersamaan untuk membandingkan hasilnya sebelum sistem baru benar-benar dipakai secara penuh. Proses semacam ini pada praktiknya bisa memakan waktu berminggu-minggu, bukan hitungan jam.

Kenapa butuh waktu selama itu untuk sekadar "pindah data"? Karena setiap sistem punya cara berbeda dalam menyimpan dan membaca data — format file yang cocok di satu aplikasi belum tentu terbaca benar di aplikasi lain. Risiko kegagalan migrasi data atau masalah kompatibilitas format adalah risiko nyata yang diakui secara luas di industri perbankan — bukan kekhawatiran berlebihan.

Inilah persis yang dibahas di elemen kompetensi ketiga dari Melakukan Pemasukan Data: **mengimpor data dari sumber elektronis**.

---

## Kerangka Konseptual: Elemen 3 — Meng-import Data dari Sumber Elektronis

Berbeda dari Elemen 1-2 yang kamu pelajari di L2 (data dimasukkan manual satu per satu), Elemen 3 berurusan dengan data yang **sudah dalam bentuk file elektronis** dan perlu dibawa masuk (import) ke sistem yang kamu gunakan — misalnya file CSV hasil ekspor dari sistem core banking yang perlu dibawa masuk ke SPKO.

KUK-nya terdiri dari empat kriteria:

**3.1 — Jenis file diidentifikasi dengan tepat sesuai aplikasi yang dapat membacanya**

Tidak semua aplikasi bisa membaca semua jenis file. Sebelum impor dilakukan, petugas harus tahu persis format file apa yang diterima SPKO — apakah CSV, Excel (.xlsx), atau format lain.

**3.2 — Jenis file dapat disimpan dengan tepat sesuai dengan aplikasi yang akan menggunakannya**

Kadang file dari sumber (misalnya core banking) perlu dikonversi dulu ke format yang bisa dibaca SPKO. Menyimpan dengan format yang salah — misalnya menyimpan file yang seharusnya CSV sebagai .txt tanpa delimiter yang jelas — membuat proses impor gagal atau data terbaca tidak sesuai aslinya.

**3.3 — Berkas yang di-import dibaca ke program sesuai dengan berkas aslinya**

Ini adalah langkah verifikasi: setelah file diimpor, apakah data yang muncul di SPKO benar-benar sama dengan data di file asli? Kesalahan encoding karakter, kolom yang bergeser, atau data yang terpotong adalah risiko nyata di tahap ini.

**3.4 — Pekerjaan pengimportan data dicatat pada logbook**

Sama seperti Elemen 2, setiap proses impor harus tercatat — file apa yang diimpor, kapan, oleh siapa, dan hasilnya seperti apa.

<!-- VISUAL PLACEHOLDER: Diagram alur menunjukkan file dari Core Banking (format CSV) → Verifikasi Jenis File → Konversi (jika perlu) → Impor ke SPKO → Verifikasi Kesesuaian Data → Catat Logbook, dengan tanda silang merah pada jalur yang menunjukkan "jika data tidak sesuai, kembali ke sumber" -->

### Mengapa Praktik Migrasi Data Ini Relevan di Sini

Perhatikan tahap uji operasional paralel (parallel run) yang lazim dilakukan dalam migrasi core banking — menjalankan sistem lama dan baru secara bersamaan untuk membandingkan hasilnya. Ini pada dasarnya adalah bentuk skala besar dari KUK 3.3: memverifikasi bahwa data yang diimpor/dimigrasikan benar-benar sesuai dengan data aslinya. Bedanya, yang kamu lakukan di SPKO berskala jauh lebih kecil (satu file, bukan satu sistem penuh) — tapi prinsip verifikasinya identik: **jangan asumsikan impor berhasil hanya karena tidak ada pesan error.**

---

## Konteks SPKO: Mengimpor Data dari Sistem Core Banking

Di lingkungan latihan SPKO, sumber impor elektronis yang paling umum kamu hadapi adalah **file CSV hasil ekspor dari sistem core banking** — berisi data nasabah dalam jumlah besar sekaligus, bukan diketik satu per satu.

Hal yang perlu diperiksa saat mengimpor file ini ke SPKO:

| Yang Diperiksa | Risiko Jika Diabaikan |
|---|---|
| Format file (CSV vs Excel vs lainnya) | SPKO gagal membaca atau membaca dengan susunan kolom salah |
| Delimiter/pemisah kolom (koma vs titik koma) | Data tergabung dalam satu kolom, bukan terpisah sesuai field |
| Encoding karakter (terutama untuk nama dengan karakter khusus) | Nama nasabah muncul sebagai karakter aneh/rusak |
| Jumlah baris data (sebelum vs sesudah impor) | Baris data hilang tanpa disadari saat proses impor |

### Kenapa Ini Kritis Khusus untuk Solusi AI

Berbeda dari sistem pelaporan biasa yang mungkin sekadar menampilkan data ke layar, data yang kamu impor di sini akan langsung menjadi **input** yang diproses model AI SPKO untuk menghasilkan skor kredit — baik untuk melatih ulang model (retraining) maupun untuk diproses saat model beroperasi (inference). Jika satu batch impor mengandung data yang tergeser kolomnya atau baris yang hilang tanpa disadari, itu bukan cuma "data yang salah tampil" — itu berarti **model AI belajar dari atau memutuskan berdasarkan data yang cacat**, dan kesalahan itu bisa memengaruhi ratusan keputusan kredit sekaligus dalam satu batch, jauh lebih besar dampaknya dibanding satu kesalahan input manual di L2.

---

## Quick Check
**(Target: 2 menit)**

**Setelah mengimpor file CSV berisi 500 data nasabah ke SPKO, sistem menunjukkan "Impor berhasil" tanpa pesan error. Apakah ini cukup untuk memastikan data sudah benar? Jawab dalam 1-2 kalimat.**

<details>
<summary>Lihat jawaban</summary>

Tidak cukup. Pesan "berhasil" hanya berarti proses teknis impor berjalan tanpa error sistem — bukan jaminan bahwa data yang masuk sesuai dengan berkas aslinya (KUK 3.3). Petugas tetap harus memverifikasi, misalnya membandingkan jumlah baris data sebelum dan sesudah impor, serta memeriksa sampel data untuk memastikan tidak ada kolom yang bergeser atau karakter yang rusak.
</details>

---

## Latihan Terstruktur (Simulasi Singkat)
**(Target: 10 menit)**

**Skenario:** Kamu menerima file CSV berisi 500 baris data nasabah dari sistem core banking untuk diimpor ke SPKO. Setelah proses impor, kamu memeriksa hasilnya dan menemukan tiga kondisi berikut. Untuk masing-masing, tentukan: (a) apakah ini menunjukkan masalah pada KUK 3.1/3.2/3.3, dan (b) tindakan yang harus diambil.

| Temuan Setelah Impor | Kondisi |
|---|---|
| A | SPKO hanya menampilkan 480 baris data, padahal file asli berisi 500 baris |
| B | Kolom "nama lengkap" dan "penghasilan bulanan" tergabung jadi satu kolom |
| C | Semua 500 baris tampil lengkap dan sesuai, tidak ada anomali |

**Instruksi:** Kerjakan dalam 10 menit, isi kolom analisis KUK dan tindakan untuk tiap baris.

<details>
<summary>Lihat kunci jawaban</summary>

| Temuan | KUK Terkait | Tindakan |
|---|---|---|
| A | 3.3 (berkas tidak sesuai aslinya — ada baris hilang) | Jangan lanjutkan proses; telusuri penyebab 20 baris hilang (kemungkinan baris kosong yang terlewat, batas jumlah baris pada aplikasi, atau kesalahan saat ekspor dari core banking). Impor ulang setelah penyebab ditemukan. |
| B | 3.2 (format/delimiter tidak sesuai — kemungkinan delimiter salah terbaca) | Periksa delimiter file asli (kemungkinan menggunakan titik koma, sementara SPKO membaca dengan koma). Perbaiki pengaturan impor atau format file, jangan pisahkan kolom secara manual satu per satu. |
| C | Tidak ada masalah | Lanjutkan — catat hasil impor pada logbook sesuai KUK 3.4 |

**Poin penilaian mandiri:** Bila kamu langsung "menerima" Temuan A karena SPKO tidak menampilkan pesan error, ulangi bagian "Mengapa Praktik Migrasi Data Ini Relevan di Sini" di atas — verifikasi tidak boleh bergantung pada ada/tidaknya pesan error sistem.
</details>

---

## Analisis Kasus: Kembali ke Praktik Migrasi Data Perbankan

Skala migrasi sistem core banking penuh jauh lebih besar dari sekadar mengimpor satu file CSV — bank memindahkan seluruh sistem operasionalnya. Tapi prinsip yang membuat migrasi semacam itu direncanakan berminggu-minggu (bukan sekali klik) adalah prinsip yang sama yang berlaku di skala kecil: **data mapping** (memastikan struktur data sumber cocok dengan struktur sistem tujuan — setara KUK 3.1-3.2), **data cleansing** (memastikan data bersih sebelum masuk — terkait persiapan data di L2), dan **uji operasional paralel/verifikasi** (parallel run — memastikan hasil migrasi sesuai — setara KUK 3.3).

Ini menunjukkan bahwa kompetensi yang kamu pelajari di lesson ini bukan sekadar "keterampilan level operator entry-level" yang remeh — ia adalah versi skala-kecil dari proses yang sama yang dilakukan bank saat mengganti seluruh sistem intinya.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Jangan asumsikan proses impor data antarsistem "hanya masalah teknis IT" yang bisa diselesaikan cepat. Praktik migrasi core banking di industri menunjukkan bahkan migrasi terencana butuh waktu berminggu-minggu dengan verifikasi berlapis.

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Antarmuka hasil impor sebaiknya menampilkan ringkasan otomatis (jumlah baris sebelum vs sesudah, sampel data yang diimpor) agar petugas tidak perlu memeriksa manual satu per satu — mengurangi risiko Temuan A/B di latihan di atas terlewat.

**Bagi pengembang/petugas teknis (developer/engineer):**
Proses impor idealnya menyertakan validasi otomatis (jumlah baris, integritas kolom) sebagai bagian dari sistem, bukan mengandalkan petugas memeriksa manual — meskipun petugas tetap perlu tahu cara memverifikasi jika validasi otomatis tidak tersedia.

---

## Pertanyaan Refleksi

1. Pernahkah kamu mengalami situasi di mana sebuah proses "tampak berhasil" (tidak ada pesan error) tapi ternyata hasilnya salah? Apa yang membuatmu akhirnya menyadari kesalahannya?
2. Praktik migrasi core banking di industri melibatkan uji operasional paralel (parallel run). Menurutmu, adakah versi sederhana dari uji ini yang bisa diterapkan saat mengimpor data ke SPKO, meski skalanya jauh lebih kecil?

---

## Ringkasan Lesson

- Elemen 3 (mengimpor data dari sumber elektronis) menuntut identifikasi jenis file yang tepat, penyimpanan format yang sesuai, dan verifikasi bahwa data yang diimpor benar-benar sesuai dengan berkas asli — bukan sekadar mengandalkan tidak adanya pesan error.
- Praktik migrasi data core banking di industri perbankan Indonesia menunjukkan bahwa prinsip data mapping, data cleansing, dan verifikasi hasil berlaku baik di skala migrasi sistem penuh maupun skala impor satu file.
- "Impor berhasil" secara teknis tidak sama dengan "data benar" — verifikasi tetap wajib dilakukan.

---

## Referensi

- Praktik umum migrasi data core banking pada industri perbankan Indonesia — mencakup tahapan data mapping, data cleansing, dan uji operasional paralel (parallel run) sebagai standar mitigasi risiko migrasi sistem.

---

## Navigasi

**[← M1-L2: Mempersiapkan & Memasukkan Data Nasabah](l2-mempersiapkan-memasukkan-data)** | **[M1-L4: Mengidentifikasi Substansi & Referensi Data →](l4-substansi-referensi-data)**
