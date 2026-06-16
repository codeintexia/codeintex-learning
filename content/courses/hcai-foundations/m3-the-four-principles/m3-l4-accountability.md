---
course: hcai-foundations
module: 3
module_title: "The Four Principles — What HCAI Demands"
lesson: 4
title: "Accountability: Ketika Ada yang Harus Bertanggung Jawab atas Keputusan AI"
duration_minutes: 12
bloom_level: understand
keywords:
  - AI accountability
  - responsible AI governance
  - AI who is responsible
  - many hands problem AI
  - AI audit trail
is_free: true
status: draft
---

# Accountability: Ketika Ada yang Harus Bertanggung Jawab atas Keputusan AI

**Modul 3 · The Four Principles — What HCAI Demands** · Lesson 4 dari 5
**Estimasi waktu baca:** 12 menit · **Level:** Foundational · **Prasyarat:** M3-L3

---

> **Yang akan kamu capai di lesson ini:**
> - Menjelaskan mengapa akuntabilitas AI lebih rumit dari akuntabilitas keputusan manusia, dan apa yang membuatnya sering tercerai-berai
> - Mengidentifikasi tiga level akuntabilitas — individual, organisasi, sistemik — beserta fungsi masing-masing
> - Mendeskripsikan mekanisme konkret yang bisa dibangun untuk memastikan akuntabilitas bermakna dalam sistem AI

---

## Hook

18 Maret 2018. Elaine Herzberg berjalan mendorong sepeda melalui penyeberangan jalan di Tempe, Arizona. Sebuah kendaraan otonom Uber menabraknya. Ia meninggal beberapa jam kemudian — menjadi korban jiwa pertama yang terdokumentasi dalam kecelakaan kendaraan otonom yang melibatkan pejalan kaki.

Yang terjadi setelahnya menjadi pelajaran paling jelas tentang apa yang terjadi ketika akuntabilitas tidak dirancang sejak awal.

Uber mengatakan sistem keamanan operator manusia — Rafaela Vasquez, yang duduk di kursi pengemudi — gagal menjalankan tugasnya. Rekaman menunjukkan Vasquez melihat ke bawah sesaat sebelum tabrakan.

Vasquez mengatakan ia tidak diberikan informasi yang cukup tentang kapan harus mengintervensi sistem otonom, dan bahwa tuntutannya untuk memantau layar sistem sambil siap mengambil alih kemudi kapan saja adalah permintaan yang melebihi kapasitas kognitif manusia.

Investigasi NTSB menemukan bahwa sistem Uber mendeteksi Herzberg 6 detik sebelum tabrakan tapi mengklasifikasikannya sebagai objek yang tidak perlu dihindari karena logika yang cacat dalam kode — dan kemudian sistem menghapus respons pengereman darurat karena konfigurasi yang dibuat oleh insinyur Uber untuk mengurangi "pengereman yang tidak perlu."

Siapa yang bertanggung jawab? Uber menyalahkan Vasquez. Vasquez menyalahkan Uber. Insinyur yang menulis kode penghapusan pengereman darurat tidak tahu kalau keputusan teknis mereka akan diterapkan di jalan publik tanpa pengujian yang memadai. Eksekutif yang menyetujui peluncuran di jalan publik tidak memahami detail teknis yang membuat sistem itu tidak aman.

Semua orang bisa menunjuk ke orang lain. Tidak ada satu pihak pun yang punya gambaran penuh atas semua keputusan yang, secara kumulatif, menyebabkan kematian Elaine Herzberg.

**Ini adalah "masalah banyak tangan" (many hands problem) dalam AI** — dan tanpa akuntabilitas yang dirancang secara eksplisit, ia adalah kondisi default.

---

## Kerangka Konseptual

### Mengapa akuntabilitas AI lebih rumit

Dalam keputusan yang dibuat manusia, rantai akuntabilitas relatif jelas: seseorang membuat keputusan, seseorang bisa dimintai pertanggungjawaban. Sistem AI memecah rantai ini menjadi fragmen yang tersebar di banyak tangan:

- Peneliti yang mengembangkan model
- Insinyur yang mengimplementasikannya
- Product manager yang mendefinisikan use case
- Eksekutif yang menyetujui peluncuran
- Operator yang menggunakannya sehari-hari
- Regulator yang (atau tidak) mengawasi

Ketika keputusan sistem AI menyebabkan kerugian, setiap pihak dalam rantai ini bisa berargumen bahwa mereka hanya bertanggung jawab atas komponen kecil mereka — dan tidak ada yang bertanggung jawab atas keseluruhan.

Nissenbaum (1994), dalam analisis seminalnya tentang akuntabilitas dalam sistem komputasi, menyebut ini sebagai "problem of many hands" — kondisi di mana tanggung jawab tersebar ke begitu banyak pihak sehingga tidak ada satu pun yang merasa bertanggung jawab penuh atas keseluruhan sistem.

### Tiga level akuntabilitas dalam sistem AI

Akuntabilitas yang efektif harus bekerja di tiga level sekaligus:

**Level 1 — Akuntabilitas individual:**
Siapa yang membuat keputusan spesifik yang berkontribusi pada hasil yang merugikan? Ini mencakup bukan hanya keputusan besar, tapi juga keputusan teknis kecil yang memiliki konsekuensi besar ketika digabungkan.

*Mekanisme:* Dokumentasi keputusan (*decision log*) yang mencatat siapa yang memutuskan apa, kapan, dan berdasarkan informasi apa. Ini bukan untuk mencari kambing hitam — tapi untuk memastikan setiap orang dalam rantai pengembangan memiliki kesadaran tentang konsekuensi potensial dari keputusan mereka.

**Level 2 — Akuntabilitas organisasi:**
Apakah organisasi sebagai entitas memiliki kebijakan, proses, dan struktur yang memadai untuk mencegah kerugian? Ini termasuk pertanyaan tentang insentif: apakah organisasi lebih menghargai kecepatan peluncuran atau keamanan sistem?

*Mekanisme:* Audit etika AI berkala, dewan pengawas independen, kebijakan yang mewajibkan penilaian risiko sebelum peluncuran di domain berisiko tinggi.

**Level 3 — Akuntabilitas sistemik:**
Apakah regulasi dan norma industri memadai untuk mengawasi penggunaan AI di domain ini? Ketika kegagalan individual dan organisasi berulang, ini sering menunjukkan kelemahan di level sistemik.

*Mekanisme:* Regulasi seperti EU AI Act yang mewajibkan audit pihak ketiga untuk sistem AI berisiko tinggi, standar industri yang bisa diaudit, dan mekanisme pelaporan publik.

<!-- DIAGRAM: Tiga Level Akuntabilitas AI
     Render sebagai diagram piramida atau lapisan bertingkat saat membangun UI.
     Atas (terkecil): Sistemik — regulasi, standar industri, pengawasan publik
     Tengah: Organisasi — kebijakan internal, proses review, insentif
     Bawah (terlebar): Individual — keputusan, dokumentasi, kesadaran konsekuensi
     Catatan: kegagalan di level bawah sering merupakan gejala dari kelemahan di level atas
     Warna: piramida teal, teks tiap level menjelaskan mekanisme utamanya
-->

### Mekanisme konkret untuk akuntabilitas bermakna

Empat mekanisme yang paling terbukti efektif dalam membangun akuntabilitas dalam sistem AI:

**1. Jejak audit (audit trail) yang bisa diakses**
Setiap keputusan sistem AI yang signifikan harus meninggalkan jejak yang bisa diperiksa: input apa yang digunakan, model versi berapa yang membuat keputusan, parameter apa yang aktif. Tanpa ini, investigasi setelah kegagalan tidak mungkin dilakukan secara akurat. Perhatikan koneksinya dengan Transparency dari L1 — jejak audit adalah implementasi paling konkret dari transparansi faktor dan transparansi proses dalam konteks akuntabilitas.

**2. Mekanisme banding yang nyata**
Orang yang terdampak oleh keputusan AI harus memiliki jalur yang jelas dan dapat diakses untuk mempertanyakan keputusan itu. Bukan hanya secara teoritis — tapi dengan timeline yang jelas, prosedur yang tidak berlebihan, dan jaminan bahwa banding akan ditinjau oleh manusia yang berwenang.

**3. Pengungkapan insiden (incident disclosure)**
Ketika sistem AI membuat kesalahan yang signifikan, ada insentif kuat untuk meminimalkan atau menyembunyikannya. Akuntabilitas yang bermakna membutuhkan budaya dan kebijakan yang mendorong pengungkapan insiden — bukan untuk menghukum, tapi untuk belajar dan memperbaiki secara sistematis.

**4. Penetapan tanggung jawab yang eksplisit**
Sebelum peluncuran, harus ada dokumen tertulis yang menjawab: *"Jika sistem ini membuat keputusan yang merugikan pengguna, siapa yang bertanggung jawab untuk merespons, menyelidiki, dan memberikan kompensasi?"* Ketidakjelasan di sini bukan ambiguitas yang netral — ini adalah risiko yang aktif.

---

> **Quick Check** — Sebelum melanjutkan:
> *Dari empat mekanisme akuntabilitas di atas — audit trail, mekanisme banding, incident disclosure, penetapan tanggung jawab eksplisit — mana yang paling sering absen dalam organisasi yang kamu kenal? Dan apa yang menghalangi keberadaannya?*

---

## Analisis Kasus

Kembali ke kasus Uber dengan kerangka tiga level:

**Akuntabilitas individual:** Vasquez dipidana karena kelalaian. Tapi keputusan yang lebih konsekuensial — menghapus pengereman darurat, meluncurkan di jalan publik tanpa pengujian memadai, mendefinisikan peran operator manusia dengan ambigu — dibuat oleh banyak individu yang tidak pernah dipidana dan yang sebagian besar tidak menyadari dampak penuh dari keputusan mereka. *Tidak berfungsi.*

**Akuntabilitas organisasi:** Uber tidak memiliki proses review keamanan yang memadai sebelum peluncuran di jalan publik. Insentif internal lebih menghargai kecepatan pengembangan teknologi otonom dibanding keamanan sistemik. *Tidak berfungsi.*

**Akuntabilitas sistemik:** Pada 2018, Arizona tidak memiliki regulasi memadai untuk kendaraan otonom di jalan publik. NHTSA tidak memiliki mandat pengawasan yang jelas untuk teknologi ini. *Tidak berfungsi.*

Semua tiga level gagal sekaligus. Dan hasilnya adalah kematian yang, berdasarkan investigasi NTSB, seharusnya bisa dicegah.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Sebelum meluncurkan fitur AI apapun, isi dokumen singkat ini: *"Jika fitur ini merugikan pengguna, siapa yang bertanggung jawab untuk (a) merespons dalam 24 jam, (b) menyelidiki dalam 7 hari, (c) memberikan kompensasi atau koreksi?"* Jika jawabannya tidak jelas, akuntabilitas belum ada.

**Jika kamu UX researcher atau designer:**
Rancang mekanisme banding sebagai bagian dari alur pengguna — bukan sebagai afterthought di halaman bantuan yang tersembunyi. Tombol "Pertanyakan keputusan ini" yang jelas dan aksesibel adalah fitur desain yang sama pentingnya dengan fitur utama produk.

**Jika kamu developer atau engineer:**
Bangun logging yang komprehensif sejak awal — bukan sebagai debugging tool, tapi sebagai infrastruktur akuntabilitas. Pertanyaan "apa yang sistem putuskan dan mengapa, pada tanggal dan waktu ini?" harus bisa dijawab dalam hitungan menit, bukan minggu investigasi.

---

## Pertanyaan Refleksi

> "Many hands problem" adalah kondisi default dalam pengembangan produk AI yang melibatkan banyak orang — dan hampir semua produk melibatkan banyak orang.
>
> **Dalam tim atau organisasimu**, jika sistem AI yang sedang dikembangkan membuat keputusan yang salah dan merugikan pengguna minggu depan — siapa yang akan kamu telepon? Apakah jawaban itu jelas bagi semua orang di tim, atau hanya bagi sebagian?

---

## Ringkasan Lesson

- Akuntabilitas AI lebih rumit dari akuntabilitas keputusan manusia karena "masalah banyak tangan" — tanggung jawab tersebar ke banyak pihak sehingga tidak ada yang merasa bertanggung jawab penuh.
- Tiga level akuntabilitas — individual, organisasi, sistemik — harus bekerja bersamaan. Kegagalan di satu level sering menunjukkan kelemahan di level lain.
- Empat mekanisme konkret: audit trail, mekanisme banding yang nyata, incident disclosure, dan penetapan tanggung jawab yang eksplisit sebelum peluncuran.
- Kasus Uber menunjukkan konsekuensi fatal ketika ketiga level akuntabilitas gagal sekaligus dalam sistem AI yang beroperasi di dunia nyata.
- Lesson berikutnya adalah latihan terapan: menggunakan keempat prinsip yang sudah kita pelajari untuk mengaudit satu produk AI nyata — persiapan langsung untuk capstone di Modul 6.

---

## Referensi

- Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press. — Bab 9.
- National Transportation Safety Board (NTSB). (2019). *Collision Between Vehicle Controlled by Developmental Automated Driving System and Pedestrian*. NTSB/HAR-19/03.
- Nissenbaum, H. (1994). Computing and accountability. *Communications of the ACM*, 37(1), 72–80.
- Mittelstadt, B., et al. (2016). The ethics of algorithms: Mapping the debate. *Big Data & Society*, 3(2).
- European Parliament. (2024). *Regulation (EU) 2024/1689 — Artificial Intelligence Act*. — Pasal 17–20 tentang kewajiban akuntabilitas sistem AI berisiko tinggi.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
