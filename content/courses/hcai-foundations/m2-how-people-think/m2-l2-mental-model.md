---
course: hcai-foundations
module: 2
module_title: "How People Think About and Trust AI"
lesson: 2
title: "Mental Model: Gambaran AI di Kepala Penggunamu — dan Bagaimana Membentuknya"
duration_minutes: 12
bloom_level: understand
keywords:
  - mental model AI interface design
  - user mental model AI
  - cognitive representation AI
  - designing AI mental models
  - AI user expectations
is_free: true
status: draft
---

# Mental Model: Gambaran AI di Kepala Penggunamu — dan Bagaimana Membentuknya

**Modul 2 · How People Think About and Trust AI** · Lesson 2 dari 4
**Estimasi waktu baca:** 12 menit · **Level:** Foundational · **Prasyarat:** M2-L1

---

> **Yang akan kamu capai di lesson ini:**
> - Menjelaskan apa itu mental model dan mengapa ia relevan untuk desain sistem AI
> - Mengklasifikasikan tiga jenis mental model gap yang paling umum dalam interaksi manusia-AI
> - Mendeskripsikan strategi desain konkret untuk membentuk mental model yang lebih akurat pada pengguna

---

## Hook

Pada 2019, penelitian yang diterbitkan di *JAMA Internal Medicine* (Khoong et al., 2019) menganalisis terjemahan instruksi medis pasien menggunakan sistem mesin terjemahan yang umum digunakan. Hasilnya mengkhawatirkan: 8 dari 10 instruksi yang diuji mengandung setidaknya satu kesalahan yang dinilai berpotensi membahayakan — bukan karena sistem menghasilkan output yang terlihat salah, melainkan karena outputnya terlihat *benar*.

Para pasien yang menerimanya tidak memiliki alasan untuk curiga. Kalimat-kalimatnya terbaca normal, formatnya profesional. Tapi di balik kelancaran itu, instruksi tentang dosis obat, frekuensi pemberian, dan kondisi darurat mengandung nuansa yang salah secara medis — nuansa yang hanya akan terdeteksi oleh seseorang yang memahami terminologi klinis dalam kedua bahasa sekaligus.

Yang membuat kasus ini sangat instruktif: para pengguna awal sistem terjemahan ini — staf klinis yang menggunakannya untuk berkomunikasi dengan pasien — membawa mental model yang keliru sejak awal. Mereka mengasumsikan bahwa sistem menghasilkan terjemahan setara dengan yang dilakukan penerjemah manusia terlatih. Dalam kenyataannya, sistem menghasilkan *terjemahan yang secara statistik probable* — dua hal yang sangat berbeda, terutama ketika nyawa bergantung pada ketepatan nuansa.

Ini adalah contoh paling tepat dari apa yang akan kita pelajari di lesson ini: **mental model yang salah tentang kemampuan AI tidak hanya mengecewakan — ia bisa berbahaya. Dan kesalahannya hampir tidak pernah terletak pada pengguna.**

---

## Kerangka Konseptual

### Mental model: definisi yang bekerja

Philip Johnson-Laird, psikolog kognitif yang mempopulerkan konsep ini, mendefinisikan mental model sebagai representasi internal yang disederhanakan dari bagaimana sesuatu bekerja di dunia nyata (Johnson-Laird, 1983).

Mental model bukan peta yang akurat. Ia selalu:
- **Tidak lengkap** — hanya mencakup aspek yang relevan dari sudut pandang penggunanya
- **Fungsional** — cukup akurat untuk memungkinkan tindakan sehari-hari
- **Dinamis** — berubah seiring pengalaman baru

Dalam konteks AI, mental model pengguna adalah jawaban mereka — biasanya implisit dan tidak pernah diartikulasikan — terhadap pertanyaan: *"Bagaimana sistem ini bekerja, apa yang ia bisa lakukan, dan kapan ia bisa salah?"*

### Tiga jenis mental model gap dalam interaksi manusia-AI

Penelitian dalam HCI dan AI menunjukkan tiga gap yang paling konsisten muncul antara mental model pengguna dan cara sistem AI sebenarnya bekerja:

**Gap 1 — Capability gap: pengguna terlalu melebih-lebihkan atau meremehkan kemampuan sistem**

Ini adalah gap yang paling sering ditemukan. Pengguna yang belum pernah berinteraksi dengan sistem AI tertentu cenderung memiliki ekspektasi yang sangat tinggi di satu dimensi ("AI ini pasti tahu semua hal tentang topik ini") dan sangat rendah di dimensi lain ("AI tidak mungkin bisa memahami nuansa bahasa daerah saya").

Keduanya adalah miskalibrasi yang berbahaya. Ekspektasi terlalu tinggi menghasilkan kepercayaan berlebihan — pengguna tidak memeriksa output dengan kritis. Ekspektasi terlalu rendah menghasilkan penolakan — pengguna menghindari sistem bahkan ketika sistem itu bisa membantu.

**Gap 2 — Transparency gap: pengguna tidak tahu faktor apa yang mempengaruhi output**

Pengguna tahu *bahwa* sistem menghasilkan output tertentu, tapi tidak tahu *mengapa*. Mereka tidak tahu variabel apa yang digunakan, data apa yang menjadi basis, atau kondisi apa yang membuat output lebih atau kurang reliabel.

Tanpa pemahaman ini, pengguna tidak bisa menggunakan sistem secara cerdas — mereka tidak tahu kapan harus lebih percaya dan kapan harus lebih skeptis. Semua output diperlakukan sama, padahal reliabilitas output sangat bervariasi tergantung konteks.

**Gap 3 — Agency gap: pengguna tidak memahami batas otonomi sistem**

Ini adalah gap yang paling berbahaya untuk keputusan berisiko tinggi. Pengguna tidak memahami sejauh mana sistem beroperasi secara independen versus membutuhkan validasi manusia. Apakah rekomendasi ini sudah final atau hanya titik awal? Apakah sistem ini "memutuskan" atau "menyarankan"?

Kasus perawat di lesson sebelumnya adalah contoh klasik agency gap: mereka tidak memahami bahwa sistem rekomenasi dosis adalah alat bantu yang membutuhkan validasi manusia — bukan otoritas independen.

### Bagaimana desainer bisa membentuk mental model yang akurat

Mental model tidak terbentuk dari dokumen FAQ yang panjang atau tooltip tersembunyi. Ia terbentuk dari **interaksi langsung dengan sistem** — bagaimana sistem bereaksi, apa yang ia katakan tentang dirinya sendiri, dan bagaimana ia menangani momen-momen kritis.

Tiga strategi yang terbukti efektif dalam HCI research:

**Strategi 1 — Onboarding yang jujur tentang batas sistem**
Daripada hanya menunjukkan apa yang sistem *bisa* lakukan, onboarding yang efektif juga secara eksplisit menunjukkan apa yang sistem *tidak bisa* lakukan — dan dalam kondisi apa. Ini menciptakan mental model yang lebih akurat sejak interaksi pertama.

**Strategi 2 — Indikator keyakinan (confidence indicators) yang bermakna**
Sistem AI yang menampilkan satu output tanpa indikasi tingkat kepercayaan mendorong pengguna untuk memperlakukan semua output sebagai sama-sama reliabel. Indikator keyakinan — seberapa yakin sistem terhadap outputnya — membantu pengguna mengkalibrasi kepercayaan mereka secara proporsional.

**Strategi 3 — Isyarat penjelasan (explanation cues) di momen kritis**
Ketika sistem membuat keputusan atau rekomendasi yang penting, satu kalimat penjelasan singkat ("Rekomendasi ini berdasarkan riwayat transaksi 90 hari terakhir") secara signifikan meningkatkan akurasi mental model pengguna — tanpa perlu penjelasan teknis yang panjang.

---

> **Quick Check** — Sebelum melanjutkan:
> *Dari tiga jenis gap di atas, gap mana yang paling mungkin ada dalam produk AI yang pernah kamu gunakan atau kerjakan? Capability gap, transparency gap, atau agency gap?*

---

## Analisis Kasus

Kasus terjemahan kontrak di hook adalah contoh capability gap dan transparency gap yang terjadi bersamaan.

**Capability gap:** pengguna memiliki ekspektasi bahwa "terjemahan bagus" berarti "akurat secara hukum" — padahal keduanya adalah dimensi yang berbeda, dan sistem tidak pernah mengklaim akurasi hukum.

**Transparency gap:** pengguna tidak tahu bahwa sistem dilatih pada korpus umum yang mungkin tidak banyak mengandung teks hukum berbahasa Indonesia — yang artinya reliabilitas untuk konteks spesifik ini jauh lebih rendah dari rata-rata.

Apa yang seharusnya dilakukan sistem? Setidaknya: menampilkan confidence indicator yang lebih rendah untuk teks dengan terminologi domain-spesifik, dan menyertakan catatan bahwa untuk dokumen hukum formal, validasi profesional sangat dianjurkan.

Ini bukan perubahan besar pada model AI-nya. Ini adalah perubahan pada cara sistem mengomunikasikan kemampuan dan batasnya — yang sepenuhnya adalah keputusan desain.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Jadikan "akurasi mental model pengguna" sebagai metrik yang secara eksplisit kamu ukur. Caranya: dalam user testing, tanyakan pengguna baru untuk menjelaskan cara kerja fitur AI sebelum dan sesudah onboarding. Gap antara penjelasan mereka dan cara sistem sebenarnya bekerja adalah ukuran seberapa efektif onboarding-mu membentuk mental model yang akurat.

**Jika kamu UX researcher atau designer:**
Gunakan teknik *pemetaan model mental (mental model mapping)* dalam riset pengguna untuk AI: minta peserta menggambar atau mendeskripsikan "apa yang terjadi di dalam sistem" ketika mereka menggunakannya. Visualisasi ini sering mengungkap miskalibrasi yang tidak akan terdeteksi dengan pertanyaan langsung tentang kepuasan atau usability.

**Jika kamu developer atau engineer:**
Setiap kali kamu mempertimbangkan bagaimana sistem menangani edge case atau kondisi tidak pasti — pertanyaan bukan hanya "apa output yang benar?" tapi "bagaimana pengguna akan menginterpretasi output ini, dan apakah interpretasi itu akurat?" Jawaban pertanyaan kedua sering berbeda dari yang kamu asumsikan.

---

## Pertanyaan Refleksi

> Pilih satu sistem AI yang kamu kenal dengan baik — baik sebagai pengguna maupun sebagai orang yang terlibat dalam pembuatannya.
>
> **Bayangkan kamu adalah pengguna baru yang tidak tahu cara sistem itu bekerja.** Mental model apa yang paling mungkin kamu bentuk dari interaksi pertama? Apakah onboarding, UI copy, atau cara sistem merespons secara aktif memandu kamu ke mental model yang akurat — atau membiarkanmu menyimpulkan sendiri?

---

## Ringkasan Lesson

- Mental model adalah representasi internal yang disederhanakan tentang cara sistem bekerja — selalu tidak lengkap, tapi fungsional.
- Tiga gap paling umum: capability gap (ekspektasi kemampuan yang salah), transparency gap (tidak tahu faktor yang mempengaruhi output), dan agency gap (tidak paham batas otonomi sistem).
- Mental model tidak terbentuk dari dokumentasi — ia terbentuk dari interaksi langsung. Desainer bisa secara aktif membentuknya melalui onboarding yang jujur, confidence indicators, dan explanation cues.
- Pada lesson berikutnya, kita akan melihat bagaimana mental model yang tidak akurat berinteraksi dengan mekanisme kepercayaan — dan menghasilkan dua jenis kegagalan yang sangat berbeda: overtrust dan undertrust.

---

## Referensi

- Khoong, E. C., et al. (2019). Assessing the use of Google Translate for Spanish and Chinese translations of emergency department discharge instructions. *JAMA Internal Medicine*, 179(4), 580–582.
- Johnson-Laird, P. N. (1983). *Mental Models: Towards a Cognitive Science of Language, Inference, and Consciousness*. Harvard University Press.
- Norman, D. A. (1983). Some observations on mental models. In D. Gentner & A. Stevens (Eds.), *Mental Models*. Lawrence Erlbaum Associates.
- Kulesza, T., et al. (2013). Too much, too little, or just right? Ways explanations impact end users' mental models. *2013 IEEE Symposium on Visual Languages and Human-Centric Computing*, 3–10.
- Cai, C. J., et al. (2019). Human-centered tools for coping with imperfect algorithms during medical decision-making. *CHI 2019*.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
