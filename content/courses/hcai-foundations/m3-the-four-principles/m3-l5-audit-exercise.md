---
course: hcai-foundations
module: 3
module_title: "The Four Principles — What HCAI Demands"
lesson: 5
title: "Latihan Terapan: Audit Empat Prinsip HCAI pada Produk AI Nyata"
duration_minutes: 18
bloom_level: apply
keywords:
  - HCAI principles audit exercise
  - responsible AI checklist
  - AI product audit framework
  - human-centered AI evaluation tool
is_free: true
status: draft
---

# Latihan Terapan: Audit Empat Prinsip HCAI pada Produk AI Nyata

**Modul 3 · The Four Principles — What HCAI Demands** · Lesson 5 dari 5
**Estimasi waktu baca:** ~5 menit · **Estimasi waktu pengerjaan:** 10–15 menit tambahan · **Level:** Foundational · **Prasyarat:** M3-L1 s/d M3-L4

---

> **Yang akan kamu capai di lesson ini:**
> - Menerapkan kerangka empat prinsip HCAI sebagai alat audit terstruktur pada satu produk AI nyata
> - Mengidentifikasi celah spesifik berdasarkan pertanyaan diagnostik per prinsip
> - Mendeskripsikan satu rekomendasi konkret untuk setiap prinsip yang dinilai lemah

---

## Pengantar

Empat lesson sebelumnya membangun pemahaman konseptual tentang Transparency, Fairness, Human Control, dan Accountability. Lesson ini adalah tentang menggunakan keempat prinsip itu sebagai alat kerja — bukan sebagai teori yang dibaca, melainkan sebagai checklist yang dijalankan.

Ingat dari M1-L4 bahwa keempat prinsip ini pertama kali diperkenalkan sebagai "peta" — masing-masing dengan satu pertanyaan diagnostik. Lesson ini memperluas pertanyaan diagnostik itu menjadi checklist yang lebih operasional, siap digunakan pada produk nyata.

Ini bukan kuis. Tidak ada jawaban benar atau salah. Tujuannya adalah melatih cara berpikir yang akan kamu gunakan di capstone Modul 6 — di mana kamu akan melakukan audit yang lebih mendalam dengan semua alat dari kursus ini.

---

## Cara Menggunakan Audit Ini

**Langkah 1:** Pilih satu produk atau fitur AI yang kamu kenal dengan baik — bisa produk yang kamu gunakan sehari-hari, yang kamu kerjakan, atau yang kamu pelajari.

**Langkah 2:** Untuk setiap prinsip, baca pertanyaan diagnostiknya dan jawab *Ya*, *Sebagian*, atau *Tidak*. Gunakan baris "Catatan" untuk mencatat observasi spesifik.

**Langkah 3:** Untuk setiap prinsip yang kamu nilai *Tidak* atau *Sebagian*, tulis satu rekomendasi konkret — tindakan spesifik yang bisa diambil untuk memperkuat prinsip itu.

**Langkah 4:** Lihat pola yang muncul. Apakah ada satu prinsip yang secara konsisten lemah? Apakah kelemahannya saling berkaitan?

---

## Checklist Audit HCAI

### Prinsip 1 — Transparency

| Pertanyaan diagnostik | Ya / Sebagian / Tidak |
|---|---|
| Apakah pengguna tahu bahwa keputusan ini dibuat oleh AI? | |
| Apakah pengguna bisa mengetahui faktor apa yang mempengaruhi keputusan? | |
| Apakah sistem mengomunikasikan kondisi di mana ia bisa salah? | |
| Apakah penjelasan diberikan secara proaktif, tanpa perlu diminta? | |

**Catatan observasi:**

**Rekomendasi (jika ada yang *Tidak* atau *Sebagian*):**

---

### Prinsip 2 — Fairness

| Pertanyaan diagnostik | Ya / Sebagian / Tidak |
|---|---|
| Apakah performa sistem sudah diperiksa untuk kelompok pengguna yang berbeda? | |
| Apakah data pelatihan sudah diperiksa dari bias historis yang relevan? | |
| Apakah definisi fairness yang digunakan sudah dideklarasikan secara eksplisit? | |
| Apakah kelompok yang paling terdampak dilibatkan dalam desain dan evaluasi? | |

**Catatan observasi:**

**Rekomendasi (jika ada yang *Tidak* atau *Sebagian*):**

---

### Prinsip 3 — Human Control

| Pertanyaan diagnostik | Ya / Sebagian / Tidak |
|---|---|
| Apakah ada mekanisme override yang bisa digunakan dalam kondisi nyata (bukan hanya teknis)? | |
| Apakah tingkatan keterlibatan manusia sesuai dengan taruhan keputusannya? | |
| Apakah pengguna terlatih dan tahu kapan harus mengintervensi sistem? | |
| Apakah sistem menampilkan informasi yang cukup untuk intervensi yang terinformasi? | |

**Catatan observasi:**

**Rekomendasi (jika ada yang *Tidak* atau *Sebagian*):**

---

### Prinsip 4 — Accountability

| Pertanyaan diagnostik | Ya / Sebagian / Tidak |
|---|---|
| Apakah ada entitas yang jelas bertanggung jawab jika sistem merugikan pengguna? | |
| Apakah ada mekanisme banding yang bisa diakses oleh pengguna yang terdampak? | |
| Apakah sistem meninggalkan jejak audit yang bisa diperiksa setelah insiden? | |
| Apakah ada proses untuk mendokumentasikan dan belajar dari kegagalan sistem? | |

**Catatan observasi:**

**Rekomendasi (jika ada yang *Tidak* atau *Sebagian*):**

---

## Contoh Walkthrough: Google Maps Navigasi

Untuk memberikan gambaran tentang cara mengisi audit ini, berikut contoh singkat menggunakan Google Maps sebagai produk AI yang umum dikenal.

**Transparency:**
- Pengguna tahu rute dihasilkan oleh algoritma ✓
- Pengguna bisa melihat alasan rute tertentu disarankan (ada lalu lintas, estimasi waktu) ✓ *Sebagian* — informasinya ada tapi terbatas
- Batas sistem (akurasi di daerah dengan data crowdsourced rendah) tidak dikomunikasikan secara proaktif ✗
- **Celah:** Pengguna di daerah terpencil tidak tahu bahwa akurasi estimasi waktu bisa jauh lebih rendah dari biasanya.

**Fairness:**
- Data lebih kaya untuk daerah perkotaan padat dibanding pedesaan dan daerah berkembang — ketimpangan dalam kualitas layanan yang tidak dikomunikasikan *Sebagian*
- **Celah:** Pengguna di Indonesia di luar Jawa mungkin mendapat kualitas navigasi yang berbeda tanpa menyadarinya.

**Human Control:**
- Pengguna bisa memilih rute alternatif atau mengabaikan navigasi kapan saja ✓
- Kontrol bermakna tersedia dan mudah digunakan ✓
- **Kekuatan terbesar** dari perspektif Human Control di antara produk AI konsumen.

**Accountability:**
- Tidak ada mekanisme banding yang jelas jika navigasi menyebabkan kerugian (salah rute yang menyebabkan kecelakaan, misalnya) ✗
- Tanggung jawab hukum didistribusikan ke pengguna melalui syarat layanan ✗
- **Celah:** Pengguna yang dirugikan tidak memiliki jalur yang jelas untuk mendapat kompensasi atau koreksi.

**Pola yang terlihat:** Google Maps relatif kuat di Transparency dan Human Control, tapi lemah di Accountability dan fairness geografis. Ini konsisten dengan produk konsumen yang dirancang untuk kenyamanan penggunaan tapi tidak untuk akuntabilitas konsekuensi.

---

## Panduan Interpretasi Hasil

**Jika sebagian besar jawaban *Ya*:** Produk ini sudah menerapkan prinsip HCAI dengan baik di area yang kamu periksa. Tantangan selanjutnya: apakah penerapannya konsisten di semua segmen pengguna, atau hanya di kelompok yang paling terlihat?

**Jika banyak *Sebagian*:** Fondasi sudah ada tapi implementasinya tidak konsisten atau tidak lengkap. Ini adalah titik perbaikan yang paling actionable — perbaikan inkremental yang spesifik bisa memberikan dampak besar.

**Jika banyak *Tidak*:** Ini adalah sinyal bahwa prinsip-prinsip ini belum menjadi prioritas dalam desain produk. Mulai dari yang paling mudah — seringkali Transparency adalah prinsip yang paling cepat bisa diperbaiki dengan perubahan UX yang relatif kecil.

---

## Koneksi ke Capstone Modul 6

Audit singkat ini adalah latihan pertama dari capstone yang akan kamu kerjakan di Modul 6. Di sana, kamu akan menggunakan kerangka yang lebih lengkap — menambahkan perspektif dari Modul 4 (explainability dan bias dalam praktik) dan Modul 5 (IFRAME) — untuk menghasilkan analisis yang lebih mendalam dan rekomendasi yang lebih terstruktur.

Simpan produk yang kamu pilih hari ini. Kamu akan kembali menganalisisnya di Modul 6 dengan lebih banyak alat.

---

## Pertanyaan Refleksi

> Setelah menjalankan audit ini, **prinsip mana yang paling mengejutkan kamu** — baik karena lebih kuat dari yang kamu ekspektasikan, atau lebih lemah?
>
> Dan dari semua celah yang kamu temukan, mana yang paling mudah diperbaiki dalam 30 hari — dan mana yang membutuhkan perubahan mendasar dalam cara produk dirancang?

---

## Ringkasan Modul 3

Kita telah menempuh empat prinsip HCAI secara mendalam dan menggunakannya sebagai alat audit:

- **L1 · Transparency:** Tiga lapisan (proses, faktor, batas) dan pentingnya transparansi proaktif — kasus Belanda menunjukkan konsekuensi fatal dari ketidaktransparanan sistemik.
- **L2 · Fairness:** Netral algoritmik ≠ adil — tiga definisi fairness yang saling bertentangan dan mengapa memilihnya adalah keputusan nilai, bukan teknis.
- **L3 · Human Control:** Kontrol nominal vs bermakna, tiga tingkatan keterlibatan manusia, dan Ironies of Automation — kasus 737 MAX sebagai peringatan paling kuat.
- **L4 · Accountability:** Many hands problem, tiga level akuntabilitas, dan empat mekanisme konkret — kasus Uber menunjukkan konsekuensi ketika semua level gagal bersamaan.
- **L5 · Latihan terapan:** Checklist audit HCAI yang bisa langsung digunakan.

**Modul 4** akan membawa dua prinsip paling teknis — Transparency dan Fairness — ke level implementasi yang lebih dalam: bagaimana explainability bekerja dalam praktik, dan bagaimana mendeteksi serta merespons bias dalam sistem nyata.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
