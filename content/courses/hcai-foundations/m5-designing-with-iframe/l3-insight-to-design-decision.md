---
course: hcai-foundations
module: 5
module_title: "Designing Human-Centered AI with IFRAME"
lesson: 3
title: "Dari Insight Pengguna ke Keputusan Desain AI: Menjembatani Gap yang Sering Terabaikan"
duration_minutes: 14
bloom_level: apply
keywords:
  - research to design AI
  - translating user insights to AI features
  - design decision AI
  - HCAI insight translation
  - user research AI product design
is_free: true
status: draft
---

# Dari Insight Pengguna ke Keputusan Desain AI: Menjembatani Gap yang Sering Terabaikan

**Modul 5 · Designing Human-Centered AI with IFRAME** · Lesson 3 dari 4
**Estimasi waktu baca:** 14 menit · **Level:** Foundational · **Prasyarat:** M5-L2

---

> **Yang akan kamu capai di lesson ini:**
> - Menerapkan kerangka empat tipe insight untuk memetakan temuan riset pengguna ke keputusan desain AI yang spesifik
> - Menggunakan konsep "decision log" sebagai jembatan antara riset dan implementasi
> - Membangun alur dari insight ke keputusan menggunakan tahap Identify dan Flow dalam IFRAME

---

## Hook

Sebuah tim riset UX baru saja menyelesaikan studi 6 minggu yang komprehensif tentang bagaimana pasien diabetes menggunakan aplikasi manajemen insulin berbasis AI. Mereka mewawancarai 40 pasien, melakukan observasi lapangan, dan menganalisis data kuantitatif dari 2.000 pengguna.

Hasilnya? Tiga temuan yang sangat kuat:

1. Pasien berusia di atas 55 tahun secara konsisten tidak memahami kapan mereka harus mengikuti rekomendasi AI vs bertanya kepada dokter.
2. Pasien dengan pengalaman lebih dari 10 tahun cenderung mengabaikan rekomendasi karena merasa "lebih tahu dari aplikasi."
3. Waktu pengambilan keputusan meningkat 40% ketika aplikasi menampilkan confidence interval dibanding hanya menampilkan angka tunggal.

Laporan riset ditulis, dipresentasikan kepada stakeholder, dan... berhenti di sana.

Tim engineering yang mengimplementasikan fitur berikutnya tidak pernah melihat laporan itu. Tim desain yang membuat wireframe baru tidak mengetahui temuan nomor 3. Model AI diperbarui dengan data baru tanpa mempertimbangkan implikasinya terhadap temuan nomor 1.

Enam bulan kemudian, tim riset melakukan studi lanjutan dan menemukan masalah yang sama. **Risetnya sudah ada. Insightnya sudah ada. Tapi tidak ada yang mengubah insight itu menjadi keputusan desain yang konkret.**

Ini adalah "translation gap" — dan ini adalah salah satu masalah paling umum dan paling mahal dalam pengembangan produk AI.

---

## Kerangka Konseptual

### Mengapa translation gap terjadi

Translation gap bukan karena peneliti yang buruk atau desainer yang tidak peduli. Ia terjadi karena tidak ada struktur yang memastikan insight menemukan jalan dari penelitian ke implementasi secara sistematis.

Dalam proses konvensional, riset menghasilkan laporan. Laporan dipresentasikan. Kemudian setiap anggota tim menginterpretasikan implikasinya secara berbeda — atau tidak menginterpretasikannya sama sekali.

Yang dibutuhkan bukan laporan yang lebih panjang atau presentasi yang lebih menarik. Yang dibutuhkan adalah kerangka yang mengklasifikasikan insight berdasarkan *jenis keputusan desain yang mereka implikasikan* — sehingga setiap insight langsung terhubung ke orang yang tepat dan keputusan yang tepat.

<!-- DIAGRAM: Empat Tipe Insight ke Tahap IFRAME
     Render sebagai diagram mapping dua kolom saat membangun UI.
     Kolom kiri: 4 tipe insight (masing-masing dengan warna berbeda)
       1. Mental model (biru)
       2. Kalibrasi kepercayaan (oranye)
       3. Gangguan alir (merah)
       4. Fairness persepsi (hijau)
     Kolom kanan: 6 tahap IFRAME
       Identify · Flow · Rank · Apply · Measure · Expose
     Panah dari setiap insight ke tahap yang relevan:
       Mental model → Identify + Flow
       Kalibrasi kepercayaan → Rank + Apply
       Gangguan alir → Flow + Rank
       Fairness persepsi → Identify + Measure
     Warna panah sesuai warna insight type
-->

### Empat tipe insight dan keputusan desain yang mereka implikasikan

**Tipe 1 — Insight mental model:**
Deskripsi: Bagaimana pengguna memahami cara kerja sistem, apa yang mereka asumsikan tentang kapabilitasnya, dan di mana pemahaman mereka berbeda dari realitas.

Contoh dari kasus insulin: *"Pasien berusia di atas 55 tahun tidak memahami kapan harus mengikuti AI vs dokter"* → ini adalah mental model gap tentang agen (M2-L2).

Keputusan desain yang diimplikasikan: desain eksplanabilitas (dari M4-L1) — antarmuka harus secara proaktif mengomunikasikan kapan sistem lebih reliable dan kapan manusia harus mengambil alih.

Tahap IFRAME: insight ini masuk ke **Identify** (mendefinisikan siapa yang terdampak dan bagaimana) dan **Flow** (mendefinisikan titik dalam alir di mana keputusan ini terjadi).

**Tipe 2 — Insight kalibrasi kepercayaan (trust calibration):**
Deskripsi: Apakah pengguna mempercayai sistem secara proporsional — overtrusting atau undertrusting — dan dalam kondisi apa.

Contoh dari kasus insulin: *"Pasien berpengalaman cenderung mengabaikan rekomendasi AI"* → ini adalah algorithm aversion (M2-L3).

Keputusan desain yang diimplikasikan: bagaimana antarmuka membangun kredibilitas yang tepat untuk segmen pengguna ini — bukan dengan mempromosikan akurasi sistem, tapi dengan mengomunikasikan kontribusi unik sistem dibanding pengetahuan manusia.

Tahap IFRAME: insight ini masuk ke **Rank** (apakah mengatasi algorithm aversion diprioritaskan?) dan **Apply** (bagaimana antarmuka dirancang untuk segmen ini).

**Tipe 3 — Insight gangguan alir (flow disruption):**
Deskripsi: Di mana dalam alir pengguna pengalaman terganggu, keputusan tertunda, atau tindakan tidak diambil karena cara sistem menyampaikan informasi.

Contoh dari kasus insulin: *"Waktu pengambilan keputusan meningkat 40% dengan confidence interval"* → ini adalah friction di alir pengambilan keputusan.

Keputusan desain yang diimplikasikan: bagaimana menyampaikan uncertainty tanpa menghambat alir — ada trade-off antara kejujuran tentang ketidakpastian (Transparency) dan efisiensi pengambilan keputusan (usability). Ini adalah keputusan yang harus didokumentasikan secara eksplisit di Rank.

Tahap IFRAME: insight ini masuk langsung ke **Flow** (ini adalah gangguan integritas alir) dan **Rank** (trade-off antara transparency dan usability harus diputuskan secara eksplisit).

**Tipe 4 — Insight fairness persepsi:**
Deskripsi: Bagaimana kelompok pengguna yang berbeda mengalami sistem secara berbeda — termasuk siapa yang merasa terlayani dengan baik dan siapa yang tidak.

Contoh dari kasus insulin: jika analisis disagregasi (M4-L3) menunjukkan bahwa temuan nomor 1 (confusion tentang kapan mengikuti AI) secara tidak proporsional memengaruhi lansia dari latar belakang pendidikan tertentu — ini adalah insight fairness persepsi.

Keputusan desain yang diimplikasikan: desain yang responsif terhadap kelompok yang paling rentan, bukan hanya yang paling mudah dilayani.

Tahap IFRAME: insight ini masuk ke **Identify** (pemetaan siapa yang terdampak) dan **Measure** (kriteria evaluasi harus mencakup fairness antar segmen).

### Decision log: jembatan yang memastikan insight tidak hilang

IFRAME menggunakan konsep "decision log" — catatan keputusan terstruktur yang menjadi jembatan antara insight riset dan implementasi. Format sederhana:

```
Keputusan: [apa yang diputuskan]
Konteks: [insight riset yang memotivasi keputusan ini]
Alternatif yang dipertimbangkan: [opsi lain yang dipertimbangkan]
Alasan pemilihan: [mengapa opsi ini dipilih]
Trade-off yang diterima: [apa yang dikorbankan]
Siapa yang memutuskan: [nama/peran]
Tanggal: [kapan]
```

Decision log bukan dokumentasi teknis. Ini adalah narasi keputusan yang memungkinkan siapapun — termasuk tim di masa depan — memahami mengapa sesuatu dibangun dengan cara tertentu.

---

> **Quick Check** — Sebelum melanjutkan:
> *Dari tiga temuan riset di kasus insulin, mana yang termasuk insight mental model, mana kalibrasi kepercayaan, dan mana gangguan alir? Setelah diklasifikasikan, keputusan desain konkret apa yang paling urgent untuk didokumentasikan dalam decision log?*

---

## Analisis Kasus

Mari kita terapkan kerangka empat tipe insight pada kasus insulin secara lengkap dan buat decision log untuk satu keputusan:

**Mengklasifikasikan tiga temuan:**

Temuan 1 (*"Pasien 55+ tidak memahami kapan mengikuti AI vs dokter"*) → **Tipe 1 (mental model)** + **Tipe 2 (trust calibration)**. Keduanya berkaitan: mental model yang salah menghasilkan trust yang tidak terkalibrasi.

Temuan 2 (*"Pasien berpengalaman mengabaikan rekomendasi"*) → **Tipe 2 (trust calibration)** — spesifik: undertrust/algorithm aversion.

Temuan 3 (*"Confidence interval meningkatkan waktu pengambilan keputusan 40%"*) → **Tipe 3 (flow disruption)** — ketegangan antara transparency dan usability.

**Decision log untuk temuan 3:**

```
Keputusan: Menampilkan confidence indicator dengan format
           "tinggi/sedang/rendah" (bukan angka atau interval)
Konteks:   Riset menunjukkan confidence interval numerik
           meningkatkan waktu pengambilan keputusan 40%.
           Tapi menghilangkan confidence indicator sepenuhnya
           melanggar prinsip Transparency (M3-L1).
Alternatif: (a) Tidak tampilkan confidence → melanggar transparency
            (b) Confidence numerik/interval → mempersulit alir
            (c) Confidence kategoris (tinggi/sedang/rendah) → kompromi
Alasan:    Opsi (c) mempertahankan informasi yang actionable
           tanpa menghambat alir keputusan untuk mayoritas pengguna
Trade-off: Pengguna kehilangan presisi numerik. Untuk pengguna
           yang butuh presisi (dokter), tersedia di lapisan lain.
Memutuskan: Lead designer + clinical advisor
Tanggal:   [tanggal keputusan]
```

Dengan decision log ini, ketika tim engineering enam bulan kemudian bertanya "mengapa confidence ditampilkan sebagai tinggi/sedang/rendah dan bukan angka?" — jawabannya terdokumentasi. Ketika regulator bertanya apakah sistem sudah mempertimbangkan transparency — jawabannya ada.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Setelah setiap sesi riset pengguna untuk fitur AI, jadwalkan satu sesi "insight classification" bersama tim: klasifikasikan setiap temuan ke dalam empat tipe, identifikasi keputusan desain yang paling urgent, dan buat decision log untuk setiap keputusan tersebut. Ini tidak membutuhkan lebih dari dua jam — tapi mencegah translation gap yang bisa menghabiskan berminggu-minggu pekerjaan di masa depan.

**Jika kamu UX researcher atau designer:**
Sajikan laporan riset dalam format yang mengklasifikasikan insight berdasarkan tipe dan implikasi keputusannya — bukan hanya temuan dan rekomendasi umum. *"Temuan ini adalah insight mental model yang mengimplikasikan keputusan tentang desain eksplanabilitas di tahap Apply IFRAME"* adalah sajian yang jauh lebih actionable dari *"pengguna perlu pemahaman yang lebih baik tentang AI."*

**Jika kamu developer atau engineer:**
Sebelum mulai implementasi fitur AI, minta decision log dari tim desain dan riset. Jika decision log belum ada, ini adalah sinyal bahwa keputusan penting belum dibuat secara eksplisit — dan implementasi tanpa itu berisiko menghasilkan produk yang tidak bisa dijelaskan atau dipertanggungjawabkan.

---

## Pertanyaan Refleksi

> Kasus insulin menggambarkan situasi yang sangat umum: riset ada, insight ada, tapi tidak ada yang mengubah insight itu menjadi keputusan konkret yang terdokumentasi.
>
> **Pikirkan satu proyek riset pengguna yang kamu ketahui** — di mana temuan yang bagus tidak berhasil mengubah keputusan desain atau implementasi. Dari empat tipe insight, tipe mana yang paling banyak hilang? Dan langkah konkret apa yang bisa mencegah hal yang sama terjadi di proyek berikutnya?

---

## Ringkasan Lesson

- Translation gap — ketika insight riset tidak mengubah keputusan desain — adalah salah satu pemborosan terbesar dalam pengembangan produk AI.
- Empat tipe insight dengan implikasi berbeda: mental model (→ eksplanabilitas), kalibrasi kepercayaan (→ desain interface kepercayaan), gangguan alir (→ trade-off transparency vs usability), fairness persepsi (→ desain inklusif).
- Decision log adalah artefak governance yang menjembatani riset dan implementasi: apa yang diputuskan, mengapa, alternatif apa yang dipertimbangkan, dan trade-off apa yang diterima.
- Tahap Identify dan Flow dalam IFRAME adalah tempat insight riset masuk secara sistematis ke dalam proses desain — bukan sebagai laporan yang dibaca sekali, tapi sebagai basis untuk keputusan yang terdokumentasi.
- Lesson berikutnya: latihan terpandu menerapkan IFRAME secara penuh pada satu skenario desain AI nyata.

---

## Referensi

- CodeinteX. (2026). *IFRAME: A Flow-Centered Decision Orchestration and Evidence Governance Methodology*. codeintex.com/iframe
- Kulesza, T., et al. (2013). Too much, too little, or just right? Ways explanations impact end users' mental models. *2013 IEEE Symposium on Visual Languages and Human-Centric Computing*.
- Amershi, S., et al. (2014). Power to the people: The role of humans in interactive machine learning. *AI Magazine*, 35(4), 105–120.
- Cai, C. J., et al. (2019). Human-centered tools for coping with imperfect algorithms during medical decision-making. *CHI '19 Proceedings*.
- Baxter, K., Courage, C., & Caine, K. (2015). *Understanding Your Users: A Practical Guide to User Research Methods* (2nd ed.). Morgan Kaufmann. — Bab tentang translating research to design.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
