---
course: hcai-foundations
module: 2
module_title: "How People Think About and Trust AI"
lesson: 4
title: "Studi Kasus: Ketika Pengguna Ojek Online Indonesia Tidak Percaya Saran Rute AI"
duration_minutes: 14
bloom_level: understand
keywords:
  - ride-hailing AI UX Indonesia
  - Gojek Grab AI trust
  - local AI case study Indonesia
  - AI trust Southeast Asia
  - mobility AI user behavior
is_free: true
status: draft
---

# Studi Kasus: Ketika Pengguna Ojek Online Indonesia Tidak Percaya Saran Rute AI

**Modul 2 · How People Think About and Trust AI** · Lesson 4 dari 4
**Estimasi waktu baca:** 14 menit · **Level:** Foundational · **Prasyarat:** M2-L1, M2-L2, M2-L3

---

> **Yang akan kamu capai di lesson ini:**
> - Menginterpretasi konsep mental model, gap, dan trust calibration dari M2-L1 s/d M2-L3 melalui konteks nyata di Indonesia
> - Menjelaskan mengapa konteks lokal — budaya, infrastruktur, dan dinamika sosial — secara signifikan mempengaruhi kepercayaan pengguna pada AI
> - Mendeskripsikan implikasi desain spesifik yang muncul dari analisis kasus ini

---

## Hook

Seorang pengemudi ojek online di Jakarta, sebut saja Pak Rudi, sudah mengemudi selama tiga tahun. Ia hapal rute-rute di kawasan Sudirman, Kuningan, dan Gatot Subroto seperti hapal nama anggota keluarganya. Ia tahu jalan mana yang macet jam berapa. Ia tahu gang kecil mana yang bisa memotong waktu sepuluh menit di jam sibuk.

Ketika aplikasi merekomendasikan rute yang berbeda dari yang ia rencanakan, Pak Rudi hampir selalu mengabaikannya.

Bukan karena ia tidak tahu cara menggunakan teknologi. Bukan karena ia anti-AI. Melainkan karena ia pernah beberapa kali mengikuti rekomendasi aplikasi dan tiba-tiba terjebak di kemacetan yang seharusnya bisa dihindari — kemacetan yang "tidak ada" di peta digital tapi sangat nyata di jalanan. Ia menarik kesimpulan yang masuk akal secara empiris: *"Aplikasi tidak tahu kondisi jalan sebenarnya."*

Kesimpulan itu tidak sepenuhnya salah. Tapi juga tidak sepenuhnya benar. Dan di antara ketidakakuratan itulah, ada pelajaran yang sangat kaya tentang bagaimana manusia membangun kepercayaan pada AI — dan mengapa desain yang tidak mempertimbangkan konteks lokal akan selalu menghasilkan trust gap yang mahal.

---

## Kerangka Konseptual

### Mengapa konteks lokal penting untuk kepercayaan pada AI

Sebagian besar penelitian tentang trust dalam sistem AI dilakukan di laboratorium di Amerika Serikat atau Eropa, dengan partisipan yang sebagian besar adalah mahasiswa universitas dengan akses internet stabil, infrastruktur yang relatif dapat diprediksi, dan literasi digital yang tinggi.

Indonesia adalah konteks yang sangat berbeda — dan perbedaan itu bukan hanya soal infrastruktur teknis. Ia menyentuh cara manusia membangun kepercayaan secara fundamental.

**Dimensi 1 — Ketidakpastian infrastruktur**

Sistem AI navigasi dirancang untuk dunia yang relatif dapat diprediksi: jalan-jalan yang statusnya konsisten, data lalu lintas yang akurat dan real-time, kondisi yang berubah secara perlahan. Jakarta — dan banyak kota besar Indonesia — adalah konteks di mana kondisi jalan bisa berubah dramatis dalam hitungan menit karena banjir mendadak, demo spontan, proyek konstruksi dadakan, atau pasar tumpah yang tidak terjadwal.

Sistem AI yang akurat secara rata-rata tapi gagal secara dramatis dalam kondisi-kondisi ekstrem ini akan, secara rasional, menghasilkan undertrust. Pengguna yang pernah mengalami kegagalan dramatis akan mengkalibrasi kepercayaan mereka ke bawah secara tidak proporsional — persis seperti algorithm aversion yang kita pelajari di lesson sebelumnya.

**Dimensi 2 — Pengetahuan lokal sebagai sumber identitas profesional**

Untuk Pak Rudi dan ribuan pengemudi ojek online lainnya, pengetahuan tentang kota bukan hanya keahlian teknis — ini adalah sumber kebanggaan profesional dan keunggulan kompetitif. Mengikuti rekomendasi aplikasi secara membabi buta, dari sudut pandang ini, bukan efisiensi — ini adalah pengakuan bahwa pengetahuan yang dibangun bertahun-tahun tidak bernilai.

Ini adalah dimensi algorithm aversion yang jarang dibahas dalam literatur akademik barat: ancaman pada identitas profesional sebagai penghambat kepercayaan pada AI. Di konteks kerja di mana keahlian manusia adalah sumber daya utama, AI yang terasa "menggantikan" penilaian manusia akan menghadapi resistensi yang jauh lebih kuat dari AI yang terasa "mendukung" penilaian manusia.

**Dimensi 3 — Kepercayaan berbasis relasi, bukan sistem**

Penelitian lintas budaya tentang kepercayaan menunjukkan bahwa budaya kolektif — di mana relasi personal dan reputasi komunal lebih penting dari aturan institusional — cenderung membangun kepercayaan melalui hubungan personal, bukan melalui sertifikasi sistem atau statistik validasi (Yuki et al., 2005).

Ketika sebuah aplikasi ojek online menampilkan bahwa "algoritma kami memiliki akurasi 95%," pesan ini mungkin efektif untuk audiens yang terbiasa dengan jaminan institusional berbasis data. Untuk audiens yang kepercayaannya dibangun melalui pengalaman personal dan rekomendasi dari orang yang dikenal, angka ini tidak berbicara dalam bahasa yang bermakna.

---

> **Quick Check** — Sebelum melanjutkan:
> *Dari tiga dimensi di atas — ketidakpastian infrastruktur, pengetahuan sebagai identitas, dan kepercayaan berbasis relasi — mana yang menurutmu paling sering diabaikan oleh tim pengembang produk AI yang berbasis di luar Indonesia?*

---

## Analisis Kasus: Menerapkan Kerangka M2

Mari kita terapkan tiga konsep yang sudah kita pelajari di modul ini untuk menganalisis kasus Pak Rudi secara sistematis.

### Mental model gap (dari M2-L2)

**Capability gap:** Pak Rudi kemungkinan memiliki mental model bahwa sistem navigasi "tidak tahu kondisi jalan real-time" — yang parsial benar. Yang ia mungkin tidak tahu adalah bahwa sistem sebenarnya menggunakan data crowdsourced dari ribuan pengguna aktif lain, yang berarti kondisi jalan yang sering dilalui banyak orang relatif akurat, sementara gang kecil yang jarang dilalui memang kurang akurat.

Perbedaan reliabilitas berdasarkan densitas pengguna adalah informasi yang sangat relevan untuk trust calibration — tapi tidak pernah ditampilkan kepada pengguna secara eksplisit.

**Transparency gap:** Pak Rudi tidak tahu *mengapa* sistem merekomendasikan rute tertentu pada momen tertentu. Apakah karena ada insiden lalu lintas yang baru dilaporkan? Karena data historis menunjukkan kemacetan di rute biasanya pada jam ini? Karena ada perubahan status jalan?

Tanpa informasi ini, setiap rekomendasi terasa seperti keputusan yang tidak bisa diverifikasi — dan ketika sekali ternyata salah, tidak ada cara untuk memahami *mengapa* salah, sehingga tidak ada update yang bermakna pada mental model.

### Trust calibration (dari M2-L3)

Pak Rudi ada dalam zona undertrust — algorithm aversion yang terbentuk dari pengalaman kegagalan yang tidak proporsional. Ini bukan irasional. Ini adalah Bayesian updating yang masuk akal berdasarkan informasi yang tersedia untuknya.

Yang menarik adalah: sistem navigasi kemungkinan besar lebih akurat dari intuisi Pak Rudi untuk rute-rute yang ia tidak hafal di luar kawasan kerjanya — tapi karena ia hanya bekerja di kawasan yang ia hafal, ia tidak pernah mendapat pengalaman di mana sistem navigasi secara jelas lebih baik dari pengetahuannya sendiri.

Ini adalah bentuk asimetri pengalaman — kepercayaan yang terkalibrasi secara tidak proporsional bukan karena pengguna irasional, melainkan karena pengalaman yang tersedia secara alami hanya menunjukkan satu sisi kemampuan sistem.

### Apa yang bisa didesain berbeda?

Berdasarkan analisis ini, setidaknya tiga intervensi desain yang bisa membantu:

**1. Tampilkan sumber rekomendasi secara ringkas**
"Rute ini disarankan karena ada laporan kemacetan di Jl. Sudirman dari 847 pengguna aktif 10 menit lalu" jauh lebih persuasif dan membangun mental model yang akurat dibanding sekadar garis biru di peta.

**2. Akui keterbatasan sistem secara eksplisit**
"Untuk rute di gang kecil yang kurang sering dilalui, akurasi estimasi waktu bisa lebih rendah" adalah pesan yang menurunkan ekspektasi di tempat yang tepat — dan secara paradoks meningkatkan kepercayaan di tempat lain karena sistem terlihat jujur tentang batasnya.

**3. Jadikan pengalaman pengemudi sebagai input, bukan hanya output**
Jika pengemudi berpengalaman seperti Pak Rudi bisa melaporkan kondisi jalan dengan mudah dan melihat kontribusinya secara eksplisit dalam rekomendasi untuk pengguna lain, sistem berubah dari "sesuatu yang menggantikan penilaiannya" menjadi "sesuatu yang diperkuat oleh penilaiannya." Ini secara langsung mengubah dinamika algorithm aversion.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Jangan impor assumption tentang kepercayaan dari literatur atau produk yang dikembangkan di konteks berbeda. Riset trust calibration harus dilakukan secara lokal, dengan pengguna lokal, dalam konteks lokal. Pertanyaan *"apakah pengguna mempercayai sistem kami?"* tidak bisa dijawab dengan data dari pasar lain.

**Jika kamu UX researcher atau designer:**
Ketika melakukan riset pengguna untuk produk AI di Indonesia, tambahkan pertanyaan eksplisit tentang dimensi lokal: "Bagaimana kamu memutuskan kapan harus percaya dan kapan tidak?" dan "Ceritakan pengalaman ketika sistem memberimu saran yang ternyata salah." Narasi pengalaman kegagalan seringkali mengungkap lebih banyak tentang trust gap daripada survei kepuasan.

**Jika kamu developer atau engineer:**
Data tentang rute yang sering diabaikan pengguna adalah sinyal berharga yang seringkali tidak dianalisis. Jika pengemudi berpengalaman secara konsisten mengabaikan rekomendasi tertentu, itu bisa berarti dua hal: (1) model memang kurang akurat untuk konteks itu, atau (2) ada trust gap yang perlu diatasi melalui desain komunikasi. Keduanya penting dan bisa dibedakan melalui analisis data yang tepat.

---

## Pertanyaan Refleksi

> Kamu baru saja mempelajari bagaimana konteks lokal — infrastruktur, identitas profesional, budaya kepercayaan — secara fundamental mempengaruhi bagaimana pengguna membangun dan mengkalibrasi kepercayaan mereka pada AI.
>
> **Pikirkan satu produk atau layanan AI yang digunakan di Indonesia** — bisa e-commerce, fintech, layanan pemerintah digital, atau lainnya.
>
> Dimensi konteks lokal mana yang paling mungkin menciptakan trust gap dalam produk itu? Dan sebagai desainer atau pengembang, apa satu intervensi paling konkret yang bisa kamu lakukan untuk menutup gap itu?

---

## Ringkasan Modul 2

Kita telah menempuh empat lesson dalam Modul 2. Ini yang kita bangun bersama:

- **L1:** Kesalahpahaman tentang AI adalah output default dari cara otak manusia bekerja — melalui antropomorfisme, cognitive ease, dan efek black box. Ini bukan masalah pengguna; ini adalah brief desain.
- **L2:** Mental model pengguna tentang AI hampir selalu tidak lengkap dan miskalibrasi. Tiga jenis gap — capability, transparency, dan agency — bisa diidentifikasi dan diatasi melalui desain yang aktif membentuk representasi yang akurat.
- **L3:** Kepercayaan yang tepat bukan kepercayaan yang tinggi — melainkan trust calibration yang proporsional. Overtrust (automation bias) dan undertrust (algorithm aversion) adalah dua arah kegagalan yang sama-sama mahal.
- **L4:** Konteks lokal — khususnya di Indonesia — menciptakan dinamika kepercayaan yang tidak bisa disalin dari literatur atau produk barat. Riset dan desain harus bersifat kontekstual, bukan universal.

**Modul 3** akan membawa kita dari *bagaimana manusia berpikir tentang AI* ke *apa yang seharusnya sistem AI berikan kepada manusia* — dengan membahas keempat prinsip HCAI secara lebih mendalam: Transparency, Fairness, Control, dan Accountability.

---

## Referensi

- Yuki, M., et al. (2005). Cross-cultural differences in relationship- and group-based trust. *Personality and Social Psychology Bulletin*, 31(1), 48–62.
- Hofstede, G. (2001). *Culture's Consequences: Comparing Values, Behaviors, Institutions and Organizations Across Nations* (2nd ed.). Sage Publications. — Dimensi kolektivisme dan jarak kekuasaan Indonesia.
- Triandis, H. C. (1995). *Individualism and Collectivism*. Westview Press. — Fondasi teoritis kepercayaan berbasis relasi di budaya kolektif.
- Dietvorst, B. J., Logg, J. M., & Massey, C. (2015). Algorithm aversion. *Journal of Experimental Psychology: General*, 144(1), 114–126.
- Lee, J. D., & See, K. A. (2004). Trust in automation. *Human Factors*, 46(1), 50–80.
- Prasetyo, Y. T., et al. (2021). Factors affecting customer satisfaction and loyalty in online food delivery service during the COVID-19 pandemic. *Computers in Human Behavior*, 123. — Konteks kepercayaan digital di Indonesia.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
