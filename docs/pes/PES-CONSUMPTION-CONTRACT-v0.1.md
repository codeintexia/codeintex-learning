# Product Experience System — Consumption Contract v0.1

- **Project:** CodeInteX
- **Status:** PROVISIONAL BASELINE
- **Document type:** Cross-workstream consumption contract
- **Version:** 0.1
- **Date:** 2026-09-19
- **Depends on:** `PES-FOUNDATION-DECISION-MODEL-v0.1.md`

---

## 0. Purpose

Dokumen ini menjelaskan bagaimana product workstream, implementation workstream, dan AI coding agents mengonsumsi Product Experience System (PES).

Dokumen ini bukan pengganti PES Foundation.

Tujuannya adalah memberikan kontrak operasional yang cukup singkat agar workstream seperti LMS dapat:

- menggunakan PES secara konsisten;
- mengetahui decision authority masing-masing layer;
- mengetahui apa yang boleh diputuskan secara lokal;
- mengetahui apa yang tidak boleh di-override secara lokal;
- menggunakan theme, tokens, components, dan patterns secara benar;
- mengeskalasi kebutuhan yang belum didukung PES;
- menghindari parallel local design system;
- tetap bergerak tanpa menunggu seluruh PES selesai.

**Decision state: LOCKED**

---

## 1. Consumption Model

Canonical consumption flow:

~~~text
PES CORE
   ↓
PRODUCT EXPERIENCE PROFILE
   ↓
IMPLEMENTATION PROFILE
   ↓
PRODUCT IMPLEMENTATION
~~~

Contoh LMS:

~~~text
PES Core
   ↓
LMS Experience Profile
   ↓
Web / Next.js Implementation Profile
   ↓
CodeInteX LMS
~~~

PES Core mendefinisikan aturan lintas-produk.

Product Experience Profile mendefinisikan domain experience.

Implementation Profile mendefinisikan bagaimana contracts tersebut diwujudkan pada stack tertentu.

Product implementation menggunakan ketiganya.

**Decision state: LOCKED**

---

## 2. Authority Model

Jika terdapat konflik keputusan, authority ditentukan berdasarkan concern.

### 2.1 PES Core owns

PES Core memiliki authority terhadap:

- experience principles;
- accessibility baseline;
- semantic token architecture;
- visual foundations;
- interaction semantics;
- component contracts;
- general UX patterns;
- content-design principles;
- responsive/adaptive principles;
- theme contract;
- AI interaction principles;
- experience quality gates.

### 2.2 Product Experience Profile owns

Product profile memiliki authority terhadap:

- domain terminology;
- domain workflows;
- domain-specific information architecture;
- domain-specific components;
- domain-specific states;
- domain-specific content requirements.

Contoh LMS:

- Course;
- Lesson;
- Curriculum;
- Enrollment;
- Assessment;
- Learning Progress;
- Certificate.

### 2.3 Implementation Profile owns

Implementation profile memiliki authority terhadap:

- framework integration;
- rendering strategy;
- component wiring;
- API consumption;
- state-management implementation;
- styling implementation;
- build tooling;
- test tooling;
- package integration.

### 2.4 Backend workstream owns

Backend/domain workstream memiliki authority terhadap:

- canonical business rules;
- persistence;
- domain data;
- permissions;
- workflow invariants;
- backend validation;
- API contracts.

### 2.5 Conflict rule

Jika dua layers memberikan keputusan yang tampak bertentangan:

1. identifikasi concern yang sebenarnya;
2. tentukan owner layer;
3. jangan override silently;
4. catat conflict;
5. eskalasi sebagai decision/change proposal jika perlu.

**Decision state: LOCKED**

---

## 3. Mandatory PES Invariants

Semua consumer PES wajib mematuhi invariant berikut.

### 3.1 Semantic tokens

Feature code tidak boleh menggunakan raw visual values jika semantic token yang sesuai tersedia.

Tidak diperbolehkan secara default:

~~~text
raw hex colors
arbitrary spacing
arbitrary radius
arbitrary typography
local shadow scales
local motion timings
~~~

### 3.2 Accessibility

Consumer tidak boleh menurunkan accessibility contract PES.

Minimum baseline tetap:

~~~text
WCAG 2.2 AA
~~~

### 3.3 Interaction semantics

Theme atau product customization tidak boleh mengubah semantic behavior seperti:

- destructive-action meaning;
- focus behavior;
- keyboard behavior;
- disabled semantics;
- error semantics;
- required confirmation behavior.

### 3.4 Component reuse

Jika approved component atau pattern sudah tersedia, consumer harus menggunakannya sebelum membuat alternatif baru.

### 3.5 State completeness

Consumer harus menangani state relevan seperti:

~~~text
loading
empty
partial
error
disabled
permission-denied
stale
offline
success
~~~

sesuai context.

### 3.6 Theme independence

Product/domain logic tidak boleh bergantung pada theme tertentu.

### 3.7 No parallel design foundations

Consumer tidak boleh membuat:

~~~text
local color system
local typography system
local spacing system
local radius system
local button grammar
local icon grammar
local motion vocabulary
~~~

jika concern tersebut sudah dimiliki PES.

**Decision state: LOCKED**

---

## 4. What Product Workstreams May Decide Locally

Product workstream boleh menentukan domain-specific experience yang tidak dimiliki PES Core.

Contoh LMS:

- struktur Course Overview;
- hierarchy program/course/module/lesson;
- progress semantics;
- assessment flow;
- enrollment flow;
- completion logic;
- certificate workflow;
- learner/instructor/admin information architecture.

Namun product workstream harus mengekspresikan kebutuhan tersebut menggunakan PES foundations dan contracts.

Contoh:

~~~text
LMS decides:
"Course Progress must expose current lesson, completed lessons,
and recommended next action."

PES decides:
how progress state is communicated accessibly,
which semantic status patterns are used,
how hierarchy and interaction remain consistent.
~~~

**Decision state: LOCKED**

---

## 5. What Product Workstreams Must Not Decide Locally

Product workstream tidak boleh secara sepihak menentukan:

- independent color palette;
- independent typography hierarchy;
- independent spacing scale;
- arbitrary component anatomy;
- arbitrary focus treatment;
- alternate keyboard interaction;
- alternate destructive-action semantics;
- independent icon style;
- independent motion language;
- alternate theme contract;
- lower accessibility standard.

Jika kebutuhan produk membutuhkan perubahan pada concern tersebut, buat PES change proposal.

**Decision state: LOCKED**

---

## 6. Theme Consumption Contract

Product harus menggunakan theme melalui semantic contract.

Feature code berpikir dalam terms seperti:

~~~text
surface.canvas
surface.raised
text.primary
text.secondary
border.default
action.primary
action.destructive
status.success
status.warning
status.danger
~~~

Feature code tidak boleh mengasumsikan nilai aktual token.

Contoh:

~~~text
GOOD

CourseCard
→ surface.raised
→ text.primary
→ border.subtle
→ action.primary
~~~

Bukan:

~~~text
BAD

CourseCard
→ dark gray background
→ blue button
→ 12px radius
~~~

### 6.1 Theme switching

Changing theme must not require rewriting:

- product logic;
- API logic;
- domain workflow;
- component behavior;
- accessibility behavior.

### 6.2 Product-specific theme request

Jika product membutuhkan theme behavior baru:

~~~text
requirement
   ↓
check existing theme contract
   ↓
supported?
   ├─ YES → consume
   └─ NO  → PES change proposal
~~~

**Decision state: LOCKED**

---

## 7. Component Consumption Contract

Approved components merupakan default implementation surface.

Consumer harus:

1. menggunakan existing component jika semantics cocok;
2. compose existing components sebelum membuat primitive baru;
3. menggunakan approved variants sebelum membuat variant lokal;
4. mendokumentasikan kebutuhan jika existing component tidak cukup.

### 7.1 New component decision

Sebelum membuat component baru:

~~~text
Is this domain-specific?
   ├─ YES → product profile candidate
   └─ NO
       ↓
Does PES already solve it?
   ├─ YES → reuse
   └─ NO → PES component candidate
~~~

### 7.2 Component ownership

~~~text
Generic reusable component
→ PES

Domain-specific reusable component
→ Product Experience Profile

One-off layout composition
→ Product implementation
~~~

One-off composition tidak otomatis menjadi design-system component.

**Decision state: LOCKED**

---

## 8. General UX Pattern Consumption

Consumer harus menggunakan PES general patterns untuk concern seperti:

- forms;
- search;
- filtering;
- sorting;
- save;
- autosave;
- delete;
- undo;
- confirmation;
- upload;
- permissions;
- empty states;
- long-running operations;
- failure recovery.

Product boleh memperluas pattern jika domain membutuhkan behavior tambahan.

Product tidak boleh mengganti underlying general pattern tanpa explicit rationale.

**Decision state: LOCKED**

---

## 9. Backend-to-UI Contract

Backend representation tidak boleh langsung menjadi UI contract.

Canonical flow:

~~~text
Backend Domain Model
        ↓
API / Domain Contract
        ↓
Frontend Adapter / View Model
        ↓
PES-aware Product Component
~~~

Tujuannya:

- backend independence;
- frontend independence;
- stable UI contracts;
- testability;
- explicit data transformation;
- reduced coupling.

### 9.1 LMS example

Jika backend adalah Wagtail:

~~~text
Wagtail Course model
        ↓
Course API schema
        ↓
CourseViewModel
        ↓
CourseOverview / CourseCard
~~~

UI component tidak boleh mengetahui implementation detail internal Wagtail yang tidak relevan terhadap experience.

**Decision state: LOCKED**

---

## 10. AI Coding Agent Consumption Contract

AI coding agents harus membaca dan mengikuti:

1. PES Foundation;
2. Consumption Contract;
3. relevant Product Experience Profile;
4. relevant Implementation Profile;
5. current Decision Log.

Agent tidak boleh menganggap chat prompt terbaru otomatis mengalahkan normative PES decision.

Jika prompt bertentangan dengan LOCKED PES decision, agent harus:

~~~text
identify conflict
   ↓
explain impact
   ↓
offer compliant alternative
   ↓
request explicit PES decision change if required
~~~

### 10.1 AI agents must not

AI agents tidak boleh secara default:

- invent new theme values;
- introduce raw visual constants;
- install overlapping UI libraries;
- create local primitive libraries;
- bypass accessibility;
- copy benchmark styling;
- silently modify LOCKED PES semantics;
- generate arbitrary component variants;
- treat visual preference as architectural requirement.

### 10.2 AI agents should

AI agents sebaiknya:

- reuse canonical components;
- prefer composition;
- expose states explicitly;
- preserve semantic hierarchy;
- produce accessible behavior;
- use current decision state;
- report unmet PES requirements;
- create reusable artifacts when appropriate.

**Decision state: LOCKED**


---

## 11. Conflict Escalation

Jika product requirement bertentangan dengan PES, implementation workstream tidak boleh memilih sendiri secara diam-diam.

Canonical flow:

~~~text
Requirement conflict detected
        ↓
Identify affected PES rule
        ↓
Determine whether rule is LOCKED / PROVISIONAL / OPEN
        ↓
Document impact
        ↓
Evaluate alternatives
        ↓
Escalate as:
- product-specific exception, or
- PES change proposal
~~~

### 11.1 Product-specific exception

Exception hanya valid jika:

- requirement benar-benar domain-specific;
- exception tidak merusak accessibility;
- exception tidak menciptakan parallel design foundation;
- exception terdokumentasi;
- exception tidak diasumsikan reusable.

### 11.2 PES change proposal

PES change proposal diperlukan jika:

- kebutuhan berpotensi lintas-produk;
- existing PES rule tidak cukup;
- existing component/pattern menghasilkan recurring friction;
- accessibility atau usability evidence menuntut perubahan;
- implementation constraint material ditemukan.

Minimum proposal:

~~~text
Context
Requirement
Current PES rule
Conflict
Evidence
Alternatives
Recommendation
Risks
Migration impact
Requested decision state
~~~

**Decision state: LOCKED**

---

## 12. Product Experience Profile Contract

Setiap domain besar dapat memiliki Product Experience Profile.

Contoh:

~~~text
LMS Experience Profile
Research Experience Profile
CRM Experience Profile
Analytics Experience Profile
~~~

Product Experience Profile berfungsi sebagai extension PES Core.

### 12.1 Product profile may define

- domain objects;
- domain terminology;
- domain workflows;
- domain-specific component contracts;
- domain-specific navigation;
- domain-specific information hierarchy;
- domain-specific state semantics.

### 12.2 Product profile must not redefine

- global semantic-token architecture;
- accessibility baseline;
- global typography system;
- global spacing system;
- global radius/elevation grammar;
- core interaction semantics;
- global theme architecture.

### 12.3 Domain component rule

Domain component harus menggunakan core PES foundations.

Contoh:

~~~text
CourseCard
= LMS-owned domain component
+ PES tokens
+ PES accessibility
+ PES interaction contracts
~~~

**Decision state: LOCKED**

---

## 13. LMS Consumption Profile — Interim Rules

Sampai `LMS-EXPERIENCE-PROFILE` tersedia, workstream LMS menggunakan interim rules berikut.

### 13.1 LMS may continue

LMS boleh terus mengembangkan:

- backend architecture;
- Wagtail models;
- APIs;
- domain logic;
- enrollment;
- progression rules;
- assessment logic;
- permissions;
- routing;
- data contracts;
- non-visual functionality.

### 13.2 LMS should avoid locking

Sampai PES foundations lebih matang, LMS sebaiknya tidak mengunci secara lokal:

- final color palette;
- final typography system;
- final spacing scale;
- final radius/elevation language;
- final motion vocabulary;
- independent design tokens;
- duplicate primitive components.

### 13.3 LMS may implement provisional UI

UI implementation boleh berjalan secara provisional jika dibutuhkan untuk product development.

Syarat:

- gunakan PES semantic intent sejauh tersedia;
- minimalkan raw visual values;
- tandai local workaround yang perlu dimigrasikan;
- jangan menganggap workaround sebagai PES decision;
- hindari dependency yang sulit dilepas.

### 13.4 LMS benchmark

Udacity adalah primary learner-experience benchmark.

LMS workstream boleh mempelajari:

- learner orientation;
- curriculum navigation;
- progress;
- resume learning;
- lesson continuity;
- assessment/project workflow.

LMS tidak boleh menyalin visual identity benchmark.

**Decision state: LOCKED**

---

## 14. Implementation Profile Contract

Implementation Profile menerjemahkan PES ke technology stack tertentu.

Contoh:

~~~text
PES Core
   ↓
Web Implementation Profile
   ↓
Next.js / React
~~~

Implementation Profile boleh menentukan:

- framework bindings;
- primitive-library mapping;
- styling implementation;
- component packaging;
- token transformation;
- Storybook integration;
- test tooling;
- SSR/CSR behavior;
- frontend state implementation.

Implementation Profile tidak boleh mengubah semantic intent PES.

### 14.1 Example provisional web mapping

~~~text
PES semantic tokens
→ Tailwind/CSS variables

PES component contracts
→ shadcn/ui-based components

PES behavioral primitives
→ Base UI

PES motion contracts
→ Motion

PES icon contracts
→ Lucide
~~~

Mapping ini masih **PROVISIONAL**.

Jika implementation library berubah, PES Core tidak boleh ikut berubah kecuali memang ada perubahan experience requirement.

**Decision state: LOCKED untuk boundary; PROVISIONAL untuk mapping**

---

## 15. Dependency Governance

Consumer tidak boleh menambahkan UI dependency hanya karena component yang dibutuhkan tersedia di library tersebut.

Setiap dependency baru harus menjawab:

~~~text
What problem does it solve?
Why existing PES implementation is insufficient?
What alternatives were considered?
What is the accessibility quality?
What is the maintenance risk?
What is the lock-in risk?
How difficult is migration?
Does it overlap existing dependencies?
~~~

### 15.1 Preferred strategy

Prefer:

~~~text
existing component
   ↓
composition
   ↓
small custom implementation
   ↓
new dependency
~~~

New dependency adalah opsi terakhir, bukan default.

**Decision state: LOCKED**

---

## 16. Validation Contract

Consumer harus memvalidasi experience, bukan hanya compilation.

Validation yang relevan dapat mencakup:

- component behavior;
- keyboard operation;
- responsive behavior;
- accessibility;
- loading states;
- error states;
- empty states;
- theme compatibility;
- visual regressions;
- product workflow;
- PES compliance.

### 16.1 Critical workflow rule

Critical workflow tidak dianggap complete hanya karena happy path bekerja.

Minimal harus diperiksa:

~~~text
success
loading
error
empty
permission
responsive
keyboard
~~~

sesuai relevansi.

### 16.2 Theme validation

Shared component yang digunakan lintas-theme harus diuji minimal terhadap:

- default theme;
- alternative theme;
- light/dark mode jika didukung;
- reduced motion jika menggunakan motion.

**Decision state: LOCKED**

---

## 17. Consumption Checklist

Sebelum implementasi UI dianggap sesuai PES, consumer harus dapat menjawab:

### Foundations

- Apakah semantic tokens digunakan?
- Apakah raw visual values diminimalkan?
- Apakah product tidak membuat local design system?

### Components

- Apakah approved components digunakan?
- Apakah duplicate primitives dihindari?
- Apakah states relevan tersedia?

### UX

- Apakah workflow mengikuti PES patterns?
- Apakah error recovery tersedia?
- Apakah user mengetahui system state?

### Accessibility

- Apakah keyboard interaction bekerja?
- Apakah focus terlihat?
- Apakah status tidak hanya disampaikan lewat warna?
- Apakah semantic HTML/ARIA sesuai?

### Responsive

- Apakah experience tetap usable pada target viewport?
- Apakah hierarchy tetap jelas?

### Theme

- Apakah domain logic theme-independent?
- Apakah component menggunakan semantic values?

### AI-generated implementation

- Apakah agent mematuhi normative PES documents?
- Apakah agent tidak menciptakan arbitrary component/style system?

Jika jawaban material adalah "tidak", implementasi belum dianggap PES-compliant.

**Decision state: LOCKED**

---

## 18. Normative Source Order

Jika terdapat perbedaan instruksi, gunakan urutan berikut:

~~~text
1. Current LOCKED PES decisions
2. PES Foundation
3. PES Consumption Contract
4. Relevant Product Experience Profile
5. Relevant Implementation Profile
6. Product requirement
7. Local implementation preference
~~~

Namun precedence hanya berlaku dalam concern yang memang dimiliki layer tersebut.

Contoh:

PES tidak boleh menggunakan precedence ini untuk membatalkan valid backend business rule.

Jika ownership tidak jelas, conflict harus dieksplisitkan.

**Decision state: LOCKED**

---

## 19. Versioning and Compatibility

Consumer harus mengetahui versi PES yang digunakan.

Minimum metadata:

~~~text
PES Core version
Product Experience Profile version
Implementation Profile version
Theme version, if relevant
~~~

Breaking changes pada stable PES contracts harus:

- didokumentasikan;
- memiliki migration guidance;
- memiliki deprecation period jika rasional;
- tidak dilakukan diam-diam.

**Decision state: LOCKED**

---

## 20. Consumption Success Criteria

Consumption Contract dianggap berhasil jika:

- product workstream dapat menggunakan PES tanpa membaca seluruh decision history;
- LMS tidak menciptakan parallel visual foundation;
- theme dapat berubah tanpa product-logic rewrite;
- implementation library dapat berubah tanpa mengubah PES semantics;
- AI coding agents menghasilkan UI lebih konsisten;
- conflicts dapat ditelusuri dan diselesaikan secara eksplisit;
- domain components tetap dapat berkembang tanpa mencemari PES Core.

**Decision state: LOCKED**

---

## 21. Decision State Summary — v0.1

### LOCKED

- PES dikonsumsi melalui Product Experience Profile dan Implementation Profile.
- Concern ownership menentukan authority.
- Semantic tokens adalah mandatory consumption boundary.
- Accessibility tidak boleh diturunkan oleh consumer.
- Product workstream tidak boleh membuat parallel design foundation.
- Theme tidak boleh bocor ke product/domain logic.
- Domain components dapat memperluas PES.
- Backend models tidak langsung menjadi UI contracts.
- AI coding agents wajib mengikuti normative PES artifacts.
- Conflicts harus diekskalasi secara eksplisit.
- UI dependencies harus melalui dependency governance.
- Product implementation harus divalidasi terhadap relevant states dan accessibility.
- Consumer harus mengetahui versi PES yang digunakan.

### PROVISIONAL

- Web implementation mapping.
- Next.js/React implementation profile.
- Tailwind CSS mapping.
- shadcn/ui mapping.
- Base UI mapping.
- Motion mapping.
- Lucide mapping.

### OPEN

- Exact implementation-profile document format.
- Exact PES compliance automation.
- Exact exception-record format.
- Exact multi-repository distribution model.

---

## 22. Next Dependency

Dokumen berikut yang harus dibuat setelah Consumption Contract:

`PES-DECISION-LOG.md`

Decision Log menjadi authoritative history untuk:

~~~text
LOCKED
PROVISIONAL
OPEN
DEPRECATED
~~~

dan mencatat perubahan keputusan lintas versi.

---

## 23. Document Status

Dokumen ini merupakan **PROVISIONAL BASELINE v0.1**.

Bagian LOCKED dapat digunakan oleh workstream lain sejak sekarang.

Bagian PROVISIONAL tidak boleh dianggap permanen.

Bagian OPEN tidak boleh diputuskan secara lokal tanpa explicit decision.

Dokumen ini harus digunakan bersama:

`PES-FOUNDATION-DECISION-MODEL-v0.1.md`
