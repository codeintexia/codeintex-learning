---
title: 'Studi Kasus: Menangani Insiden Performa SPKO'
course: ai-untuk-proses-data
module: 5
module_title: Merawat Solusi AI
lesson: 3
slug: l3-studi-kasus-insiden-performa
unit_kompetensi:
  - kode: J.62AIN00.017.1
    nama: Merawat Solusi AI
    elemen: Latihan terintegrasi Elemen 1-2
level: Foundational — Competency
kategori: Competency
bloom_level: Evaluate
durasi_menit: 32
durasi_baca_menit: 7
durasi_latihan_menit: 25
bahasa: Indonesia
duration_minutes: 32
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Lesson ini adalah **latihan terintegrasi** yang menutup Modul 5 — menggabungkan L1 (menyiapkan perawatan) dan L2 (melakukan & mendokumentasikan perawatan) dalam satu skenario insiden operasional yang berbeda dari kasus F1-Score/recall yang sudah kamu kerjakan di Modul 4.

Di akhir lesson ini, kamu akan mampu:
- Menangani insiden performa yang sifatnya operasional/infrastruktur, bukan hanya masalah akurasi model
- Menyiapkan dan mengeksekusi perawatan dalam kondisi mendesak
- Mendokumentasikan penanganan insiden sesuai standar

---

## Konteks: Insiden di Akhir Bulan

Tim IT Bank Nusantara Sejahtera menemukan bahwa waktu respons SPKO melambat signifikan pada akhir bulan, bertepatan dengan lonjakan volume pengajuan kredit. Berikut data yang tersedia:

### Data Insiden

| Waktu | Volume Pengajuan/Jam | Waktu Respons Rata-rata |
|---|---|---|
| Hari biasa | ~50 pengajuan | 1.7 detik |
| Akhir bulan (3 hari terakhir) | ~180 pengajuan | 5.8 detik |
| Target SLA (Service Level Agreement) | — | < 2 detik |

### Informasi Tambahan
- Pola ini terjadi konsisten setiap akhir bulan selama 3 bulan terakhir, tapi baru sekarang volumenya cukup besar hingga melewati ambang batas SLA.
- Recall dan F1-Score model (metrik akurasi) tetap stabil sesuai target — ini murni masalah kapasitas infrastruktur, bukan kualitas model.
- Tim IT belum punya rencana kapasitas khusus untuk lonjakan periodik ini — infrastruktur dikonfigurasi untuk volume rata-rata harian.
- Beberapa petugas kredit melaporkan mulai menghindari menggunakan SPKO saat lambat, memilih memproses manual — yang berisiko mengurangi konsistensi keputusan kredit.

---

## Latihan Terstruktur: Menangani Insiden dari Awal hingga Dokumentasi
**(Target: 25 menit)**

Kerjakan tugas berikut mengikuti alur Elemen 1 (menyiapkan) dan Elemen 2 (melakukan & mendokumentasikan).

### Tugas 1 — Verifikasi Kebutuhan Perawatan (L1, 5 menit)
Berdasarkan data di atas, komponen arsitektur mana yang perlu dirawat? Apakah ini masalah yang sama dengan yang kamu tangani di Modul 4?

### Tugas 2 — Menentukan Prosedur Perawatan (L1, 5 menit)
Karena pola ini berulang dan bisa diprediksi (akhir bulan), tindakan apa yang lebih tepat: solusi reaktif (menambah kapasitas setiap kali terjadi) atau solusi terencana (mengantisipasi pola)? Kaitkan dengan prinsip yang sudah kamu pelajari di M4-L3.

### Tugas 3 — Eksekusi dan Dokumentasi (L2, 10 menit)
Susun rencana eksekusi konkret, termasuk bagaimana kamu akan memvalidasi bahwa solusi ini berhasil (bukan sekadar "sudah dilakukan").

### Tugas 4 — Menangani Dampak Samping (5 menit)
Petugas kredit yang mulai menghindari SPKO saat lambat adalah masalah tambahan yang tidak murni teknis. Bagaimana kamu mengatasi ini sebagai bagian dari perawatan menyeluruh?

---

<details>
<summary>Lihat kunci jawaban lengkap</summary>

### Tugas 1 — Verifikasi Kebutuhan Perawatan

Komponen yang perlu dirawat: **infrastruktur/kapasitas komputasi** (server, alokasi CPU/GPU), bukan model AI itu sendiri. Ini **berbeda** dari kasus Modul 4 — di sana masalahnya di akurasi model (recall, F1-Score), di sini metrik model tetap sehat tapi *waktu respons* infrastruktur yang bermasalah. Ini menegaskan bahwa "merawat Solusi AI" mencakup lebih dari sekadar model — termasuk seluruh komponen arsitektur (ingat cakupan Elemen 4 unit Merawat Solusi AI: strategi AI, arsitektur & infrastruktur data, dst).

### Tugas 2 — Menentukan Prosedur Perawatan

Karena pola ini **berulang dan bisa diprediksi** (terjadi konsisten setiap akhir bulan selama 3 bulan), solusi **terencana/preventif** jauh lebih tepat dibanding reaktif — persis prinsip "sepuluh kali lebih mahal" dari M4-L3. Menunggu insiden terjadi lagi setiap bulan dan menambah kapasitas secara darurat setiap kali adalah pendekatan reaktif yang mahal dan berisiko; solusi yang tepat adalah **auto-scaling terjadwal** atau alokasi kapasitas tambahan yang otomatis aktif menjelang akhir bulan, berdasarkan pola yang sudah teridentifikasi jelas dari data 3 bulan terakhir.

### Tugas 3 — Eksekusi dan Dokumentasi

**Rencana eksekusi:** Implementasikan mekanisme auto-scaling atau alokasi kapasitas tambahan terjadwal untuk 3-5 hari terakhir tiap bulan, berdasarkan pola volume yang sudah teridentifikasi.

**Validasi:** Pantau waktu respons pada akhir bulan berikutnya setelah solusi diterapkan — kriteria sukses: waktu respons tetap di bawah 2 detik meski volume pengajuan meningkat serupa dengan pola sebelumnya. Jangan anggap selesai hanya karena kapasitas sudah ditambah — perlu bukti nyata bahwa SLA terpenuhi di siklus berikutnya.

**Dokumentasi:** Catat pola volume yang mendasari keputusan, solusi teknis yang diterapkan, tanggal implementasi, dan hasil validasi di siklus akhir bulan berikutnya.

### Tugas 4 — Menangani Dampak Samping

Petugas yang menghindari SPKO dan memproses manual adalah risiko tambahan yang perlu ditangani terpisah dari perbaikan infrastruktur:
- **Komunikasikan** ke tim petugas kredit bahwa perbaikan sedang/sudah dilakukan, dengan target waktu jelas
- **Pantau** apakah praktik pemrosesan manual selama periode lambat sudah menghasilkan keputusan yang konsisten dengan yang biasanya dihasilkan SPKO — ini penting untuk audit kepatuhan
- Setelah solusi kapasitas diterapkan dan tervalidasi, **verifikasi ulang** bahwa petugas kembali memakai SPKO secara konsisten — masalah kepercayaan pada sistem butuh waktu pulih, tidak otomatis selesai begitu masalah teknis diperbaiki

**Poin penting:** Ini menunjukkan bahwa perawatan Solusi AI yang menyeluruh mencakup dimensi manusia (kepercayaan pengguna terhadap sistem), bukan cuma dimensi teknis semata.

</details>

---

## Refleksi Penutup Modul 5

Modul 5 ini menunjukkan bahwa "merawat Solusi AI" mencakup spektrum yang lebih luas dari yang mungkin kamu bayangkan sebelum memulai kursus ini — dari retraining model karena masalah akurasi (Modul 4, dilanjutkan eksekusinya di L1-L2), hingga masalah infrastruktur murni seperti kapasitas server (studi kasus ini), hingga dimensi manusia seperti kepercayaan pengguna terhadap sistem. Keenam unit kompetensi yang sudah kamu pelajari sejak Modul 1 sekarang membentuk siklus lengkap: dari data yang masuk, terintegrasi, dipasang, dipantau, direncanakan perawatannya, hingga dirawat secara nyata.

Modul 6 — capstone kursus ini — akan membawamu menyusuri kembali seluruh siklus ini dalam satu audit menyeluruh.

---

## Ringkasan Modul 5

- Merawat Solusi AI mencakup lebih dari sekadar model AI — termasuk infrastruktur, kapasitas komputasi, dan bahkan dimensi manusia seperti kepercayaan pengguna terhadap sistem.
- Pola masalah yang berulang dan bisa diprediksi (seperti lonjakan volume akhir bulan) sebaiknya ditangani dengan solusi preventif/terencana, bukan reaktif setiap kali insiden terjadi.
- Validasi hasil perawatan tetap wajib dilakukan terlepas dari jenis masalahnya (akurasi model atau infrastruktur) — "sudah dilakukan" tidak sama dengan "sudah terbukti berhasil".
- Dampak samping non-teknis (seperti perubahan perilaku pengguna akibat insiden) perlu ditangani sebagai bagian dari perawatan menyeluruh, bukan diabaikan setelah masalah teknis selesai.

---

## Navigasi

**[← M5-L2: Melakukan & Mendokumentasikan Perawatan](l2-melakukan-mendokumentasikan-perawatan)** | **[M6-L1: Menyeluruh Melihat Siklus Hidup Solusi AI →](../m6-audit-siklus-hidup/l1-menyeluruh-siklus-hidup)**
