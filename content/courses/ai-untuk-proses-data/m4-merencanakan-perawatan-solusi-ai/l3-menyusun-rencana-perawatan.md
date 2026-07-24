---
title: Menyusun Rencana Perawatan
course: ai-untuk-proses-data
module: 4
module_title: Merencanakan Perawatan Solusi AI
lesson: 3
slug: l3-menyusun-rencana-perawatan
unit_kompetensi:
  - kode: J.62AIN00.016.1
    nama: Merencanakan Perawatan Solusi AI
    elemen: 'Elemen 2: Menyusun rencana perawatan Solusi AI'
level: Foundational — Competency
kategori: Competency
bloom_level: Apply
durasi_menit: 30
durasi_baca_menit: 16
durasi_latihan_menit: 14
bahasa: Indonesia
duration_minutes: 16
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Di akhir lesson ini, kamu akan mampu:
- Membuat rencana perawatan berdasarkan hasil evaluasi monitoring
- Mendokumentasikan rencana perawatan sesuai standar dokumentasi

---

## Hook: Sepuluh Kali Lebih Mahal

Sebuah prinsip yang sudah lama dikenal dalam manajemen aset dan sistem: **mengoperasikan peralatan atau sistem hingga benar-benar rusak bisa menghabiskan biaya hingga sepuluh kali lebih banyak** dibanding mengikuti jadwal perawatan preventif yang terencana. Prinsip ini berlaku luas — dari mesin pabrik hingga sistem IT, dan tidak terkecuali untuk Solusi AI.

Perbedaan mendasarnya sederhana: perawatan **reaktif** menunggu sampai ada yang benar-benar gagal sebelum bertindak — pada titik itu, kerusakan sudah terjadi, dampaknya sudah dirasakan, dan perbaikannya harus dilakukan dalam kondisi darurat yang mahal dan berisiko. Perawatan **preventif/terencana** bertindak berdasarkan sinyal-sinyal awal — seperti hasil evaluasi monitoring yang sudah kamu pelajari di L2 — sebelum masalah berkembang menjadi kegagalan penuh.

Ingat kembali temuan di L2: F1-Score SPKO turun dari target 0.85 menjadi 0.79. Ini adalah persis jenis sinyal awal yang membedakan organisasi yang merencanakan perawatan secara proaktif dari yang menunggu sampai nasabah mulai mengeluh secara masif atau regulator turun tangan. Lesson ini akan membawamu dari "mendeteksi ada masalah" (L2) ke "menyusun rencana konkret untuk menanganinya" — sebelum masalah itu berkembang jadi krisis yang sepuluh kali lebih mahal untuk diperbaiki.

---

## Kerangka Konseptual: Elemen 2 — Menyusun Rencana Perawatan Solusi AI

**2.1 — Rencana perawatan dibuat berdasarkan hasil evaluasi monitoring**

Rencana perawatan bukan daftar tindakan generik — ia harus secara langsung merespons temuan spesifik dari evaluasi monitoring (L2). Kalau F1-Score turun karena recall yang menurun tajam, rencana perawatan harus fokus ke situ — bukan tindakan umum yang tidak menyasar akar masalah.

**2.2 — Rencana perawatan didokumentasikan sesuai standar dokumentasi**

Sama seperti prosedur integrasi (Modul 2) dan deployment (Modul 3), rencana perawatan harus terdokumentasi formal — bukan sekadar kesepakatan lisan tim. Dokumentasi ini penting sebagai bukti kepatuhan sekaligus panduan konkret untuk tahap eksekusi di Modul 5.

### Elemen Kunci dalam Rencana Perawatan yang Baik

- **Akar masalah** — bukan cuma gejala (F1-Score turun), tapi penyebab yang mendasarinya (data drift? bug di pipeline data? perubahan kondisi ekonomi yang wajar?)
- **Tindakan spesifik** — retraining model? memperbaiki kualitas data sumber? menyesuaikan threshold keputusan?
- **Prioritas dan urgensi** — berdasarkan seberapa jauh performa menyimpang dan seberapa besar dampaknya
- **Sumber daya yang dibutuhkan** — waktu, tim, data tambahan yang diperlukan
- **Kriteria keberhasilan** — bagaimana kamu tahu perawatan ini berhasil? (kembali ke metrik kesuksesan dari L1-L2)

<!-- VISUAL PLACEHOLDER: Template dokumen rencana perawatan sederhana dengan kolom: Temuan Monitoring | Akar Masalah | Tindakan | Prioritas | Sumber Daya | Kriteria Sukses — mengilustrasikan struktur dokumentasi yang konkret -->

### Kenapa Rencana Perawatan Solusi AI Berbeda dari Perawatan Sistem Biasa

Perawatan sistem software biasa sering berarti "perbaiki bug, ganti komponen yang rusak". Perawatan Solusi AI lebih kompleks karena penyebab penurunan performa **belum tentu berupa "kerusakan" dalam arti tradisional** — modelnya mungkin masih berjalan sempurna secara teknis, tapi dunia nyata yang direpresentasikannya sudah berubah (data drift, seperti yang sudah kamu pelajari sejak Modul 3). Ini berarti "akar masalah" dalam rencana perawatan Solusi AI sering butuh investigasi yang lebih mendalam sebelum tindakan bisa ditentukan — tidak sesederhana "ganti komponen yang rusak".

---

## Konteks SPKO: Menyusun Rencana Perawatan

Berdasarkan temuan L2 (F1-Score turun ke 0.79, di bawah target 0.85):

| Elemen Rencana | Isi |
|---|---|
| Akar masalah | Perlu investigasi — kemungkinan data drift terkait perubahan kebijakan suku bunga OJK (seperti disebutkan di config kasus awal kursus ini) |
| Tindakan | Analisis distribusi data terbaru dibanding data pelatihan awal; jika terkonfirmasi drift, jadwalkan retraining model dengan data terbaru |
| Prioritas | Tinggi — penurunan F1-Score berkorelasi dengan kemungkinan keputusan kredit yang kurang akurat |
| Sumber daya | Tim data science untuk analisis drift, akses data terbaru dari core banking, waktu untuk retraining dan validasi ulang |
| Kriteria sukses | F1-Score kembali ke atau di atas 0.85 setelah retraining, tervalidasi dengan data uji terbaru |

---

## Quick Check
**(Target: 2 menit)**

**Tim SPKO menyusun rencana perawatan yang hanya berisi "perbaiki F1-Score" tanpa menyebutkan akar masalah, tindakan spesifik, atau kriteria sukses. Apa yang kurang dari rencana ini?**

<details>
<summary>Lihat jawaban</summary>

Rencana ini terlalu generik dan tidak actionable — tidak menjawab KUK 2.1 yang menuntut rencana berdasarkan hasil evaluasi monitoring secara spesifik. Tanpa akar masalah yang jelas, tim tidak tahu tindakan apa yang tepat (retraining? perbaikan data? penyesuaian threshold?). Tanpa kriteria sukses, tidak ada cara mengukur apakah perawatan berhasil. Rencana perawatan yang baik harus konkret dan bisa dieksekusi, bukan sekadar pernyataan niat.
</details>

---

## Latihan Terstruktur (Simulasi Singkat)
**(Target: 10 menit)**

**Skenario:** Berdasarkan tiga temuan monitoring berikut (dari latihan L2), susun elemen kunci rencana perawatan untuk masing-masing.

| Temuan | Detail |
|---|---|
| A | Recall turun dari 0.82 ke 0.71 dalam 2 bulan, berkorelasi dengan keluhan nasabah yang merasa ditolak kreditnya |
| C | Akurasi keseluruhan tinggi (94%) tapi recall untuk nasabah tanpa riwayat kredit turun signifikan |

**Instruksi:** Untuk masing-masing, tentukan (a) kemungkinan akar masalah, (b) tindakan awal yang diperlukan. Kerjakan dalam 10 menit.

<details>
<summary>Lihat kunci jawaban</summary>

| Temuan | Kemungkinan Akar Masalah | Tindakan Awal |
|---|---|---|
| A | Data drift akibat perubahan kondisi ekonomi, atau masalah kualitas data terbaru yang masuk ke model | Investigasi distribusi data 2 bulan terakhir dibanding data pelatihan; korelasikan dengan periode kebijakan ekonomi yang berubah; jadwalkan retraining jika drift terkonfirmasi |
| C | Model kekurangan representasi data pelatihan untuk kelompok nasabah tanpa riwayat kredit (data tidak seimbang) | Kumpulkan lebih banyak data pelatihan untuk kelompok ini secara spesifik; pertimbangkan teknik penyeimbangan data (seperti SMOTE yang disebut di penelitian L1); retraining dengan data yang lebih representatif |

**Poin penilaian mandiri:** Kalau rencana perawatanmu untuk kedua temuan ini identik ("retraining model" tanpa detail lebih lanjut), itu tanda rencana belum cukup spesifik — akar masalah keduanya berbeda (drift temporal vs data tidak seimbang), sehingga tindakannya pun seharusnya punya penekanan berbeda.
</details>

---

## Analisis Kasus: Kembali ke Prinsip "Sepuluh Kali Lebih Mahal"

Latihan di atas menunjukkan kenapa rencana perawatan yang terburu-buru atau generik berisiko menjadi perawatan yang gagal menyasar akar masalah — yang pada akhirnya berarti masalah yang sama akan muncul kembali, dan biaya penanganannya terus membengkak seiring waktu. Prinsip di hook menegaskan: investasi waktu untuk menyusun rencana yang tepat sasaran di tahap ini jauh lebih murah dibanding menghadapi krisis yang sudah berkembang penuh karena rencana yang asal-asalan.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Alokasikan waktu yang cukup untuk investigasi akar masalah sebelum menyetujui rencana perawatan — tekanan untuk "cepat memperbaiki" sering menghasilkan rencana yang menyasar gejala, bukan akar masalah.

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Rancang template dokumentasi rencana perawatan yang terstruktur (seperti tabel di atas) agar tim tidak melewatkan elemen penting seperti kriteria sukses — bukan dokumen bebas yang mudah jadi tidak lengkap.

**Bagi pengembang/petugas teknis (developer/engineer):**
Sebelum mengeksekusi retraining atau tindakan teknis lain, pastikan hipotesis akar masalah sudah diverifikasi dengan data — retraining model tanpa memahami akar masalah bisa jadi hanya menunda masalah yang sama muncul kembali.

---

## Pertanyaan Refleksi

1. Di organisasimu, seberapa sering rencana perawatan/perbaikan disusun berdasarkan investigasi akar masalah yang mendalam, dibanding tindakan cepat yang menyasar gejala saja?
2. Modul 4 ini menutup dengan rencana perawatan yang terdokumentasi. Menurutmu, informasi apa dari rencana ini yang paling penting dibawa ke Modul 5 (eksekusi perawatan)?

---

## Ringkasan Lesson

- Elemen 2 menuntut rencana perawatan yang dibuat berdasarkan hasil evaluasi monitoring secara spesifik dan didokumentasikan sesuai standar — bukan pernyataan niat generik.
- Prinsip "sepuluh kali lebih mahal" menegaskan nilai investasi waktu untuk perawatan preventif yang terencana, dibanding menunggu masalah berkembang jadi krisis reaktif.
- Rencana perawatan Solusi AI yang baik harus mengidentifikasi akar masalah (bukan cuma gejala), tindakan spesifik, prioritas, sumber daya, dan kriteria sukses yang terukur.

---

## Referensi

- Prinsip manajemen aset mengenai perbandingan biaya pemeliharaan preventif dan reaktif, literatur manajemen operasi.

---

## Navigasi

**[← M4-L2: Mengumpulkan & Mengevaluasi Hasil Monitoring](l2-mengumpulkan-mengevaluasi-monitoring)** | **[M4-L4: Studi Kasus — Menyusun Rencana Perawatan SPKO →](l4-studi-kasus-rencana-perawatan)**
