# Brief untuk Antigravity: Pasang Konten Kursus 2 (AI untuk Proses Data)

## Konteks
File terlampir (`ai-untuk-proses-data-content.zip`) berisi 25 lesson markdown + `_course.json` untuk kursus baru "AI untuk Proses Data", dibuat mengikuti pola folder yang sama seperti kursus `hcai-foundations` yang sudah ada.

## Tugas

1. **Extract file zip** ke `content/courses/` di repo `codeintex-learning`, di branch baru (`content/ai-untuk-proses-data`, dibuat dari `dev`) — bukan langsung ke `main`.

2. **Cek `_course.json` yang saya buat** cocok atau tidak dengan schema yang benar-benar dibaca oleh kode di `lib/content.ts`. Saya membuatnya menebak-nebak dari deskripsi, jadi kemungkinan ada field yang perlu disesuaikan atau dihapus. Perbaiki supaya cocok dengan yang sistem butuhkan.

3. **Cek frontmatter tiap lesson** (di bagian atas tiap file, antara `---`) apakah field-nya cocok dengan yang dipakai `LessonRenderer.tsx`. Field seperti `bloom_level`, `durasi_baca_menit` saya buat menebak dari pola HCAI — sesuaikan kalau ternyata beda.

4. **PALING PENTING — cek komponen Quick Check:** Semua 25 lesson memakai format HTML biasa seperti ini untuk bagian tanya-jawab:
   ```html
   <details>
   <summary>Lihat jawaban</summary>
   [isi jawaban]
   </details>
   ```
   Tapi kalau `QuickCheck.tsx` yang sudah ada di sistem itu komponen interaktif MDX khusus (bukan HTML `<details>` biasa), semua 25 file ini perlu dikonversi ke format komponen yang benar. **Cek ini duluan sebelum lanjut yang lain** — kalau formatnya salah, harus diperbaiki di semua file sekaligus, jadi lebih baik ketahuan di awal.

5. **Jalankan `npm run dev` dan buka tiap modul di browser** — pastikan render rapi: tabel markdown, bagian jawaban (`<details>`), navigasi sidebar, breadcrumb.

6. **Ganti semua placeholder diagram** — di tiap file ada baris `<!-- VISUAL PLACEHOLDER: ... -->` yang menjelaskan diagram apa yang seharusnya ada di situ. Ini instruksi untuk desain visual, belum jadi diagram sungguhan.

7. **JANGAN ubah status course jadi "Live" di homepage dulu** — tunggu konfirmasi dari saya (Yudi), karena isi lesson-nya belum saya baca ulang secara menyeluruh sendiri.

8. Setelah semua di atas beres dan dites jalan lancar di local: commit dengan pesan `content: add Kursus 2 - AI untuk Proses Data (25 lessons)`, push ke branch `content/ai-untuk-proses-data`, biar saya review sebelum merge ke `dev`.

## Kalau Ada yang Tidak Jelas
Laporkan balik ke saya (Yudi) — jangan menebak dan lanjut sendiri, terutama untuk poin 2-4 yang menyangkut kecocokan dengan kode yang sudah ada.
