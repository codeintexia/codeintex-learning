---
course: hcai-foundations
module: 1
module_title: "What Is Human-Centered AI?"
lesson: 4
title: "Empat Prinsip HCAI — Peta yang Memandu Seluruh Kursus Ini"
duration_minutes: 13
bloom_level: remember
keywords:
  - HCAI principles transparency fairness control accountability
  - responsible AI principles
  - AI ethics framework
  - human-centered AI checklist
  - trustworthy AI design
is_free: true
status: draft
---

# Empat Prinsip HCAI — Peta yang Memandu Seluruh Kursus Ini

**Modul 1 · What Is Human-Centered AI?** · Lesson 4 dari 4
**Estimasi waktu baca:** 20 menit · **Level:** Foundational · **Prasyarat:** M1-L1, M1-L2, M1-L3

---

> **Yang akan kamu capai di lesson ini:**
> - Menyebutkan keempat prinsip HCAI — Transparency, Fairness, Control, Accountability — beserta pertanyaan diagnostik masing-masing
> - Mengenali bagaimana keempat prinsip terhubung ke kerangka dua sumbu Shneiderman dari lesson sebelumnya
> - Mengidentifikasi di modul mana setiap prinsip akan dikembangkan lebih dalam sepanjang kursus ini

---

## Hook

Bayangkan sebuah sistem yang digunakan hakim di pengadilan Amerika Serikat untuk membantu memutuskan apakah seorang terdakwa harus ditahan sebelum persidangan — atau dibebaskan dengan jaminan.

Sistem itu bernama COMPAS (*Correctional Offender Management Profiling for Alternative Sanctions*). Ia menghasilkan skor risiko antara 1 dan 10: semakin tinggi skor, semakin besar kemungkinan terdakwa dianggap akan melakukan kejahatan lagi.

Di atas kertas, ini terdengar seperti alat yang berguna — menggunakan data untuk membantu keputusan yang selama ini terlalu bergantung pada intuisi hakim yang bisa bias.

Kenyataannya jauh lebih rumit.

Pada 2016, lembaga jurnalisme investigatif ProPublica menganalisis lebih dari 7.000 keputusan COMPAS di Broward County, Florida. Temuannya mengejutkan: terdakwa kulit hitam yang akhirnya *tidak* melakukan kejahatan baru dua kali lebih sering diberi skor risiko tinggi dibanding terdakwa kulit putih dalam situasi yang sama. Sebaliknya, terdakwa kulit putih yang kemudian *benar-benar* melakukan kejahatan baru lebih sering diberi skor risiko rendah.

Yang membuat kasus ini menjadi pelajaran klasik dalam HCAI bukan hanya soal bias statistiknya — melainkan **empat masalah yang terjadi sekaligus dan saling memperburuk**:

Pertama, tidak ada yang bisa melihat bagaimana skor itu dihitung. Perusahaan pembuatnya, Northpointe, menolak mengungkap algoritma dengan alasan rahasia dagang. **Tidak ada transparansi.**

Kedua, hasilnya secara sistematis lebih merugikan kelompok tertentu berdasarkan ras. **Tidak ada fairness.**

Ketiga, banyak hakim menerima skor itu sebagai otoritas tanpa pertanyaan kritis — meski pelatihan mereka mengharuskan mereka mempertimbangkan banyak faktor lain. **Kontrol manusia yang bermakna tidak berjalan.**

Keempat, ketika bias terungkap, tidak ada entitas yang bertanggung jawab secara jelas — apakah pembuat algoritma, pengadilan yang mengadopsinya, atau hakim yang menggunakannya? **Tidak ada accountability yang jelas.**

Kasus COMPAS adalah ilustrasi paling lengkap tentang apa yang terjadi ketika keempat prinsip Human-Centered AI sekaligus diabaikan. Dan keempat prinsip itulah — **Transparency, Fairness, Control, dan Accountability** — yang akan menjadi peta navigasimu di seluruh kursus ini.

---

## Kerangka Konseptual

### Dari dua sumbu ke empat prinsip: koneksi yang perlu dibuat eksplisit

Di lesson sebelumnya, kita memetakan sistem AI pada dua sumbu Shneiderman: **tingkat kontrol manusia** dan **tingkat keandalan sistem**. Keduanya membentuk empat kuadran yang menggambarkan kondisi sistem dari yang berbahaya hingga ideal.

Empat prinsip yang akan kita pelajari di lesson ini adalah cara mengoperasionalkan kedua sumbu itu — cara menjawab pertanyaan praktis: *apa konkretnya yang harus ada agar sebuah sistem berada di kuadran ideal?*

- **Control** adalah operasionalisasi langsung dari sumbu "tingkat kontrol manusia" — prinsip ini mendefinisikan apa yang dimaksud dengan kontrol yang bermakna, bukan hanya kontrol nominal.
- **Transparency, Fairness, dan Accountability** adalah tiga dimensi yang bersama-sama membangun apa yang kita sebut sistem yang "andal dan dapat dipercaya" — sumbu kedua Shneiderman. Sistem yang transparan bisa diaudit. Sistem yang fair tidak menciptakan bahaya tersembunyi. Sistem yang accountable punya mekanisme koreksi ketika sesuatu berjalan salah.

Dengan kata lain: **dua sumbu Shneiderman adalah peta; empat prinsip adalah kompas yang membantumu bergerak menuju kuadran ideal.**

### Mengapa empat prinsip ini — dan bukan yang lain?

Banyak kerangka etika AI yang telah dipublikasikan oleh institusi akademik, perusahaan teknologi, dan badan regulasi menyebutkan berbagai prinsip: keamanan, privasi, inklusivitas, keberlanjutan, dan seterusnya.

CodeinteX memilih empat prinsip ini sebagai kerangka utama karena satu alasan pragmatis: **keempat prinsip ini paling langsung bisa dioperasionalkan oleh siapapun yang terlibat dalam pembuatan atau evaluasi sistem AI** — bukan hanya oleh peneliti etika AI atau regulator.

Setiap prinsip bisa diuji dengan satu pertanyaan sederhana. Dan setiap pertanyaan itu bisa dijawab oleh product manager, desainer, developer, maupun researcher — tanpa perlu gelar dalam filsafat etika.

---

### Prinsip 1: Transparency — "Bisakah kamu melihat apa yang sedang terjadi?"

Transparency dalam konteks HCAI berarti sistem AI beroperasi dengan cara yang bisa dipahami oleh mereka yang menggunakannya dan terdampak olehnya — pada tingkat detail yang proporsional dengan taruhan keputusannya.

Ini bukan berarti setiap pengguna harus memahami arsitektur neural network atau kode sumber sistem. Transparency berjalan pada beberapa lapisan:

- **Transparency proses:** pengguna tahu *bahwa* keputusan dibuat oleh AI, bukan oleh manusia
- **Transparency faktor:** pengguna memahami, setidaknya secara umum, faktor apa yang mempengaruhi keputusan
- **Transparency batas:** pengguna tahu dalam kondisi apa sistem bisa salah

COMPAS gagal di ketiga lapisan: terdakwa tidak tahu skor mereka dihasilkan oleh algoritma, tidak tahu faktor apa yang digunakan, dan tidak ada informasi tentang di mana algoritma itu cenderung tidak akurat.

**Pertanyaan diagnostik:** *Apakah orang yang terdampak oleh keputusan sistem ini tahu bagaimana keputusan itu dibuat — setidaknya pada level yang memungkinkan mereka merespons secara bermakna?*

---

### Prinsip 2: Fairness — "Apakah sistem ini bekerja setara untuk semua orang?"

Fairness berarti sistem AI tidak secara sistematis menguntungkan atau merugikan kelompok tertentu — berdasarkan ras, gender, usia, lokasi, tingkat pendidikan, atau karakteristik lain yang tidak relevan dengan keputusan yang dibuat.

Ini lebih mudah diucapkan daripada diimplementasikan, karena fairness sendiri bukan konsep tunggal. Satu sistem bisa "fair" menurut satu definisi matematis dan "tidak fair" menurut definisi yang berbeda — dan ini bukan soal memilih definisi yang paling menguntungkan, melainkan soal memahami implikasi dari setiap pilihan.

Yang perlu diingat di level foundational ini adalah: **bias dalam sistem AI hampir selalu bukan hasil dari niat jahat, melainkan hasil dari data yang tidak representatif atau tujuan optimasi yang tidak mempertimbangkan semua kelompok yang terdampak.** Seperti yang kita lihat di Lesson 1 dengan kasus Amazon dan pulse oximeter.

**Pertanyaan diagnostik:** *Apakah ada kelompok pengguna atau pihak terdampak yang secara sistematis mendapat pengalaman atau hasil yang lebih buruk dari sistem ini — bahkan jika itu tidak disengaja?*

---

### Prinsip 3: Control — "Bisakah manusia mengintervensi ketika dibutuhkan?"

Control berarti manusia — baik pengguna langsung, operator, maupun pengawas — memiliki kemampuan nyata untuk memantau, mempertanyakan, mengoreksi, dan jika perlu menghentikan keputusan sistem AI, terutama untuk keputusan yang berdampak signifikan.

Penting untuk membedakan dua jenis kontrol:

**Kontrol nominal** adalah kontrol yang secara teknis tersedia tapi tidak bisa digunakan secara efektif dalam praktik — misalnya, tombol "override" yang ada tapi membutuhkan proses birokrasi yang panjang untuk diaktifkan, atau opsi "tolak rekomendasi AI" yang ada tapi tidak ada panduan tentang kapan dan bagaimana menggunakannya.

**Kontrol bermakna** adalah kontrol yang bisa digunakan secara praktis oleh manusia yang memiliki kapasitas dan informasi yang diperlukan — tanpa hambatan yang tidak proporsional.

Kasus AF447 di Lesson 3 adalah contoh kontrol yang secara teknis tersedia (pilot bisa mengambil alih kemudi kapan saja) tapi tidak bermakna dalam praktik karena kondisi kognitif, pelatihan, dan informasi yang tidak mendukung penggunaannya secara efektif.

**Pertanyaan diagnostik:** *Apakah orang yang bertanggung jawab atas keputusan ini memiliki kemampuan nyata — bukan hanya kemampuan teoritis — untuk mengintervensi, mengoreksi, atau menolak rekomendasi sistem saat diperlukan?*

---

### Prinsip 4: Accountability — "Siapa yang bertanggung jawab atas konsekuensinya?"

Accountability berarti ada entitas yang jelas — individu, tim, atau organisasi — yang bertanggung jawab atas dampak keputusan sistem AI. Ketika sistem membuat keputusan yang salah dan merugikan seseorang, harus ada jalur yang jelas: kepada siapa seseorang bisa mengajukan keberatan, dan siapa yang akan merespons.

Ini adalah prinsip yang paling sering diabaikan dalam desain sistem AI, dan alasannya dapat dipahami: akuntabilitas adalah beban. Tidak ada yang ingin bertanggung jawab atas kesalahan sistem yang kompleks.

Namun tanpa accountability, tiga prinsip lainnya kehilangan taringnya. Transparency tanpa accountability hanya menjadi informasi tanpa konsekuensi. Fairness tanpa accountability tidak bisa ditegakkan ketika dilanggar. Control tanpa accountability tidak mendorong siapapun untuk benar-benar menggunakannya.

Dalam konteks regulasi, EU AI Act (2024) mewajibkan setiap sistem AI berisiko tinggi untuk memiliki entitas yang bertanggung jawab secara hukum atas keputusan sistemnya. Ini bukan hanya pergeseran etika — ini adalah pergeseran hukum yang sedang terjadi sekarang.

**Pertanyaan diagnostik:** *Jika sistem ini membuat keputusan yang merugikan seseorang, kepada siapa orang itu bisa mengajukan keberatan — dan siapa yang akan bertanggung jawab untuk merespons dan memperbaikinya?*

---

## Keempat Prinsip sebagai Peta Kursus

Empat prinsip ini bukan hanya konsep yang akan kamu pelajari — mereka adalah **struktur navigasi** untuk keseluruhan kursus ini. Setiap modul ke depan akan mengeksplorasi satu atau lebih prinsip ini secara lebih dalam:

| Modul | Fokus | Prinsip yang dieksplorasi |
|---|---|---|
| **M2** | Bagaimana manusia berpikir tentang AI | Semua 4 prinsip dari sudut psikologi |
| **M3** | Prinsip-prinsip HCAI secara mendalam | Transparency, Fairness, Control, Accountability |
| **M4** | Explainability dan fairness dalam praktik | Transparency, Fairness |
| **M5** | Desain HCAI dengan IFRAME | Control, Transparency |
| **M6** | Evaluasi sistem HCAI | Accountability, semua prinsip |
| **Capstone** | Analisis produk AI nyata | Semua 4 prinsip |

Setiap kali kamu menganalisis sistem AI — baik selama kursus ini maupun sesudahnya — keempat pertanyaan diagnostik di atas adalah titik awal yang paling konsisten dan praktis.

---

> **Quick Check** — Sebelum melanjutkan:
> *Dari keempat prinsip — Transparency, Fairness, Control, Accountability — prinsip mana yang paling sering kamu lihat dilanggar dalam produk digital yang kamu kenal? Dan prinsip mana yang menurutmu paling sulit diimplementasikan — dan mengapa?*

---

## Analisis Kasus

Mari kita kembali ke COMPAS dan lihat bagaimana keempat prinsip bisa menjadi alat diagnosis yang konkret.

**Transparency:** Skor dihasilkan oleh algoritma proprietary yang tidak bisa diaudit oleh terdakwa, pengacara pembela, atau bahkan hakim itu sendiri. Keputusan yang berdampak pada kebebasan seseorang dibuat berdasarkan kalkulasi yang tidak bisa dipertanyakan. *Diagnosis: gagal total.*

**Fairness:** Data historis yang digunakan untuk melatih algoritma mencerminkan pola penangkapan dan penghukuman yang sudah ada — yang sendirinya sudah mengandung bias sistemik. Algoritma mempelajari dan mereproduksi bias itu. *Diagnosis: gagal, dengan konsekuensi yang tidak proporsional terhadap kelompok tertentu.*

**Control:** Secara nominal, hakim bebas mengabaikan skor COMPAS. Dalam praktik, skor itu menciptakan anchoring yang kuat — sebuah angka konkret dalam dokumen resmi yang sulit untuk diabaikan tanpa justifikasi eksplisit. Banyak hakim tidak memiliki pelatihan untuk mengkritisi validitas statistik skor tersebut. *Diagnosis: kontrol nominal ada, kontrol bermakna tidak.*

**Accountability:** Northpointe (pembuat algoritma) berargumen bahwa mereka hanya menyediakan alat, bukan membuat keputusan. Pengadilan berargumen bahwa hakim yang membuat keputusan akhir. Tidak ada satu entitas pun yang menerima tanggung jawab penuh atas bias sistemik yang terdokumentasi. *Diagnosis: gap akuntabilitas yang lengkap.*

Dari empat pertanyaan diagnostik, keempat-empatnya menghasilkan jawaban yang mengkhawatirkan. Ini bukan sistem yang "sedikit tidak sempurna" — ini adalah sistem yang gagal pada setiap dimensi yang relevan untuk keputusan yang berdampak pada kebebasan manusia.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Gunakan keempat pertanyaan diagnostik ini sebagai checklist minimum sebelum meluncurkan fitur AI apapun. Ini bukan pengganti audit etika yang komprehensif — tapi ini adalah filter pertama yang bisa menangkap masalah terbesar sebelum mereka sampai ke tangan pengguna. Keempat pertanyaan ini bisa diajukan dalam satu sesi product review tanpa membutuhkan keahlian khusus.

**Jika kamu UX researcher atau designer:**
Setiap prinsip mengimplikasikan pertanyaan riset yang berbeda. Transparency mendorong pertanyaan tentang mental model pengguna. Fairness mendorong riset yang melibatkan kelompok yang paling rentan terdampak. Control mendorong observasi tentang bagaimana pengguna aktualnya berinteraksi dengan mekanisme override. Accountability mendorong studi tentang apa yang terjadi ketika pengguna mengalami kesalahan sistem. Desain penelitianmu bisa distrukturkan di sekitar kerangka ini.

**Jika kamu developer atau engineer:**
Setiap prinsip juga punya implikasi teknis. Transparency membutuhkan logging dan audit trail yang dapat diakses. Fairness membutuhkan disagregasi metrik performa berdasarkan kelompok. Control membutuhkan mekanisme override yang dirancang untuk digunakan, bukan hanya untuk ada. Accountability membutuhkan dokumentasi yang jelas tentang siapa bertanggung jawab atas komponen mana.

---

## Pertanyaan Refleksi

> Di Lesson 1, kamu diminta memikirkan satu produk AI dan bertanya: "Siapa semua pihak yang terdampak?"
>
> Sekarang, dengan empat prinsip di tangan, **terapkan keempat pertanyaan diagnostik pada produk yang sama:**
>
> 1. Apakah mereka yang terdampak bisa melihat bagaimana keputusan dibuat? *(Transparency)*
> 2. Apakah ada kelompok yang secara sistematis mendapat hasil lebih buruk? *(Fairness)*
> 3. Apakah ada mekanisme kontrol bermakna untuk mengintervensi keputusan? *(Control)*
> 4. Jika ada yang dirugikan, kepada siapa mereka bisa mengadu? *(Accountability)*
>
> Simpan jawaban ini. Di akhir kursus — di capstone Modul 6 — kamu akan kembali ke produk ini dengan semua alat yang sudah dipelajari, dan menghasilkan analisis yang jauh lebih dalam.

---

## Ringkasan Modul 1

Kita telah menempuh empat lesson dalam Modul 1. Ini yang kita bangun bersama:

- **L1:** Kegagalan AI paling mahal bukan soal model yang tidak cukup pintar — melainkan soal tidak mengenal siapa yang terdampak dan apa konsekuensi kesalahannya.
- **L2:** Paradigma AI sedang bergeser dari "mengalahkan manusia" ke "membantu manusia" — dan pergeseran ini didorong oleh kegagalan publik, tekanan regulasi, dan konsekuensi bisnis.
- **L3:** Setiap sistem AI bisa dipetakan pada dua sumbu: tingkat kontrol manusia dan tingkat keandalan sistem. Posisi yang tepat bergantung pada konteks dan taruhan keputusan — bukan pada asumsi bahwa "makin otonom makin baik."
- **L4:** Empat prinsip — Transparency, Fairness, Control, Accountability — adalah alat diagnosis yang bisa digunakan oleh siapapun untuk mengevaluasi sistem AI, dan mereka adalah peta untuk seluruh kursus ini.

**Modul 2** akan membawa kita ke lapisan yang lebih dalam: bagaimana manusia secara psikologis membangun pemahaman tentang AI — dan mengapa pemahaman itu sering tidak akurat dengan cara yang konsisten dan bisa diprediksi.

---

## Referensi

- Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press. — Bab 1–5.
- Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2016). Machine bias. *ProPublica*, 23 Mei 2016. Diakses dari propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
- Dressel, J., & Farid, H. (2018). The accuracy, fairness, and limits of predicting recidivism. *Science Advances*, 4(1).
- European Parliament. (2024). *Regulation (EU) 2024/1689 — Artificial Intelligence Act*. Official Journal of the European Union.
- Doshi-Velez, F., & Kim, B. (2017). Towards a rigorous science of interpretable machine learning. *arXiv preprint* arXiv:1702.08608.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
