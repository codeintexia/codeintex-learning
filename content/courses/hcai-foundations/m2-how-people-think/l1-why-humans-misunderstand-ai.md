---
course: hcai-foundations
module: 2
module_title: "How People Think About and Trust AI"
lesson: 1
title: "Mengapa Manusia Salah Paham tentang AI — dan Kenapa Itu Bukan Kesalahan Mereka"
duration_minutes: 12
bloom_level: understand
keywords:
  - mental models AI users
  - user perception artificial intelligence
  - AI misconceptions
  - anthropomorphism AI
  - why users misunderstand AI
is_free: true
status: draft
---

# Mengapa Manusia Salah Paham tentang AI — dan Kenapa Itu Bukan Kesalahan Mereka

**Modul 2 · How People Think About and Trust AI** · Lesson 1 dari 4
**Estimasi waktu baca:** 12 menit · **Level:** Foundational · **Prasyarat:** M1-L1 s/d M1-L4

---

> **Yang akan kamu capai di lesson ini:**
> - Menjelaskan mengapa kesalahpahaman tentang AI adalah respons kognitif yang wajar, bukan tanda ketidaktahuan
> - Mengidentifikasi tiga mekanisme psikologis yang menyebabkan manusia salah memahami sistem AI
> - Menginterpretasi implikasi kesalahpahaman ini untuk desain produk dan komunikasi AI

---

## Hook

Pada 2015, sebuah rumah sakit di Amerika Serikat mulai menggunakan sistem AI untuk membantu dokter menentukan dosis obat pengencer darah — warfarin — yang sangat sensitif terhadap berat badan, usia, dan kondisi genetik pasien. Sistemnya tervalidasi secara klinis. Rekomendasinya lebih akurat dari kalkulasi manual rata-rata.

Tapi ada sesuatu yang tidak diperhitungkan oleh tim implementasi: para perawat yang menggunakan sistem itu percaya bahwa AI "sudah mempertimbangkan semua faktor yang relevan." Ketika sistem merekomendasikan dosis, mereka cenderung tidak lagi memeriksa silang dengan kondisi pasien secara individual — karena mereka mengasumsikan komputer sudah melakukannya.

Komputer tidak melakukannya. Sistem itu hanya memproses variabel yang dimasukkan ke dalamnya. Jika seorang pasien baru mengonsumsi suplemen yang berinteraksi dengan warfarin tapi tidak tercatat di sistem, AI tidak tahu. AI tidak bisa tahu.

Kepercayaan para perawat bukan kelalaian profesional. Mereka adalah tenaga medis terlatih yang bekerja keras. Yang terjadi adalah sesuatu yang jauh lebih fundamental: **mereka memiliki gambaran yang salah tentang apa yang sistem AI itu sebenarnya bisa dan tidak bisa lakukan** — dan tidak ada yang secara sengaja membentuk gambaran yang benar.

Inilah yang terjadi ketika pengguna memiliki gambaran yang keliru tentang kemampuan dan batas sistem AI — sebuah gap yang menjadi salah satu sumber risiko terbesar dalam penerapan AI, sering diabaikan karena tidak terlihat di dashboard monitoring manapun. Kita akan mempelajari konsep ini lebih dalam, lengkap dengan namanya, di lesson berikutnya.

---

## Kerangka Konseptual

### Otak manusia bukan alat yang dirancang untuk memahami AI

Ini poin yang paling penting di seluruh lesson ini: **kesalahpahaman tentang AI bukan tanda ketidaktahuan atau kecerobohan. Ini adalah output default dari cara otak manusia bekerja.**

Selama ratusan ribu tahun evolusi, otak manusia berkembang untuk memahami dunia melalui tiga mekanisme utama. Dan ketiga mekanisme itulah yang secara konsisten menghasilkan gambaran yang salah tentang sistem AI.

### Mekanisme 1 — Antropomorfisme: kita melihat agen di balik setiap perilaku

Manusia adalah makhluk sosial yang luar biasa mahir mendeteksi agen — entitas yang punya niat, tujuan, dan perasaan. Kemampuan ini begitu kuat sehingga kita mendeteksinya bahkan di tempat yang tidak ada agen sama sekali.

Penelitian Waytz, Morewedge, dan Epley (2010) menunjukkan bahwa manusia secara konsisten mengaitkan niat, emosi, dan kepribadian pada sistem yang tidak memiliki satupun dari itu — mulai dari robot sederhana hingga termostat. Ketika kita berinteraksi dengan AI yang menggunakan bahasa natural, kecenderungan ini menjadi sangat kuat.

Ketika seseorang bertanya kepada chatbot "apakah kamu mengerti masalah saya?" dan chatbot menjawab "tentu saja, saya mengerti" — otak kita memproses ini bukan sebagai output statistik, melainkan sebagai konfirmasi pemahaman yang tulus. Kita tidak bisa tidak melakukannya. Ini bukan pilihan sadar.

**Implikasi desain:** Setiap sistem AI yang menggunakan bahasa first-person ("saya", "kami") atau ekspresi yang menyiratkan pemahaman emosional secara aktif mendorong pengguna ke arah antropomorfisme — dengan semua kesalahpahaman yang menyertainya.

### Mekanisme 2 — Kemudahan kognitif (cognitive ease): kita memilih penjelasan yang paling mudah

Daniel Kahneman (2011) dalam *Thinking, Fast and Slow* mendeskripsikan dua sistem berpikir: Sistem 1 yang cepat, otomatis, dan berbasis pola; dan Sistem 2 yang lambat, analitis, dan butuh usaha. Dalam kehidupan sehari-hari, kita sangat bergantung pada Sistem 1.

Ketika pengguna berinteraksi dengan AI, Sistem 1 tidak mau repot memahami cara kerja statistik, probabilitas, atau batas dataset. Ia mencari penjelasan paling sederhana yang *cukup masuk akal*. Dan penjelasan paling sederhana untuk perilaku AI yang terlihat cerdas adalah: *sistem ini tahu apa yang dilakukannya.*

Ini bukan malas berpikir. Ini adalah efisiensi kognitif yang sangat bermanfaat dalam sebagian besar konteks kehidupan — hanya tidak dalam konteks berinteraksi dengan sistem AI yang bisa gagal dengan cara yang tidak terlihat.

### Mekanisme 3 — Efek black box: kita mengisi kekosongan dengan imajinasi

Ketika kita tidak bisa melihat bagaimana sesuatu bekerja, otak kita tidak diam. Ia mengisi kekosongan itu dengan model yang paling masuk akal berdasarkan pengalaman sebelumnya.

Untuk sistem AI, mayoritas pengguna tidak memiliki pengalaman sebelumnya yang relevan. Mereka mengisi kekosongan dengan dua sumber: fiksi sains (AI yang "sangat cerdas" dari film dan novel), atau analogi yang salah dengan manusia ("seperti bertanya kepada seseorang yang tahu segalanya").

Kedua sumber ini menghasilkan ekspektasi yang hampir selalu terlalu tinggi di domain tertentu (kemampuan "memahami konteks") dan terlalu rendah di domain lain (kecepatan memproses data besar).

---

> **Quick Check** — Sebelum melanjutkan, pastikan kamu bisa menjawab:
> *Dari tiga mekanisme di atas — antropomorfisme, cognitive ease, efek black box — mana yang paling kamu kenali dalam pengalamanmu sendiri menggunakan AI? Tidak perlu jawaban tertulis, cukup pikirkan sejenak.*

---

## Analisis Kasus

Kembali ke kasus perawat di awal. Dengan kerangka tiga mekanisme, kita bisa membaca kasusnya lebih dalam:

**Antropomorfisme** bekerja ketika sistem AI dideskripsikan dengan bahasa yang menyiratkan "pemahaman" — "sistem ini akan *mempertimbangkan* kondisi pasien Anda." Kata *mempertimbangkan* memiliki konotasi agen yang sadar.

**Cognitive ease** bekerja ketika antarmuka sistem sangat mulus dan hasilnya terlihat meyakinkan. Tidak ada friction yang mendorong perawat untuk masuk ke Sistem 2 dan berpikir kritis: "apa batas dari rekomendasi ini?"

**Efek black box** bekerja karena tidak ada yang pernah menjelaskan kepada perawat variabel apa yang digunakan sistem, dan yang lebih penting — variabel apa yang *tidak* digunakan sistem.

Tiga mekanisme, satu antarmuka yang tidak dirancang untuk mengoreksinya, satu risiko medis yang tidak terlihat.

Ini bukan masalah yang bisa diselesaikan dengan pelatihan saja — meskipun pelatihan membantu. Ini adalah masalah desain. Sistem yang tidak secara aktif membangun mental model yang akurat di kepala penggunanya adalah sistem yang aktif membiarkan mental model yang salah terbentuk.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Setiap kali tim kamu memilih kata-kata untuk mendeskripsikan kemampuan produk AI — di landing page, onboarding, UI copy — tanyakan: *"Apakah deskripsi ini mendorong mental model yang akurat atau yang berlebihan?"* Overpromising bukan hanya masalah etika; ini adalah sumber utama churn ketika pengguna menemukan batas sistem yang tidak mereka ekspektasikan.

**Jika kamu UX researcher atau designer:**
Tambahkan satu pertanyaan standar ke semua sesi riset pengguna yang melibatkan AI: *"Menurut kamu, bagaimana sistem ini bekerja di baliknya?"* Jawaban pengguna akan mengungkap mental model mereka — dan celah antara mental model itu dengan realitas adalah brief desain yang paling berharga yang bisa kamu dapatkan.

**Jika kamu developer atau engineer:**
Ketika menulis dokumentasi, notifikasi error, atau pesan sistem untuk fitur AI — hindari bahasa yang menyiratkan otonomi atau pemahaman yang tidak ada. *"Sistem tidak dapat memproses permintaan ini"* lebih akurat dari *"Saya tidak mengerti maksud Anda."* Perbedaan kecil dalam kata-kata membentuk mental model yang sangat berbeda dalam jangka panjang.

---

## Pertanyaan Refleksi

> Pikirkan satu produk AI yang digunakan oleh orang-orang di sekitar kamu — bisa chatbot layanan pelanggan, rekomendasi e-commerce, atau asisten virtual.
>
> **Mental model apa yang kemungkinan besar dimiliki pengguna rata-ratanya tentang sistem itu?** Apakah mereka berpikir sistem "mengerti" mereka? Apakah mereka tahu variabel apa yang digunakan dan tidak digunakan?
>
> Kemudian tanyakan: apakah desain sistem itu — cara ia berbicara, cara ia menampilkan hasil, cara ia menangani kesalahan — secara aktif membangun mental model yang akurat, atau membiarkan mental model yang salah terbentuk sendiri?

---

## Ringkasan Lesson

- Kesalahpahaman tentang AI adalah output default dari cara otak manusia bekerja — bukan tanda ketidaktahuan pengguna.
- Tiga mekanisme utama: antropomorfisme (kita melihat agen di balik perilaku), cognitive ease (kita memilih penjelasan termudah), dan efek black box (kita mengisi kekosongan dengan imajinasi).
- Ketiga mekanisme ini bisa dieksploitasi oleh desain yang buruk, atau dimitigasi oleh desain yang baik.
- Pada lesson berikutnya, kita akan mendalami konsep *mental model* secara lebih terstruktur — dan bagaimana desainer bisa secara sengaja membentuk mental model yang akurat di kepala pengguna.

---

## Referensi

- Waytz, A., Morewedge, C. K., & Epley, N. (2010). Making sense by making sentient: Effectance motivation increases anthropomorphism. *Journal of Personality and Social Psychology*, 99(3), 410–435.
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux. — Bab 1–5.
- Cai, C. J., et al. (2019). Human-centered tools for coping with imperfect algorithms during medical decision-making. *CHI Conference on Human Factors in Computing Systems*.
- Amershi, S., et al. (2019). Software engineering for machine learning: A case study. *2019 IEEE/ACM 41st ICSE*, 291–300.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
