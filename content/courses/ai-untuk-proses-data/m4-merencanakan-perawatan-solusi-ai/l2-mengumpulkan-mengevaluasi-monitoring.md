---
title: Mengumpulkan & Mengevaluasi Hasil Monitoring
course: ai-untuk-proses-data
module: 4
module_title: Merencanakan Perawatan Solusi AI
lesson: 2
slug: l2-mengumpulkan-mengevaluasi-monitoring
unit_kompetensi:
  - kode: J.62AIN00.016.1
    nama: Merencanakan Perawatan Solusi AI
    elemen: 'Elemen 1: Menyiapkan rencana perawatan Solusi AI'
level: Foundational — Competency
kategori: Competency
bloom_level: Analyze
durasi_menit: 32
durasi_baca_menit: 17
durasi_latihan_menit: 15
bahasa: Indonesia
duration_minutes: 17
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Di akhir lesson ini, kamu akan mampu:
- Mengumpulkan hasil monitoring sesuai kebutuhan yang mengacu parameter evaluasi
- Mengevaluasi hasil monitoring sesuai metrik kesuksesan Solusi AI
- Menentukan komponen arsitektur yang harus dirawat berdasarkan hasil evaluasi monitoring

---

## Hook: Mesin yang Merekomendasikan, Manusia yang Memutuskan

Sebuah kasus dari tim engineering di salah satu unicorn Indonesia menunjukkan bagaimana evaluasi berbasis machine intelligence bisa mengubah cara tim merespons masalah operasional. Sistem mereka mendeteksi pola lalu lintas yang meningkat setiap hari Jumat pukul 19.00 WIB, lalu secara otomatis merekomendasikan penambahan kapasitas server di zona tertentu. Rekomendasi ini diterapkan dan berhasil menurunkan tingkat kesalahan sistem dari 2,3 persen menjadi 0,4 persen selama delapan minggu berturut-turut.

Tapi ada satu detail yang lebih penting dari angka-angka itu: sebuah survei terhadap 150 tim engineering di kawasan Asia Pasifik menemukan bahwa **67 persen responden masih ingin melakukan verifikasi manual** terhadap rekomendasi yang dihasilkan mesin, terutama untuk keputusan yang berdampak besar. Ini bukan soal kurang percaya pada teknologi — ini soal tanggung jawab. Ketika sistem salah mengevaluasi, manusia yang harus bertanggung jawab, bukan mesin.

Ini adalah prinsip yang akan membentuk cara kamu bekerja di lesson ini: mengumpulkan dan mengevaluasi hasil monitoring bukan proses yang bisa sepenuhnya diserahkan ke otomasi. Data monitoring memberimu sinyal — tapi keputusan tentang komponen mana yang benar-benar perlu dirawat tetap membutuhkan evaluasi manusia yang memahami konteks bisnis, bukan cuma angka.

---

## Kerangka Konseptual: Elemen 1 — Menyiapkan Rencana Perawatan

**1.1 — Hasil monitoring dikumpulkan sesuai kebutuhan yang mengacu parameter evaluasi**

Ingat lima parameter evaluasi dari L1 (akurasi, presisi, recall, F1-score, MAE). Pengumpulan data monitoring harus terstruktur mengacu ke parameter-parameter ini — bukan sekadar mengumpulkan "semua data yang ada", tapi data yang relevan untuk menjawab pertanyaan spesifik tentang performa SPKO.

**1.2 — Hasil monitoring dievaluasi sesuai metrik kesuksesan Solusi AI**

Evaluasi berarti membandingkan hasil monitoring saat ini dengan **metrik kesuksesan** yang sudah ditetapkan sejak awal (misalnya, target F1-score minimum yang disepakati saat SPKO pertama kali dipasang di Modul 3). Ini adalah perbandingan performa awal saat operasional dimulai versus performa saat ini.

**1.3 — Komponen arsitektur yang harus dirawat ditentukan berdasarkan hasil evaluasi monitoring**

Hasil evaluasi ini bukan cuma angka di laporan — ia harus diterjemahkan jadi keputusan konkret: komponen mana yang butuh perhatian? Apakah model perlu dilatih ulang? Apakah masalahnya di kualitas data, bukan di modelnya?

<!-- VISUAL PLACEHOLDER: Diagram alur — "Data Monitoring Terkumpul" → "Bandingkan dengan Metrik Kesuksesan Awal" → dua cabang: "Sesuai Target (lanjutkan)" dan "Di Bawah Target (identifikasi komponen bermasalah)" → "Verifikasi Manusia Sebelum Keputusan Final" -->

### Kenapa Verifikasi Manusia Tetap Kritis untuk Solusi AI

Sistem otomatis bisa mendeteksi pola dan bahkan merekomendasikan tindakan — seperti contoh di hook. Tapi bagi Solusi AI yang menangani keputusan kredit, konsekuensi dari keputusan yang salah (baik terlalu cepat merawat komponen yang sebenarnya baik-baik saja, atau terlambat merawat komponen yang benar-benar bermasalah) bisa berdampak langsung ke nasabah. Inilah kenapa evaluasi hasil monitoring — meski dibantu otomasi untuk mengumpulkan dan menyajikan data — tetap membutuhkan keputusan manusia yang memahami konteks bisnis sebelum menentukan tindakan perawatan.

---

## Konteks SPKO: Mengevaluasi Hasil Monitoring

| Data Monitoring | Metrik Kesuksesan Awal | Hasil Saat Ini | Evaluasi |
|---|---|---|---|
| F1-Score model | 0.85 (target minimum) | 0.79 | Di bawah target — perlu investigasi lebih lanjut |
| Waktu respons sistem | < 2 detik | 1.8 detik | Sesuai target |
| Distribusi skor kredit | Stabil dari bulan ke bulan | Bergeser signifikan bulan ini | Perlu diselidiki — apakah wajar (perubahan kondisi ekonomi) atau bermasalah? |

**Keputusan awal berdasarkan tabel ini:** F1-Score yang turun di bawah target menjadi prioritas utama untuk diselidiki lebih lanjut — apakah karena data drift, atau masalah lain yang akan kamu identifikasi di L3.

---

## Quick Check
**(Target: 2 menit)**

**Sistem monitoring otomatis SPKO merekomendasikan "tidak perlu tindakan" karena semua metrik dalam batas normal. Apakah rekomendasi ini bisa langsung diterima tanpa evaluasi tambahan? Jawab 1-2 kalimat.**

<details>
<summary>Lihat jawaban</summary>

Tergantung tingkat risikonya — untuk keputusan berdampak besar seperti Solusi AI yang menangani kredit, prinsip yang sama dengan survei di hook tetap berlaku: verifikasi manusia terhadap rekomendasi otomatis penting, terutama untuk memastikan tidak ada konteks bisnis yang terlewat oleh sistem otomatis (misalnya, metrik "dalam batas normal" tapi ada tren perlahan yang mengarah ke masalah di masa depan).
</details>

---

## Latihan Terstruktur (Simulasi Singkat)
**(Target: 12 menit)**

**Skenario:** Kamu meninjau hasil monitoring bulanan SPKO berikut.

| Data | Kondisi |
|---|---|
| A | Recall model turun dari 0.82 menjadi 0.71 dalam 2 bulan terakhir, bertepatan dengan meningkatnya keluhan nasabah yang merasa ditolak kreditnya secara tidak wajar |
| B | Semua metrik stabil dalam batas target selama 6 bulan berturut-turut |
| C | Akurasi keseluruhan tetap tinggi (94%), tapi recall untuk kelompok nasabah tanpa riwayat kredit turun signifikan |

**Instruksi:** Tentukan (a) apakah ini butuh evaluasi lebih lanjut/tindakan, (b) komponen apa yang mungkin perlu dirawat. Kerjakan dalam 12 menit.

<details>
<summary>Lihat kunci jawaban</summary>

| Data | Perlu Tindakan? | Komponen yang Mungkin Perlu Dirawat |
|---|---|---|
| A | Ya, urgent | Model kemungkinan mengalami drift; korelasi dengan keluhan nasabah memperkuat urgensi — perlu investigasi model dan kemungkinan retraining |
| B | Tidak — lanjutkan monitoring rutin | Tidak ada, dokumentasikan sebagai baseline sehat |
| C | Ya | Ini mirip pola yang sudah dipelajari di Modul 2 (Hasil B, akurasi tinggi tapi ada pola kegagalan tersembunyi) — model mungkin perlu dilatih ulang dengan data yang lebih representatif untuk kelompok nasabah tanpa riwayat kredit |

**Poin penilaian mandiri:** Data C adalah yang paling mudah terlewat kalau kamu hanya melihat akurasi keseluruhan (94% terlihat baik) — pola ini seharusnya sudah kamu kenali dari Modul 2, menegaskan pentingnya tidak berhenti di satu angka ringkasan.
</details>

---

## Analisis Kasus: Kembali ke Verifikasi Manusia

Contoh di hook menunjukkan sisi positif otomasi — mendeteksi pola dan merekomendasikan tindakan jauh lebih cepat dari manusia. Tapi survei 67% yang tetap ingin verifikasi manual menegaskan batasnya: otomasi baik untuk mengumpulkan dan menyajikan data (KUK 1.1), tapi evaluasi final terhadap apa yang benar-benar butuh perawatan (KUK 1.2-1.3) tetap perlu penilaian manusia yang memahami konteks — seperti korelasi antara Data A dalam latihan di atas dengan keluhan nasabah, sesuatu yang mungkin tidak langsung "terlihat" oleh sistem otomatis yang hanya melihat angka metrik semata.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Investasikan dalam sistem monitoring otomatis untuk efisiensi pengumpulan data, tapi jangan hilangkan lapisan evaluasi manusia untuk keputusan perawatan yang berdampak besar — kombinasi keduanya, bukan salah satu saja.

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Dashboard evaluasi monitoring sebaiknya menyandingkan data metrik dengan konteks bisnis yang relevan (seperti tren keluhan nasabah) — bukan menampilkan angka metrik dalam ruang hampa tanpa konteks pendukung.

**Bagi pengembang/petugas teknis (developer/engineer):**
Bangun sistem yang memudahkan korelasi antar sumber data berbeda (metrik model, keluhan nasabah, log operasional) — evaluasi yang baik sering butuh menggabungkan beberapa sumber data, bukan hanya satu dashboard performa model.

---

## Pertanyaan Refleksi

1. Di organisasimu, seberapa besar kepercayaan diberikan pada rekomendasi otomatis dibanding verifikasi manual? Apakah keseimbangannya sudah tepat menurutmu?
2. Data A dalam latihan menunjukkan korelasi antara penurunan recall dan keluhan nasabah. Sumber data lain apa yang menurutmu penting digabungkan saat mengevaluasi hasil monitoring Solusi AI?

---

## Ringkasan Lesson

- Elemen 1 menuntut pengumpulan data monitoring yang terstruktur mengacu parameter evaluasi, dibandingkan dengan metrik kesuksesan yang sudah ditetapkan, untuk menentukan komponen yang perlu dirawat.
- Kasus dari tim engineering Indonesia menunjukkan kekuatan otomasi dalam mendeteksi pola dan merekomendasikan tindakan — tapi survei industri menegaskan verifikasi manusia tetap penting untuk keputusan berdampak besar.
- Evaluasi hasil monitoring yang baik menggabungkan data metrik dengan konteks bisnis (seperti keluhan nasabah), bukan hanya melihat angka dalam ruang hampa.

---

## Referensi

- Analisis mengenai evaluasi berbasis machine intelligence dan hubungannya dengan performa platform, termasuk survei terhadap tim engineering Asia Pasifik, 2026.

---

## Navigasi

**[← M4-L1: Memahami Parameter Evaluasi Solusi AI](l1-parameter-evaluasi)** | **[M4-L3: Menyusun Rencana Perawatan →](l3-menyusun-rencana-perawatan)**
