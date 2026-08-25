---
title: Melakukan & Mendokumentasikan Perawatan
course: ai-untuk-proses-data
module: 5
module_title: Merawat Solusi AI
lesson: 2
slug: l2-melakukan-mendokumentasikan-perawatan
unit_kompetensi:
  - kode: J.62AIN00.017.1
    nama: Merawat Solusi AI
    elemen: 'Elemen 2: Melakukan perawatan Solusi AI berdasarkan rencana perawatan'
level: Foundational — Competency
kategori: Competency
bloom_level: Apply
durasi_menit: 32
durasi_baca_menit: 17
durasi_latihan_menit: 15
bahasa: Indonesia
duration_minutes: 32
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Di akhir lesson ini, kamu akan mampu:
- Merawat komponen arsitektur lengkap sesuai prosedur dan rencana perawatan
- Mendokumentasikan seluruh aktivitas perawatan sesuai standar dokumentasi

---

## Hook: Model yang "Sudah Diperbaiki" Tapi Belum Tentu Lebih Baik

Salah satu prinsip dasar dalam siklus kerja machine learning yang sering diabaikan saat perawatan dilakukan terburu-buru: **retraining model harus divalidasi dengan data yang belum pernah dilihat sebelumnya** sebelum dianggap selesai. Ini bukan langkah formalitas — tanpa validasi ini, tim tidak benar-benar tahu apakah model yang baru dilatih ulang benar-benar lebih baik, atau justru memperkenalkan masalah baru yang belum terlihat.

Ini poin yang mudah terlewat karena terasa kontraintuitif: kamu melakukan retraining justru **karena** model lama bermasalah (recall turun, misalnya) — jadi ada godaan untuk menganggap "sudah dilatih ulang" otomatis berarti "sudah lebih baik". Padahal proses retraining sendiri bisa memperkenalkan masalah baru — overfitting ke data terbaru, hilangnya kemampuan menangani pola lama yang masih relevan, atau bias baru dari komposisi data pelatihan yang berubah.

Inilah kenapa Elemen 2 — melakukan DAN mendokumentasikan perawatan — bukan dua tugas terpisah yang bisa dipisah prioritasnya. Dokumentasi yang baik memaksa kamu memvalidasi hasil secara eksplisit sebelum menyatakan perawatan "selesai" — bukan sekadar mencatat "sudah dilakukan retraining" tanpa bukti bahwa hasilnya benar-benar lebih baik.

---

## Kerangka Konseptual: Elemen 2 — Melakukan Perawatan Solusi AI

**2.1 — Komponen arsitektur lengkap dirawat sesuai prosedur dan rencana perawatan**

Eksekusi harus mengikuti rencana yang sudah disusun dan diverifikasi di L1 — bukan improvisasi di tengah jalan. Kalau selama eksekusi ditemukan hal yang tidak sesuai rencana awal, itu perlu dicatat dan dievaluasi, bukan diam-diam diubah tanpa dokumentasi.

**2.2 — Seluruh aktivitas perawatan didokumentasikan sesuai standar dokumentasi**

Dokumentasi mencakup: apa yang dilakukan, kapan, oleh siapa, data apa yang dipakai untuk retraining, dan yang paling penting — **hasil validasi** yang membuktikan perawatan ini benar-benar memperbaiki masalah yang menjadi tujuan awal (bukan sekadar klaim tanpa bukti).

<!-- VISUAL PLACEHOLDER: Diagram alur — "Eksekusi Sesuai Rencana" → "Retraining dengan Data Terbaru" → "Validasi dengan Data Belum Pernah Dilihat" → dua cabang: "Performa Membaik Sesuai Kriteria Sukses (dokumentasikan sebagai selesai)" dan "Performa Belum Sesuai atau Ada Masalah Baru (kembali ke evaluasi, JANGAN deploy)" -->

### Kenapa Validasi Sebelum "Selesai" Sangat Kritis untuk Solusi AI

Ingat prinsip yang berulang di kursus ini sejak Modul 1: sistem yang "terlihat berjalan" atau proses yang "sudah dilakukan" bukan bukti bahwa hasilnya benar. Model yang sudah di-retraining tetap perlu melalui proses validasi yang setara ketatnya dengan pengujian sebelum deployment pertama (Modul 2-3) — bukan diperlakukan sebagai "sekadar update kecil" yang tidak perlu diverifikasi seketat pemasangan awal.

---

## Konteks SPKO: Melakukan dan Mendokumentasikan Perawatan

| Tahap | Aktivitas | Dokumentasi |
|---|---|---|
| Eksekusi retraining | Model dilatih ulang dengan data 3 bulan terakhir, termasuk representasi nasabah tanpa riwayat kredit yang lebih seimbang | Tanggal eksekusi, versi data yang dipakai, konfigurasi pelatihan |
| Validasi | Model baru diuji dengan data yang belum pernah dilihat (holdout data), dibandingkan dengan kriteria sukses dari M4-L4 (recall ≥ 0.80, F1-Score ≥ 0.80) | Hasil metrik validasi, perbandingan dengan model versi sebelumnya |
| Keputusan akhir | Jika hasil validasi memenuhi kriteria, model baru siap menggantikan yang lama (mengikuti prosedur deployment bertahap dari Modul 3) | Keputusan final dan penanggung jawab yang menyetujui |

---

## Quick Check
**(Target: 2 menit)**

**Tim SPKO menyelesaikan retraining model dan mencatat di dokumentasi: "Retraining selesai pada [tanggal], model baru sudah menggantikan versi lama." Apa yang kurang dari dokumentasi ini?**

<details>
<summary>Lihat jawaban</summary>

Dokumentasi ini tidak menyertakan hasil validasi — tidak ada bukti bahwa model baru benar-benar memenuhi kriteria sukses (recall, F1-Score) yang ditetapkan di rencana perawatan. "Sudah dilakukan" bukan sama dengan "sudah terbukti lebih baik". Dokumentasi yang lengkap (KUK 2.2) harus menyertakan hasil validasi dengan data yang belum pernah dilihat sebelumnya, dibandingkan dengan kriteria sukses yang sudah ditetapkan.
</details>

---

## Latihan Terstruktur (Simulasi Singkat)
**(Target: 12 menit)**

**Skenario:** Kamu meninjau tiga laporan hasil perawatan SPKO berikut.

| Laporan | Isi |
|---|---|
| A | "Model diretraining dengan data 3 bulan terakhir. Recall pada data validasi baru: 0.83 (memenuhi target ≥0.80). F1-Score: 0.81. Model disetujui untuk menggantikan versi lama oleh [nama penanggung jawab]." |
| B | "Model diretraining. Hasil terlihat bagus di data latih (recall 0.95), langsung diterapkan ke produksi." |
| C | "Model diretraining, tapi hasil validasi menunjukkan recall hanya 0.74 — di bawah target. Model TIDAK diterapkan, akan dilakukan investigasi tambahan pada data pelatihan." |

**Instruksi:** Tentukan (a) apakah laporan ini memenuhi KUK 2.1-2.2, (b) tindakan yang diperlukan jika ada kekurangan. Kerjakan dalam 12 menit.

<details>
<summary>Lihat kunci jawaban</summary>

| Laporan | Memenuhi KUK? | Tindakan |
|---|---|---|
| A | Ya | Contoh baik — validasi dengan data terpisah, hasil dibandingkan dengan kriteria sukses, ada penanggung jawab yang jelas |
| B | Tidak | **Berbahaya** — recall tinggi di data latih (0.95) tidak sama dengan validasi di data belum pernah dilihat; kemungkinan overfitting. Tindakan: hentikan penerapan, lakukan validasi yang benar dengan holdout data sebelum keputusan diambil |
| C | Ya, meski hasilnya "gagal" | Ini justru contoh baik dari sisi proses — validasi dilakukan dengan benar, dan yang penting: model TIDAK diterapkan karena belum memenuhi kriteria. Kegagalan mencapai target bukan berarti prosesnya salah |

**Poin penilaian mandiri:** Laporan B adalah yang paling berbahaya justru karena "terlihat sukses" (recall 0.95) — ini contoh nyata dari peringatan di hook: hasil bagus di data latih tanpa validasi independen adalah tanda peringatan, bukan bukti keberhasilan.
</details>

---

## Analisis Kasus: Kembali ke Prinsip Validasi Data Terpisah

Laporan B dalam latihan di atas adalah ilustrasi tepat dari risiko yang dibahas di hook — kesalahan yang terasa kontraintuitif karena angka yang ditampilkan (recall 0.95) terlihat sangat baik. Tapi angka tinggi di data yang sama dipakai untuk melatih model adalah sinyal peringatan klasik, bukan bukti keberhasilan — model mungkin hanya "menghafal" data latih, bukan benar-benar belajar pola yang bisa digeneralisasi ke data baru. Laporan C, meski hasilnya "gagal" mencapai target, justru menunjukkan proses yang lebih sehat karena validasinya jujur dan keputusan untuk tidak menerapkan model diambil berdasarkan bukti, bukan berdasarkan harapan.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Jangan menilai keberhasilan perawatan model hanya dari "sudah selesai dikerjakan" — minta bukti validasi konkret dengan data yang independen dari proses pelatihan, dan terima bahwa kadang hasilnya menunjukkan perawatan belum berhasil (seperti Laporan C) — ini bukan kegagalan tim, tapi proses yang berjalan benar.

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Rancang template laporan perawatan yang mewajibkan kolom hasil validasi terisi sebelum status bisa ditandai "selesai" — mencegah laporan seperti B yang melewatkan langkah krusial ini.

**Bagi pengembang/petugas teknis (developer/engineer):**
Selalu sisihkan data yang benar-benar terpisah (tidak pernah dipakai sama sekali dalam proses pelatihan) khusus untuk validasi akhir — jangan menggunakan sebagian data latih sebagai "validasi" karena ini tidak memberikan gambaran jujur tentang kemampuan generalisasi model.

---

## Pertanyaan Refleksi

1. Pernahkah kamu atau timmu tergoda untuk menganggap "sudah dikerjakan" sama dengan "sudah berhasil" tanpa bukti validasi yang memadai? Apa yang terjadi kemudian?
2. Laporan C dalam latihan menunjukkan hasil yang "gagal" tapi prosesnya benar. Bagaimana budaya organisasi bisa dibangun agar tim tidak takut melaporkan hasil validasi yang tidak sesuai target, alih-alih menyembunyikannya?

---

## Ringkasan Lesson

- Elemen 2 menuntut eksekusi perawatan sesuai prosedur dan rencana, serta dokumentasi lengkap yang mencakup hasil validasi — bukan sekadar catatan bahwa aktivitas "sudah dilakukan".
- Validasi model yang diretraining harus memakai data yang belum pernah dilihat sebelumnya — performa tinggi di data latih tanpa validasi independen adalah tanda peringatan overfitting, bukan bukti keberhasilan.
- Hasil validasi yang tidak memenuhi target bukan kegagalan proses — justru menunjukkan proses perawatan yang sehat, selama keputusan untuk tidak menerapkan model diambil berdasarkan bukti.

---

## Referensi

- Prinsip validasi model dengan data terpisah dalam siklus kerja machine learning, literatur teknis pembelajaran mesin, 2024-2025.

---

## Navigasi

**[← M5-L1: Dari Rencana ke Aksi — Menyiapkan Perawatan](l1-menyiapkan-perawatan)** | **[M5-L3: Studi Kasus — Menangani Insiden Performa SPKO →](l3-studi-kasus-insiden-performa)**
