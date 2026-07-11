# Design Brief v2 — CodeinteX Learning Platform
## Closing the Gap to God Tier

---

## IMPORTANT RULES

- Do NOT change any routing, content parsing, or component logic
- Do NOT change any .md content files
- Do NOT change package.json or next.config.ts
- Only change visual styling and layout
- Every change must be in English code comments

---

## FIX 1 — Homepage Hero: Fill the empty right side

The right half of the hero is completely empty. This must be filled.

Add a visual element to the right side of the hero — a stylized course preview card:

```
Layout: flex row, left 55% text + right 45% visual
Gap: 64px

Right side visual — a floating course card:
  background: white
  border: 1px solid #e2e8f0
  border-radius: 12px
  padding: 24px
  box-shadow: 0 4px 24px rgba(0,0,0,0.08)
  max-width: 340px
  transform: rotate(1.5deg) (subtle tilt for visual interest)

Inside the card:
  - Badge: "Human-Centered AI" in teal
  - Progress bar: thin teal bar showing 0% progress
  - Text: "6 Modul · 25 Lesson · 6 Jam"
  - Three lesson preview items (just text, no links):
      "Ketika AI Gagal Bukan Karena Bodoh..."
      "Dari AI-Centered ke Human-Centered..."
      "Dua Sumbu Shneiderman..."
  - Each item prefixed with a small teal circle number
  - Dimmed overlay on items 2 and 3 (suggesting more content below)
```

---

## FIX 2 — Homepage: Add "Yang Akan Kamu Kuasai" section

Add this section BETWEEN the stats bar and the module cards:

```
Section background: #f8fafc
Padding: 64px 0

Section label: "LEARNING OUTCOMES"
  color: #0d9488
  font-size: 11px
  font-weight: 700
  letter-spacing: 0.1em
  uppercase

Heading: "Yang akan kamu kuasai"
  color: #0f172a
  font-size: 28px
  font-weight: 700
  text-align: center
  margin-bottom: 40px

4 outcome cards in a 2x2 grid:
  Card 1: "Evaluasi sistem AI" — menggunakan kerangka 4 prinsip HCAI
  Card 2: "Desain dengan IFRAME" — metodologi eksklusif CodeinteX
  Card 3: "Deteksi dan tangani bias" — dalam konteks Asia Tenggara
  Card 4: "Audit produk AI nyata" — dengan checklist yang bisa langsung dipakai

Each card:
  background: white
  border: 1px solid #e2e8f0
  border-radius: 8px
  padding: 20px 24px
  display: flex
  align-items: flex-start
  gap: 12px
  
  Icon: teal checkmark circle (✓) — 20px, color #0d9488
  Title: color #0f172a, font-size 15px, font-weight 600
  Description: color #64748b, font-size 14px, line-height 1.5
```

---

## FIX 3 — Homepage Module Cards: Make them more premium

Current cards are too flat. Upgrade:

```
Remove: "Lihat Outline Modul →" link from each card (it's redundant, the whole card is clickable)

Make the entire card clickable — cursor: pointer, link to /courses/hcai-foundations/[module]

Add hover state:
  border-color: #0d9488
  box-shadow: 0 4px 12px rgba(13,148,136,0.1)
  transform: translateY(-2px)
  transition: all 200ms ease

Add to each card — a Bloom's level badge:
  Module 1-2: "Remember · Understand" — gray pill
  Module 3: "Understand" — gray pill
  Module 4: "Analyze" — gray pill
  Module 5: "Apply" — gray pill
  Module 6: "Evaluate" — gray pill
  
  Badge styling:
    background: #f1f5f9
    color: #64748b
    font-size: 10px
    padding: 2px 8px
    border-radius: 999px
    font-weight: 500
    margin-top: 12px
```

---

## FIX 4 — Lesson Page: Fix sidebar

Sidebar is too narrow and text too small. Fix:

```
Sidebar width: 300px (increase from current)
Sidebar padding: 20px 0

Course title at top of sidebar:
  text: "HCAI Foundations"
  color: #0f172a
  font-size: 13px
  font-weight: 700
  padding: 0 16px 16px
  border-bottom: 1px solid #e2e8f0
  display: flex
  align-items: center
  gap: 8px
  
  Add small teal dot before text: width 6px, height 6px, background #0d9488, border-radius 50%

Module group label:
  font-size: 11px
  font-weight: 700
  color: #94a3b8
  letter-spacing: 0.08em
  uppercase
  padding: 16px 16px 6px

Lesson item (default):
  font-size: 13px
  color: #64748b
  padding: 7px 16px
  line-height: 1.4
  border-left: 2px solid transparent
  cursor: pointer

Lesson item (active):
  background: #f0fdfa
  color: #0d9488
  font-weight: 600
  border-left: 2px solid #0d9488
  font-size: 13px

Lesson item (hover):
  background: #f8fafc
  color: #334155
  border-left: 2px solid #e2e8f0
```

---

## FIX 5 — Lesson Page: Fix content width and double title

Two separate fixes:

**5A — Remove double title:**
The lesson title appears twice: once from the page component, once from the MDX H1.
In LessonRenderer, before rendering the markdown content:
- Find and remove the first H1 element from the content string
- Use regex: `content.replace(/^#\s+.+\n?/m, '').trimStart()`
- The page component already renders the title from frontmatter — that's the only title needed

**5B — Fix content width:**
```
Content area max-width: 720px (not full width)
Centered within the content column
Padding: 48px 64px on desktop, 24px 20px on mobile
```

---

## FIX 6 — Lesson Page: Upgrade Quick Check component

Current QuickCheck looks like a plain div. Target: feels like an intentional, premium interactive element.

```
Container:
  background: linear-gradient(135deg, #f0fdfa 0%, #e6fffa 100%)
  border: 1.5px solid #5eead4
  border-radius: 12px
  padding: 28px
  margin: 48px 0
  position: relative
  overflow: hidden

Add decorative element — top right corner:
  width: 80px
  height: 80px
  background: radial-gradient(circle, rgba(13,148,136,0.08) 0%, transparent 70%)
  position: absolute
  top: -20px
  right: -20px
  border-radius: 50%

Label "Quick Check":
  display: flex
  align-items: center
  gap: 8px
  margin-bottom: 12px
  
  Icon: lightning bolt emoji ⚡ or a small teal SVG icon
  Text: color #0d9488, font-size 11px, font-weight 700, uppercase, letter-spacing 0.1em

Question text:
  color: #0f172a
  font-size: 16px
  line-height: 1.65
  font-weight: 500
  margin-bottom: 20px

Button (unchecked state):
  background: #0d9488
  color: white
  border-radius: 8px
  padding: 10px 20px
  font-size: 14px
  font-weight: 600
  border: none
  cursor: pointer
  transition: background 150ms
  hover: background #0f766e
  text: "Saya sudah memikirkannya →"

Checked state:
  Remove button
  Show: 
    "✓ Bagus — lanjutkan ke analisis kasus."
    color: #0f766e
    font-size: 14px
    font-weight: 600
    display: flex
    align-items: center
    gap: 8px
```

---

## FIX 7 — Lesson Page: Add reading progress bar

A thin teal line fixed at the very top of the viewport that fills as user scrolls:

```javascript
// Add to lesson page as client component
'use client'
import { useEffect, useState } from 'react'

export function ReadingProgress() {
  const [progress, setProgress] = useState(0)
  
  useEffect(() => {
    const updateProgress = () => {
      const scrollTop = window.scrollY
      const docHeight = document.documentElement.scrollHeight - window.innerHeight
      const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0
      setProgress(progress)
    }
    window.addEventListener('scroll', updateProgress)
    return () => window.removeEventListener('scroll', updateProgress)
  }, [])
  
  return (
    <div
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        height: '3px',
        width: `${progress}%`,
        backgroundColor: '#0d9488',
        zIndex: 100,
        transition: 'width 100ms linear',
      }}
    />
  )
}
```

Add `<ReadingProgress />` inside the lesson page layout, outside the scrollable content area.

---

## FIX 8 — CourseNavigation: Show lesson title, not just arrow

The prev/next navigation at bottom of lesson shows only "→". Fix:

```
Container:
  margin-top: 80px
  padding-top: 32px
  border-top: 1px solid #e2e8f0
  display: grid
  grid-template-columns: 1fr 1fr
  gap: 16px

Previous card (if exists):
  border: 1px solid #e2e8f0
  border-radius: 8px
  padding: 16px 20px
  cursor: pointer
  hover: border-color #0d9488
  
  Label: "← Sebelumnya"
    color: #94a3b8
    font-size: 12px
    font-weight: 500
    margin-bottom: 4px
  
  Title: [previous lesson title]
    color: #0f172a
    font-size: 14px
    font-weight: 600
    line-height: 1.3

Next card (if exists):
  border: 1px solid #e2e8f0
  border-radius: 8px
  padding: 16px 20px
  cursor: pointer
  text-align: right
  hover: border-color #0d9488
  background: #f8fafc (subtle differentiation)
  
  Label: "Berikutnya →"
    color: #0d9488
    font-size: 12px
    font-weight: 500
    margin-bottom: 4px
  
  Title: [next lesson title]
    color: #0f172a
    font-size: 14px
    font-weight: 600
    line-height: 1.3
```

---

## What NOT to change

- All routing and URL structure
- Content parsing in lib/content.ts
- generateStaticParams
- MD content files
- package.json
- next.config.ts
- tailwind.config.ts
- Anything in the /docs folder

---

## Priority order

Execute in this order. Stop and verify each fix before moving to the next:

1. FIX 5A — Double title (most annoying bug)
2. FIX 7 — Reading progress bar (quick win)
3. FIX 6 — Quick Check upgrade
4. FIX 4 — Sidebar improvement
5. FIX 8 — CourseNavigation with titles
6. FIX 1 — Homepage hero right side
7. FIX 2 — Learning outcomes section
8. FIX 3 — Module card upgrade

---

*Design Brief v2 — July 2026*
*Target: Close the gap between current state and Coursera/edX visual quality*
