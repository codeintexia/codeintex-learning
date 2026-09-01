---
title: Melakukan Deployment Solusi AI
course: ai-untuk-proses-data
module: 3
module_title: Deployment Solusi AI
lesson: 2
slug: l2-melakukan-deployment
unit_kompetensi:
  - kode: J.62AIN00.015.1
    nama: Memasang Solusi AI
    elemen: 'Elemen 2: Melakukan deployment Solusi AI'
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
- Menyiapkan model dan komponen sistem untuk deployment sesuai prosedur
- Menyusun dependensi dan konfigurasi pendukung sesuai kebutuhan solusi
- Melakukan deployment ke lingkungan yang telah disiapkan

---

## Hook: Mayoritas Proyek AI Tidak Pernah Sampai ke Tahap Ini

Sebuah analisis industri mengenai kegagalan proyek AI korporasi mengungkap angka yang mengejutkan: **tingkat kegagalan proyek AI diperkirakan mencapai 50 hingga 95 persen** — proyek yang tidak pernah berhasil mencapai tahap produksi atau tidak terbukti memberikan nilai bisnis yang nyata. Ini bukan statistik kosong; ia mencerminkan investasi besar yang menguap dan ekspektasi yang tidak terpenuhi.

Poin yang penting untuk direnungkan: kalau kamu sudah sampai ke lesson ini — Solusi AI SPKO sudah terintegrasi (Modul 2), lingkungannya sudah disiapkan (L1) — kamu sudah melewati sebagian besar titik-titik gagal yang membuat mayoritas proyek AI berhenti sebelum sampai sejauh ini. Tapi tahap **deployment yang sesungguhnya** — yang akan kamu pelajari di lesson ini — tetap menjadi salah satu titik paling rawan, karena di sinilah model yang sudah teruji di lingkungan terkontrol pertama kali benar-benar "hidup" di lingkungan operasional nyata.

Sebuah pengamatan tentang siklus proyek AI menegaskan hal ini: tanpa rencana rollback yang jelas dan teruji untuk kembali ke sistem sebelumnya jika model baru bermasalah, **setiap deployment pada dasarnya adalah taruhan tanpa jaring pengaman**.

---

## Kerangka Konseptual: Elemen 2 — Melakukan Deployment Solusi AI

**2.1 — Model dan komponen sistem disiapkan untuk deployment sesuai prosedur**

Sebelum deployment sesungguhnya, model dan komponen perlu dipersiapkan mengikuti prosedur yang sudah ditentukan — bukan proses ad-hoc yang berbeda setiap kali.

**2.2 — Dependensi dan konfigurasi pendukung disusun sesuai kebutuhan solusi**

Model AI jarang berdiri sendiri — ia butuh library tertentu, versi runtime tertentu, variabel konfigurasi yang harus disusun tepat. Kesalahan kecil di sini (versi library yang tidak cocok, misalnya) bisa membuat model berperilaku berbeda dari saat diuji.

**2.3 — Deployment dilakukan ke lingkungan yang telah disiapkan**

Ini tahap eksekusi — memindahkan model dan komponen dari lingkungan pengujian ke lingkungan operasional (yang sudah kamu siapkan di L1).

### Mengingat Kembali CI/CD dari Modul 2

Ingat konsep CI/CD/MLOps yang dijelaskan di M2-L1? **Inilah tempat konsep itu benar-benar dipraktikkan.** Praktik deployment yang matang tidak melakukan seluruh proses secara manual satu per satu — melainkan memakai **pipeline otomatis** yang menjalankan quality gate (pengecekan kualitas kode dan model), memberikan notifikasi cepat jika ada kegagalan, dan yang paling penting: menyiapkan **rencana rollback** yang bisa dieksekusi cepat jika deployment ternyata bermasalah.

Beberapa strategi deployment yang umum dipakai untuk meminimalkan risiko:

- **Canary release** — model baru dipasang untuk sebagian kecil traffic/pengguna dulu, dipantau, baru ditingkatkan bertahap ke 100% jika stabil
- **Blue-green deployment** — dua lingkungan identik (lama dan baru) dijalankan bergantian; deployment baru diuji di lingkungan "hijau" sebelum traffic dialihkan sepenuhnya dari lingkungan "biru" yang lama

<!-- VISUAL PLACEHOLDER: Diagram blue-green deployment — kotak "Biru (versi lama, aktif)" dan "Hijau (versi baru, diuji)" dengan panah traffic yang awalnya 100% ke Biru, lalu berpindah bertahap ke Hijau setelah pengujian berhasil, dengan panah putus-putus "rollback" kembali ke Biru jika gagal -->

### Kenapa Ini Sangat Kritis untuk Solusi AI

Deployment software biasa yang gagal biasanya menghasilkan error yang jelas (aplikasi tidak bisa diakses, halaman error). **Deployment model AI yang bermasalah seringkali TIDAK menghasilkan error yang jelas** — sistem tetap berjalan, tetap memberi jawaban, hanya saja jawabannya (skor kredit, dalam kasus SPKO) mungkin sudah tidak seakurat versi yang diuji sebelumnya, karena perbedaan kecil pada dependensi atau konfigurasi lingkungan operasional dibanding lingkungan pengujian. Inilah kenapa rencana rollback dan strategi bertahap seperti canary release jadi jauh lebih penting untuk Solusi AI — mendeteksi masalah sebelum berdampak ke seluruh keputusan kredit yang diproses sistem.

---

## Konteks SPKO: Melakukan Deployment

| Tahap | Penerapan di SPKO |
|---|---|
| Persiapan model & komponen | Model credit scoring yang sudah diuji di Modul 2 dikemas sesuai prosedur deployment standar bank |
| Dependensi & konfigurasi | Versi library machine learning, konfigurasi koneksi ke core banking, variabel lingkungan diverifikasi sesuai kebutuhan |
| Strategi deployment | Canary release — model baru awalnya hanya memproses 10% pengajuan kredit, dipantau performanya, baru ditingkatkan bertahap |
| Rencana rollback | Jika skor yang dihasilkan model baru menunjukkan pola anomali dibanding versi sebelumnya, sistem otomatis kembali ke model versi lama |

---

## Quick Check

**Tim SPKO melakukan deployment model versi baru langsung ke 100% traffic (semua pengajuan kredit) tanpa tahap bertahap, karena model ini sudah "lolos pengujian" di Modul 2. Apa risiko dari pendekatan ini?**

<details>
<summary>Lihat jawaban</summary>

Risikonya adalah pengujian di Modul 2 dilakukan di lingkungan terkontrol, sementara lingkungan operasional nyata bisa punya perbedaan kecil (dependensi, konfigurasi, pola data nyata yang lebih beragam) yang tidak sepenuhnya tertangkap saat pengujian. Deployment langsung ke 100% traffic tanpa tahap bertahap (seperti canary release) berarti jika ada masalah yang baru muncul di lingkungan nyata, dampaknya langsung ke seluruh pengajuan kredit, bukan hanya sebagian kecil yang bisa dipantau dan diperbaiki dulu.
</details>

---

## Latihan Terstruktur (Simulasi Singkat)
**(Target: 12 menit)**

**Skenario:** Kamu meninjau rencana deployment model SPKO versi baru berikut.

| Rencana | Deskripsi |
|---|---|
| A | Model baru langsung menggantikan model lama sepenuhnya, tanpa rencana rollback jika bermasalah |
| B | Model baru dipasang dengan canary release (10% traffic awal), dipantau 3 hari, lalu ditingkatkan bertahap jika stabil |
| C | Dependensi library model baru belum diverifikasi kompatibel dengan versi yang berjalan di lingkungan operasional, tapi deployment tetap dilanjutkan karena jadwal sudah mepet |

**Instruksi:** Tentukan (a) KUK yang dilanggar/dipenuhi (2.1/2.2/2.3), (b) tindakan yang diperlukan. Kerjakan dalam 12 menit.

<details>
<summary>Lihat kunci jawaban</summary>

| Rencana | KUK | Tindakan |
|---|---|---|
| A | Melanggar prinsip deployment yang aman (terkait 2.3) | Susun rencana rollback sebelum deployment dilanjutkan — "setiap deployment tanpa jaring pengaman adalah taruhan" |
| B | Memenuhi 2.3 dengan baik | Tidak perlu tindakan tambahan — lanjutkan pemantauan sesuai rencana |
| C | Melanggar 2.2 (dependensi belum sesuai kebutuhan solusi) | Jangan lanjutkan deployment karena tekanan jadwal; verifikasi kompatibilitas dependensi terlebih dahulu — deployment dengan dependensi yang belum terverifikasi berisiko menghasilkan perilaku model yang berbeda dari saat diuji |
</details>

**Poin penilaian mandiri:** Rencana C adalah jebakan paling umum dalam dunia nyata — tekanan jadwal sering dipakai sebagai alasan melewati verifikasi dependensi, padahal ini persis salah satu penyebab tersembunyi kegagalan deployment yang disebut di hook.

---

## Analisis Kasus: Kembali ke Statistik Kegagalan Proyek AI

Angka kegagalan 50-95% yang dibahas di hook tidak semuanya terjadi di tahap awal (perencanaan atau pengembangan model) — sebagian signifikan terjadi justru di tahap deployment seperti yang kamu pelajari di lesson ini. Rencana C dalam latihan di atas adalah ilustrasi konkret: tekanan untuk segera "meluncurkan" sering mengorbankan verifikasi teknis yang seharusnya wajib, menciptakan risiko yang baru terlihat setelah sistem berjalan di produksi — saat perbaikannya jauh lebih mahal dan berisiko dibanding mencegahnya sejak awal.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Jangan biarkan tekanan jadwal peluncuran mengorbankan verifikasi dependensi atau rencana rollback — deployment yang terburu-buru sering menjadi penyebab tersembunyi mengapa proyek AI gagal memberikan nilai bisnis yang dijanjikan.

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Untuk deployment bertahap seperti canary release, pertimbangkan bagaimana dashboard menampilkan indikator bahwa sebagian keputusan sedang diproses model versi baru — transparansi ini membantu petugas memahami konteks jika ada perbedaan hasil selama masa pemantauan.

**Bagi pengembang/petugas teknis (developer/engineer):**
Selalu uji rencana rollback SEBELUM deployment dilakukan, bukan menyiapkannya "kalau-kalau nanti dibutuhkan" — rollback yang belum pernah diuji seringkali gagal tepat saat paling dibutuhkan.

---

## Pertanyaan Refleksi

1. Pernahkah kamu mengalami atau mendengar situasi deployment yang terburu-buru karena tekanan jadwal? Apa dampaknya?
2. Canary release membutuhkan waktu pemantauan sebelum ditingkatkan ke seluruh sistem — di dunia nyata, bagaimana kamu akan menyeimbangkan antara kehati-hatian ini dengan tekanan bisnis untuk segera "meluncurkan penuh"?

---

## Ringkasan Lesson

- Elemen 2 menuntut persiapan model sesuai prosedur, penyusunan dependensi dan konfigurasi yang tepat, serta eksekusi deployment yang hati-hati ke lingkungan operasional.
- Statistik kegagalan proyek AI korporasi (50-95%) menegaskan bahwa deployment adalah salah satu titik paling rawan dalam siklus hidup Solusi AI — bahkan setelah integrasi dan pengujian berhasil.
- Praktik CI/CD/MLOps yang dijelaskan di Modul 2 dipraktikkan langsung di sini lewat strategi seperti canary release dan blue-green deployment, dengan rencana rollback sebagai jaring pengaman yang wajib diuji sebelum dibutuhkan.

---

## Referensi

- Analisis industri teknologi mengenai faktor-faktor kegagalan proyek AI korporasi, 2026.
- Analisis mengenai lifecycle proyek AI dari masalah bisnis hingga produksi, 2026.

---

## Navigasi

**[← M3-L1: Menyiapkan Lingkungan Deployment](l1-menyiapkan-lingkungan-deployment)** | **[M3-L3: Validasi & Pengujian Pascadeployment →](l3-validasi-pengujian-pascadeployment)**
