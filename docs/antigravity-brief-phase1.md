# Brief untuk Antigravity — CodeinteX Learning Platform
## Phase 1: Content Rendering (Static)
## Versi: 2.0 — Updated Juni 2026

---

## Konteks proyek

Platform kursus online CodeinteX di learning.codeintex.com.
Kursus pertama: **"Human-Centered AI — Foundations"** — gratis, 25 lesson, 6 modul, Bahasa Indonesia.
Semua konten sudah ada sebagai Markdown files di `content/courses/hcai-foundations/`.

Phase 1 tujuan: semua 25 lesson bisa dibaca di localhost. Tanpa auth, tanpa database.

---

## PENTING: Versi yang dipinned

Jangan gunakan versi lain. Alasan ada di catatan di bawah setiap package.

```json
{
  "engines": {
    "node": ">=20.9.0"
  },
  "dependencies": {
    "next": "16.2.7",
    "react": "19.1.0",
    "react-dom": "19.1.0",
    "@next/mdx": "16.2.9",
    "@mdx-js/loader": "3.1.0",
    "@mdx-js/react": "3.1.0",
    "@types/mdx": "2.0.13",
    "gray-matter": "4.0.3",
    "tailwindcss": "3.4.17",
    "@tailwindcss/typography": "0.5.15"
  },
  "devDependencies": {
    "@opennextjs/cloudflare": "1.19.11",
    "wrangler": "3.114.0",
    "typescript": "5.7.3",
    "@types/node": "22.10.0",
    "@types/react": "19.1.0",
    "@types/react-dom": "19.1.0"
  }
}
```

**Catatan versioning penting:**
- `next-mdx-remote` → JANGAN PAKAI. Diarsipkan April 9, 2026. Gunakan `@next/mdx` saja.
- `@cloudflare/next-on-pages` → JANGAN PAKAI. Deprecated oleh Cloudflare. Gunakan `@opennextjs/cloudflare`.
- `next` harus `16.2.7` atau lebih baru dalam 16.x — ada CVE di semua versi 13.x, 14.x, 15.x.
- `tailwindcss` tetap `3.4.17` (bukan v4) — `@tailwindcss/typography` lebih stabil di v3.
- Semua versi harus exact (tanpa `^` atau `~`) di package.json untuk menghindari drift antara local dan production.

---

## File `.nvmrc` (buat di root project)

```
22.15.0
```

Node.js 22 LTS. Siapapun yang clone repo ini menjalankan `nvm use` dan mendapat versi yang sama.

---

## File `package.json` lengkap

```json
{
  "name": "codeintex-learning",
  "version": "0.1.0",
  "private": true,
  "engines": {
    "node": ">=20.9.0"
  },
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "preview": "opennextjs-cloudflare build && wrangler pages dev",
    "deploy": "opennextjs-cloudflare build && wrangler pages deploy"
  },
  "dependencies": {
    "next": "16.2.7",
    "react": "19.1.0",
    "react-dom": "19.1.0",
    "@next/mdx": "16.2.9",
    "@mdx-js/loader": "3.1.0",
    "@mdx-js/react": "3.1.0",
    "@types/mdx": "2.0.13",
    "gray-matter": "4.0.3",
    "tailwindcss": "3.4.17",
    "@tailwindcss/typography": "0.5.15"
  },
  "devDependencies": {
    "@opennextjs/cloudflare": "1.19.11",
    "wrangler": "3.114.0",
    "typescript": "5.7.3",
    "@types/node": "22.10.0",
    "@types/react": "19.1.0",
    "@types/react-dom": "19.1.0",
    "postcss": "8.5.3",
    "autoprefixer": "10.4.21"
  }
}
```

---

## Tech stack Phase 1

| Komponen | Tools | Alasan |
|---|---|---|
| Framework | Next.js 16.2.7 App Router | Stable, security patched |
| Content rendering | @next/mdx 16.2.9 | Official, dirawat aktif, next-mdx-remote sudah deprecated |
| Frontmatter parsing | gray-matter 4.0.3 | Stable, tidak berubah bertahun-tahun |
| Styling | Tailwind CSS 3.4.17 + typography plugin | v3 paling stabil untuk prose content |
| Language | TypeScript 5.7.3 | Type safety sejak hari pertama |
| Deployment local | next dev | Standard |
| Deployment production | @opennextjs/cloudflare + Cloudflare Workers | Gratis, unlimited bandwidth, commercial use OK |

---

## Setup project (jalankan persis seperti ini)

```bash
# 1. Buat project
npx create-next-app@16.2.7 codeintex-learning \
  --typescript \
  --tailwind \
  --app \
  --no-src-dir \
  --import-alias "@/*"

cd codeintex-learning

# 2. Install exact versions (hapus yang di-install otomatis dulu)
npm install \
  next@16.2.7 \
  react@19.1.0 \
  react-dom@19.1.0 \
  @next/mdx@16.2.9 \
  @mdx-js/loader@3.1.0 \
  @mdx-js/react@3.1.0 \
  "@types/mdx@2.0.13" \
  gray-matter@4.0.3 \
  tailwindcss@3.4.17 \
  "@tailwindcss/typography@0.5.15"

npm install -D \
  "@opennextjs/cloudflare@1.19.11" \
  "wrangler@3.114.0"

# 3. Buat .nvmrc
echo "22.15.0" > .nvmrc
```

---

## next.config.ts

```typescript
import type { NextConfig } from 'next'
import createMDX from '@next/mdx'

const withMDX = createMDX({
  options: {
    remarkPlugins: [],
    rehypePlugins: [],
  },
})

const nextConfig: NextConfig = {
  pageExtensions: ['js', 'jsx', 'md', 'mdx', 'ts', 'tsx'],
  experimental: {
    mdxRs: true,
  },
}

export default withMDX(nextConfig)
```

---

## tailwind.config.ts

```typescript
import type { Config } from 'tailwindcss'
import typography from '@tailwindcss/typography'

const config: Config = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './content/**/*.{md,mdx}',
  ],
  theme: {
    extend: {
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '72ch',
            color: 'inherit',
          },
        },
      },
    },
  },
  plugins: [typography],
}

export default config
```

---

## Struktur folder yang harus dibuat

```
codeintex-learning/
├── content/
│   └── courses/
│       └── hcai-foundations/
│           ├── _course.json
│           ├── m1-what-is-hcai/
│           │   ├── l1-when-ai-fails.md
│           │   ├── l2-paradigm-shift.md
│           │   ├── l3-shneiderman-axes.md
│           │   └── l4-four-hcai-principles.md
│           ├── m2-how-people-think/
│           │   ├── l1-why-humans-misunderstand-ai.md
│           │   ├── l2-mental-models.md
│           │   ├── l3-overtrust-undertrust.md
│           │   └── l4-case-study-ridehailing.md
│           ├── m3-the-four-principles/
│           │   ├── l1-transparency.md
│           │   ├── l2-fairness.md
│           │   ├── l3-human-control.md
│           │   ├── l4-accountability.md
│           │   └── l5-audit-exercise.md
│           ├── m4-explainability-fairness/
│           │   ├── l1-black-box-to-glass-box.md
│           │   ├── l2-who-needs-what-explanation.md
│           │   ├── l3-where-bias-comes-from.md
│           │   └── l4-case-study-sea-bias.md
│           ├── m5-designing-with-iframe/
│           │   ├── l1-why-conventional-design-fails.md
│           │   ├── l2-iframe-how-it-works.md
│           │   ├── l3-insight-to-design-decision.md
│           │   └── l4-iframe-exercise.md
│           └── m6-evaluating-hcai/
│               ├── l1-beyond-accuracy.md
│               ├── l2-human-centered-evaluation.md
│               ├── l3-measuring-trust.md
│               └── l4-capstone.md
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── globals.css
│   └── courses/
│       └── [course]/
│           ├── page.tsx
│           └── [module]/
│               ├── page.tsx
│               └── [lesson]/
│                   └── page.tsx
├── components/
│   ├── LessonRenderer.tsx
│   ├── QuickCheck.tsx
│   ├── DiagramRenderer.tsx
│   └── CourseNavigation.tsx
├── lib/
│   └── content.ts
├── docs/
│   ├── iframe-rank-learning-platform.md
│   └── antigravity-brief-phase1.md  ← file ini
├── .nvmrc
├── next.config.ts
├── tailwind.config.ts
├── tsconfig.json
└── package.json
```

---

## _course.json

```json
{
  "slug": "hcai-foundations",
  "title": "Human-Centered AI — Foundations",
  "subtitle": "Merancang sistem AI yang benar-benar bekerja untuk manusia",
  "language": "id",
  "level": "foundational",
  "duration_hours": 6,
  "is_free": true,
  "modules": [
    { "number": 1, "slug": "m1-what-is-hcai", "title": "What Is Human-Centered AI?", "lessons": 4 },
    { "number": 2, "slug": "m2-how-people-think", "title": "How People Think About and Trust AI", "lessons": 4 },
    { "number": 3, "slug": "m3-the-four-principles", "title": "The Four Principles — What HCAI Demands", "lessons": 5 },
    { "number": 4, "slug": "m4-explainability-fairness", "title": "Explainability and Fairness in Practice", "lessons": 4 },
    { "number": 5, "slug": "m5-designing-with-iframe", "title": "Designing Human-Centered AI with IFRAME", "lessons": 4 },
    { "number": 6, "slug": "m6-evaluating-hcai", "title": "Evaluating and Improving HCAI Systems", "lessons": 4 }
  ]
}
```

---

## lib/content.ts

```typescript
import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'

const contentDir = path.join(process.cwd(), 'content/courses')

export interface LessonFrontmatter {
  course: string
  module: number
  module_title: string
  lesson: number
  title: string
  duration_minutes: number
  bloom_level: string
  keywords: string[]
  is_free: boolean
  status: string
  slug?: string
}

export interface LessonData {
  frontmatter: LessonFrontmatter
  content: string
  slug: string
  moduleSlug: string
  courseSlug: string
}

export function getLessonSlugs(courseSlug: string, moduleSlug: string): string[] {
  const moduleDir = path.join(contentDir, courseSlug, moduleSlug)
  return fs
    .readdirSync(moduleDir)
    .filter((f) => f.endsWith('.md') && !f.startsWith('_'))
    .map((f) => f.replace('.md', ''))
    .sort()
}

export function getLesson(
  courseSlug: string,
  moduleSlug: string,
  lessonSlug: string
): LessonData {
  const filePath = path.join(contentDir, courseSlug, moduleSlug, `${lessonSlug}.md`)
  const raw = fs.readFileSync(filePath, 'utf-8')
  const { data, content } = matter(raw)

  return {
    frontmatter: data as LessonFrontmatter,
    content,
    slug: lessonSlug,
    moduleSlug,
    courseSlug,
  }
}

export function getModuleSlugs(courseSlug: string): string[] {
  const courseDir = path.join(contentDir, courseSlug)
  return fs
    .readdirSync(courseDir)
    .filter((f) => {
      const fullPath = path.join(courseDir, f)
      return fs.statSync(fullPath).isDirectory() && f.startsWith('m')
    })
    .sort()
}

export function getAllLessons(courseSlug: string): LessonData[] {
  const lessons: LessonData[] = []
  const moduleSlugs = getModuleSlugs(courseSlug)

  for (const moduleSlug of moduleSlugs) {
    const lessonSlugs = getLessonSlugs(courseSlug, moduleSlug)
    for (const lessonSlug of lessonSlugs) {
      lessons.push(getLesson(courseSlug, moduleSlug, lessonSlug))
    }
  }

  return lessons
}
```

---

## Komponen QuickCheck.tsx

Setiap lesson punya Quick Check dalam format:
```
> **Quick Check** — Sebelum melanjutkan:
> *[pertanyaan]*
```

Render sebagai komponen interaktif:
- Card dengan background teal muda
- Label "Quick Check" yang prominan
- Tombol "Saya sudah memikirkannya →" yang bisa di-toggle
- State di `useState` (tidak perlu localStorage untuk Phase 1)
- Tidak ada jawaban "benar" — hanya mendorong refleksi

```typescript
'use client'

import { useState } from 'react'

interface QuickCheckProps {
  question: string
}

export default function QuickCheck({ question }: QuickCheckProps) {
  const [checked, setChecked] = useState(false)

  return (
    <div className="my-8 rounded-lg border border-teal-200 bg-teal-50 p-6">
      <p className="mb-1 text-xs font-semibold uppercase tracking-widest text-teal-600">
        Quick Check
      </p>
      <p className="mb-4 text-sm text-gray-700">{question}</p>
      {!checked ? (
        <button
          onClick={() => setChecked(true)}
          className="rounded-md bg-teal-600 px-4 py-2 text-sm font-medium text-white hover:bg-teal-700"
        >
          Saya sudah memikirkannya →
        </button>
      ) : (
        <p className="text-sm text-teal-700">
          ✓ Bagus. Lanjutkan ke analisis kasus di bawah.
        </p>
      )}
    </div>
  )
}
```

---

## Komponen DiagramRenderer.tsx

Diagram placeholder ada dalam HTML comment di dalam MD:
```html
<!-- DIAGRAM: [Judul]
     [spesifikasi]
-->
```

Render sebagai styled callout — bukan diagram sesungguhnya, hanya placeholder yang jelas:

```typescript
interface DiagramProps {
  title: string
  spec: string
}

export default function DiagramPlaceholder({ title, spec }: DiagramProps) {
  return (
    <div className="my-8 rounded-lg border-2 border-dashed border-gray-300 bg-gray-50 p-6">
      <div className="mb-2 flex items-center gap-2">
        <span className="text-lg">📊</span>
        <span className="text-sm font-semibold text-gray-600">Diagram: {title}</span>
      </div>
      <p className="text-xs italic text-gray-400">{spec}</p>
      <p className="mt-2 text-xs text-gray-400">
        Diagram interaktif akan hadir di versi berikutnya.
      </p>
    </div>
  )
}
```

---

## LessonRenderer.tsx

Komponen utama yang merender konten MD, memproses Quick Check dan Diagram:

```typescript
import ReactMarkdown from 'react-markdown'
import QuickCheck from './QuickCheck'
import DiagramPlaceholder from './DiagramRenderer'

interface LessonRendererProps {
  content: string
}

export default function LessonRenderer({ content }: LessonRendererProps) {
  // Proses Quick Check dari blockquote pattern
  // Proses Diagram dari HTML comment pattern
  // Render sisanya sebagai Markdown biasa dengan prose styling

  return (
    <article className="prose prose-gray max-w-none">
      {/* Parsing dan rendering konten */}
    </article>
  )
}
```

Untuk implementasi lengkap parsing Quick Check dan Diagram dari MD — gunakan regex untuk mengekstrak patterns dan replace dengan komponen React.

---

## Komponen CourseNavigation.tsx

Tombol navigasi prev/next di bawah setiap lesson:

```typescript
interface CourseNavigationProps {
  prevLesson?: { title: string; href: string }
  nextLesson?: { title: string; href: string }
}

export default function CourseNavigation({ prevLesson, nextLesson }: CourseNavigationProps) {
  return (
    <nav className="mt-12 flex items-center justify-between border-t pt-8">
      {prevLesson ? (
        <a href={prevLesson.href} className="flex items-center gap-2 text-sm text-gray-600 hover:text-teal-600">
          ← {prevLesson.title}
        </a>
      ) : <div />}
      {nextLesson && (
        <a href={nextLesson.href} className="flex items-center gap-2 text-sm font-medium text-teal-600 hover:text-teal-700">
          {nextLesson.title} →
        </a>
      )}
    </nav>
  )
}
```

---

## Design direction

- **Tone:** Professional tapi tidak dingin. Bersih, readable.
- **Font:** Inter (sudah ada di Next.js default) atau system-ui
- **Color:** Teal (#0d9488) sebagai accent utama, putih, slate/gray
- **Layout:** Single column, max-w-3xl untuk konten lesson
- **Sidebar:** Navigasi modul/lesson di kiri, sticky
- **Mobile:** Responsive sejak awal

---

## Output yang diharapkan dari Phase 1

Setelah selesai, harusnya bisa:
1. `npm run dev` → buka `localhost:3000`
2. Navigasi ke `/courses/hcai-foundations`
3. Melihat daftar 6 modul
4. Masuk ke lesson manapun dan membaca konten
5. Melihat Quick Check yang interaktif
6. Navigasi prev/next antar lesson
7. `npm run preview` → test di Cloudflare Workers runtime lokal

---

## Yang TIDAK perlu dibangun sekarang

- Login/register
- Progress tracking
- Certificate
- Payment
- Search
- Comments
- Analytics

---

*Brief ini adalah artefak IFRAME tahap Apply — Phase 1.*
*Versi: 2.0 | Diupdate: Juni 2026*
*Perubahan dari v1: next-mdx-remote → @next/mdx, Vercel → Cloudflare Workers via OpenNext, versi semua package dipinned*
