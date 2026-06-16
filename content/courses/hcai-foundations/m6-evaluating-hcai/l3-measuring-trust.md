---
course: hcai-foundations
module: 6
module_title: "Evaluating and Improving HCAI Systems"
lesson: 3
title: "Mengukur Kepercayaan Pengguna pada AI: Instrumen dan Pendekatan yang Tervalidasi"
duration_minutes: 12
bloom_level: evaluate
keywords:
  - AI trust measurement scale
  - trust in automation instrument
  - user trust AI survey
  - trust calibration measurement
  - human-AI trust evaluation
is_free: true
status: draft
---

# Mengukur Kepercayaan Pengguna pada AI: Instrumen dan Pendekatan yang Tervalidasi

**Modul 6 · Evaluating and Improving HCAI Systems** · Lesson 3 dari 4
**Estimasi waktu baca:** 12 menit · **Level:** Foundational · **Prasyarat:** M6-L2

---

> **Yang akan kamu capai di lesson ini:**
> - Mengevaluasi kelebihan dan keterbatasan instrumen pengukuran kepercayaan yang tersedia untuk konteks AI
> - Menilai perbedaan antara mengukur kepercayaan sebagai sikap dan mengukur kalibrasi kepercayaan sebagai perilaku
> - Merekomendasikan pendekatan pengukuran kepercayaan yang sesuai untuk konteks produk AI yang berbeda

---

## Hook

Sebuah tim yang baru saja meluncurkan sistem AI diagnostik untuk klinik primer merancang survei kepuasan yang mencakup pertanyaan kepercayaan. Hasilnya: 82% pengguna menyatakan "percaya" atau "sangat percaya" pada sistem.

Tim senang. Mereka mempublikasikan angka ini sebagai bukti adopsi yang sukses.

Tiga bulan kemudian, analisis log menunjukkan pola yang berbeda: 78% dari kasus di mana sistem AI memberikan saran yang berbeda dari diagnosis awal dokter, saran AI diabaikan tanpa didokumentasikan. Tapi dari subset kasus yang diaudit secara mendalam, 40% dari kasus di mana dokter mengabaikan saran AI ternyata saran AI lebih akurat.

Ada kontradiksi yang sangat jelas: pengguna melaporkan *percaya* pada sistem, tapi *berperilaku* seperti tidak percaya.

Ini bukan karena dokternya berbohong dalam survei. Ini karena **kepercayaan yang dilaporkan sebagai sikap berbeda dari kepercayaan yang terekspresi sebagai perilaku** — dan mengukur hanya salah satunya memberikan gambaran yang sangat tidak lengkap.

*Skenario ini adalah komposit representatif dari pola yang terdokumentasi dalam penelitian kalibrasi kepercayaan — termasuk dalam Parasuraman & Manzey (2010) dan Schaefer et al. (2016). Angka-angka spesifik bersifat ilustratif.*

---

## Kerangka Konseptual

### Dua dimensi kepercayaan yang sering dikonfusikan

Dari M2-L3, kita sudah membahas kalibrasi kepercayaan sebagai konsep. Di lesson ini, kita masuk ke pertanyaan yang lebih operasional: bagaimana mengukurnya?

Penting untuk membedakan dua dimensi yang berbeda:

**Kepercayaan sebagai sikap (attitude-based trust):**
Seberapa positif pengguna menilai sistem — apakah mereka percaya sistem kompeten, dapat diandalkan, dan bermaksud baik. Ini adalah kepercayaan yang diukur oleh sebagian besar survei: "Seberapa besar kamu mempercayai sistem ini?"

Kepercayaan sikap penting tapi tidak cukup. Seseorang bisa memiliki sikap positif terhadap sistem (menganggapnya berguna secara umum) sambil tetap tidak mengandalkannya untuk keputusan spesifik.

**Kepercayaan sebagai perilaku (behavior-based trust):**
Sejauh mana pengguna *bertindak* berdasarkan rekomendasi sistem — seberapa sering mereka mengikutinya, kapan mereka mengabaikannya, dan bagaimana mereka mengintegrasikan output sistem ke dalam pengambilan keputusan mereka.

Untuk tujuan evaluasi HCAI, kepercayaan perilaku lebih penting dari kepercayaan sikap — karena kepercayaan perilaku yang menentukan apakah sistem berfungsi sebagaimana dirancang dalam kondisi nyata.

### Kalibrasi kepercayaan: ukuran yang paling relevan

Di atas dua dimensi ini, ada konsep yang paling relevan untuk evaluasi HCAI: **kalibrasi kepercayaan** — sejauh mana tingkat kepercayaan pengguna proporsional dengan kemampuan sistem yang sebenarnya.

Sistem yang dikalibrasi dengan baik menghasilkan:
- Pengguna yang mengikuti rekomendasi AI *ketika AI reliabel* untuk konteks itu
- Pengguna yang mengevaluasi kritis *ketika AI kurang reliabel*
- Pengguna yang tahu perbedaannya

Ini adalah ukuran yang jauh lebih berguna dari sekadar "seberapa besar kepercayaan" — karena kepercayaan yang sangat tinggi pada sistem yang tidak reliabel sama berbahayanya dengan kepercayaan yang sangat rendah pada sistem yang reliabel (dari M2-L3).

### Instrumen yang tersedia: apa yang tervalidasi

<!-- DIAGRAM: Spektrum instrumen pengukuran kepercayaan AI
     Render sebagai tabel perbandingan saat membangun UI.
     Kolom: Instrumen | Fokus | Jumlah item | Kelebihan | Keterbatasan
     Baris:
     1. Jian et al. (2000) — Kepercayaan sikap pada sistem otomasi — 12 item
     2. Checklist perilaku — Override rate, follow rate, task performance — Berbasis log
     3. Verbal protocol — Kalibrasi momen per momen — Kualitatif
     Sorot: tidak ada instrumen tunggal yang mengukur kalibrasi secara langsung
-->

**Instrumen 1 — Jian, Bisantz & Drury (2000): Skala kepercayaan pada sistem otomasi**

Ini adalah instrumen yang paling banyak dikutip untuk mengukur kepercayaan pada sistem otomasi. Instrumen 12-item ini mengukur kepercayaan sikap pada dua dimensi: *trust* (kepercayaan positif) dan *distrust* (ketidakpercayaan aktif) — yang secara empiris terbukti sebagai dua konstruk yang berbeda, bukan sekadar ujung berlawanan dari satu kontinum.

*Kelebihan:* Tervalidasi secara psikometrik, relatif singkat (dapat diselesaikan dalam 2-3 menit), dan didesain spesifik untuk sistem otomasi bukan hanya teknologi secara umum.

*Keterbatasan:* Mengukur kepercayaan sikap umum terhadap sistem — tidak menangkap variasi kepercayaan berdasarkan jenis keputusan atau kondisi penggunaan. Tidak mengukur kalibrasi.

*Referensi:* Jian, J.-Y., Bisantz, A. M., & Drury, C. G. (2000). Foundations for an empirically determined scale of trust in automated systems. *International Journal of Cognitive Ergonomics*, 4(1), 53–71.

**Instrumen 2 — Pendekatan berbasis perilaku (log analysis)**

Kepercayaan perilaku tidak bisa diukur dengan survei — ia harus diukur dari data sistem. Tiga metrik perilaku yang paling informatif:

- **Tingkat penerimaan rekomendasi (recommendation acceptance rate):** Berapa persen rekomendasi AI yang diikuti pengguna? Terlalu tinggi (>90%) bisa mengindikasikan overtrust; terlalu rendah (<30%) bisa mengindikasikan undertrust.
- **Pola override:** Kapan dan dalam kondisi apa pengguna mengabaikan rekomendasi AI? Analisis ini mengungkap apakah override terjadi secara acak atau sistematis berdasarkan jenis keputusan.
- **Perbandingan kualitas keputusan:** Apakah keputusan yang dibuat *dengan* bantuan AI menghasilkan outcomes yang lebih baik dari keputusan yang dibuat *tanpa* bantuan AI? Ini adalah ukuran kalibrasi yang paling langsung tapi juga paling sulit diukur.

**Instrumen 3 — Protokol verbal dan wawancara terstruktur**

Untuk memahami *mengapa* pengguna mempercayai atau tidak mempercayai sistem dalam kondisi tertentu, data kuantitatif tidak cukup. Wawancara terstruktur yang mengeksplorasi episode keputusan spesifik — "Ceritakan tentang satu momen ketika kamu memutuskan untuk tidak mengikuti rekomendasi sistem" — memberikan data yang kaya tentang proses kalibrasi yang tidak terlihat dalam survei atau log.

### Pendekatan tiga-sumber untuk evaluasi kepercayaan yang komprehensif

Tidak ada satu instrumen yang mengukur semua aspek kepercayaan yang relevan untuk HCAI. Pendekatan yang paling komprehensif menggabungkan:

1. **Survei sikap** (Jian et al., 2000 atau instrumen serupa) → mengukur kepercayaan umum
2. **Analisis log perilaku** → mengukur kepercayaan aktual dalam penggunaan
3. **Wawancara episodik** → memahami kondisi yang mempengaruhi kalibrasi

Perbedaan antara sumber 1 dan 2 adalah sinyal diagnostik yang sangat berharga: jika kepercayaan sikap tinggi tapi perilaku menunjukkan undertrust, ada faktor kontekstual yang perlu dieksplorasi (biasanya melalui sumber 3).

---

> **Quick Check** — Sebelum melanjutkan:
> *Kembali ke kasus klinik di hook. Dari tiga sumber pengukuran, sumber mana yang memberikan gambaran paling akurat tentang situasi yang sebenarnya terjadi? Dan mengapa hanya menggunakan sumber 1 (survei) memberikan gambaran yang menyesatkan?*

---

## Analisis Kasus

Kasus klinik dengan kontradiksi "percaya tapi tidak mengikuti":

**Sumber 1 (survei):** 82% percaya atau sangat percaya. Ini adalah data yang valid — pengguna memang memiliki sikap positif. Tapi survei tidak menangkap kondisi di mana kepercayaan itu runtuh.

**Sumber 2 (log perilaku):** 78% saran AI diabaikan saat berbeda dari diagnosis awal dokter. Ini mengungkap undertrust yang tidak terlihat dalam survei. Lebih jauh: perbandingan dengan audit kualitas keputusan menunjukkan bahwa 40% dari kasus yang diabaikan seharusnya diikuti.

**Sumber 3 (wawancara):** Jika dilakukan, kemungkinan akan mengungkap akar penyebab: mungkin dokter tidak memahami dalam kondisi apa sistem lebih akurat (mental model gap dari M2), atau mungkin tidak ada mekanisme yang memudahkan dokter untuk mendokumentasikan alasan override (accountability gap dari M3-L4).

Dengan data dari tiga sumber, tim bisa mendiagnosis masalah spesifik dan merancang intervensi yang tepat — bukan hanya merayakan angka survei yang tinggi.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Jangan pernah melaporkan "tingkat kepercayaan pengguna" hanya berdasarkan survei. Selalu kombinasikan dengan setidaknya satu metrik perilaku dari log. Perbedaan antara keduanya adalah informasi yang paling berharga yang bisa kamu miliki tentang kalibrasi kepercayaan pengguna.

**Jika kamu UX researcher atau designer:**
Rancang studi evaluasi kepercayaan dengan pertanyaan eksplisit tentang episode keputusan spesifik — bukan hanya penilaian umum. "Seberapa kamu percaya sistem ini?" jauh kurang informatif dari "Ceritakan tiga momen ketika kamu memutuskan untuk tidak mengikuti saran sistem, dan mengapa."

**Jika kamu developer atau engineer:**
Bangun kemampuan untuk melacak dan menganalisis pola override sejak awal. Ini bukan hanya berguna untuk debugging — ini adalah metrik kalibrasi kepercayaan yang paling langsung. Override rate yang terlalu tinggi atau terlalu rendah, atau override yang terpola berdasarkan kondisi tertentu, adalah sinyal yang membutuhkan investigasi.

---

## Pertanyaan Refleksi

> Kasus klinik menunjukkan bahwa kepercayaan yang dilaporkan dan kepercayaan yang diperagakan bisa bertolak belakang — dan mengukur hanya salah satunya bisa menyesatkan keputusan produk.
>
> **Untuk produk AI yang kamu analisis**, kepercayaan yang bagaimana yang lebih mudah diukur saat ini — sikap atau perilaku? Dan sumber mana yang paling sering tidak tersedia — dan mengapa tidak tersedia?

---

## Ringkasan Lesson

- Kepercayaan sebagai sikap (apa yang pengguna katakan) berbeda dari kepercayaan sebagai perilaku (apa yang pengguna lakukan) — dan kalibrasi kepercayaan (seberapa proporsional kepercayaan dengan kemampuan sistem) adalah ukuran yang paling relevan untuk HCAI.
- Jian et al. (2000) adalah instrumen tervalidasi untuk kepercayaan sikap pada sistem otomasi; analisis log memberikan data kepercayaan perilaku; wawancara episodik mengungkap kondisi yang mempengaruhi kalibrasi.
- Pendekatan tiga sumber memberikan gambaran paling komprehensif. Perbedaan antara sumber 1 (survei) dan sumber 2 (log) adalah sinyal diagnostik yang paling berharga.
- Lesson terakhir adalah capstone — saatnya menggabungkan semua yang dipelajari sepanjang kursus ini dalam satu evaluasi terintegrasi.

---

## Referensi

- Jian, J.-Y., Bisantz, A. M., & Drury, C. G. (2000). Foundations for an empirically determined scale of trust in automated systems. *International Journal of Cognitive Ergonomics*, 4(1), 53–71.
- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50–80.
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation. *Human Factors*, 52(3), 381–410.
- Madsen, M., & Gregor, S. (2000). Measuring human-computer trust. *Proceedings of the 11th Australasian Conference on Information Systems*, 6–8.
- Schaefer, K. E., et al. (2016). A meta-analysis of factors influencing the development of trust in automation. *Human Factors*, 58(3), 377–400.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
