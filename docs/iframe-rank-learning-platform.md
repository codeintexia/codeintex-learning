# IFRAME Decision Log — CodeinteX Learning Platform UI
**Tahap: Rank**
**Tanggal:** 2026
**Produk:** learning.codeintex.com — Course platform untuk "Human-Centered AI — Foundations"

---

## Konteks (Identify)

**Produk:** Platform kursus online untuk kursus HCAI Foundations (gratis, 25 lesson, 6 modul)
**Audiens awal:** PM, startup founder, UX researcher, developer — Indonesia dan global
**Constraint:** Solo founder, dibantu AI (Antigravity), deploy bertahap
**Tujuan immediate:** Local preview yang bisa divalidasi, kemudian deploy ke learning.codeintex.com

---

## Flow utama yang harus dilayani UI (Flow)

1. **Discovery flow** — visitor memahami value prop kursus → memutuskan daftar
2. **Onboarding flow** — register → mulai lesson pertama
3. **Learning flow** — buka lesson → baca → Quick Check → navigasi ke lesson berikutnya
4. **Progress flow** — learner melihat posisi dan progres di kursus
5. **Completion flow** — selesai kursus → dapat certificate → bisa di-share

---

## Keputusan arsitektur (Rank)

### DIPUTUSKAN: Tech stack

| Komponen | Keputusan | Alasan |
|---|---|---|
| Framework | Next.js 14 (App Router) | SSR + route protection + file-based routing |
| Content rendering | next-mdx-remote | Render MD files dari /content/courses |
| Auth | Clerk | Zero config, free tier 10k MAU, custom domain support |
| Database | Supabase (PostgreSQL) | Free tier, portable schema, row-level security |
| Styling | Tailwind CSS | Utility-first, konsisten dengan ekosistem Next.js |
| Deployment (awal) | Local (npm run dev) | Validasi konten sebelum invest ke hosting |
| Deployment (final) | Vercel (frontend) + Supabase (DB) | Free tier cukup untuk fase awal |

**Trade-off yang diterima:** Clerk adalah vendor dependency. Jika perlu migrasi, gunakan NextAuth.js — skema DB tidak berubah.

---

### DIPUTUSKAN: Build sequence (4 phase)

**Phase 1 — Content rendering (prioritas tertinggi)**
- Render semua 25 lesson dari /content/courses sebagai halaman Next.js
- Navigasi: course → module → lesson (breadcrumb)
- Semua lesson terbuka tanpa auth (untuk validasi konten)
- Progress bar visual per modul (dummy, belum connected ke DB)
- Quick Check sebagai komponen interaktif (state lokal)
- Diagram placeholder dirender sebagai SVG berdasarkan komentar HTML di MD

**Trade-off:** Tanpa auth di Phase 1, semua konten terbuka. Ini disengaja untuk validasi cepat.

**Phase 2 — Auth + enrollment**
- Integrasi Clerk untuk register/login
- Supabase: tabel users dan enrollments
- Route protection: lesson hanya bisa diakses setelah enroll
- Free course = auto-enroll saat register pertama kali

**Phase 3 — Progress tracking**
- Supabase: tabel lesson_progress
- Mark lesson complete saat learner scroll ke bawah + klik tombol
- Progress bar per modul connected ke DB
- Dashboard learner: modul yang sudah selesai, lesson yang sedang berjalan

**Phase 4 — Certificate**
- Generate certificate HTML saat lesson_progress 100% untuk semua lesson
- Simpan cert_hash (UUID) di tabel certificates Supabase
- Halaman /certificate/[cert_hash] yang bisa di-share dan diverifikasi
- Certificate bisa di-print sebagai PDF dari browser

---

### DIPUTUSKAN: Database schema (portable)

```sql
-- Users (dikelola Clerk, disinkronkan ke Supabase)
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  clerk_id TEXT UNIQUE NOT NULL,
  email TEXT NOT NULL,
  name TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Enrollments
CREATE TABLE enrollments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  course_slug TEXT NOT NULL,  -- e.g., 'hcai-foundations'
  enrolled_at TIMESTAMPTZ DEFAULT NOW(),
  completed_at TIMESTAMPTZ
);

-- Lesson Progress
CREATE TABLE lesson_progress (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  course_slug TEXT NOT NULL,
  module_number INTEGER NOT NULL,
  lesson_number INTEGER NOT NULL,
  completed_at TIMESTAMPTZ DEFAULT NOW()
);

-- Certificates
CREATE TABLE certificates (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  course_slug TEXT NOT NULL,
  cert_hash TEXT UNIQUE DEFAULT gen_random_uuid()::TEXT,
  issued_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

### DIPUTUSKAN: Struktur folder project

```
codeintex-learning/
├── content/
│   └── courses/
│       └── hcai-foundations/
│           ├── _course.json         ← metadata kursus
│           ├── m1-what-is-hcai/
│           │   ├── _module.json     ← metadata modul
│           │   ├── l1-ketika-ai-gagal.md
│           │   ├── l2-pergeseran-paradigma.md
│           │   ├── l3-dua-sumbu-shneiderman.md
│           │   └── l4-empat-prinsip-hcai.md
│           ├── m2-how-people-think/
│           │   └── [4 lesson files]
│           ├── m3-the-four-principles/
│           │   └── [5 lesson files]
│           ├── m4-explainability-fairness/
│           │   └── [4 lesson files]
│           ├── m5-designing-with-iframe/
│           │   └── [4 lesson files]
│           └── m6-evaluating-hcai/
│               └── [4 lesson files]
├── src/
│   └── app/
│       ├── page.tsx                 ← halaman utama kursus
│       ├── courses/
│       │   └── [course]/
│       │       ├── page.tsx         ← overview kursus
│       │       └── [module]/
│       │           └── [lesson]/
│       │               └── page.tsx ← halaman lesson
│       ├── dashboard/
│       │   └── page.tsx             ← learner dashboard (Phase 3)
│       └── certificate/
│           └── [hash]/
│               └── page.tsx         ← halaman certificate (Phase 4)
├── src/components/
│   ├── LessonRenderer.tsx           ← render MDX + Quick Check
│   ├── ModuleProgress.tsx           ← progress bar per modul
│   ├── QuickCheck.tsx               ← komponen Quick Check interaktif
│   ├── DiagramRenderer.tsx          ← render DIAGRAM placeholders sebagai SVG
│   └── CourseNavigation.tsx         ← navigasi prev/next lesson
└── src/lib/
    ├── content.ts                   ← fungsi baca MD files
    └── supabase.ts                  ← Supabase client
```

---

## Yang sengaja TIDAK dibangun di Phase 1

- Komentar dan diskusi antar learner (bisa ditambahkan nanti)
- Email notifications
- Analytics dashboard (pakai Vercel Analytics yang sudah built-in)
- Multi-course support (satu kursus dulu, arsitektur sudah mendukung scaling)
- Payment (kursus ini gratis)

**Alasan:** Memvalidasi learning experience sebelum menambah kompleksitas.

---

*Dokumen ini adalah artefak IFRAME tahap Rank untuk CodeinteX Learning Platform.*
*Update ketika ada keputusan baru di tahap Apply atau Measure.*
