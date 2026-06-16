---
course: hcai-foundations
module: 3
module_title: "The Four Principles — What HCAI Demands"
lesson: 1
title: "Transparency: Ketika Sistem AI Harus Bisa Dibaca"
duration_minutes: 12
bloom_level: understand
keywords:
  - AI transparency principle
  - transparent AI design
  - explainable AI transparency
  - AI opacity harms
  - right to explanation AI
is_free: true
status: draft
---

# Transparency: Ketika Sistem AI Harus Bisa Dibaca

**Modul 3 · The Four Principles — What HCAI Demands** · Lesson 1 dari 5
**Estimasi waktu baca:** 12 menit · **Level:** Foundational · **Prasyarat:** M1-L1 s/d M2-L4

---

> **Yang akan kamu capai di lesson ini:**
> - Menjelaskan mengapa transparansi AI bukan sekadar pilihan etis, melainkan kebutuhan fungsional untuk sistem yang bisa dipercaya
> - Mengidentifikasi tiga lapisan transparansi yang berbeda dan konteks di mana masing-masing relevan
> - Membedakan transparansi proaktif dari transparansi reaktif beserta implikasi desainnya

---

## Hook

Antara 2013 dan 2021, lebih dari 26.000 keluarga di Belanda dituduh melakukan penipuan tunjangan anak oleh sistem AI milik otoritas pajak pemerintah. Mereka diminta mengembalikan puluhan ribu euro tunjangan yang sudah diterima. Banyak yang tidak bisa membayar. Akibatnya: kehilangan rumah, perceraian, kebangkrutan, dan setidaknya beberapa kasus bunuh diri yang dikaitkan dengan tekanan finansial yang tiba-tiba.

Yang membuat kasus ini — dikenal sebagai *toeslagenaffaire* di Belanda — menjadi landmark dalam sejarah HCAI adalah apa yang ditemukan ketika parlemen mulai menyelidikinya: **tidak ada seorang pun yang bisa menjelaskan dengan tepat mengapa seseorang ditandai sebagai penipu.**

Bukan karena sistemnya rahasia secara teknis. Melainkan karena sistem itu dibangun dengan cara yang membuat penjelasan menjadi tidak mungkin diberikan — bahkan kepada orang-orang yang bertanggung jawab menjalankannya. Kombinasi antara model yang kompleks, data yang terfragmentasi, dan proses pengambilan keputusan yang tidak didokumentasikan menciptakan situasi di mana ribuan hidup hancur oleh keputusan yang tidak bisa dipertanggungjawabkan kepada siapapun.

Skandal ini akhirnya menyebabkan jatuhnya pemerintah koalisi Belanda pada Januari 2021 — dan menjadi salah satu referensi utama dalam penyusunan EU AI Act.

Kasus ini bukan tentang algoritma yang jahat. Ini tentang sistem yang **tidak transparan** — dan konsekuensi nyata dari ketidaktransparanan itu.

---

## Kerangka Konseptual

### Mengapa transparansi adalah kebutuhan fungsional, bukan hanya etika

Dalam diskusi sehari-hari, transparansi sering ditempatkan sebagai nilai etis yang *seharusnya* ada tapi bisa dikompromikan demi kecepatan atau efisiensi. Ini adalah framing yang salah.

Transparansi adalah **prasyarat fungsional** untuk sistem AI yang bisa dipercaya dalam jangka panjang. Sistem yang tidak transparan tidak bisa diaudit. Sistem yang tidak bisa diaudit tidak bisa diperbaiki ketika ia salah. Sistem yang tidak bisa diperbaiki akan terus salah dengan cara yang sama — dan pada skala yang tidak bisa dikendalikan.

Kasus Belanda menunjukkan ini bukan teori. Sistem yang tidak transparan menciptakan kerentanan sistemik yang tidak terlihat sampai ia meledak.

### Tiga lapisan transparansi

Transparansi bukan konsep tunggal. Ia bekerja pada tiga lapisan yang berbeda, masing-masing menjawab pertanyaan yang berbeda:

**Lapisan 1 — Transparansi proses:** *Apakah pengguna tahu bahwa keputusan ini dibuat oleh AI?*

Ini adalah lapisan paling dasar. Seseorang tidak bisa mengevaluasi keputusan AI jika mereka tidak tahu bahwa AI terlibat. Di banyak sistem saat ini — dari rekomendasi konten hingga keputusan kredit — pengguna seringkali tidak tahu apakah keputusan yang mempengaruhi mereka dibuat oleh manusia atau algoritma.

EU AI Act (2024) mewajibkan notifikasi eksplisit ketika sistem AI berinteraksi dengan manusia dalam domain berisiko tinggi. Ini adalah formalisasi legal dari lapisan transparansi paling dasar.

**Lapisan 2 — Transparansi faktor:** *Apakah pengguna memahami faktor apa yang mempengaruhi keputusan?*

Lapisan ini lebih dalam. Tahu bahwa AI membuat keputusan tidak cukup — pengguna juga perlu memahami, setidaknya secara umum, variabel apa yang digunakan dan bagaimana bobotnya. Tanpa ini, mereka tidak bisa mengidentifikasi ketika sistem membuat keputusan berdasarkan faktor yang seharusnya tidak relevan.

Dalam kasus Belanda, salah satu faktor yang kemudian teridentifikasi sebagai pemicu penandaan "penipu" adalah kepemilikan rekening bank di luar Belanda — sesuatu yang sangat umum di kalangan imigran generasi pertama, kelompok yang kemudian terbukti secara tidak proporsional terkena dampaknya.

**Lapisan 3 — Transparansi batas:** *Apakah pengguna tahu kondisi di mana sistem bisa salah?*

Ini adalah lapisan yang paling sering diabaikan dan paling berharga. Setiap sistem AI memiliki domain di mana performanya lebih lemah — jenis input, kondisi, atau populasi di mana prediksinya kurang akurat. Mengomunikasikan batas ini secara eksplisit memungkinkan pengguna mengkalibrasi kepercayaan mereka secara tepat.

### Transparansi proaktif vs reaktif

Ada dua pendekatan implementasi transparansi yang menghasilkan pengalaman pengguna yang sangat berbeda:

**Transparansi reaktif** — informasi tentang cara kerja sistem hanya tersedia jika pengguna secara aktif meminta atau mencarinya. Ini adalah pendekatan yang paling umum, dan yang paling lemah. Pengguna yang paling membutuhkan transparansi — mereka yang tidak tahu harus bertanya apa — justru paling tidak terlayani oleh pendekatan ini.

**Transparansi proaktif** — sistem secara aktif mengomunikasikan alasan, dasar, dan keterbatasannya tanpa menunggu diminta. Ini adalah standar yang lebih tinggi, tapi juga yang lebih efektif dalam membangun kepercayaan yang terkalibrasi. "Rekomendasi ini berdasarkan 3 bulan riwayat pembelianmu" adalah contoh sederhana transparansi proaktif yang tidak membutuhkan kompleksitas teknis tambahan.

---

> **Quick Check** — Sebelum melanjutkan:
> *Dari tiga lapisan transparansi — proses, faktor, dan batas — lapisan mana yang paling sering absen dalam produk digital yang kamu gunakan sehari-hari? Apa yang membuat lapisan itu sulit disediakan oleh tim pengembang?*

---

## Analisis Kasus

Kembali ke kasus Belanda. Dengan kerangka tiga lapisan, kita bisa memetakan kegagalannya secara presisi:

**Transparansi proses:** Keluarga yang menerima tagihan tidak diberi tahu bahwa keputusan itu dihasilkan oleh sistem otomasi. Surat-surat yang dikirim terlihat seperti keputusan yang dibuat oleh petugas manusia. *Kegagalan total.*

**Transparansi faktor:** Bahkan ketika keluarga meminta penjelasan, otoritas pajak tidak bisa memberikan faktor spesifik yang menyebabkan penandaan. Investigasi parlemen kemudian menemukan bahwa faktor-faktor seperti memiliki kewarganegaraan ganda digunakan sebagai indikator risiko — tapi ini tidak pernah dikomunikasikan. *Kegagalan total.*

**Transparansi batas:** Tidak ada mekanisme untuk mengidentifikasi populasi di mana sistem kurang akurat. Akibatnya, bias sistemik terhadap keluarga imigran berlangsung selama bertahun-tahun tanpa terdeteksi. *Kegagalan total.*

Ketiga lapisan gagal sekaligus — dan hasilnya adalah delapan tahun penderitaan yang tidak perlu bagi puluhan ribu keluarga.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Mulai dengan pertanyaan: *"Jika sistem ini membuat keputusan yang salah tentang pengguna, apakah mereka akan tahu — dan apakah kita akan tahu?"* Jika jawabannya tidak, transparansi adalah celah risiko yang perlu ditutup sebelum skala produk membuat celah itu mahal.

**Jika kamu UX researcher atau designer:**
Rancang "transparency touchpoints" — momen dalam alur pengguna di mana sistem secara proaktif menjelaskan apa yang sedang terjadi dan mengapa. Ini tidak harus panjang atau teknis; satu kalimat di waktu yang tepat lebih efektif dari halaman dokumentasi yang tidak pernah dibaca.

**Jika kamu developer atau engineer:**
Bangun kemampuan logging dan audit trail sejak awal, bukan sebagai tambahan. Sistem yang tidak bisa menjelaskan keputusannya sendiri kepada pengembangnya adalah sistem yang tidak bisa diperbaiki secara sistematis. *Explainability untuk internal tim* adalah prasyarat untuk *explainability untuk pengguna*.

---

## Pertanyaan Refleksi

> Di lesson ini kita melihat bagaimana ketidaktransparanan AI bisa menghancurkan kehidupan ribuan orang tanpa ada yang menyadarinya selama bertahun-tahun.
>
> **Pikirkan satu sistem AI di organisasimu atau yang kamu kenal** — apakah ada keputusan yang sistem itu buat yang tidak bisa dijelaskan dengan tepat kepada orang yang terdampak? Lapisan transparansi mana yang paling lemah — proses, faktor, atau batas?

---

## Ringkasan Lesson

- Transparansi bukan pilihan etis opsional — ia adalah prasyarat fungsional untuk sistem AI yang bisa diaudit, diperbaiki, dan dipercaya jangka panjang.
- Tiga lapisan: transparansi proses (pengguna tahu AI terlibat), transparansi faktor (pengguna tahu faktor apa yang digunakan), transparansi batas (pengguna tahu kondisi di mana sistem bisa salah).
- Transparansi proaktif lebih efektif dari reaktif — sistem yang menjelaskan dirinya sendiri tanpa diminta membangun kepercayaan yang jauh lebih solid.
- Kasus Belanda menunjukkan bahwa kegagalan transparansi bukan hanya masalah etika — ini adalah kegagalan governance yang bisa menghancurkan ribuan hidup dan menjatuhkan pemerintahan.
- Lesson berikutnya akan membahas prinsip kedua: Fairness — dan mengapa "netral" tidak selalu berarti "adil."

---

## Referensi

- Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press. — Bab 6.
- European Parliament. (2024). *Regulation (EU) 2024/1689 — Artificial Intelligence Act*. Official Journal of the European Union. — Pasal 13–14 tentang kewajiban transparansi.
- Dutch House of Representatives. (2021). *Unprecedented Injustice: Report of the Parliamentary Inquiry Committee on the childcare benefit affair*. Tweede Kamer der Staten-Generaal.
- Doshi-Velez, F., & Kim, B. (2017). Towards a rigorous science of interpretable machine learning. *arXiv preprint* arXiv:1702.08608.
- Wachter, S., Mittelstadt, B., & Russell, C. (2017). Counterfactual explanations without opening the black box. *Harvard Journal of Law & Technology*, 31(2).

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
