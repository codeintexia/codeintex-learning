---
course: hcai-foundations
module: 6
module_title: "Evaluating and Improving HCAI Systems"
lesson: 2
title: "Metode Evaluasi Human-Centered: Memilih Pendekatan yang Tepat untuk Produk AI"
duration_minutes: 14
bloom_level: evaluate
keywords:
  - UX research AI products
  - wizard of oz AI testing
  - think aloud AI evaluation
  - human-centered evaluation methods
  - AI usability testing
is_free: true
status: draft
---

# Metode Evaluasi Human-Centered: Memilih Pendekatan yang Tepat untuk Produk AI

**Modul 6 · Evaluating and Improving HCAI Systems** · Lesson 2 dari 4
**Estimasi waktu baca:** 14 menit · **Level:** Foundational · **Prasyarat:** M6-L1

---

> **Yang akan kamu capai di lesson ini:**
> - Mengevaluasi kelebihan dan keterbatasan tiga metode evaluasi human-centered utama untuk produk AI
> - Menilai kondisi di mana setiap metode paling sesuai dan paling tidak sesuai untuk evaluasi sistem AI
> - Merekomendasikan kombinasi metode evaluasi yang tepat untuk skenario produk AI yang berbeda

---

## Hook

Sebuah tim e-commerce meluncurkan fitur rekomendasi produk berbasis AI. Sebelum peluncuran, mereka melakukan usability testing standar: 12 peserta, skenario terstruktur, think-aloud protocol. Task completion rate: 94%. Semua peserta berhasil menemukan dan membeli produk.

Tiga bulan setelah peluncuran, data analytics menunjukkan penurunan 18% dalam kepuasan pelanggan untuk segmen pengguna yang paling aktif menggunakan fitur rekomendasi.

Investigasi mengungkap masalah yang tidak terdeteksi dalam testing: pengguna yang menggunakan fitur rekomendasi secara intensif mulai *berhenti menjelajahi* produk secara mandiri. Mereka menjadi sangat bergantung pada rekomendasi AI — bahkan ketika rekomendasi itu tidak akurat untuk kebutuhan mereka saat itu. Kepuasan turun bukan karena fitur tidak bisa digunakan, melainkan karena penggunaan intensif mengubah perilaku mereka dengan cara yang merugikan pengalaman mereka secara keseluruhan.

Usability testing yang baik tidak mendeteksi ini karena usability testing tidak dirancang untuk mengukur efek jangka menengah, perubahan perilaku, atau kualitas keputusan pengguna. Ia dirancang untuk mengukur apakah pengguna bisa menyelesaikan tugas — dan untuk itu, metode itu bekerja dengan sempurna.

Masalahnya bukan metodologinya buruk. Masalahnya adalah tim menggunakan satu metode untuk menjawab pertanyaan yang membutuhkan metode yang berbeda.

*Skenario ini adalah komposit representatif dari pola yang terdokumentasi dalam literatur evaluasi produk AI — termasuk dalam Amershi et al. (2019) dan Yang et al. (2020).*

---

## Kerangka Konseptual

### Mengapa produk AI membutuhkan pendekatan evaluasi yang berbeda

Evaluasi usability standar mengasumsikan produk yang berperilaku konsisten dan deterministik (*deterministic*): jika pengguna melakukan X, sistem selalu merespons dengan Y. Produk AI melanggar asumsi ini — responsnya bervariasi, ia "berubah" seiring waktu, dan kualitas outputnya bergantung pada konteks yang sering tidak terlihat.

Ini membutuhkan metode evaluasi yang bisa menangkap tiga hal yang tidak ditangani usability testing standar:
1. Bagaimana pengguna membangun kepercayaan (atau ketidakpercayaan) seiring waktu
2. Bagaimana keputusan pengguna berubah karena adanya AI
3. Bagaimana pengguna memahami atau salah memahami kapabilitas dan batas sistem

### Tiga metode evaluasi human-centered untuk produk AI

**Metode 1 — Think-Aloud Protocol (Protokol Berpikir Keras)**

*Apa itu:* Pengguna diminta mengucapkan apa yang mereka pikirkan saat berinteraksi dengan sistem. Peneliti merekam verbalisasi ini untuk memahami model mental, titik kebingungan, dan proses pengambilan keputusan.

*Asal:* Ericsson & Simon (1993) mengembangkan protokol ini untuk penelitian kognisi; Nielsen (1994) mempopulerkannya dalam usability testing.

*Nilai unik untuk produk AI:* Think-aloud adalah metode terbaik untuk mengungkap mental model gap — kesenjangan antara apa yang pengguna pikirkan tentang cara kerja sistem dan cara sistem sebenarnya bekerja. Dari M2-L2, kita tahu ini adalah salah satu sumber risiko terbesar dalam produk AI. Think-aloud membuatnya terlihat secara langsung.

*Keterbatasan untuk AI:* (a) Efek reaktivitas — mengucapkan pikiran mengubah proses berpikir, yang bisa mengubah cara pengguna berinteraksi dengan sistem AI. (b) Tidak efektif untuk mengukur efek jangka panjang atau perubahan kepercayaan seiring waktu. (c) Penggunaan think-aloud dalam kondisi tekanan (seperti keputusan medis darurat) tidak realistis.

*Kapan gunakan:* Evaluasi awal untuk memahami mental model gap, identifikasi titik kebingungan dalam antarmuka, dan pengujian penjelasan AI (apakah penjelasan yang diberikan sistem dipahami dengan benar?).

**Metode 2 — Wizard of Oz (WoZ)**

*Apa itu:* Pengguna berinteraksi dengan sistem yang mereka percaya adalah AI, tapi sebenarnya dikontrol oleh manusia di balik layar ("wizard"). Digunakan untuk mengevaluasi konsep atau antarmuka AI sebelum sistem sebenarnya dibangun.

*Asal:* Dinamai dari karakter dalam novel L. Frank Baum; dipopulerkan dalam penelitian HCI oleh Kelley (1984) untuk pengembangan sistem natural language interface.

*Nilai unik untuk produk AI:* WoZ memungkinkan evaluasi respons pengguna terhadap jenis output AI tertentu — termasuk output yang salah — sebelum sistem sebenarnya dibangun. Ini sangat berharga untuk mengevaluasi desain eksplanabilitas (M4) dan mekanisme kontrol manusia (M3-L3): apakah pengguna menggunakan tombol override? Kapan mereka mempertanyakan rekomendasi?

*Keterbatasan untuk AI:* (a) "Wizard" harus sangat konsisten agar tidak mengintroduksi variasi yang tidak ada di sistem nyata. (b) Tidak bisa mensimulasikan karakteristik probabilistik model AI — seperti confidence yang bervariasi berdasarkan konteks. (c) Mahal dalam waktu dan tenaga untuk skenario yang kompleks.

*Kapan gunakan:* Prototipe konsep sebelum model dibangun, pengujian eksplanabilitas dan mekanisme kontrol sebelum implementasi, eksplorasi perilaku pengguna terhadap output AI yang salah atau tidak pasti.

**Metode 3 — Evaluasi Lapangan Longitudinal (Field Study)**

*Apa itu:* Observasi penggunaan sistem AI dalam kondisi nyata selama periode waktu yang diperpanjang — minggu atau bulan, bukan satu sesi lab. Mengkombinasikan observasi, wawancara, dan analisis log secara berkelanjutan.

*Nilai unik untuk produk AI:* Satu-satunya metode yang bisa menangkap: (a) bagaimana kepercayaan berkembang atau runtuh seiring waktu, (b) efek jangka menengah seperti penurunan kemampuan karena kurang digunakan (*de-skilling*) atau ketergantungan berlebih, dan (c) bagaimana sistem berperilaku dalam kondisi kasus tepi (*edge case*) yang tidak muncul dalam sesi testing yang terbatas. Ini adalah metode yang seharusnya digunakan untuk mendeteksi masalah dalam kasus e-commerce di hook.

*Keterbatasan:* (a) Mahal dan membutuhkan waktu lama. (b) Lebih sulit untuk mengontrol variabel — sulit mengatribusikan perubahan perilaku ke sistem AI vs faktor lain. (c) Tidak bisa dilakukan sebelum produk diluncurkan.

*Kapan gunakan:* Post-launch monitoring untuk sistem AI dengan dampak jangka panjang pada perilaku pengguna, evaluasi sistem di mana trust calibration adalah metrik kritis, dan studi de-skilling untuk sistem yang menggantikan keahlian manusia.

### Matriks pemilihan metode

| Pertanyaan evaluasi | Think-aloud | WoZ | Field study |
|---|---|---|---|
| Mental model pengguna | ✓✓ Terbaik | ✓ Baik | ○ Terbatas |
| Kalibrasi kepercayaan awal | ✓ Baik | ✓ Baik | ✓✓ Terbaik |
| Perubahan kepercayaan seiring waktu | ✗ Tidak bisa | ✗ Tidak bisa | ✓✓ Terbaik |
| Efektivitas eksplanabilitas | ✓✓ Terbaik | ✓✓ Terbaik | ✓ Baik |
| Perilaku terhadap output yang salah | ✓ Baik | ✓✓ Terbaik | ○ Sulit dikontrol |
| Efek de-skilling | ✗ Tidak bisa | ✗ Tidak bisa | ✓✓ Terbaik |
| Sebelum sistem dibangun | ✓ Dengan prototipe | ✓✓ Ya | ✗ Tidak bisa |

---

> **Quick Check** — Sebelum melanjutkan:
> *Kembali ke kasus e-commerce di hook. Dari tiga metode di atas, metode mana yang seharusnya digunakan untuk mendeteksi masalah de-skilling sebelum atau sesegera mungkin setelah peluncuran? Dan bagaimana kamu mendesain studinya?*

---

## Analisis Kasus

Dengan matriks pemilihan metode, kita bisa mengevaluasi kegagalan tim e-commerce secara sistematis:

Tim menggunakan **think-aloud dalam satu sesi lab** — tepat untuk mengukur usability dan mental model awal. Task completion rate 94% adalah hasil yang akurat dan valid untuk pertanyaan yang ditanyakan metode itu.

Yang tidak ditanya — dan tidak bisa dijawab oleh metode itu — adalah: "Apa yang terjadi pada perilaku pengguna setelah menggunakan fitur ini selama tiga bulan?"

Metode yang seharusnya ditambahkan: **field study longitudinal** selama 4-8 minggu setelah soft launch pada subset pengguna, mengukur:
- Perubahan dalam pola eksplorasi produk (apakah pengguna mulai lebih bergantung pada rekomendasi dan kurang menjelajahi sendiri?)
- Kualitas keputusan pembelian (apakah produk yang dibeli via rekomendasi AI menghasilkan tingkat kepuasan yang sama, lebih tinggi, atau lebih rendah dari pembelian tanpa rekomendasi?)
- Kalibrasi kepercayaan: apakah pengguna yang mengandalkan rekomendasi lebih sering kecewa?

Ini bukan kegagalan tim — ini adalah gap sistemik dalam pemahaman tentang kapan metode evaluasi yang berbeda dibutuhkan.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Untuk setiap fitur AI baru, buat matriks evaluasi sederhana: pertanyaan evaluasi apa yang perlu dijawab, dan metode mana yang bisa menjawabnya? Jika semua pertanyaan dijawab hanya dengan satu metode, kamu kemungkinan melewatkan dimensi penting dari evaluasi. Biasanya, kombinasi minimal yang efektif adalah: think-aloud (mental model, eksplanabilitas) + field study pendek (kepercayaan dan perubahan perilaku).

**Jika kamu UX researcher atau designer:**
Perluas toolkit evaluasi melampaui usability testing. Untuk produk AI, kemampuan merancang WoZ study dan field study longitudinal adalah kompetensi yang semakin kritis — dan belum banyak dipahami oleh peneliti UX yang latar belakangnya lebih ke produk non-AI.

**Jika kamu developer atau engineer:**
Bangun infrastruktur logging yang mendukung field study dari hari pertama: log tidak hanya interaksi pengguna dengan AI, tapi juga perilaku yang mendahului dan mengikutinya. Perubahan dalam pola perilaku — seperti penurunan eksplorasi mandiri — tidak terlihat tanpa data kontekstual yang komprehensif.

---

## Pertanyaan Refleksi

> Setiap metode evaluasi menjawab pertanyaan yang berbeda — dan tidak ada satu metode yang cukup untuk semua pertanyaan.
>
> **Untuk produk AI yang kamu analisis sepanjang kursus ini**, pertanyaan evaluasi terpenting apa yang belum pernah dijawab secara sistematis? Dan dari tiga metode di atas, mana yang paling tepat untuk menjawabnya? Apa yang menghalangi penggunaannya?

---

## Ringkasan Lesson

- Produk AI membutuhkan evaluasi yang melampaui usability testing standar karena mereka mempengaruhi kepercayaan, keputusan, dan perilaku dengan cara yang tidak terlihat dalam satu sesi lab.
- Tiga metode utama dengan keunggulan berbeda: think-aloud (mental model dan eksplanabilitas), Wizard of Oz (pengujian konsep sebelum sistem dibangun), dan field study longitudinal (efek jangka menengah dan perubahan kepercayaan).
- Pemilihan metode harus berdasarkan pertanyaan evaluasi yang perlu dijawab — bukan kebiasaan atau kemudahan.
- Kasus e-commerce menunjukkan konsekuensi nyata dari menggunakan metode yang tepat untuk pertanyaan yang salah: evaluasi lulus, tapi masalah nyata tidak terdeteksi sampai setelah dampak terjadi.
- Lesson berikutnya akan membahas instrumen spesifik untuk mengukur satu dimensi yang paling sering tidak terukur: kepercayaan pengguna.

---

## Referensi

- Ericsson, K. A., & Simon, H. A. (1993). *Protocol Analysis: Verbal Reports as Data* (rev. ed.). MIT Press.
- Nielsen, J. (1994). Usability inspection methods. *CHI '94 Conference Companion*, 413–414.
- Kelley, J. F. (1984). An iterative design methodology for user-friendly natural language office information applications. *ACM Transactions on Information Systems*, 2(1), 26–41.
- Dahlbäck, N., Jönsson, A., & Ahrenberg, L. (1993). Wizard of Oz studies — why and how. *Knowledge-Based Systems*, 6(4), 258–266.
- Yang, Q., et al. (2020). Re-examining whether, why, and how human-AI interaction is uniquely difficult to design. *CHI '20 Proceedings*.
- Amershi, S., et al. (2019). Guidelines for human-AI interaction. *CHI '19 Proceedings*, Paper 3.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
