---
title: 'Mengenal SPKO: Data sebagai Fondasi Solusi AI'
course: ai-untuk-proses-data
module: 1
module_title: Fondasi Pemasukan & Validitas Data
lesson: 1
slug: l1-mengenal-spko
unit_kompetensi:
  - kode: J.63OPR00.014.2
    nama: Melakukan Pemasukan Data
  - kode: J.63OPR00.015.2
    nama: Memastikan Validitas Data
level: Foundational — Competency
kategori: Competency
bloom_level: Remember
durasi_menit: 25
durasi_baca_menit: 18
durasi_latihan_menit: 7
bahasa: Indonesia
duration_minutes: 25
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Di akhir lesson ini, kamu akan mampu:
- Menjelaskan mengapa kualitas data yang dimasukkan menjadi fondasi yang menentukan keberhasilan seluruh siklus hidup Solusi AI (AI Solution lifecycle)
- Mengenali hubungan antara enam unit kompetensi yang akan kamu pelajari di kursus ini — dari pemasukan data hingga perawatan Solusi AI
- Mengikuti studi kasus **SPKO (Sistem Penilaian Kredit Otomatis)** milik Bank Nusantara Sejahtera, yang akan jadi lingkungan latihan sepanjang kursus ini

---

## Hook: Ketika Data yang Salah Menunda Akses Kredit Jutaan Orang

Pada 2024, Otoritas Jasa Keuangan (OJK) menerbitkan **POJK Nomor 29/2024** tentang layanan penilaian kredit alternatif berbasis data non-konvensional — sebuah regulasi yang secara eksplisit membuka ruang bagi lembaga jasa keuangan untuk memakai sumber data di luar riwayat kredit formal (seperti data transaksi digital atau pola pembayaran non-bank) untuk menilai kelayakan seseorang menerima kredit.

Sejak regulasi ini terbit, sejumlah lembaga jasa keuangan di Indonesia mulai mengadopsi solusi berbasis kecerdasan buatan untuk penilaian kredit (credit scoring) yang memakai data non-konvensional semacam ini — dengan tujuan meningkatkan akurasi penilaian, memitigasi risiko penipuan (fraud), dan memperluas akses pembiayaan yang aman kepada masyarakat yang selama ini sulit dijangkau sistem kredit konvensional.

Bayangkan implikasinya: sebuah model AI yang dipakai lembaga jasa keuangan untuk memutuskan apakah seseorang layak menerima kredit — **sepenuhnya bergantung pada satu hal yang sering dianggap remeh: data yang dimasukkan ke dalamnya benar, lengkap, dan valid.**

Jika satu digit nomor identitas salah ketik, satu kolom penghasilan kosong padahal wajib diisi, atau satu dokumen fisik salah dipindai — bukan cuma satu baris data yang cacat. Keputusan kredit yang dihasilkan model itu bisa salah, dan bagi orang yang mengajukan, itu berarti akses pembiayaan yang tertunda, ditolak secara keliru, atau — sebaliknya — diberikan kepada pihak yang sebenarnya berisiko tinggi gagal bayar.

**Ini bukan skenario hipotetis.** Ini adalah alasan mengapa OJK, dalam POJK 11/2022 tentang Penyelenggaraan Teknologi Informasi Oleh Bank Umum, secara eksplisit mewajibkan bank menerapkan manajemen risiko atas *"ketergantungan pada data yang tidak akurat"* sebagai bagian dari tata kelola Solusi AI.

Kursus ini akan membawamu menyusuri seluruh siklus hidup sebuah Solusi AI perbankan — dimulai persis dari titik paling mendasar ini: bagaimana data dimasukkan dan dipastikan valid, sebelum ia layak dipakai sebagai fondasi keputusan otomatis apa pun.

---

## Kerangka Konseptual: Enam Unit Kompetensi, Satu Siklus Hidup

Kursus **AI untuk Proses Data** ini menguji enam unit kompetensi yang, jika dilihat satu per satu, tampak seperti daftar tugas terpisah. Tapi jika disusun berurutan, keenamnya membentuk satu siklus hidup (*lifecycle*) Solusi AI yang utuh:

```
[Modul 1] Memasukkan & Memvalidasi Data
        ↓
[Modul 2] Mengintegrasikan Komponen Solusi AI
        ↓
[Modul 3] Memasang (Deploy) Solusi AI
        ↓
[Modul 4] Merencanakan Perawatan
        ↓
[Modul 5] Merawat Solusi AI
        ↓
[Modul 6] Audit Menyeluruh Siklus Hidup
```

<!-- VISUAL PLACEHOLDER: Diagram siklus hidup melingkar (bukan linear) menunjukkan 6 tahap di atas, dengan ikon berbeda tiap tahap, dan panah kembali dari "Merawat" ke "Memasukkan & Memvalidasi Data" untuk menunjukkan bahwa data baru terus mengalir masuk selama solusi beroperasi -->

Setiap kompetensi ini punya nama resminya masing-masing di SKKNI (Standar Kompetensi Kerja Nasional Indonesia), yang akan kamu temui sepanjang kursus:

| Modul | Unit Kompetensi | Kode |
|---|---|---|
| 1 | Melakukan Pemasukan Data | J.63OPR00.014.2 |
| 1 | Memastikan Validitas Data | J.63OPR00.015.2 |
| 2 | Mengintegrasikan Komponen Solusi AI | J.62AIN00.014.1 |
| 3 | Memasang Solusi AI | J.62AIN00.015.1 |
| 4 | Merencanakan Perawatan Solusi AI | J.62AIN00.016.1 |
| 5 | Merawat Solusi AI | J.62AIN00.017.1 |

Mengapa urutan ini penting, bukan sekadar administratif? Karena secara teknis, setiap tahap **membutuhkan** output dari tahap sebelumnya. Kamu tidak bisa merencanakan perawatan (Modul 4) tanpa hasil monitoring dari solusi yang sudah dipasang (Modul 3). Kamu tidak bisa memasang solusi (Modul 3) tanpa komponennya sudah terintegrasi (Modul 2). Dan semuanya, pada akhirnya, berpijak pada data yang masuk di Modul 1.

Inilah mengapa kualitas data (*data quality*) bukan cuma topik pembuka yang sopan-sopan sebelum masuk ke hal yang "lebih teknis" seperti integrasi AI. Ia adalah fondasi literal — kalau retak di sini, retaknya menjalar ke seluruh siklus.

---

## Mengenal Lingkungan Latihan: SPKO milik Bank Nusantara Sejahtera

Sepanjang kursus ini, kamu akan berlatih menggunakan satu studi kasus yang konsisten: **Bank Nusantara Sejahtera**, sebuah bank fiktif yang sedang mengoperasikan **Sistem Penilaian Kredit Otomatis (SPKO)** — solusi AI *credit scoring* untuk mempercepat proses persetujuan kredit nasabah.

> **Catatan penting:** Bank Nusantara Sejahtera dan SPKO adalah **studi kasus fiktif**, dirancang khusus sebagai lingkungan latihan. Ini disengaja — data nasabah bank sungguhan tidak boleh dipakai untuk materi pelatihan publik, karena termasuk data pribadi yang dilindungi Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi. Namun, setiap tantangan teknis yang akan kamu hadapi di SPKO — dari data yang tidak lengkap, sistem yang perlu diintegrasikan, hingga model yang performanya menurun — mencerminkan pola nyata yang terjadi di industri, seperti tren adopsi AI berbasis data non-konvensional yang didorong POJK 29/2024.

Di Modul 1 (lesson berikutnya), kamu akan mulai dari titik paling dasar: memasukkan dan memvalidasi data pengajuan kredit nasabah SPKO — persis tahap yang, jika salah, bisa menunda atau menyalahi keputusan kredit seseorang.

---

## Quick Check

**Mengapa kualitas data pemasukan dianggap sebagai fondasi, bukan sekadar langkah administratif awal, dalam siklus hidup Solusi AI perbankan? Jawab dalam 2-3 kalimat.**

<details>
<summary>Lihat jawaban</summary>

Karena setiap tahap berikutnya dalam siklus hidup Solusi AI — integrasi, deployment, perencanaan perawatan, hingga perawatan — bekerja di atas asumsi bahwa data yang masuk ke sistem sudah benar dan valid. Kesalahan di tahap pemasukan data tidak berhenti di situ; ia menjalar menjadi keputusan model yang salah (seperti penilaian kredit yang keliru), yang berdampak langsung pada orang yang mengajukan kredit. Regulator seperti OJK bahkan secara eksplisit mewajibkan bank mengelola risiko ini (POJK 11/2022) karena dampaknya bersifat sistemik, bukan sekadar teknis.
</details>

---

## Analisis Kasus: Kembali ke POJK 29/2024

Perhatikan kembali semangat di balik POJK 29/2024: membuka ruang bagi penilaian kredit menggunakan **data non-konvensional** — yaitu sumber data yang lebih beragam dan kompleks dibanding data kredit tradisional.

Semakin beragam sumber data yang dipakai sebuah model AI, semakin besar pula risiko terjadinya kesalahan pemasukan atau inkonsistensi data — karena data itu datang dari lebih banyak sistem, format, dan proses input yang berbeda-beda. Ini justru memperkuat alasan mengapa POJK 29/2024 (yang membuka pintu bagi data non-konvensional) berjalan beriringan dengan POJK 11/2022 (yang mewajibkan manajemen risiko atas keakuratan data) — regulator memahami bahwa membuka akses ke lebih banyak data harus dibarengi dengan disiplin yang lebih ketat dalam memastikan data itu valid sebelum dipakai.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Keputusan untuk mengadopsi sumber data baru (seperti data non-konvensional yang dibuka POJK 29/2024) tidak boleh dipisahkan dari investasi pada proses validasi data. Menambah sumber data tanpa memperkuat kontrol kualitas data hanya memindahkan risiko dari "kekurangan data" menjadi "data yang tidak terpercaya."

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Antarmuka pemasukan data (seperti formulir input SPKO) harus dirancang untuk mencegah kesalahan sedini mungkin — validasi format secara real-time, penanda field wajib yang jelas — karena mendeteksi kesalahan setelah data masuk ke sistem jauh lebih mahal daripada mencegahnya saat dimasukkan.

**Bagi pengembang/petugas teknis (developer/engineer):**
Proses import data dari sumber elektronis (seperti file CSV dari sistem core banking) memerlukan validasi otomatis pada level sistem — bukan hanya mengandalkan ketelitian manusia yang memasukkan data satu per satu.

---

## Pertanyaan Refleksi

1. Di tempat kerjamu, pada tahap mana data biasanya mulai "retak" — saat dimasukkan manual, saat diimpor dari sistem lain, atau saat divalidasi? Mengapa menurutmu begitu?
2. Kalau kamu jadi petugas yang menemukan data pengajuan kredit dengan field penghasilan kosong padahal wajib diisi, langkah apa yang akan kamu ambil sebelum data itu diproses lebih lanjut oleh SPKO?

---

## Ringkasan Lesson

- Kualitas data pemasukan (*data entry quality*) adalah fondasi yang menentukan keberhasilan seluruh siklus hidup Solusi AI, bukan sekadar langkah administratif di awal.
- Terbitnya POJK 29/2024 tentang penilaian kredit alternatif berbasis data non-konvensional menunjukkan bagaimana industri jasa keuangan Indonesia secara aktif bergerak ke arah AI berbasis data yang lebih beragam — sekaligus menghadapi tuntutan regulasi (POJK 11/2022) untuk menjaga keakuratan data tersebut.
- Kursus ini akan menuntunmu melalui enam unit kompetensi yang membentuk satu siklus hidup Solusi AI: pemasukan & validitas data → integrasi → deployment → perencanaan perawatan → perawatan → audit menyeluruh.
- Sepanjang kursus, kamu akan berlatih menggunakan studi kasus fiktif Bank Nusantara Sejahtera dan SPKO — dirancang aman secara hukum namun mencerminkan tantangan nyata di industri.

---

## Referensi

- Peraturan Otoritas Jasa Keuangan Nomor 11/POJK.03/2022 tentang Penyelenggaraan Teknologi Informasi Oleh Bank Umum.
- Peraturan Otoritas Jasa Keuangan Nomor 29/2024 tentang Layanan Penilaian Kredit Alternatif Berbasis Data Non-Konvensional.
- Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi.

---

## Lanjut ke Lesson Berikutnya

**[M1-L2: Mempersiapkan & Memasukkan Data Nasabah →](l2-mempersiapkan-memasukkan-data)**

Kamu akan mulai berlatih langsung: mempersiapkan dan memasukkan data pengajuan kredit nasabah SPKO, termasuk menangani dokumen fisik dan memastikan kelengkapan field data sesuai borang.
