---
title: "IFRAME Methodology"
description: "IFRAME is a flow-centered decision orchestration and evidence governance methodology developed by CodeinteX."
version: "1.0"
status: public
last_updated: "2026"
keywords:
  - IFRAME methodology
  - flow-centered design
  - decision orchestration
  - evidence governance
  - human-centered AI design process
  - CodeinteX IFRAME
---

# IFRAME
## A Flow-Centered Decision Orchestration and Evidence Governance Methodology

**Developed by CodeinteX** · Version 1.0

---

## Definisi

IFRAME adalah metodologi yang berpusat pada alir (flow-centered) untuk mengorkestrasikan keputusan dan mengelola bukti di sepanjang siklus hidup produk digital, layanan, penelitian, dan inisiatif organisasi — sambil tetap kompatibel dengan berbagai keluarga metode yang sudah ada.

Dalam satu kalimat: **IFRAME memastikan bahwa keputusan bersifat eksplisit, trade-off terlihat, bukti terdokumentasi, dan hasil dapat ditelusuri.**

---

## Latar Belakang: Mengapa IFRAME Diciptakan

Banyak pendekatan desain dan pengembangan yang kuat dalam domain spesifiknya, tapi secara konsisten meninggalkan celah antara:

- **penelitian dan implementasi** — temuan riset tidak selalu menginformasikan keputusan desain
- **implementasi dan evaluasi** — apa yang dibangun tidak selalu dievaluasi terhadap kriteria yang awalnya ditetapkan
- **keputusan dan bukti** — keputusan diambil tanpa jejak yang bisa diperiksa
- **output dan memori organisasi** — pengetahuan proyek hilang setelah tim bubar

Mode kegagalan yang paling umum bukan kekurangan metode — melainkan:

- keputusan yang tidak terdokumentasi
- alasan prioritisasi yang tidak jelas
- riset pengguna yang terputus dari implementasi
- kehilangan pengetahuan setelah proyek selesai
- ketidakmampuan merekonstruksi mengapa sesuatu dibangun dengan cara tertentu

IFRAME diciptakan untuk menyediakan struktur governance yang stabil di sekitar celah-celah ini, tanpa menggantikan metode yang sudah ada.

---

## Prinsip Dasar

### Flow sebagai unit pengorganisasi sentral

Unit pengorganisasi sentral IFRAME adalah **alir (flow)** — bukan persona, bukan fitur, bukan halaman, bukan requirements, bukan task.

**Alir** adalah urutan kohesif dari aksi pengguna dan respons sistem yang memberikan nilai.

Contoh alir dalam produk digital:
- "Pengguna menyadari kebutuhan → mencari → menemukan → mengevaluasi → memutuskan → menggunakan → menilai kembali"
- "Pasien melaporkan gejala → sistem AI menganalisis → dokter menerima rekomendasi → dokter memutuskan → pasien menerima tindakan"
- "Tim mendeteksi masalah → mengumpulkan bukti → menentukan prioritas → mengimplementasikan solusi → mengukur dampak"

Alir menjadi jembatan yang menghubungkan konteks, prioritas, implementasi, dan evaluasi. Semua dalam IFRAME diorganisasikan di sekitar menjaga integritas alir.

### Dua kontribusi utama

IFRAME berkontribusi pada dua hal yang berbeda namun saling terkait:

**1. Orkestrasi Keputusan (Decision Orchestration)**
IFRAME menstrukturkan keputusan apa yang harus dibuat, kapan harus dibuat, dan bagaimana keputusan satu berkaitan dengan keputusan lainnya. IFRAME tidak mendikte metode mana yang harus digunakan — ia menentukan *kapasitas keputusan* yang harus tersedia di setiap tahap.

**2. Tata Kelola Bukti (Evidence Governance)**
Setiap keputusan penting harus meninggalkan bukti — bukan sebagai dokumentasi formal yang memberatkan, melainkan sebagai catatan yang memungkinkan peninjauan di masa depan untuk memahami: apa yang diputuskan, mengapa diputuskan, alternatif apa yang dipertimbangkan, dan hasil apa yang terjadi. Ini memungkinkan kemampuan audit, reproduksibilitas, dan pembelajaran organisasi.

---

## Enam Tahap IFRAME

<!-- DIAGRAM: Enam tahap IFRAME dalam alur horizontal
     Render sebagai diagram pipeline horizontal saat membangun UI.
     Setiap tahap memiliki: nama, ikon, pertanyaan kunci, warna berbeda
     Urutan: Identify → Flow → Rank → Apply → Measure → Expose
     Highlight khusus pada tahap Flow — diberi label "Central Unit"
     Warna progresif dari biru (Identify) ke hijau (Expose)
     Tampilkan juga dua lapisan di bawah pipeline:
     - "Orkestrasi Keputusan" mencakup: Identify, Flow, Rank, Apply
     - "Tata Kelola Bukti" mencakup semua 6 tahap
-->

### I — Identify (Identifikasi)

**Pertanyaan sentral:** *"Ruang masalah apa yang sedang kita hadapi?"*

Tahap ini mendefinisikan konteks, batasan, pemangku kepentingan, dan ruang lingkup. Identify bukan sekadar brief — ini adalah pemetaan eksplisit dari semua pihak yang terlibat dan terdampak, termasuk yang tidak langsung terlihat.

**Yang dilakukan di tahap ini:**
- Mendefinisikan ruang masalah dan batasan sistem
- Memetakan semua pemangku kepentingan — termasuk yang terdampak tapi tidak terlibat langsung
- Mengidentifikasi konteks penggunaan, termasuk kondisi ekstrem
- Mendokumentasikan asumsi kritis yang perlu divalidasi

**Artefak/bukti yang dihasilkan:**
- Peta pemangku kepentingan (stakeholder map)
- Definisi ruang masalah yang tertulis dan disepakati
- Daftar asumsi kritis

**Sinyal bahwa tahap ini selesai:** Tim memiliki pemahaman bersama yang terdokumentasi tentang *untuk siapa* dan *dalam konteks apa* sistem ini bekerja.

---

### F — Flow (Alir)

**Pertanyaan sentral:** *"Alir apa yang ada, dan mana yang paling penting?"*

Flow adalah tahap di mana alir-alir yang relevan dipetakan, didefinisikan, dan dipilih. Ini bukan sekadar tahap memilih — ini adalah tahap di mana konsep sentral IFRAME dikunci ke dalam kerja nyata: semua yang dikerjakan dari sini ke depan berangkat dari alir yang didefinisikan di sini.

Menempatkan Flow sebagai tahap eksplisit mencerminkan komitmen IFRAME: **flow bukan hanya konsep panduan, ia adalah unit kerja yang harus dipetakan sebelum apapun diputuskan.**

**Yang dilakukan di tahap ini:**
- Memetakan semua alir yang relevan dalam ruang masalah yang sudah diidentifikasi
- Mendefinisikan setiap alir: titik awal, langkah-langkah, titik akhir, dan kondisi gagal
- Memilih alir mana yang paling kritis untuk nilai pengguna dan integritas sistem
- Mengidentifikasi di mana dalam alir keputusan AI terlibat — dan siapa yang terdampak

**Artefak/bukti yang dihasilkan:**
- Peta alir lengkap (semua alir yang teridentifikasi)
- Definisi alir kritis yang dipilih (bukan wireframe — deskripsi struktural dari urutan aksi-respons)
- Justifikasi tertulis mengapa alir tertentu diprioritaskan di atas yang lain

**Sinyal bahwa tahap ini selesai:** Tim memiliki peta alir yang disepakati dan dapat menjelaskan mengapa alir yang dipilih lebih penting dari yang tidak dipilih.

---

### R — Rank (Prioritas)

**Pertanyaan sentral:** *"Apa yang paling penting sekarang?"*

Rank adalah tahap di mana trade-off dibuat eksplisit. Dalam semua proyek, tidak semua hal bisa dikerjakan sekaligus. IFRAME memastikan bahwa keputusan prioritisasi — termasuk apa yang *tidak* dikerjakan — terdokumentasi dengan alasan yang jelas.

**Yang dilakukan di tahap ini:**
- Mendefinisikan kriteria prioritisasi secara eksplisit
- Membuat keputusan trade-off yang terdokumentasi
- Mengidentifikasi risiko dari pilihan prioritas yang diambil
- Memastikan keputusan prioritas dapat dijelaskan kepada semua pemangku kepentingan

**Artefak/bukti yang dihasilkan:**
- Backlog yang diprioritaskan dengan justifikasi tertulis per item
- Catatan trade-off: apa yang tidak dikerjakan dan mengapa

**Sinyal bahwa tahap ini selesai:** Setiap keputusan prioritas bisa dijelaskan secara eksplisit — termasuk mengapa sesuatu *tidak* diprioritaskan.

---

### A — Apply (Aplikasi)

**Pertanyaan sentral:** *"Bagaimana ini seharusnya diwujudkan?"*

Apply adalah tahap transformasi: keputusan dari tahap sebelumnya diubah menjadi implementasi. IFRAME tidak mendikte metode implementasi — ia memastikan bahwa implementasi tetap dapat ditelusuri ke keputusan dan alir yang mendasarinya.

**Yang dilakukan di tahap ini:**
- Menerapkan metode implementasi yang sesuai (desain, prototyping, pengembangan, dll.)
- Memastikan setiap keputusan implementasi dapat ditelusuri ke alir dan keputusan yang mendahuluinya
- Mendokumentasikan perubahan signifikan dari rencana awal beserta alasannya
- Membangun mekanisme transparansi dan kontrol yang relevan untuk sistem AI

**Artefak/bukti yang dihasilkan:**
- Output implementasi (desain, prototipe, kode, dll.)
- Catatan keputusan implementasi yang signifikan
- Jejak keterlacakan dari implementasi ke alir yang mendasarinya

**Sinyal bahwa tahap ini selesai:** Setiap elemen implementasi dapat ditelusuri ke alir dan keputusan yang memotivasinya.

---

### M — Measure (Ukur)

**Pertanyaan sentral:** *"Apakah berhasil?"*

Measure adalah tahap evaluasi yang terstruktur — bukan hanya mengukur apakah sistem berfungsi secara teknis, melainkan apakah ia berhasil menurut kriteria yang ditetapkan di Identify dan Rank. Untuk sistem AI, ini termasuk evaluasi terhadap dimensi manusia: kepercayaan, fairness, kontrol yang bermakna.

**Yang dilakukan di tahap ini:**
- Mengevaluasi output terhadap kriteria sukses yang ditetapkan di tahap awal
- Mengukur performa terhadap alir yang menjadi fokus
- Untuk sistem AI: mengevaluasi trust calibration, fairness antar kelompok, dan efektivitas kontrol manusia
- Mendokumentasikan hasil, termasuk yang tidak diharapkan

**Artefak/bukti yang dihasilkan:**
- Laporan evaluasi terstruktur
- Perbandingan hasil terhadap kriteria sukses awal
- Temuan yang tidak diantisipasi dan implikasinya

**Sinyal bahwa tahap ini selesai:** Ada jawaban yang terdokumentasi untuk pertanyaan "apakah berhasil?" — termasuk untuk kelompok pengguna yang berbeda.

---

### E — Expose (Ekspos)

**Pertanyaan sentral:** *"Apa yang harus dipelajari oleh tim di masa depan?"*

Expose adalah kontribusi paling distintif IFRAME. Ini adalah tahap di mana pengetahuan proyek dikonversi menjadi pengetahuan organisasi yang dapat digunakan kembali. Bukan laporan akhir yang tidak pernah dibaca — melainkan artefak pengetahuan terstruktur yang memungkinkan tim lain belajar dari apa yang sudah dikerjakan.

**Yang dilakukan di tahap ini:**
- Mengekstraksi keputusan penting dan pelajarannya ke dalam format yang dapat dicari dan digunakan
- Mendokumentasikan pola yang berhasil dan yang tidak berhasil beserta kondisinya
- Mengidentifikasi asumsi yang terbukti benar dan yang terbukti salah
- Menyiapkan "brief untuk tim berikutnya" — ringkasan konteks yang memungkinkan seseorang yang tidak terlibat di proyek ini memahami mengapa sesuatu dibangun dengan cara tertentu

**Artefak/bukti yang dihasilkan:**
- Knowledge artifacts (bukan dokumentasi teknis, melainkan narasi keputusan yang dapat dicari)
- Pattern library dari apa yang berhasil dan tidak berhasil dalam konteks apa
- Brief untuk tim berikutnya

**Sinyal bahwa tahap ini selesai:** Seseorang yang tidak terlibat di proyek ini bisa memahami keputusan-keputusan kunci dan alasannya hanya dari artefak yang dihasilkan.

---

## IFRAME dan Metodologi Lain

IFRAME tidak menggantikan metodologi yang sudah ada. Ia bertindak sebagai lapisan governance dan kompatibilitas yang dapat menampung berbagai keluarga metode:

| Keluarga Metode | Cocok di Tahap IFRAME |
|---|---|
| Human-Centered Design (ISO 9241-210) | Identify, Flow, Apply, Measure |
| Design Science Research (DSR/DSRM) | Identify, Rank, Apply, Measure, Expose |
| Lean UX | Flow, Rank, Apply, Measure |
| Agile UX | Apply, Measure (iteratif) |
| Object-Oriented UX (OOUX) | Flow, Apply |
| Service Design | Identify, Flow, Apply |
| Systems Thinking | Identify, Rank, Expose |
| Product Discovery | Identify, Flow, Rank |

Tim bisa menggunakan metode yang mereka kuasai di dalam tahap IFRAME yang relevan, sementara IFRAME memastikan keputusan tetap eksplisit dan pengetahuan tetap terdokumentasi di seluruh proses.

---

## IFRAME dan Prinsip Human-Centered AI

Untuk tim yang membangun sistem AI, IFRAME memiliki titik temu eksplisit dengan empat prinsip HCAI:

| Prinsip HCAI | Tahap IFRAME yang relevan | Bagaimana IFRAME mengimplementasikannya |
|---|---|---|
| **Transparency** | Identify, Apply, Expose | Setiap keputusan terdokumentasi; alasan tersedia untuk audit; Expose memastikan pengetahuan tentang cara kerja sistem dapat diakses |
| **Fairness** | Identify, Rank, Measure | Identify memetakan semua pihak terdampak; Rank membuat trade-off fairness eksplisit; Measure mengevaluasi fairness antar kelompok |
| **Human Control** | Flow, Apply, Measure | Flow memastikan alir tidak merampas agen pengguna; Apply membangun titik kontrol manusia; Measure mengevaluasi apakah kontrol bermakna |
| **Accountability** | Semua tahap | Evidence governance di setiap tahap menciptakan jejak audit yang memungkinkan pertanggungjawaban yang bermakna |

---

## Apa yang IFRAME BUKAN

IFRAME bukan:
- metode UX
- sistem desain
- kerangka komponen
- metodologi manajemen proyek
- siklus hidup pengembangan perangkat lunak
- metode penelitian
- kerangka penulisan konten

IFRAME dapat berdampingan dengan semua di atas.

---

## Panduan Penggunaan AI dalam IFRAME

Ketika bekerja dengan asisten AI dalam konteks IFRAME, prinsip berikut berlaku:

**AI tidak boleh:**
- Menciptakan strategi
- Menciptakan prioritas
- Menciptakan persona
- Menciptakan alir
- Mengambil keputusan governance

**AI dapat membantu:**
- Analisis dan sintesis
- Pembuatan konten
- Generasi desain
- Perencanaan implementasi
- Dokumentasi
- Evaluasi

Sambil menjaga:
- Integritas alir
- Keterlacakan keputusan
- Kontinuitas bukti

---

## Glosarium IFRAME

**Alir (Flow):** Urutan kohesif dari aksi pengguna dan respons sistem yang memberikan nilai. Unit pengorganisasi sentral IFRAME.

**Bukti (Evidence):** Artefak yang mendokumentasikan apa yang diputuskan, mengapa, alternatif yang dipertimbangkan, dan hasil yang terjadi.

**Integritas alir (Flow integrity):** Kondisi di mana alir pengguna tetap kohesif, dapat ditelusuri, dan sejalan dengan nilai yang ingin disampaikan di sepanjang siklus implementasi.

**Keterlacakan (Traceability):** Kemampuan untuk menelusuri setiap elemen implementasi kembali ke keputusan dan alir yang memotivasinya.

**Orkestrasi keputusan (Decision orchestration):** Struktur yang menentukan keputusan apa yang harus dibuat, kapan, dan bagaimana keputusan satu berkaitan dengan lainnya.

**Tata kelola bukti (Evidence governance):** Sistem yang memastikan setiap keputusan penting meninggalkan bukti yang dapat diaudit dan digunakan untuk pembelajaran.

---

## Sitasi dan Referensi

Jika mengutip IFRAME dalam karya akademis atau profesional:

> CodeinteX. (2026). *IFRAME: A Flow-Centered Decision Orchestration and Evidence Governance Methodology* (Version 1.0). CodeinteX. https://codeintex.com/iframe

Untuk pertanyaan tentang IFRAME, hubungi: hello@codeintex.com

---

*IFRAME dikembangkan oleh CodeinteX. Metodologi ini dipublikasikan untuk kepentingan komunitas praktisi dan peneliti di bidang Human-Centered AI dan desain produk digital.*
