---
title: 'Dari Rencana ke Aksi: Menyiapkan Perawatan'
course: ai-untuk-proses-data
module: 5
module_title: Merawat Solusi AI
lesson: 1
slug: l1-menyiapkan-perawatan
unit_kompetensi:
  - kode: J.62AIN00.017.1
    nama: Merawat Solusi AI
    elemen: >-
      Elemen 1: Menyiapkan perawatan dari Solusi AI berdasarkan rencana
      perawatan
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
- Memastikan hasil monitoring sistem sesuai kebutuhan perawatan komponen arsitektur lengkap
- Menentukan kebutuhan perawatan komponen arsitektur sesuai prosedur perawatan

**🌉 Dari Modul 4 ke Modul 5:** Rencana perawatan yang kamu susun di M4-L4 — dengan akar masalah, tindakan, prioritas, sumber daya, dan kriteria sukses yang jelas — sekarang siap dieksekusi. Modul 5 ini adalah tentang mengubah rencana di atas kertas menjadi tindakan nyata.

---

## Hook: Rencana yang Baik, Eksekusi yang Sering Terlupakan

Sebuah panduan mengenai siklus hidup proyek AI menyoroti sesuatu yang sering diabaikan organisasi: anggaran untuk perawatan (maintenance) sebaiknya direncanakan sekitar **15 hingga 25 persen dari biaya implementasi awal per tahun** — bukan sekadar biaya tambahan kecil yang bisa "diselesaikan nanti kalau ada waktu". Untuk sistem yang lebih kompleks, alokasi tambahan bahkan diperlukan untuk audit tata kelola secara berkala.

Angka ini penting karena mengungkap pola yang sering terjadi: organisasi menginvestasikan banyak sumber daya untuk membangun dan meluncurkan Solusi AI (Modul 2-3), menyusun rencana perawatan yang baik (Modul 4) — tapi kemudian **eksekusi perawatannya justru kekurangan sumber daya**, karena dianggap "sudah selesai" setelah rencana disusun.

Ini yang disebut sebagai kesenjangan eksekusi (execution gap) — jarak antara rencana yang bagus di atas kertas dan tindakan nyata yang benar-benar dijalankan secara konsisten. Bagi Solusi AI, kesenjangan ini berbahaya karena performa model terus bergerak (ingat data drift dari Modul 3) — rencana yang tidak segera dieksekusi menjadi rencana yang basi, dan masalah yang seharusnya bisa dicegah malah berkembang jadi krisis, persis seperti prinsip "sepuluh kali lebih mahal" yang kamu pelajari di M4-L3.

---

## Kerangka Konseptual: Elemen 1 — Menyiapkan Perawatan Berdasarkan Rencana

**1.1 — Hasil monitoring sistem dipastikan sesuai kebutuhan perawatan komponen arsitektur lengkap**

Sebelum eksekusi dimulai, pastikan dulu bahwa data monitoring yang mendasari rencana perawatan (dari Modul 4) masih relevan dan lengkap. Kalau rencana disusun berdasarkan data Bulan 3, tapi eksekusi baru dimulai Bulan 5, kondisi mungkin sudah berubah — perlu verifikasi ulang, bukan asumsi bahwa rencana lama masih 100% berlaku.

**1.2 — Kebutuhan perawatan komponen arsitektur ditentukan sesuai prosedur perawatan**

Ini tahap menerjemahkan rencana (yang sifatnya strategis) menjadi kebutuhan teknis konkret: komponen arsitektur mana yang akan disentuh (model, pipeline data, infrastruktur), sumber daya apa yang harus disiapkan sebelum eksekusi dimulai, dan siapa yang bertanggung jawab.

<!-- VISUAL PLACEHOLDER: Diagram alur — "Rencana Perawatan (Modul 4)" → "Verifikasi Kondisi Terkini Masih Relevan?" → jika ya "Siapkan Sumber Daya & Prosedur" → jika tidak "Perbarui Rencana Berdasarkan Data Terbaru" → keduanya bermuara ke "Siap Eksekusi (L2)" -->

### Kenapa Verifikasi Ulang Ini Penting untuk Solusi AI

Berbeda dari perawatan mesin fisik yang kondisinya relatif stabil antara waktu perencanaan dan eksekusi, Solusi AI beroperasi di lingkungan yang terus berubah — data baru terus masuk, kondisi bisnis terus bergeser. Rencana perawatan yang dibuat berdasarkan data satu titik waktu bisa jadi sudah tidak sepenuhnya akurat kalau eksekusinya tertunda. Ini bukan alasan untuk menunda-nunda karena "datanya akan berubah lagi" — justru sebaliknya, ini alasan untuk **mempercepat siklus dari rencana ke eksekusi**, sesuai semangat anggaran perawatan yang memadai dari hook di atas.

---

## Konteks SPKO: Menyiapkan Perawatan

Berdasarkan rencana perawatan dari M4-L4 (mengatasi penurunan recall dan F1-Score karena kemungkinan data drift dan pergeseran komposisi data):

| Langkah Persiapan | Tindakan |
|---|---|
| Verifikasi kondisi terkini | Cek apakah tren penurunan recall masih berlanjut sejak rencana disusun, atau sudah membaik/memburuk |
| Komponen yang disentuh | Model credit scoring (untuk retraining) dan pipeline data pelatihan (untuk memastikan representasi data nasabah tanpa riwayat kredit) |
| Sumber daya yang disiapkan | Akses ke data terbaru dari core banking, tim data science yang dialokasikan, waktu yang dijadwalkan untuk retraining dan validasi |
| Penanggung jawab | Ditentukan secara eksplisit — siapa yang mengeksekusi, siapa yang memvalidasi hasil |

---

## Quick Check

**Rencana perawatan SPKO disusun berdasarkan data Bulan 3, tapi karena keterbatasan sumber daya, eksekusinya baru bisa dimulai di Bulan 5. Apa yang harus dilakukan sebelum melanjutkan eksekusi berdasarkan rencana lama tersebut?**

<details>
<summary>Lihat jawaban</summary>

Verifikasi ulang kondisi terkini (KUK 1.1) — pastikan data monitoring dari Bulan 4-5 masih menunjukkan pola yang sama dengan yang mendasari rencana di Bulan 3. Kalau kondisinya sudah berubah signifikan (membaik, memburuk, atau muncul faktor baru), rencana perlu disesuaikan sebelum eksekusi, bukan dijalankan mentah-mentah berdasarkan data yang sudah usang dua bulan.
</details>

---

## Latihan Terstruktur (Simulasi Singkat)
**(Target: 10 menit)**

**Skenario:** Dua bulan setelah rencana perawatan SPKO disusun (M4-L4), tim baru siap mengeksekusi. Kamu memeriksa tiga kondisi berikut sebelum melanjutkan.

| Kondisi | Situasi |
|---|---|
| A | Data monitoring terbaru menunjukkan recall sudah membaik sedikit (dari 0.68 ke 0.72) tanpa intervensi apa pun — kemungkinan karena data drift mulai stabil dengan sendirinya |
| B | Tim data science yang direncanakan mengeksekusi retraining sudah dialokasikan ke proyek lain, belum ada pengganti |
| C | Data terbaru menunjukkan kondisi konsisten dengan rencana awal, semua sumber daya siap sesuai jadwal |

**Instruksi:** Tentukan (a) apakah rencana masih bisa dieksekusi langsung, (b) tindakan yang diperlukan. Kerjakan dalam 10 menit.

<details>
<summary>Lihat kunci jawaban</summary>

| Kondisi | Bisa Langsung Eksekusi? | Tindakan |
|---|---|---|
| A | Tidak — perlu evaluasi ulang | Meski membaik, perlu diverifikasi apakah ini pemulihan sementara atau tren jangka panjang sebelum menjalankan rencana retraining penuh; kondisi sudah berubah dari yang mendasari rencana awal |
| B | Tidak — kebutuhan sumber daya belum terpenuhi | Eskalasi kebutuhan sumber daya sebelum eksekusi dimulai (KUK 1.2 menuntut kebutuhan perawatan ditentukan sesuai prosedur, termasuk memastikan sumber daya tersedia) |
| C | Ya | Lanjutkan ke eksekusi (L2) sesuai rencana yang sudah disusun |

**Poin penilaian mandiri:** Kondisi A adalah yang paling mudah disalahartikan sebagai "tidak perlu tindakan lagi" — tapi perbaikan kecil tanpa intervensi bisa jadi kebetulan sementara, bukan bukti masalah sudah selesai dengan sendirinya.
</details>

---

## Analisis Kasus: Kembali ke Kesenjangan Eksekusi

Kondisi B dalam latihan di atas adalah ilustrasi persis dari kesenjangan eksekusi yang dibahas di hook — rencana sudah bagus, tapi sumber daya yang dijanjikan ternyata tidak tersedia saat dibutuhkan. Ini menegaskan kenapa anggaran dan alokasi sumber daya perawatan (15-25% dari biaya implementasi) perlu dikomitmenkan sejak awal sebagai bagian dari siklus hidup Solusi AI — bukan dianggap sebagai "nice to have" yang mudah dikorbankan saat ada prioritas lain yang mendesak.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Komitmenkan anggaran dan sumber daya perawatan sejak awal proyek (bukan setelah masalah muncul) — perlakukan ini sebagai bagian tak terpisahkan dari total cost of ownership Solusi AI, bukan biaya tambahan opsional.

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Rancang dashboard yang menunjukkan status rencana perawatan (belum dieksekusi, sedang berjalan, selesai) agar keterlambatan eksekusi seperti Kondisi B mudah terlihat oleh manajemen, bukan tersembunyi sampai masalah membesar.

**Bagi pengembang/petugas teknis (developer/engineer):**
Sebelum mengeksekusi rencana yang sudah "usang" beberapa minggu/bulan, selalu verifikasi ulang data terkini — jangan berasumsi kondisi yang mendasari rencana masih sama persis.

---

## Pertanyaan Refleksi

1. Di organisasimu, seberapa sering rencana perbaikan/perawatan yang sudah disetujui benar-benar dieksekusi tepat waktu, dibanding tertunda karena prioritas lain?
2. Kondisi A dalam latihan (perbaikan tanpa intervensi) adalah situasi yang menggoda untuk diabaikan. Bagaimana kamu akan meyakinkan tim atau manajemen bahwa verifikasi tetap diperlukan meski angka terlihat membaik?

---

## Ringkasan Lesson

- Elemen 1 menuntut verifikasi bahwa hasil monitoring masih relevan dengan kondisi terkini, dan penentuan kebutuhan perawatan komponen arsitektur secara konkret sebelum eksekusi dimulai.
- Kesenjangan eksekusi — jarak antara rencana yang baik dan tindakan nyata yang dijalankan — adalah risiko nyata yang sering diabaikan organisasi, dengan anggaran perawatan yang idealnya direncanakan 15-25% dari biaya implementasi awal per tahun.
- Solusi AI beroperasi di lingkungan yang terus berubah, sehingga rencana yang tertunda eksekusinya perlu diverifikasi ulang, bukan dijalankan berdasarkan asumsi bahwa kondisi masih sama seperti saat rencana disusun.

---

## Referensi

- Panduan mengenai siklus hidup proyek AI dari masalah bisnis hingga produksi dan perawatan, 2026.

---

## Navigasi

**[← M4-L4: Studi Kasus — Menyusun Rencana Perawatan SPKO](../m4-merencanakan-perawatan-solusi-ai/l4-studi-kasus-rencana-perawatan)** | **[M5-L2: Melakukan & Mendokumentasikan Perawatan →](l2-melakukan-mendokumentasikan-perawatan)**
