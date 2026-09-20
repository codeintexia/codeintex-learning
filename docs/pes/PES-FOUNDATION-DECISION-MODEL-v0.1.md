# Product Experience System — Foundation & Decision Model v0.1

- **Project:** CodeInteX
- **Status:** PROVISIONAL BASELINE
- **Document type:** Normative foundation
- **Version:** 0.1
- **Date:** 2026-09-19

---

## 0. Purpose

Product Experience System (PES) adalah sistem lintas-produk yang mengatur bagaimana pengalaman digital CodeInteX dirancang, diimplementasikan, dievaluasi, dipelihara, dan dikembangkan.

PES bukan hanya:

- UI component library;
- design-token collection;
- Figma library;
- theme;
- CSS framework;
- frontend framework;
- UX guideline;
- documentation set.

PES menyatukan:

- experience principles;
- visual and interaction foundations;
- semantic design tokens;
- component contracts;
- general UX patterns;
- domain experience patterns;
- accessibility;
- content design;
- responsive/adaptive behavior;
- AI and agent interaction principles;
- quality assurance;
- governance;
- rules for human and AI implementers.

PES harus dapat dikonsumsi oleh manusia maupun AI coding agents sebagai sumber aturan pengalaman yang jelas, auditable, dan machine-actionable.

**Decision state: LOCKED**

---

## 1. Scope and Boundaries

PES mengatur concern berikut:

| Area | PES authority |
| --- | --- |
| Experience principles | Yes |
| Information hierarchy principles | Yes |
| Accessibility baseline | Yes |
| Design tokens | Yes |
| Typography | Yes |
| Color semantics | Yes |
| Spacing and layout | Yes |
| Shape, radius, elevation, density | Yes |
| Motion principles | Yes |
| Component contracts | Yes |
| General UX patterns | Yes |
| Content design | Yes |
| Responsive/adaptive behavior | Yes |
| Theme architecture | Yes |
| AI/agent interaction patterns | Yes |
| Domain experience patterns | Extension |
| Quality assurance | Yes |
| Experience governance | Yes |
| Product business logic | No |
| Database architecture | No |
| Backend implementation | No |
| Product-specific domain model | No, except interface contracts |
| Framework-specific implementation | No, at PES Core level |

### 1.1 Non-goals

PES tidak boleh menjadi tempat seluruh keputusan engineering atau product dimasukkan.

PES mengatur **experience rules dan experience contracts**.

Contoh separation of concerns:

- LMS mengatur learning-domain behavior.
- Backend workstream mengatur backend architecture.
- Security workstream mengatur security architecture.
- PES mengatur bagaimana concern tersebut diekspos kepada pengguna ketika berdampak pada pengalaman.

**Decision state: LOCKED**

---

## 2. Canonical PES Layer Model

Canonical PES terdiri atas tujuh conceptual layers.

~~~text
L7 — EXPERIENCE GOVERNANCE
     Quality · Testing · Metrics · Versioning · Decision Governance

L6 — AI / AGENT EXPERIENCE
     Capability · Control · Approval · Provenance · Failure · HITL

L5 — DOMAIN EXPERIENCE PATTERNS
     LMS · Research · CRM · Analytics · Future Product Extensions

L4 — GENERAL UX PATTERNS
     Navigation · Forms · Search · Save · Delete · Upload
     Error Recovery · Long-running Tasks · Permissions

L3 — COMPONENT SYSTEM
     Contracts · Anatomy · States · Behavior · Accessibility

L2 — FOUNDATIONS
     Tokens · Typography · Color · Spacing · Layout
     Shape · Elevation · Motion · Iconography · Density

L1 — EXPERIENCE CONSTITUTION
     Principles · Quality Attributes · Human Factors
~~~

Implementation technology berada di bawah dan di luar PES Core:

~~~text
PES
 ↓
Product Experience Profile
 ↓
Implementation Profile
 ↓
Framework / Runtime / Libraries
~~~

PES tidak boleh secara konseptual bergantung pada React, Next.js, Wagtail, shadcn/ui, Base UI, Tailwind CSS, atau implementation technology lainnya.

**Decision state: LOCKED**

---

## 3. Experience Constitution

Seluruh implementasi PES harus mengikuti prinsip berikut.

### 3.1 Outcome over interface

Kualitas pengalaman dinilai dari kemampuan pengguna menyelesaikan tujuan, bukan dari jumlah fitur, efek visual, atau kompleksitas interface.

### 3.2 Clarity over cleverness

Interaksi yang jelas dan dapat diprediksi lebih disukai daripada novelty yang meningkatkan cognitive load tanpa manfaat substantif.

### 3.3 Recognition over recall

Informasi, pilihan, status, dan navigasi penting harus dapat dikenali tanpa mengharuskan pengguna mengingat state sebelumnya.

### 3.4 Progressive disclosure

Tampilkan informasi paling relevan terlebih dahulu. Complexity muncul ketika diperlukan, bukan sekaligus.

### 3.5 Predictability by default

Komponen dan pattern dengan semantic meaning yang sama harus berperilaku konsisten di seluruh produk.

### 3.6 Accessible by construction

Accessibility adalah requirement desain dan engineering sejak awal.

Baseline release PES adalah:

**WCAG 2.2 AA**

Accessibility tidak boleh diperlakukan hanya sebagai audit akhir.

### 3.7 User remains in control

Automation tidak boleh menghilangkan kemampuan pengguna untuk memahami, menghentikan, mengoreksi, membatalkan, mengambil alih, atau meninjau tindakan ketika konsekuensinya material.

### 3.8 State must be visible

Sistem harus mengomunikasikan state yang relevan secara eksplisit.

Canonical vocabulary mencakup, bila relevan:

~~~text
idle
queued
running
waiting
blocked
needs-input
needs-approval
completed
partial
failed
cancelled
stale
offline
~~~

### 3.9 Errors are first-class states

Loading, empty, partial, stale, disconnected, permission denied, validation failure, dan operation failure bukan edge cases.

Semua harus dipertimbangkan sebagai bagian desain.

### 3.10 Content is interface

Terminologi, action labels, statuses, confirmations, guidance, empty states, dan error messages merupakan bagian dari experience architecture.

### 3.11 Motion communicates

Motion hanya digunakan untuk membantu menjelaskan:

- state change;
- hierarchy;
- continuity;
- causality;
- spatial orientation;
- feedback.

Motion dekoratif tidak boleh merusak usability, performance, atau accessibility.

### 3.12 Evidence before authority

Sistem tidak boleh menampilkan precision, confidence, score, atau authoritative recommendation tanpa semantic definition dan basis yang dapat dipertanggungjawabkan.

### 3.13 Risk determines friction

Friction bukan selalu UX defect.

Semakin tinggi konsekuensi tindakan, semakin kuat kebutuhan terhadap:

- preview;
- confirmation;
- validation;
- approval;
- undo;
- recovery.

### 3.14 Graceful failure

Jika sistem gagal, pengguna harus dapat mengetahui:

- apa yang gagal;
- apa dampaknya;
- apa yang masih tersimpan;
- tindakan apa yang dapat dilakukan;
- apa yang akan dilakukan sistem selanjutnya.

**Decision state: LOCKED**

---

## 4. Experience Quality Model

Istilah seperti:

- world-class;
- god-tier;
- premium;
- excellent;
- future-proof;

tidak dianggap sebagai acceptance criteria tanpa definisi operasional.

### 4.1 Quality dimensions

| Dimension | Provisional weight |
| --- | ---: |
| Task success and workflow effectiveness | 20 |
| Information architecture and clarity | 15 |
| Accessibility | 15 |
| Error prevention and recovery | 10 |
| Performance and perceived responsiveness | 10 |
| Consistency and PES compliance | 10 |
| Responsive/adaptive usability | 5 |
| Content and terminology | 5 |
| Trust, transparency, and user control | 5 |
| Visual craft | 5 |
| **Total** | **100** |

### 4.2 Critical-failure rule

Nilai agregat tidak boleh menutupi critical failure.

Contoh critical failure:

- primary task tidak dapat diselesaikan;
- critical accessibility barrier;
- destructive action tidak aman;
- kehilangan data tanpa recovery;
- navigation dead end;
- serious error tanpa recovery;
- misleading system or AI state.

### 4.3 Decision state

- Quality dimensions: **LOCKED**
- Weighting: **PROVISIONAL**
- Release thresholds: **OPEN**

Threshold final harus divalidasi melalui reference implementation dan usability testing.

---

## 5. Portability Architecture

Portability merupakan architectural requirement PES.

Namun portability dibedakan menjadi beberapa jenis.

### 5.1 Specification portability

Experience principles, semantic tokens, component contracts, UX patterns, accessibility rules, dan domain patterns harus independen dari frontend framework.

**Target: HIGH**

### 5.2 Theme portability

Visual identity harus dapat berubah tanpa mengubah product/domain logic atau interaction semantics.

**Target: HIGH**

### 5.3 Technology portability

Implementation code tidak diwajibkan portable langsung antara React, Flutter, SwiftUI, atau platform lainnya.

Yang harus portable adalah:

- specification;
- semantic model;
- contracts;
- patterns;
- quality requirements.

**Target: specification portable; implementation replaceable**

**Decision state: LOCKED**

---

## 6. Design Token Architecture

Canonical token hierarchy:

~~~text
REFERENCE TOKENS
       ↓
SEMANTIC TOKENS
       ↓
COMPONENT TOKENS
~~~

Feature code tidak boleh bergantung langsung pada raw values jika semantic token yang sesuai tersedia.

Contoh:

~~~text
reference.blue.600
        ↓
action.primary
        ↓
button.primary.background
~~~

Bukan:

~~~text
CourseCard
  → #2563EB
~~~

### 6.1 Token domains

PES minimal harus mampu merepresentasikan:

~~~text
color
typography
spacing
size
layout
radius
border
elevation
opacity
motion
density
z-index
data visualization
~~~

### 6.2 Serialization

Format token machine-readable harus mendukung:

- semantic aliasing;
- multiple themes;
- tooling interoperability;
- validation;
- transformation ke implementation platform berbeda.

DTCG-compatible token serialization menjadi kandidat utama.

Namun format serialization adalah implementation standard, bukan bagian immutable dari PES architecture.

**Decision state:**

- Semantic-token architecture: **LOCKED**
- Exact token serialization format: **PROVISIONAL**

---

## 7. Theme Architecture

Theme adalah konfigurasi visual dan presentational yang tunduk pada PES semantics.

### 7.1 Theme may control

Theme dapat mengontrol:

~~~text
color
typography
shape
radius
elevation
density
motion character
data-visualization palette
selected component aliases
~~~

### 7.2 Theme must not control

Theme tidak boleh mengubah:

~~~text
semantic meaning
keyboard interaction
accessibility semantics
information hierarchy
destructive-action meaning
workflow correctness
required interaction states
~~~

Contoh:

Theme boleh mengubah `action.primary` dari biru menjadi hijau.

Theme tidak boleh membuat destructive action terlihat atau berperilaku identik dengan harmless primary action.

### 7.3 Theme axes

PES harus memungkinkan, sesuai kebutuhan:

~~~text
color mode
brand theme
typography theme
shape language
density
motion preference
~~~

### 7.4 Theme goals

Theme switching harus memungkinkan perubahan identitas visual tanpa:

- fork product logic;
- duplicate component implementations;
- mass manual style rewrites;
- accessibility regression.

### 7.5 Themeability is not unlimited

Tidak semua aspek experience boleh di-theme.

PES membedakan:

~~~text
STABLE
interaction semantics
accessibility
information hierarchy
component anatomy
workflow behavior

THEMEABLE
color
typography
radius
elevation
density
motion character

PRODUCT-SPECIFIC
domain objects
domain workflows
domain-specific information architecture
~~~

**Decision state: LOCKED**

---

## 8. Benchmark Policy

Benchmark digunakan sebagai evidence source, bukan visual template.

### 8.1 Benchmark goals

Benchmark digunakan untuk mempelajari:

~~~text
interaction principles
information architecture
workflow solutions
navigation strategies
state treatment
domain patterns
accessibility approaches
content strategies
~~~

Benchmark tidak digunakan untuk menyalin:

~~~text
branding
colors
visual identity
copy
component appearance
proprietary assets
~~~

### 8.2 LMS primary benchmark

**Udacity ditetapkan sebagai PRIMARY benchmark untuk LMS learner experience.**

Area benchmark meliputi:

~~~text
learner dashboard
course/program hierarchy
curriculum navigation
lesson consumption
resume learning
progress visibility
assessment and projects
learning continuity
resource access
~~~

Udacity bukan authority untuk:

~~~text
PES architecture
CodeInteX visual language
implementation technology
accessibility standard
backend architecture
~~~

### 8.3 Benchmark triangulation

Tidak ada satu produk pun yang menjadi satu-satunya sumber desain.

Canonical model:

~~~text
Primary product benchmark
          +
Specialist benchmarks
          +
HCI/accessibility evidence
          +
Actual user testing
~~~

Setiap benchmark-derived proposal harus menjawab:

~~~text
What problem does this solve?
What evidence supports it?
What are the trade-offs?
Does it fit our users and constraints?
~~~

**Decision state: LOCKED**

---

## 9. Relationship to Product Workstreams

PES adalah cross-cutting capability CodeInteX.

Produk mengonsumsi PES melalui Product Experience Profile.

Canonical architecture:

~~~text
PES CORE
   ↓
PRODUCT EXPERIENCE PROFILE
   ↓
IMPLEMENTATION PROFILE
   ↓
PRODUCT
~~~

Contoh:

~~~text
PES Core
    ↓
LMS Experience Profile
    ↓
Web / Next.js Implementation Profile
    ↓
CodeInteX LMS
~~~

PES Core tidak boleh mengandung implementation detail khusus satu produk.

Product Experience Profile boleh memperluas PES dengan domain semantics, tetapi tidak boleh menciptakan parallel design foundations.

**Decision state: LOCKED**

---

## 10. LMS Integration Boundary

LMS memiliki domain-specific experience objects seperti:

~~~text
CourseCard
CourseOverview
CurriculumTree
LessonNavigator
LearningProgress
Assessment
ProjectSubmission
Enrollment
Certificate
~~~

Domain components harus menggunakan:

~~~text
PES semantic tokens
PES component contracts
PES accessibility rules
PES UX patterns
~~~

Tetapi learning-domain semantics tetap dimiliki workstream LMS.

### 10.1 No local design system

LMS tidak boleh menciptakan parallel visual foundation sendiri jika concern tersebut sudah dimiliki PES.

Contoh yang tidak boleh menjadi local LMS decisions tanpa alasan:

~~~text
local color system
local spacing scale
local typography hierarchy
local radius system
local button grammar
local motion vocabulary
~~~

Jika kebutuhan LMS tidak dapat dipenuhi PES, kebutuhan tersebut harus menjadi feedback/change proposal terhadap PES.

### 10.2 LMS as reference consumer

LMS menjadi salah satu reference consumers pertama PES.

Tujuannya bukan agar PES mengikuti setiap kebutuhan lokal LMS, tetapi untuk menguji:

- completeness;
- portability;
- themeability;
- accessibility;
- component contracts;
- responsive behavior;
- AI-agent usability;
- governance process.

**Decision state: LOCKED**

---

## 11. Backend and Frontend Boundary

Jika LMS menggunakan Wagtail sebagai backend dan Next.js sebagai frontend:

~~~text
Wagtail
   ↓
API / Domain Contract
   ↓
Frontend Adapter / View Model
   ↓
PES-aware Next.js Components
~~~

UI component tidak boleh bergantung langsung pada arbitrary backend model shape.

Tujuannya:

- backend dapat berevolusi;
- frontend dapat berevolusi;
- PES tetap stabil;
- domain contracts dapat diuji;
- implementation coupling berkurang.

### 11.1 Backend responsibility

Backend bertanggung jawab terhadap:

- domain data;
- business rules;
- content structure;
- permissions;
- canonical state;
- APIs/contracts.

### 11.2 Frontend responsibility

Frontend bertanggung jawab terhadap:

- presentation;
- interaction;
- client-side experience state;
- accessibility implementation;
- responsive/adaptive behavior;
- PES compliance.

### 11.3 PES responsibility

PES bertanggung jawab terhadap:

- experience principles;
- semantic visual system;
- component contracts;
- UX patterns;
- interaction rules;
- accessibility requirements;
- quality gates.

**Decision state: LOCKED**

---

## 12. Implementation Boundary

PES Core tidak menentukan implementation library tertentu.

Setiap platform dapat memiliki Reference Implementation Profile.

### 12.1 Current web candidates

Current web implementation candidates:

~~~text
Next.js / React
TypeScript
Tailwind CSS
shadcn/ui
Base UI
Motion
Lucide
Storybook
~~~

Status seluruh pilihan tersebut tetap **PROVISIONAL** sampai divalidasi terhadap product requirements dan reference implementation.

### 12.2 Layer distinction

Implementation technologies berada pada layer berbeda dan tidak boleh dibandingkan sebagai substitusi langsung tanpa memperhatikan fungsinya.

~~~text
Design language / PES
    ↓
Behavioral primitives
    ↓
Application components
    ↓
Visual enhancement
    ↓
Domain UI
    ↓
AI / agent interaction layer
~~~

Contoh provisional mapping:

~~~text
Behavioral primitives
→ Base UI

Application components
→ shadcn/ui

Styling / token execution
→ Tailwind CSS

Motion implementation
→ Motion

Icon implementation
→ Lucide

Visual enhancement
→ Magic UI / Lightswind / Aceternity, selectively

Data visualization
→ Recharts / ECharts, if required

Agent interaction
→ CopilotKit / assistant-ui, only if required
~~~

### 12.3 Optional-library rule

Library seperti berikut tidak termasuk default PES Core:

~~~text
Magic UI
Lightswind
Aceternity
Tremor
CopilotKit
assistant-ui
~~~

Library tambahan hanya boleh masuk jika terdapat requirement konkret yang tidak dapat dipenuhi secara sederhana oleh existing implementation.

Canonical decision flow:

~~~text
Need
 ↓
Requirement
 ↓
Existing PES solution?
 ↓
YES → reuse
NO  → evaluate extension
~~~

Bukan:

~~~text
Interesting library
 ↓
Install
 ↓
Find a use for it
~~~

### 12.4 Dependency minimization

PES implementation harus menghindari:

- overlapping component libraries;
- duplicate primitives;
- conflicting theme systems;
- multiple icon grammars;
- multiple motion vocabularies;
- unnecessary abstraction layers.

Setiap dependency baru harus memiliki:

- explicit problem statement;
- alternatives considered;
- lock-in assessment;
- maintenance assessment;
- migration path;
- ownership boundary.

**Decision state:**

- Implementation-boundary principles: **LOCKED**
- Current web stack candidates: **PROVISIONAL**


---

## 13. AI Coding Agent Contract

PES harus dapat digunakan coding agents tanpa menyebabkan visual, behavioral, semantic, atau architectural drift.

AI-generated UI tunduk pada PES constraints.

PES tidak tunduk pada preferences yang diciptakan ad hoc oleh coding agents.

### 13.1 Default rules

Coding agents harus mengikuti aturan berikut:

1. Do not create a new primitive if an approved primitive already exists.
2. Do not introduce raw color values when semantic tokens exist.
3. Do not introduce arbitrary spacing, radius, typography, elevation, or motion values.
4. Do not bypass approved accessibility behavior.
5. Do not create a new visual language locally.
6. Do not add UI dependencies without explicit justification.
7. Check the relevant Product Experience Profile before inventing domain components.
8. Implement all relevant loading, empty, partial, error, disabled, stale, offline, and permission states.
9. Honor reduced-motion preferences.
10. Do not silently override PES when product requirements conflict with it.
11. Prefer composition over duplicated component variants.
12. Preserve semantic meaning across themes.
13. Do not invent confidence, score, precision, or authority that the underlying system cannot justify.
14. Do not copy benchmark visual identity into CodeInteX products.
15. Do not create product-local design foundations when PES already owns that concern.

### 13.2 Escalation rule

Jika coding agent menemukan requirement yang tidak dapat dipenuhi oleh PES, agent harus:

~~~text
identify the requirement
        ↓
identify the PES constraint
        ↓
describe the conflict
        ↓
propose alternatives
        ↓
request / create a PES change proposal
~~~

Agent tidak boleh menyelesaikan konflik dengan silent local override.

### 13.3 AI-readable artifacts

PES harus secara bertahap menyediakan artefak yang mudah dikonsumsi coding agents, antara lain:

~~~text
normative Markdown documentation
semantic token files
component registry
component contracts
pattern documentation
implementation profiles
product experience profiles
validation rules
decision log
~~~

**Decision state: LOCKED**

---

## 14. Decision Governance

Semua significant decisions menggunakan canonical decision states.

### 14.1 LOCKED

Evidence dan constraints cukup kuat untuk menjadi normative baseline.

Perubahan membutuhkan explicit reconsideration dan rationale.

### 14.2 PROVISIONAL

Pilihan terbaik berdasarkan evidence saat ini, tetapi belum cukup diuji untuk menjadi stable baseline.

### 14.3 OPEN

Keputusan belum dibuat atau evidence belum cukup.

### 14.4 DEPRECATED

Keputusan pernah menjadi arah resmi tetapi tidak lagi berlaku.

### 14.5 Required decision record

Significant decisions sebaiknya mencatat:

~~~text
Context
Evidence
Constraints
Alternatives
Decision
Rationale
Risks
Status
Migration impact
Date
~~~

### 14.6 Conflict resolution

Jika dua workstream menghasilkan keputusan yang bertentangan:

1. conflict harus dinyatakan eksplisit;
2. tanggal dan status keputusan diperiksa;
3. requirement dan evidence dibandingkan;
4. keputusan baru dibuat secara eksplisit;
5. keputusan yang kalah ditandai DEPRECATED bila relevan.

Tidak boleh ada silent precedence.

**Decision state: LOCKED**

---

## 15. Change Governance

PES harus dapat berevolusi tanpa menjadi arbitrary.

Canonical lifecycle:

~~~text
EXPERIMENTAL
    ↓
CANDIDATE
    ↓
STABLE
    ↓
DEPRECATED
    ↓
REMOVED
~~~

### 15.1 Experimental

Digunakan untuk eksplorasi atau kebutuhan lokal yang belum tervalidasi.

Tidak boleh diasumsikan reusable.

### 15.2 Candidate

Sudah cukup menjanjikan untuk digunakan pada lebih dari satu context atau untuk diuji sebagai bagian PES.

### 15.3 Stable

Sudah memenuhi quality requirements dan dapat digunakan sebagai normative implementation.

### 15.4 Deprecated

Masih dapat digunakan sementara untuk compatibility, tetapi tidak boleh dipakai untuk implementation baru.

### 15.5 Removed

Tidak lagi menjadi bagian supported PES.

Komponen atau pattern baru tidak otomatis menjadi stable hanya karena digunakan pada satu screen atau satu produk.

**Decision state: LOCKED**

---

## 16. Feedback and Evolution Loop

PES tidak dibangun di ruang hampa.

Canonical evolution loop:

~~~text
PES specification
      ↓
Product implementation
      ↓
Real-world friction
      ↓
Evidence
      ↓
Change proposal
      ↓
PES evaluation
      ↓
Updated specification
~~~

LMS menjadi salah satu reference consumers pertama untuk menguji PES.

Product workstream tidak boleh melakukan silent local override.

Jika PES tidak mampu memenuhi requirement produk yang valid, hal tersebut dianggap PES feedback, bukan otomatis product violation.

### 16.1 Evidence sources

Feedback dapat berasal dari:

- usability testing;
- accessibility testing;
- production analytics;
- support issues;
- product implementation friction;
- coding-agent failures;
- benchmark analysis;
- user research;
- performance measurements;
- security or privacy findings.

**Decision state: LOCKED**

---

## 17. Accessibility Baseline

Minimum baseline:

~~~text
WCAG 2.2 AA
~~~

Core experiences harus dirancang untuk:

~~~text
keyboard operation
visible focus
screen-reader interpretation
touch usability
zoom
responsive reflow
reduced motion
sufficient contrast
non-color-only communication
accessible authentication where applicable
~~~

### 17.1 Automated testing is insufficient

Automated accessibility testing merupakan quality gate, tetapi tidak dianggap cukup.

Critical workflows memerlukan, sesuai relevansi:

- manual keyboard evaluation;
- focus-order review;
- screen-reader evaluation;
- zoom/reflow evaluation;
- reduced-motion evaluation;
- high-contrast evaluation.

### 17.2 Accessibility invariants

Theme, product customization, dan implementation choice tidak boleh menurunkan accessibility contract PES.

**Decision state: LOCKED**

---

## 18. Responsive and Adaptive Experience

Responsive design tidak didefinisikan hanya sebagai breakpoint.

Setiap meaningful pattern harus menentukan behavior ketika:

- viewport berubah;
- input modality berubah;
- content density berubah;
- user preference berubah;
- device capability berubah.

Possible strategies:

~~~text
reflow
stack
collapse
scroll
drawer
sheet
progressive disclosure
pagination
alternative navigation
~~~

Contoh:

~~~text
desktop:
three-column workspace

tablet:
two-column workspace + contextual drawer

mobile:
single primary surface + sheet
~~~

Responsive behavior harus mempertahankan:

- task continuity;
- information hierarchy;
- action availability;
- accessibility;
- semantic consistency.

**Decision state: LOCKED**

---

## 19. Content Design System

Content adalah bagian dari interaction design.

PES harus mengatur setidaknya:

~~~text
action labels
status terminology
error structure
confirmation structure
empty states
helper text
system feedback
AI capability language
uncertainty language
destructive-action language
~~~

### 19.1 Action labels

Actions harus menjelaskan consequence secara cukup jelas.

Prefer:

~~~text
Save changes
Delete course
Publish lesson
Resume learning
~~~

daripada:

~~~text
OK
Yes
Submit
Continue
~~~

jika konteks tidak cukup menjelaskan tindakan.

### 19.2 Error messages

Error message idealnya menjawab:

~~~text
What happened?
What is the consequence?
What can the user do?
What has been preserved?
~~~

### 19.3 Confirmation

Confirmation harus proporsional dengan risiko.

Low-risk reversible action tidak memerlukan excessive confirmation.

High-risk irreversible action memerlukan stronger friction.

### 19.4 AI content

AI-generated messaging harus membedakan secara jelas:

- fact;
- inference;
- uncertainty;
- recommendation;
- system state;
- user-required action.

**Decision state: LOCKED**

---

## 20. Internationalization and Localization

PES harus menghindari keputusan yang membuat internationalization mahal atau secara arsitektural mustahil.

Implementation harus mempertimbangkan:

- text expansion;
- locale-aware dates;
- locale-aware numbers;
- locale-aware currency;
- pluralization;
- timezone handling;
- bidirectional layout feasibility;
- avoiding text embedded in images;
- avoiding fixed-width assumptions for textual content.

Full RTL support tidak otomatis diwajibkan untuk setiap product v1, tetapi PES Core tidak boleh menghalanginya secara fundamental.

**Decision state:**

- Internationalization readiness: **LOCKED**
- Exact supported locales per product: **PRODUCT-SPECIFIC**

---

## 21. Performance and Perceived Responsiveness

Performance merupakan bagian dari UX quality, bukan concern engineering yang sepenuhnya terpisah.

PES harus menyediakan pattern untuk:

- immediate feedback;
- skeleton/loading treatment;
- optimistic updates ketika aman;
- progressive rendering;
- long-running operations;
- cancellation;
- retry;
- partial results;
- background completion indication.

### 21.1 False progress prohibited

Progress indicators tidak boleh menyatakan precision yang tidak dimiliki sistem.

Jika exact progress tidak diketahui, gunakan indeterminate atau stage-based progress.

### 21.2 Perceived performance

UI harus memberi feedback secepat mungkin ketika user action diterima.

Namun perceived-performance technique tidak boleh menyembunyikan failure atau misleading state.

**Decision state: LOCKED**

---

## 22. Component Contract Requirement

Komponen PES bukan hanya visual implementation.

Setiap stable interactive component harus memiliki contract yang mendefinisikan, sesuai relevansi:

~~~text
purpose
anatomy
variants
states
content rules
interaction behavior
keyboard behavior
accessibility behavior
responsive behavior
theme behavior
error behavior
do / do not guidance
~~~

### 22.1 State completeness

Komponen harus mempertimbangkan state yang relevan dari vocabulary seperti:

~~~text
default
hover
focus
active
selected
disabled
loading
empty
partial
error
success
read-only
permission-denied
stale
offline
~~~

Tidak semua state berlaku untuk semua komponen.

Namun state yang relevan tidak boleh diabaikan hanya karena happy path sudah bekerja.

**Decision state: LOCKED**

---

## 23. General UX Pattern Requirement

Pattern berada satu tingkat di atas component.

Contoh general UX patterns:

~~~text
navigation
search
filtering
sorting
forms
autosave
manual save
upload
delete
undo
confirmation
permissions
bulk actions
long-running operations
empty states
error recovery
authentication
onboarding
notifications
~~~

Setiap stable pattern sebaiknya mendokumentasikan:

~~~text
user intent
when to use
when not to use
workflow
components involved
states
failure modes
recovery
keyboard behavior
responsive behavior
content rules
analytics / measurement points
~~~

**Decision state: LOCKED**

---

## 24. Domain Experience Patterns

Domain Experience Patterns merupakan extension PES Core.

Domain patterns dapat memiliki:

- domain-specific components;
- domain-specific workflows;
- domain-specific terminology;
- domain-specific information architecture.

Namun tetap tunduk pada:

- Experience Constitution;
- accessibility baseline;
- semantic-token system;
- core interaction contracts;
- general UX patterns;
- governance.

### 24.1 LMS example

Potential LMS domain patterns meliputi:

~~~text
LearnerDashboard
CourseDiscovery
CourseOverview
CurriculumNavigation
LessonExperience
ResumeLearning
LearningProgress
Assessment
ProjectSubmission
Completion
Certificate
InstructorWorkflow
~~~

Exact LMS pattern taxonomy masih **OPEN** dan akan dikembangkan dalam LMS Experience Profile.

**Decision state: LOCKED untuk architecture; OPEN untuk taxonomy**

---

## 25. Measurement and Validation

PES tidak boleh mengandalkan subjective visual judgement saja.

Validation dapat mencakup:

- task completion;
- time on task;
- error rate;
- abandonment;
- recovery success;
- accessibility violations;
- performance;
- responsive failures;
- design-system violations;
- semantic-token violations;
- coding-agent compliance;
- user confidence;
- qualitative usability findings.

### 25.1 Metrics must fit the problem

Tidak semua produk harus menggunakan seluruh metric.

Metric dipilih berdasarkan workflow, risk, user population, dan product objective.

### 25.2 No vanity metrics

Metric yang mudah dikumpulkan tetapi tidak merepresentasikan user outcome tidak boleh digunakan sebagai primary evidence kualitas UX.

**Decision state: LOCKED**

---

## 26. Definition of Success for PES v1.0

PES belum dianggap v1.0 hanya karena dokumentasi selesai.

Minimum proof requirements:

~~~text
one substantial real product implementation

at least two meaningfully different themes

responsive implementation

keyboard usability validation

WCAG 2.2 AA-oriented accessibility validation

loading / empty / error / partial states

component and pattern documentation

AI coding-agent consumption test

theme switching without product-logic rewrite

evidence that product teams can implement UI
without creating a parallel local design system
~~~

Tambahan requirements dapat muncul setelah reference implementation.

**Decision state: LOCKED**

---

## 27. Decision State Summary — v0.1

### LOCKED

- PES adalah cross-cutting Product Experience System CodeInteX.
- PES berada di atas framework dan implementation libraries.
- Canonical PES memiliki tujuh conceptual layers.
- Experience Constitution menjadi normative foundation.
- Semantic tokens menjadi portability boundary utama.
- Theme dipisahkan dari product/domain logic.
- Theme tidak boleh mengubah semantic interaction behavior.
- Accessibility adalah by-construction requirement.
- WCAG 2.2 AA menjadi minimum baseline.
- Product-specific domain UX dipisahkan dari PES Core.
- Product Experience Profile menjadi boundary domain extension.
- LMS menjadi reference consumer PES.
- LMS tidak membuat parallel design foundations.
- Backend data melalui explicit contract/adapter sebelum masuk ke UI components.
- Udacity menjadi primary learner-experience benchmark untuk LMS, bukan visual template.
- Benchmark harus ditriangulasi dengan evidence lain dan usability testing.
- AI coding agents harus tunduk pada PES constraints.
- PES menggunakan explicit decision states.
- PES menggunakan controlled change lifecycle.
- Content design merupakan bagian PES.
- Responsive/adaptive behavior merupakan bagian PES.
- Internationalization readiness merupakan requirement.
- Performance dan perceived responsiveness merupakan UX concern.
- Components membutuhkan explicit contracts.
- General UX patterns didokumentasikan sebagai reusable experience rules.
- Domain patterns memperluas PES tanpa mengganti core foundations.
- PES harus diuji melalui produk nyata sebelum v1.0.

### PROVISIONAL

- Quality-model weighting.
- Exact design-token serialization.
- Next.js/React sebagai first web reference implementation.
- Tailwind CSS sebagai styling/token execution layer.
- shadcn/ui sebagai application-component implementation.
- Base UI sebagai behavioral primitive implementation.
- Motion sebagai motion implementation.
- Lucide sebagai icon implementation.
- Storybook sebagai component specification/test surface.

### OPEN

- Final visual language.
- Final typography families.
- Final color system.
- Final spacing scale.
- Final radius/elevation system.
- Exact theme runtime architecture.
- Exact token file structure.
- LMS domain component taxonomy.
- Additional benchmarks beyond Udacity.
- Quantitative UX release thresholds.
- Multi-brand requirements.
- Build-time versus runtime theme switching.
- Agent-UI framework requirement.
- Data-visualization implementation.
- Repository/package topology.
- Exact design-to-code synchronization strategy.

---

## 28. Next Artifacts

Setelah dokumen ini direview dan foundational decisions dianggap cukup kuat, artefak berikutnya adalah:

### 28.1 PES Consumption Contract v0.1

Menentukan bagaimana workstream lain mengonsumsi PES tanpa harus memahami seluruh internal architecture PES.

### 28.2 PES Decision Log

Mencatat perubahan keputusan:

~~~text
LOCKED
PROVISIONAL
OPEN
DEPRECATED
~~~

beserta rationale, evidence, dan migration impact.

### 28.3 Benchmark Evidence Pack v0.1

Tahap pertama:

**Udacity Learner Experience Decomposition**

Area awal:

~~~text
Dashboard
Course discovery/detail
Program/course hierarchy
Curriculum navigation
Lesson experience
Resume learning
Progress
Assessment/projects
Search
Resources
Completion/certificate
Responsive behavior
Accessibility observations
Failure/empty states
~~~

Setiap observation diproses sebagai:

~~~text
OBSERVATION
→ UX PROBLEM
→ EVIDENCE / RATIONALE
→ ADOPT / MODIFY / REJECT
→ PES PATTERN CANDIDATE
~~~

### 28.4 LMS Experience Profile

Dibuat setelah benchmark dan core contracts cukup matang.

Dokumen ini akan menjadi bridge antara PES Core dan LMS implementation.

---

## 29. Document Status

Dokumen ini merupakan **PROVISIONAL BASELINE v0.1**.

Bagian berstatus LOCKED dapat digunakan sebagai normative guidance sejak sekarang.

Bagian PROVISIONAL harus divalidasi melalui:

- reference implementation;
- benchmark evidence;
- product constraints;
- accessibility evaluation;
- usability evaluation.

Bagian OPEN tidak boleh diasumsikan telah diputuskan oleh implementation workstream.

Perubahan substantive terhadap bagian LOCKED harus dicatat melalui PES Decision Log.
