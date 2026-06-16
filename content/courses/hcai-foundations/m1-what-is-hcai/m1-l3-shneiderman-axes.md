---
course: hcai-foundations
module: 1
module_title: "What Is Human-Centered AI?"
lesson: 3
title: "Dua Sumbu Shneiderman: Cara Membaca Posisi Sistem AI Mana Pun"
duration_minutes: 12
bloom_level: remember
keywords:
  - Shneiderman HCAI two axes
  - AI reliability vs human control
  - HCAI quadrant
  - human oversight AI systems
  - AI autonomy spectrum
is_free: true
status: draft
---

# Dua Sumbu Shneiderman: Cara Membaca Posisi Sistem AI Mana Pun

**Modul 1 · What Is Human-Centered AI?** · Lesson 3 dari 4
**Estimasi waktu baca:** 12 menit · **Level:** Foundational · **Prasyarat:** M1-L1, M1-L2

---

> **Yang akan kamu capai di lesson ini:**
> - Mengidentifikasi posisi sebuah sistem AI pada dua sumbu Shneiderman: tingkat kontrol manusia dan tingkat keandalan
> - Menyebutkan karakteristik dan contoh dari keempat kuadran yang terbentuk
> - Membedakan kontrol nominal dari kontrol bermakna — dan mengapa perbedaan ini kritis dalam desain AI

---

## Hook

Pada malam 1 Juni 2009, Air France penerbangan 447 terbang di atas Samudra Atlantik dari Rio de Janeiro menuju Paris. Di ketinggian 11.000 meter, sensor kecepatan membeku karena kristal es. Autopilot — yang membutuhkan data kecepatan untuk bekerja — mati secara otomatis dan menyerahkan kendali kepada pilot.

Selama beberapa menit berikutnya, terjadi sesuatu yang kemudian dikaji oleh para peneliti human-computer interaction di seluruh dunia: para pilot, yang terbiasa memantau autopilot dan jarang menerbangkan pesawat secara manual di ketinggian itu, tidak segera memahami situasi yang sedang terjadi. Dalam kondisi panik dan kebingungan, salah satu kopilot secara konsisten menarik kemudi ke atas — respons yang justru membuat pesawat kehilangan daya angkat. Seluruh 228 penumpang dan awak tidak selamat.

Investigasi resmi menyimpulkan bahwa penyebab teknisnya adalah sensor yang membeku. Tapi laporan tersebut juga mencatat sesuatu yang lebih dalam: **sistem autopilot yang sangat diandalkan selama ini telah, tanpa disadari, mengikis kemampuan pilot untuk mengambil alih kendali saat sistem itu gagal.** Kepercayaan pada otomasi yang tinggi, dikombinasikan dengan kurangnya latihan manual, menciptakan titik buta yang fatal ketika reliabilitas sistem tiba-tiba turun.

Kasus ini bukan tentang teknologi yang terlalu canggih. Ini tentang dua variabel yang tidak pernah didesain secara bersamaan: **seberapa andal sistem itu**, dan **seberapa siap manusia untuk mengambil alih kendali ketika sistem itu tidak andal**.

Dua variabel inilah yang menjadi inti kerangka Shneiderman.

---

## Kerangka Konseptual

### Dua pertanyaan yang harus selalu ditanyakan bersama

Dalam *Human-Centered AI* (2022), Ben Shneiderman mengajukan bahwa setiap sistem AI bisa dipetakan pada dua sumbu yang terpisah namun saling terkait:

**Sumbu pertama: Tingkat Kontrol Manusia**
Seberapa besar kemampuan manusia untuk memantau, mengintervensi, mengoreksi, dan mengambil alih keputusan dari sistem AI? Di ujung kiri: sistem yang sepenuhnya otonom, beroperasi tanpa pengawasan manusia. Di ujung kanan: sistem di mana manusia memegang kendali penuh dan AI hanya memberi masukan.

**Sumbu kedua: Tingkat Keandalan Sistem**
Seberapa konsisten, akurat, aman, dan dapat diaudit sistem AI itu bekerja? Di ujung bawah: sistem yang sering salah, tidak bisa diprediksi, dan sulit diverifikasi. Di ujung atas: sistem yang konsisten, tervalidasi, dan hasil kerjanya bisa dijelaskan.

Dari dua sumbu ini, terbentuk empat kuadran yang masing-masing menggambarkan kondisi yang berbeda — dengan implikasi yang sangat berbeda pula.

### Empat kuadran: membaca kondisi sistem AI

<!-- DIAGRAM: Shneiderman HCAI Matrix
     Render sebagai SVG interaktif saat membangun UI.
     Sumbu X (horizontal): Tingkat Kontrol Manusia — Rendah (kiri) → Tinggi (kanan)
     Sumbu Y (vertikal):   Tingkat Keandalan Sistem — Rendah (bawah) → Tinggi (atas)
     Kuadran I   (kiri-bawah):  "Zona Berbahaya"            — warna merah
     Kuadran II  (kanan-bawah): "Zona Tidak Efisien"         — warna oranye
     Kuadran III (kiri-atas):   "Zona Otomasi Diterima"      — warna kuning
     Kuadran IV  (kanan-atas):  "Zona Ideal HCAI" ⭐         — warna hijau
     Tandai posisi contoh: GPS (III), Medical AI (IV), COMPAS (I), Spam Filter lama (II)
-->

**Kuadran I — Kontrol rendah, Keandalan rendah: Zona berbahaya**

Ini adalah kondisi terburuk: sistem yang sering salah *dan* tidak ada mekanisme yang memadai bagi manusia untuk mendeteksi atau mengoreksi kesalahan itu. Sistem beroperasi seperti kotak hitam — keputusan diambil tanpa transparansi, tanpa jejak audit, tanpa jalur banding yang jelas.

Contoh: sistem penilaian risiko kriminal yang digunakan di beberapa negara tanpa mekanisme pengawasan yang memadai, atau sistem moderasi konten otomatis yang memblokir akun tanpa proses banding yang dapat diakses pengguna.

Tidak ada alasan valid untuk menaruh sistem di kuadran ini. Keberadaannya hampir selalu merupakan hasil dari desain yang tidak mempertimbangkan manusia sama sekali.

**Kuadran II — Kontrol tinggi, Keandalan rendah: Zona tidak efisien**

Di sini, manusia memiliki kendali penuh — tapi sistem AI yang ada sering salah sehingga manusia harus terus-menerus memverifikasi, mengoreksi, dan membuang output yang tidak berguna. Secara teknis "aman" karena manusia selalu mengawasi, tapi tidak memberikan nilai nyata.

Contoh: sistem transkripsi otomatis yang akurasinya 60% sehingga editor harus mengoreksi hampir setiap kalimat, atau sistem deteksi fraud yang menghasilkan terlalu banyak false positive sehingga tim analis kewalahan memvalidasi alert.

Sistem di kuadran ini tidak berbahaya, tapi mereka menghabiskan kepercayaan dan waktu manusia tanpa memberikan manfaat yang sebanding.

**Kuadran III — Kontrol rendah, Keandalan tinggi: Zona otomasi yang bisa diterima**

Sistem yang sangat andal dan beroperasi dengan otonomi tinggi. Manusia tidak perlu aktif memantau setiap keputusan karena sistem terbukti bekerja dengan baik secara konsisten. Ini adalah zona di mana otomasi memang masuk akal.

Contoh: kalkulator, spell-checker, algoritma kompresi data, atau sistem autopilot dalam kondisi normal (bukan saat sensor membeku seperti AF447). Reliabilitasnya sudah tervalidasi secara ketat, taruhannya terkontrol, dan mekanisme failsafe tersedia.

Catatan penting: sistem hanya boleh berada di kuadran ini setelah melewati proses validasi yang ketat — bukan karena asumsi bahwa "AI sudah cukup canggih."

**Kuadran IV — Kontrol tinggi, Keandalan tinggi: Zona ideal Human-Centered AI**

Sistem yang andal *dan* manusia tetap memiliki kontrol bermakna atas keputusan yang penting. AI memberi rekomendasi, analisis, dan insight berkualitas tinggi — tapi manusia yang memutuskan, terutama untuk keputusan yang berdampak signifikan pada kehidupan orang.

Contoh: sistem pendukung keputusan medis yang memberi dokter daftar diagnosis diferensial yang terurut berdasarkan probabilitas, dengan penjelasan mengapa setiap diagnosis dipertimbangkan — tapi dokter yang membuat diagnosis akhir. Atau sistem AI legal yang mengidentifikasi preseden hukum relevan — tapi pengacara yang menganalisis dan menggunakannya dalam argumen.

### Mengapa "makin otonom makin baik" adalah asumsi yang salah

Salah satu kontribusi terpenting Shneiderman adalah membantah intuisi yang lazim di komunitas AI: bahwa tujuan akhir pengembangan AI adalah otonomi penuh — sistem yang bisa membuat semua keputusan sendiri tanpa campur tangan manusia.

Shneiderman berargumen sebaliknya. Untuk domain dengan taruhan tinggi — kesehatan, hukum, keuangan, keamanan publik — mempertahankan kontrol manusia yang bermakna bukan tanda kelemahan teknologi. Ini adalah desain yang bertanggung jawab.

Alasannya bukan hanya etika. Ini juga soal **kepercayaan jangka panjang**. Sistem yang memberi manusia kendali nyata atas keputusan penting cenderung diadopsi lebih luas, digunakan lebih bertanggung jawab, dan bertahan lebih lama — karena pengguna merasa sebagai mitra, bukan sebagai penonton.

---

> **Quick Check** — Sebelum melanjutkan:
> *Pikirkan satu sistem AI yang kamu gunakan minggu ini. Tanpa melihat dokumentasi apapun, coba tempatkan ia di salah satu dari empat kuadran: Berbahaya, Tidak Efisien, Otomasi Diterima, atau Ideal HCAI. Apa yang membuatmu memilih kuadran itu?*

---

## Analisis Kasus

Mari kita petakan beberapa sistem AI yang mungkin kamu kenal pada kerangka ini.

**Rekomendasi konten di platform streaming (Netflix, Spotify, TikTok):**
Keandalan tinggi dalam arti teknis — algoritmanya sangat efektif memprediksi konten yang akan ditonton atau didengarkan. Kontrol manusia rendah dalam arti substansial — pengguna tidak tahu mengapa konten tertentu direkomendasikan, dan sulit secara aktif membentuk ulang preferensinya. Posisi: antara Kuadran III dan batas berbahaya jika algoritma mulai membentuk preferensi pengguna secara tidak transparan.

**Sistem kredit scoring di fintech Indonesia:**
Banyak sistem kredit berbasis AI di Indonesia menggunakan data yang sangat luas — dari riwayat transaksi hingga pola penggunaan aplikasi. Keandalan teknis bervariasi. Kontrol manusia sangat rendah — pengguna sering tidak tahu faktor apa yang memengaruhi keputusan, tidak ada mekanisme banding yang efektif, dan keputusan bisa berdampak signifikan pada akses keuangan seseorang. Posisi: Kuadran I atau II, tergantung akurasi sistemnya. Ini adalah contoh di mana regulasi seharusnya mendorong pergeseran menuju Kuadran IV.

**Asisten AI percakapan (ChatGPT, Gemini, dan sejenisnya):**
Kontrol manusia tinggi — pengguna bisa menolak, mengoreksi, atau mengabaikan output kapan saja. Keandalan bervariasi tergantung topik dan cara penggunaan. Posisi: Kuadran IV ketika digunakan dengan literasi yang baik, bisa merosot ke Kuadran II ketika pengguna tidak tahu cara memverifikasi output.

Pemetaan ini menunjukkan sesuatu penting: **posisi sistem di kuadran bukan hanya soal desain teknisnya, tapi juga soal bagaimana ia digunakan dan oleh siapa.**

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Sebelum meluncurkan fitur AI apapun, lakukan pemetaan sederhana: di mana posisinya pada dua sumbu Shneiderman? Apakah levelnya sesuai dengan taruhan keputusan yang dihasilkan? Fitur rekomendasi produk dengan keandalan sedang bisa diterima di Kuadran III. Fitur yang memengaruhi akses kredit atau kesehatan pengguna harus berada di Kuadran IV — atau tidak diluncurkan sama sekali.

**Jika kamu UX researcher atau designer:**
Ketika melakukan riset pengguna untuk produk AI, tambahkan satu pertanyaan eksplisit: *"Seberapa yakin pengguna tentang kapan mereka harus mempercayai sistem, dan kapan harus mempertanyakannya?"* Kesenjangan antara kepercayaan yang diberikan pengguna dan keandalan sistem yang sesungguhnya adalah salah satu sumber risiko terbesar dalam desain AI.

**Jika kamu developer atau engineer:**
Setiap kali ada diskusi tentang "meningkatkan otomasi" atau "mengurangi intervensi manusia" dalam pipeline AI, tanyakan dua hal: *Apakah keandalan sistem sudah tervalidasi untuk level otonomi yang diinginkan?* dan *Apakah mekanisme kontrol manusia yang bermakna tetap tersedia jika sistem gagal?* Kedua pertanyaan ini harus dijawab sebelum otonomi ditingkatkan — bukan setelahnya.

---

## Pertanyaan Refleksi

> Ambil satu sistem AI yang sedang kamu kerjakan atau gunakan secara profesional.
>
> **Petakan secara jujur: di kuadran mana ia berada sekarang?**
>
> Kemudian tanyakan: apakah posisi itu sesuai dengan tingkat taruhan keputusan yang dihasilkan sistem itu? Kalau ada ketidaksesuaian — sistem terlalu otonom untuk taruhannya, atau kontrol manusia terlalu rendah untuk tingkat keandalannya — itulah titik intervensi desain yang paling mendesak.

---

## Ringkasan Lesson

- Kerangka Shneiderman memetakan sistem AI pada dua sumbu: tingkat kontrol manusia dan tingkat keandalan sistem.
- Empat kuadran yang terbentuk menggambarkan kondisi mulai dari yang berbahaya (kontrol rendah + keandalan rendah) hingga ideal (kontrol tinggi + keandalan tinggi).
- Otonomi penuh bukan tujuan akhir desain AI yang baik — keseimbangan yang tepat antara otonomi dan kontrol manusia bergantung pada konteks dan taruhan keputusan.
- Posisi sistem di kuadran bukan hanya ditentukan oleh desain teknisnya, tapi juga oleh bagaimana ia digunakan — dan ini membuka peran penting bagi desainer, researcher, dan product manager dalam membentuk posisi itu.
- Pada lesson berikutnya, kita akan menggunakan kerangka ini sebagai titik masuk untuk memperkenalkan empat prinsip HCAI yang akan memandu seluruh kursus.

---

## Referensi

- Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press. — Bab 2–4.
- Bureau d'Enquêtes et d'Analyses (BEA). (2012). *Final Report on the Accident on 1st June 2009 to the Airbus A330-203 operated by Air France — Flight AF 447*. BEA France.
- Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics*, 30(3), 286–297.
- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50–80.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
