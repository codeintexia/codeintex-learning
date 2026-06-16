---
course: hcai-foundations
module: 4
module_title: "Explainability and Fairness in Practice"
lesson: 2
title: "Siapa Butuh Penjelasan Apa: Menganalisis Kebutuhan Eksplanabilitas per Pemangku Kepentingan"
duration_minutes: 12
bloom_level: analyze
keywords:
  - XAI stakeholders
  - explainability for regulators
  - AI explanation types
  - explanation fidelity accessibility tradeoff
  - user explanation needs AI
is_free: true
status: draft
---

# Siapa Butuh Penjelasan Apa: Menganalisis Kebutuhan Eksplanabilitas per Pemangku Kepentingan

**Modul 4 · Explainability and Fairness in Practice** · Lesson 2 dari 4
**Estimasi waktu baca:** 12 menit · **Level:** Foundational · **Prasyarat:** M4-L1

---

> **Yang akan kamu capai di lesson ini:**
> - Menganalisis bagaimana kebutuhan penjelasan berbeda secara fundamental antara pengguna, pengembang, dan regulator
> - Membandingkan trade-off antara keakuratan penjelasan teknis dan aksesibilitas penjelasan untuk non-teknis
> - Mengidentifikasi kesalahan desain yang paling umum ketika tim membangun satu jenis penjelasan untuk semua audiens

---

## Hook

2022. Sebuah bank di Eropa menerima surat dari regulator: sistem AI kredit mereka harus memberikan penjelasan yang memadai kepada nasabah yang ditolak pinjamannya — sesuai kewajiban GDPR Pasal 22.

Tim engineering merespons dengan solusi yang menurut mereka sempurna: mereka menambahkan output SHAP ke setiap keputusan penolakan. Nasabah sekarang menerima email berisi tabel dengan 12 fitur dan nilai kontribusi masing-masing dalam skala -1.0 hingga +1.0.

Regulator menolak solusi itu.

Tim legal bank bingung. Penjelasan teknis sudah ada — akurat, dapat diaudit, dihasilkan oleh teknik yang diakui secara ilmiah. Mengapa tidak cukup?

Jawabannya datang dari wawancara dengan 15 nasabah yang menerima email itu: **tidak satu pun dari mereka memahami apa yang tertulis.** Mereka tahu ditolak. Mereka tidak tahu mengapa dengan cara yang bisa mereka tindaklanjuti. Dan mereka tidak tahu apa yang harus dilakukan selanjutnya.

Penjelasan yang akurat secara teknis adalah hal yang berbeda dari penjelasan yang berguna bagi manusia yang membacanya.

---

## Kerangka Konseptual

### Tiga audiens, tiga kebutuhan yang berbeda fundamental

Kesalahan paling umum dalam desain eksplanabilitas adalah mengasumsikan bahwa satu jenis penjelasan cukup untuk semua orang. Ini tidak benar — dan bukan hanya soal tingkat kesederhanaan bahasa. Ini soal **apa yang ingin dilakukan seseorang dengan penjelasan itu.**

**Audiens 1 — Pengguna yang terdampak:**
Pertanyaan yang ingin mereka jawab: *"Mengapa ini terjadi pada saya, dan apa yang bisa saya lakukan?"*

Pengguna tidak membutuhkan penjelasan tentang cara model bekerja. Mereka membutuhkan penjelasan yang:
- menggunakan bahasa yang mereka pahami dalam konteks kehidupan mereka
- mengidentifikasi faktor yang relevan dengan situasi mereka secara spesifik
- menunjukkan jalan ke depan — apa yang bisa berubah, apa yang bisa mereka lakukan

Penjelasan terbaik untuk pengguna sering bukan penjelasan yang paling akurat secara teknis — melainkan penjelasan kontrafaktual sederhana: *"Pengajuan Anda ditolak terutama karena riwayat pembayaran tiga tahun terakhir. Jika tidak ada tunggakan dalam 12 bulan ke depan, peluang persetujuan meningkat signifikan."*

**Audiens 2 — Pengembang dan tim internal:**
Pertanyaan yang ingin mereka jawab: *"Bagaimana model ini berperilaku, di mana ia lemah, dan apa yang perlu diperbaiki?"*

Pengembang membutuhkan penjelasan yang:
- akurat secara teknis dan bisa direproduksi
- menunjukkan pola perilaku di seluruh dataset, bukan hanya satu kasus
- bisa digunakan untuk debugging, perbaikan, dan validasi

Untuk audiens ini, output SHAP atau LIME yang detail justru berguna. Mereka bisa membaca tabel nilai kontribusi dan menggunakannya untuk mengidentifikasi bias atau anomali.

**Audiens 3 — Regulator dan auditor eksternal:**
Pertanyaan yang ingin mereka jawab: *"Apakah sistem ini dapat diaudit, dan apakah ia beroperasi sesuai standar yang ditetapkan?"*

Regulator membutuhkan penjelasan yang:
- dapat diverifikasi secara independen
- konsisten dan dapat direproduksi
- menunjukkan bahwa proses pengambilan keputusan tidak diskriminatif
- disertai dokumentasi tentang bagaimana sistem divalidasi dan dimonitor

Ini bukan penjelasan per keputusan — ini adalah penjelasan tentang sistem secara keseluruhan: bagaimana model dilatih, divalidasi, dimonitor, dan bagaimana bias ditangani.

### Trade-off antara keakuratan dan aksesibilitas

Ini adalah salah satu trade-off paling penting dalam desain eksplanabilitas, dan ia sering tidak diakui secara eksplisit:

**Keakuratan (fidelity):** Seberapa tepat penjelasan mencerminkan apa yang sebenarnya terjadi di dalam model. Penjelasan yang sangat akurat sering kompleks secara matematis.

**Aksesibilitas:** Seberapa mudah penjelasan dipahami oleh audiens target. Penjelasan yang sangat aksesibel sering menyederhanakan atau bahkan mendistorsi realitas teknis.

Tidak ada solusi yang memaksimalkan keduanya sekaligus untuk semua audiens. Yang bisa dilakukan adalah:

1. Membuat keputusan eksplisit tentang *untuk siapa* sebuah penjelasan dirancang
2. Menerima trade-off yang menyertainya secara sadar
3. Menyediakan beberapa lapisan penjelasan untuk audiens yang berbeda — bukan satu penjelasan untuk semua

### Lapisan penjelasan: satu sistem, banyak antarmuka

Solusi paling efektif untuk masalah "satu penjelasan untuk semua" adalah membangun arsitektur penjelasan berlapis:

- **Lapisan pengguna:** penjelasan kontrafaktual sederhana dalam bahasa natural, fokus pada tindakan yang bisa diambil
- **Lapisan internal:** penjelasan teknis lengkap untuk tim pengembang dan analis
- **Lapisan audit:** dokumentasi sistem yang dapat diverifikasi untuk regulator dan auditor

Ketiga lapisan mengacu pada keputusan yang sama — tapi menerjemahkannya dengan cara yang berbeda untuk audiens yang berbeda.

<!-- DIAGRAM: Arsitektur Tiga Lapisan Penjelasan AI
     Render sebagai diagram vertikal tiga tingkat saat membangun UI.
     Atas: Lapisan Audit — dokumentasi sistem untuk regulator
           Label: "Dapat diverifikasi secara independen"
           Contoh output: laporan validasi, dokumentasi bias testing, audit trail
     Tengah: Lapisan Internal — output teknis untuk pengembang
             Label: "Akurat secara teknis, dapat direproduksi"
             Contoh output: SHAP values, feature importance, model cards
     Bawah: Lapisan Pengguna — penjelasan untuk user yang terdampak
            Label: "Dapat ditindaklanjuti, bahasa natural"
            Contoh output: "Ditolak karena X. Untuk disetujui, pertimbangkan Y."
     Tunjukkan dengan panah: ketiga lapisan merujuk pada keputusan yang sama
     Warna: tiap lapisan berbeda (biru, teal, hijau dari atas ke bawah)
-->

---

> **Quick Check** — Sebelum melanjutkan:
> *Kembali ke kasus bank di hook. Tim engineering memberikan output SHAP — itu adalah lapisan penjelasan untuk audiens mana? Apa yang seharusnya mereka bangun untuk memenuhi kebutuhan nasabah dan regulator sekaligus?*

---

## Analisis Kasus

Mari kita dekonstruksi kegagalan bank di hook menggunakan kerangka tiga audiens:

**Untuk pengguna:** Tim membangun lapisan teknis (SHAP output) tapi tidak membangun lapisan pengguna. Nasabah menerima data yang akurat tapi tidak bisa digunakan. Yang dibutuhkan: *"Pengajuan Anda ditolak terutama karena rasio utang-penghasilan melebihi batas kami. Untuk pengajuan berikutnya, pertimbangkan untuk melunasi kredit X terlebih dahulu."*

**Untuk pengembang:** Output SHAP adalah tepat untuk audiens ini. Tim sudah memiliki alat debugging yang mereka butuhkan.

**Untuk regulator:** Regulator tidak hanya butuh penjelasan per keputusan — mereka butuh bukti bahwa sistem secara keseluruhan tidak diskriminatif, bisa dimonitor, dan ada mekanisme banding yang efektif. Ini adalah dokumentasi sistem, bukan output model.

Bank gagal bukan karena tidak memiliki teknologi yang tepat. Mereka gagal karena mengira satu solusi teknis bisa melayani tiga audiens yang berbeda secara fundamental.

Ingat dari M2-L2: mental model yang salah — dalam hal ini asumsi bahwa "penjelasan teknis yang akurat = penjelasan yang berguna" — adalah sumber kegagalan desain yang paling umum.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Ketika merencanakan fitur eksplanabilitas, buat matriks tiga kolom: pengguna, tim internal, regulator. Untuk setiap kolom, jawab: pertanyaan apa yang ingin mereka jawab, dan penjelasan seperti apa yang bisa mereka gunakan? Jika jawabannya sama untuk semua kolom, kamu mungkin belum cukup dalam berpikir tentang audiens yang berbeda.

**Jika kamu UX researcher atau designer:**
Lakukan riset pengguna spesifik tentang eksplanabilitas — bukan hanya tentang usability secara umum. Tanyakan: *"Setelah menerima keputusan ini, apa pertanyaan pertama yang muncul di benak Anda?"* Jawaban mereka akan menunjukkan jenis penjelasan yang benar-benar dibutuhkan — yang sering sangat berbeda dari apa yang diasumsikan tim teknis.

**Jika kamu developer atau engineer:**
Pertimbangkan eksplanabilitas sebagai tiga sistem terpisah yang perlu dibangun: explanation engine untuk pengguna, analytic tools untuk tim internal, dan audit documentation untuk regulator. Ketiga sistem menggunakan data yang sama tapi mempresentasikannya dengan cara yang berbeda. Ini bukan duplikasi — ini adalah layanan yang berbeda untuk kebutuhan yang berbeda.

---

## Pertanyaan Refleksi

> Kasus bank menunjukkan bahwa membangun penjelasan yang akurat secara teknis belum cukup — penjelasan harus berguna untuk audiens spesifik yang menerimanya.
>
> **Pikirkan produk AI yang kamu analisis di M3-L5.** Untuk tiga audiens — pengguna yang terdampak, tim internal, dan regulator/pengawas — penjelasan jenis apa yang saat ini tersedia? Lapisan mana yang paling lemah, dan apa konsekuensinya jika lapisan itu terus absen?

---

## Ringkasan Lesson

- Tiga audiens memiliki kebutuhan penjelasan yang berbeda fundamental: pengguna butuh penjelasan yang bisa ditindaklanjuti, pengembang butuh penjelasan yang bisa digunakan untuk debugging, regulator butuh penjelasan yang bisa diverifikasi.
- Trade-off antara keakuratan teknis dan aksesibilitas tidak bisa dihindari — solusinya adalah membangun lapisan penjelasan yang berbeda untuk audiens yang berbeda, bukan mencari satu penjelasan yang optimal untuk semua.
- Kegagalan paling umum: membangun lapisan teknis yang akurat dan mengasumsikan itu cukup untuk semua audiens.
- Lesson berikutnya beralih ke dimensi fairness: dari mana bias AI datang, dan bagaimana mendeteksinya sebelum ia menjadi masalah yang mahal.

---

## Referensi

- Wachter, S., Mittelstadt, B., & Russell, C. (2017). Counterfactual explanations without opening the black box. *Harvard Journal of Law & Technology*, 31(2).
- Adadi, A., & Berrada, M. (2018). Peeking inside the black box: A survey on explainable artificial intelligence. *IEEE Access*, 6, 52138–52160.
- European Parliament. (2024). *Regulation (EU) 2024/1689 — Artificial Intelligence Act*. — Pasal 13 tentang transparency dan Pasal 86 tentang hak penjelasan.
- Langer, M., et al. (2021). What do we want from explainable artificial intelligence (XAI)? *Information Fusion*, 78, 268–280.
- Regulation (EU) 2016/679 (GDPR). Article 22: Automated individual decision-making, including profiling.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
