---
course: hcai-foundations
module: 5
module_title: "Designing Human-Centered AI with IFRAME"
lesson: 4
title: "Latihan Terpandu: Menerapkan IFRAME pada Satu Fitur AI"
duration_minutes: 18
bloom_level: apply
keywords:
  - HCAI design exercise
  - applied human-centered AI
  - IFRAME practice
  - AI feature design walkthrough
  - decision orchestration exercise
is_free: true
status: draft
---

# Latihan Terpandu: Menerapkan IFRAME pada Satu Fitur AI

**Modul 5 · Designing Human-Centered AI with IFRAME** · Lesson 4 dari 4
**Estimasi waktu baca:** ~5 menit · **Estimasi waktu pengerjaan:** 12–15 menit tambahan · **Level:** Foundational · **Prasyarat:** M5-L1 s/d M5-L3

---

> **Yang akan kamu capai di lesson ini:**
> - Menerapkan keenam tahap IFRAME secara berurutan pada satu skenario fitur AI yang realistis
> - Menggunakan template decision log untuk mendokumentasikan satu keputusan kritis
> - Membangun koneksi antara penggunaan IFRAME dan empat prinsip HCAI dalam konteks desain nyata

---

## Pengantar

Kita sudah memahami mengapa proses konvensional tidak cukup (L1), bagaimana IFRAME bekerja (L2), dan bagaimana insight riset diterjemahkan ke keputusan desain (L3). Lesson ini adalah tentang menggunakannya.

Ingat dari M1-L4: kamu sudah memilih satu produk AI untuk dianalisis sepanjang kursus ini. Lesson ini memberikan dua jalur:

**Jalur A:** Gunakan skenario yang sudah disediakan di bawah (direkomendasikan untuk pertama kali).

**Jalur B:** Gunakan produk AI yang kamu pilih sendiri sejak M1-L4. Ini adalah persiapan langsung untuk capstone di M6.

---

## Skenario: Fitur "Rekomendasi Pinjaman Cerdas" untuk Aplikasi Fintech

Kamu adalah anggota tim produk di sebuah perusahaan fintech Indonesia yang sedang membangun fitur baru: **sistem AI yang merekomendasikan produk pinjaman yang paling sesuai** untuk pengguna berdasarkan profil keuangan, riwayat transaksi, dan pola penggunaan aplikasi.

Konteks:
- Perusahaan melayani 2 juta pengguna aktif, 60% di antaranya adalah pekerja informal atau wirausaha kecil
- Fitur ini akan memengaruhi keputusan kredit yang berdampak signifikan pada kehidupan pengguna
- Tim memiliki 3 bulan sebelum peluncuran

---

## Panduan Pengerjaan IFRAME

### Tahap 1 — Identify

Jawab pertanyaan-pertanyaan berikut (tuliskan jawabanmu sebelum membaca panduan di bawah):

**Pertanyaan:**
1. Siapa saja pemangku kepentingan yang terdampak — langsung maupun tidak langsung?
2. Apa konteks penggunaan yang berbeda yang perlu dipertimbangkan?
3. Apa asumsi kritis yang perlu divalidasi sebelum desain dimulai?
4. Di kondisi apa sistem sebaiknya *tidak* beroperasi?

**Panduan analisis:**

Pemangku kepentingan yang sering terlewat: pekerja informal yang tidak memiliki riwayat kredit formal, pasangan/keluarga yang terpengaruh keputusan pinjaman, dan pengawas OJK yang perlu mengaudit sistem.

Asumsi kritis yang perlu divalidasi: "pengguna memahami bahwa ini adalah rekomendasi, bukan keputusan final bank." Dari pembelajaran M2, ini adalah asumsi yang sangat sering salah.

---

### Tahap 2 — Flow

**Pertanyaan:**
1. Gambarkan alir utama: dari mana pengguna memulai sampai keputusan diambil?
2. Di mana dalam alir ini AI membuat keputusan atau rekomendasi?
3. Siapa yang terdampak di setiap titik keputusan AI dalam alir?

**Panduan analisis:**

Alir yang sering terlupakan: **alir penolakan** — apa yang terjadi ketika pengguna mendapat rekomendasi negatif atau tidak ada produk yang sesuai? Alir ini sama pentingnya dengan alir sukses, tapi jarang didesain dengan seksama.

Titik kritis dalam alir ini yang perlu didesain secara eksplisit:
- Bagaimana sistem mengomunikasikan uncertainty rekomendasinya?
- Kapan dan bagaimana sistem menyarankan pengguna untuk berkonsultasi dengan manusia?
- Apa yang terjadi jika pengguna tidak setuju dengan rekomendasi?

---

### Tahap 3 — Rank

**Pertanyaan:**
1. Dari semua yang perlu dibangun, apa yang paling kritis untuk diluncurkan pertama?
2. Trade-off apa yang paling berat yang harus diputuskan secara eksplisit?
3. Apa yang *tidak* akan dibangun di versi pertama — dan mengapa?

**Panduan analisis:**

Trade-off kritis yang harus didokumentasikan untuk fitur ini:

| Trade-off | Opsi A | Opsi B |
|---|---|---|
| Akurasi vs eksplanabilitas | Model yang lebih akurat tapi black box | Model sedikit kurang akurat tapi bisa dijelaskan |
| Personalisisasi vs privasi | Gunakan semua data tersedia | Gunakan subset data dengan consent eksplisit |
| Kecepatan pengambilan keputusan | Tampilkan satu rekomendasi langsung | Tampilkan beberapa opsi dengan perbandingan |

Setiap pilihan dalam trade-off ini harus terdokumentasi dalam decision log — bukan hanya yang dipilih, tapi mengapa yang lain tidak dipilih.

---

### Tahap 4 — Apply

**Pertanyaan:**
1. Bagaimana mekanisme transparansi diimplementasikan dalam antarmuka?
2. Di mana kontrol manusia yang bermakna dibangun dalam alir?
3. Bagaimana sistem mengomunikasikan batasnya kepada pengguna?

**Panduan analisis:**

Tiga mekanisme konkret yang perlu ada berdasarkan prinsip HCAI (M3):

**Transparency (M3-L1):** Label yang jelas bahwa rekomendasi dihasilkan AI, dengan penjelasan ringkas tentang faktor utama yang mempengaruhi rekomendasi (bukan SHAP values — kalimat sederhana yang bisa dipahami pengguna biasa).

**Human Control (M3-L3):** Tombol "Saya tidak setuju" atau "Hubungi konsultan" yang proaktif muncul, bukan tersembunyi. Perlu diuji apakah kontrol ini bermakna dalam kondisi nyata — bukan hanya nominal.

**Accountability (M3-L4):** Setiap rekomendasi meninggalkan jejak: model versi berapa, faktor apa yang digunakan, kapan dihasilkan. Ini bukan untuk pengguna — ini adalah infrastruktur accountability internal.

---

### Tahap 5 — Measure

**Pertanyaan:**
1. Kriteria sukses apa yang akan digunakan untuk mengevaluasi fitur ini?
2. Metrik apa yang perlu didisagregasi berdasarkan segmen pengguna?
3. Bagaimana kamu akan mengukur trust calibration — bukan hanya kepuasan?

**Panduan analisis:**

Metrik yang paling sering terlewat untuk fitur AI kredit:

- **False negative rate per segmen:** Apakah pekerja informal mendapat false negative (ditolak padahal seharusnya diterima) lebih sering dari karyawan tetap?
- **Trust calibration:** Apakah pengguna yang mengikuti rekomendasi memiliki outcome yang lebih baik dari yang mengabaikannya? Jika ya, sistem earning trust-nya. Jika tidak, ada miskalibrasi.
- **Mekanisme banding utilization:** Apakah pengguna yang tidak setuju menggunakan mekanisme banding? Jika tidak, apakah karena sistemnya bekerja atau karena mekanismenya tidak terlihat?

---

### Tahap 6 — Expose

**Pertanyaan:**
1. Keputusan apa yang paling penting untuk didokumentasikan agar tim berikutnya bisa memahami mengapa sistem dibangun dengan cara ini?
2. Pola apa yang ditemukan dalam testing yang perlu diketahui oleh tim yang memperbarui model di masa depan?
3. Asumsi awal mana yang terbukti benar dan mana yang terbukti salah?

**Panduan analisis:**

Artefak Expose yang paling kritis untuk fitur ini adalah satu dokumen yang menjawab: *"Jika model diperbarui enam bulan dari sekarang, apa yang harus tim baru ketahui tentang keputusan desain yang sudah dibuat?"*

Ini mencakup: keputusan trade-off di Rank, mekanisme transparency yang dipilih dan mengapa, temuan fairness dari disagregasi pertama, dan populasi mana yang ternyata paling berbeda dari asumsi awal.

---

## Template Decision Log — Gunakan Ini

Pilih satu keputusan kritis dari tahap Rank atau Apply, lalu isi template ini:

```
Keputusan:
[Deskripsi satu kalimat tentang apa yang diputuskan]

Konteks:
[Insight riset atau kondisi yang memotivasi keputusan ini]
[Referensi ke tipe insight: mental model / trust calibration /
 flow disruption / fairness persepsi]

Alternatif yang dipertimbangkan:
[Opsi 1]: ...
[Opsi 2]: ...

Alasan pemilihan:
[Mengapa opsi yang dipilih lebih baik dari alternatif,
 dalam konteks alir dan prinsip HCAI yang relevan]

Trade-off yang diterima:
[Apa yang dikorbankan dengan pilihan ini]

Prinsip HCAI yang paling relevan:
[ ] Transparency  [ ] Fairness  [ ] Human Control  [ ] Accountability

Siapa yang memutuskan:
[Nama / peran]

Tanggal:
[Tanggal keputusan]
```

---

## Koneksi ke Capstone M6

Latihan ini adalah persiapan langsung untuk capstone Modul 6. Di M6, kamu akan:

1. Menggunakan produk AI yang kamu pilih sejak M1-L4
2. Menerapkan seluruh kerangka kursus ini — empat prinsip HCAI (M3), eksplanabilitas dan fairness (M4), dan IFRAME (M5) — dalam satu analisis yang terintegrasi
3. Menghasilkan dokumen evaluasi dengan rekomendasi konkret yang bisa diimplementasikan

Decision log yang kamu buat hari ini adalah salah satu artefak yang akan diminta di capstone.

---

## Pertanyaan Refleksi

> Latihan ini mungkin mengungkap keputusan-keputusan yang terasa sulit untuk dibuat secara eksplisit — trade-off yang tidak ada jawaban "benar"nya, pilihan yang membutuhkan kompromi antara nilai-nilai yang sama pentingnya.
>
> **Dari enam tahap IFRAME yang baru kamu kerjakan**, tahap mana yang paling sulit? Apakah kesulitannya bersifat teknis (tidak tahu bagaimana melakukannya) atau bersifat organisasi (tahu bagaimana, tapi tidak ada ruang untuk melakukannya dalam proses yang ada)?

---

## Ringkasan Modul 5

Modul ini membangun kemampuan untuk merancang sistem AI yang human-centered secara aktif:

- **L1:** Proses desain konvensional tidak cukup untuk AI — empat tantangan unik membutuhkan lapisan governance di atasnya.
- **L2:** IFRAME sebagai metodologi governance layer — enam tahap yang mengorkestrasikan keputusan dan mengelola bukti, dengan alir sebagai unit pengorganisasi sentral.
- **L3:** Translation gap antara riset dan implementasi — empat tipe insight dan decision log sebagai jembatan yang memastikan insight tidak hilang.
- **L4:** Latihan terpandu — menerapkan IFRAME secara penuh pada satu fitur AI nyata, dengan decision log sebagai output utama.

**Modul 6** adalah modul terakhir: bagaimana mengevaluasi sistem HCAI yang sudah ada — dan capstone di mana semua yang dipelajari sepanjang kursus diintegrasikan dalam satu analisis menyeluruh.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
