# Git Flow — CodeinteX Learning Platform
## Sederhana tapi kelas dunia

---

## Filosofi

Dua prinsip yang saling melengkapi:
- **GitHub Flow** untuk kesederhanaan (bukan GitFlow yang kompleks)
- **Conventional Commits** untuk konsistensi dan keterlacakan

Hasil: setiap keputusan bisa ditelusuri. Setiap perubahan punya konteks.
Ini yang membedakan repo pribadi biasa dengan repo yang siap diaudit oleh acquirer.

---

## Struktur branch

```
main          ← production (auto-deploy ke Cloudflare)
  └── dev     ← staging / development
       ├── feature/[deskripsi]    ← fitur baru
       ├── content/[modul-lesson] ← perubahan konten
       ├── fix/[deskripsi]        ← bug fix
       └── hotfix/[deskripsi]     ← fix kritis langsung ke main
```

### Aturan per branch

**`main`**
- Selalu production-ready dan auto-deploy ke Cloudflare
- Tidak pernah di-commit langsung — hanya menerima merge dari `dev` atau `hotfix/`
- Setiap merge ke `main` diberi Git tag versi

**`dev`**
- Tempat semua pekerjaan diintegrasikan sebelum naik ke production
- Boleh broken sementara — ini adalah staging
- Auto-deploy ke preview URL Cloudflare (opsional)

**`feature/`, `content/`, `fix/`**
- Branch dari `dev`
- Merge kembali ke `dev` setelah selesai
- Hapus setelah merge

**`hotfix/`**
- Branch dari `main` untuk fix kritis yang tidak bisa menunggu siklus normal
- Merge ke `main` DAN ke `dev` setelah selesai

---

## Conventional Commits — format standar

```
<type>(<scope>): <deskripsi singkat>

[body opsional]

[footer opsional]
```

### Type yang digunakan

| Type | Kapan dipakai | Contoh |
|---|---|---|
| `feat` | Fitur baru | `feat(navigation): add breadcrumb to lesson page` |
| `fix` | Bug fix | `fix(quickcheck): state not resetting on navigation` |
| `content` | Perubahan konten kursus | `content(m1-l1): apply audit fixes — bilingual terms` |
| `style` | Perubahan visual/CSS | `style(lesson): improve mobile typography` |
| `refactor` | Refactoring tanpa feature/fix | `refactor(lib): simplify content parsing logic` |
| `docs` | Dokumentasi | `docs(iframe-rank): add auth decision` |
| `chore` | Maintenance | `chore(deps): update Next.js to 16.2.9` |
| `perf` | Performance | `perf(images): add lazy loading to lesson images` |

### Scope yang digunakan

| Scope | Apa |
|---|---|
| `lesson` | Komponen atau halaman lesson |
| `navigation` | Navigasi course/module/lesson |
| `content` | File MD di /content |
| `m1` s/d `m6` | Modul spesifik |
| `deps` | Dependencies |
| `config` | Konfigurasi Next.js, Tailwind, dll |
| `deploy` | Cloudflare, wrangler config |

---

## Workflow sehari-hari

### Untuk fitur baru atau fix

```bash
# 1. Pastikan dev terbaru
git checkout dev
git pull origin dev

# 2. Buat branch baru
git checkout -b feature/quick-check-animation

# 3. Kerja, commit dengan pesan yang jelas
git add components/QuickCheck.tsx
git commit -m "feat(lesson): add slide-down animation to QuickCheck reveal"

# 4. Push ke remote
git push origin feature/quick-check-animation

# 5. Merge ke dev (langsung, tanpa PR karena solo founder)
git checkout dev
git merge feature/quick-check-animation --no-ff
git push origin dev

# 6. Hapus branch yang sudah selesai
git branch -d feature/quick-check-animation
git push origin --delete feature/quick-check-animation
```

### Untuk perubahan konten kursus

```bash
git checkout dev
git pull origin dev
git checkout -b content/m2-l2-hook-fix

# Edit file konten
git add content/courses/hcai-foundations/m2-how-people-think/l2-mental-models.md
git commit -m "content(m2-l2): replace hypothetical hook with Khoong et al. 2019 case"

git checkout dev
git merge content/m2-l2-hook-fix --no-ff
git push origin dev
git branch -d content/m2-l2-hook-fix
```

### Deploy ke production

```bash
# Setelah dev sudah diverifikasi
git checkout main
git merge dev --no-ff
git tag -a v0.2.0 -m "feat: Phase 1 complete — all 25 lessons rendered"
git push origin main --tags
```

---

## Versi tagging — Semantic Versioning

Format: `vMAJOR.MINOR.PATCH`

| Versi | Kapan naik |
|---|---|
| PATCH (0.0.x) | Bug fix, perubahan konten kecil |
| MINOR (0.x.0) | Fitur baru (phase baru, komponen baru) |
| MAJOR (x.0.0) | Perubahan fundamental (auth, DB, redesign) |

Milestone yang direncanakan:
- `v0.1.0` — Setup project selesai
- `v0.2.0` — Phase 1 selesai: semua 25 lesson bisa dibaca
- `v0.3.0` — Phase 2 selesai: auth + enrollment
- `v0.4.0` — Phase 3 selesai: progress tracking
- `v0.5.0` — Phase 4 selesai: certificate
- `v1.0.0` — Public launch

---

## .gitignore

```
# Dependencies
node_modules/
.pnp
.pnp.js

# Build outputs
.next/
.open-next/
out/
dist/

# Cloudflare
.wrangler/

# Environment
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# OS
.DS_Store
Thumbs.db

# IDE
.idea/
.vscode/
*.swp
*.swo

# Debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

---

## Commit pertama yang benar

```bash
cd codeintex-learning
git init
git add .
git commit -m "chore: initial project setup

- Next.js 16.2.7 + TypeScript + Tailwind 3.4.17
- @next/mdx 16.2.9 untuk content rendering
- @opennextjs/cloudflare 1.19.11 untuk deployment
- 25 lesson files di content/courses/hcai-foundations/
- Semua versi dipinned untuk konsistensi local/staging/production"

git branch -M main
git checkout -b dev
git push -u origin main
git push -u origin dev
```

---

## Setup GitHub repository

```bash
# Buat repo di GitHub (private), lalu:
git remote add origin https://github.com/[username]/codeintex-learning.git
git push -u origin main
git push -u origin dev
```

Branch protection rules yang disarankan (Settings → Branches):
- `main`: require pull request before merging, atau minimal manual review
- `dev`: tidak perlu protection untuk solo founder

---

*Dokumen ini adalah referensi Git flow untuk CodeinteX Learning Platform.*
*Dibuat berdasarkan GitHub Flow + Conventional Commits — standar yang dipakai Angular, Vue, dan sebagian besar open source besar.*
