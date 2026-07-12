---
course: hcai-foundations
module: 4
module_title: "Explainability and Fairness in Practice"
lesson: 1
title: "Dari Black Box ke Glass Box: Membuat AI Bisa Dijelaskan Tanpa Rumus"
duration_minutes: 13
bloom_level: analyze
keywords:
  - explainable AI for non-technical
  - XAI analogy
  - AI black box explanation
  - SHAP LIME explained simply
  - AI transparency implementation
is_free: true
status: draft
---

# Dari Black Box ke Glass Box: Membuat AI Bisa Dijelaskan Tanpa Rumus

**Modul 4 · Explainability and Fairness in Practice** · Lesson 1 dari 4
**Estimasi waktu baca:** 13 menit · **Level:** Foundational · **Prasyarat:** M3-L1 s/d M3-L5

---

> **Yang akan kamu capai di lesson ini:**
> - Menganalisis perbedaan antara sistem AI yang "tidak bisa dijelaskan" dan yang "tidak mau dijelaskan"
> - Menguraikan tiga jenis penjelasan AI — global, lokal, dan kontrafaktual — dan kapan masing-masing dibutuhkan
> - Membandingkan pendekatan eksplanabilitas utama menggunakan analogi yang tidak membutuhkan latar belakang matematis

---

## Hook

Pada 2017, rumah sakit-rumah sakit di seluruh dunia mulai menggunakan IBM Watson for Oncology — sistem AI yang diklaim bisa merekomendasikan pengobatan kanker dengan akurasi tinggi, dilatih dari catatan medis ribuan pasien di Memorial Sloan Kettering Cancer Center.

Masalahnya bukan rekomendasinya selalu salah. Masalahnya adalah **tidak ada yang bisa menjelaskan mengapa sistem itu merekomendasikan apa yang direkomendasikannya.**

Onkologis di India, Korea, dan Eropa mulai melaporkan hal yang sama: sistem sering merekomendasikan pengobatan yang bertentangan dengan standar klinis lokal — dan ketika mereka bertanya kepada sistem *mengapa*, tidak ada jawaban yang bisa mereka gunakan untuk membuat keputusan medis yang bertanggung jawab. Mereka harus memilih antara dua opsi yang tidak nyaman: mengikuti rekomendasi sistem yang tidak bisa dipertanggungjawabkan, atau mengabaikannya sepenuhnya.

Pada 2018, MD Anderson Cancer Center secara terbuka mengakhiri proyek senilai $62 juta dengan IBM Watson. Alasannya bukan karena sistemnya terbukti salah — melainkan karena sistem yang tidak bisa menjelaskan dirinya sendiri tidak bisa diintegrasikan secara aman ke dalam proses pengambilan keputusan medis.

Ini adalah kasus paling mahal dan paling jelas dari masalah yang kita sebut **black box problem** — dan ia menunjukkan sesuatu yang fundamental: **kemampuan teknis tanpa kemampuan penjelasan bukan hanya tidak berguna, ia aktif berbahaya.**

---

## Kerangka Konseptual

### Black box bukan takdir teknis — ini pilihan desain

Perbedaan penting yang perlu dipahami sejak awal: sebagian besar sistem AI tidak bisa dijelaskan bukan karena *tidak mungkin* dijelaskan, melainkan karena eksplanabilitas tidak pernah menjadi requirements dalam proses pembuatannya.

Ini adalah perbedaan antara sistem yang **tidak bisa** dijelaskan (kompleksitas matematis yang memang sulit dipahami secara intuitif) dan sistem yang **tidak mau** dijelaskan (tidak ada investasi dalam mekanisme penjelasan).

Watson for Oncology masuk kategori kedua. Sistemnya dibangun untuk akurasi — dan akurasi adalah satu-satunya kriteria sukses yang ditetapkan. Eksplanabilitas tidak pernah masuk dalam desain.

Pelajaran dari M3-L1 (Transparency) relevan di sini: transparansi adalah kebutuhan fungsional, bukan pilihan etis. Eksplanabilitas adalah implementasi teknisnya.

### Spektrum dari black box ke glass box

<!-- DIAGRAM: Spektrum Eksplanabilitas AI
     Render sebagai skala horizontal saat membangun UI.
     Kiri: Black Box — tidak ada penjelasan, tidak ada akses ke logika internal
     Tengah: Grey Box — penjelasan sebagian, beberapa faktor terlihat
     Kanan: Glass Box — penjelasan penuh, logika dapat diaudit
     Contoh posisi:
     - Deep neural network tanpa XAI → Black Box
     - Neural network + SHAP/LIME → Grey Box
     - Decision tree sederhana → Glass Box
     - Linear regression → Glass Box
     Catatan di bawah: "Glass box bukan selalu yang terbaik — trade-off dengan akurasi"
-->

Tidak ada sistem AI yang sepenuhnya transparan secara teknis. Yang bisa kita lakukan adalah bergerak di sepanjang spektrum ini dengan sadar — memilih posisi yang sesuai dengan taruhan keputusan, bukan membiarkan posisi ditentukan oleh kenyamanan teknis.

### Tiga jenis penjelasan AI

Ini adalah kerangka yang paling praktis untuk memahami eksplanabilitas:

**Jenis 1 — Penjelasan global:** *"Bagaimana model ini bekerja secara umum?"*

Penjelasan global mendeskripsikan perilaku model secara keseluruhan — faktor apa yang secara umum paling mempengaruhi prediksi. Ini berguna untuk memahami apakah model belajar dari hal yang seharusnya.

Analogi: membaca silabus kursus — kamu tahu topik besar apa yang diajarkan, tapi tidak tahu bagaimana setiap mahasiswa spesifik dinilai.

**Jenis 2 — Penjelasan lokal:** *"Mengapa model membuat keputusan ini untuk kasus ini?"*

Penjelasan lokal mendeskripsikan mengapa sebuah prediksi spesifik dibuat untuk input spesifik. Ini yang paling dibutuhkan oleh pengguna yang terdampak keputusan.

Analogi: menerima laporan nilai dengan komentar guru — kamu tahu bukan hanya nilai akhirnya tapi faktor apa yang berkontribusi pada nilai itu.

**Jenis 3 — Penjelasan kontrafaktual:** *"Apa yang perlu berubah agar keputusan berubah?"*

Penjelasan kontrafaktual menjawab pertanyaan "jika... maka..." — kondisi apa yang perlu dipenuhi agar sistem menghasilkan keputusan yang berbeda. Ini sangat berharga untuk pengguna yang ingin tahu *apa yang bisa mereka lakukan*.

Analogi: *"Pengajuan pinjaman Anda ditolak karena rasio utang-penghasilan di atas 40%. Jika rasio tersebut turun di bawah 35%, pengajuan kemungkinan besar akan disetujui."*

### SHAP dan LIME tanpa matematika

Dua teknik eksplanabilitas yang paling banyak digunakan — SHAP (*SHapley Additive exPlanations*) dan LIME (*Local Interpretable Model-agnostic Explanations*) — sering terdengar teknis dan mengintimidasi. Tapi konsepnya intuitif.

**SHAP — analogi pembagian tagihan yang adil:**
Bayangkan sebuah tim yang bersama-sama memenangkan sebuah kompetisi. SHAP menjawab pertanyaan: seberapa besar kontribusi masing-masing anggota tim terhadap kemenangan itu? Ia mengkalkulasi "nilai Shapley" — kontribusi bersih setiap fitur terhadap prediksi — dengan cara yang matematis adil: setiap fitur dinilai berdasarkan kontribusinya di semua kemungkinan kombinasi dengan fitur lain.

Hasilnya: untuk sebuah keputusan pinjaman, SHAP bisa mengatakan "riwayat kredit berkontribusi +40% pada keputusan, status pekerjaan +25%, lokasi -15%, dan usia tidak signifikan."

**LIME — analogi peta lokal:**
Peta dunia tidak akurat untuk navigasi di kota — terlalu general. Tapi peta jalan kota sangat akurat untuk area itu. LIME bekerja dengan cara yang sama: untuk setiap prediksi spesifik, LIME membangun model yang sederhana dan bisa dijelaskan yang akurat *di sekitar titik itu* — meski model simpel itu tidak akurat untuk kasus lain yang jauh berbeda.

---

> **Quick Check** — Sebelum melanjutkan:
> *Dari tiga jenis penjelasan — global, lokal, kontrafaktual — mana yang paling berguna untuk seorang pasien yang ingin memahami rekomendasi medis AI? Mana yang paling berguna untuk regulator yang mengawasi sistem itu? Apakah jawabannya berbeda — dan mengapa?*

---

## Analisis Kasus

Kembali ke Watson for Oncology. Dengan kerangka tiga jenis penjelasan, kita bisa menganalisis tepat di mana sistemnya gagal:

**Penjelasan global:** Ada — IBM memiliki dokumentasi tentang cara sistem dilatih. Tapi ini hanya berguna untuk peneliti dan insinyur, bukan untuk onkologis yang menghadapi pasien.

**Penjelasan lokal:** Tidak ada yang bermakna. Sistem tidak bisa mengatakan "untuk pasien dengan profil ini, rekomendasi pengobatan X didasarkan pada faktor A, B, dan C dari rekam medisnya." Onkologis mendapat rekomendasi tanpa jejak alasan yang bisa diperiksa.

**Penjelasan kontrafaktual:** Tidak ada sama sekali. Tidak ada cara untuk mengetahui "jika kondisi pasien berbeda dalam hal apa, rekomendasinya akan berubah?"

Tanpa penjelasan lokal dan kontrafaktual, sistem tidak bisa diintegrasikan ke dalam praktik klinis yang bertanggung jawab — bukan karena dokternya tidak mau menggunakan AI, melainkan karena standar medis mensyaratkan bahwa setiap keputusan bisa dipertanggungjawabkan kepada pasien.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Saat mendefinisikan requirements untuk fitur AI, tambahkan satu baris eksplisit: *"Pengguna harus bisa mendapat penjelasan [global/lokal/kontrafaktual] tentang keputusan sistem."* Jenis penjelasan yang dibutuhkan ditentukan oleh siapa penggunanya dan apa yang mereka lakukan dengan keputusan itu — bukan oleh apa yang paling mudah diimplementasikan.

**Jika kamu UX researcher atau designer:**
Rancang "explanation interfaces" sebagai fitur utama, bukan tambahan. Pertanyaan riset yang perlu dijawab sebelum merancang: *Dalam bahasa apa pengguna memahami keputusan ini? Apa yang mereka lakukan setelah mendapat penjelasan?* Penjelasan yang tidak mengubah perilaku pengguna adalah penjelasan yang tidak berguna.

**Jika kamu developer atau engineer:**
SHAP dan LIME tersedia sebagai library open-source yang bisa ditambahkan ke pipeline model yang sudah ada tanpa mengubah model itu sendiri. Eksplanabilitas tidak selalu membutuhkan membangun ulang sistem — seringkali ia bisa ditambahkan sebagai lapisan di atas. Pertanyaannya adalah: kapan dalam pipeline pengembangan kamu merencanakan untuk menambahkannya?

---

## Pertanyaan Refleksi

> Watson for Oncology menghabiskan $62 juta sebelum akhirnya ditinggalkan — sebagian besar karena masalah eksplanabilitas yang tidak pernah menjadi prioritas desain.
>
> **Pikirkan satu produk AI yang kamu kenal.** Jenis penjelasan mana yang saat ini tersedia, dan jenis mana yang tidak ada? Jika kamu harus menambahkan satu jenis penjelasan hari ini dengan sumber daya terbatas, mana yang akan memberikan dampak terbesar pada kepercayaan dan keamanan pengguna?

---

## Ringkasan Lesson

- Black box bukan takdir teknis — ini adalah konsekuensi dari tidak memasukkan eksplanabilitas sebagai requirements sejak awal.
- Tiga jenis penjelasan: global (bagaimana model bekerja umumnya), lokal (mengapa keputusan ini dibuat), dan kontrafaktual (apa yang perlu berubah agar keputusan berubah). Ketiganya menjawab pertanyaan berbeda untuk audiens berbeda.
- SHAP dan LIME adalah teknik eksplanabilitas yang bisa dipahami secara intuitif: SHAP menghitung kontribusi adil setiap faktor; LIME membangun model sederhana yang akurat di sekitar satu prediksi spesifik.
- Kasus Watson for Oncology menunjukkan konsekuensi bisnis dan klinis dari sistem yang kuat secara teknis tapi tidak bisa menjelaskan dirinya sendiri.
- Lesson berikutnya akan membahas siapa yang butuh penjelasan apa — karena penjelasan yang tepat untuk satu audiens bisa tidak berguna atau bahkan menyesatkan untuk audiens lain.

---

## Referensi

- Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press. — Bab 10.
- Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems*, 30.
- Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why should I trust you?": Explaining the predictions of any classifier. *KDD 2016 Proceedings*, 1135–1144.
- Ross, C., & Swetlitz, I. (2017). IBM pitched its Watson supercomputer as a revolution in cancer care. It's been a bust. *STAT News*, 5 September 2017.
- Doshi-Velez, F., & Kim, B. (2017). Towards a rigorous science of interpretable machine learning. *arXiv preprint* arXiv:1702.08608.

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
