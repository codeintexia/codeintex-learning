---
title: 'Capstone: Audit Terintegrasi SPKO'
course: ai-untuk-proses-data
module: 6
module_title: Audit Siklus Hidup & Evaluasi Terintegrasi
lesson: 3
slug: l3-capstone-audit-terintegrasi
unit_kompetensi:
  - kode: Semua 6 unit
    nama: >-
      J.63OPR00.014.2, J.63OPR00.015.2, J.62AIN00.014.1, J.62AIN00.015.1,
      J.62AIN00.016.1, J.62AIN00.017.1
level: Foundational — Competency
kategori: Competency
bloom_level: Evaluate
durasi_menit: 45
durasi_baca_menit: 10
durasi_latihan_menit: 35
bahasa: Indonesia
duration_minutes: 10
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Ini adalah lesson penutup seluruh kursus **AI untuk Proses Data**. Dalam satu skenario audit menyeluruh, kamu akan mendemonstrasikan pemahaman terhadap keenam unit kompetensi sekaligus — dari kualitas data hingga status perawatan Solusi AI.

Di akhir lesson ini, kamu akan mampu:
- Menelusuri jejak sebuah masalah dari gejala akhir kembali ke akar penyebabnya di sepanjang siklus hidup Solusi AI
- Mengevaluasi kepatuhan dan kualitas SPKO secara menyeluruh, bukan per elemen kompetensi terpisah
- Menyusun rekomendasi audit yang mencakup seluruh siklus hidup, bukan tambalan di satu titik saja

---

## Skenario: Permintaan Audit Menyeluruh

Otoritas Jasa Keuangan meminta Bank Nusantara Sejahtera melakukan audit internal menyeluruh terhadap SPKO, menyusul laporan rutin yang menunjukkan sejumlah anomali. Sebagai bagian dari tim audit, kamu diberi akses ke ringkasan riwayat operasional SPKO berikut.

### Ringkasan Riwayat SPKO (6 Bulan Terakhir)

**Bulan 1-2 (Fondasi Data):**
Ditemukan dalam log bahwa sejumlah data nasabah diinput dengan kode klasifikasi pekerjaan yang berasal dari sistem lama (sebelum pembaruan tabel referensi organisasi), tanpa pemetaan eksplisit ke kode baru.

**Bulan 2-3 (Integrasi & Deployment):**
SPKO diintegrasikan dan dipasang menggunakan strategi canary release. Dokumentasi deployment lengkap tersedia, termasuk hasil validasi pascadeployment. Mekanisme enkripsi dan autentikasi multi-faktor sudah diterapkan sesuai POJK 11/2022.

**Bulan 4 (Insiden Performa Infrastruktur):**
Waktu respons SPKO melambat signifikan setiap akhir bulan karena lonjakan volume pengajuan. Solusi auto-scaling terjadwal diterapkan dan tervalidasi berhasil pada siklus berikutnya.

**Bulan 5 (Penurunan Metrik Model):**
Recall model turun dari 0.83 ke 0.68, berkorelasi dengan peningkatan keluhan nasabah. Tim mengidentifikasi dua kemungkinan akar masalah: data drift dari perubahan kebijakan suku bunga, dan pergeseran komposisi data nasabah tanpa riwayat kredit.

**Bulan 6 (Perawatan):**
Model diretraining. Laporan internal menunjukkan hasil validasi pada data terpisah: recall 0.79 — **masih di bawah target 0.80**, meski sudah membaik dari 0.68. Model tetap diterapkan ke produksi karena "sudah cukup mendekati target dan tim butuh segera menyelesaikan siklus perawatan sebelum tenggat internal."

---

## Latihan Audit Menyeluruh
**(Target: 35 menit — ini adalah latihan terbesar dan paling kompleks di kursus ini)**

### Tugas 1 — Identifikasi Pelanggaran KUK di Sepanjang Siklus (10 menit)

Tinjau ringkasan riwayat di atas. Identifikasi minimal tiga titik dalam siklus ini di mana KUK dari unit kompetensi tertentu berpotensi tidak terpenuhi. Sebutkan unit, elemen, dan alasannya.

### Tugas 2 — Telusuri Akar Masalah Lintas Modul (10 menit)

Apakah masalah di Bulan 5 (penurunan recall) punya kemungkinan hubungan dengan temuan di Bulan 1-2 (kode klasifikasi yang tidak dipetakan)? Jelaskan alasanmu.

### Tugas 3 — Evaluasi Keputusan Bulan 6 (10 menit)

Keputusan menerapkan model ke produksi meski recall (0.79) masih di bawah target (0.80) adalah keputusan yang perlu dievaluasi kritis. Apakah ini keputusan yang tepat? Apa yang seharusnya dilakukan berbeda?

### Tugas 4 — Susun Rekomendasi Audit (5 menit)

Sebagai penutup, susun tiga rekomendasi audit paling prioritas untuk Bank Nusantara Sejahtera, mencakup lebih dari satu titik dalam siklus hidup SPKO.

---

<details>
<summary>Lihat kunci jawaban lengkap</summary>

### Tugas 1 — Pelanggaran KUK Teridentifikasi

**1. Bulan 1-2 — Memastikan Validitas Data (Elemen 2, KUK 2.1-2.2):** Kode klasifikasi lama yang tidak dipetakan eksplisit ke kode baru melanggar prinsip referensi dan kodifikasi data yang konsisten (M1-L4). Ini bukan pelanggaran yang "terlihat" — data tetap masuk secara teknis, tapi substansinya keliru.

**2. Bulan 6 — Merawat Solusi AI (Elemen 2, KUK 2.1):** Menerapkan model yang belum memenuhi kriteria sukses yang ditetapkan (recall ≥ 0.80) melanggar prinsip bahwa perawatan harus dilakukan "sesuai rencana perawatan" — bukan disesuaikan secara sepihak karena tekanan tenggat internal (M5-L2).

**3. Bulan 6 — Merencanakan Perawatan Solusi AI (kriteria sukses yang ditetapkan di Elemen 2):** Kalau kriteria sukses "direlaksasi" tanpa proses formal (hanya karena "sudah cukup mendekati"), ini menunjukkan kelemahan dalam bagaimana kriteria sukses awal ditegakkan — bukan cuma soal Modul 5, tapi juga menunjukkan proses di Modul 4 tidak dijalankan dengan disiplin penuh sampai akhir.

### Tugas 2 — Hubungan Lintas Modul

**Ya, ada kemungkinan hubungan yang perlu diinvestigasi lebih lanjut.** Kode klasifikasi pekerjaan yang tidak konsisten sejak Bulan 1-2 berarti sebagian data pelatihan awal model kemungkinan mengandung representasi yang keliru untuk field ini. Ini bisa jadi berkontribusi pada kerentanan model terhadap perubahan pola data di kemudian hari (Bulan 5) — model yang dilatih dengan fondasi data yang sudah retak sejak awal lebih rentan terhadap drift, karena ia tidak pernah benar-benar mempelajari pola yang representatif untuk field tersebut. Ini bukan kepastian mutlak tanpa investigasi teknis lebih lanjut, tapi ini **hipotesis yang harus dimasukkan** ke dalam investigasi akar masalah — persis seperti prinsip "menelusuri kembali ke fondasi" yang ditekankan di M6-L1.

### Tugas 3 — Evaluasi Keputusan Bulan 6

**Ini keputusan yang bermasalah.** Menerapkan model yang belum memenuhi kriteria sukses karena tekanan tenggat internal mengulangi persis kesalahan yang sudah diperingatkan di M3-L2 (deployment yang terburu-buru karena tekanan jadwal) dan M5-L2 (pentingnya validasi jujur, bahkan ketika hasilnya "gagal"). 

**Yang seharusnya dilakukan:** Jika recall 0.79 masih di bawah target 0.80, opsi yang lebih tepat adalah (a) melanjutkan investigasi dan penyempurnaan sebelum menerapkan ke produksi, (b) mempertimbangkan penerapan bertahap terbatas (seperti canary release yang sudah dipelajari di M3-L2) sambil terus memantau ketat, atau (c) secara formal merevisi kriteria sukses dengan justifikasi yang jelas dan disetujui pihak berwenang — bukan diam-diam "dianggap cukup" tanpa proses.

### Tugas 4 — Rekomendasi Audit Prioritas

1. **Audit menyeluruh terhadap seluruh data historis untuk memastikan tidak ada kode referensi/klasifikasi lain yang belum dipetakan** — bukan hanya kasus yang sudah ditemukan, karena ini menunjukkan kemungkinan ada masalah sistemik dalam proses pemasukan data di masa lalu.

2. **Tetapkan proses formal untuk mengubah atau merelaksasi kriteria sukses** — kriteria sukses yang ditetapkan di tahap perencanaan (Modul 4) tidak boleh "ditawar" secara informal saat eksekusi (Modul 5) tanpa persetujuan dan dokumentasi resmi.

3. **Investigasi hubungan antara kualitas data historis (Bulan 1-2) dan drift model (Bulan 5)** — untuk memastikan retraining di masa depan tidak hanya menambal gejala terbaru, tapi juga memperbaiki fondasi data yang mungkin masih membawa masalah lama.

</details>

---

## Penutup Kursus

Selamat — kamu telah menyelesaikan seluruh 25 lesson kursus **AI untuk Proses Data**, menyusuri siklus hidup Solusi AI secara menyeluruh: dari kualitas data paling mendasar, integrasi komponen, deployment yang patuh regulasi, evaluasi berbasis bukti, hingga perawatan yang disiplin.

Skenario capstone ini sengaja dirancang tanpa jawaban yang sepenuhnya "hitam putih" — seperti yang sudah kamu alami berulang kali sepanjang kursus, kompetensi yang sesungguhnya bukan soal menghafal prosedur, tapi kemampuan mengevaluasi situasi kompleks dengan penilaian yang cermat dan bertanggung jawab, persis seperti yang dituntut "ketepatan" dan "ketelitian" di aspek kritis keenam unit yang sudah kamu pelajari di L2.

---

## Ringkasan Kursus

- Siklus hidup Solusi AI adalah rantai yang saling terhubung — kelemahan di satu titik (seperti kualitas data di awal) bisa menjalar ke titik yang jauh di kemudian hari (seperti drift model).
- Kepatuhan terhadap kriteria dan prosedur bukan formalitas yang bisa dilonggarkan di bawah tekanan tenggat atau prioritas bisnis — pelonggaran informal adalah sumber risiko yang berulang kali muncul sepanjang kursus ini.
- Audit yang baik tidak berhenti di gejala yang paling terlihat, tapi menelusuri kemungkinan hubungan ke titik-titik lain di sepanjang siklus.

---

## Navigasi

**[← M6-L2: Kriteria Penilaian per Unit Kompetensi](l2-kriteria-penilaian)** | **Selesai — Kembali ke Halaman Kursus**
