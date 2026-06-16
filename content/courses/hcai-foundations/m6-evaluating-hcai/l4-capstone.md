---
course: hcai-foundations
module: 6
module_title: "Evaluating and Improving HCAI Systems"
lesson: 4
title: "Capstone: Evaluasi dan Rekomendasikan Perbaikan untuk Satu Produk AI Nyata"
duration_minutes: 18
bloom_level: evaluate
keywords:
  - HCAI product evaluation
  - applied human-centered AI audit
  - AI improvement recommendation
  - HCAI capstone project
  - human-centered AI assessment
is_free: true
status: draft
---

# Capstone: Evaluasi dan Rekomendasikan Perbaikan untuk Satu Produk AI Nyata

**Modul 6 · Evaluating and Improving HCAI Systems** · Lesson 4 dari 4
**Estimasi waktu baca:** ~8 menit · **Estimasi waktu pengerjaan:** 20–30 menit · **Level:** Foundational · **Prasyarat:** M6-L1 s/d M6-L3

---

> **Yang akan kamu capai di capstone ini:**
> - Mengevaluasi satu produk AI menggunakan kerangka terintegrasi dari seluruh kursus ini
> - Merekomendasikan perbaikan konkret berdasarkan analisis yang terstruktur
> - Menghasilkan dokumen evaluasi yang bisa digunakan sebagai dasar keputusan nyata

---

## Pengantar

Sejak M1-L4, kamu sudah memiliki produk AI yang dipilih untuk dianalisis. Kamu membawa produk itu melalui:
- Audit empat prinsip HCAI (M3-L5)
- Latihan IFRAME (M5-L4)
- Dan sekarang, evaluasi komprehensif menggunakan semua kerangka dari enam modul ini.

Ini bukan latihan akademis. Output capstone ini adalah dokumen evaluasi yang bisa kamu gunakan, bagikan kepada tim, atau jadikan dasar untuk diskusi perubahan produk yang nyata.

---

## Kerangka Evaluasi Capstone: Enam Dimensi

Capstone ini menggunakan enam dimensi yang masing-masing terhubung langsung ke modul yang relevan.

---

### Dimensi 1 — Kejelasan Ruang Masalah dan Pemangku Kepentingan
*(Dari M1, M3-L4, M5-L2 — IFRAME: Identify)*

**Pertanyaan evaluasi:**
1. Apakah sistem ini menjawab masalah yang jelas dan signifikan bagi penggunanya?
2. Siapa semua pihak yang terdampak — termasuk yang tidak terlihat dalam antarmuka?
3. Apakah ada kelompok yang terdampak tapi tidak dilibatkan dalam desain?

**Skala penilaian:** 1 (tidak jelas/tidak ada) → 5 (sangat jelas/komprehensif)

**Catatanmu:**

---

### Dimensi 2 — Empat Prinsip HCAI
*(Dari M3-L1 s/d M3-L4)*

Gunakan pertanyaan diagnostik yang sudah dikembangkan di M3-L5, dengan kedalaman analisis yang lebih besar berdasarkan semua yang sudah dipelajari.

**Transparency:**
- Apakah pengguna tahu AI terlibat dalam keputusan ini?
- Apakah faktor yang mempengaruhi keputusan dapat diketahui?
- Apakah batas sistem dikomunikasikan secara proaktif?

*Penilaian (1-5):* ___

**Fairness:**
- Apakah performa sistem telah diperiksa untuk semua kelompok pengguna yang relevan?
- Apakah ada kelompok yang secara sistematis mendapat hasil lebih buruk?
- Apakah definisi fairness yang digunakan sudah dideklarasikan?

*Penilaian (1-5):* ___

**Human Control:**
- Apakah ada mekanisme kontrol yang bermakna (bukan hanya nominal)?
- Apakah tingkat otomasi sesuai dengan taruhan keputusan?
- Apakah pengguna terlatih untuk menggunakan mekanisme kontrol?

*Penilaian (1-5):* ___

**Accountability:**
- Apakah ada entitas yang jelas bertanggung jawab atas dampak sistem?
- Apakah ada mekanisme banding yang dapat diakses?
- Apakah sistem meninggalkan jejak audit yang dapat diperiksa?

*Penilaian (1-5):* ___

---

### Dimensi 3 — Eksplanabilitas dan Fairness dalam Praktik
*(Dari M4-L1 s/d M4-L3)*

**Pertanyaan evaluasi:**
1. Jenis penjelasan apa yang tersedia — global, lokal, kontrafaktual?
2. Apakah penjelasan yang ada melayani semua audiens yang membutuhkannya (pengguna, developer, regulator)?
3. Dari mana kemungkinan besar bias berasal — data, model, atau konteks deployment?
4. Apakah ada bukti bahwa bias telah dideteksi dan ditangani?

**Temuan utamamu:**

---

### Dimensi 4 — Alir dan Keputusan Desain
*(Dari M5-L2 dan M5-L3 — IFRAME: Flow, Rank, Apply)*

**Pertanyaan evaluasi:**
1. Apakah alir utama produk ini sudah terdefinisi dengan jelas — termasuk alir kegagalan?
2. Di mana dalam alir keputusan AI terlibat, dan apakah desain pada titik itu mendukung kontrol yang bermakna?
3. Apakah trade-off desain utama sudah didokumentasikan (decision log tersedia)?

**Temuan utamamu:**

---

### Dimensi 5 — Evaluasi dan Pengukuran
*(Dari M6-L1, M6-L2, M6-L3 — dan konsep dari M2 tentang mental model dan kalibrasi kepercayaan)*

**Pertanyaan evaluasi:**
1. Dimensi evaluasi mana yang saat ini diukur (metrik model, interaksi, sistem, dampak)?
2. Metode evaluasi apa yang digunakan — dan apakah tepat untuk pertanyaan yang perlu dijawab?
3. Apakah kepercayaan pengguna diukur — dan jika ya, apakah sikap atau perilaku atau keduanya?
4. Apakah ada bukti bahwa mental model pengguna tentang kapabilitas dan batas sistem sudah akurat — bukan hanya bahwa mereka bisa menggunakan sistem?

**Temuan utamamu:**

---

### Dimensi 6 — Pengetahuan Organisasi
*(Dari M5-L2 — IFRAME: Expose)*

**Pertanyaan evaluasi:**
1. Jika tim yang membangun sistem ini bubar hari ini, apakah pengetahuan tentang keputusan desain kritis bisa direkonstruksi?
2. Apakah ada dokumentasi yang memungkinkan tim baru memahami *mengapa* sistem dibangun dengan cara tertentu?
3. Apakah ada proses untuk belajar dari kegagalan sistem secara sistematis?

**Temuan utamamu:**

---

## Template Dokumen Evaluasi

Setelah mengisi enam dimensi, rangkum dalam format berikut:

```
EVALUASI HCAI — [Nama Produk]
Tanggal: [Tanggal]
Evaluator: [Nama/Peran]

RINGKASAN EKSEKUTIF (2-3 kalimat):
[Apa kesimpulan paling penting dari evaluasi ini?]

PENILAIAN PER DIMENSI:
Dimensi 1 — Ruang Masalah & Pemangku Kepentingan:  [1-5]
Dimensi 2a — Transparency:  [1-5]
Dimensi 2b — Fairness:  [1-5]
Dimensi 2c — Human Control:  [1-5]
Dimensi 2d — Accountability:  [1-5]
Dimensi 3 — Eksplanabilitas & Fairness dalam Praktik:  [1-5]
Dimensi 4 — Alir & Keputusan Desain:  [1-5]
Dimensi 5 — Evaluasi & Pengukuran:  [1-5]
Dimensi 6 — Pengetahuan Organisasi:  [1-5]

TIGA CELAH TERPENTING:
1. [Celah dengan dampak tertinggi — deskripsi konkret]
2. [Celah dengan urgensi tertinggi]
3. [Celah yang paling mudah diperbaiki dalam 30 hari]

TIGA REKOMENDASI KONKRET:
1. [Rekomendasi untuk celah pertama]
   Effort: Rendah / Sedang / Tinggi
   Dampak: Rendah / Sedang / Tinggi
   Prinsip HCAI yang diperkuat: [Transparency/Fairness/Control/Accountability]

2. [Rekomendasi untuk celah kedua]
   Effort: ...
   Dampak: ...
   Prinsip HCAI yang diperkuat: ...

3. [Rekomendasi untuk celah ketiga]
   Effort: ...
   Dampak: ...
   Prinsip HCAI yang diperkuat: ...

CATATAN UNTUK TIM BERIKUTNYA:
[Satu paragraf tentang apa yang perlu diketahui tim berikutnya
 berdasarkan evaluasi ini — format Expose IFRAME]
```

---

## Contoh: Evaluasi Singkat untuk Sistem Navigasi GPS

Untuk memberikan referensi tentang level kedalaman yang diharapkan, berikut contoh evaluasi singkat yang sudah diisi:

**Dimensi 2 — Empat Prinsip:**

*Transparency (3/5):* Pengguna tahu sistem menggunakan data lalu lintas real-time (transparency proses: baik). Tapi kondisi di mana akurasi lebih rendah — daerah dengan data crowdsourced yang tipis — tidak dikomunikasikan (transparency batas: lemah).

*Fairness (3/5):* Kualitas layanan berbeda secara signifikan antara kota besar dan daerah rural atau peri-urban — tanpa pengguna tahu perbedaan ini ada. Pengguna di daerah dengan data lebih sedikit mendapat akurasi lebih rendah secara konsisten.

*Human Control (4/5):* Pengguna bisa memilih rute alternatif kapan saja, dan kontrol ini mudah digunakan. Kelemahannya: tidak ada penjelasan mengapa rute tertentu disarankan, membuat override sulit dilakukan secara terinformasi.

*Accountability (2/5):* Tidak ada mekanisme banding yang jelas. Jika navigasi menyebabkan kerugian (rute yang salah di kondisi darurat), tidak ada jalur yang jelas untuk pertanggungjawaban.

**Celah terpenting:** Transparency batas dan Accountability adalah dua titik paling lemah dengan dampak nyata pada pengguna yang paling rentan (pengguna di daerah dengan data tipis).

**Rekomendasi konkret:** Tampilkan confidence indicator sederhana untuk estimasi waktu berdasarkan densitas data — "estimasi ini berdasarkan X laporan aktif di rute ini." Effort rendah, dampak langsung pada transparency dan trust calibration.

---

## Panduan Interpretasi Hasil

**Penilaian rata-rata 4.0–5.0:** Sistem sudah menerapkan prinsip HCAI dengan baik. Fokus pada konsistensi dan monitoring berkelanjutan.

**Penilaian rata-rata 2.5–3.9:** Ada fondasi yang baik tapi celah yang signifikan. Prioritaskan rekomendasi berdasarkan kombinasi dampak dan feasibility.

**Penilaian rata-rata di bawah 2.5:** Celah sistemik yang membutuhkan perubahan fundamental, bukan perbaikan inkremental. Rekomendasikan review menyeluruh sebelum peluncuran lebih lanjut.

---

## Pertanyaan Refleksi

> Kamu baru saja menyelesaikan evaluasi yang menggunakan kerangka dari enam modul — dari definisi HCAI (M1) sampai pengukuran kepercayaan (M6-L3), dari prinsip-prinsip (M3) sampai metodologi desain (M5).
>
> **Dua pertanyaan untuk menutup kursus ini:**
>
> Pertama: Sebelum memulai kursus ini, dimensi mana dari evaluasi di atas yang tidak pernah kamu pertimbangkan? Dan apa yang berubah dalam cara kamu berpikir tentang produk AI?
>
> Kedua: Dari tiga rekomendasi yang kamu tulis, mana yang paling mungkin kamu tindaklanjuti dalam 30 hari ke depan — dan siapa yang perlu kamu ajak bicara untuk memulainya?

---

## Ringkasan Modul 6 dan Kursus

**Modul 6 membangun kemampuan evaluasi:**

- **L1:** Akurasi tidak cukup — empat dimensi evaluasi dan kerangka dua tingkat yang memisahkan evaluasi sistem dari evaluasi sistem-dalam-konteks.
- **L2:** Tiga metode evaluasi human-centered — think-aloud (mental model), Wizard of Oz (konsep pre-implementation), dan field study (efek jangka panjang) — dengan matriks pemilihan yang jelas.
- **L3:** Kepercayaan sikap vs perilaku vs kalibrasi — instrumen tervalidasi (Jian et al., 2000) dan pendekatan tiga sumber untuk gambaran komprehensif.
- **L4:** Capstone — evaluasi terintegrasi menggunakan semua kerangka kursus.

---

**Kursus Human-Centered AI — Foundations telah selesai.**

Enam modul. Dua puluh satu lesson. Satu benang merah: AI yang benar-benar bekerja untuk manusia bukan sekadar AI yang akurat — ia adalah AI yang dirancang dengan pemahaman tentang manusia, diimplementasikan dengan prinsip yang jelas, dan dievaluasi terhadap dampak nyata pada kehidupan manusia.

Itu bukan tujuan yang mudah. Tapi dengan kerangka yang kamu miliki sekarang, ini adalah tujuan yang bisa dikerjakan — secara sistematis, secara bertanggung jawab, dan secara konsisten.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
