---
title: 'Dari Integrasi ke Deployment: Menyiapkan Lingkungan'
course: ai-untuk-proses-data
module: 3
module_title: Deployment Solusi AI
lesson: 1
slug: l1-menyiapkan-lingkungan-deployment
unit_kompetensi:
  - kode: J.62AIN00.015.1
    nama: Memasang Solusi AI
    elemen: 'Elemen 1: Menyiapkan lingkungan deployment'
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
- Memilih lingkungan deployment berdasarkan kebutuhan teknis
- Memeriksa konfigurasi infrastruktur deployment sesuai spesifikasi teknis

**🌉 Dari Modul 2 ke Modul 3:** Sistem SPKO yang sudah kamu integrasikan dan uji sepanjang Modul 2 — model credit scoring, sistem core banking, dashboard petugas kredit, semuanya sudah terhubung dan teruji — sekarang siap memasuki tahap berikutnya: **dipasang (deploy)** ke lingkungan operasional yang sesungguhnya.

---

## Hook: Ketika Regulasi Menentukan di Mana Data Boleh Disimpan

Untuk kebanyakan perusahaan teknologi, memilih lingkungan deployment (on-premise, cloud, atau edge computing) adalah keputusan yang murni berdasarkan pertimbangan teknis dan biaya. Tapi untuk bank, ada satu variabel tambahan yang tidak bisa ditawar: **regulasi**.

Berdasarkan dokumen tanya-jawab resmi Otoritas Jasa Keuangan mengenai POJK Nomor 11/POJK.03/2022, **sistem core banking wajib ditempatkan pada pusat data dan pusat pemulihan bencana di wilayah Indonesia** — tidak bisa sembarangan dipindahkan ke pusat data di luar negeri, berapa pun efisiensi biaya yang ditawarkan. Bank yang ingin menempatkan sistem elektronik tertentu di luar Indonesia harus mengajukan permohonan izin eksplisit ke OJK, dan hanya sistem tertentu (bukan core banking) yang berpotensi diizinkan — itu pun dengan proses persetujuan yang ketat.

Regulasi lain yang berkaitan (POJK 38/POJK.03/2016 dan Peraturan Bank Indonesia yang lebih lama) menegaskan hal serupa: bank wajib memiliki pusat data dan Data Recovery Center yang ditempatkan di Indonesia, mempertimbangkan faktor geografis untuk keperluan mitigasi bencana.

Ini berarti bagi Solusi AI seperti SPKO yang terhubung langsung dengan data nasabah dan sistem core banking, **pilihan lingkungan deployment bukan cuma soal "mana yang paling murah atau paling cepat"** — ia harus dimulai dari pertanyaan kepatuhan: bolehkah komponen ini ditempatkan di sini secara hukum?

---

## Kerangka Konseptual: Elemen 1 — Menyiapkan Lingkungan Deployment

**1.1 — Lingkungan deployment dipilih berdasarkan kebutuhan teknis**

Tiga pilihan utama lingkungan deployment:
- **On-premise** — infrastruktur fisik dikelola sendiri oleh organisasi, biasanya di lokasi milik organisasi
- **Cloud computing** — infrastruktur disediakan pihak ketiga, diakses lewat internet, lebih fleksibel untuk skala
- **Edge computing** — pemrosesan dilakukan dekat dengan sumber data (misalnya di cabang bank itu sendiri), mengurangi latensi untuk kebutuhan respons cepat

**1.2 — Konfigurasi infrastruktur deployment diperiksa sesuai spesifikasi teknis**

Sebelum deployment dilakukan, konfigurasi (kapasitas server, alokasi CPU/GPU, kapasitas penyimpanan, konfigurasi jaringan) harus diperiksa memenuhi kebutuhan teknis Solusi AI — bukan diasumsikan "pasti cukup" tanpa verifikasi eksplisit.

<!-- VISUAL PLACEHOLDER: Diagram tiga kotak (On-Premise, Cloud, Edge) dengan checklist kepatuhan regulasi di atas kotak On-Premise bertuliskan "Wajib untuk Core Banking (POJK 11/2022)", menunjukkan bahwa pilihan ini bukan sekadar preferensi teknis -->

### Kenapa Ini Sangat Kritis untuk Solusi AI di Perbankan

Model AI seperti SPKO seringkali butuh sumber daya komputasi besar (terutama untuk pelatihan ulang/retraining model) — kebutuhan yang secara alami menarik organisasi ke arah cloud computing karena fleksibilitas skalanya. Tapi regulasi perbankan menarik ke arah sebaliknya untuk komponen yang menangani data inti nasabah. Ini menciptakan tantangan desain yang unik untuk Solusi AI perbankan: bagaimana memenuhi kebutuhan komputasi model AI yang besar, sambil tetap patuh pada kewajiban penempatan data yang ketat?

Solusi umum: memisahkan komponen berdasarkan sensitivitas datanya — komponen yang menangani data nasabah inti (core banking) tetap on-premise di Indonesia, sementara komponen pemrosesan model yang tidak langsung menyimpan data nasabah (misalnya sebagian pipeline pelatihan yang memakai data teranonimkan) berpotensi memakai cloud dengan persetujuan yang sesuai.

---

## Konteks SPKO: Memilih Lingkungan Deployment

| Komponen | Lingkungan yang Dipilih | Alasan |
|---|---|---|
| Sistem core banking (data nasabah) | On-premise, di Indonesia | Wajib sesuai POJK 11/2022 — tidak ada opsi lain yang legal tanpa izin khusus |
| Model credit scoring (inference) | On-premise, terhubung langsung ke core banking | Menghindari perpindahan data nasabah ke luar infrastruktur bank saat pemrosesan skor |
| Dashboard petugas kredit | On-premise, jaringan internal bank | Konsisten dengan kebijakan keamanan data internal |

**Catatan:** SPKO di skenario latihan ini memilih on-premise di seluruh komponen — bukan karena cloud tidak pernah bisa dipakai bank, tapi karena skenario ini melibatkan data nasabah inti yang jatuh langsung di bawah kewajiban POJK 11/2022.

---

## Quick Check

**Tim SPKO mempertimbangkan memindahkan sebagian pemrosesan model credit scoring ke cloud computing untuk mengurangi biaya infrastruktur. Pertanyaan apa yang HARUS dijawab lebih dulu sebelum keputusan biaya ini diambil?**

<details>
<summary>Lihat jawaban</summary>

Pertanyaan yang harus dijawab lebih dulu: apakah komponen yang dipindahkan ke cloud ini menangani atau menyimpan data nasabah inti (core banking)? Jika ya, ini melanggar kewajiban POJK 11/2022 kecuali sudah mendapat izin eksplisit dari OJK. Pertimbangan biaya tidak boleh mendahului pertimbangan kepatuhan regulasi untuk sistem yang menangani data nasabah.
</details>

---

## Latihan Terstruktur (Simulasi Singkat)
**(Target: 12 menit)**

**Skenario:** Tim SPKO mengevaluasi tiga rencana penempatan infrastruktur berikut.

| Rencana | Deskripsi |
|---|---|
| A | Memindahkan seluruh sistem core banking ke cloud provider internasional untuk menghemat biaya operasional |
| B | Menyimpan core banking tetap on-premise di Indonesia, tapi memakai layanan cloud untuk pipeline pelatihan ulang model dengan data yang sudah dianonimkan sepenuhnya, setelah mendapat kajian internal kepatuhan |
| C | Konfigurasi server on-premise diperiksa memiliki kapasitas GPU yang cukup untuk kebutuhan inference model sebelum deployment dimulai |

**Instruksi:** Tentukan (a) apakah rencana ini sesuai KUK dan regulasi, (b) tindakan yang diperlukan. Kerjakan dalam 12 menit.

<details>
<summary>Lihat kunci jawaban</summary>

| Rencana | Sesuai? | Tindakan |
|---|---|---|
| A | Tidak — melanggar POJK 11/2022 | Batalkan rencana ini kecuali sudah mengajukan dan mendapat izin eksplisit OJK; core banking wajib tetap di Indonesia |
| B | Berpotensi sesuai, dengan syarat | Pastikan proses anonimisasi data benar-benar menghilangkan kemungkinan re-identifikasi nasabah, dan kajian kepatuhan didokumentasikan sebelum implementasi — jangan asumsikan "data teranonimkan" otomatis aman tanpa verifikasi |
| C | Sesuai — ini persis KUK 1.2 | Lanjutkan; ini contoh baik dari pemeriksaan konfigurasi infrastruktur sebelum deployment |

**Poin penilaian mandiri:** Rencana B adalah yang paling sering disalahpahami — anonimisasi data bukan jaminan otomatis lolos dari kewajiban regulasi; perlu verifikasi teknis dan kepatuhan yang eksplisit, bukan asumsi.
</details>

---

## Analisis Kasus: Kembali ke Kewajiban Penempatan Data

Regulasi POJK 11/2022 menunjukkan bahwa bagi Solusi AI perbankan, pertanyaan "di mana kita akan deploy sistem ini" tidak bisa dijawab murni dari sisi teknis atau biaya. Rencana A dalam latihan di atas adalah pengingat konkret: godaan efisiensi biaya cloud internasional harus selalu diuji dulu terhadap kewajiban regulasi penempatan data inti nasabah — mengabaikan ini bukan cuma risiko teknis, tapi risiko kepatuhan yang bisa berujung sanksi dari regulator.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Libatkan tim kepatuhan sejak tahap perencanaan arsitektur deployment, bukan setelah keputusan infrastruktur sudah diambil — mengubah keputusan deployment setelah sistem berjalan jauh lebih mahal daripada merencanakannya dengan benar sejak awal.

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Pahami batasan lingkungan deployment saat merancang antarmuka — misalnya, jika beberapa komponen harus tetap on-premise sementara yang lain di cloud, pastikan desain sistem mengakomodasi kemungkinan latensi yang berbeda antar komponen.

**Bagi pengembang/petugas teknis (developer/engineer):**
Dokumentasikan secara eksplisit klasifikasi data untuk setiap komponen (data nasabah inti vs data teranonimkan) sebagai dasar keputusan penempatan infrastruktur — jangan biarkan klasifikasi ini implisit atau berdasarkan asumsi.

---

## Pertanyaan Refleksi

1. Di organisasimu, siapa yang biasanya terlibat dalam keputusan memilih lingkungan deployment — hanya tim teknis, atau juga tim kepatuhan/legal sejak awal?
2. Regulasi POJK 11/2022 menciptakan ketegangan antara kebutuhan komputasi AI yang besar (yang condong ke cloud) dan kewajiban penempatan data (yang condong ke on-premise). Menurutmu, solusi arsitektur apa yang paling masuk akal untuk menyeimbangkan keduanya?

---

## Ringkasan Lesson

- Elemen 1 menuntut pemilihan lingkungan deployment berdasarkan kebutuhan teknis dan pemeriksaan konfigurasi infrastruktur sesuai spesifikasi.
- Bagi Solusi AI perbankan, regulasi (POJK 11/2022 dan aturan terkait) menjadi variabel penentu yang tidak bisa ditawar dalam memilih lingkungan deployment — core banking wajib tetap di Indonesia.
- Solusi umum untuk menyeimbangkan kebutuhan komputasi AI dan kepatuhan regulasi adalah memisahkan komponen berdasarkan sensitivitas data, bukan memperlakukan seluruh sistem secara seragam.

---

## Referensi

- Otoritas Jasa Keuangan. *Tanya Jawab Peraturan Otoritas Jasa Keuangan Nomor 11/POJK.03/2022 tentang Penyelenggaraan Teknologi Informasi Oleh Bank Umum*.
- Peraturan Otoritas Jasa Keuangan Nomor 38/POJK.03/2016 tentang Penerapan Manajemen Risiko dalam Penggunaan Teknologi Informasi oleh Bank Umum.

---

## Navigasi

**[← M2-L4: Menguji Sistem Terintegrasi & Dokumentasi](../m2-integrasi-komponen-solusi-ai/l4-menguji-sistem-terintegrasi)** | **[M3-L2: Melakukan Deployment Solusi AI →](l2-melakukan-deployment)**
