---
title: Memahami Parameter Evaluasi Solusi AI
course: ai-untuk-proses-data
module: 4
module_title: Merencanakan Perawatan Solusi AI
lesson: 1
slug: l1-parameter-evaluasi
unit_kompetensi:
  - kode: J.62AIN00.016.1
    nama: Merencanakan Perawatan Solusi AI
    elemen: 'Pengetahuan dasar: parameter evaluasi Solusi AI'
level: Foundational — Competency
kategori: Competency
bloom_level: Understand
durasi_menit: 34
durasi_baca_menit: 19
durasi_latihan_menit: 15
bahasa: Indonesia
duration_minutes: 34
keywords: []
is_free: false
status: published
---

## Yang Akan Kamu Capai

Di akhir lesson ini, kamu akan mampu:
- Menjelaskan perbedaan akurasi, presisi, recall, F1-score, dan MAE sebagai parameter evaluasi Solusi AI
- Memilih parameter evaluasi yang tepat sesuai konteks bisnis dan risiko
- Memahami kenapa parameter evaluasi ini menjadi dasar keputusan perawatan Solusi AI di modul ini

**🌉 Dari Modul 3 ke Modul 4:** Hasil monitoring yang kamu siapkan di M3-L5 — data performa SPKO dari waktu ke waktu — sekarang akan jadi bahan mentah untuk mengevaluasi apakah SPKO masih bekerja sesuai harapan, dan jika tidak, menyusun rencana perawatannya.

---

## Hook: Ketika Dua Model "Bagus" Ternyata Bagus untuk Alasan Berbeda

Sebuah penelitian akademik Indonesia yang membandingkan model credit scoring menemukan sesuatu yang penting: dua pendekatan model yang sama-sama terlihat "berhasil" secara keseluruhan ternyata unggul di aspek yang sama sekali berbeda. Satu model (Logistic Regression) menunjukkan performa lebih baik dalam hal akurasi, presisi, dan ROC-AUC — cocok untuk lembaga yang mengutamakan interpretabilitas dan stabilitas model. Model lain (Decision Tree dengan AdaBoost) justru menunjukkan recall yang lebih unggul, menjadikannya lebih efektif dalam **mendeteksi peminjam berisiko tinggi** — cocok untuk lembaga yang fokus pada deteksi risiko di tengah data yang tidak seimbang.

Poin krusialnya: **tidak ada satu jawaban benar tentang "model mana yang lebih bagus"** tanpa tahu dulu apa yang paling penting bagi institusi tersebut. Kalau kamu hanya melihat angka akurasi keseluruhan, kamu bisa saja memilih model yang secara teknis "benar" lebih sering — tapi justru gagal mendeteksi nasabah berisiko tinggi yang paling penting untuk ditangkap.

Ini adalah alasan kenapa Modul 4 dimulai dengan memahami parameter evaluasi secara mendalam — sebelum kamu bisa merencanakan perawatan Solusi AI dengan tepat, kamu harus tahu persis apa yang sedang diukur, dan kenapa satu angka saja (seperti akurasi) tidak pernah cukup untuk bercerita.

---

## Kerangka Konseptual: Lima Parameter Evaluasi Solusi AI

### Confusion Matrix — Fondasi di Balik Semua Parameter

Semua parameter evaluasi berikut dihitung dari **confusion matrix** — tabel yang membandingkan prediksi model dengan kenyataan sebenarnya, dipecah jadi empat kemungkinan: prediksi benar untuk kasus positif (mis. nasabah yang benar diprediksi berisiko), prediksi benar untuk kasus negatif, prediksi salah yang mengira positif padahal negatif (*false positive*), dan prediksi salah yang mengira negatif padahal positif (*false negative*).

### 1. Akurasi (Accuracy)
Persentase prediksi yang benar dari keseluruhan prediksi. Metrik paling umum dan mudah dipahami — tapi **bisa menyesatkan** kalau data tidak seimbang (misalnya, jauh lebih banyak nasabah yang layak kredit dibanding yang berisiko tinggi).

### 2. Presisi (Precision)
Dari semua nasabah yang diprediksi model sebagai "berisiko tinggi", berapa persen yang benar-benar berisiko tinggi? Presisi tinggi penting saat kamu ingin mengurangi *false positive* — misalnya, tidak ingin menolak kredit nasabah yang sebenarnya layak.

### 3. Recall (Sensitivitas)
Dari semua nasabah yang benar-benar berisiko tinggi, berapa persen yang berhasil terdeteksi model? Recall tinggi penting saat *false negative* jauh lebih berbahaya — misalnya, tidak ingin meloloskan kredit ke nasabah yang sebenarnya berisiko gagal bayar.

### 4. F1-Score
Rata-rata harmonik antara presisi dan recall — dipakai saat kamu butuh keseimbangan antara keduanya, terutama pada data yang tidak seimbang (seperti kasus deteksi risiko kredit, di mana nasabah berisiko tinggi biasanya jauh lebih sedikit dibanding yang tidak).

### 5. MAE (Mean Absolute Error)
Berbeda dari empat metrik di atas yang cocok untuk klasifikasi (berisiko/tidak berisiko), MAE dipakai untuk model yang memprediksi **angka** (misalnya skor kredit dalam skala 0-100, bukan sekadar kategori). MAE mengukur rata-rata selisih absolut antara prediksi model dan nilai sebenarnya — semakin kecil MAE, semakin akurat prediksi angkanya.

<!-- VISUAL PLACEHOLDER: Tabel confusion matrix 2x2 (Prediksi Positif/Negatif vs Aktual Positif/Negatif) dengan highlight warna berbeda untuk True Positive, False Positive, True Negative, False Negative, dan rumus sederhana precision/recall di sampingnya -->

### Trade-off yang Tidak Bisa Dihindari

Presisi dan recall punya hubungan yang saling tarik-menarik (*trade-off*) — meningkatkan salah satunya sering menurunkan yang lain. Model yang sangat "hati-hati" (recall rendah, presisi tinggi) jarang salah menuduh nasabah berisiko, tapi berisiko melewatkan nasabah berisiko yang sebenarnya. Model yang sangat "waspada" (recall tinggi, presisi rendah) menangkap hampir semua nasabah berisiko, tapi sering salah menandai nasabah yang sebenarnya layak sebagai berisiko.

### Kenapa Ini Sangat Kritis untuk Solusi AI

Tidak seperti software biasa yang punya "benar" atau "salah" yang jelas, Solusi AI selalu beroperasi dalam spektrum trade-off ini. Memilih parameter evaluasi yang salah untuk konteks bisnis tertentu — misalnya mengoptimalkan akurasi keseluruhan padahal yang penting adalah recall untuk mendeteksi risiko — bisa membuat Solusi AI "terlihat sukses" di atas kertas, padahal gagal total di tujuan bisnis yang sebenarnya.

---

## Konteks SPKO: Memilih Parameter yang Relevan

| Parameter | Relevansi untuk SPKO |
|---|---|
| Akurasi | Berguna sebagai gambaran umum, tapi tidak cukup sendirian karena nasabah berisiko tinggi biasanya jauh lebih sedikit dibanding yang tidak (data tidak seimbang) |
| Presisi | Penting untuk menghindari menolak kredit nasabah yang sebenarnya layak (false positive merugikan nasabah) |
| Recall | Penting untuk menangkap nasabah yang benar-benar berisiko gagal bayar (false negative merugikan bank) |
| F1-Score | Dipakai sebagai ukuran keseimbangan, terutama karena data risiko kredit biasanya tidak seimbang |
| MAE | Relevan jika SPKO menghasilkan skor kredit dalam skala angka (bukan sekadar kategori layak/tidak layak) |

**Keputusan desain:** SPKO memprioritaskan **F1-Score** sebagai metrik utama pemantauan, karena keseimbangan antara tidak merugikan nasabah (presisi) dan tidak merugikan bank (recall) sama-sama penting — bukan mengorbankan salah satu demi yang lain.

---

## Quick Check

**Tim SPKO melaporkan model mencapai akurasi 96%. Kenapa angka ini saja tidak cukup untuk menyimpulkan model bekerja baik untuk mendeteksi nasabah berisiko tinggi?**

<details>
<summary>Lihat jawaban</summary>

Karena data nasabah berisiko tinggi biasanya jauh lebih sedikit dibanding yang tidak berisiko (data tidak seimbang). Model bisa mencapai akurasi tinggi hanya dengan memprediksi "tidak berisiko" untuk hampir semua nasabah, karena mayoritas memang tidak berisiko — tapi ini berarti model gagal total mendeteksi nasabah berisiko tinggi yang justru paling penting ditangkap. Presisi, recall, dan F1-score memberikan gambaran yang jauh lebih jujur untuk kasus seperti ini.
</details>

---

## Latihan Terstruktur (Simulasi Singkat)
**(Target: 12 menit)**

**Skenario:** Tiga institusi keuangan fiktif memakai model penilaian risiko dengan prioritas berbeda. Tentukan parameter evaluasi mana yang paling relevan untuk masing-masing.

| Institusi | Prioritas Bisnis |
|---|---|
| A | Sangat menghindari menolak nasabah yang sebenarnya layak kredit (reputasi layanan pelanggan jadi prioritas utama) |
| B | Sangat menghindari meloloskan kredit ke nasabah yang berisiko tinggi gagal bayar (menjaga kualitas portofolio kredit) |
| C | Ingin keseimbangan antara keduanya, mengingat data nasabah berisiko tinggi jumlahnya jauh lebih sedikit |

**Instruksi:** Tentukan parameter evaluasi utama (akurasi/presisi/recall/F1) untuk masing-masing, dan alasannya. Kerjakan dalam 12 menit.

<details>
<summary>Lihat kunci jawaban</summary>

| Institusi | Parameter Utama | Alasan |
|---|---|---|
| A | Presisi | Prioritas menghindari false positive (menolak nasabah layak) — presisi tinggi berarti prediksi "berisiko" jarang salah |
| B | Recall | Prioritas menghindari false negative (meloloskan nasabah berisiko) — recall tinggi berarti hampir semua nasabah berisiko berhasil terdeteksi |
| C | F1-Score | Butuh keseimbangan antara presisi dan recall, terutama karena data tidak seimbang membuat akurasi saja tidak cukup informatif |

**Poin penilaian mandiri:** Kalau kamu memilih "akurasi" untuk salah satu institusi di atas, tinjau ulang kenapa akurasi saja tidak pernah cukup untuk keputusan berisiko tinggi dengan data yang tidak seimbang — akurasi menjawab pertanyaan yang berbeda dari yang sebenarnya dibutuhkan tiap institusi.
</details>

---

## Analisis Kasus: Kembali ke Trade-off Presisi vs Recall

Penelitian yang dibahas di hook menunjukkan dengan jelas bahwa "model terbaik" bukan konsep universal — ia bergantung pada apa yang paling penting bagi institusi yang memakainya. Latihan di atas adalah versi konkret dari prinsip yang sama: Institusi A dan B punya prioritas bisnis yang bertentangan secara langsung (menghindari menolak nasabah layak vs menghindari meloloskan nasabah berisiko), dan tidak ada satu model atau metrik yang bisa memuaskan keduanya sekaligus tanpa kompromi.

---

## Implikasi Praktis

**Bagi manajer produk atau pengambil keputusan bisnis (PM/founder):**
Sebelum menentukan target performa model, tetapkan dulu prioritas bisnis secara eksplisit — apakah lebih penting menghindari menolak nasabah layak, atau menghindari meloloskan nasabah berisiko? Ini keputusan bisnis, bukan keputusan teknis semata.

**Bagi perancang sistem/dashboard (UX researcher/designer):**
Dashboard yang menampilkan performa model sebaiknya menyertakan lebih dari satu metrik (bukan hanya akurasi) — memberi konteks yang lebih jujur kepada pengambil keputusan, terutama untuk data yang tidak seimbang.

**Bagi pengembang/petugas teknis (developer/engineer):**
Dokumentasikan secara eksplisit metrik mana yang jadi prioritas utama untuk model tertentu dan alasannya — supaya keputusan perawatan atau penyesuaian model di masa depan (Modul 4-5) tidak kehilangan konteks kenapa metrik itu dipilih sejak awal.

---

## Pertanyaan Refleksi

1. Kalau kamu harus memilih antara model dengan presisi tinggi atau recall tinggi untuk sistem yang kamu kelola, faktor apa yang akan paling menentukan pilihanmu?
2. Penelitian di hook menyebut trade-off antara interpretabilitas (Logistic Regression) dan kemampuan deteksi risiko (Decision Tree+AdaBoost). Menurutmu, seberapa penting interpretabilitas model dibanding performa mentah untuk institusi keuangan yang diatur ketat seperti bank?

---

## Ringkasan Lesson

- Lima parameter evaluasi utama — akurasi, presisi, recall, F1-score, dan MAE — masing-masing menjawab pertanyaan berbeda tentang performa model, dan tidak ada satu metrik yang selalu "paling benar".
- Penelitian akademik Indonesia tentang model credit scoring menunjukkan trade-off nyata antara presisi dan recall, dengan pilihan model yang tepat bergantung pada prioritas bisnis institusi.
- Memahami parameter evaluasi ini adalah fondasi wajib sebelum masuk ke lesson berikutnya — mengevaluasi hasil monitoring SPKO untuk menyusun rencana perawatan yang tepat sasaran.

---

## Referensi

- Penelitian akademik Indonesia mengenai optimalisasi model credit scoring, perbandingan algoritma Logistic Regression dan Decision Tree dengan AdaBoost, Jurnal Ilmiah Informatika Global, 2025.

---

## Navigasi

**[← M3-L5: Dokumentasi & Monitoring Pascadeployment](../m3-deployment-solusi-ai/l5-dokumentasi-monitoring)** | **[M4-L2: Mengumpulkan & Mengevaluasi Hasil Monitoring →](l2-mengumpulkan-mengevaluasi-monitoring)**
