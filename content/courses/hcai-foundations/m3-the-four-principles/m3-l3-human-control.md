---
course: hcai-foundations
module: 3
module_title: "The Four Principles — What HCAI Demands"
lesson: 3
title: "Human Control: Ketika Manusia Harus Tetap Memegang Kendali yang Bermakna"
duration_minutes: 12
bloom_level: understand
keywords:
  - human control AI systems
  - meaningful human oversight AI
  - human in the loop AI
  - automation control design
  - ironies of automation
is_free: true
status: draft
---

# Human Control: Ketika Manusia Harus Tetap Memegang Kendali yang Bermakna

**Modul 3 · The Four Principles — What HCAI Demands** · Lesson 3 dari 5
**Estimasi waktu baca:** 12 menit · **Level:** Foundational · **Prasyarat:** M3-L2

---

> **Yang akan kamu capai di lesson ini:**
> - Menjelaskan perbedaan antara kontrol nominal dan kontrol bermakna dalam sistem AI
> - Mengidentifikasi tiga tingkatan keterlibatan manusia dalam pengawasan sistem AI beserta konteks penggunaannya
> - Menginterpretasi "Ironies of Automation" sebagai kerangka untuk memahami mengapa kontrol sering gagal justru saat paling dibutuhkan

---

## Hook

29 Oktober 2018. Lion Air penerbangan 610 jatuh ke Laut Jawa 13 menit setelah lepas landas dari Jakarta. Seluruh 189 orang di dalamnya tidak selamat.

29 Maret 2019. Ethiopian Airlines penerbangan 302 jatuh enam menit setelah lepas landas dari Addis Ababa. Seluruh 157 orang di dalamnya tidak selamat.

Penyebab keduanya: sistem otomasi bernama MCAS (*Maneuvering Characteristics Augmentation System*) yang dipasang di Boeing 737 MAX secara berulang mendorong hidung pesawat ke bawah berdasarkan data sensor yang salah — dan pilot di kedua penerbangan itu tidak berhasil menghentikannya.

Yang membuat kasus ini sangat penting bagi HCAI bukan hanya tragedinya, melainkan **apa yang terungkap dari investigasi**: pilot secara teknis memiliki kemampuan untuk menonaktifkan MCAS. Prosedur ada di manual. Tombol tersedia di kokpit.

Tapi kontrol itu tidak bermakna dalam kondisi nyata. Para pilot tidak pernah dilatih untuk menghadapi perilaku MCAS karena Boeing tidak mendokumentasikan sistem ini secara penuh di manual pilot untuk menghindari biaya pelatihan ulang. Dalam kekacauan kokpit dengan sensor-sensor yang saling bertentangan dan alarm yang berbunyi bersamaan, menemukan dan menggunakan prosedur yang tidak pernah dilatih adalah tugas yang melampaui kapasitas kognitif manusia dalam situasi darurat.

Kontrol nominal ada. Kontrol bermakna tidak.

---

## Kerangka Konseptual

### Mengapa perbedaan kontrol nominal vs bermakna kritis

Kita sudah memperkenalkan perbedaan ini di M1-L3 dalam konteks Shneiderman. Di lesson ini, kita mendalami mekanisme psikologis dan desainnya.

**Kontrol nominal** adalah kontrol yang secara teknis tersedia dalam sistem — tombol ada, prosedur ada, override secara legal dimungkinkan. Ini adalah jenis kontrol yang paling mudah diklaim oleh pembuat sistem: "pengguna selalu bisa mengambil alih."

**Kontrol bermakna** adalah kontrol yang bisa digunakan secara efektif oleh manusia yang memiliki kapasitas kognitif, informasi, dan waktu yang realistis dalam kondisi penggunaan yang sesungguhnya — termasuk kondisi tekanan, kelelahan, dan ketidakpastian.

Kasus 737 MAX adalah bukti terkuat bahwa menyediakan kontrol nominal tanpa kontrol bermakna bukan hanya tidak berguna — ia bisa lebih berbahaya dari tidak menyediakan kontrol sama sekali, karena menciptakan ilusi keamanan.

### Tiga tingkatan keterlibatan manusia

Penelitian dalam otomasi dan HCAI mengidentifikasi tiga tingkatan keterlibatan manusia yang berbeda secara fundamental:

**Tingkat 1 — Manusia dalam loop (human-in-the-loop):**
Manusia secara aktif terlibat dalam setiap keputusan. AI menganalisis dan merekomendasikan, manusia yang memutuskan. Tidak ada keputusan yang diambil tanpa persetujuan eksplisit manusia.

*Kapan dibutuhkan:* Keputusan ireversibel berisiko tinggi — diagnosis medis yang mengarah pada tindakan, keputusan hukum, intervensi militer. Taruhannya terlalu tinggi untuk mendelegasikan ke sistem otonom.

**Tingkat 2 — Manusia di atas loop (human-on-the-loop):**
Sistem beroperasi secara otonom tapi manusia memantau dan bisa mengintervensi. Manusia tidak terlibat di setiap keputusan, tapi ada mekanisme untuk menghentikan atau mengoreksi sistem.

*Kapan sesuai:* Sistem dengan kecepatan tinggi yang tidak memungkinkan review per keputusan, tapi dengan risiko yang terkelola — moderasi konten, deteksi fraud real-time dengan eskalasi manual untuk kasus ambiguous.

**Tingkat 3 — Manusia di luar loop (human-out-of-the-loop):**
Sistem beroperasi sepenuhnya otonom. Manusia menetapkan parameter di awal dan memeriksa output secara berkala, tapi tidak terlibat dalam keputusan operasional.

*Kapan bisa diterima:* Hanya untuk domain dengan keandalan yang sangat tinggi dan konsekuensi kegagalan yang sangat rendah atau reversibel — rekomendasi musik, navigasi rute alternatif, filter spam.

### Ironies of Automation: mengapa kontrol gagal saat paling dibutuhkan

Lisanne Bainbridge, dalam makalah klasiknya *"Ironies of Automation"* (1983), mengidentifikasi paradoks yang relevan hingga hari ini: **semakin canggih sistem otomasi, semakin lemah kemampuan manusia untuk mengambil alih kendali ketika sistem itu gagal.**

Alasannya: sistem otomasi yang canggih menangani semua situasi normal dengan sangat baik sehingga manusia jarang perlu mengintervensi. Akibatnya, keterampilan manusia untuk intervensi manual menurun karena kurang berlatih. Ketika situasi abnormal terjadi — tepat saat kontrol manusia paling dibutuhkan — keterampilan itu sudah melemah.

Ini bukan ironi yang bisa diselesaikan dengan lebih banyak pelatihan saja. Ini adalah tantangan desain fundamental: **sistem yang ingin memberikan kontrol bermakna harus secara aktif menjaga keterampilan manusia untuk menggunakan kontrol itu** — melalui latihan berkala, simulasi, dan antarmuka yang membuat intervensi terasa natural, bukan darurat.

<!-- DIAGRAM: Tiga tingkatan keterlibatan manusia
     Render sebagai diagram horizontal saat membangun UI.
     Tiga kotak berurutan dari kiri ke kanan:
     1. "Human-in-the-loop" — manusia di setiap keputusan (hijau, high control)
     2. "Human-on-the-loop" — manusia memantau + bisa intervensi (kuning, medium)
     3. "Human-out-of-the-loop" — sistem otonom penuh (oranye, low control)
     Sumbu di bawah: "Tingkat otomasi" (rendah ke tinggi)
     Sumbu di atas: "Kontrol manusia" (tinggi ke rendah)
     Tambahkan contoh: diagnosis medis (in-loop), moderasi konten (on-loop), filter spam (out-of-loop)
-->

---

> **Quick Check** — Sebelum melanjutkan:
> *Dari tiga tingkatan keterlibatan manusia — in-the-loop, on-the-loop, out-of-the-loop — di tingkatan mana sebaiknya sistem AI untuk keputusan kredit perbankan? Dan untuk rekomendasi rute GPS? Apa yang membedakan keduanya secara mendasar?*

---

## Analisis Kasus

Kembali ke 737 MAX dengan kerangka kontrol bermakna dan Ironies of Automation:

**Mengapa kontrol nominal gagal:** MCAS bisa dinonaktifkan, tapi prosedurnya tidak ada dalam pelatihan standar pilot, tidak ada dalam checklist darurat yang mudah diakses, dan tidak pernah disimulasikan dalam kondisi yang menyerupai apa yang terjadi di kedua penerbangan itu. Kontrol ada di manual; tidak ada dalam memori otot dan refleks pilot.

**Ironies of Automation bekerja:** 737 MAX memiliki sistem otomasi yang sangat canggih yang menangani semua penerbangan normal dengan sempurna. Pilot yang memiliki jam terbang di pesawat ini tidak pernah perlu mengintervensi MCAS secara manual. Ketika sensor rusak dan MCAS mulai berperilaku abnormal, pilot menghadapi situasi yang tidak pernah mereka latih dengan peralatan yang tidak pernah mereka gunakan dalam kondisi nyata.

**Apa yang seharusnya berbeda:** Kontrol bermakna untuk MCAS membutuhkan: (1) dokumentasi penuh dalam materi pelatihan, (2) simulasi berkala dari skenario kegagalan, (3) antarmuka kokpit yang memberikan indikasi jelas bahwa MCAS sedang aktif dan sedang beroperasi berdasarkan input sensor tunggal, dan (4) desain sistem yang memberikan informasi cukup untuk pilot mendiagnosis masalah dalam kondisi tekanan tinggi.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Untuk setiap fitur AI yang membuat keputusan penting, tanyakan: *"Dalam kondisi penggunaan yang paling buruk — pengguna yang kelelahan, terburu-buru, atau tertekan — apakah override masih bisa digunakan secara efektif?"* Jika tidak, kontrol yang kamu sediakan adalah kontrol nominal.

**Jika kamu UX researcher atau designer:**
Rancang skenario pengujian yang mensimulasikan kondisi nyata penggunaan, termasuk kondisi stres dan tekanan waktu. Override yang bekerja baik dalam kondisi tenang di lab sering gagal dalam kondisi lapangan yang sesungguhnya. Uji kontrol dalam kondisi yang paling menantang, bukan yang paling mudah.

**Jika kamu developer atau engineer:**
Bangun logging untuk seberapa sering pengguna menggunakan mekanisme override atau intervensi. Frekuensi yang sangat rendah bisa berarti dua hal yang berlawanan: sistem berjalan sangat baik (tidak perlu intervensi) atau kontrol terlalu sulit digunakan sehingga pengguna menyerah. Bedakan keduanya dengan riset pengguna, bukan hanya dengan data.

---

## Pertanyaan Refleksi

> Bainbridge menulis "Ironies of Automation" pada 1983 — jauh sebelum era AI modern. Tapi paradoksnya semakin relevan: semakin canggih sistem AI yang kita bangun, semakin jarang manusia perlu mengintervensi, dan semakin lemah kemampuan mereka untuk mengintervensi ketika benar-benar perlu.
>
> **Bagaimana kamu akan merancang sistem AI di domainmu** — baik itu produk kesehatan, keuangan, atau layanan publik — agar kontrol manusia tetap bermakna, bukan hanya nominal? Mekanisme konkret apa yang akan kamu masukkan?

---

## Ringkasan Lesson

- Kontrol nominal (tersedia secara teknis) tidak sama dengan kontrol bermakna (bisa digunakan secara efektif dalam kondisi nyata). Perbedaan ini bisa menentukan hidup dan mati.
- Tiga tingkatan keterlibatan manusia — in-the-loop, on-the-loop, out-of-the-loop — harus dipilih berdasarkan taruhan keputusan dan konsekuensi kegagalan, bukan berdasarkan efisiensi teknis semata.
- Ironies of Automation (Bainbridge, 1983) menunjukkan bahwa semakin canggih otomasi, semakin lemah kemampuan manusia untuk mengambil alih — dan ini harus diatasi secara aktif melalui desain, bukan hanya pelatihan.
- Kasus 737 MAX adalah pengingat paling kuat bahwa kontrol nominal tanpa kontrol bermakna bisa lebih berbahaya dari tidak menyediakan kontrol sama sekali.
- Lesson berikutnya akan membahas prinsip keempat: Accountability — siapa yang bertanggung jawab ketika AI membuat keputusan yang salah dan tidak ada yang mengaku.

---

## Referensi

- Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press. — Bab 8.
- Bainbridge, L. (1983). Ironies of automation. *Automatica*, 19(6), 775–779.
- National Transportation Safety Board (NTSB). (2019). *Safety Recommendation Report: Assumptions Used in the Safety Assessment Process and the Effects of Multiple Alerts and Indications on Pilot Performance*. NTSB/SIR-19/01.
- Joint Authorities Technical Review (JATR). (2019). *JATR — Cyclops Team: Final Report*. Federal Aviation Administration.
- Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics*, 30(3), 286–297.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
