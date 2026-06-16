---
course: hcai-foundations
module: 6
module_title: "Evaluating and Improving HCAI Systems"
lesson: 1
title: "Akurasi Model Bukan Ukuran Keberhasilan: Apa yang Sebenarnya Perlu Diukur"
duration_minutes: 12
bloom_level: evaluate
keywords:
  - AI evaluation metrics
  - human-AI performance measurement
  - AI success criteria
  - beyond accuracy AI evaluation
  - human-centered AI metrics
is_free: true
status: draft
---

# Akurasi Model Bukan Ukuran Keberhasilan: Apa yang Sebenarnya Perlu Diukur

**Modul 6 · Evaluating and Improving HCAI Systems** · Lesson 1 dari 4
**Estimasi waktu baca:** 12 menit · **Level:** Foundational · **Prasyarat:** M1-L1 s/d M5-L4

---

> **Yang akan kamu capai di lesson ini:**
> - Mengevaluasi kecukupan metrik teknis standar (akurasi, presisi, recall) untuk mengukur keberhasilan sistem AI yang melibatkan manusia
> - Menilai trade-off antara metrik model dan metrik human-centered untuk konteks penggunaan yang berbeda
> - Merekomendasikan set metrik yang tepat untuk mengevaluasi sistem HCAI berdasarkan konteks dan taruhannya

---

## Hook

2015. Sebuah tim peneliti di Microsoft Research membangun model AI untuk memprediksi risiko kematian pasien pneumonia — untuk membantu rumah sakit memprioritaskan pasien yang membutuhkan perawatan intensif.

Model mereka mencapai akurasi yang tinggi. Evaluasi teknis berhasil.

Tapi ketika tim mulai memeriksa *apa yang dipelajari model* — bukan hanya seberapa akurat prediksinya — mereka menemukan sesuatu yang berbahaya. Model telah belajar bahwa pasien asma yang terdiagnosis pneumonia memiliki risiko kematian yang *lebih rendah* dan seharusnya mendapat prioritas lebih rendah.

Secara teknis, model itu benar berdasarkan data. Pasien asma dengan pneumonia memang memiliki tingkat kematian lebih rendah dalam data historis — tapi bukan karena kondisi mereka kurang parah. Justru sebaliknya: karena mereka *diketahui berisiko tinggi*, mereka selalu mendapat perawatan yang lebih agresif dan karenanya survive lebih baik. Model belajar dari hasil yang sudah terdistorsi oleh intervensi medis.

Jika model ini diluncurkan tanpa pemeriksaan lebih lanjut, ia akan secara sistematis de-prioritaskan pasien yang paling membutuhkan perawatan intensif — berdasarkan akurasi prediksi yang tinggi terhadap data yang salah ditafsirkan.

Tim menangkap ini karena mereka tidak berhenti di metrik akurasi. Mereka bertanya: *"Apa yang sebenarnya dipelajari model ini, dan apa konsekuensinya bagi manusia yang terdampak?"* (Caruana et al., 2015).

---

## Kerangka Konseptual

### Mengapa akurasi tidak cukup sebagai satu-satunya ukuran

Metrik teknis standar — akurasi, presisi, *recall*, F1 score — menjawab satu pertanyaan dengan sangat baik: *"Seberapa sering model memprediksi label yang benar pada data uji?"*

Yang tidak mereka jawab:
- Apakah prediksi yang benar menghasilkan keputusan yang baik oleh manusia yang menggunakannya?
- Apakah kesalahan terjadi secara merata di semua kelompok pengguna?
- Apakah pengguna mempercayai sistem secara proporsional dengan kemampuannya yang sebenarnya?
- Apakah sistem membantu manusia mencapai tujuan mereka — atau justru mengganggu?

Dari M3, kita sudah tahu bahwa Accountability membutuhkan evaluasi terhadap outcomes nyata, bukan hanya metrik sistem. Dari M4, kita tahu bahwa disagregasi metrik adalah minimum yang diperlukan. M6-L1 adalah tentang membangun kerangka evaluasi yang komprehensif dari pelajaran-pelajaran itu.

### Empat dimensi evaluasi yang sering terlewat

<!-- DIAGRAM: Empat Dimensi Evaluasi HCAI
     Render sebagai diagram empat kuadran saat membangun UI.
     Sumbu X: Teknis ← → Manusia
     Sumbu Y: Proses ← → Outcomes
     Kuadran 1 (kiri-atas, Teknis+Proses): Metrik model (akurasi, F1, AUC)
     Kuadran 2 (kanan-atas, Manusia+Proses): Metrik interaksi (usability, task completion, trust calibration)
     Kuadran 3 (kiri-bawah, Teknis+Outcomes): Metrik sistem (latency, uptime, error rate)
     Kuadran 4 (kanan-bawah, Manusia+Outcomes): Metrik dampak (kualitas keputusan, keadilan, wellbeing)
     Highlight: sebagian besar tim hanya mengukur Kuadran 1 dan 3
-->

**Dimensi 1 — Metrik model (sudah umum dilakukan):**
Akurasi, presisi, recall, F1, AUC-ROC. Perlu dilakukan, tapi tidak cukup. Harus selalu didisagregasi per subkelompok populasi (dari M4-L3).

**Dimensi 2 — Metrik interaksi manusia-AI:**
Seberapa efektif manusia berinteraksi dengan sistem? Ini mencakup: tingkat penyelesaian tugas (*task completion rate*), waktu pengambilan keputusan, tingkat override (seberapa sering manusia mengabaikan rekomendasi AI), dan kalibrasi kepercayaan.

Yang paling jarang diukur tapi paling penting: **kualitas keputusan manusia dengan AI dibanding tanpa AI.** Bukan hanya apakah mereka menggunakan AI, tapi apakah penggunaan AI membuat keputusan mereka lebih baik.

**Dimensi 3 — Metrik sistem operasional:**
Latensi, ketersediaan, tingkat kesalahan teknis, drift model seiring waktu. Penting untuk reliability tapi sering diperlakukan sebagai satu-satunya metrik engineering.

**Dimensi 4 — Metrik dampak pada manusia (paling jarang diukur):**
Apakah sistem meningkatkan kualitas hidup atau outcomes nyata bagi penggunanya? Apakah ia bekerja setara untuk semua kelompok yang dilayaninya? Apakah ada efek tidak diinginkan — seperti de-skilling (manusia kehilangan kemampuan karena terlalu bergantung pada AI)?

### Kerangka evaluasi dua-tingkat

Untuk sistem AI yang melibatkan manusia, evaluasi yang komprehensif membutuhkan setidaknya dua tingkat:

**Tingkat 1 — Evaluasi sistem:** Apakah model bekerja secara teknis sebagaimana dirancang? (Dimensi 1 dan 3)

**Tingkat 2 — Evaluasi sistem-dalam-konteks:** Apakah sistem membantu manusia membuat keputusan yang lebih baik dalam kondisi penggunaan nyata? (Dimensi 2 dan 4)

Tingkat 2 tidak bisa dilakukan hanya dengan data log. Ia membutuhkan riset pengguna, studi lapangan, dan evaluasi yang melibatkan manusia nyata dalam kondisi nyata — tema yang akan kita bahas di L2.

---

> **Quick Check** — Sebelum melanjutkan:
> *Kembali ke kasus pneumonia di hook. Model yang memiliki akurasi tinggi tapi belajar pola berbahaya — dari keempat dimensi evaluasi, dimensi mana yang akan mendeteksi masalah ini? Dan dimensi mana yang akan gagal mendeteksinya?*

---

## Analisis Kasus

Dengan kerangka dua tingkat, kita bisa mengevaluasi kasus pneumonia secara sistematis:

**Tingkat 1 — Evaluasi sistem:**
Model lulus di semua metrik standar. Akurasi tinggi. Presisi dan recall baik. Tidak ada kesalahan teknis yang terdeteksi. Evaluasi tingkat 1 tidak akan menemukan masalah apapun.

**Tingkat 2 — Evaluasi sistem-dalam-konteks:**
Di sinilah masalah terdeteksi. Pertanyaan yang diajukan: *"Apa yang sebenarnya dipelajari model, dan apa konsekuensinya bagi pasien nyata?"* Ini adalah pertanyaan Dimensi 4 — metrik dampak pada manusia — yang tidak bisa dijawab dengan metrik teknis saja.

Metrik yang seharusnya ada: *analisis ketidaksepakatan* (*disagreement analysis*) — perbandingan antara rekomendasi model dan penilaian dokter ahli pada kasus yang sama, dengan fokus khusus pada kasus di mana keduanya berbeda. Analisis semacam ini secara sistematis mengekspos pola seperti yang ditemukan di kasus asma.

Ini bukan hanya pelajaran tentang evaluasi model. Ini adalah pelajaran tentang governance: sistem yang tidak dievaluasi pada Dimensi 4 sebelum diluncurkan adalah sistem yang secara aktif menghindari pertanyaan paling penting tentang dampaknya.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Sebelum menetapkan kriteria sukses untuk fitur AI, pastikan keempat dimensi terwakili dalam definisi sukses. Kriteria sukses yang hanya mencakup Dimensi 1 (metrik model) dan 3 (sistem operasional) adalah kriteria yang secara aktif menghindari pertanyaan tentang dampak pada pengguna.

**Jika kamu UX researcher atau designer:**
Dimensi 2 adalah domain utamamu — dan sering menjadi dimensi yang paling berkontribusi pada evaluasi yang komprehensif. Rancang evaluasi yang mengukur bukan hanya "apakah pengguna bisa menggunakan sistem" tapi "apakah sistem membantu pengguna membuat keputusan yang lebih baik."

**Jika kamu developer atau engineer:**
Tambahkan Dimensi 2 ke dalam definisi "done" untuk setiap fitur AI. Sebelum fitur dianggap selesai, harus ada bukti bahwa ia meningkatkan — atau setidaknya tidak memperburuk — kualitas keputusan manusia yang menggunakannya.

---

## Pertanyaan Refleksi

> Kasus pneumonia menunjukkan bahwa model yang lulus semua evaluasi teknis bisa berbahaya karena tidak ada yang mengajukan pertanyaan tingkat 2.
>
> **Pikirkan satu produk AI yang kamu kenal.** Dari keempat dimensi evaluasi, dimensi mana yang saat ini diukur? Dimensi mana yang tidak? Dan apa konsekuensi potensial dari dimensi yang tidak diukur itu jika sistem terus beroperasi?

---

## Ringkasan Lesson

- Akurasi dan metrik teknis lainnya menjawab pertanyaan penting tapi tidak cukup — mereka hanya mengukur dua dari empat dimensi yang diperlukan untuk evaluasi HCAI yang komprehensif.
- Empat dimensi: metrik model, metrik interaksi manusia-AI, metrik sistem operasional, dan metrik dampak pada manusia. Tim yang hanya mengukur dimensi 1 dan 3 secara aktif menghindari pertanyaan terpenting.
- Kerangka dua tingkat: evaluasi sistem (teknis) dan evaluasi sistem-dalam-konteks (manusia). Tingkat 2 membutuhkan metode evaluasi yang berbeda dari tingkat 1 — yang akan dibahas di lesson berikutnya.
- Kasus pneumonia membuktikan bahwa evaluasi tingkat 2 bukan "nice to have" — ini adalah perlindungan minimum terhadap sistem yang secara teknis benar tapi secara fungsional berbahaya.

---

## Referensi

- Caruana, R., et al. (2015). Intelligible models for healthcare: Predicting pneumonia risk and hospital 30-day readmission. *Proceedings of the 21st ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 1721–1730.
- Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press. — Bab 14–15.
- Amershi, S., et al. (2019). Software engineering for machine learning: A case study. *2019 IEEE/ACM 41st ICSE*, 291–300.
- Yang, Q., et al. (2020). Re-examining whether, why, and how human-AI interaction is uniquely difficult to design. *CHI '20 Proceedings*.
- Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning: Limitations and Opportunities*. MIT Press. — Bab tentang evaluation beyond accuracy.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
