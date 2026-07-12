---
course: hcai-foundations
module: 4
module_title: "Explainability and Fairness in Practice"
lesson: 4
title: "Studi Kasus: Menganalisis Bias Algoritma di Fintech dan Rekrutmen Asia Tenggara"
duration_minutes: 18
bloom_level: analyze
keywords:
  - AI bias Southeast Asia
  - fintech AI fairness Indonesia
  - algorithmic discrimination
  - gig economy AI bias
  - credit scoring bias Indonesia
is_free: true
status: draft
---

# Studi Kasus: Menganalisis Bias Algoritma di Fintech dan Rekrutmen Asia Tenggara

**Modul 4 · Explainability and Fairness in Practice** · Lesson 4 dari 4
**Estimasi waktu baca:** 18 menit · **Level:** Foundational · **Prasyarat:** M4-L3

---

> **Yang akan kamu capai di lesson ini:**
> - Menganalisis pola bias algoritma yang spesifik pada konteks ekonomi dan sosial Asia Tenggara
> - Membandingkan manifestasi bias yang berbeda antara domain fintech dan rekrutmen menggunakan kerangka dari M4-L3
> - Mengidentifikasi intervensi desain yang konkret untuk setiap jenis bias yang dianalisis

---

## Hook

2019. Seorang driver ojek online di Surabaya — sebut saja Pak Hendra — mendapat rating konsisten 4.8 dari 5.0 selama dua tahun. Ia hafal kota, responsif, dan mendapat ulasan positif dari ratusan penumpang.

Kemudian platform mengubah algoritma penilaian driver. Beberapa minggu setelah perubahan itu, pendapatan Pak Hendra turun 30% karena ia mulai jarang mendapat pesanan di waktu-waktu tertentu. Ia tidak mendapat notifikasi bahwa algoritma berubah. Tidak ada penjelasan. Tidak ada mekanisme banding.

Ketika ia menghubungi customer service, jawabannya: "Algoritma kami memastikan pencocokan yang optimal antara driver dan penumpang."

Pak Hendra tidak pernah tahu apa yang berubah, mengapa pendapatannya turun, atau apa yang bisa ia lakukan.

Ini bukan kasus tunggal. Ini adalah pola yang berulang di seluruh ekosistem platform digital Asia Tenggara — di mana keputusan algoritmik berdampak langsung pada pendapatan jutaan pekerja informal yang tidak memiliki mekanisme perlindungan yang setara dengan karyawan formal.

---

## Kerangka Konseptual

### Mengapa konteks Asia Tenggara menghasilkan pola bias yang khas

Sebelum menganalisis kasus Pak Hendra lebih dalam — yang akan kita lakukan secara menyeluruh di akhir lesson ini menggunakan semua kerangka dari M4 — kita perlu memahami tiga karakteristik konteks yang menjelaskan *mengapa* kasus seperti ini terjadi secara sistemik di Asia Tenggara, bukan hanya secara individual.

**Karakteristik 1 — Informalitas ekonomi yang besar:**
Di Indonesia, sekitar 60% angkatan kerja bekerja di sektor informal (BPS, 2023). Ini menciptakan populasi besar yang kurang terwakili dalam data formal — riwayat kredit, slip gaji, catatan pajak — yang sering menjadi input utama model AI.

Konsekuensi: model yang dilatih pada data formal akan secara sistematis kurang akurat untuk populasi informal yang besar ini. Ini adalah bias konteks deployment yang struktural, bukan kebetulan.

**Karakteristik 2 — Adopsi AI yang cepat tanpa regulasi yang setara:**
Asia Tenggara, terutama Indonesia, mengalami pertumbuhan fintech dan platform digital yang sangat cepat — seringkali jauh melampaui kapasitas regulasi untuk mengawasinya. Ini menciptakan kondisi di mana sistem AI dengan dampak besar beroperasi tanpa kewajiban transparansi atau fairness audit yang memadai.

**Karakteristik 3 — Asimetri kekuasaan platform-pekerja:**
Model platform seperti ojek online, marketplace, dan gig economy menciptakan ketergantungan ekonomi yang tinggi bagi pekerja platform — yang berarti dampak keputusan algoritmik sangat tidak proporsional dibanding konteks di mana banyak opsi tersedia.

### Analisis dua domain: fintech dan rekrutmen

**Domain 1 — Credit scoring di fintech Indonesia**

Ekosistem fintech di Indonesia berkembang pesat sebagian karena menjangkau segmen yang kurang terlayani perbankan tradisional (*underbanked* — yang tidak memiliki akses memadai ke layanan perbankan formal). Tapi cara model kredit dibangun sering menciptakan paradoks: sistem yang mengklaim memperluas akses justru mengeksklusikan populasi yang sama yang seharusnya dijangkau.

*Pola bias yang teridentifikasi:*

Penggunaan data alternatif — pola penggunaan aplikasi, kontak telepon, aktivitas media sosial — sebagai proksi (*proxy*) kredibilitas kredit membawa asumsi-asumsi yang belum divalidasi secara adil. Misalnya: jumlah kontak telepon sebagai proksi jaringan sosial yang digunakan beberapa model kredit secara tidak proporsional menguntungkan pengguna urban dengan konektivitas lebih luas.

Lokasi sebagai variabel — baik secara eksplisit atau sebagai proksi melalui kode pos, operator telepon, atau pola perjalanan — berkorelasi kuat dengan demografi dan pendapatan dengan cara yang bisa menghasilkan diskriminasi berbasis tempat tinggal yang masuk akal secara statistik tapi tidak adil secara sosial.

*Sumber bias:* Terutama bias data (data pelatihan yang tidak merepresentasikan populasi target) dan bias deployment (model yang bekerja baik untuk populasi tertentu digunakan untuk populasi yang berbeda).

*Menganalisis dengan kerangka M4-L3:* Deteksi membutuhkan disagregasi metrik performa (approval rate, default rate, false negative rate) berdasarkan pekerjaan, lokasi, dan jenis rekening. Diagnosis membutuhkan pemeriksaan korelasi antara variabel-variabel yang digunakan dan karakteristik demografis.

**Domain 2 — Rekrutmen berbasis AI di korporat Indonesia**

Adopsi ATS (*Applicant Tracking System*) dan screening berbasis AI di perusahaan Indonesia meningkat signifikan pasca-pandemi, terutama untuk rekrutmen volume tinggi. Tapi sebagian besar sistem ini diimpor dari vendor global yang tidak mengkalibrasi modelnya untuk konteks lokal.

*Pola bias yang teridentifikasi:*

Model yang dilatih pada pola rekrutmen sukses dari perusahaan di negara lain membawa asumsi tentang "kandidat ideal" yang tidak netral — pilihan universitas, nama, pola karir — yang mencerminkan biografi profesional dari konteks yang berbeda.

Bias bahasa: model pemrosesan bahasa alami (NLP, *Natural Language Processing*) yang memproses CV dan surat lamaran sering dioptimalkan untuk bahasa Inggris formal, menilai lebih rendah lamaran yang ditulis dalam Bahasa Indonesia atau menggunakan konvensi penulisan lokal — bukan karena kualitasnya lebih rendah, melainkan karena pelatihan model tidak mencakup representasi yang adil.

*Sumber bias:* Terutama bias data (pelatihan pada dataset yang tidak representatif untuk konteks Indonesia) dan bias model (arsitektur yang dioptimalkan untuk konteks tertentu).

*Menganalisis dengan kerangka M4-L3:* Deteksi membutuhkan audit statistik terhadap output sistem — apakah acceptance rate berbeda berdasarkan nama, universitas asal, atau bahasa penulisan lamaran?

---

> **Quick Check** — Sebelum melanjutkan:
> *Dari dua domain — fintech dan rekrutmen — mana yang menurutmu lebih sulit untuk diaudit dari sisi fairness, dan mengapa? Pertimbangkan ketersediaan data, kompleksitas intervensi, dan siapa yang memiliki insentif untuk melakukan audit.*

---

## Analisis Mendalam: Kasus Driver Platform

Kembali ke Pak Hendra. Mari kita dekonstruksi kasusnya menggunakan semua kerangka dari M4:

**Dari perspektif eksplanabilitas (M4-L1 dan L2):**
Pak Hendra tidak mendapat penjelasan apapun tentang perubahan yang memengaruhinya. Tidak ada penjelasan lokal (mengapa pendapatannya turun), tidak ada penjelasan kontrafaktual (apa yang bisa ia ubah), tidak ada penjelasan untuk audiens yang paling terdampak.

**Dari perspektif sumber bias (M4-L3):**
Perubahan algoritma yang berdampak pada pendapatan bisa berasal dari ketiga sumber sekaligus. Bias data: jika algoritma baru dilatih pada pola permintaan yang berubah selama pandemi, distribusi data mungkin bergeser. Bias model: perubahan bobot variabel tertentu. Bias deployment: model yang dioptimalkan untuk metrik platform (efisiensi pencocokan, meminimalkan cancellation) mungkin tidak dioptimalkan untuk keadilan pendapatan driver.

**Dari perspektif HCAI principles (M3):**
Transparency: tidak ada. Fairness: tidak bisa dievaluasi karena data tidak transparan. Human Control: sangat rendah — driver tidak punya mekanisme berarti untuk mempertanyakan keputusan algoritmik. Accountability: tidak ada entitas yang secara jelas bertanggung jawab atas dampak pada pendapatan driver.

**Apa intervensi yang konkret?**

Berdasarkan analisis ini, setidaknya tiga intervensi yang bisa diimplementasikan:

Pertama, notifikasi perubahan algoritma yang signifikan dengan penjelasan sederhana tentang apa yang berubah dan mengapa — setara dengan notifikasi perubahan syarat layanan tapi dalam bahasa yang bisa ditindaklanjuti.

Kedua, mekanisme banding untuk driver yang pendapatannya turun signifikan pasca perubahan algoritma — dengan jaminan review oleh manusia, bukan hanya bot.

Ketiga, disagregasi metrik performa algoritma berdasarkan karakteristik driver (senioritas, lokasi, jam kerja) sebagai bagian dari monitoring fairness yang berkelanjutan.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Jika produkmu beroperasi dalam ekonomi platform atau membuat keputusan kredit, tanyakan secara eksplisit: *"Apakah populasi yang paling bergantung pada produk kami adalah populasi yang paling terwakili dalam data pelatihan kami?"* Jika jawabannya tidak, kamu memiliki kesenjangan representasi yang perlu ditangani sebelum sistem berdampak pada kelompok yang sudah rentan.

**Jika kamu UX researcher atau designer:**
Lakukan "fairness walkthrough" — dokumentasi narasi tentang bagaimana sistem berdampak pada pengguna di segmen yang berbeda, termasuk mereka yang paling tidak terlihat dalam proses pengembangan biasa. Driver platform, pekerja informal, dan migran adalah segmen yang sering tidak hadir dalam riset pengguna standar tapi menanggung dampak terbesar.

**Jika kamu developer atau engineer:**
Untuk sistem yang beroperasi di konteks Asia Tenggara, anggap representasi yang tidak memadai untuk populasi informal sebagai *default assumption* sampai terbukti sebaliknya. Ini membalikkan beban pembuktian: bukan "apakah ada bias?" tapi "apakah kita sudah cukup memeriksa bahwa tidak ada bias?"

---

## Pertanyaan Refleksi

> Kasus-kasus di lesson ini adalah representasi dari pola yang terjadi setiap hari di seluruh Asia Tenggara, mempengaruhi jutaan orang yang tidak tahu bahwa keputusan tentang mereka dibuat oleh algoritma.
>
> **Dari sudut pandang peranmu** — PM, researcher, designer, atau engineer — satu perubahan konkret apa yang bisa kamu lakukan dalam 30 hari untuk membuat sistem yang kamu kerjakan lebih adil terhadap kelompok yang paling rentan terdampak?

---

## Ringkasan Modul 4

Kita telah menempuh empat lesson yang membangun kemampuan analisis tentang eksplanabilitas dan fairness dalam praktik:

- **L1:** Black box bukan takdir — tiga jenis penjelasan (global, lokal, kontrafaktual) dan cara memahami SHAP dan LIME secara intuitif.
- **L2:** Satu penjelasan tidak cukup untuk semua audiens — pengguna, pengembang, dan regulator membutuhkan jenis penjelasan yang berbeda fundamental, dan trade-off antara akurasi teknis dan aksesibilitas harus dikelola secara sadar.
- **L3:** Tiga sumber bias (data, model, deployment), disagregasi sebagai teknik deteksi utama, dan perbedaan antara deteksi dan diagnosis.
- **L4:** Pola bias spesifik di konteks Asia Tenggara — fintech, rekrutmen, dan platform — dengan analisis menggunakan semua kerangka yang sudah dibangun.

**Modul 5** akan membawa semua yang sudah dipelajari ke dalam proses desain: bagaimana IFRAME menjadi kerangka operasional untuk merancang sistem AI yang human-centered dari awal.

---

## Referensi

- BPS (Badan Pusat Statistik). (2023). *Keadaan Ketenagakerjaan Indonesia Agustus 2023*. BPS Indonesia.
- Datta, A., Tschantz, M. C., & Datta, A. (2015). Automated experiments on ad privacy settings. *Proceedings on Privacy Enhancing Technologies*, 2015(1), 92–112.
- Lee, M. K. (2018). Understanding perception of algorithmic decisions. *Big Data & Society*, 5(1).
- Irani, L., & Silberman, M. S. (2013). Turkopticon: Interrupting worker invisibility in Amazon Mechanical Turk. *CHI '13 Proceedings*, 611–620.
- Suresh, H., & Guttag, J. (2021). A framework for understanding sources of harm throughout the machine learning life cycle. *CRAFT '21 Proceedings*.
- Prasetyo, B., et al. (2022). Fintech lending in Indonesia: Access, risks, and regulation. *OECD Development Centre Working Papers*, No. 350.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
