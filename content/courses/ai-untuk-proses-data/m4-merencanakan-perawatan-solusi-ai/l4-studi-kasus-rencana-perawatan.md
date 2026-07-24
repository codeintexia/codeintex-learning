---
title: 'Studi Kasus: Menyusun Rencana Perawatan SPKO'
course: ai-untuk-proses-data
module: 4
module_title: Merencanakan Perawatan Solusi AI
lesson: 4
slug: l4-studi-kasus-rencana-perawatan
unit_kompetensi:
  - kode: J.62AIN00.016.1
    nama: Merencanakan Perawatan Solusi AI
    elemen: Latihan terintegrasi Elemen 1-2
level: Foundational — Competency
kategori: Competency
bloom_level: Evaluate
durasi_menit: 35
durasi_baca_menit: 8
durasi_latihan_menit: 27
bahasa: Indonesia
duration_minutes: 8
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Lesson ini adalah **latihan terintegrasi** yang menutup Modul 4 — menggabungkan semua yang sudah kamu pelajari di L1 (parameter evaluasi), L2 (mengevaluasi hasil monitoring), dan L3 (menyusun rencana perawatan) dalam satu skenario yang lebih kompleks, meniru kondisi yang akan kamu hadapi saat demonstrasi kompetensi.

Di akhir lesson ini, kamu akan mampu:
- Mengevaluasi data monitoring multi-dimensi secara mandiri
- Mengidentifikasi komponen yang perlu dirawat berdasarkan bukti, bukan asumsi
- Menyusun rencana perawatan lengkap yang terdokumentasi sesuai standar

---

## Konteks: Tiga Bulan Operasional SPKO

Bank Nusantara Sejahtera telah mengoperasikan SPKO selama tiga bulan sejak deployment di Modul 3. Sebagai bagian dari tim yang bertanggung jawab merencanakan perawatan, kamu menerima laporan monitoring triwulanan berikut untuk dievaluasi.

### Data Monitoring Triwulanan SPKO

| Metrik | Bulan 1 | Bulan 2 | Bulan 3 | Target Awal |
|---|---|---|---|---|
| Akurasi keseluruhan | 93% | 92% | 94% | ≥ 90% |
| Presisi | 0.81 | 0.79 | 0.80 | ≥ 0.75 |
| Recall | 0.83 | 0.76 | 0.68 | ≥ 0.80 |
| F1-Score | 0.82 | 0.77 | 0.74 | ≥ 0.80 |
| Waktu respons rata-rata | 1.6 detik | 1.7 detik | 1.9 detik | < 2 detik |

### Informasi Tambahan
- Jumlah keluhan nasabah terkait "penolakan kredit yang terasa tidak wajar" meningkat 40% di Bulan 3 dibanding Bulan 1.
- OJK menerbitkan penyesuaian kebijakan suku bunga acuan pada pertengahan Bulan 2.
- Tim core banking melaporkan tidak ada perubahan skema data sejak deployment (berbeda dari skenario "silent schema drift" di Modul 3).
- Distribusi pengajuan kredit dari nasabah tanpa riwayat kredit sebelumnya meningkat sejak Bulan 2, sebagai bagian dari inisiatif bank memperluas akses kredit sesuai POJK 29/2024.

---

## Latihan Terstruktur: Evaluasi dan Rencana Perawatan Lengkap
**(Target: 25 menit — ini latihan lebih besar dari biasanya, meniru skala demonstrasi kompetensi sesungguhnya)**

Kerjakan empat tugas berikut secara berurutan.

### Tugas 1 — Identifikasi Metrik Bermasalah (5 menit)
Dari tabel di atas, metrik mana yang menunjukkan tren mengkhawatirkan, dan metrik mana yang masih sehat?

### Tugas 2 — Analisis Akar Masalah (8 menit)
Berdasarkan informasi tambahan yang tersedia, susun hipotesis tentang akar masalah dari metrik yang bermasalah. Pertimbangkan lebih dari satu kemungkinan penyebab.

### Tugas 3 — Prioritas Tindakan (5 menit)
Tentukan tindakan mana yang paling mendesak untuk dilakukan lebih dulu, dan mana yang bisa menunggu.

### Tugas 4 — Susun Rencana Perawatan (7 menit)
Buat rencana perawatan singkat mengikuti elemen kunci dari L3 (akar masalah, tindakan, prioritas, sumber daya, kriteria sukses).

---

<details>
<summary>Lihat kunci jawaban lengkap</summary>

### Tugas 1 — Metrik Bermasalah

**Bermasalah:** Recall (turun dari 0.83 ke 0.68, penurunan tajam) dan F1-Score (turun dari 0.82 ke 0.74, sudah di bawah target 0.80 sejak Bulan 3).

**Masih sehat:** Akurasi keseluruhan (stabil di atas target), presisi (relatif stabil), waktu respons (masih dalam target meski sedikit meningkat).

**Poin penting:** Kalau kamu hanya melihat akurasi (94% di Bulan 3, bahkan naik), kamu akan salah menyimpulkan semuanya baik-baik saja — ini persis prinsip yang sudah dipelajari sejak Modul 2 (akurasi hanyalah satu sisi mata uang).

### Tugas 2 — Analisis Akar Masalah

Ada **dua hipotesis yang sama-sama masuk akal**, dan keduanya perlu dipertimbangkan bersamaan, bukan saling eksklusif:

**Hipotesis A — Data drift dari perubahan kebijakan suku bunga OJK:** Penyesuaian kebijakan di Bulan 2 bertepatan langsung dengan mulai turunnya recall. Ini konsisten dengan prinsip data drift yang dipelajari di Modul 3 — pola yang dipelajari model sebelum perubahan kebijakan tidak lagi merepresentasikan kondisi setelahnya.

**Hipotesis B — Pergeseran komposisi data akibat perluasan akses kredit:** Meningkatnya proporsi nasabah tanpa riwayat kredit (sejak Bulan 2, sejalan dengan POJK 29/2024) berarti model semakin sering menghadapi profil data yang mungkin kurang terwakili di data pelatihan awal — mirip pola yang sudah dipelajari di Modul 2 (Kondisi C: akurasi tinggi tapi recall rendah untuk kelompok tertentu).

**Yang BUKAN penyebab:** Perubahan skema data (tim core banking mengonfirmasi tidak ada perubahan) — ini penting untuk mengeliminasi kemungkinan yang salah, bukan berasumsi tanpa verifikasi.

### Tugas 3 — Prioritas Tindakan

**Mendesak:** Investigasi kedua hipotesis akar masalah secara paralel — korelasi dengan keluhan nasabah (naik 40%) menunjukkan dampak nyata sudah terjadi, bukan sekadar risiko teoretis.

**Bisa menunggu:** Waktu respons (1.9 detik) masih dalam target, meski tren meningkat — perlu dipantau tapi belum mendesak untuk tindakan segera.

### Tugas 4 — Contoh Rencana Perawatan

| Elemen | Isi |
|---|---|
| Akar masalah | Kombinasi data drift dari kebijakan suku bunga dan pergeseran komposisi data nasabah tanpa riwayat kredit |
| Tindakan | (1) Analisis data Bulan 2-3 dibanding data pelatihan untuk konfirmasi drift; (2) Evaluasi representasi nasabah tanpa riwayat kredit di data pelatihan; (3) Retraining model dengan data terbaru yang mencakup kedua faktor ini |
| Prioritas | Tinggi — korelasi dengan keluhan nasabah nyata, bukan sekadar penurunan angka di dashboard |
| Sumber daya | Tim data science, akses data 3 bulan terakhir, kemungkinan konsultasi dengan tim kepatuhan terkait implikasi POJK 29/2024 |
| Kriteria sukses | Recall kembali ke ≥ 0.80 dan F1-Score ≥ 0.80, tervalidasi dengan data uji yang mencakup proporsi nasabah tanpa riwayat kredit yang representatif |

</details>

---

## Refleksi Penutup Modul 4

Modul 4 ini menutup dengan satu pelajaran yang berulang sepanjang kursus: **data monitoring yang lengkap tidak berguna tanpa evaluasi yang cermat, dan evaluasi yang cermat tidak berguna tanpa rencana yang actionable.** Ketiga elemen — parameter evaluasi (L1), evaluasi hasil monitoring (L2), dan penyusunan rencana (L3) — adalah rantai yang harus utuh, bukan langkah-langkah terpisah yang bisa dilewati sebagian.

Rencana perawatan yang kamu susun di lesson ini akan menjadi **input langsung** bagi Modul 5 — di mana kamu akan mempelajari bagaimana benar-benar mengeksekusi perawatan berdasarkan rencana ini.

---

## Ringkasan Modul 4

- Parameter evaluasi (akurasi, presisi, recall, F1-score, MAE) masing-masing menjawab pertanyaan berbeda — mengandalkan satu metrik saja berisiko menyembunyikan masalah nyata.
- Evaluasi hasil monitoring membutuhkan kombinasi data kuantitatif (metrik) dan konteks bisnis (keluhan nasabah, perubahan regulasi) — bukan angka dalam ruang hampa.
- Rencana perawatan yang baik mengidentifikasi akar masalah secara spesifik (bahkan mempertimbangkan lebih dari satu hipotesis), bukan tindakan generik yang menyasar gejala.
- Skenario nyata sering melibatkan lebih dari satu penyebab yang bekerja bersamaan — seperti kombinasi data drift dan pergeseran komposisi data di studi kasus ini.

---

## Navigasi

**[← M4-L3: Menyusun Rencana Perawatan](l3-menyusun-rencana-perawatan)** | **[M5-L1: Dari Rencana ke Aksi — Menyiapkan Perawatan →](../m5-merawat-solusi-ai/l1-menyiapkan-perawatan)**
