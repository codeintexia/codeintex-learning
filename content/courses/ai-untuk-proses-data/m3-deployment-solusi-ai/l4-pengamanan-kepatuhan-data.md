---
title: Menerapkan Pengamanan & Kepatuhan Data
course: ai-untuk-proses-data
module: 3
module_title: Deployment Solusi AI
lesson: 4
slug: l4-pengamanan-kepatuhan-data
unit_kompetensi:
  - kode: J.62AIN00.015.1
    nama: Memasang Solusi AI
    elemen: 'Elemen 4: Menerapkan pengamanan Solusi AI'
level: Foundational — Competency
kategori: Competency
bloom_level: Apply/Analyze
durasi_menit: 34
durasi_baca_menit: 18
durasi_latihan_menit: 16
bahasa: Indonesia
duration_minutes: 34
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Di akhir lesson ini, kamu akan mampu:
- Menerapkan mekanisme pengamanan sesuai kebutuhan solusi dan regulasi
- Memeriksa ketentuan kepatuhan data terhadap standar yang berlaku

---

## Hook: Ketika Sistem Diserang, Kepercayaan yang Hilang Duluan

Serangan ransomware — jenis serangan siber yang menyusup ke sistem, mengenkripsi data penting, lalu meminta tebusan untuk memulihkannya — telah beberapa kali menghantam institusi perbankan di Indonesia dalam beberapa tahun terakhir. Dalam salah satu kasus besar yang tercatat, investigasi internal menemukan bahwa pelaku berhasil mengakses sistem selama beberapa waktu sebelum akhirnya mengenkripsi dan menyalin data nasabah dalam jumlah besar.

Dampaknya bukan cuma teknis. Nasabah kehilangan kepercayaan. Reputasi institusi terguncang. Ini adalah pengingat keras bahwa era digital menuntut bank untuk membangun sistem keamanan dan manajemen insiden siber yang benar-benar tangguh — bukan sekadar formalitas kepatuhan di atas kertas.

Secara hukum, kewajiban bank menjaga kerahasiaan data nasabah sudah ada sejak lama — Pasal 40 ayat (1) Undang-Undang Nomor 10 Tahun 1998 tentang Perbankan secara eksplisit mewajibkan bank menjaga kerahasiaan informasi nasabah. Tapi kasus-kasus kebocoran yang terus terjadi menunjukkan satu hal penting: **regulasi yang ketat saja tidak cukup tanpa implementasi teknis yang konkret.**

Inilah kenapa Elemen 4 — menerapkan pengamanan Solusi AI — bukan tahap administratif yang bisa "ditambal belakangan" setelah sistem berjalan. Ia harus jadi bagian integral dari deployment sejak awal, sesuai yang sudah kamu pelajari soal kewajiban penempatan data di L1: peraturan bukan formalitas, tapi konsekuensi hukum nyata.

---

## Kerangka Konseptual: Elemen 4 — Menerapkan Pengamanan Solusi AI

**4.1 — Mekanisme pengamanan diterapkan sesuai kebutuhan solusi dan regulasi**

Ini mencakup langkah teknis konkret, bukan sekadar kebijakan tertulis:
- **Enkripsi data** — mengubah data menjadi format yang tidak bisa dibaca tanpa kunci enkripsi, baik saat disimpan maupun saat berpindah antar komponen
- **Autentikasi multi-faktor** — memastikan hanya pihak berwenang yang bisa mengakses data dan sistem
- **Audit keamanan berkala** — bukan pemeriksaan satu kali saat sistem diluncurkan, tapi proses berulang untuk mendeteksi celah baru

**4.2 — Ketentuan kepatuhan data diperiksa terhadap standar yang berlaku**

Ini bukan cuma soal regulasi perbankan (POJK 11/2022, POJK 38/POJK.03/2016) — untuk Solusi AI seperti SPKO yang memproses data pribadi nasabah, kepatuhan juga harus diperiksa terhadap **Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)**, yang sudah kamu kenal sejak lesson pembuka kursus ini (M1-L1).

<!-- VISUAL PLACEHOLDER: Diagram lapisan keamanan konsentris — lapisan terluar "Kepatuhan Regulasi (POJK, UU PDP)", lapisan tengah "Kebijakan Organisasi (audit, pelatihan)", lapisan terdalam "Mekanisme Teknis (enkripsi, autentikasi multi-faktor)" — menunjukkan bahwa pengamanan butuh ketiga lapisan bekerja bersama, bukan salah satu saja -->

### Kenapa Ini Sangat Kritis untuk Solusi AI

Solusi AI seperti SPKO punya permukaan risiko keamanan yang lebih luas dibanding sistem pencatatan biasa — data mengalir melalui lebih banyak titik (core banking, model AI, dashboard), setiap titik penghubung adalah potensi celah. Selain itu, Solusi AI sering menyimpan data pelatihan (training data) dalam jumlah besar sebagai aset tambahan yang perlu diamankan — bukan cuma data operasional harian, tapi juga histori data yang dipakai melatih model. Kalau data pelatihan ini bocor, dampaknya bisa lebih luas karena mencakup data historis nasabah dalam skala besar, bukan hanya data transaksi terkini.

---

## Konteks SPKO: Menerapkan Pengamanan

| Mekanisme | Penerapan di SPKO |
|---|---|
| Enkripsi | Data nasabah dienkripsi baik saat disimpan (at rest) di core banking maupun saat berpindah (in transit) melalui API ke model dan dashboard |
| Autentikasi multi-faktor | Petugas kredit wajib verifikasi dua langkah untuk mengakses dashboard SPKO |
| Audit keamanan berkala | Pemeriksaan rutin (bukan sekali di awal) terhadap celah keamanan di seluruh komponen SPKO |
| Kepatuhan regulasi | Verifikasi berkala terhadap POJK 11/2022 (tata kelola TI), UU PDP (data pribadi), dan ketentuan kerahasiaan data nasabah dari UU Perbankan |

---

## Quick Check
**(Target: 2 menit)**

**Tim SPKO menerapkan enkripsi data saat disimpan (at rest) di core banking, tapi belum menerapkan enkripsi saat data berpindah (in transit) melalui API ke model AI. Apakah ini sudah memenuhi KUK 4.1? Jawab 1-2 kalimat.**

<details>
<summary>Lihat jawaban</summary>

Belum sepenuhnya. Mekanisme pengamanan yang lengkap perlu mencakup data baik saat disimpan maupun saat berpindah antar komponen — celah pada salah satu titik (seperti komunikasi API yang tidak terenkripsi) tetap menjadi risiko nyata, apalagi mengingat Solusi AI memiliki lebih banyak titik penghubung dibanding sistem pencatatan biasa.
</details>

---

## Latihan Terstruktur (Simulasi Singkat)
**(Target: 12 menit)**

**Skenario:** Kamu melakukan audit keamanan SPKO dan menemukan tiga kondisi berikut.

| Kondisi | Temuan |
|---|---|
| A | Data pelatihan model (training data) yang berisi histori data nasabah selama 3 tahun disimpan tanpa enkripsi terpisah, hanya mengandalkan keamanan jaringan internal |
| B | Enkripsi diterapkan konsisten di semua titik (at rest dan in transit), autentikasi multi-faktor aktif, audit keamanan terjadwal setiap 3 bulan |
| C | Sistem sudah mengikuti POJK 11/2022 untuk penempatan data, tapi belum ada verifikasi eksplisit terhadap UU PDP untuk data pelatihan model |

**Instruksi:** Tentukan (a) KUK yang relevan (4.1/4.2), (b) tindakan yang diperlukan. Kerjakan dalam 12 menit.

<details>
<summary>Lihat kunci jawaban</summary>

| Kondisi | KUK | Tindakan |
|---|---|---|
| A | 4.1 (mekanisme pengamanan belum sesuai kebutuhan) | Terapkan enkripsi khusus untuk data pelatihan, jangan hanya mengandalkan keamanan jaringan internal — data pelatihan dalam skala besar adalah target bernilai tinggi yang butuh perlindungan setara dengan data operasional |
| B | Memenuhi 4.1 | Pertahankan dan dokumentasikan sebagai baseline keamanan |
| C | 4.2 (kepatuhan belum diperiksa menyeluruh) | Lakukan verifikasi eksplisit terhadap UU PDP untuk data pelatihan model, terpisah dari verifikasi POJK 11/2022 — kepatuhan terhadap satu regulasi tidak otomatis berarti kepatuhan terhadap regulasi lain yang relevan |

**Poin penilaian mandiri:** Kondisi A sering terlewat karena tim fokus mengamankan data operasional harian, sementara data pelatihan yang tersimpan "di belakang layar" justru berisiko lebih besar karena mencakup data historis dalam skala besar.
</details>

---

## Analisis Kasus: Kembali ke Kasus Ransomware Perbankan

Kasus ransomware yang dibahas di hook menunjukkan bahwa pelaku sempat mengakses sistem "selama beberapa waktu" sebelum aksinya terdeteksi — persis jenis celah yang bisa dicegah dengan audit keamanan berkala (bukan sekali di awal) dan deteksi dini terhadap aktivitas tidak wajar. Kondisi A dalam latihan di atas — data pelatihan yang tidak dienkripsi secara khusus — adalah jenis celah yang sering luput dari perhatian karena tim cenderung fokus mengamankan sistem operasional yang terlihat aktif setiap hari, bukan data yang "tersimpan di belakang layar" seperti data pelatihan model.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Alokasikan sumber daya untuk audit keamanan berkala sebagai bagian dari biaya operasional rutin, bukan pengeluaran darurat setelah insiden terjadi — kasus ransomware menunjukkan biaya kehilangan kepercayaan nasabah jauh lebih mahal daripada investasi pencegahan.

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Rancang alur autentikasi multi-faktor yang tetap praktis bagi petugas kredit — keamanan yang terlalu rumit sering berujung pengguna mencari celah untuk mempermudah, yang justru melemahkan tujuan keamanan itu sendiri.

**Bagi pengembang/petugas teknis (developer/engineer):**
Jangan asumsikan keamanan jaringan internal sudah cukup untuk melindungi data sensitif seperti data pelatihan model — terapkan enkripsi berlapis (defense in depth) di setiap titik yang menyimpan atau memproses data nasabah.

---

## Pertanyaan Refleksi

1. Di organisasimu, apakah audit keamanan dilakukan secara terjadwal rutin, atau baru dilakukan setelah ada insiden atau dorongan eksternal?
2. Data pelatihan model AI sering diabaikan dari perhatian keamanan dibanding data operasional harian. Menurutmu, kenapa hal ini bisa terjadi, dan bagaimana kesadaran ini bisa ditingkatkan di tim teknis?

---

## Ringkasan Lesson

- Elemen 4 menuntut penerapan mekanisme pengamanan konkret (enkripsi, autentikasi multi-faktor, audit berkala) dan pemeriksaan kepatuhan terhadap regulasi yang berlaku (POJK, UU PDP, UU Perbankan).
- Kasus ransomware yang berulang kali menghantam institusi perbankan Indonesia menunjukkan bahwa regulasi yang ketat saja tidak cukup tanpa implementasi teknis yang konkret dan konsisten.
- Solusi AI punya permukaan risiko keamanan yang lebih luas dibanding sistem biasa — termasuk data pelatihan model yang sering luput dari perhatian keamanan dibanding data operasional harian.

---

## Referensi

- Undang-Undang Nomor 10 Tahun 1998 tentang Perbankan, Pasal 40 ayat (1).
- Peraturan Otoritas Jasa Keuangan Nomor 11/POJK.03/2022 tentang Penyelenggaraan Teknologi Informasi Oleh Bank Umum.
- Surat Edaran Otoritas Jasa Keuangan Nomor 29/SEOJK.03/2022 tentang Ketahanan dan Keamanan Siber.
- Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi.

---

## Navigasi

**[← M3-L3: Validasi & Pengujian Pascadeployment](l3-validasi-pengujian-pascadeployment)** | **[M3-L5: Dokumentasi & Monitoring Pascadeployment →](l5-dokumentasi-monitoring)**
