---
course: hcai-foundations
module: 3
module_title: "The Four Principles — What HCAI Demands"
lesson: 2
title: "Fairness: Ketika AI Harus Adil untuk Semua — dan Mengapa Itu Lebih Rumit dari yang Terlihat"
duration_minutes: 12
bloom_level: understand
keywords:
  - AI fairness principle
  - equitable AI design
  - algorithmic fairness definition
  - AI bias fairness tradeoff
  - demographic parity AI
is_free: true
status: draft
---

# Fairness: Ketika AI Harus Adil untuk Semua — dan Mengapa Itu Lebih Rumit dari yang Terlihat

**Modul 3 · The Four Principles — What HCAI Demands** · Lesson 2 dari 5
**Estimasi waktu baca:** 12 menit · **Level:** Foundational · **Prasyarat:** M3-L1

---

> **Yang akan kamu capai di lesson ini:**
> - Menjelaskan mengapa "netral secara algoritmik" tidak sama dengan "adil"
> - Mengidentifikasi tiga definisi fairness yang berbeda dan mengapa memilih satu berarti mengorbankan yang lain
> - Menginterpretasi implikasi pilihan definisi fairness pada kelompok yang berbeda dalam populasi yang dilayani sistem

---

## Hook

Agustus 2020. Ratusan ribu siswa di Inggris menunggu hasil ujian A-level — ujian yang menentukan universitas mana yang bisa mereka masuki. Karena pandemi COVID-19, ujian fisik dibatalkan. Sebagai pengganti, pemerintah Inggris menggunakan algoritma untuk menentukan nilai berdasarkan performa historis sekolah masing-masing siswa.

Sistemnya secara teknis "adil" dalam satu pengertian: semua siswa diperlakukan dengan aturan yang sama. Algoritma yang sama diterapkan pada semua orang.

Tapi hasilnya jauh dari adil.

Siswa di sekolah-sekolah yang secara historis berprestasi rendah — yang mayoritas berlokasi di daerah berpenghasilan rendah — mendapat nilai yang diturunkan secara masif dari prediksi guru mereka. Sementara siswa di sekolah-sekolah elite mendapat nilai yang lebih tinggi atau tetap sama. Seorang siswa yang secara konsisten mendapat nilai A dalam simulasi mendapat nilai C hanya karena sekolahnya secara historis menghasilkan banyak nilai C.

Dalam tiga hari, lebih dari 39% nilai A-level diturunkan. Ribuan siswa kehilangan tawaran universitas yang sudah mereka terima. Ribuan lagi yang berasal dari keluarga kurang mampu mengalami mobilitas sosial yang terputus dalam sekejap.

Protes massal memaksa pemerintah membatalkan hasilnya dalam sepuluh hari. Tapi kerusakan sudah terjadi — dan pertanyaannya tetap relevan: **bagaimana sistem yang menggunakan aturan yang sama untuk semua orang bisa menghasilkan hasil yang sangat tidak adil?**

---

## Kerangka Konseptual

### Netral ≠ adil: mengapa perlakuan yang sama bisa menghasilkan hasil yang tidak setara

Intuisi umum tentang fairness adalah *perlakuan yang sama* — aturan yang sama untuk semua orang. Algoritma A-level Inggris memenuhi standar ini: formula yang identik diterapkan pada setiap siswa.

Tapi fairness dalam AI mengharuskan kita membedakan antara dua konsep yang sering dikacaukan:

**Kesetaraan perlakuan (equal treatment)** — semua orang diperlakukan dengan aturan yang sama, tanpa memandang latar belakang.

**Kesetaraan hasil (equitable outcomes)** — hasilnya proporsional dan tidak merugikan kelompok tertentu secara tidak proporsional, meski aturannya mungkin berbeda untuk mengakomodasi perbedaan konteks.

Sistem A-level memiliki equal treatment tapi tidak equitable outcomes. Mengapa? Karena "performa historis sekolah" sebagai variabel membawa serta semua ketidaksetaraan struktural yang sudah ada sebelumnya — pendanaan sekolah, komposisi demografis, akses sumber daya. Algoritma tidak menciptakan ketidakadilan itu; ia mewariskannya dan mengokohkannya.

Ini adalah pola yang berulang dalam kasus-kasus bias AI: **sistem yang secara teknis "netral" menjadi pembawa dan penguat ketidaksetaraan historis jika data pelatihannya mencerminkan dunia yang tidak adil.**

### Tiga definisi fairness — dan mengapa kamu harus memilih

Ini adalah salah satu temuan paling penting dalam penelitian fairness AI: secara matematis terbukti bahwa tidak mungkin memaksimalkan semua definisi fairness secara bersamaan ketika distribusi kelompok dalam data berbeda (Chouldechova, 2017; Kleinberg et al., 2016).

Kamu harus memilih. Dan pilihan itu bukan pilihan teknis — ini adalah pilihan nilai.

**Definisi 1 — Paritas demografis (demographic parity):**
Sistem dianggap fair jika proporsi keputusan positif sama di semua kelompok. Jika 30% pelamar dari kelompok A diterima, maka 30% pelamar dari kelompok B juga harus diterima.

*Kapan cocok:* Ketika tujuannya adalah representasi proporsional — rekrutmen, penerimaan universitas, akses layanan.
*Kelemahan:* Mengabaikan perbedaan distribusi yang mungkin relevan dan sah.

**Definisi 2 — Kesempatan yang setara (equal opportunity):**
Di antara mereka yang seharusnya mendapat keputusan positif, proporsi yang benar-benar mendapatkannya harus sama di semua kelompok. Fokus pada kesalahan yang merugikan — yang seharusnya diterima tapi ditolak.

*Kapan cocok:* Ketika yang paling berbahaya adalah menolak orang yang seharusnya diterima — misalnya dalam diagnosis medis atau penilaian kredit.
*Kelemahan:* Tidak mengontrol proporsi false positive di kelompok berbeda.

**Definisi 3 — Konsistensi prediksi (calibration):**
Jika sistem memprediksi probabilitas 70% untuk suatu hasil, maka 70% dari kasus dengan prediksi itu harus benar-benar mengalami hasil itu — konsisten di semua kelompok. Ini adalah properti akurasi prediksi, bukan definisi fairness dalam arti representasi, tapi ia sering digunakan sebagai standar karena dapat diukur secara objektif.

*Kapan relevan:* Ketika akurasi prediksi yang konsisten adalah prioritas utama — misalnya dalam sistem rekomendasi medis atau penilaian risiko.
*Keterbatasan:* Bisa menghasilkan representasi yang tidak setara jika distribusi baseline berbeda antar kelompok.

<!-- DIAGRAM: Trade-off Tiga Pendekatan Fairness
     Render sebagai tabel perbandingan 3 kolom saat membangun UI.
     Kolom 1 — Paritas demografis: Fokus pada representasi proporsional antar kelompok
     Kolom 2 — Kesempatan setara: Fokus pada mengurangi false negative yang merugikan
     Kolom 3 — Konsistensi prediksi: Fokus pada akurasi yang merata antar kelompok
     Baris tambahan: "Kapan cocok" + "Kelemahannya"
     Footer: "Secara matematis tidak mungkin memaksimalkan ketiganya sekaligus (Chouldechova, 2017)"
     Warna: tiap kolom ramp berbeda untuk membedakan — teal, amber, purple
-->

### Fairness sebagai pilihan nilai, bukan kalkulasi teknis

Yang penting dipahami: memilih pendekatan fairness bukanlah keputusan yang bisa diserahkan sepenuhnya kepada tim teknis. Ini adalah keputusan yang melibatkan nilai-nilai masyarakat, konteks penggunaan, dan konsekuensi pada kelompok yang berbeda.

Ingat dari M2-L1 bahwa mental model pengguna tentang keadilan sering terbangun dari pengalaman pertama mereka dengan sistem. Pilihan pendekatan fairness ini berdampak jauh melampaui angka statistik — ia membentuk gambaran yang pengguna bangun tentang apakah sistem ini "untuk mereka" atau tidak.

Pertanyaan yang perlu dijawab sebelum memilih: *Kesalahan mana yang lebih merugikan — menolak yang seharusnya diterima, atau menerima yang seharusnya ditolak? Untuk kelompok mana konsekuensinya paling berat?*

Jawaban atas pertanyaan ini harus melibatkan kelompok yang paling terdampak — bukan hanya tim pengembang.

---

> **Quick Check** — Sebelum melanjutkan:
> *Bayangkan kamu sedang membangun sistem AI untuk seleksi beasiswa. Dari tiga definisi fairness di atas — paritas demografis, kesempatan yang setara, atau kalibrasi — mana yang akan kamu prioritaskan? Apa yang menentukan pilihanmu?*

---

## Analisis Kasus

Kembali ke kasus A-level. Dari sudut pandang tiga definisi fairness:

**Paritas demografis:** Gagal. Proporsi nilai yang diturunkan secara masif berbeda antara sekolah swasta dan negeri, yang berkorelasi kuat dengan latar belakang sosial ekonomi siswa.

**Kesempatan yang setara:** Gagal. Di antara siswa yang seharusnya mendapat nilai tinggi (berdasarkan prediksi guru yang mengenal mereka), proporsi yang benar-benar mendapatkan nilai tinggi jauh lebih rendah di sekolah-sekolah dengan riwayat performa rendah.

**Kalibrasi:** Secara teknis mungkin terpenuhi di level statistik agregat — tapi ini justru menunjukkan bahwa kalibrasi saja tidak cukup sebagai standar fairness ketika konteksnya adalah keputusan yang mengubah hidup individu.

Yang paling instruktif dari kasus ini adalah **apa yang tidak dipertanyakan oleh tim yang membangun sistem**: apakah "performa historis sekolah" adalah variabel yang sah untuk digunakan dalam menilai kemampuan individu? Mereka tidak mempertanyakannya karena secara teknis variabel itu prediktif — dan itulah batas dari perspektif teknis semata.

---

## Implikasi Praktis

**Jika kamu product manager atau startup founder:**
Sebelum meluncurkan fitur AI yang membuat keputusan tentang pengguna, tanyakan: *"Apakah kita sudah mendefinisikan secara eksplisit fairness apa yang kita kejar — dan apakah kelompok yang paling terdampak sudah dilibatkan dalam definisi itu?"* Mendefinisikan fairness setelah sistem berjalan jauh lebih mahal dari mendefinisikannya di awal.

**Jika kamu UX researcher atau designer:**
Sertakan kelompok yang paling rentan terdampak dalam riset pengguna sejak awal — bukan sebagai afterthought. Mereka yang paling mungkin dirugikan oleh sistem adalah sumber wawasan terpenting untuk mendefinisikan fairness yang relevan.

**Jika kamu developer atau engineer:**
Disagregasi metrik performa model berdasarkan kelompok — bukan hanya akurasi agregat. Sistem dengan akurasi 94% mungkin memiliki akurasi 98% untuk satu kelompok dan 87% untuk kelompok lain. Angka agregat menyembunyikan ketidaksetaraan ini sampai terlambat.

---

## Pertanyaan Refleksi

> Kasus A-level menunjukkan bagaimana data historis yang tidak adil menghasilkan keputusan yang tidak adil — bahkan ketika algoritmanya sendiri "netral."
>
> **Pikirkan satu produk AI yang menggunakan data historis untuk membuat keputusan tentang orang.** Apakah data historis itu mencerminkan dunia yang sudah adil — atau ia mewarisi dan mengokohkan ketidaksetaraan yang sudah ada? Definisi fairness mana yang paling relevan untuk konteks itu?

---

## Ringkasan Lesson

- "Netral secara algoritmik" tidak berarti adil — sistem yang menggunakan aturan sama untuk semua orang bisa menghasilkan hasil yang tidak setara jika data dan konteks yang mendasarinya sudah tidak setara.
- Ada tiga definisi fairness yang berbeda — paritas demografis, kesempatan yang setara, dan kalibrasi — dan secara matematis tidak mungkin memaksimalkan ketiganya sekaligus.
- Memilih definisi fairness adalah keputusan nilai, bukan kalkulasi teknis. Kelompok yang paling terdampak harus dilibatkan dalam keputusan ini.
- Kasus A-level menunjukkan konsekuensi nyata ketika pertanyaan tentang fairness tidak diajukan sampai sistem sudah beroperasi dan kerusakan sudah terjadi.
- Lesson berikutnya akan membahas prinsip ketiga: Human Control — dan mengapa kontrol yang *ada secara teknis* tidak sama dengan kontrol yang *bisa digunakan secara nyata*.

---

## Referensi

- Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press. — Bab 7.
- Chouldechova, A. (2017). Fair prediction with disparate impact. *Big Data*, 5(2), 153–163.
- Kleinberg, J., Mullainathan, S., & Raghavan, M. (2016). Inherent trade-offs in the fair determination of risk scores. *arXiv preprint* arXiv:1609.05807.
- Hardt, M., Price, E., & Srebro, N. (2016). Equality of opportunity in supervised learning. *Advances in Neural Information Processing Systems*, 29.
- BBC News. (2020, August 26). A-levels and GCSEs: How did the exam algorithm work? *BBC News*. bbc.com/news/explainers-53807730

---

*Lesson ini adalah bagian dari kursus **Human-Centered AI — Foundations** oleh CodeinteX. Konten dilisensikan untuk penggunaan pribadi dan pendidikan.*
