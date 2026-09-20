# Product Experience System — Decision Log

- **Project:** CodeInteX
- **Status:** ACTIVE
- **Document type:** Authoritative decision history
- **Created:** 2026-09-19

---

## 0. Purpose

Dokumen ini mencatat keputusan material Product Experience System (PES) dari waktu ke waktu.

Decision Log digunakan untuk:

- mengetahui keputusan yang sedang berlaku;
- membedakan `LOCKED`, `PROVISIONAL`, `OPEN`, dan `DEPRECATED`;
- mencatat rationale dan evidence;
- menghindari keputusan lintas-chat yang saling bertentangan;
- mencatat perubahan atau penggantian keputusan;
- menyediakan konteks ringkas untuk manusia dan AI coding agents.

Decision Log tidak menggantikan normative specification.

Normative specification tetap berada pada dokumen PES terkait.

---

## 1. Decision States

### LOCKED

Keputusan telah memiliki evidence dan constraint yang cukup kuat untuk menjadi normative baseline.

Perubahan harus dilakukan secara eksplisit dan dicatat di Decision Log.

### PROVISIONAL

Keputusan terbaik berdasarkan evidence saat ini, tetapi belum cukup diuji untuk dikunci.

### OPEN

Belum ada keputusan final atau evidence masih kurang.

### DEPRECATED

Keputusan pernah berlaku tetapi sudah tidak menjadi arah resmi.

Jika relevan, decision entry harus menunjuk keputusan penggantinya.

---

## 2. Decision Record Schema

Setiap significant decision menggunakan format berikut:

~~~text
ID
Date
Status
Scope
Decision
Context
Evidence
Alternatives
Rationale
Risks
Migration impact
Supersedes
Superseded by
Related artifacts
~~~

Tidak semua field wajib memiliki isi jika tidak relevan.

---

# CURRENT DECISIONS

## PES-001 — PES is a cross-cutting CodeInteX capability

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** Architecture

### Decision

PES adalah capability lintas-produk CodeInteX dan bukan design system lokal milik satu produk.

### Rationale

PES harus dapat digunakan oleh LMS dan produk CodeInteX lain tanpa membuat parallel design foundations.

### Related artifacts

- `PES-FOUNDATION-DECISION-MODEL-v0.1.md`
- `PES-CONSUMPTION-CONTRACT-v0.1.md`

---

## PES-002 — PES remains implementation-independent at Core level

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** Architecture

### Decision

PES Core tidak bergantung secara konseptual pada React, Next.js, Wagtail, Tailwind CSS, shadcn/ui, Base UI, atau library implementasi tertentu.

### Rationale

Experience semantics dan contracts harus dapat bertahan ketika implementation technology berubah.

---

## PES-003 — Canonical PES uses seven conceptual layers

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** PES architecture

### Decision

Canonical PES layer model:

~~~text
L7 Experience Governance
L6 AI / Agent Experience
L5 Domain Experience Patterns
L4 General UX Patterns
L3 Component System
L2 Foundations
L1 Experience Constitution
~~~

### Rationale

Layering memisahkan principles, implementation-independent experience contracts, domain concerns, dan governance.

---

## PES-004 — Semantic tokens are the primary portability boundary

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** Foundations

### Decision

Visual implementation harus menggunakan semantic-token architecture dengan hierarchy:

~~~text
Reference Tokens
→ Semantic Tokens
→ Component Tokens
~~~

### Rationale

Semantic tokens memungkinkan theme, brand, dan implementation technology berubah tanpa menyebarkan raw visual values ke product code.

---

## PES-005 — Theme is separated from product logic

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** Theme architecture

### Decision

Theme dapat mengubah visual/presentational characteristics tetapi tidak boleh mengubah:

- semantic meaning;
- accessibility semantics;
- keyboard behavior;
- information hierarchy;
- workflow correctness.

### Rationale

Themeability harus meningkatkan portability tanpa mengubah product behavior.

---

## PES-006 — WCAG 2.2 AA is the minimum accessibility baseline

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** Accessibility

### Decision

WCAG 2.2 AA menjadi minimum accessibility baseline PES.

Automated accessibility testing tidak dianggap cukup untuk critical workflows.

---

## PES-007 — Product-specific experience is separated from PES Core

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** Architecture

### Decision

Domain-specific UX berada pada Product Experience Profile.

Contoh:

~~~text
PES Core
→ LMS Experience Profile
→ Web Implementation Profile
→ LMS Product
~~~

### Rationale

Domain semantics harus dapat berkembang tanpa mencemari core lintas-produk.

---

## PES-008 — LMS is a reference consumer, not the owner of PES

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** LMS integration

### Decision

LMS menjadi salah satu reference consumers pertama PES.

LMS tidak boleh menciptakan parallel:

- color system;
- typography system;
- spacing system;
- radius/elevation grammar;
- button grammar;
- icon grammar;
- motion vocabulary.

### Rationale

LMS digunakan untuk stress-test PES, bukan menjadi sumber visual foundation independen.

---

## PES-009 — Backend models do not directly become UI contracts

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** Frontend/backend boundary

### Decision

Canonical data flow:

~~~text
Backend Domain Model
→ API / Domain Contract
→ Frontend Adapter / View Model
→ PES-aware Product Component
~~~

### Rationale

Mengurangi coupling dan memungkinkan backend, frontend, serta PES berevolusi secara independen.

---

## PES-010 — Udacity is the primary LMS learner-experience benchmark

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** Benchmarking

### Decision

Udacity digunakan sebagai primary benchmark untuk learner experience, khususnya:

- learner dashboard;
- curriculum navigation;
- lesson continuity;
- progress;
- resume learning;
- assessment/projects;
- learning resources.

### Constraint

Udacity bukan visual template dan bukan authority untuk:

- CodeInteX branding;
- PES architecture;
- accessibility standard;
- technical stack.

### Rationale

Benchmark digunakan untuk mempelajari experience patterns, bukan melakukan visual imitation.

---

## PES-011 — Benchmark decisions require triangulation

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** Benchmarking

### Decision

Tidak ada satu benchmark product yang dianggap authoritative.

Canonical model:

~~~text
Primary benchmark
+ Specialist benchmarks
+ HCI / accessibility evidence
+ Actual user validation
~~~

---

## PES-012 — AI coding agents are PES consumers

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** AI-assisted development

### Decision

AI coding agents wajib mengikuti normative PES artifacts dan tidak boleh:

- membuat parallel design system;
- memperkenalkan arbitrary raw visual values;
- mengabaikan accessibility;
- menambah overlapping UI libraries tanpa justification;
- mengubah LOCKED PES decision secara diam-diam.

---

## PES-013 — PES uses explicit change governance

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** Governance

### Decision

Lifecycle reusable PES artifacts:

~~~text
EXPERIMENTAL
→ CANDIDATE
→ STABLE
→ DEPRECATED
→ REMOVED
~~~

Decision state:

~~~text
LOCKED
PROVISIONAL
OPEN
DEPRECATED
~~~

---

## PES-014 — PES v1.0 requires real-product validation

- **Date:** 2026-09-19
- **Status:** LOCKED
- **Scope:** Release governance

### Decision

PES tidak dianggap v1.0 hanya karena dokumentasi selesai.

Minimum proof harus mencakup:

- substantial real product implementation;
- at least two meaningfully different themes;
- responsive validation;
- keyboard usability;
- accessibility validation;
- loading/empty/error/partial states;
- component and pattern documentation;
- AI coding-agent consumption test;
- theme switching tanpa product-logic rewrite.

---

## PES-015 — LMS Experience Profile v0.1 normative baseline

- **Date:** 2026-09-19
- **Status:** LOCKED

`LMS-EXPERIENCE-PROFILE-v0.1.md` is the authorized current
learner-domain experience baseline for CodeInteX LMS.

It consumes PES Core and translates validated learner-experience
evidence into normative LMS contracts.

Implementation must not override its LOCKED learner semantics through
local UI decisions.

---

## PES-016 — Web Implementation Profile v0.1 implementation baseline

- **Date:** 2026-09-19
- **Status:** LOCKED

`WEB-IMPLEMENTATION-PROFILE-v0.1.md` is the authorized current web
implementation baseline.

Technology choices remain subordinate to PES Core and the LMS
Experience Profile.

Reference implementation may expose contradictions, but implementation
does not become a higher-authority source merely because code exists.

---

## PES-017 — Next.js, React, and TypeScript web runtime baseline

- **Date:** 2026-09-19
- **Status:** LOCKED

The current web baseline uses:

- supported Next.js 16.x release line;
- App Router;
- React 19.x compatible with the selected supported Next.js release;
- TypeScript.

Server Components are the default execution boundary.

Client Components are introduced only where client execution is
required.

Exact patch versions remain operational dependency-management
decisions and must follow supported/security-patched releases.

**Supersedes:** `PES-P001`

---

## PES-018 — Tailwind CSS implementation role

- **Date:** 2026-09-19
- **Status:** LOCKED

Tailwind CSS 4.x is the primary styling implementation engine for the
current web baseline.

Tailwind is not the source of truth for CodeInteX design semantics.

PES semantic tokens remain authoritative, with Tailwind consuming the
approved web representation of those semantics.

Exact breakpoint values and token serialization remain OPEN.

**Supersedes:** `PES-P002`

---

## PES-019 — Base UI default behavioral primitive foundation

- **Date:** 2026-09-19
- **Status:** LOCKED

Base UI is the default behavioral primitive foundation for new
CodeInteX web components where an appropriate primitive exists.

Product/domain screens should normally consume CodeInteX-owned
components rather than importing Base UI primitives directly.

Base UI remains an implementation dependency, not a PES authority.

**Supersedes:** `PES-P004`

---

## PES-020 — shadcn-derived source is CodeInteX-owned implementation

- **Date:** 2026-09-19
- **Status:** LOCKED

shadcn/ui may be used as a bootstrap/source for CodeInteX components.

Adopted/generated source becomes CodeInteX-owned implementation code
and may be modified, simplified, replaced, or removed.

shadcn/ui is not treated as a parallel design-system authority.

For the current baseline, shadcn-derived components may use Base UI
primitives underneath the CodeInteX-owned component boundary.

**Supersedes:** `PES-P003`

---

## PES-021 — Storybook component workbench baseline

- **Date:** 2026-09-19
- **Status:** LOCKED

Storybook is the standard isolated component workbench for the current
CodeInteX web implementation baseline.

Its roles include:

- component development;
- meaningful state coverage;
- interaction validation;
- automated accessibility checks;
- responsive inspection;
- component implementation documentation.

For standard new Next.js App Router implementation, the current
preferred adapter is `@storybook/nextjs-vite`.

Storybook stories are validation fixtures and executable examples;
they are not higher authority than PES/component contracts.

**Supersedes:** `PES-P007`

---

## PES-022 — Playwright browser E2E baseline

- **Date:** 2026-09-19
- **Status:** LOCKED

Playwright is the standard browser E2E framework for the current web
baseline.

It is used to protect representative critical learner workflows and
important failure/recovery paths.

Tests should prefer user-perceivable semantic locators such as role,
accessible name, and label over brittle implementation selectors.

Exact browser/CI execution matrix remains PROVISIONAL.

---

## PES-023 — Automated E2E accessibility baseline

- **Date:** 2026-09-19
- **Status:** LOCKED

`@axe-core/playwright` is the standard automated E2E accessibility
capability for the current web baseline.

It complements:

- Storybook accessibility checks;
- static analysis;
- manual accessibility validation.

Automated accessibility success does not establish WCAG conformance.

---

# PROVISIONAL DECISIONS

## PES-P005 — Motion as default motion implementation

- **Date:** 2026-09-19
- **Status:** PROVISIONAL
- **Scope:** Motion implementation

---
- **Current interpretation (2026-09-19):** Motion remains PROVISIONAL and capability-triggered; it is not required by default. Prefer CSS/platform behavior when sufficient.

## PES-P006 — Lucide as default icon implementation

- **Date:** 2026-09-19
- **Status:** PROVISIONAL
- **Scope:** Iconography implementation

---
- **Current interpretation (2026-09-19):** Lucide remains a PROVISIONAL default candidate pending final visual-language validation.

# OPEN DECISIONS

## PES-O001 — Final visual language

- **Date:** 2026-09-19
- **Status:** OPEN

Includes:

- typography;
- color;
- shape;
- elevation;
- density;
- visual hierarchy.

---

## PES-O002 — Exact token serialization and file structure

- **Date:** 2026-09-19
- **Status:** OPEN

DTCG-compatible serialization remains a candidate.

---

## PES-O003 — Exact theme runtime architecture

- **Date:** 2026-09-19
- **Status:** OPEN

Includes:

- build-time themes;
- runtime themes;
- multi-brand;
- theme packages;
- theme-provider strategy.

---

## PES-O004 — Final LMS domain component taxonomy

- **Date:** 2026-09-19
- **Status:** OPEN

To be defined in the future LMS Experience Profile.

---

## PES-O005 — Additional LMS benchmarks

- **Date:** 2026-09-19
- **Status:** OPEN

Udacity is primary, but specialist benchmark coverage remains open.

---

## PES-O006 — Quantitative UX release thresholds

- **Date:** 2026-09-19
- **Status:** OPEN

Quality dimensions are defined, but final thresholds require empirical validation.

---

## PES-O007 — Agent UI framework requirement

- **Date:** 2026-09-19
- **Status:** OPEN

No default commitment to CopilotKit, assistant-ui, or equivalent framework exists yet.

---

## PES-O008 — Data visualization implementation

- **Date:** 2026-09-19
- **Status:** OPEN

No final commitment to Recharts, ECharts, Tremor, or another solution.

---

## PES-O009 — Canonical repository/package topology

- **Date:** 2026-09-19
- **Status:** OPEN

Possible models include:

- CodeInteX monorepo;
- dedicated PES repository;
- shared package;
- hybrid documentation/package model.

No repository topology should be inferred from the current `pes.project` working directory.

---

## PES-O010 — Exact design-to-code synchronization strategy

- **Date:** 2026-09-19
- **Status:** OPEN

Includes potential interaction between:

- design tools;
- tokens;
- component documentation;
- code;
- AI coding agents.

---

# DEPRECATED DECISIONS

## PES-P001 — Next.js / React as first web reference implementation

- **Date:** 2026-09-19
- **Status:** DEPRECATED

- **Superseded by:** `PES-017`
- **Scope:** Web implementation

### Decision

Next.js / React menjadi kandidat reference implementation pertama.

### Validation required

Harus divalidasi terhadap requirement produk aktual, terutama LMS.

---
---
## PES-P002 — Tailwind CSS as styling and token execution layer

- **Date:** 2026-09-19
- **Status:** DEPRECATED

- **Superseded by:** `PES-018`
- **Scope:** Web implementation

### Decision

Tailwind CSS menjadi kandidat styling/token execution layer.

### Validation required

- semantic-token integration;
- theme portability;
- maintainability;
- AI coding-agent compliance.

---
---
## PES-P003 — shadcn/ui as application-component implementation approach

- **Date:** 2026-09-19
- **Status:** DEPRECATED

- **Superseded by:** `PES-020`
- **Scope:** Component implementation

### Decision

shadcn/ui menjadi kandidat implementation approach untuk application components.

### Important distinction

shadcn/ui bukan PES dan bukan CodeInteX design system.

---
---
## PES-P004 — Base UI as behavioral primitive implementation

- **Date:** 2026-09-19
- **Status:** DEPRECATED

- **Superseded by:** `PES-019`
- **Scope:** Component implementation

### Decision

Base UI menjadi kandidat behavioral primitive implementation untuk web.

### Validation required

- accessibility;
- component coverage;
- integration quality;
- maintainability;
- migration cost.

---
---
## PES-P007 — Storybook as component specification and test surface

- **Date:** 2026-09-19
- **Status:** DEPRECATED

- **Superseded by:** `PES-021`
- **Scope:** Documentation/testing

---
---

## Decision Log Rules

1. Do not delete old decisions when replaced.
2. Mark replaced decisions as `DEPRECATED`.
3. Add `Superseded by` when applicable.
4. Significant implementation changes must reference relevant decision IDs.
5. Do not change a LOCKED decision only by editing another document.
6. Update this log when normative decision state changes.
7. Prefer append/history-preserving changes over rewriting historical rationale.

---

## Current Baseline

Current normative baseline:

- `PES-FOUNDATION-DECISION-MODEL-v0.1.md`
- `PES-CONSUMPTION-CONTRACT-v0.1.md`
- `LMS-EXPERIENCE-PROFILE-v0.1.md`
- `WEB-IMPLEMENTATION-PROFILE-v0.1.md`
- `PES-DECISION-LOG.md`
