---
course: hcai-foundations
module: 2
module_title: "How People Think About and Trust AI"
lesson: 3
title: "Terlalu Percaya atau Tidak Percaya: Dua Cara Kepercayaan pada AI Bisa Salah Arah"
duration_minutes: 12
bloom_level: understand
keywords:
  - AI trust calibration
  - automation bias
  - algorithm aversion
  - overtrust AI
  - undertrust artificial intelligence
  - appropriate reliance AI
is_free: true
status: draft
---

# Terlalu Percaya atau Tidak Percaya: Dua Cara Kepercayaan pada AI Bisa Salah Arah

**Modul 2 · How People Think About and Trust AI** · Lesson 3 dari 4
**Estimasi waktu baca:** 12 menit · **Level:** Foundational · **Prasyarat:** M2-L1, M2-L2

---

> **Yang akan kamu capai di lesson ini:**
> - Membedakan overtrust (automation bias) dari undertrust (algorithm aversion) beserta mekanisme psikologis masing-masing
> - Menjelaskan konsep trust calibration dan mengapa ia lebih penting dari sekadar meningkatkan kepercayaan pengguna
> - Menginterpretasi faktor-faktor yang mempengaruhi di mana kepercayaan pengguna akan mendarat pada spektrum ini

---

## Hook

**Kasus A.** Seorang radiolog berpengalaman sedang memeriksa hasil CT scan pasien dengan gejala batuk berkepanjangan. Sistem AI diagnostic di kliniknya menandai satu area sebagai "low probability — tidak memerlukan tindak lanjut segera." Sang radiolog, yang sudah memeriksa ratusan hasil scan hari itu, menerima penilaian sistem itu. Pasien dipulangkan.

Enam minggu kemudian, pasien kembali dengan tumor yang sudah berkembang ke stadium yang lebih sulit ditangani. Area yang ditandai "low probability" oleh AI ternyata adalah tumor stadium awal yang terlewat.

**Kasus B.** Sebuah tim pengembang aplikasi fintech mengintegrasikan model AI untuk mendeteksi transaksi mencurigakan. Model ini telah divalidasi dengan akurasi 94%. Namun tim analis fraud menolak menggunakannya secara aktif — mereka hanya melihat alert AI sebagai "referensi kedua" yang mereka abaikan lebih sering daripada tidak. Setelah tiga bulan, analisis menunjukkan bahwa 40% kasus fraud yang terdeteksi AI tapi diabaikan analis ternyata adalah fraud nyata.

Dua kasus, dua tim profesional yang kompeten, dua keputusan yang merugikan. Dan keduanya berasal dari masalah yang berlawanan arah: **kepercayaan yang terlalu besar pada AI, dan kepercayaan yang terlalu kecil.**

---

## Kerangka Konseptual

### Trust calibration: tujuannya bukan kepercayaan yang tinggi

<!-- DIAGRAM: Spektrum Kalibrasi Kepercayaan pada AI
     Render sebagai SVG horizontal saat membangun UI.
     Sumbu horizontal: dari kiri (Undertrust) ke kanan (Overtrust)
     Tiga zona:
       Kiri:   "Undertrust / Keengganan algoritma" — warna merah/oranye
       Tengah: "Kalibrasi tepat / Appropriate reliance" — warna hijau (zona ideal)
       Kanan:  "Overtrust / Bias otomasi" — warna merah/oranye
     Tambahkan contoh posisi produk: 
       - Analis fraud (kasus B) → sisi undertrust
       - Radiolog (kasus A) → sisi overtrust
       - Target ideal → zona tengah
     Catatan: lebar zona tengah lebih sempit dari dua zona ekstrem
     untuk menunjukkan bahwa kalibrasi tepat adalah target yang presisi.
-->

Kesalahan umum dalam desain produk AI adalah mengasumsikan bahwa tujuan interaksi manusia-AI adalah *meningkatkan kepercayaan pengguna*. Formulasi ini salah — dan berbahaya.

Lee dan See (2004), dalam salah satu paper paling berpengaruh tentang kepercayaan manusia pada otomasi, mendefinisikan kepercayaan yang tepat bukan sebagai kepercayaan yang tinggi, melainkan sebagai **kalibrasi kepercayaan (trust calibration)** — kepercayaan yang proporsional dengan kemampuan dan keandalan sistem yang sebenarnya.

Sistem yang dipercaya terlalu tinggi *maupun* terlalu rendah sama-sama menghasilkan outcomes yang buruk. Yang ingin dicapai adalah *ketergantungan yang tepat (appropriate reliance)* — percaya ketika sistem reliabel untuk konteks itu, skeptis ketika tidak.

### Overtrust — Bias otomasi (automation bias): ketika kepercayaan melampaui kemampuan sistem

*Bias otomasi (automation bias)* adalah kecenderungan manusia untuk terlalu mengandalkan sistem otomasi — menerima rekomendasinya tanpa pemeriksaan kritis yang seharusnya dilakukan (Parasuraman & Manzey, 2010).

Perhatikan bagaimana agency gap dari lesson sebelumnya langsung menjadi kondisi yang memperbesar bias otomasi — ketika seseorang tidak tahu di mana batas otonomi sistem, mereka tidak tahu kapan harus mengambil alih. Bias otomasi adalah yang terjadi ketika gap itu tidak pernah ditutup.

Bias otomasi muncul dalam dua bentuk:
- **Kesalahan omisi (omission errors):** manusia gagal mendeteksi masalah karena mengasumsikan sistem sudah mendeteksinya
- **Kesalahan komisi (commission errors):** manusia mengikuti rekomendasi sistem yang salah tanpa pertanyaan

Kasus radiolog di hook adalah omission error klasik. Kelelahan kognitif setelah memeriksa ratusan scan membuat Sistem 1 (berpikir cepat) mengambil alih, dan sinyal "low probability" dari AI menjadi alasan yang cukup untuk tidak memeriksa lebih dalam.

Yang memperburuk automation bias:
- **Konsistensi performa sebelumnya:** sistem yang sering benar membuat orang kurang waspada ketika sistem salah
- **Antarmuka yang terlalu percaya diri:** output AI yang ditampilkan tanpa uncertainty indicator mendorong penerimaan tanpa pertanyaan
- **Beban kognitif tinggi:** ketika manusia kelelahan atau kewalahan, mereka lebih cenderung mendelegasikan keputusan ke sistem

### Undertrust — Keengganan algoritma (algorithm aversion): ketika kepercayaan lebih rendah dari yang seharusnya

Di arah yang berlawanan, *keengganan algoritma (algorithm aversion)* adalah fenomena di mana manusia menolak atau mengabaikan rekomendasi algoritma bahkan ketika algoritma itu terbukti lebih akurat dari penilaian manusia (Dietvorst, Logg & Massey, 2015).

Ini paradoks yang menarik: tunjukkan kepada orang bahwa sebuah algoritma lebih akurat dari intuisi mereka sendiri, dan alih-alih meningkatkan kepercayaan mereka pada algoritma, hal itu sering justru *menurunkannya*.

Alasannya? Ketika manusia melihat algoritma membuat satu kesalahan, mereka kehilangan kepercayaan secara tidak proporsional — jauh lebih cepat dari ketika mereka melihat manusia membuat kesalahan yang setara. Penelitian Dietvorst et al. menunjukkan bahwa orang lebih memaafkan kesalahan manusia dibanding kesalahan algoritma, bahkan ketika algoritma secara keseluruhan lebih akurat.

Kasus tim analis fraud di hook adalah algorithm aversion yang terselubung sebagai "kehati-hatian profesional." Kepercayaan yang terlalu rendah pada model yang divalidasi 94% akurat menghasilkan 40% fraud yang terlewat.

Faktor yang mendorong algorithm aversion:
- **Pengalaman melihat algoritma gagal** — bahkan satu kali
- **Ketidakmampuan melihat bagaimana algoritma bekerja** — algoritma yang tidak transparan sulit dipercaya
- **Ancaman pada identitas profesional** — "jika algoritma lebih akurat dari saya, apa nilai keahlian saya?"

---

> **Quick Check** — Sebelum melanjutkan:
> *Dari dua fenomena di atas — automation bias dan algorithm aversion — mana yang menurutmu lebih umum terjadi di konteks kerja atau industri yang kamu kenal? Dan kondisi apa yang paling mendorongnya?*

---

## Analisis Kasus

Menariknya, kedua kasus di hook memiliki satu benang merah yang sama dari sisi desain: **tidak ada satu pun sistem yang dirancang untuk secara aktif membantu penggunanya mengkalibrasi kepercayaan mereka.**

Sistem diagnostik radiologi hanya menampilkan penilaian tanpa menunjukkan: pada kondisi CT scan seperti apa sistem ini paling sering membuat kesalahan? Apakah kasus ini mirip dengan kondisi-kondisi di mana sistem historis-nya kurang akurat?

Sistem fraud detection hanya menghasilkan alert tanpa menunjukkan: mengapa transaksi ini dianggap mencurigakan? Faktor apa yang paling berkontribusi? Apakah pola ini mirip dengan kasus fraud yang sebelumnya terkonfirmasi?

Dalam kedua kasus, informasi yang dibutuhkan untuk trust calibration yang tepat *ada* di sistem — tapi tidak pernah ditampilkan kepada pengguna. Ini bukan kekurangan model AI. Ini adalah kekurangan desain interaksi yang bisa diperbaiki tanpa mengubah satu baris pun kode model.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Ukur trust calibration secara aktif dalam user research — bukan hanya *berapa banyak* pengguna mempercayai sistem, tapi *apakah kepercayaan mereka akurat*. Survei sederhana: "Seberapa sering kamu mengikuti rekomendasi sistem tanpa memeriksa ulang?" dikombinasikan dengan data aktual tentang akurasi sistem dalam konteks itu akan menunjukkan apakah pengguna over- atau under-trusting.

**Jika kamu UX researcher atau designer:**
Desain untuk *appropriate reliance*, bukan untuk kepercayaan tertinggi. Ini berarti: tampilkan uncertainty secara eksplisit, beri penjelasan singkat tentang dasar rekomendasi, dan buat friction yang bermakna di momen keputusan berisiko tinggi — bukan kemudahan tanpa refleksi.

**Jika kamu developer atau engineer:**
Salah satu investasi teknis dengan return tertinggi untuk trust calibration: **uncertainty quantification** — kemampuan sistem untuk melaporkan seberapa yakin ia tentang outputnya, bukan hanya outputnya sendiri. Ini adalah fitur teknis yang secara langsung mendukung tujuan desain "appropriate reliance."

---

## Pertanyaan Refleksi

> Pikirkan sebuah keputusan yang secara rutin dibuat di tempat kerja atau konteks yang kamu kenal, dan bayangkan ada sistem AI yang memberi rekomendasi untuk keputusan itu.
>
> **Tanpa melihat data apapun, tebak: apakah orang-orang di konteks itu cenderung overtrust atau undertrust sistem AI?** Faktor apa dari konteksnya yang mendorongmu ke tebakan itu?
>
> Kemudian tanyakan: apa yang perlu diubah — dalam desain sistem, dalam cara sistem dikomunikasikan, atau dalam proses kerja di sekitarnya — untuk mendorong mereka ke zona trust calibration yang tepat?

---

## Ringkasan Lesson

- Tujuan desain interaksi manusia-AI bukan kepercayaan yang tinggi, melainkan trust calibration — kepercayaan yang proporsional dengan kemampuan dan keandalan sistem yang sebenarnya.
- Overtrust (automation bias) terjadi ketika kepercayaan melampaui kemampuan sistem — pengguna gagal mendeteksi kesalahan atau mengikuti rekomendasi salah tanpa pertanyaan.
- Undertrust (algorithm aversion) terjadi ketika kepercayaan lebih rendah dari yang seharusnya — pengguna mengabaikan rekomendasi akurat karena ketidakpercayaan yang tidak proporsional.
- Kedua masalah seringkali bukan soal model AI, melainkan soal bagaimana sistem dikomunikasikan dan didesain untuk mendukung pengambilan keputusan manusia.
- Pada lesson berikutnya, kita akan melihat semua konsep modul ini dalam konteks yang sangat konkret dan lokal: bagaimana pengguna ojek online Indonesia membangun dan mengkalibrasi kepercayaan mereka pada rekomendasi AI.

---

## Referensi

- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50–80.
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors*, 52(3), 381–410.
- Dietvorst, B. J., Logg, J. M., & Massey, C. (2015). Algorithm aversion: People erroneously avoid algorithms after seeing them err. *Journal of Experimental Psychology: General*, 144(1), 114–126.
- Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. *Organizational Behavior and Human Decision Processes*, 151, 90–103.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
