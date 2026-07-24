# Design Brief v5 — CodeinteX Learning Platform
## Hero Redesign: Single Course → Multi-Course Platform

---

## IMPORTANT RULES

- Do NOT change anything below the hero section
- Do NOT change lesson pages, sidebar, or course detail pages
- Do NOT change routing or content logic
- Do NOT display any personal name
- Keep all existing design tokens (teal #0d9488, navy #1e3a8a)

---

## WHAT TO CHANGE

Only the hero section (the very top section above the stats bar).
Everything else stays exactly as-is.

---

## NEW HERO SECTION

Replace the entire current hero section with this:

```
Container:
  background: #ffffff
  padding: 80px 0 72px
  max-width: 1200px
  margin: 0 auto
  display: grid
  grid-template-columns: 1fr 1fr
  gap: 80px
  align-items: center
  padding-left: 40px
  padding-right: 40px
```

---

### LEFT SIDE — Platform messaging

```
Badge (top):
  text: "✦ Kursus Baru · Gratis & Terbuka"
  background: #f0fdfa
  color: #0d9488
  border: 1px solid #99f6e4
  font-size: 12px
  font-weight: 500
  padding: 4px 14px
  border-radius: 999px
  display: inline-block
  margin-bottom: 24px

Heading H1:
  Line 1: "Kuasai AI yang"
  Line 2: "Berpusat pada Manusia"
  color: #0f172a
  font-size: 44px
  font-weight: 800
  line-height: 1.15
  margin-bottom: 20px

  No teal accent on heading — clean, authoritative

Subheading:
  text: "Kursus berbasis penelitian akademis untuk
  profesional yang ingin merancang, mengevaluasi,
  dan mengaudit sistem AI secara bertanggung jawab."
  color: #475569
  font-size: 17px
  line-height: 1.7
  max-width: 480px
  margin-bottom: 32px

Three proof points (horizontal row):
  display: flex
  gap: 20px
  flex-wrap: wrap
  margin-bottom: 36px

  Each proof point:
    display: flex
    align-items: center
    gap: 6px
    font-size: 13px
    color: #64748b

  Items:
    "✓ Referensi akademis terverifikasi"
    "✓ Metodologi IFRAME eksklusif"
    "✓ 100% gratis & terbuka"

CTA buttons (horizontal):
  display: flex
  gap: 12px
  align-items: center

  Primary button:
    text: "Mulai Belajar — Gratis"
    background: #1e3a8a
    color: white
    padding: 12px 24px
    border-radius: 8px
    font-size: 15px
    font-weight: 600
    border: none
    cursor: pointer
    transition: background 150ms
    hover: background #1e40af

  Secondary button:
    text: "Lihat Semua Kursus"
    background: transparent
    color: #1e3a8a
    border: 1.5px solid #1e3a8a
    padding: 12px 24px
    border-radius: 8px
    font-size: 15px
    font-weight: 600
    cursor: pointer
    hover: background #f8fafc
    onclick: scroll to course grid section
```

---

### RIGHT SIDE — Stacked course cards visual

```
Container:
  position: relative
  width: 100%
  height: 320px

Three stacked cards — positioned absolutely to create depth:

CARD 3 (back, most tilted):
  position: absolute
  top: 20px
  left: 20px
  right: -10px
  transform: rotate(3deg)
  background: #e2e8f0
  border-radius: 12px
  height: 200px
  opacity: 0.5
  z-index: 1

CARD 2 (middle):
  position: absolute
  top: 10px
  left: 10px
  right: -5px
  transform: rotate(1.5deg)
  background: #f1f5f9
  border: 1px solid #e2e8f0
  border-radius: 12px
  height: 210px
  opacity: 0.75
  z-index: 2

CARD 1 (front, main):
  position: absolute
  top: 0
  left: 0
  right: 0
  transform: rotate(0deg)
  background: #ffffff
  border: 1px solid #e2e8f0
  border-radius: 12px
  box-shadow: 0 8px 32px rgba(0,0,0,0.12)
  z-index: 3
  padding: 20px

  Inside CARD 1:
    Top teal bar:
      height: 4px
      background: linear-gradient(90deg, #0d9488, #14b8a6)
      border-radius: 12px 12px 0 0
      margin: -20px -20px 16px -20px

    Category badge:
      text: "Literacy"
      background: #f0fdfa
      color: #0d9488
      font-size: 10px
      font-weight: 700
      letter-spacing: 0.08em
      text-transform: uppercase
      padding: 2px 8px
      border-radius: 999px
      margin-bottom: 8px

    Course title:
      text: "Human-Centered AI — Foundations"
      color: #0f172a
      font-size: 14px
      font-weight: 700
      margin-bottom: 8px

    Metadata row:
      color: #94a3b8
      font-size: 12px
      "6 Modul · 25 Lesson · 6 Jam"
      margin-bottom: 12px

    Three lesson preview items:
      Each: display flex, align-items center, gap 8px

      Number circle:
        width: 18px
        height: 18px
        background: #f0fdfa
        color: #0d9488
        border-radius: 50%
        font-size: 10px
        font-weight: 700
        display flex
        align-items: center
        justify-content: center
        flex-shrink: 0

      Lesson title:
        font-size: 12px
        color: #475569
        line-height: 1.3

      Item 1: "Ketika AI Gagal Bukan Karena Bodoh..."
      Item 2: "Dari AI-Centered ke Human-Centered..." (opacity 0.6)
      Item 3: "Dua Sumbu Shneiderman..." (opacity 0.4)
      margin-bottom: 6px each

    Status badge at bottom:
      text: "Tersedia Sekarang"
      background: #f0fdfa
      color: #0d9488
      font-size: 11px
      font-weight: 600
      padding: 3px 10px
      border-radius: 999px
      margin-top: 12px

Small label below stacked cards:
  text: "6 kursus tersedia · 5 dalam pengembangan"
  color: #94a3b8
  font-size: 12px
  text-align: center
  margin-top: 16px
  position: absolute
  bottom: 0
  left: 0
  right: 0
```

---

## MOBILE BEHAVIOR

On screens smaller than 768px:
- Hide right side stacked cards entirely
- Left side takes full width
- Adjust heading to font-size 32px
- Three proof points become a vertical list

---

## REMOVE

Remove from current hero:
- "Kursus Baru Dirilis" pill badge (replaced by new badge)
- "Human-Centered AI — Foundations" as the main H1
- "— Foundations" teal accent
- "Merancang sistem AI..." body text
- Single course preview card on the right
- "Mulai Belajar Sekarang (Gratis) →" and "Lihat Kurikulum" buttons

---

## KEEP EXACTLY AS-IS

- Stats bar (6 · 25 · 6 Jam · 100%)
- "Yang akan kamu kuasai" section
- Institutional trust block
- "JALUR PEMBELAJARAN" tab navigation
- 6 course cards grid
- Footer

---

*Design Brief v5 — July 2026*
*Goal: Reposition hero from single-course to multi-course platform*
*Reference: Coursera, edX homepage hero pattern*
