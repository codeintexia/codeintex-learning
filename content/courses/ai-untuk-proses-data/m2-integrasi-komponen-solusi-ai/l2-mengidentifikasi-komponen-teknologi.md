---
title: Mengidentifikasi Komponen & Teknologi Integrasi
course: ai-untuk-proses-data
module: 2
module_title: Integrasi Komponen Solusi AI
lesson: 2
slug: l2-mengidentifikasi-komponen-teknologi
unit_kompetensi:
  - kode: J.62AIN00.014.1
    nama: Mengintegrasikan Komponen Solusi AI
    elemen: 'Elemen 1: Mengidentifikasi komponen solusi yang akan diintegrasikan'
level: Foundational — Competency
kategori: Competency
bloom_level: Apply
durasi_menit: 30
durasi_baca_menit: 16
durasi_latihan_menit: 14
bahasa: Indonesia
duration_minutes: 30
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Di akhir lesson ini, kamu akan mampu:
- Mengidentifikasi komponen Solusi AI yang akan diintegrasikan berdasarkan arsitektur teknis dan dokumentasi proyek
- Memilih teknologi integrasi sesuai kebutuhan komunikasi antarmodul
- Menyesuaikan format pertukaran data dengan kebutuhan integrasi sistem

---

## Hook: Ketika Setiap Bank Bicara "Bahasa" API yang Berbeda

Sebelum 2021, integrasi antara bank dan penyelenggara fintech di Indonesia menghadapi masalah yang sangat mendasar: **tidak ada standar bersama**. Setiap bank membangun API dengan protokol komunikasi sendiri, format data sendiri, dan metode autentikasi sendiri. Akibatnya, setiap kali sebuah fintech ingin terhubung dengan bank baru, mereka harus membangun ulang integrasi dari nol — bahkan meski secara konsep yang dilakukan sama persis (mengecek saldo, memverifikasi transaksi).

Bank Indonesia akhirnya menetapkan **SNAP (Standar Nasional Open API Pembayaran)** melalui Surat Keputusan Gubernur BI No.23/10/KEP.GBI/2021 — sebuah standar yang mengatur protokol komunikasi, format data request dan response, metode autentikasi, hingga metode enkripsi yang harus dipakai seragam oleh seluruh pelaku industri pembayaran. Tujuannya jelas: mengakhiri era di mana setiap institusi "berbicara bahasa API yang berbeda", sehingga integrasi bisa dilakukan lebih cepat, aman, dan konsisten.

Kenapa standar seperti ini perlu regulasi setingkat Bank Indonesia? Karena masalah yang coba diselesaikannya sangat nyata: **kesalahan memilih teknologi integrasi atau format pertukaran data bukan cuma soal preferensi teknis** — ia bisa berujung pada kegagalan sistem, ketidaksesuaian data antarplatform, bahkan celah keamanan yang berdampak langsung pada nasabah.

Ini persis inti dari Elemen 1 yang akan kamu pelajari: mengidentifikasi komponen apa yang perlu diintegrasikan, dan memilih teknologi serta format yang tepat — bukan sekadar teknologi yang "familiar" atau "kebetulan sudah dipakai di proyek lain".

---

## Kerangka Konseptual: Elemen 1 — Mengidentifikasi Komponen yang Akan Diintegrasikan

**1.1 — Komponen Solusi AI yang akan diintegrasikan diidentifikasi berdasarkan arsitektur teknis dan dokumentasi proyek**

Sebelum integrasi dimulai, kamu harus tahu persis komponen apa saja yang perlu saling terhubung. Ini bukan asumsi — harus merujuk ke dokumentasi arsitektur proyek yang sudah disepakati (seperti konsep yang kamu pelajari di L1: monolitik vs mikroservis menentukan bagaimana komponen-komponen ini dipetakan).

**1.2 — Teknologi integrasi dipilih sesuai kebutuhan komunikasi antarmodul**

Bukan semua kebutuhan integrasi sama. REST API cocok untuk komunikasi standar berbasis permintaan-jawaban; GraphQL lebih cocok kalau sistem butuh mengambil data secara fleksibel dari berbagai sumber sekaligus; gRPC dipakai saat kecepatan komunikasi jadi prioritas (misalnya untuk sistem yang butuh respons dalam hitungan milidetik).

**1.3 — Format pertukaran data disesuaikan dengan kebutuhan integrasi sistem**

Format seperti JSON atau XML harus dipilih dan disepakati bersama semua pihak yang terlibat dalam integrasi — persis seperti yang dipaksakan SNAP secara nasional untuk sektor pembayaran, supaya semua pihak "berbicara bahasa data yang sama".

<!-- VISUAL PLACEHOLDER: Diagram tiga komponen SPKO (Model Credit Scoring, Core Banking, Dashboard) dengan panah bertuliskan "REST API / format JSON" yang menghubungkan ketiganya, menekankan bahwa teknologi dan format yang sama dipakai konsisten di semua koneksi -->

### Kenapa Ini Sangat Kritis untuk Solusi AI

Kesalahan memilih format pertukaran data untuk Solusi AI punya konsekuensi yang lebih halus dan berbahaya dibanding software biasa. Kalau model AI menerima data dalam format atau struktur yang sedikit berbeda dari yang diharapkan — misalnya field numerik yang datang sebagai teks, atau urutan field yang berubah — model **tidak akan otomatis error dengan jelas**. Ia mungkin tetap menghasilkan skor kredit, hanya saja skor itu dihitung dari interpretasi data yang salah, tanpa ada tanda peringatan bahwa terjadi kesalahan. Ini beda dari aplikasi web biasa yang biasanya langsung menampilkan pesan error yang jelas kalau formatnya tidak sesuai.

---

## Konteks SPKO: Memilih Komponen dan Teknologi Integrasi

Berdasarkan dokumentasi arsitektur SPKO (dari L1), komponen yang perlu diintegrasikan adalah:

| Komponen | Kebutuhan Komunikasi | Teknologi yang Dipilih |
|---|---|---|
| Model credit scoring ↔ Sistem core banking | Mengambil data nasabah untuk diproses model | REST API, format JSON |
| Model credit scoring ↔ Dashboard petugas kredit | Mengirim hasil skor kelayakan kredit | REST API, format JSON |
| Dashboard ↔ Sistem core banking | Menampilkan data nasabah pendukung keputusan | REST API, format JSON |

**Keputusan desain:** SPKO memakai REST API dan format JSON secara konsisten di semua koneksi — bukan karena ini satu-satunya pilihan valid, tapi karena konsistensi format across semua komponen mengurangi risiko kesalahan interpretasi data, mengikuti semangat yang sama dengan standardisasi SNAP di tingkat nasional.

---

## Quick Check
**(Target: 2 menit)**

**Tim SPKO mempertimbangkan memakai gRPC untuk komunikasi antara model credit scoring dan dashboard petugas kredit, meski semua koneksi lain di SPKO memakai REST API. Apa risiko dari keputusan ini, terlepas dari performa teknisnya?**

<details>
<summary>Lihat jawaban</summary>

Risikonya adalah inkonsistensi format dan protokol di dalam satu sistem yang sama — mirip masalah yang coba diselesaikan SNAP di tingkat nasional. Meski gRPC punya keunggulan performa, mencampur teknologi integrasi yang berbeda dalam satu Solusi AI menambah kompleksitas pemeliharaan dan risiko kesalahan interpretasi data antar komponen, kecuali ada kebutuhan performa spesifik yang benar-benar mengharuskannya (KUK 1.2 menekankan pemilihan "sesuai kebutuhan", bukan sekadar mengikuti tren teknologi).
</details>

---

## Latihan Terstruktur (Simulasi Singkat)
**(Target: 10 menit)**

**Skenario:** Kamu diminta merekomendasikan teknologi integrasi untuk tiga kebutuhan komunikasi baru di SPKO.

| Kebutuhan | Konteks |
|---|---|
| A | Dashboard petugas butuh menampilkan riwayat kredit, data pekerjaan, dan skor model sekaligus dalam satu tampilan, dari beberapa sumber data berbeda |
| B | Model credit scoring perlu memberi jawaban skor dalam hitungan milidetik untuk mendukung keputusan kredit instan di cabang |
| C | Sistem pelaporan bulanan mengambil data ringkasan dari core banking sekali per bulan untuk keperluan audit |

**Instruksi:** Tentukan teknologi integrasi yang paling sesuai (REST API/GraphQL/gRPC) untuk masing-masing, dan alasannya. Kerjakan dalam 10 menit.

<details>
<summary>Lihat kunci jawaban</summary>

| Kebutuhan | Teknologi | Alasan |
|---|---|---|
| A | GraphQL | Memungkinkan dashboard meminta data spesifik dari beberapa sumber sekaligus dalam satu permintaan, lebih efisien dibanding beberapa panggilan REST API terpisah |
| B | gRPC | Prioritas kecepatan respons yang sangat tinggi (milidetik) menjadi kebutuhan spesifik yang membenarkan penggunaan gRPC meski berbeda dari konsistensi REST API di komponen lain |
| C | REST API | Kebutuhan sederhana, tidak butuh performa ekstrem atau fleksibilitas kompleks — REST API standar sudah cukup dan tetap konsisten dengan mayoritas komponen SPKO |

**Poin penilaian mandiri:** Kalau kamu memilih teknologi yang sama untuk ketiganya tanpa mempertimbangkan konteks masing-masing, tinjau ulang KUK 1.2 — pemilihan teknologi integrasi harus "sesuai kebutuhan komunikasi", bukan keseragaman buta.
</details>

---

## Analisis Kasus: Kembali ke Standardisasi SNAP

SNAP lahir dari pengakuan bahwa fragmentasi teknologi integrasi — setiap institusi memilih protokol dan format sendiri-sendiri — menciptakan biaya dan risiko besar di skala industri. Latihan di atas menunjukkan versi kecil dari prinsip yang sama dalam skala satu Solusi AI: pemilihan teknologi integrasi tidak boleh sembarangan atau sekadar ikut tren, tapi juga tidak harus seragam membuta di semua kondisi — perlu pertimbangan kebutuhan komunikasi yang eksplisit (KUK 1.2), sambil tetap menjaga konsistensi di mana pun memungkinkan untuk mengurangi kompleksitas.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Standardisasi teknologi integrasi (seperti semangat SNAP) mengurangi biaya jangka panjang, meski mungkin terasa membatasi fleksibilitas di awal proyek.

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Kalau dashboard perlu menampilkan data dari banyak sumber sekaligus, pertimbangkan GraphQL sejak tahap desain — bukan menambal dengan banyak panggilan REST API terpisah yang memperlambat pengalaman pengguna.

**Bagi pengembang/petugas teknis (developer/engineer):**
Dokumentasikan keputusan pemilihan teknologi integrasi dan format data secara eksplisit (KUK 1.1) — supaya siapa pun yang bekerja di sistem ini nanti memahami alasan di balik pilihan tersebut, bukan sekadar warisan keputusan yang tidak terdokumentasi.

---

## Pertanyaan Refleksi

1. Pernahkah kamu bekerja dengan sistem yang menggunakan campuran teknologi integrasi tanpa alasan jelas? Bagaimana dampaknya terhadap pemeliharaan sistem?
2. SNAP adalah standar yang dipaksakan secara nasional oleh regulator. Menurutmu, kapan standardisasi semacam ini lebih baik ditentukan organisasi sendiri, dan kapan perlu campur tangan regulator?

---

## Ringkasan Lesson

- Elemen 1 menuntut identifikasi komponen berdasarkan dokumentasi arsitektur, pemilihan teknologi integrasi sesuai kebutuhan komunikasi, dan format pertukaran data yang konsisten.
- SNAP (Standar Nasional Open API Pembayaran) dari Bank Indonesia menunjukkan bagaimana fragmentasi teknologi integrasi menciptakan risiko nyata di skala industri — dan bagaimana standardisasi mengatasinya.
- Bagi Solusi AI, kesalahan format data lebih berbahaya dibanding software biasa karena model bisa tetap menghasilkan output tanpa pesan error yang jelas, meski input yang diterimanya sebenarnya keliru.

---

## Referensi

- Bank Indonesia. Surat Keputusan Gubernur Bank Indonesia No.23/10/KEP.GBI/2021 tentang Penetapan Standar Open Application Programming Interface (API) Pembayaran (SNAP).

---

## Navigasi

**[← M2-L1: Konsep Integrasi & Arsitektur Sistem Terintegrasi](l1-konsep-integrasi-arsitektur)** | **[M2-L3: Menggabungkan Arsitektur Teknis →](l3-menggabungkan-arsitektur-teknis)**
