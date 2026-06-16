---
course: hcai-foundations
module: 1
module_title: "What Is Human-Centered AI?"
lesson: 1
title: "Ketika AI Gagal Bukan Karena Bodoh, Tapi Karena Tidak Mengenal Penggunanya"
duration_minutes: 10
bloom_level: remember
keywords:
  - why AI fails users
  - human centered AI definition
  - AI design failures
  - human-centered AI vs AI-centered
is_free: true
status: draft
---

# Ketika AI Gagal Bukan Karena Bodoh, Tapi Karena Tidak Mengenal Penggunanya

**Modul 1 · What Is Human-Centered AI?** · Lesson 1 dari 4
**Estimasi waktu baca:** 10 menit · **Level:** Foundational · **Prasyarat:** Tidak ada

---

> **Yang akan kamu capai di lesson ini:**
> - Mengenali perbedaan antara kegagalan teknis dan kegagalan human-centered pada sistem AI
> - Mengidentifikasi tiga penyebab utama kegagalan AI yang bukan soal kecerdasan model
> - Menyebutkan pertanyaan kunci yang membedakan pendekatan AI-centered dari Human-Centered AI

---

## Hook

Pada 2018, Amazon membongkar sistem AI rekrutmen internal yang telah mereka bangun selama lebih dari empat tahun. Sistemnya dirancang untuk menyaring ribuan lamaran kerja secara otomatis — memilih kandidat terbaik berdasarkan pola dari data historis karyawan Amazon yang sukses.

Secara teknis, sistem itu bekerja persis seperti yang diminta.

Masalahnya: sistem itu secara konsisten memberi nilai lebih rendah pada resume yang mencantumkan kata "perempuan" — baik dalam nama organisasi ("klub catur perempuan"), nama universitas ("perguruan tinggi khusus perempuan"), maupun konteks apapun. Ini bukan bug. Bukan kesalahan kode. Sistem memang belajar dari data yang diberikan — dan selama satu dekade, mayoritas karyawan sukses Amazon adalah laki-laki. Algoritma hanya mempelajari pola yang sudah ada.

Amazon tidak pernah meluncurkan sistem itu ke publik. Tapi pertanyaan yang lebih penting bukan *bagaimana memperbaikinya* — melainkan: **mengapa tidak ada yang bertanya sejak awal, "siapa pengguna sistem ini, dan apa yang terjadi pada mereka ketika sistem ini keliru?"**

---

## Kerangka Konseptual

### AI yang "berhasil secara teknis" bisa sepenuhnya gagal

Dalam pengembangan AI konvensional, keberhasilan diukur dari performa model: akurasi, presisi, recall, F1 score. Angka-angka ini mengukur seberapa baik sistem memprediksi label yang benar pada data uji.

Yang tidak diukur: apakah prediksi itu *bermakna* bagi orang yang terdampak.

Ben Shneiderman, dalam bukunya *Human-Centered AI* (Oxford University Press, 2022), mengajukan pertanyaan yang sederhana tapi jarang ditanyakan oleh tim pengembang AI:

> *"Does the system amplify human performance in ways that users find valuable, while avoiding unacceptable harms?"*

Perhatikan dua bagiannya. Pertama: *users find valuable* — bukan sekedar akurat secara statistik, tapi bernilai menurut penggunanya. Kedua: *avoiding unacceptable harms* — konsekuensi pada manusia, bukan hanya metrik model.

Inilah inti perbedaan antara AI-centered dan Human-Centered AI.

**AI-centered** bertanya: *"Seberapa akurat model kita?"*

**Human-Centered AI** bertanya: *"Apakah sistem ini benar-benar membantu manusia yang menggunakannya — dan apakah ia adil terhadap semua orang yang terdampak olehnya?"*

### Tiga penyebab kegagalan yang bukan soal kecerdasan

Ketika sistem AI gagal melayani penggunanya, hampir selalu karena salah satu dari tiga hal berikut — dan ketiganya bukan soal model yang tidak cukup canggih:

**1. Sistem dioptimalkan untuk tujuan yang salah.**
Amazon melatih sistemnya untuk memprediksi "kandidat yang mirip dengan karyawan sukses kami." Tujuan itu terdengar masuk akal — sampai kamu sadari bahwa "karyawan sukses historis" adalah populasi yang tidak representatif. Tujuan optimasi menentukan perilaku sistem. Kalau tujuannya salah, sistem yang sangat akurat pun akan konsisten menghasilkan keputusan yang salah.

**2. Sistem tidak tahu siapa penggunanya.**
Pulse oximeter — alat medis yang mengukur kadar oksigen darah menggunakan cahaya — selama puluhan tahun dikalibrasi terutama menggunakan data dari individu berkulit terang. Ketika pandemi COVID-19 memaksa penggunaannya secara masif, penelitian di *New England Journal of Medicine* (Sjoding et al., 2020) menemukan bahwa alat ini tiga kali lebih sering salah mendeteksi hipoksemia pada pasien berkulit gelap dibanding berkulit terang. Bukan karena algoritmanya jelek — tapi karena tidak pernah ada yang bertanya: *"Untuk tubuh siapa alat ini dirancang?"*

**3. Konsekuensi kegagalan tidak pernah dipetakan.**
Dalam rekayasa perangkat lunak, ada praktik bernama *failure mode analysis* — mengidentifikasi apa yang terjadi ketika sebuah sistem gagal. Sebagian besar tim AI tidak melakukan ini untuk dimensi manusia. Mereka bertanya "apa yang terjadi kalau model meleset 5%?" tapi tidak bertanya "siapa yang paling dirugikan ketika model meleset, dan seberapa parah dampaknya?"

---

> **Quick Check** — Sebelum melanjutkan:
> *Dari tiga penyebab kegagalan di atas — tujuan optimasi yang salah, tidak mengenal semua pihak yang terdampak, konsekuensi kegagalan tidak dipetakan — mana yang menurutmu paling sering terjadi tapi paling jarang disadari oleh tim yang membangun produk AI?*

---

## Analisis Kasus

Mari kita gunakan kerangka di atas untuk membedah kasus Amazon lebih dalam.

**Apakah tujuan optimasinya tepat?** Tidak. "Mirip dengan karyawan sukses masa lalu" adalah proksi yang cacat untuk "kandidat yang akan sukses di masa depan" — terutama ketika masa lalu itu sendiri sudah bias.

**Apakah mereka tahu siapa penggunanya?** Sebagian. Mereka tahu *pengguna sistem* adalah tim rekrutmen. Tapi mereka tidak memetakan *semua pihak yang terdampak* — termasuk pelamar yang lamarannya dinilai secara tidak adil tanpa sepengetahuan mereka.

**Apakah konsekuensi kegagalan dipetakan?** Tidak secara eksplisit. Tidak ada yang mengajukan pertanyaan: "Kalau sistem ini salah, siapa yang paling dirugikan, dan bagaimana dampaknya terhadap karier mereka?"

Ini bukan kritik terhadap Amazon saja. Pola ini berulang di hampir setiap kasus kegagalan AI besar — dari sistem pengenalan wajah yang lebih sering salah pada wajah perempuan berkulit gelap (Buolamwini & Gebru, 2018), hingga sistem yang digunakan dalam keputusan peradilan pidana yang terbukti bias secara sistemik terhadap kelompok tertentu.

Benang merahnya selalu sama: **sistem yang secara teknis berfungsi, tapi tidak dirancang dengan pemahaman tentang manusia yang akan terdampak olehnya.**

---

## Implikasi Praktis

Apa artinya ini untuk pekerjaanmu sehari-hari?

**Jika kamu product manager atau startup founder:**
Setiap kali kamu mendefinisikan *success metric* untuk fitur AI — conversion rate, click-through rate, prediksi akurat — tanyakan satu pertanyaan tambahan: *"Sukses bagi siapa?"* Metrik bisnismu dan pengalaman penggunamu bisa bergerak ke arah yang berlawanan. Kenali kapan itu terjadi sebelum produk diluncurkan.

**Jika kamu UX researcher atau designer:**
"Memahami pengguna" dalam konteks AI tidak cukup hanya dengan wawancara tentang preferensi. Kamu perlu memetakan *semua pihak yang terdampak* — termasuk mereka yang tidak secara langsung menggunakan antarmuka tapi terkena dampak dari keputusan sistem. Dalam kasus rekrutmen: pelamar adalah pihak yang terdampak, meski mereka bukan "pengguna" sistem dalam arti konvensional.

**Jika kamu developer atau engineer:**
Pertanyaan "apakah model ini cukup akurat?" perlu dilengkapi dengan "akurat untuk siapa, dan tidak akurat untuk siapa?" Disagregasi performa model berdasarkan kelompok pengguna bukan hanya soal etika — ini adalah praktik rekayasa yang baik.

---

## Pertanyaan Refleksi

> Pikirkan satu produk atau layanan berbasis AI yang kamu gunakan atau kerjakan sekarang — bisa aplikasi, fitur, atau sistem internal.
>
> **Apakah kamu tahu siapa *semua* pihak yang terdampak oleh keputusan sistem itu?** Bukan hanya pengguna yang kamu wawancarai atau yang datanya kamu lihat — tapi semua orang yang hidupnya berubah karena apa yang sistem putuskan.
>
> Jika jawabanmu belum jelas, itulah titik mulai yang paling jujur untuk perjalanan di kursus ini.

---

## Ringkasan Lesson

- Kegagalan AI yang paling mahal jarang terjadi karena model yang tidak cukup pintar — melainkan karena tidak ada yang bertanya siapa penggunanya dan apa konsekuensi ketika sistem keliru.
- Tiga penyebab utama: tujuan optimasi yang salah, tidak mengenal semua pihak yang terdampak, dan tidak memetakan konsekuensi kegagalan.
- Human-Centered AI dimulai dari pertanyaan tentang manusia, bukan dari metrik model.
- Pada lesson berikutnya, kita akan menelusuri bagaimana pergeseran paradigma ini terjadi — dan mengapa ia justru menjadi lebih mendesak seiring AI semakin canggih.

---

## Referensi

- Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press.
- Dastin, J. (2018). Amazon scraps secret AI recruiting tool that showed bias against women. *Reuters*, 10 Oktober 2018.
- Sjoding, M. W., et al. (2020). Racial bias in pulse oximetry measurement. *New England Journal of Medicine*, 383(25), 2477–2478.
- Buolamwini, J., & Gebru, T. (2018). Gender shades: Intersectional accuracy disparities in commercial gender classification. *Proceedings of Machine Learning Research*, 81, 1–15.
- Angwin, J., et al. (2016). Machine bias. *ProPublica*, 23 Mei 2016.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
