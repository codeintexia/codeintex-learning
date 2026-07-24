# Kursus 2: Sistem Variabel Studi Kasus per Audiens
## Template + Config Bank (Training Juli 2026)

**Prinsip dasar:** Mekanika proses & data (yang dinilai asesor BNSP) harus IDENTIK lintas audiens. Yang boleh berubah hanya "kulit narasi" — nama organisasi, istilah domain, skenario yang relate ke industri. Ini menjaga keadilan penilaian antar cohort training yang berbeda klien.

---

## A. SKEMA VARIABEL (Template Abstrak)

Setiap audiens punya satu file config berisi variabel berikut. Lesson MDX ditulis dengan placeholder yang merujuk ke variabel ini (mis. `{{org.name}}`, `{{case.field_1}}`), bukan hardcode teks per audiens.

```yaml
# audience-config-template.yaml
audience_id: string              # slug unik, mis. "bank", "tendik-kampus"
audience_label: string           # label tampilan, mis. "Pegawai Bank"

organisasi:
  nama: string                   # nama organisasi fiktif
  jenis_industri: string
  regulator: string              # badan regulasi yang relevan (jika ada)

solusi_ai:
  nama_solusi: string            # nama fiktif Solusi AI yang jadi "benang merah"
  tujuan_bisnis: string          # sasaran bisnis Solusi AI (dipakai konsisten dari M1-M6)
  jenis_model: string            # mis. "credit scoring", "prediksi drop-out"

data_M1:                         # untuk Modul 1: Pemasukan & Validitas Data
  jenis_data_utama: string       # mis. "data pengajuan kredit nasabah"
  field_list: array              # daftar field — TIPE datanya harus konsisten lintas audiens
  dokumen_fisik: string          # jenis dokumen yang di-scan (elemen 2.4 KUK)
  contoh_data_tidak_valid: array # skenario kesalahan data yang harus dideteksi peserta
  sumber_import_elektronis: string # untuk elemen 3 (import data) — mis. "file CSV dari core banking"

komponen_M2:                     # untuk Modul 2: Integrasi
  daftar_komponen: array         # komponen yang diintegrasikan (jumlah HARUS sama lintas audiens)
  teknologi_integrasi: string    # REST API / GraphQL / gRPC — boleh sama, ini teknis bukan naratif

deployment_M3:                   # untuk Modul 3: Deployment
  lingkungan_deployment: string  # on-premise / cloud / edge — dipilih sesuai konteks regulasi industri
  regulasi_kepatuhan: array      # regulasi spesifik industri (mengisi elemen 4 KUK yang tadinya gap)

evaluasi_M4:                     # untuk Modul 4: Rencana Perawatan
  parameter_evaluasi_relevan: array  # parameter mana yang paling relevan didemonstrasikan (akurasi/precision/recall/dst — tetap semua dijelaskan, tapi contoh kasus pilih yang relevan)
  skenario_penurunan_performa: string # mis. "model gagal mendeteksi pola nasabah baru pasca perubahan kebijakan bunga"

insiden_M5:                      # untuk Modul 5: Perawatan
  skenario_insiden_operasional: string
```

**Yang TIDAK boleh masuk sebagai variabel** (harus tetap identik untuk semua audiens):
- Jumlah field data di M1 (jumlah kolom yang harus diperiksa/divalidasi peserta)
- Jumlah komponen yang diintegrasikan di M2
- Jumlah & jenis parameter evaluasi yang dijelaskan konsepnya di M4 (semua tetap dijelaskan lengkap — akurasi, presisi, recall, F1, MAE — hanya contoh kasusnya yang dipilih relevan)
- Urutan proses/lifecycle M1→M6
- Checkpoint KUK di tiap Quick Check

---

## B. CONFIG TERISI — AUDIENS: PEGAWAI BANK

```yaml
audience_id: bank
audience_label: "Pegawai Bank"

organisasi:
  nama: "Bank Nusantara Sejahtera"       # nama fiktif, tidak merujuk bank riil manapun
  jenis_industri: "Perbankan"
  regulator: "Otoritas Jasa Keuangan (OJK)"

solusi_ai:
  nama_solusi: "Sistem Penilaian Kredit Otomatis (SPKO)"
  tujuan_bisnis: "Mempercepat proses persetujuan kredit tanpa mengorbankan akurasi penilaian risiko"
  jenis_model: "Credit scoring (klasifikasi risiko kredit nasabah)"

data_M1:
  jenis_data_utama: "Data pengajuan kredit nasabah"
  field_list:
    - "Nomor identitas nasabah (KTP)"
    - "Nama lengkap"
    - "Penghasilan bulanan"
    - "Riwayat kredit (skor internal)"
    - "Jumlah pengajuan pinjaman"
    - "Status pekerjaan"
  dokumen_fisik: "Formulir pengajuan kredit fisik dan salinan KTP nasabah"
  contoh_data_tidak_valid:
    - "Nomor KTP dengan jumlah digit tidak sesuai standar"
    - "Penghasilan bulanan diisi dengan nilai negatif"
    - "Field status pekerjaan kosong padahal wajib diisi"
  sumber_import_elektronis: "File data nasabah dalam format CSV hasil ekspor dari sistem core banking"

komponen_M2:
  daftar_komponen:
    - "Model credit scoring (machine learning)"
    - "Sistem core banking (basis data nasabah)"
    - "Dashboard pengambilan keputusan untuk petugas kredit"
  teknologi_integrasi: "REST API untuk komunikasi antara model scoring dan core banking"

deployment_M3:
  lingkungan_deployment: "On-premise (server internal bank) — sesuai kebijakan keamanan data perbankan yang membatasi penempatan data nasabah di luar infrastruktur bank"
  regulasi_kepatuhan:
    - "POJK Nomor 11/POJK.03/2022 tentang Penyelenggaraan Teknologi Informasi Oleh Bank Umum — Pasal 15 ayat (3) mewajibkan manajemen risiko atas algoritma dan model machine learning (bias, kesalahan prediksi, ketergantungan data tidak akurat)"
    - "Panduan OJK 'Tata Kelola Kecerdasan Artifisial Perbankan Indonesia' (terbit April 2025) — melengkapi POJK 11/2022, SEOJK 29/2022 (Ketahanan & Keamanan Siber), SEOJK 24/2023 (Maturitas Digital)"
    - "Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (disahkan 17 Oktober 2022) — karena data nasabah tergolong data pribadi"

evaluasi_M4:
  parameter_evaluasi_relevan:
    - "Akurasi (ketepatan keseluruhan prediksi risiko kredit)"
    - "Presisi (dari nasabah yang diprediksi layak, berapa persen benar-benar layak)"
    - "Recall (dari nasabah yang benar-benar layak, berapa persen berhasil terdeteksi model)"
  skenario_penurunan_performa: "Model SPKO mulai salah menilai nasabah baru setelah OJK menerbitkan kebijakan suku bunga baru — pola data lama tidak lagi merepresentasikan kondisi pasar"

insiden_M5:
  skenario_insiden_operasional: "Tim IT bank menemukan waktu respons SPKO melambat signifikan saat volume pengajuan kredit meningkat di akhir bulan — perlu perawatan kapasitas sistem"
```

---

## C. Bagaimana Ini Dipakai dalam Penulisan Lesson

Setiap lesson di `content/courses/ai-proses-data/` ditulis dengan merujuk variabel dari config, bukan menulis "Bank Nusantara Sejahtera" secara hardcode langsung di teks. Praktisnya untuk Phase 1 (tanpa sistem templating runtime), ada dua opsi implementasi:

**Opsi 1 — Generate saat authoring (direkomendasikan untuk sekarang):**
Lesson MDX ditulis sekali dengan variabel config bank ini "dicetak permanen" ke dalam teks (bukan placeholder hidup). Kalau nanti butuh varian tendik kampus, kita duplikasi struktur lesson yang sama, ganti isi sesuai config baru, tapi checklist KUK/struktur/jumlah lesson tetap identik karena mengikuti template & matriks cross-check yang sama.

**Opsi 2 — Templating runtime (butuh Phase 2+):**
Lesson MDX pakai komponen `<CaseVariable name="organisasi.nama" />` yang di-resolve saat render berdasarkan audience yang login. Ini baru masuk akal setelah ada auth (Phase 2), karena baru saat itu sistem tahu siapa yang sedang login dan config mana yang harus dipakai.

**Rekomendasi saya:** pakai Opsi 1 untuk training bulan ini. Tapi karena penulisan lesson akan saya susun dengan disiplin merujuk ke variabel config di atas (bukan menulis bebas), transisi ke Opsi 2 nanti jadi jauh lebih murah — tinggal mencari-ganti teks hardcode dengan placeholder, karena kita sudah tahu persis bagian mana yang variabel dan mana yang fixed.

---

*Dokumen ini adalah pelengkap dari `kursus2-skkni-reference.md`. Update terakhir: Juli 2026.*
