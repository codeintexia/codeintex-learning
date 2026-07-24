# Design Brief v4 — CodeinteX Learning Platform
## Multi-Course Homepage: Category Navigation + Placeholders

---

## IMPORTANT RULES

- Do NOT change lesson pages, sidebar, or any existing components
- Do NOT change routing or content parsing logic
- Do NOT display any personal name
- Attribution always to "CodeinteX" as entity
- All new UI elements follow existing design tokens (teal #0d9488, navy #1e3a8a, white #ffffff)

---

## CONTEXT

The homepage currently shows one course. It needs to be redesigned to show a multi-course catalog with:
- Three category tabs as primary navigation
- 6 course cards total (1 live + 5 placeholders)
- Domain tags as secondary metadata on each card

---

## NEW HOMEPAGE STRUCTURE

Replace the current "Kurikulum Human-Centered AI" section entirely with this new structure.

Keep everything above it (hero, stats bar, learning outcomes, institutional trust block).

---

## COMPONENT 1 — Category Navigation Tabs

Place this immediately after the institutional trust block, before the course grid.

```
Container:
  padding: 64px 0 0
  text-align: center

Section label above tabs:
  text: "JALUR PEMBELAJARAN"
  color: #0d9488
  font-size: 11px
  font-weight: 700
  letter-spacing: 0.1em
  text-transform: uppercase
  margin-bottom: 16px

Heading:
  text: "Pilih jalur yang sesuai dengan tujuanmu"
  color: #0f172a
  font-size: 28px
  font-weight: 700
  margin-bottom: 40px

Tab container:
  display: inline-flex
  background: #f1f5f9
  border-radius: 12px
  padding: 4px
  gap: 4px
  margin-bottom: 48px

Three tabs — default state:
  background: transparent
  color: #64748b
  font-size: 14px
  font-weight: 500
  padding: 10px 24px
  border-radius: 8px
  cursor: pointer
  transition: all 150ms ease

Tab — active state:
  background: #ffffff
  color: #0f172a
  font-weight: 600
  box-shadow: 0 1px 4px rgba(0,0,0,0.1)

Tab 1 (default active):
  Label: "Literacy"
  Subtitle below label: "Pemahaman konsep dan lanskap AI"
  Subtitle: font-size 11px, color #94a3b8, font-weight 400

Tab 2:
  Label: "Competency"
  Subtitle: "Kemampuan terverifikasi dan tersertifikasi"

Tab 3:
  Label: "Specialization"
  Subtitle: "Keahlian mendalam di domain spesifik"
```

Tab behavior:
- Clicking a tab filters the course grid below to show only courses in that category
- Default: show "Literacy" tab active, show all courses (since all 5 placeholders are Competency, show them greyed out or with a note)
- Actually: show ALL courses regardless of tab for now, but highlight which category each belongs to via a badge on the card
- Add "Semua" tab as first tab so learner can see everything at once

Revised tab order:
```
[ Semua ] [ Literacy ] [ Competency ] [ Specialization ]
```
"Semua" is active by default and shows all 6 cards.

---

## COMPONENT 2 — Course Grid

```
Grid:
  display: grid
  grid-template-columns: repeat(3, 1fr)
  gap: 24px
  padding: 0 0 64px

Responsive:
  2 columns on tablet
  1 column on mobile
```

---

## COMPONENT 3 — Course Card (Live)

For the existing HCAI Foundations course:

```
Card container:
  background: #ffffff
  border: 1px solid #e2e8f0
  border-radius: 12px
  overflow: hidden
  cursor: pointer
  transition: all 200ms ease
  hover: transform translateY(-3px)
  hover: box-shadow 0 8px 24px rgba(0,0,0,0.1)
  hover: border-color #0d9488

Top color bar:
  height: 4px
  background: linear-gradient(90deg, #0d9488, #14b8a6)
  width: 100%

Card body:
  padding: 20px

Category badge (top of card):
  text: "Literacy"
  background: #f0fdfa
  color: #0d9488
  font-size: 10px
  font-weight: 700
  letter-spacing: 0.08em
  text-transform: uppercase
  padding: 2px 8px
  border-radius: 999px
  display: inline-block
  margin-bottom: 12px

Course title:
  text: "Human-Centered AI — Foundations"
  color: #0f172a
  font-size: 16px
  font-weight: 700
  line-height: 1.3
  margin-bottom: 8px

Course description (1 line):
  text: "Merancang sistem AI yang benar-benar bekerja untuk manusia."
  color: #64748b
  font-size: 13px
  line-height: 1.5
  margin-bottom: 16px

Metadata row:
  display: flex
  gap: 12px
  flex-wrap: wrap
  margin-bottom: 16px

  Each metadata item:
    color: #94a3b8
    font-size: 12px
    display: flex
    align-items: center
    gap: 4px

  Items to show:
    "6 Modul"
    "25 Lesson"
    "6 Jam"

Domain tag:
  text: "AI & Kecerdasan Buatan"
  background: #f8fafc
  border: 1px solid #e2e8f0
  color: #64748b
  font-size: 11px
  padding: 2px 8px
  border-radius: 4px
  display: inline-block
  margin-bottom: 16px

Card footer:
  display: flex
  align-items: center
  justify-content: space-between
  padding-top: 16px
  border-top: 1px solid #f1f5f9

  Left: Status badge
    text: "Tersedia Sekarang"
    background: #f0fdfa
    color: #0d9488
    font-size: 11px
    font-weight: 600
    padding: 3px 10px
    border-radius: 999px

  Right: CTA
    text: "Mulai Belajar →"
    color: #0d9488
    font-size: 13px
    font-weight: 600
```

---

## COMPONENT 4 — Course Card (Placeholder)

Five placeholder cards. All in "Competency" category.

```
Card container:
  Same dimensions as live card
  background: #fafafa
  border: 1px solid #e2e8f0
  border-radius: 12px
  overflow: hidden
  opacity: 0.85
  cursor: default (not clickable)

Top color bar:
  height: 4px
  background: #e2e8f0 (grey, not teal — not yet available)
  width: 100%

Card body:
  padding: 20px

Category badge:
  text: "Competency"
  background: #f1f5f9
  color: #94a3b8
  Same styling as live card badge

Course titles (use exactly these):
  Card 2: "AI untuk Proses Data"
  Card 3: "AI untuk Pengalaman Pelanggan"
  Card 4: "AI untuk Keamanan Informasi"
  Card 5: "AI untuk Strategi Metode Pembelajaran"
  Card 6: "AI untuk Pengelolaan Pelanggan"

  title styling:
    color: #334155
    font-size: 16px
    font-weight: 700
    line-height: 1.3
    margin-bottom: 8px

Description placeholder:
  text: "Materi sedang dalam pengembangan. Daftarkan dirimu untuk mendapat notifikasi saat tersedia."
  color: #94a3b8
  font-size: 13px
  line-height: 1.5
  margin-bottom: 16px

Domain tag:
  text: "AI & Kecerdasan Buatan"
  Same styling as live card

Card footer:
  display: flex
  align-items: center
  justify-content: space-between
  padding-top: 16px
  border-top: 1px solid #f1f5f9

  Left: Status badge
    text: "Dalam Pengembangan"
    background: #fef9c3
    color: #854d0e
    font-size: 11px
    font-weight: 600
    padding: 3px 10px
    border-radius: 999px

  Right: No CTA (not clickable)
    text: "Segera Hadir"
    color: #94a3b8
    font-size: 13px
```

---

## COMPONENT 5 — Tab filtering behavior (JavaScript)

```javascript
// Simple tab filter — no framework needed
// Add data-category attribute to each card:
// Live card: data-category="literacy"
// Placeholder cards: data-category="competency"

// Tab click handler:
// "Semua" → show all cards
// "Literacy" → show only literacy cards
// "Competency" → show only competency cards
// "Specialization" → show message: 
//   "Jalur Spesialisasi sedang dalam pengembangan. 
//    Tersedia setelah kamu menyelesaikan jalur Competency."
//   Center this message in the grid area, styled in #64748b
```

---

## REMOVE from current homepage

Remove entirely:
- Current "Kurikulum Human-Centered AI" section with the 6 module cards
- "Mulai Petualangan Belajarmu →" bottom CTA button

Replace with the new structure above.

---

## KEEP from current homepage

Keep exactly as-is:
- Navbar
- Hero section with course preview card
- Stats bar (6, 25, 6 Jam, 100%)
- "Yang akan kamu kuasai" section
- Institutional trust block ("Dikembangkan oleh CodeinteX")
- Footer

---

## What NOT to change

- Lesson pages
- Course detail/syllabus page
- Sidebar navigation
- Any routing or content logic
- package.json
- Any .md files
- /docs folder

---

*Design Brief v4 — July 2026*
*Goal: Multi-course homepage that scales from 6 to 60+ courses without restructuring*
