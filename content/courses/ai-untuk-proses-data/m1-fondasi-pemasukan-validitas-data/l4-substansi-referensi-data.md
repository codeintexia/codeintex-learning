---
title: Mengidentifikasi Substansi & Referensi Data
course: ai-untuk-proses-data
module: 1
module_title: Fondasi Pemasukan & Validitas Data
lesson: 4
slug: l4-substansi-referensi-data
unit_kompetensi:
  - kode: J.63OPR00.015.2
    nama: Memastikan Validitas Data
    elemen: >-
      Elemen 1-2: Mengidentifikasi substansi data & Mengidentifikasi referensi
      data
level: Foundational — Competency
kategori: Competency
bloom_level: Understand
durasi_menit: 30
durasi_baca_menit: 17
durasi_latihan_menit: 13
bahasa: Indonesia
duration_minutes: 17
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Di akhir lesson ini, kamu akan mampu:
- Memastikan data sesuai dengan keperluan data pada proses bisnis organisasi
- Memastikan jenis data yang dimasukkan sesuai kebutuhan aplikasi
- Mengidentifikasi penggunaan referensi data berdasarkan jenis data yang dimasukkan
- Memastikan data yang dimasukkan sesuai dengan kodifikasi yang berlaku

---

## Hook: Ketika Kode Referensi Berubah, Data Lama Menjadi Retak

Asosiasi profesi manajemen data di Indonesia mendokumentasikan sebuah pola yang berulang di banyak organisasi: **perubahan data referensi yang tidak terkendali**. Ketika referensi seperti kode wilayah atau klasifikasi produk diubah tanpa memperbarui data historis yang sudah ada, konsistensi data langsung rusak.

Bayangkan skenarionya: sebuah kode klasifikasi yang dipakai bertahun-tahun tiba-tiba diperbarui — mungkin karena regulasi baru, mungkin karena standar internal berubah. Data baru yang masuk memakai kode yang diperbarui. Tapi data lama yang sudah tersimpan bertahun-tahun sebelumnya masih memakai kode versi lama. Hasilnya: sistem sekarang punya dua "bahasa" berbeda untuk merujuk hal yang sama, dan siapa pun yang mengolah data itu — termasuk model AI — tidak tahu bahwa kedua kode itu sebenarnya merujuk konsep yang identik.

Pola ini diperparah oleh **pengelolaan master data yang lemah** — misalnya referensi yang tidak konsisten atau duplikasi identitas klien di berbagai unit bisnis, yang pada akhirnya menyulitkan audit dan bahkan membuka celah manipulasi data yang sulit dilacak.

Ini bukan skenario langka. Ini adalah alasan kenapa memastikan **referensi dan kodifikasi data** bukan sekadar administrasi teknis — ia adalah pertahanan terhadap kekacauan yang bisa terjadi diam-diam selama bertahun-tahun sebelum ada yang menyadarinya.

---

## Kerangka Konseptual: Elemen 1-2 dari Memastikan Validitas Data

Unit **Memastikan Validitas Data (J.63OPR00.015.2)** terdiri dari empat elemen. Lesson ini fokus ke dua elemen pertama — fondasi sebelum kamu bisa memeriksa validitas data secara aktif di L5.

### Elemen 1: Mengidentifikasi Substansi Data yang Dimasukkan

- **Data dipastikan sesuai keperluan data pada proses bisnis organisasi** — bukan sekadar "data ada", tapi data itu memang relevan dengan kebutuhan operasional SPKO
- **Jenis data yang dimasukkan sesuai kebutuhan jenis data pada aplikasi** — memverifikasi bahwa substansi (isi) data, bukan cuma formatnya, memang cocok dengan apa yang dibutuhkan sistem

### Elemen 2: Mengidentifikasi Referensi dari Data yang Dimasukkan

- **Pemasukan berdasarkan jenis data diidentifikasi sesuai penggunaan referensi data** — misalnya kode wilayah domisili nasabah harus merujuk ke tabel referensi wilayah yang berlaku saat ini, bukan versi lama
- **Data yang dimasukkan sesuai kodifikasi dari data tersebut** — kode klasifikasi pekerjaan, kode jenis kredit, dan kode lain harus konsisten dengan standar kodifikasi yang berlaku di organisasi

<!-- VISUAL PLACEHOLDER: Diagram menunjukkan satu data nasabah dengan garis penghubung ke berbagai tabel referensi (tabel kode wilayah, tabel klasifikasi pekerjaan, tabel jenis kredit), dengan highlight pada satu garis yang "putus" menunjukkan referensi usang -->

### Kenapa Ini Berbeda dan Lebih Kritis untuk Solusi AI

Sistem pencatatan manual mungkin bisa "mentolerir" inkonsistensi kode referensi — seorang petugas yang berpengalaman bisa mengenali bahwa kode lama dan kode baru merujuk hal yang sama, lalu menyesuaikan secara manual saat membaca laporan. **Model AI tidak punya pengenalan kontekstual semacam itu.**

Bagi model SPKO, kode referensi adalah **kategori numerik atau simbolik yang diperlakukan sebagai entitas berbeda** kecuali secara eksplisit dipetakan sebagai setara. Jika separuh data nasabah memakai kode wilayah versi lama dan separuh lainnya versi baru tanpa pemetaan yang jelas, model AI akan memperlakukan nasabah dari wilayah yang sama sebagai dua kelompok yang berbeda — berpotensi menghasilkan penilaian kredit yang tidak konsisten untuk orang-orang dengan profil risiko yang sebenarnya identik, semata karena kebetulan data mereka dimasukkan pada periode kodifikasi yang berbeda.

---

## Konteks SPKO: Referensi Data yang Dipakai

| Jenis Data | Tabel Referensi yang Harus Dipakai |
|---|---|
| Kode wilayah domisili nasabah | Tabel kode wilayah administratif terbaru |
| Status pekerjaan | Tabel klasifikasi pekerjaan standar organisasi |
| Jenis produk kredit yang diajukan | Tabel kodifikasi jenis kredit SPKO |

**Aturan dasar:** sebelum data dimasukkan, petugas harus memastikan data merujuk ke **versi tabel referensi yang sedang berlaku**, bukan versi yang sudah digantikan — meskipun kode lama itu masih "terlihat masuk akal" saat diketik.

---

## Quick Check
**(Target: 2 menit)**

**Seorang petugas menemukan bahwa kode wilayah domisili di formulir pengajuan kredit adalah kode versi lama yang sudah tidak dipakai organisasi sejak setahun lalu, meski secara format terlihat valid (angka 4 digit, sesuai pola). Apakah ini masalah, dan mengapa?**

<details>
<summary>Lihat jawaban</summary>

Ya, ini masalah — meski format terlihat benar (4 digit sesuai pola), substansi kodenya tidak sesuai dengan referensi yang berlaku saat ini (Elemen 2, KUK 2.1). Format yang valid tidak sama dengan referensi yang valid. Kode wilayah lama ini harus dipetakan ke kode terbaru sebelum dimasukkan ke SPKO, atau model AI akan memperlakukannya sebagai wilayah yang berbeda dari yang sebenarnya dimaksud.
</details>

---

## Latihan Terstruktur (Simulasi Singkat)
**(Target: 10 menit)**

**Skenario:** Kamu memeriksa 3 data pengajuan kredit berikut untuk memastikan substansi dan referensinya benar sebelum diproses SPKO.

| Data | Kondisi |
|---|---|
| A | Kode klasifikasi pekerjaan "07" — organisasi baru saja memperbarui tabel klasifikasi bulan lalu, dan kode "07" di tabel lama berarti "Wiraswasta", tapi di tabel baru kode itu berarti "Karyawan Swasta" |
| B | Kode jenis kredit sesuai tabel kodifikasi SPKO terbaru, semua field lain juga sesuai |
| C | Nasabah mengisi "pegawai negeri" secara bebas di kolom status pekerjaan, bukan memilih dari kode klasifikasi yang tersedia |

**Instruksi:** Tentukan untuk masing-masing: (a) apakah ini masalah substansi/referensi, (b) elemen KUK yang relevan, (c) tindakan yang diambil. Kerjakan dalam 10 menit.

<details>
<summary>Lihat kunci jawaban</summary>

| Data | Masalah? | KUK | Tindakan |
|---|---|---|---|
| A | Ya — ambiguitas referensi | Elemen 2 (kodifikasi) | Konfirmasi periode data ini diinput — jika sebelum pembaruan tabel, kode "07" berarti Wiraswasta; jangan asumsikan otomatis memakai arti tabel terbaru. Petakan secara eksplisit ke kodifikasi yang benar sebelum masuk SPKO |
| B | Tidak | — | Lanjutkan ke elemen berikutnya (pemeriksaan validitas di L5) |
| C | Ya — substansi tidak sesuai kebutuhan aplikasi | Elemen 1 (substansi data) | Data dalam bentuk teks bebas tidak bisa langsung dipetakan ke kode klasifikasi standar; perlu dikonfirmasi ulang dan dipetakan manual ke kode yang sesuai sebelum masuk sistem |

**Poin penilaian mandiri:** Kasus A adalah yang paling mudah terlewat — kalau kamu langsung menerima kode "07" tanpa mengecek kapan data itu diinput, kamu berisiko salah memetakan status pekerjaan nasabah secara diam-diam.
</details>

---

## Analisis Kasus: Kembali ke Pola Perubahan Referensi Tanpa Kontrol

Ingat kembali temuan DAMA Indonesia: perubahan referensi tanpa pembaruan data historis merusak konsistensi, menyulitkan audit, dan membuka celah kesalahan yang sulit dilacak. Kasus A di latihan di atas adalah contoh konkret dari pola ini dalam skala kecil — satu kode yang maknanya berubah seiring waktu, tanpa penanda eksplisit yang membedakan data lama dan data baru.

Di skala organisasi yang menangani ribuan data nasabah, masalah seperti ini bisa terjadi berulang kali setiap kali ada pembaruan kebijakan atau standar internal — dan tanpa disiplin memeriksa referensi secara eksplisit setiap kali data dimasukkan, kesalahan semacam ini bisa terakumulasi tanpa terdeteksi selama bertahun-tahun, persis seperti yang didokumentasikan DAMA.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Setiap kali organisasi memutuskan mengubah kode referensi atau standar klasifikasi, itu bukan keputusan teknis semata — itu keputusan yang butuh rencana migrasi data historis, bukan cuma menerapkan kode baru untuk data baru saja.

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Antarmuka input idealnya membatasi pilihan hanya ke kode referensi yang sedang berlaku (dropdown, bukan input teks bebas) — mencegah masalah seperti Data C di latihan di atas sejak awal.

**Bagi pengembang/petugas teknis (developer/engineer):**
Sistem sebaiknya menyimpan riwayat versi tabel referensi (bukan cuma versi terbaru), sehingga data lama bisa dipetakan otomatis ke standar terbaru tanpa bergantung sepenuhnya pada ketelitian manual petugas.

---

## Pertanyaan Refleksi

1. Di organisasimu, pernahkah ada perubahan kode/klasifikasi yang tidak disertai rencana migrasi data lama? Apa dampaknya yang kamu amati?
2. Kalau kamu menemukan data dengan kode referensi yang ambigu (seperti Data A), tapi tidak ada cara mudah mengecek kapan data itu diinput, langkah apa yang akan kamu ambil?

---

## Ringkasan Lesson

- Elemen 1 (substansi data) memastikan isi data relevan dengan kebutuhan proses bisnis; Elemen 2 (referensi data) memastikan kode yang dipakai konsisten dengan kodifikasi yang berlaku saat ini — bukan sekadar format yang terlihat benar.
- Bagi Solusi AI, inkonsistensi referensi jauh lebih berbahaya dibanding sistem manual, karena model memperlakukan kode berbeda sebagai entitas berbeda tanpa pengenalan kontekstual manusia.
- Pola nyata yang didokumentasikan DAMA Indonesia — perubahan referensi tanpa pembaruan data historis — menunjukkan bagaimana masalah kecil semacam ini bisa terakumulasi tanpa terdeteksi dalam skala besar.

---

## Referensi

- DAMA Indonesia (Data Management Association Indonesia). *Mengurai Penyebab Buruknya Kualitas Data di Organisasi*, berdasarkan kerangka DAMA-DMBOK (Data Management Body of Knowledge).

---

## Navigasi

**[← M1-L3: Mengimpor Data dari Sumber Elektronis](l3-mengimpor-data-elektronis)** | **[M1-L5: Memeriksa Validitas Data Nasabah →](l5-memeriksa-validitas-data)**
