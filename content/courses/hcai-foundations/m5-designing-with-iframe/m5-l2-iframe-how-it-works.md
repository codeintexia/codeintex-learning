---
course: hcai-foundations
module: 5
module_title: "Designing Human-Centered AI with IFRAME"
lesson: 2
title: "IFRAME: Metodologi Desain Berpusat-Manusia dari CodeinteX — Cara Kerjanya"
duration_minutes: 18
bloom_level: apply
keywords:
  - IFRAME methodology CodeinteX
  - user-flow centric design
  - HCAI design framework
  - decision orchestration AI
  - evidence governance design
is_free: true
status: draft
---

# IFRAME: Metodologi Desain Berpusat-Manusia dari CodeinteX — Cara Kerjanya

**Modul 5 · Designing Human-Centered AI with IFRAME** · Lesson 2 dari 4
**Estimasi waktu baca:** 18 menit · **Level:** Foundational · **Prasyarat:** M5-L1

---

> **Yang akan kamu capai di lesson ini:**
> - Menerapkan keenam tahap IFRAME — Identify, Flow, Rank, Apply, Measure, Expose — pada skenario desain produk AI yang nyata
> - Menggunakan konsep "alir (flow)" sebagai unit pengorganisasi sentral untuk menghubungkan semua keputusan desain
> - Membangun pemahaman tentang bagaimana IFRAME mengimplementasikan empat prinsip HCAI yang dipelajari di Modul 3

---

## Hook

Sebuah tim di perusahaan healthtech sedang membangun aplikasi pendeteksi gejala berbasis AI. Mereka menggunakan Design Thinking: empati, definisi masalah, ideasi, prototyping, testing. Prosesnya berjalan dengan baik.

Enam bulan setelah peluncuran, tim menerima laporan dari dokter mitra: pasien mulai datang dengan diagnosis mandiri yang sepenuhnya didasarkan pada output aplikasi — dan beberapa salah serius. Yang lebih mengkhawatirkan: tidak ada dalam tim yang bisa menjawab pertanyaan sederhana dari regulator kesehatan: *"Mengapa fitur ini dibangun dengan cara ini, dan siapa yang memutuskan?"*

Dokumen riset pengguna ada. Wireframe ada. Sprint reviews ada. Tapi tidak ada jejak keputusan yang terdokumentasi secara sistematis — tidak ada yang bisa menjelaskan mengapa fitur tertentu diprioritaskan di atas yang lain, mengapa tingkat kepercayaan ditampilkan dengan cara tertentu, atau apa yang tim rencanakan jika model menghasilkan rekomendasi yang berbahaya.

Tim memiliki metode desain yang baik. Yang tidak mereka miliki adalah **metodologi untuk mengorkestrasi keputusan dan mengelola bukti** di sepanjang perjalanan itu.

---

## Kerangka Konseptual

### IFRAME: posisi dan filosofi

IFRAME adalah metodologi yang berpusat pada alir (*flow-centered*) untuk mengorkestrasikan keputusan dan mengelola bukti di sepanjang siklus hidup produk digital. Ia tidak menggantikan Design Thinking, Lean UX, atau metodologi lain — ia bertindak sebagai lapisan governance yang memastikan keputusan eksplisit, trade-off terlihat, bukti terdokumentasi, dan outcomes dapat ditelusuri.

Unit pengorganisasi sentral IFRAME adalah **alir (flow)** — bukan persona, bukan fitur, bukan halaman. Alir adalah urutan kohesif dari aksi pengguna dan respons sistem yang memberikan nilai. Semua yang dikerjakan dalam IFRAME diorganisasikan di sekitar menjaga integritas alir ini.

Dokumentasi lengkap IFRAME tersedia di [codeintex.com/iframe](https://codeintex.com/iframe).

### Enam tahap IFRAME

<!-- DIAGRAM: Pipeline IFRAME
     Render sebagai diagram pipeline horizontal saat membangun UI.
     Enam kotak berurutan: Identify → Flow → Rank → Apply → Measure → Expose
     Highlight khusus pada "Flow" dengan label "Central Unit"
     Dua lapisan di bawah:
     - "Orkestrasi Keputusan" mencakup: Identify, Flow, Rank, Apply
     - "Tata Kelola Bukti" mencakup semua 6 tahap
     Warna progresif dari biru (Identify) ke hijau (Expose)
-->

**Tahap 1 — Identify (Identifikasi)**
*Pertanyaan: "Ruang masalah apa yang sedang kita hadapi?"*

Identify memetakan konteks, batasan, dan semua pemangku kepentingan secara eksplisit — termasuk yang terdampak tapi tidak terlibat langsung. Untuk produk AI, ini termasuk mengidentifikasi kelompok yang paling rentan terkena dampak sistem, asumsi kritis yang perlu divalidasi, dan batasan di mana sistem seharusnya tidak beroperasi.

Asumsi yang paling sering salah — seperti yang dipelajari di M2 — adalah asumsi tentang mental model pengguna: bahwa mereka memahami kapabilitas dan batas sistem dengan cara yang sama seperti tim pembuatnya. Identify adalah tahap di mana asumsi ini dieksplisitkan dan direncanakan untuk divalidasi, bukan dibiarkan tersembunyi sampai diluncurkan.

Koneksi ke HCAI: tahap ini adalah tempat Fairness dan Accountability dimulai — siapa yang terdampak, dan siapa yang bertanggung jawab atas keputusan sistem.

**Tahap 2 — Flow (Alir)**
*Pertanyaan: "Alir apa yang ada, dan mana yang paling penting?"*

Flow adalah tahap di mana alir-alir yang relevan dipetakan, didefinisikan, dan dipilih. Untuk produk AI, ini berarti mendefinisikan secara eksplisit di mana dalam alir pengguna keputusan AI terlibat — dan siapa yang terdampak oleh setiap titik keputusan itu.

Flow adalah tahap yang mengunci filosofi sentral IFRAME: semua keputusan berikutnya berangkat dari alir yang sudah didefinisikan, bukan dari fitur atau persona. Ini memastikan bahwa desain tidak terfragmentasi menjadi koleksi fitur tanpa kohesi.

**Tahap 3 — Rank (Prioritas)**
*Pertanyaan: "Apa yang paling penting sekarang?"*

Rank membuat trade-off eksplisit. Untuk produk AI, ini termasuk trade-off yang sangat spesifik pada AI: antara akurasi dan eksplanabilitas, antara otonomi sistem dan kontrol manusia, antara kecepatan peluncuran dan kelengkapan fairness audit.

Yang membedakan Rank dari prioritisasi backlog (*backlog prioritization*) biasa adalah kewajiban untuk mendokumentasikan *mengapa* sesuatu diprioritaskan — termasuk mengapa sesuatu *tidak* diprioritaskan. Ini adalah artefak governance yang memungkinkan tim di masa depan memahami konteks keputusan.

**Tahap 4 — Apply (Aplikasi)**
*Pertanyaan: "Bagaimana ini seharusnya diwujudkan?"*

Apply adalah implementasi — di sinilah metode spesifik (Design Thinking, engineering sprint, dll.) digunakan. IFRAME tidak mendikte cara implementasi; ia memastikan bahwa setiap keputusan implementasi dapat ditelusuri ke alir dan prioritas yang mendahuluinya.

Untuk produk AI, Apply juga adalah tempat mekanisme transparansi, kontrol manusia, dan eksplanabilitas dibangun secara konkret — bukan sebagai afterthought, melainkan sebagai bagian dari alir yang sudah didefinisikan.

**Tahap 5 — Measure (Ukur)**
*Pertanyaan: "Apakah berhasil?"*

Measure mengevaluasi output terhadap kriteria yang ditetapkan di Identify dan Rank. Untuk produk AI, ini bukan hanya evaluasi usability — ini mencakup evaluasi kalibrasi kepercayaan (*trust calibration*, apakah pengguna mempercayai sistem secara proporsional?), fairness (apakah performa konsisten di semua kelompok?), dan efektivitas kontrol manusia.

Koneksi ke modul sebelumnya: Measure adalah tempat teknik dari M4 (disagregasi, penjelasan lokal) digunakan secara sistematis.

**Tahap 6 — Expose (Ekspos)**
*Pertanyaan: "Apa yang harus dipelajari oleh tim di masa depan?"*

Expose adalah kontribusi paling distintif IFRAME. Ini bukan laporan akhir yang tidak dibaca — ini adalah konversi aktif dari pengetahuan proyek menjadi pengetahuan organisasi yang dapat dicari dan digunakan. Artefak Expose memungkinkan tim baru memahami keputusan yang dibuat tanpa harus hadir saat keputusan itu dibuat.

Untuk produk AI, Expose memiliki dimensi akuntabilitas yang kritis: dokumentasi tentang apa yang diputuskan, mengapa, dan apa hasilnya adalah fondasi dari accountability jangka panjang.

### Bagaimana IFRAME mengimplementasikan empat prinsip HCAI

| Prinsip | Tahap IFRAME | Implementasi konkret |
|---|---|---|
| Transparency | Identify, Apply, Expose | Identify memetakan siapa yang perlu tahu apa; Apply membangun mekanisme penjelasan; Expose mendokumentasikan cara kerja sistem untuk audit |
| Fairness | Identify, Flow, Measure | Identify memetakan semua kelompok terdampak; Flow mendefinisikan alir untuk semua kelompok; Measure mengevaluasi fairness secara disagregasi |
| Human Control | Flow, Apply, Measure | Flow menentukan di mana kontrol manusia dibutuhkan; Apply membangun mekanisme kontrol yang bermakna; Measure menguji apakah kontrol berfungsi dalam kondisi nyata |
| Accountability | Rank, Expose, semua | Rank mendokumentasikan trade-off; Expose mengkonversi pengetahuan jadi dapat diaudit; Keseluruhan IFRAME menciptakan jejak keputusan |

---

> **Quick Check** — Sebelum melanjutkan:
> *Kembali ke kasus healthtech di hook. Di tahap IFRAME mana seharusnya tim mendefinisikan "apa yang terjadi jika model menghasilkan rekomendasi yang salah?" — dan artefak apa yang seharusnya dihasilkan dari tahap itu?*

---

## Analisis Kasus

Kembali ke tim healthtech. Mari kita telusuri bagaimana IFRAME mengubah proses mereka:

**Identify:** Tim memetakan semua pemangku kepentingan — bukan hanya pengguna (pasien), tapi juga dokter yang merespons rekomendasi, regulator, dan keluarga pasien. Mereka mengidentifikasi asumsi kritis: "pengguna akan memahami bahwa ini adalah alat bantu, bukan diagnosis." Asumsi ini perlu divalidasi — bukan diasumsikan.

**Flow:** Tim mendefinisikan alir utama: "pasien merasakan gejala → membuka aplikasi → memasukkan gejala → menerima rekomendasi → memutuskan tindakan." Di titik "menerima rekomendasi," tim harus mendefinisikan secara eksplisit: *Apa peran AI di sini? Seberapa otonom? Bagaimana pengguna memahami batas kepercayaannya?* Ini adalah keputusan HCAI yang harus dibuat di tahap Flow, bukan di tahap implementasi.

**Rank:** Tim mendokumentasikan trade-off eksplisit: antara menghadirkan pengalaman yang mudah digunakan dan menyampaikan uncertainty model secara jujur. Mereka memilih untuk menampilkan confidence level — dan mendokumentasikan mengapa.

**Apply:** Tim membangun antarmuka dengan confidence indicator, disclaimer yang contextual (bukan legal boilerplate), dan mekanisme "hubungi dokter" yang proaktif muncul saat confidence rendah.

**Measure:** Tim mengevaluasi bukan hanya usability, tapi trust calibration: apakah pengguna dengan berbagai latar belakang medis memahami kapan harus percaya rekomendasi? Apakah ada kelompok yang secara konsisten over-trusting atau under-trusting?

**Expose:** Tim mendokumentasikan keputusan kritis — mengapa confidence indicator dirancang dengan cara tertentu, apa alternatif yang dipertimbangkan, dan apa yang team berikutnya perlu ketahui jika model diperbarui.

Ketika regulator bertanya *"mengapa fitur ini dibangun dengan cara ini?"* — jawabannya ada di artefak Expose. Tidak ada krisis. Tidak ada ketidaktahuan.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
IFRAME memberikan struktur untuk sesuatu yang sering tidak terstruktur: keputusan governance AI. Mulai dengan satu proyek — identifikasi alir utamanya, dokumentasikan trade-off di Rank, dan buat satu artefak Expose di akhir. Ini tidak membutuhkan mengubah seluruh proses; cukup menambahkan lapisan governance di atas yang sudah ada.

**Jika kamu UX researcher atau designer:**
Tahap Identify dan Flow dalam IFRAME adalah tempat di mana keahlian riset pengguna paling dibutuhkan — dan paling berdampak. Mendefinisikan alir yang mencakup semua kelompok pengguna, termasuk yang paling rentan, adalah kontribusi yang langsung menentukan fairness dan accountability sistem.

**Jika kamu developer atau engineer:**
Tahap Apply dalam IFRAME adalah di mana keputusan teknis dibuat — tapi dalam konteks alir yang sudah didefinisikan dan trade-off yang sudah didokumentasikan. Ini mengubah engineering dari "membangun apa yang diminta" menjadi "membangun apa yang sudah diputuskan secara sadar, dengan alasan yang terdokumentasi."

---

## Pertanyaan Refleksi

> IFRAME tidak menambahkan banyak langkah baru — ia menambahkan kesadaran dan dokumentasi pada keputusan yang sudah harus dibuat.
>
> **Pikirkan satu keputusan desain atau teknis yang pernah dibuat dalam proyek AI yang kamu kenal** — keputusan yang tidak terdokumentasi dan sekarang tidak ada yang ingat alasannya. Di tahap IFRAME mana keputusan itu seharusnya dibuat? Dan artefak apa yang seharusnya ada sekarang?

---

## Ringkasan Lesson

- IFRAME adalah metodologi governance layer yang kompatibel dengan semua metode desain yang ada — bukan pengganti, melainkan lapisan di atasnya.
- Flow adalah unit pengorganisasi sentral: semua keputusan berangkat dari dan kembali ke alir yang sudah didefinisikan.
- Enam tahap: Identify (konteks + pemangku kepentingan), Flow (peta dan pilih alir kritis), Rank (trade-off eksplisit), Apply (implementasi terstruktur), Measure (evaluasi human-centered), Expose (konversi ke pengetahuan organisasi).
- IFRAME mengimplementasikan empat prinsip HCAI secara konkret di setiap tahapnya — bukan sebagai checklist terpisah, melainkan sebagai bagian integral dari proses.
- Lesson berikutnya akan membahas tantangan terbesar dalam penggunaan IFRAME: bagaimana menerjemahkan insight dari riset pengguna menjadi keputusan desain AI yang konkret.

---

## Referensi

- CodeinteX. (2026). *IFRAME: A Flow-Centered Decision Orchestration and Evidence Governance Methodology* (Version 1.0). CodeinteX. codeintex.com/iframe
- Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press. — Bab 13.
- Yang, Q., et al. (2020). Re-examining whether, why, and how human-AI interaction is uniquely difficult to design. *CHI '20 Proceedings*.
- Cai, C. J., et al. (2019). Human-centered tools for coping with imperfect algorithms during medical decision-making. *CHI '19 Proceedings*.
- Madaio, M. A., et al. (2020). Co-designing checklists to understand organizational challenges and opportunities around fairness in AI. *CHI '20 Proceedings*.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
