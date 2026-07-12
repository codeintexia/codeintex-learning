# Design Brief — CodeinteX Learning Platform
## Redesign: Dark Theme → Light Theme (codeintex.com design system)

---

## Context

The current LMS uses a dark navy theme. This brief redesigns it to match the light theme of codeintex.com — consistent professional visual identity across both platforms.

Do NOT change any functional code, routing, content parsing, or component logic.
Only change visual styling: colors, typography, spacing, and layout.

---

## Design Tokens — use these exact values everywhere

```css
:root {
  /* Colors */
  --color-bg-primary: #ffffff;
  --color-bg-secondary: #f8fafc;
  --color-bg-tertiary: #f1f5f9;

  --color-text-primary: #0f172a;
  --color-text-secondary: #475569;
  --color-text-tertiary: #94a3b8;

  --color-accent-navy: #1e3a8a;
  --color-accent-teal: #0d9488;
  --color-accent-teal-light: #f0fdfa;
  --color-accent-teal-hover: #0f766e;

  --color-border: #e2e8f0;
  --color-border-strong: #cbd5e1;

  /* Typography */
  --font-sans: 'Inter', ui-sans-serif, system-ui, sans-serif;

  /* Spacing */
  --content-max-width: 68ch;
  --sidebar-width: 280px;
}
```

---

## Global Changes

### Background and text
- All dark backgrounds (`#0a1628`, `#0d1b2a`, navy, etc.) → `#ffffff` or `#f8fafc`
- All light/white text on dark → `#0f172a`
- Remove all dark mode classes

### Font
- Apply `font-family: 'Inter', ui-sans-serif, system-ui, sans-serif` globally
- Add to `<head>`: `<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">`

---

## Navbar

```
Background: #ffffff
Border-bottom: 1px solid #e2e8f0
Logo: CodeinteX (dark text, existing logo)
Nav links: #475569, hover: #0f172a
CTA button: background #1e3a8a, text white, border-radius 6px, px-4 py-2
Height: 64px
Position: sticky top-0, z-index 50
```

Remove completely:
- "Phase 1: Local MD" badge
- Any debug labels or environment indicators

---

## Homepage — Hero Section

```
Background: #ffffff
Padding: 80px 0

Badge "Kursus Baru Dirilis":
  background: #f0fdfa
  color: #0d9488
  border: 1px solid #99f6e4
  font-size: 12px
  border-radius: 999px
  padding: 4px 12px

Heading H1:
  color: #0f172a
  font-size: 48px
  font-weight: 700
  line-height: 1.15
  
Heading accent word ("— Foundations"):
  color: #0d9488

Body text:
  color: #475569
  font-size: 18px
  line-height: 1.7
  max-width: 560px

Primary button "Mulai Belajar Sekarang":
  background: #1e3a8a
  color: white
  border-radius: 6px
  padding: 12px 24px
  font-weight: 600

Secondary button "Lihat Kurikulum":
  background: transparent
  border: 1.5px solid #1e3a8a
  color: #1e3a8a
  border-radius: 6px
  padding: 12px 24px
  font-weight: 600
```

---

## Homepage — Stats Bar

```
Background: #f8fafc
Border-top: 1px solid #e2e8f0
Border-bottom: 1px solid #e2e8f0
Padding: 40px 0

Number: color #1e3a8a, font-size 32px, font-weight 700
Label: color #64748b, font-size 12px, uppercase, letter-spacing 0.08em
```

---

## Homepage — Module Cards

```
Card background: #ffffff
Card border: 1px solid #e2e8f0
Card border-radius: 8px
Card padding: 24px
Card hover: border-color #0d9488, transition 200ms

Module number: color #94a3b8, font-size 12px, font-weight 500
Module title: color #0f172a, font-size 17px, font-weight 600
Lesson count: color #64748b, font-size 12px, uppercase, letter-spacing 0.06em
Link "Lihat Outline Modul": color #0d9488, font-size 14px, font-weight 500

Section label "STRUKTUR PEMBELAJARAN":
  color: #0d9488
  font-size: 11px
  font-weight: 600
  letter-spacing: 0.1em
  uppercase
```

Remove:
- The "N" Next.js logo from bottom-left corner. Delete it entirely.

---

## Lesson Page — Layout

```
Full layout:
  background: #ffffff
  display: flex
  min-height: 100vh

Sidebar (left):
  width: 280px
  background: #f8fafc
  border-right: 1px solid #e2e8f0
  position: sticky
  top: 64px (below navbar)
  height: calc(100vh - 64px)
  overflow-y: auto
  padding: 24px 0

Content area (right):
  flex: 1
  padding: 48px 64px
  max-width: 860px
  margin: 0 auto
```

---

## Lesson Page — Sidebar

```
Course title:
  color: #0f172a
  font-size: 13px
  font-weight: 600
  padding: 0 20px 16px
  border-bottom: 1px solid #e2e8f0
  margin-bottom: 8px

Module group label:
  color: #94a3b8
  font-size: 11px
  font-weight: 600
  letter-spacing: 0.08em
  uppercase
  padding: 12px 20px 4px

Lesson item (default):
  color: #475569
  font-size: 13px
  padding: 8px 20px
  line-height: 1.4

Lesson item (active/current):
  background: #f0fdfa
  color: #0d9488
  font-weight: 500
  border-left: 2px solid #0d9488
  padding-left: 18px

Lesson item (hover):
  background: #f1f5f9
  color: #0f172a
```

---

## Lesson Page — Breadcrumb

```
Color: #94a3b8
Font-size: 13px
Separator: › (chevron, not dot)
Active/current page: color #0f172a
Padding-bottom: 24px
Border-bottom: 1px solid #e2e8f0
Margin-bottom: 32px
```

---

## Lesson Page — Header

```
Lesson title (H1):
  color: #0f172a
  font-size: 32px
  font-weight: 700
  line-height: 1.25
  margin-bottom: 16px

IMPORTANT: Show the title ONCE only — from frontmatter.
Strip the first H1 from MDX content before rendering.

Metadata row (duration, level):
  color: #64748b
  font-size: 14px
  display: flex
  gap: 16px
  margin-bottom: 40px
  padding-bottom: 24px
  border-bottom: 1px solid #e2e8f0
```

---

## Lesson Page — Body Content (prose)

```css
.prose {
  font-family: 'Inter', ui-sans-serif, system-ui, sans-serif;
  font-size: 18px;
  line-height: 1.85;
  color: #1e293b;
  max-width: 68ch;
}

.prose h2 {
  font-size: 22px;
  font-weight: 700;
  color: #0f172a;
  margin-top: 48px;
  margin-bottom: 16px;
}

.prose h3 {
  font-size: 18px;
  font-weight: 600;
  color: #0f172a;
  margin-top: 32px;
  margin-bottom: 12px;
}

.prose p {
  margin-bottom: 24px;
}

.prose strong {
  color: #0f172a;
  font-weight: 600;
}

.prose blockquote {
  border-left: 3px solid #0d9488;
  padding: 4px 0 4px 20px;
  color: #475569;
  font-style: normal;
  margin: 32px 0;
}

.prose a {
  color: #0d9488;
  text-decoration: underline;
  text-underline-offset: 3px;
}

.prose ul, .prose ol {
  padding-left: 24px;
  margin-bottom: 24px;
}

.prose li {
  margin-bottom: 8px;
}

.prose table {
  width: 100%;
  border-collapse: collapse;
  font-size: 15px;
  margin: 32px 0;
}

.prose th {
  background: #f8fafc;
  color: #0f172a;
  font-weight: 600;
  text-align: left;
  padding: 10px 14px;
  border-bottom: 2px solid #e2e8f0;
}

.prose td {
  padding: 10px 14px;
  border-bottom: 1px solid #e2e8f0;
  color: #334155;
}

.prose code {
  background: #f1f5f9;
  color: #0f172a;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 15px;
}
```

---

## QuickCheck Component

```
Container:
  background: #f0fdfa
  border: 1px solid #99f6e4
  border-radius: 8px
  padding: 24px
  margin: 40px 0

Label "Quick Check":
  color: #0d9488
  font-size: 11px
  font-weight: 700
  letter-spacing: 0.1em
  uppercase
  margin-bottom: 8px

Question text:
  color: #0f172a
  font-size: 16px
  line-height: 1.6
  margin-bottom: 16px

Button "Saya sudah memikirkannya →":
  background: #0d9488
  color: white
  border-radius: 6px
  padding: 10px 20px
  font-size: 14px
  font-weight: 500
  hover: background #0f766e

Checked state message:
  color: #0f766e
  font-size: 14px
  font-weight: 500
```

---

## Diagram Placeholder Component

```
Container:
  background: #f8fafc
  border: 1.5px dashed #cbd5e1
  border-radius: 8px
  padding: 28px
  margin: 40px 0

Icon + title:
  color: #64748b
  font-size: 14px
  font-weight: 600
  margin-bottom: 8px

Spec text:
  color: #94a3b8
  font-size: 13px
  font-style: italic
  line-height: 1.5

Note:
  color: #94a3b8
  font-size: 12px
  margin-top: 8px
```

---

## Reading Progress Bar

```
Position: fixed, top: 0, left: 0
Height: 3px
Background: #0d9488
z-index: 100
Width: controlled by scroll percentage via JavaScript
```

---

## CourseNavigation (prev/next)

```
Container:
  margin-top: 64px
  padding-top: 32px
  border-top: 1px solid #e2e8f0
  display: flex
  justify-content: space-between

Previous link:
  color: #64748b
  font-size: 14px
  hover: color #0f172a
  prefix: ← 

Next link:
  color: #0d9488
  font-size: 14px
  font-weight: 500
  hover: color #0f766e
  suffix: →
```

---

## Footer

```
Background: #f8fafc
Border-top: 1px solid #e2e8f0
Padding: 32px
Text: color #64748b, font-size 13px
Links: color #64748b, hover #0f172a
```

---

## What NOT to change

- All routing and URL structure
- All content parsing logic in lib/content.ts
- All component functionality (QuickCheck state, DiagramRenderer parsing)
- generateStaticParams
- next.config.ts
- package.json dependencies
- All .md content files

---

## Expected result

After applying this brief, the LMS should:
1. Use white/light gray backgrounds throughout
2. Match codeintex.com's professional, clean aesthetic
3. Be comfortable to read for 15+ minutes
4. Feel like the same visual family as codeintex.com
5. No dark navy backgrounds anywhere
6. No debug badges or artifacts

*Brief version: 1.0 | June 2026*
