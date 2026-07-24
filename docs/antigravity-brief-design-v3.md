# Design Brief v3 — CodeinteX Learning Platform
## Final UI Pass: Stealth Mode + Corporate Academic Tone

---

## IMPORTANT RULES

- Do NOT display any personal name (no "Yudi Utomo", no "Prayudi Utomo", no initials)
- Do NOT change any routing, content parsing, or component logic
- Do NOT change any .md content files
- Attribution is always to "CodeinteX" as an entity, never to an individual
- Target tone: corporate + academic + practical — reference: Coursera, edX

---

## FIX 1 — Lesson metadata: replace long text with pill badges

Replace the single long metadata text line with individual pill badges.

```
Container: display flex, flex-wrap wrap, gap 8px, margin-bottom 32px

Each badge:
  background: #f1f5f9
  color: #475569
  font-size: 12px
  padding: 3px 12px
  border-radius: 999px
  font-weight: 500

Badges to show (in this order):
  1. Module name (e.g. "Modul 1 · What Is Human-Centered AI?")
  2. Lesson position (e.g. "Lesson 2 dari 4")
  3. Reading time (e.g. "⏱ 12 menit")
  4. Level (e.g. "Foundational")
  5. Bloom's level (e.g. "Understand")
```

---

## FIX 2 — Sidebar active lesson: make it unmistakably obvious

```
Active lesson item:
  background: #f0fdfa
  color: #0d9488
  font-weight: 700
  border-left: 3px solid #0d9488
  padding-left: 13px

Add before active lesson title:
  A filled teal circle: width 6px, height 6px,
  background #0d9488, border-radius 50%, margin-right 8px
```

---

## FIX 3 — Homepage hero card: add depth

```
Course preview card:
  box-shadow: 0 8px 40px rgba(0,0,0,0.12)
  border: 1px solid #e2e8f0
  border-radius: 16px
  overflow: hidden

Add at very top of card:
  height: 4px
  background: linear-gradient(90deg, #0d9488, #14b8a6)
  width: 100%
```

---

## FIX 4 — Micro-interactions

```
All buttons:
  transition: all 150ms ease
  hover: transform scale(1.01)

All cards:
  transition: all 200ms ease
  hover: transform translateY(-2px)
  hover: box-shadow 0 4px 16px rgba(0,0,0,0.08)

All text links:
  transition: color 150ms ease
```

---

## FIX 5 — Replace instructor section with institutional trust block

Remove any instructor/person section entirely.
Add this section between learning outcomes and module cards:

```
Container:
  background: #f8fafc
  border: 1px solid #e2e8f0
  border-radius: 12px
  padding: 32px 40px
  display: flex
  align-items: center
  gap: 40px
  margin: 40px 0

Left side — CodeinteX logo mark:
  The existing CX logo, size 48px
  background: white
  border: 1px solid #e2e8f0
  border-radius: 10px
  padding: 10px

Right side — text:
  Label: "TENTANG KURSUS INI"
    color: #0d9488
    font-size: 11px
    font-weight: 700
    letter-spacing: 0.1em
    uppercase
    margin-bottom: 6px

  Heading: "Dikembangkan oleh CodeinteX"
    color: #0f172a
    font-size: 17px
    font-weight: 700
    margin-bottom: 8px

  Body:
    "Kursus ini dirancang dan diproduksi oleh CodeinteX —
    sebuah firma pengetahuan dan rekayasa yang berfokus pada
    sistem AI yang berpusat pada manusia dan dapat dijelaskan.
    Seluruh konten berbasis penelitian akademis terverifikasi
    dan metodologi IFRAME eksklusif CodeinteX."
    color: #64748b
    font-size: 14px
    line-height: 1.6

Three badges below body text, flex row, gap 8px:
  Badge 1: "📚 Referensi akademis terverifikasi"
  Badge 2: "⚙️ Metodologi IFRAME eksklusif"
  Badge 3: "✓ 100% gratis & terbuka"

  Badge styling:
    background: white
    border: 1px solid #e2e8f0
    color: #475569
    font-size: 12px
    padding: 4px 12px
    border-radius: 999px
```

---

## FIX 6 — Rewrite all marketing copy to outcome-focused language

Replace process-focused language with outcome-focused language throughout.

Homepage hero body text — replace with:
```
"Kuasai kerangka kerja untuk merancang, mengevaluasi,
dan mengaudit sistem AI yang transparan, adil, dan
bertanggung jawab. Berbasis penelitian akademis.
Dapat langsung diterapkan."
```

Homepage hero badge — replace with:
```
"Kursus Baru · Gratis & Terbuka"
```

Module cards "Lihat Outline Modul →" — replace with:
```
"Mulai Modul →"
```

Bottom CTA button — replace with:
```
"Mulai Belajar Sekarang — Gratis"
```

Footer copyright line — replace with:
```
"© 2026 CodeinteX. Kursus ini diproduksi sebagai bagian
dari inisiatif pendidikan AI CodeinteX."
```

---

## FIX 7 — Course page header: add institutional framing

On the course detail page (/courses/hcai-foundations), add below the course title:

```
A subtle one-line attribution:
  "Diproduksi oleh CodeinteX · Bahasa Indonesia · Tersedia gratis"
  color: #64748b
  font-size: 13px
  margin-top: 8px
```

---

## What NOT to change

- Any personal name — never display "Yudi", "Prayudi", "Y.U." or any variation
- All routing and URL structure
- All content parsing logic
- All .md content files
- generateStaticParams
- package.json and next.config.ts
- Anything in /docs folder

---

## Priority order

1. FIX 1 — Metadata badges (lesson page)
2. FIX 2 — Sidebar active state
3. FIX 5 — Institutional trust block (replaces instructor section)
4. FIX 6 — Rewrite marketing copy
5. FIX 3 — Hero card depth
6. FIX 4 — Micro-interactions
7. FIX 7 — Course page attribution

---

*Design Brief v3 — July 2026*
*Stealth mode: no personal names, attribution to CodeinteX as entity*
*Target tone: Corporate + Academic + Practical (reference: Coursera, edX)*
