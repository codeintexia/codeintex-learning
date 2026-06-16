---
course: hcai-foundations
module: 5
module_title: "Designing Human-Centered AI with IFRAME"
lesson: 1
title: "Mengapa Proses Desain Konvensional Tidak Cukup untuk Produk AI"
duration_minutes: 12
bloom_level: apply
keywords:
  - AI product design process
  - human-centered design for AI
  - HCAI design methodology
  - design thinking limitations AI
  - AI-specific design challenges
is_free: true
status: draft
---

# Mengapa Proses Desain Konvensional Tidak Cukup untuk Produk AI

**Modul 5 · Designing Human-Centered AI with IFRAME** · Lesson 1 dari 4
**Estimasi waktu baca:** 12 menit · **Level:** Foundational · **Prasyarat:** M1-L1 s/d M4-L4

---

> **Yang akan kamu capai di lesson ini:**
> - Menerapkan pemahaman tentang empat prinsip HCAI untuk mengidentifikasi celah dalam proses desain konvensional
> - Menggunakan kerangka "empat tantangan unik AI" untuk mengevaluasi kecukupan proses desain yang ada
> - Membangun argumen mengapa produk AI membutuhkan lapisan governance di atas — bukan sebagai pengganti — metode desain yang sudah ada

---

## Hook

2021. Zillow, marketplace properti terbesar di Amerika Serikat, meluncurkan program ambisius: menggunakan model AI untuk membeli dan menjual rumah secara otomatis — *iBuying*. Sistem mereka, Zestimate, sudah digunakan jutaan orang selama lebih dari satu dekade untuk memperkirakan nilai properti.

Tim produk Zillow adalah tim kelas dunia. Mereka menggunakan proses desain yang matang. Riset pengguna mereka ekstensif. UX interface mereka diakui sebagai salah satu terbaik di industri.

Tapi dalam 18 bulan, program iBuying menghasilkan kerugian lebih dari $300 juta. Zillow terpaksa menutup program itu sepenuhnya dan memecat 25% karyawan mereka.

Apa yang salah bukan desain interfacenya — itu bekerja dengan baik. Yang salah adalah sesuatu yang jauh lebih fundamental: **proses desain yang ada tidak pernah dibangun untuk menjawab pertanyaan-pertanyaan spesifik yang hanya muncul ketika AI membuat keputusan konsekuensial.**

Model Zestimate sangat akurat dalam kondisi pasar normal. Tapi tidak ada yang pernah secara sistematis bertanya: *"Apa yang terjadi ketika kondisi pasar berubah drastis? Siapa yang bertanggung jawab ketika model salah? Bagaimana kita memastikan bahwa keputusan pembelian otomatis tidak mengekspos perusahaan pada risiko yang tidak terlihat dalam metrik model?"*

Pertanyaan-pertanyaan itu bukan pertanyaan UX. Bukan pertanyaan riset pengguna. Bukan pertanyaan teknis. Mereka adalah pertanyaan tentang governance keputusan — dan proses desain konvensional tidak pernah dirancang untuk menjawabnya.

---

## Kerangka Konseptual

### Apa yang dilakukan proses desain konvensional dengan sangat baik

Penting untuk mulai dengan pengakuan yang jujur: Design Thinking, Double Diamond, Lean UX, dan metodologi desain lainnya adalah framework yang powerful. Mereka unggul dalam:

- memahami kebutuhan pengguna melalui riset kualitatif dan kuantitatif
- mendefinisikan masalah dengan cara yang bisa diselesaikan
- menghasilkan dan menguji solusi secara iteratif
- mengoptimalkan antarmuka untuk usability dan pengalaman

Tidak ada dari ini yang salah. Dan tidak ada dari ini yang perlu digantikan.

Masalahnya adalah produk AI memiliki empat karakteristik yang tidak ditangani oleh proses-proses ini — bukan karena metodologinya buruk, melainkan karena mereka dikembangkan untuk dunia sebelum AI menjadi komponen kritis dalam produk.

<!-- DIAGRAM: Proses Desain Konvensional vs Tantangan Unik Produk AI
     Render sebagai tabel dua kolom saat membangun UI.
     Kolom kiri (hijau): "Yang dilakukan proses konvensional dengan baik"
       - Memahami kebutuhan pengguna
       - Mendefinisikan masalah
       - Menghasilkan & menguji solusi secara iteratif
       - Mengoptimalkan antarmuka
     Kolom kanan (oranye): "Yang tidak ditangani untuk produk AI"
       - Perilaku non-deterministik
       - Ketidakpastian kapabilitas
       - Ketergantungan pada data
       - Celah eksplanabilitas
     Footer: "IFRAME mengisi gap ini — bukan menggantikan kolom kiri"
-->

### Empat tantangan unik produk AI yang tidak ditangani proses konvensional

**Tantangan 1 — Perilaku non-deterministik:**
Produk non-AI berperilaku konsisten: input yang sama selalu menghasilkan output yang sama. Produk AI tidak selalu demikian — model bisa menghasilkan output berbeda untuk input yang identik, berperilaku berbeda pada kasus tepi (*edge case*), dan "berubah perilaku" ketika data pelatihan diperbarui.

Proses desain konvensional mengasumsikan produk yang bisa diuji secara eksak: "jika pengguna mengklik tombol ini, ini yang terjadi." Untuk produk AI, pertanyaannya adalah: "jika pengguna mengklik tombol ini, rentang output apa yang mungkin terjadi — dan bagaimana antarmuka mengomunikasikan ketidakpastian itu?" Ini langsung terhubung ke apa yang dipelajari di M2 — mental model yang salah tentang kapabilitas AI paling sering terbentuk justru ketika perilaku sistem tidak konsisten seperti yang diharapkan pengguna.

**Tantangan 2 — Ketidakpastian kapabilitas:**
Dalam pengembangan produk konvensional, tim desain bisa mendefinisikan dengan tepat apa yang bisa dilakukan produk sebelum memulai desain. Dalam pengembangan produk AI, kapabilitas model seringkali hanya bisa diketahui setelah data dikumpulkan, model dilatih, dan evaluasi dilakukan.

Ini menciptakan situasi di mana desainer sering merancang untuk kapabilitas yang diasumsikan — yang bisa sangat berbeda dari kapabilitas yang sebenarnya ketika model selesai dibangun.

**Tantangan 3 — Ketergantungan pada data:**
Produk AI adalah produk yang berubah seiring data yang mengalirinya. Model yang dilatih hari ini akan berperilaku berbeda dari model yang dilatih enam bulan lagi — bahkan tanpa perubahan kode. Desain yang bekerja baik untuk distribusi data saat ini mungkin gagal untuk distribusi data masa depan.

Proses desain konvensional tidak memiliki mekanisme untuk menjawab pertanyaan: "bagaimana desain ini harus berevolusi seiring data dan model berubah?"

**Tantangan 4 — Celah eksplanabilitas:**
Seperti yang kita pelajari di M4, pengguna produk AI sering tidak bisa memahami mengapa sistem berperilaku seperti yang ia lakukan. Proses desain konvensional mengoptimalkan untuk *apa* yang terjadi dalam antarmuka — bukan untuk *mengapa* keputusan sistem dibuat dengan cara tertentu. Ini adalah celah Transparency (M3-L1) yang terinstitusionalisasi dalam proses desain — bukan karena tim tidak peduli, melainkan karena tidak ada mekanisme dalam proses yang memaksanya menjadi prioritas.

### Apa yang dibutuhkan: lapisan governance (*governance layer*), bukan metode baru

Kesimpulan dari keempat tantangan ini bukan bahwa tim harus membuang Design Thinking dan menggantinya dengan sesuatu yang lain. Kesimpulannya adalah: **tim membutuhkan lapisan governance yang berjalan di atas metode yang sudah ada** — lapisan yang memastikan keputusan eksplisit, trade-off terlihat, bukti terdokumentasi, dan outcomes dapat ditelusuri.

Ini persis posisi yang dijelaskan dalam dokumentasi IFRAME di codeintex.com: IFRAME bukan metode desain, ia adalah metodologi untuk mengorkestrasikan keputusan dan mengelola bukti di sepanjang siklus hidup produk — kompatibel dengan semua metode yang ada, bukan pengganti untuk satupun dari mereka.

---

> **Quick Check** — Sebelum melanjutkan:
> *Dari empat tantangan — non-deterministik, ketidakpastian kapabilitas, ketergantungan data, celah eksplanabilitas — mana yang paling relevan untuk produk atau fitur AI yang kamu kenal? Dan metode desain apa yang saat ini digunakan — apakah ada mekanisme di dalamnya yang secara eksplisit menjawab tantangan itu?*

---

## Analisis Kasus

Kembali ke Zillow. Dengan kerangka empat tantangan:

**Perilaku non-deterministik:** Model Zestimate akurat secara rata-rata, tapi perilakunya di pasar yang sangat volatile — seperti yang terjadi selama pandemi — berbeda secara dramatis. Tidak ada yang merancang antarmuka atau proses keputusan untuk kondisi ini.

**Ketidakpastian kapabilitas:** Tim produk menggunakan Zestimate yang dibangun untuk *estimasi nilai* sebagai dasar untuk *pembelian otomatis* — dua use case yang memiliki toleransi kesalahan yang sangat berbeda. Kapabilitas yang cukup untuk satu use case tidak cukup untuk use case lain, tapi perbedaan ini tidak pernah menjadi keputusan eksplisit yang terdokumentasi.

**Ketergantungan data:** Distribusi data properti selama pandemi sangat berbeda dari data historis yang melatih model. Tidak ada mekanisme governance yang mewajibkan re-evaluasi sebelum operasi dilanjutkan dalam kondisi distribusi yang berubah drastis.

**Celah eksplanabilitas:** Ketika model mulai overpaying untuk properti, tidak ada cara untuk memahami *mengapa* — faktor apa yang menyebabkan estimasi meleset. Ini membuat koreksi menjadi sangat lambat.

Zillow memiliki tim desain kelas dunia, proses yang matang, dan data yang sangat banyak. Yang tidak mereka miliki adalah lapisan governance yang menjawab pertanyaan-pertanyaan AI-specific ini secara sistematis sebelum mereka menjadi kerugian $300 juta.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Sebelum memulai sprint desain berikutnya untuk fitur AI, tanyakan kepada tim: *"Dari empat tantangan unik AI, mana yang paling relevan untuk fitur ini? Dan proses kita saat ini, apakah ada langkah yang secara eksplisit menjawab tantangan itu?"* Jika tidak ada, itulah gap yang perlu ditutup — tidak dengan mengganti metodologi, tapi dengan menambahkan governance layer di atasnya.

**Jika kamu UX researcher atau designer:**
Peran UX researcher untuk produk AI perlu diperluas melampaui usability testing dan pemahaman kebutuhan pengguna. Pertanyaan tentang kapan pengguna harus percaya sistem, bagaimana sistem mengomunikasikan ketidakpastian, dan bagaimana antarmuka berevolusi saat model berubah — semua ini adalah pertanyaan UX yang belum banyak dibahas dalam kurikulum desain standar.

**Jika kamu developer atau engineer:**
Empat tantangan ini bukan hanya masalah desain — mereka membutuhkan keputusan teknis yang spesifik: bagaimana sistem mengomunikasikan confidence level, bagaimana sistem dimonitor setelah distribusi data berubah, dan bagaimana setiap keputusan model meninggalkan jejak yang bisa diperiksa. Keputusan-keputusan ini harus dibuat sebelum implementasi, bukan setelahnya.

---

## Pertanyaan Refleksi

> Zillow menghabiskan ratusan juta dolar dan memecat ribuan karyawan karena proses yang ada tidak memiliki mekanisme untuk menjawab pertanyaan-pertanyaan governance AI.
>
> **Pikirkan satu produk atau fitur AI yang sedang atau pernah kamu kerjakan.** Dari empat tantangan di atas, mana yang paling tidak tertangani dalam proses yang digunakan saat itu? Dan apa konsekuensinya — atau konsekuensi potensialnya jika dibiarkan?

---

## Ringkasan Lesson

- Proses desain konvensional kuat dalam memahami pengguna, mendefinisikan masalah, dan mengoptimalkan antarmuka — tapi tidak dibangun untuk menjawab tantangan unik produk AI.
- Empat tantangan unik: perilaku non-deterministik, ketidakpastian kapabilitas, ketergantungan data, dan celah eksplanabilitas.
- Solusinya bukan mengganti metodologi yang ada, melainkan menambahkan lapisan governance yang berjalan di atasnya — memastikan keputusan eksplisit, trade-off terlihat, dan outcomes dapat ditelusuri.
- Lesson berikutnya memperkenalkan IFRAME sebagai metodologi governance layer tersebut — dan bagaimana enam tahapnya secara langsung menjawab keempat tantangan ini.

---

## Referensi

- Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press. — Bab 11–12.
- Cai, C. J., et al. (2019). Human-centered tools for coping with imperfect algorithms during medical decision-making. *CHI '19 Proceedings*.
- Amershi, S., et al. (2019). Software engineering for machine learning: A case study. *2019 IEEE/ACM 41st ICSE*, 291–300.
- Zillow. (2021). *Zillow Group Reports Third Quarter 2021 Financial Results*. Zillow Group Investor Relations. — Q3 2021 earnings report disclosing iBuying wind-down.
- Yang, Q., et al. (2020). Re-examining whether, why, and how human-AI interaction is uniquely difficult to design. *CHI '20 Proceedings*.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
