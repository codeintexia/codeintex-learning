# Kursus 2: AI untuk Proses Data — Referensi SKKNI
## Dokumen Acuan Produksi Konten

**Status kode unit — KEPUTUSAN FINAL:** Skema kompetensi yang sudah diajukan dan terdaftar di BNSP/LSP AII menggunakan kode **lama**: `J.62AIN00.014.1–017.1`. Ini yang mengikat secara administratif dan yang akan dicek asesor terhadap sertifikat peserta. **Semua materi yang bersentuhan dengan peserta dan sertifikasi (judul course, frontmatter lesson, badge unit kompetensi, dokumen ke LSP) WAJIB pakai kode lama ini.**

Catatan cross-reference internal (bukan untuk publikasi): teks SKKNI yang saya baca langsung dari SKKNI 2026103.pdf memakai penomoran baru untuk unit yang sama — `K.62AIN00.024.2–027.2`. Substansi KUK/elemen kompetensi/aspek kritis identik, hanya labelnya berbeda karena SKKNI direvisi jadi dokumen 27-unit yang lebih besar. Pemetaannya:

| Kode Resmi (BNSP — dipakai) | Kode SKKNI 2026103 (referensi internal saja) | Judul Unit |
|---|---|---|
| J.62AIN00.014.1 | K.62AIN00.024.2 | Mengintegrasikan Komponen Solusi AI |
| J.62AIN00.015.1 | K.62AIN00.025.2 | Memasang Solusi AI |
| J.62AIN00.016.1 | K.62AIN00.026.2 | Merencanakan Perawatan Solusi AI |
| J.62AIN00.017.1 | K.62AIN00.027.2 | Merawat Solusi AI |
| J.63OPR00.014.2 | *(sama, tidak berubah)* | Melakukan Pemasukan Data |
| J.63OPR00.015.2 | *(sama, tidak berubah)* | Memastikan Validitas Data |

Mulai bagian di bawah ini, setiap unit ditandai dengan **kode resmi (BNSP)** sebagai heading utama.

---

## Peta Fungsi (dari SKKNI 2026103)

```
Tujuan Utama: Menjamin akuntabilitas solusi Artificial Intelligence
  └─ Fungsi Kunci: Menerapkan solusi Artificial Intelligence (AI)
       ├─ Mengintegrasikan komponen solusi AI      → K.62AIN00.024.2
       ├─ Memasang solusi AI                        → K.62AIN00.025.2
       ├─ Merencanakan perawatan solusi AI          → K.62AIN00.026.2
       └─ Merawat solusi AI                         → K.62AIN00.027.2
```

Dua unit OPR (Pemasukan Data, Validitas Data) berdiri sebagai fungsi dasar terpisah dalam SKKNI 2018056, di bawah "Memproses pemasukan data" dan "Memastikan validitas data".

---

## UNIT 1 — J.62AIN00.014.1: Mengintegrasikan Komponen Solusi Artificial Intelligence
*(ref. internal SKKNI 2026103: K.62AIN00.024.2)*

**Deskripsi:** Mengidentifikasi komponen yang akan diintegrasikan, menggabungkan komponen arsitektur teknis, hingga menguji secara internal sistem terintegrasi.

### Elemen Kompetensi & KUK

**1. Mengidentifikasi komponen solusi yang akan diintegrasikan**
- 1.1 Komponen Solusi AI yang akan diintegrasikan berdasarkan arsitektur teknis dan dokumentasi proyek.
- 1.2 Teknologi integrasi dipilih sesuai kebutuhan komunikasi antarmodul.
- 1.3 Format pertukaran data disesuaikan dengan kebutuhan integrasi sistem.

**2. Menggabungkan komponen arsitektur teknis dari Solusi AI**
- 2.1 Prosedur integrasi komponen arsitektur lengkap disusun sesuai sasaran teknis dan best practice.
- 2.2 Prosedur integrasi didokumentasikan sesuai standar dokumentasi.
- 2.3 Komponen sistem disinkronisasikan sesuai prosedur integrasi.

**3. Menguji secara internal sistem terintegrasi**
- 3.1 Data kasus uji dikumpulkan sesuai sasaran teknis.
- 3.2 Simulasi sistem terintegrasi dilakukan sesuai standar pengujian.
- 3.3 Hasil simulasi dianalisis sesuai sasaran teknis.
- 3.4 Hasil analisis disosialisasikan kepada stakeholders sebagai acuan QA.

### Konteks Variabel Penting
- Teknologi integrasi: REST API, GraphQL, gRPC — komunikasi antarmodul/antarmodel, backend-frontend, atau AI-ERP/mobile app.

### Pengetahuan & Keterampilan
- Strategi & lingkungan integrasi komponen sistem Solusi AI
- Arsitektur sistem terintegrasi (monolitik vs mikroservis)
- CI/CD dalam integrasi AI (DevOps, MLOps)
- Menggunakan tools integrasi, menangani exception, dokumentasi proses

### Aspek Kritis
> Ketepatan dalam mensinkronkan komponen sistem Solusi AI sesuai dengan prosedur integrasi komponen arsitektur lengkap dari Solusi AI.

---

## UNIT 2 — J.62AIN00.015.1: Memasang Solusi Artificial Intelligence
*(ref. internal SKKNI 2026103: K.62AIN00.025.2)*

**Deskripsi:** Deployment Solusi AI ke berbagai lingkungan — dari penyiapan lingkungan deployment, pengemasan model, pemasangan, hingga penanganan keamanan.

### Elemen Kompetensi & KUK

**1. Menyiapkan lingkungan deployment**
- 1.1 Lingkungan deployment dipilih berdasarkan kebutuhan teknis.
- 1.2 Konfigurasi infrastruktur deployment diperiksa sesuai spesifikasi teknis.

**2. Melakukan deployment Solusi AI**
- 2.1 Model dan komponen sistem disiapkan untuk deployment sesuai prosedur.
- 2.2 Dependensi dan konfigurasi pendukung disusun sesuai kebutuhan solusi.
- 2.3 Deployment dilakukan ke lingkungan yang telah disiapkan.

**3. Melakukan validasi dan pengujian pascadeployment**
- 3.1 Hasil deployment diuji untuk memastikan model berjalan sesuai ekspektasi.
- 3.2 Performa model dan sistem diverifikasi terhadap sasaran teknis.

**4. Menerapkan pengamanan Solusi AI**
- 4.1 Mekanisme pengamanan diterapkan sesuai kebutuhan solusi dan regulasi.
- 4.2 Ketentuan kepatuhan data diperiksa terhadap standar yang berlaku.

**5. Mempersiapkan dokumentasi dan monitoring**
- 5.1 Dokumentasi proses deployment disusun lengkap sesuai ketentuan kepatuhan.
- 5.2 Mekanisme monitoring dan log sistem disiapkan untuk observasi pascadeployment.

### Konteks Variabel Penting
- Lingkungan deployment: on-premise, cloud computing, edge computing.
- Infrastruktur: server/VM/CPU/GPU/cloud instance, cloud bucket/NAS, LAN/VPN/internet.

### Pengetahuan & Keterampilan
- Teknik pemasangan solusi Teknologi Informasi dan Komunikasi (TIK)
- Pembuatan laporan hasil instalasi komponen sistem Solusi AI
- Menggunakan tools dan troubleshoot instalasi komponen Solusi AI
- Menggunakan deployment pipelines untuk CI/CD

### Sikap Kerja
- Teliti dalam melakukan deployment
- Cara berpikir sistematis dalam mengonfigurasi infrastruktur
- Bertanggung jawab atas keamanan sistem selama proses deployment

### Aspek Kritis
> 5.1 Ketelitian dalam melakukan deployment ke lingkungan yang telah disiapkan.
> 5.2 Ketepatan dalam mengonfigurasi infrastruktur deployment sesuai spesifikasi teknis Solusi AI.

---

## UNIT 3 — J.62AIN00.016.1: Merencanakan Perawatan Solusi Artificial Intelligence
*(ref. internal SKKNI 2026103: K.62AIN00.026.2)*

**Deskripsi:** Membuat rencana perawatan Solusi AI yang telah dioperasikan — dari penyiapan hingga penyusunan rencana perawatan.

### Elemen Kompetensi & KUK

**1. Menyiapkan rencana perawatan Solusi AI**
- 1.1 Hasil monitoring dikumpulkan sesuai kebutuhan yang mengacu parameter evaluasi.
- 1.2 Hasil monitoring dievaluasi sesuai metrik kesuksesan Solusi AI.
- 1.3 Komponen arsitektur yang harus dirawat ditentukan berdasarkan hasil evaluasi monitoring.

**2. Menyusun rencana perawatan Solusi AI**
- 2.1 Rencana perawatan dibuat berdasarkan hasil evaluasi monitoring.
- 2.2 Rencana perawatan didokumentasikan sesuai standar dokumentasi.

### Konteks Variabel Penting
- Parameter evaluasi: akurasi, presisi, recall, F1-score, kohesi, MAE.
- Hasil evaluasi monitoring = membandingkan performa awal saat operasional dimulai vs performa saat ini.

### Aspek Kritis
> Ketepatan dalam membuat rencana perawatan Solusi AI berdasarkan hasil evaluasi analisis simulasi Solusi AI dengan metrik kesuksesan.

---

## UNIT 4 — J.62AIN00.017.1: Merawat Solusi Artificial Intelligence
*(ref. internal SKKNI 2026103: K.62AIN00.027.2)*

**Deskripsi:** Menyiapkan dan melakukan perawatan Solusi AI yang dibutuhkan oleh pengguna.

### Elemen Kompetensi & KUK

**1. Menyiapkan perawatan dari Solusi AI berdasarkan rencana perawatan**
- 1.1 Hasil monitoring sistem dipastikan sesuai kebutuhan perawatan komponen arsitektur lengkap.
- 1.2 Kebutuhan perawatan komponen arsitektur ditentukan sesuai prosedur perawatan.

**2. Melakukan perawatan Solusi AI berdasarkan rencana perawatan**
- 2.1 Komponen arsitektur lengkap dirawat sesuai prosedur dan rencana perawatan.
- 2.2 Seluruh aktivitas perawatan didokumentasikan sesuai standar dokumentasi.

### Konteks Variabel Penting
- Kebutuhan perawatan mencakup: strategi AI, tata kelola, faktor manusia, ketahanan siber, kompetensi AI, kualitas data, arsitektur & infrastruktur data, pengukuran kinerja, etika, black box.

### Aspek Kritis
> Ketepatan dalam merawat komponen arsitektur lengkap dari Solusi AI sesuai prosedur perawatan Solusi AI dan rencana perawatan Solusi AI.

---

## UNIT 5 — J.63OPR00.014.2: Melakukan Pemasukan Data

**Deskripsi:** Memasukkan data menggunakan perangkat komputer.

### Elemen Kompetensi & KUK

**1. Mempersiapkan data yang akan dimasukkan**
- 1.1 Perlakuan persiapan data sesuai dengan aplikasi yang digunakan.
- 1.2 Jumlah data diperiksa kelengkapannya sesuai borang.
- 1.3 Jenis data pada tiap isian diperiksa sesuai borang.

**2. Memasukkan data dengan perangkat komputer**
- 2.1 Data dimasukkan menggunakan aplikasi komputer sesuai yang ditentukan.
- 2.2 Data disimpan pada aplikasi sesuai lokasi penyimpanan.
- 2.3 Data wajib dimasukkan secara lengkap sesuai aplikasi.
- 2.4 Dokumen fisik dipindai menjadi format elektronis sesuai dokumen fisik aslinya.
- 2.5 Pekerjaan pemasukan data dicatat pada logbook sesuai standar organisasi.

**3. Meng-import data dari sumber elektronis**
- 3.1 Jenis file diidentifikasi dengan tepat sesuai aplikasi yang dapat membacanya.
- 3.2 Jenis file dapat disimpan dengan tepat sesuai aplikasi yang akan menggunakannya.
- 3.3 Berkas yang di-import dibaca ke program sesuai berkas aslinya.
- 3.4 Pekerjaan pengimportan data dicatat pada logbook sesuai standar organisasi.

### Pengetahuan & Keterampilan
- Jenis-jenis file, manajemen file
- Mengetik pada keyboard

### Sikap Kerja
Disiplin · Teliti · Tanggung jawab · Kerjasama tim

### Aspek Kritis
> Ketepatan memperlakukan persiapan data sesuai dengan aplikasi yang digunakan.

---

## UNIT 6 — J.63OPR00.015.2: Memastikan Validitas Data

**Deskripsi:** Memastikan validitas data yang dimasukkan dengan perangkat komputer.

### Elemen Kompetensi & KUK

**1. Mengidentifikasi substansi data yang dimasukkan**
- 1.1 Data dipastikan sesuai keperluan data pada proses bisnis organisasi.
- 1.2 Jenis data yang dimasukkan sesuai kebutuhan jenis data pada aplikasi.

**2. Mengidentifikasi referensi dari data yang dimasukkan**
- 2.1 Pemasukan berdasarkan jenis data diidentifikasi sesuai penggunaan referensi data.
- 2.2 Data yang dimasukkan sesuai kodifikasi dari data tersebut.

**3. Memeriksa validitas data**
- 3.1 Akurasi sumber data diperiksa sesuai kebutuhan organisasi.
- 3.2 Data yang dimasukkan diperiksa sesuai akurasi yang ditentukan.
- 3.3 Data yang dimasukkan sesuai aspek keamanan informasi.

**4. Melakukan pemutakhiran data**
- 4.1 Data diperbaiki sesuai kriteria validitas data.
- 4.2 Data pada dokumen yang tidak lengkap dilengkapi sesuai kebutuhan aplikasi pengolah data.
- 4.3 Data dilakukan pemutakhiran sesuai data terbaru yang ada.

### Pengetahuan & Keterampilan
- Konsep jenis data, konsep kualitas data
- Mengetik pada keyboard

### Sikap Kerja
Disiplin · Teliti · Tanggung jawab · Kerjasama tim

### Aspek Kritis
> Ketepatan memastikan data sesuai dengan keperluan data pada proses bisnis organisasi.

---

## Prasyarat Kompetensi (chaining logis untuk urutan modul)

```
Melakukan Pemasukan Data (014.2)
   → prasyarat: Menggunakan Perangkat Komputer, Menggunakan Sistem Operasi

Memastikan Validitas Data (015.2)
   → prasyarat: Menggunakan Perangkat Komputer, Melakukan Pemasukan Data

Mengintegrasikan Komponen Solusi AI (024.2)
   → berdiri sendiri secara teknis, tapi logis setelah unit AI perencanaan/desain sebelumnya

Memasang Solusi AI (025.2)
   → logis setelah integrasi selesai

Merencanakan Perawatan Solusi AI (026.2)
   → logis setelah solusi terpasang (butuh data monitoring operasional)

Merawat Solusi AI (027.2)
   → prasyarat langsung: Merencanakan Perawatan Solusi AI (026.2)
```

**Implikasi untuk urutan modul kursus:** Pemasukan Data & Validitas Data secara alami adalah fondasi (operasional dasar), sementara keempat unit AI (integrasi → pasang → rencana rawat → rawat) membentuk siklus hidup solusi AI yang berurutan secara alami. Ini bisa jadi dasar pembagian modul.

---

## Riset: Level Kualifikasi & Metode Asesmen (Panduan Desain Latihan)

Bagian ini adalah hasil riset untuk mengkalibrasi kedalaman konten dan format latihan — bukan bagian dari KUK, tapi panduan desain yang harus diikuti konsisten di semua lesson.

### Level Kualifikasi — Terverifikasi Sebagian

**Tidak ditemukan:** Baik SKKNI 2026103 maupun SKKNI 2018056 tidak mencantumkan angka level KKNI eksplisit di dalam dokumennya. Pemetaan KKNI biasanya ada di dokumen skema sertifikasi terpisah, bukan di SKKNI itu sendiri.

**Ditemukan (terverifikasi via pencarian):** Persyaratan dasar peserta untuk skema sertifikasi "AI untuk Proses Data" yang sesungguhnya (dipublikasikan mitra LSP): **Ijazah SLTA/SMK semua kejuruan** + pengalaman kerja min. 1 tahun di bagian pengolahan data menggunakan AI, ATAU sertifikat pelatihan sejenis — **tidak mensyaratkan gelar sarjana**. Ini kontras jelas dengan skema "AI Engineer" dari LSP lain yang mensyaratkan S2 atau setara KKNI level 6.

**Kesimpulan (penalaran, bukan kutipan):** Skema ini berada di tingkat **operator/teknisi (kemungkinan KKNI level 2–3)**, bukan level profesional/insinyur. Konsisten dengan bahasa KUK yang seluruhnya prosedural ("diperiksa sesuai", "disusun sesuai"), bukan analitis tingkat tinggi.

**Implikasi untuk kedalaman konten:** Konsep teknis yang eksplisit diminta Pengetahuan unit (CI/CD, monolitik vs mikroservis, DevOps/MLOps di unit 024.2) tetap harus diajarkan — tapi levelnya **pengenalan konsep yang bisa dipakai** ("apa itu dan kapan dipakai"), bukan diskusi arsitektur tingkat insinyur senior ("bagaimana merancang dari nol").

### Metode Asesmen — Terverifikasi Langsung dari SKKNI

Setiap unit di kedua SKKNI mencantumkan kalimat identik pada bagian Panduan Penilaian:
> "Metode asesmen yang dapat diterapkan meliputi kombinasi metode **tes lisan, tes tertulis, observasi-tempat kerja/demonstrasi/simulasi, verifikasi bukti/portofolio, dan wawancara** serta metode lain yang relevan."

### Durasi Asesmen — Estimasi Berbasis Pola, Bukan Angka Resmi

Sumber-sumber mengenai durasi asesmen BNSP saling berbeda (4-12 jam/unit di satu sumber vs 60-120 menit/skema penuh di sumber lain untuk asesmen daring) — tidak ada angka tunggal yang bisa diklaim sebagai resmi. Estimasi kerja yang wajar untuk skema 6 unit dengan format B2B terjadwal singkat: **sekitar 15-30 menit demonstrasi praktik per unit**, bervariasi sesuai kompleksitas.

### Panduan Desain Latihan (Berlaku untuk Semua Lesson Selanjutnya)

Karena observasi tempat kerja penuh tidak realistis dalam waktu singkat, metode yang paling mungkin dipakai adalah **Demonstrasi/Simulasi Terstruktur** (skenario dan waktu sudah dirancang ketat di TUK) dikombinasikan **Tes Lisan/Wawancara singkat** untuk memverifikasi Pengetahuan. Karena itu:

1. **Quick Check** di setiap lesson dibuat **time-boxed** (target 2-3 menit pengerjaan), format singkat yang meniru tanya-jawab lisan cepat — bukan diskusi terbuka panjang.
2. **Studi Kasus/latihan praktik** di setiap lesson dibuat sebagai **"Latihan Terstruktur"** dengan skenario jelas, instruksi langkah spesifik, dan **batas waktu eksplisit** (target 10-15 menit) — meniru format demonstrasi/simulasi TUK, bukan refleksi terbuka tanpa batas waktu.
4. **Hook tidak boleh menyebut nama perusahaan/institusi/individu nyata secara spesifik** — meski harus berbasis fakta/regulasi/pola nyata terverifikasi (bukan hipotetis). Regulasi (POJK, UU) boleh disebut by name karena itu produk hukum publik. Pola industri/kejadian nyata dipakai dalam bentuk **anonim/general** ("sejumlah lembaga jasa keuangan...", "ditemukan kasus di mana...") — bukan menyeret nama perusahaan atau orang tertentu, apalagi dari sumber blog vendor/PR yang tidak otoritatif.
5. **AI harus menjadi porsi utama dan besar di setiap lesson — bukan tempelan nama di atas konten IT generik.** Kursus ini bernama "AI untuk Proses Data", bukan "Proses Data yang Kebetulan Dipakai AI". Dua unit di M1 (Pemasukan Data, Validitas Data) secara harfiah adalah unit OPR generik di SKKNI, bukan unit AI — risikonya konten jadi terasa seperti pelatihan data entry biasa dengan nama "SPKO" ditempel di permukaan. Untuk mencegah ini, **setiap lesson (termasuk di M1) wajib punya bagian eksplisit yang menjelaskan secara mekanistik kenapa isu ini berbeda/lebih kritis untuk Solusi AI dibanding sistem biasa** — misalnya: data yang salah bukan cuma "tersimpan salah" tapi menjadi *feature* yang diproses model tanpa insting curiga manusia (prinsip *garbage in, garbage out* yang lebih berbahaya di AI karena keputusan otomatis tanpa sanity check manual). Untuk M2-M6 (unit AI eksplisit), jangan biarkan konten melebar ke DevOps/software engineering generik — pertahankan kekhususan MLOps: model drift, retraining, bias/fairness monitoring, explainability — sesuai yang diminta eksplisit di Pengetahuan tiap unit, bukan versi umum yang bisa dipakai software apa saja.

---

## Kerangka Delivery: LMS Mandiri vs Onsite Praktik

**Keputusan (dikunci):** LMS (25 lesson) adalah **pengganti penuh** materi — peserta wajib baca mandiri sebelum onsite. Onsite 2 hari **bukan re-teach**, murni **praktik terstruktur + tanya jawab singkat** per unit kompetensi, meniru format demonstrasi/simulasi TUK yang sudah dianalisis di bagian sebelumnya.

**Risiko operasional yang harus diwaspadai:** LMS Phase 1 tanpa auth berarti tidak ada mekanisme melacak siapa yang sudah baca sebelum onsite. Perlu kebijakan non-teknis (kuis kesiapan di awal Hari 1, atau syarat submit bukti baca) — ini bukan masalah desain kurikulum, tapi harus diantisipasi CodeinteX secara operasional.

### Jalur 1 — JP Mandiri (LMS)
25 lesson × ~27-28 menit rata-rata ≈ **14-16 JP** (@45-50 menit)

### Jalur 2 — JP Onsite (Praktik Terstruktur)

| Hari | Sesi | Estimasi Waktu |
|---|---|---|
| **Hari 1** | Pembukaan & orientasi | 15 menit |
| | M1 — Recap singkat (10) + Praktik Terstruktur (75) + Debrief (10) | 95 menit |
| | M2 — Recap (10) + Praktik (75) + Debrief (10) | 95 menit |
| | *ISHOMA* | — |
| | M3 — Recap (10) + Praktik (90, 5 elemen kompetensi) + Debrief (15) | 115 menit |
| | **Subtotal Hari 1** | **320 menit ≈ 6,4 JP** |
| **Hari 2** | Recap Hari 1 | 10 menit |
| | M4 — Recap (10) + Praktik (75) + Debrief (10) | 95 menit |
| | M5 — Recap (10) + Praktik (60, hanya 2 elemen) + Debrief (10) | 80 menit |
| | *ISHOMA* | — |
| | M6 — Audit Capstone Terintegrasi (semua unit) | 120 menit |
| | Penutupan & briefing kesiapan uji kompetensi | 20 menit |
| | **Subtotal Hari 2** | **325 menit ≈ 6,5 JP** |
| | **Total Onsite** | **645 menit ≈ 12,9 JP** |

### Total Gabungan (jika dilaporkan sebagai satu program)
**~14-16 JP (mandiri) + ~13 JP (onsite) ≈ 27-29 JP** — sebanding dengan pembanding Kominfo (24 JP), sedikit lebih tinggi karena kompleksitas 6 unit yang sudah teridentifikasi lewat cross-check KUK sebelumnya.

### Yang Masih Perlu Dirancang (Belum Ada)
- Skenario praktik terstruktur khusus onsite per unit (beda dari "Latihan Terstruktur" di LMS yang didesain untuk individu — versi onsite perlu format kelompok/berpasangan dengan fasilitator)
- Lembar observasi instruktur bergaya asesor (mirip FR.AK yang dipakai asesmen BNSP sesungguhnya) — supaya peserta terbiasa dengan format observasi sejak latihan, bukan baru terkejut saat uji kompetensi asli
- Panduan fasilitator/instruktur per sesi (bukan sekadar mengandalkan konten LMS yang ditulis untuk pembaca mandiri)

---

## Outline Lesson Final per Modul

Disusun berdasarkan matriks cross-check di atas — jumlah lesson disesuaikan bobot elemen kompetensi tiap unit (tidak dipaksa rata 4/modul), semua gap 🔴 dan keputusan ⚠️ sudah ditindaklanjuti eksplisit di bawah. Studi kasus mengikuti config `audience_id: bank` (Bank Nusantara Sejahtera / SPKO) sebagai benang merah lintas modul.

---

### MODUL 1 — Fondasi Pemasukan & Validitas Data
**Unit:** J.63OPR00.014.2, J.63OPR00.015.2 | **6 lesson**

| # | Judul Lesson | KUK yang Ditutup | Catatan |
|---|---|---|---|
| L1 | Mengenal SPKO: Data sebagai Fondasi Solusi AI | Advance organizer, hook (skenario nasabah SPKO) | Pembuka course — memperkenalkan benang merah kasus bank yang dipakai s/d M6 |
| L2 | Mempersiapkan & Memasukkan Data Nasabah | 014.2 elemen 1–2 | Termasuk pemindaian dokumen fisik (KTP, formulir) |
| L3 | Mengimpor Data dari Sumber Elektronis | 014.2 elemen 3 | ✅ Menutup gap 🔴 — sebelumnya belum ada lesson terpisah |
| L4 | Mengidentifikasi Substansi & Referensi Data | 015.2 elemen 1–2 | ✅ Menutup gap ⚠️ — konsep referensi/kodifikasi tidak digabung sekilas |
| L5 | Memeriksa Validitas Data Nasabah | 015.2 elemen 3 | — |
| L6 | Melakukan Pemutakhiran Data | 015.2 elemen 4 | ✅ Menutup gap 🔴 — proses korektif berkelanjutan, beda dari sekadar cek validitas |

---

### MODUL 2 — Integrasi Komponen Solusi AI
**Unit:** J.62AIN00.014.1 | **4 lesson**

| # | Judul Lesson | KUK yang Ditutup | Catatan |
|---|---|---|---|
| L1 | Konsep Integrasi & Arsitektur Sistem Terintegrasi | Pengetahuan: strategi integrasi, monolitik vs mikroservis, **CI/CD dijelaskan tuntas di sini** | 🏠 Ini "rumah" utama CI/CD — M3 nanti hanya mereferensikan, tidak menjelaskan ulang |
| L2 | Mengidentifikasi Komponen & Teknologi Integrasi | Elemen 1 | Komponen SPKO: model scoring, core banking, dashboard petugas kredit |
| L3 | Menggabungkan Arsitektur Teknis | Elemen 2 | REST API sebagai teknologi integrasi (sesuai config) |
| L4 | Menguji Sistem Terintegrasi & Dokumentasi | Elemen 3 | Menutup dengan output yang jadi jembatan ke M3 |

---

### MODUL 3 — Deployment Solusi AI
**Unit:** J.62AIN00.015.1 | **5 lesson**

| # | Judul Lesson | KUK yang Ditutup | Catatan |
|---|---|---|---|
| L1 | Dari Integrasi ke Deployment: Menyiapkan Lingkungan | Elemen 1 | 🌉 Jembatan eksplisit: "Solusi yang sudah diintegrasikan di M2 sekarang siap dipasang..." |
| L2 | Melakukan Deployment Solusi AI | Elemen 2 | Mereferensikan CI/CD dari M2-L1 ("seperti dijelaskan di M2, di sini CI/CD berperan sebagai...") |
| L3 | Validasi & Pengujian Pascadeployment | Elemen 3 | — |
| L4 | Menerapkan Pengamanan & Kepatuhan Data | Elemen 4 | ✅ Menutup gap 🔴 — memakai konteks POJK & UU PDP dari config bank |
| L5 | Dokumentasi & Monitoring Pascadeployment | Elemen 5 | Output monitoring jadi jembatan ke M4 |

---

### MODUL 4 — Merencanakan Perawatan Solusi AI
**Unit:** J.62AIN00.016.1 | **4 lesson**

| # | Judul Lesson | KUK yang Ditutup | Catatan |
|---|---|---|---|
| L1 | Memahami Parameter Evaluasi Solusi AI | Pengetahuan: akurasi, presisi, recall, F1-score, MAE | ✅ Menutup gap ⚠️ — konsep dijelaskan lengkap dulu sebelum dipakai, tidak diasumsikan peserta sudah tahu |
| L2 | Mengumpulkan & Mengevaluasi Hasil Monitoring | Elemen 1 | 🌉 Memakai output monitoring dari M3-L5 |
| L3 | Menyusun Rencana Perawatan | Elemen 2 | Skenario: SPKO gagal menilai nasabah baru pasca kebijakan suku bunga OJK |
| L4 | Studi Kasus: Menyusun Rencana Perawatan SPKO | Latihan terintegrasi elemen 1–2 | Analog "audit exercise" seperti pola M3 di HCAI Foundations |

---

### MODUL 5 — Merawat Solusi AI
**Unit:** J.62AIN00.017.1 | **3 lesson**

| # | Judul Lesson | KUK yang Ditutup | Catatan |
|---|---|---|---|
| L1 | Dari Rencana ke Aksi: Menyiapkan Perawatan | Elemen 1 | 🌉 Jembatan eksplisit ke output M4 — unit ini secara literal butuh rencana perawatan sebagai input |
| L2 | Melakukan & Mendokumentasikan Perawatan | Elemen 2 | — |
| L3 | Studi Kasus: Menangani Insiden Performa SPKO | Latihan terintegrasi elemen 1–2 | Skenario: perlambatan sistem saat volume pengajuan kredit naik akhir bulan |

*(Hanya 3 lesson — konsisten dengan cross-check sebelumnya bahwa unit ini paling ramping, 2 elemen kompetensi saja.)*

---

### MODUL 6 — Audit Siklus Hidup & Evaluasi Terintegrasi
**Semua 6 unit** | **3 lesson**

| # | Judul Lesson | Cakupan | Catatan |
|---|---|---|---|
| L1 | Menyeluruh Melihat Siklus Hidup Solusi AI | Sintesis M1–M5 | Merangkai kembali benang merah SPKO dari data mentah hingga perawatan operasional |
| L2 | Kriteria Penilaian per Unit Kompetensi | Aspek kritis keenam unit, dirangkum eksplisit | Tidak menyebut "persiapan sertifikasi LSP AII" secara langsung — sesuai batasan branding |
| L3 | Capstone: Audit Terintegrasi SPKO | Semua unit didemonstrasikan dalam satu skenario audit end-to-end | Skenario final: OJK meminta audit menyeluruh terhadap SPKO — peserta menelusuri kembali dari kualitas data hingga status perawatan |

---

**Total: 25 lesson, 6 modul** — kebetulan sama dengan HCAI Foundations, tapi ini hasil dari bobot elemen kompetensi masing-masing unit (via cross-check), bukan target angka yang dipaksakan.



## Matriks Cross-Check: Cakupan Pengetahuan & Keterampilan per Modul

Tujuan bagian ini: memastikan **setiap butir** Pengetahuan, Keterampilan, dan Sikap Kerja yang tertulis di SKKNI punya tempat eksplisit di rencana modul — bukan sekadar "modulnya menyentuh topik ini secara umum". Kolom "Status" menandai apakah butir ini sudah punya rumah yang jelas atau masih perlu keputusan penempatan.

### J.62AIN00.014.1 — Mengintegrasikan Komponen Solusi AI (→ Modul 2)

| Butir | Rencana Penempatan | Status |
|---|---|---|
| Strategi & lingkungan integrasi komponen sistem | M2-L1 (konsep integrasi) | ✅ Jelas |
| Arsitektur sistem terintegrasi (monolitik vs mikroservis) | M2-L2 (arsitektur & teknologi integrasi) | ✅ Jelas |
| CI/CD dalam integrasi AI (DevOps, MLOps) | M2-L2 atau L3 — **tumpang tindih berpotensi dengan CI/CD di Modul 3 (deployment)** | ⚠️ Perlu keputusan: CI/CD dibahas sekali di M2 dan direferensikan ulang di M3, atau dipecah konsepnya? |
| Pembuatan laporan hasil integrasi | M2-L4 (dokumentasi & pengujian) | ✅ Jelas |
| Menggunakan tools integrasi (REST API, GraphQL, gRPC) | M2-L2 | ✅ Jelas |
| Menangani exception & menjaga konsistensi data | M2-L3 (pengujian internal) | ✅ Jelas |
| Melakukan dokumentasi proses integrasi | M2-L4 | ✅ Jelas |
| Sikap: Teliti, sistematis | Terintegrasi ke semua lesson M2 (bukan lesson terpisah) | ✅ Jelas (metode, bukan konten) |

### J.62AIN00.015.1 — Memasang Solusi AI (→ Modul 3)

| Butir | Rencana Penempatan | Status |
|---|---|---|
| Teknik pemasangan solusi TIK | M3-L1 (menyiapkan lingkungan deployment) | ✅ Jelas |
| Pembuatan laporan hasil instalasi | M3-L4 (dokumentasi & monitoring) | ✅ Jelas |
| Tools & troubleshoot instalasi | M3-L2 (melakukan deployment) | ✅ Jelas |
| Deployment pipelines CI/CD | M3-L2 — **lihat catatan tumpang tindih di atas** | ⚠️ Sama seperti di atas |
| Elemen 3: validasi & pengujian pascadeployment | M3-L3 | ✅ Jelas — **belum eksplisit di draft modul lama, perlu lesson tersendiri** |
| Elemen 4: pengamanan Solusi AI & kepatuhan data | **Belum ada lesson eksplisit di draft awal** | 🔴 Gap — perlu ditambahkan sebagai lesson tersendiri (M3-L3 atau L4), karena aspek keamanan & regulasi ini bobotnya cukup besar (1 dari 5 elemen kompetensi) |
| Sikap: teliti, sistematis, tanggung jawab keamanan | Terintegrasi ke semua lesson M3 | ✅ Jelas |

### J.62AIN00.016.1 — Merencanakan Perawatan Solusi AI (→ Modul 4)

| Butir | Rencana Penempatan | Status |
|---|---|---|
| Strategi & lingkungan operasional komponen sistem | M4-L1 | ✅ Jelas |
| Pembuatan laporan hasil perencanaan perawatan | M4-L2 (menyusun rencana) | ✅ Jelas |
| Tools & troubleshoot monitoring | M4-L1 (menyiapkan rencana — butuh hasil monitoring) | ✅ Jelas |
| Parameter evaluasi (akurasi, presisi, recall, F1, kohesi, MAE) | **Perlu lesson konsep tersendiri** — ini istilah teknis yang butuh penjelasan sebelum dipakai | ⚠️ Perlu dipastikan ada penjelasan eksplisit, bukan diasumsikan peserta sudah tahu |
| Sikap: sistematis, teliti | Terintegrasi ke semua lesson M4 | ✅ Jelas |

### J.62AIN00.017.1 — Merawat Solusi AI (→ Modul 5)

| Butir | Rencana Penempatan | Status |
|---|---|---|
| Lingkungan operasional sistem Solusi AI | M5-L1 | ✅ Jelas |
| Tools operasional Solusi AI | M5-L2 (melakukan perawatan) | ✅ Jelas |
| Tools pengembangan Solusi AI | M5-L2 | ✅ Jelas |
| Sikap: teliti, wawasan luas kebutuhan perawatan | Terintegrasi | ✅ Jelas |
| Ketergantungan pada Modul 4 (rencana perawatan sbg input) | Perlu cross-reference eksplisit — unit ini secara literal butuh output dari unit sebelumnya sebagai "rencana perawatan" | ✅ Sudah tercatat di bagian Prasyarat Kompetensi, tinggal dipastikan lesson pembuka M5 mereferensikan output M4 |

### J.63OPR00.014.2 — Melakukan Pemasukan Data (→ Modul 1)

| Butir | Rencana Penempatan | Status |
|---|---|---|
| Jenis-jenis file, manajemen file | M1-L1 | ✅ Jelas |
| Mengetik pada keyboard | Tidak perlu lesson konsep — ini keterampilan motorik dasar, cukup disebut sebagai prasyarat | ✅ Jelas (tidak perlu konten khusus) |
| Elemen 3: Meng-import data dari sumber elektronis | **Perlu lesson tersendiri** — beda keterampilan dari elemen 1-2 (input manual vs import file) | 🔴 Gap — draft M1 lama kemungkinan hanya cover elemen 1-2; pastikan ada lesson import data |
| Sikap: disiplin, teliti, tanggung jawab, kerjasama tim | Terintegrasi | ✅ Jelas |

### J.63OPR00.015.2 — Memastikan Validitas Data (→ Modul 1)

| Butir | Rencana Penempatan | Status |
|---|---|---|
| Konsep jenis data, konsep kualitas data | M1-L2 | ✅ Jelas |
| Elemen 2: referensi & kodifikasi data | **Perlu lesson tersendiri** — konsep "referensi data" dan "kodifikasi" cukup teknis, jangan digabung sekilas dengan elemen 1 | ⚠️ Perlu dipastikan tidak terlalu dipadatkan |
| Elemen 4: pemutakhiran data | **Perlu lesson tersendiri** — ini proses yang beda dari sekadar "memeriksa validitas" (elemen 3), sifatnya korektif/berkelanjutan | 🔴 Gap — mudah lolos kalau modul cuma fokus ke "cara mengecek data valid atau tidak" |

---

## Ringkasan Gap yang Ditemukan (untuk ditindaklanjuti)

1. 🔴 **M3 (Deployment)** — Elemen "menerapkan pengamanan & kepatuhan data" belum punya lesson eksplisit di draft modul awal. Ini 1 dari 5 elemen kompetensi unit 015.1 — porsinya signifikan, tidak boleh jadi catatan sampingan di lesson lain.
2. 🔴 **M1 (Pemasukan Data)** — Elemen "import data dari sumber elektronis" butuh lesson terpisah dari input manual biasa.
3. 🔴 **M1 (Validitas Data)** — Elemen "pemutakhiran data" (data update/correction) butuh lesson terpisah, jangan digabung sekilas ke "memeriksa validitas".
4. ⚠️ **M2/M3 tumpang tindih CI/CD** — konsep CI/CD muncul di unit integrasi (014.1) dan unit deployment (015.1). Perlu diputuskan: dijelaskan sekali secara mendalam di M2, lalu direferensikan (bukan diulang) di M3 — supaya tidak boros durasi dan tidak membingungkan peserta dengan penjelasan yang beda framing di dua tempat.
5. ⚠️ **M4** — Parameter evaluasi (akurasi, presisi, recall, F1-score, MAE) adalah istilah statistik/ML yang punya prasyarat pemahaman. Perlu dipastikan ada penjelasan konsep yang cukup, bukan diasumsikan peserta B2B sudah familiar.

**Implikasi jumlah lesson:** dengan gap-gap ini, kemungkinan besar **tidak semua modul akan punya jumlah lesson yang sama** — ini mengonfirmasi kekhawatiranmu sebelumnya bahwa pola "4 lesson rata per modul" dari HCAI Foundations tidak otomatis cocok untuk kursus ini. M3 dan M1 kemungkinan butuh lebih banyak lesson (5-6) dibanding M4/M5 yang unit kompetensinya lebih ramping (4 lesson bisa cukup).

---

 — AI untuk Proses Data. Update terakhir: Juli 2026.*
