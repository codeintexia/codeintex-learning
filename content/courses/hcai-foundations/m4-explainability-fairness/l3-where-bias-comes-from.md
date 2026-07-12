---
course: hcai-foundations
module: 4
module_title: "Explainability and Fairness in Practice"
lesson: 3
title: "Bias Datang dari Mana — dan Bagaimana Mendeteksinya Sebelum Terlambat"
duration_minutes: 14
bloom_level: analyze
keywords:
  - AI bias sources
  - dataset bias
  - algorithmic bias detection
  - bias in AI systems
  - pre-deployment bias audit
  - disaggregation AI metrics
is_free: true
status: draft
---

# Bias Datang dari Mana — dan Bagaimana Mendeteksinya Sebelum Terlambat

**Modul 4 · Explainability and Fairness in Practice** · Lesson 3 dari 4
**Estimasi waktu baca:** 14 menit · **Level:** Foundational · **Prasyarat:** M4-L2

---

> **Yang akan kamu capai di lesson ini:**
> - Menganalisis tiga sumber bias AI yang berbeda secara struktural — data, model, dan konteks deployment
> - Membedakan antara mendeteksi bias dan mendiagnosis akar penyebabnya
> - Mengidentifikasi kapan dalam siklus pengembangan setiap teknik deteksi bias paling efektif diterapkan

---

## Hook

Sebuah perusahaan asuransi kesehatan di Indonesia mengembangkan model AI untuk memprediksi risiko klaim — membantu menentukan premi yang "adil" berdasarkan profil risiko masing-masing calon nasabah.

Modelnya memiliki akurasi 89%. Tim data science bangga. Eksekutif menyebutnya sukses.

Enam bulan setelah peluncuran, seorang analis junior melakukan sesuatu yang tidak diminta: ia membagi data performa model berdasarkan profesi. Hasilnya mengejutkan. Model memprediksi klaim dengan sangat akurat untuk karyawan tetap dengan slip gaji formal — tapi secara konsisten *melebih-lebihkan* risiko untuk pekerja informal, pedagang pasar, dan pekerja lepas (freelancer).

Dampaknya: jutaan orang dalam ekonomi informal Indonesia — segmen terbesar angkatan kerja — membayar premi yang lebih tinggi dari yang seharusnya, atau ditolak secara implisit karena premi yang tidak terjangkau.

Model tidak pernah menggunakan "profesi informal" sebagai variabel. Tapi ia menggunakan pola pembayaran, lokasi, jenis rekening bank, dan puluhan variabel lain yang *berkorelasi* dengan informalitas pekerjaan. Hasilnya sama saja — diskriminasi tersembunyi di balik angka.

Tim tidak pernah memeriksa performa model berdasarkan segmen populasi. Mereka mengukur akurasi agregat dan berhenti di sana. **Angka agregat menyembunyikan ketidaksetaraan sampai seseorang bertanya pertanyaan yang tepat.**

---

## Kerangka Konseptual

### Tiga sumber bias yang berbeda secara struktural

Memahami *dari mana* bias datang adalah prasyarat untuk mengetahui *bagaimana* mengatasinya. Ketiga sumber ini membutuhkan respons yang berbeda:

**Sumber 1 — Bias data (historical bias):**
Data pelatihan mencerminkan dunia yang sudah tidak adil. Jika perekrutan historis mendiskriminasi perempuan, model yang dilatih pada data perekrutan itu akan belajar mendiskriminasi perempuan. Jika akses kredit historis tidak merata berdasarkan ras, model kredit akan mewarisi ketidakmerataan itu.

*Karakteristik:* Bias ini ada di data *sebelum* model dibangun. Bahkan model yang "benar" secara teknis — yang belajar persis seperti yang seharusnya — akan menghasilkan prediksi yang bias jika datanya bias.

*Deteksi:* Audit komposisi data pelatihan. Periksa representasi kelompok berbeda. Bandingkan distribusi label di berbagai subkelompok.

**Sumber 2 — Bias model (algorithmic bias):**
Proses pelatihan atau arsitektur model itu sendiri memperkenalkan bias — bahkan ketika data tidak bias. Ini bisa terjadi karena pilihan fungsi loss, regularisasi, atau cara model menangani ketidakseimbangan kelas.

*Karakteristik:* Bias ini muncul *selama* proses pelatihan. Model mungkin belajar memberikan bobot lebih pada mayoritas dan mengabaikan minoritas karena itu mengoptimalkan metrik agregat.

*Deteksi:* Bandingkan performa model di subkelompok berbeda menggunakan metrik yang sama. Periksa apakah akurasi, false positive rate, dan false negative rate konsisten di semua kelompok.

**Sumber 3 — Bias konteks deployment (deployment bias):**
Model yang adil di laboratorium menjadi tidak adil di dunia nyata karena konteks penggunaan berbeda dari konteks pelatihan. Pengguna nyata berbeda dari pengguna yang diasumsikan. Kondisi nyata berbeda dari kondisi pelatihan.

*Karakteristik:* Bias ini muncul *setelah* model diluncurkan. Model pulse oximeter yang bias terhadap kulit gelap adalah contoh klasik — akurat di populasi yang diuji, tidak akurat di populasi yang menggunakannya.

*Deteksi:* Monitoring performa model secara berkelanjutan di populasi nyata, bukan hanya di data uji. Disagregasi metrik performa secara rutin.

### Disagregasi: teknik deteksi yang paling underused

Disagregasi adalah membagi metrik performa model berdasarkan subkelompok populasi — dan ini adalah teknik deteksi yang paling banyak direkomendasikan tapi paling jarang dipraktikkan.

Alasannya sederhana: metrik agregat terlihat baik bahkan ketika ada kelompok yang dirugikan secara masif.

Model dengan akurasi 89% bisa memiliki akurasi 94% untuk kelompok A dan 76% untuk kelompok B. Angka 89% tidak pernah menunjukkan ini sampai kamu bertanya.

Perlu diingat dari M3-L2: pilihan definisi fairness menentukan *apa* yang kita cari saat disagregasi. Menggunakan paritas demografis sebagai standar akan memunculkan pertanyaan berbeda dibanding menggunakan kesempatan setara — sehingga sebelum disagregasi, tim harus sudah memutuskan definisi fairness mana yang relevan untuk konteks sistem mereka.

Pertanyaan disagregasi yang minimal perlu ditanyakan untuk setiap sistem AI yang membuat keputusan tentang manusia:

- Apakah akurasi konsisten di semua kelompok demografis yang relevan?
- Apakah *jenis* kesalahan konsisten? (False positive vs false negative memiliki konsekuensi berbeda)
- Apakah ada subkelompok yang secara konsisten mendapat performa lebih buruk?

### Mendeteksi vs mendiagnosis: dua langkah yang berbeda

Ini adalah perbedaan yang sering tidak dibuat secara eksplisit:

**Deteksi** menjawab: *"Apakah ada bias?"* — menggunakan disagregasi dan perbandingan metrik.

**Diagnosis** menjawab: *"Bias ini berasal dari mana?"* — menggunakan analisis data, uji penghapusan fitur secara sistematis (menguji dampak menghapus atau menonaktifkan satu komponen dari model), dan pemeriksaan pipeline secara keseluruhan.

Tanpa diagnosis, intervensi bisa salah sasaran. Jika kamu mendeteksi bias tapi salah mengira sumbernya adalah model (padahal sumbernya adalah data), membangun ulang model tidak akan menyelesaikan masalah.

<!-- DIAGRAM: Tiga sumber bias dalam pipeline AI
     Render sebagai pipeline horizontal saat membangun UI.
     Tahap 1: Data collection → Bias historis (panah ke bawah: "inherited from world")
     Tahap 2: Model training → Bias algoritmik (panah ke bawah: "introduced during training")
     Tahap 3: Deployment → Bias konteks (panah ke bawah: "emerges in real world")
     Warna: tiap sumber bias berbeda, dengan label "Deteksi" dan "Respons" per sumber
-->

---

> **Quick Check** — Sebelum melanjutkan:
> *Kembali ke kasus perusahaan asuransi di hook. Dari tiga sumber bias — data, model, konteks deployment — mana yang paling mungkin menjadi sumber utama bias pada sistem itu? Dan apa yang perlu diperiksa untuk mengkonfirmasi diagnosis itu?*

---

## Analisis Kasus

Kasus asuransi adalah ilustrasi bias data yang mengalir menjadi bias deployment:

**Sumber**: Data historis sistem asuransi di Indonesia — seperti di banyak negara berkembang — mencerminkan akses layanan keuangan yang tidak merata. Pekerja informal historis kurang terdokumentasi, lebih sering ditolak, dan memiliki pola klaim yang berbeda bukan karena mereka lebih berisiko, melainkan karena mereka memiliki akses yang berbeda.

**Mengalir ke model**: Model belajar bahwa "pola yang terlihat seperti pekerja informal = risiko lebih tinggi" — bukan dari variabel eksplisit, tapi dari korelasi tersembunyi yang tertanam di puluhan variabel proksi.

**Menjadi deployment bias**: Di dunia nyata, model ini bekerja pada populasi yang 60%+ adalah pekerja informal — jauh lebih besar dari representasi mereka di data pelatihan, yang didominasi karyawan formal.

**Yang seharusnya dilakukan**: Disagregasi metrik performa berdasarkan jenis pekerjaan *sebelum* peluncuran. Pertanyaan sederhana: "Apakah false positive rate untuk pekerja informal sama dengan karyawan tetap?" — jika tidak, investigasi dimulai di sana.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Tambahkan "fairness gate" dalam proses peluncuran produk AI: sebelum launch, tim harus menjawab secara tertulis pertanyaan disagregasi untuk kelompok yang paling mungkin terdampak. Jika jawabannya belum diketahui karena belum pernah diperiksa, launch harus ditunda sampai ada jawaban.

**Jika kamu UX researcher atau designer:**
Dalam riset pengguna, pastikan sampel mencakup kelompok yang paling rentan terdampak — bukan hanya pengguna yang paling mudah direkrut. Pekerja informal, pengguna dengan literasi digital rendah, dan kelompok yang kurang terwakili dalam data historis adalah kelompok yang paling perlu ada dalam riset sebelum system diluncurkan.

**Jika kamu developer atau engineer:**
Disagregasi bukan analisis sekali jalan — ini adalah monitoring berkelanjutan. Setelah peluncuran, metrik performa harus dipantau secara rutin berdasarkan subkelompok, bukan hanya secara agregat. Drift dalam performa agregat mungkin tidak terlihat, tapi drift yang masif pada satu subkelompok bisa tersembunyi di baliknya.

---

## Pertanyaan Refleksi

> Analis junior yang menemukan bias dalam kasus asuransi melakukan sesuatu yang tidak diminta: ia *bertanya pertanyaan yang tepat*. Tidak ada yang mewajibkannya. Tidak ada proses yang memastikannya.
>
> **Di lingkungan kerja atau organisasi yang kamu kenal**, siapa yang bertanggung jawab untuk bertanya pertanyaan disagregasi? Apakah ada proses formal yang memastikan pertanyaan itu diajukan sebelum sistem diluncurkan — atau itu bergantung pada inisiatif individual?

---

## Ringkasan Lesson

- Tiga sumber bias yang berbeda secara struktural: bias data (dari dunia yang tidak adil), bias model (dari proses pelatihan), dan bias konteks deployment (dari ketidaksesuaian antara konteks pelatihan dan penggunaan nyata).
- Disagregasi adalah teknik deteksi paling fundamental: membagi metrik performa berdasarkan subkelompok. Angka agregat menyembunyikan ketidaksetaraan.
- Mendeteksi bias (ada atau tidak) berbeda dari mendiagnosis sumbernya (dari mana). Diagnosis yang salah menghasilkan intervensi yang tidak tepat sasaran.
- Lesson berikutnya akan menerapkan semua yang sudah dipelajari di M4 ke konteks nyata Asia Tenggara: bagaimana bias terwujud dalam sistem fintech dan rekrutmen di Indonesia.

---

## Referensi

- Barocas, S., & Selbst, A. D. (2016). Big data's disparate impact. *California Law Review*, 104(3), 671–732.
- Suresh, H., & Guttag, J. (2021). A framework for understanding sources of harm throughout the machine learning life cycle. *CRAFT '21: Proceedings of the 1st ACM Conference on Equity and Access in Algorithms, Mechanisms, and Optimization*.
- Mitchell, M., et al. (2019). Model cards for model reporting. *FAT* '19: Proceedings, 220–229.
- Buolamwini, J., & Gebru, T. (2018). Gender shades: Intersectional accuracy disparities in commercial gender classification. *ICML 2018 Proceedings*, 81, 1–15.
- World Bank. (2023). *Indonesia Economic Prospects: Making the Most of Indonesia's Digital Economy*. World Bank Group. — Data tentang informalitas tenaga kerja Indonesia.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
