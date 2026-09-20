# CodeInteX LMS — Specialist Benchmark Plan v0.1

- **Project:** CodeInteX
- **Workstream:** PES / LMS
- **Status:** PROVISIONAL RESEARCH PLAN
- **Version:** 0.1
- **Date:** 2026-09-19
- **Primary benchmark:** Udacity
- **Depends on:**
  - `../PES-FOUNDATION-DECISION-MODEL-v0.1.md`
  - `../PES-CONSUMPTION-CONTRACT-v0.1.md`
  - `../PES-DECISION-LOG.md`
  - `UDACITY-LEARNER-EXPERIENCE-EVIDENCE-v0.1.md`

---

## 0. Purpose

Dokumen ini menentukan specialist benchmark research yang masih diperlukan sebelum CodeInteX mengunci LMS Experience Profile v0.1.

Tujuannya adalah:

- menutup evidence gap yang material;
- mencegah over-reliance pada Udacity;
- mencegah benchmark rabbit hole;
- menentukan research questions sebelum memilih benchmark;
- menentukan evidence standard;
- menentukan stop condition;
- menjaga perbedaan antara benchmark evidence dan product decision.

Dokumen ini bukan benchmark evidence pack.

Dokumen ini menentukan **apa yang perlu diteliti dan kapan penelitian harus berhenti**.

**Decision state: LOCKED untuk process; PROVISIONAL untuk benchmark selection**

---

## 1. Research Principle

Specialist benchmark hanya boleh ditambahkan ketika terdapat unresolved question yang material terhadap product decision.

Canonical flow:

~~~text
Unresolved product question
        ↓
Identify evidence gap
        ↓
Determine required evidence
        ↓
Select specialist benchmark
        ↓
Collect only relevant evidence
        ↓
Compare with PES + Udacity evidence
        ↓
Decision sufficiently supported?
        ├─ YES → STOP
        └─ NO  → add evidence source only if justified
~~~

Tidak diperbolehkan:

~~~text
interesting product
→ research everything
→ create giant comparison matrix
~~~

Benchmark breadth bukan objective.

Decision quality adalah objective.

**Decision state: LOCKED**

---

## 2. Evidence Hierarchy

Evidence diprioritaskan sebagai berikut:

### Tier 1 — Direct product evidence

- current official product behavior;
- official product documentation;
- directly observable interaction;
- current accessibility documentation;
- current design-system documentation where relevant.

### Tier 2 — Standards and established guidance

- WCAG;
- WAI-ARIA Authoring Practices;
- platform accessibility guidance;
- established HCI evidence;
- relevant learning-science evidence.

### Tier 3 — Independent evaluation

- credible accessibility audits;
- usability studies;
- research papers;
- practitioner evidence with clear methodology.

### Tier 4 — Secondary commentary

- reviews;
- articles;
- community discussion;
- screenshots without interaction context.

Tier 4 dapat membantu menemukan masalah, tetapi tidak boleh menjadi satu-satunya basis untuk LOCKED decision yang material.

**Decision state: LOCKED**

---

## 3. Benchmark Selection Criteria

Specialist benchmark candidate harus dievaluasi terhadap:

- relevance terhadap unresolved question;
- current availability;
- observable behavior;
- evidence quality;
- similarity of user problem;
- maturity of workflow;
- accessibility relevance;
- ability to distinguish domain pattern from branding;
- risk of importing irrelevant constraints.

Benchmark tidak dipilih berdasarkan:

- popularity semata;
- visual attractiveness;
- hype;
- market valuation;
- number of features;
- similarity of branding.

**Decision state: LOCKED**

---

## 4. Priority Model

Research priority ditentukan berdasarkan kombinasi:

~~~text
Decision impact
×
Current uncertainty
×
Cost of getting it wrong
×
Difficulty of changing later
~~~

Gunakan tiga priority levels:

### P0 — Blocking

Evidence gap menghalangi safe architecture atau critical learner workflow.

Harus diteliti sebelum relevant contract dikunci.

### P1 — Important

Material terhadap experience quality tetapi tidak memblokir architecture.

Boleh berjalan paralel dengan early implementation.

### P2 — Deferred

Useful tetapi belum mempengaruhi current milestone.

Tidak diteliti sekarang.

**Decision state: LOCKED**

---

## 5. Current Specialist Research Scope

Berdasarkan Udacity Evidence Pack v0.1, lima area berikut memerlukan evaluasi.

| Area | Priority | Current state |
|---|---|---|
| Accessibility critical learner workflows | P0 | REQUIRED |
| Assessment / project workflow | P1 | REQUIRED |
| Mobile / responsive lesson experience | P1 | REQUIRED |
| Actionable dashboard and progress | P1 | REQUIRED |
| Hosted technical workspace UX | P2 unless workspace enters v0.1 scope | CONDITIONAL |

Tidak ada specialist benchmark lain yang masuk scope saat ini kecuali evidence baru menunjukkan kebutuhan material.

**Decision state: LOCKED untuk scope v0.1**

---

## 6. Research Track A — Accessibility Critical Learner Workflows

### Priority

**P0**

### Problem

Udacity public evidence menunjukkan beberapa accessibility-supporting capabilities, tetapi tidak cukup untuk memvalidasi:

- keyboard interaction;
- screen-reader semantics;
- focus management;
- reflow;
- touch targets;
- accessible status communication;
- error handling;
- assessment accessibility.

CodeInteX tidak boleh mengisi gap tersebut dengan asumsi.

### Research questions

RQ-A1:

Bagaimana critical learner navigation harus bekerja dengan keyboard?

RQ-A2:

Bagaimana curriculum hierarchy sebaiknya direpresentasikan agar tetap understandable untuk assistive technology?

RQ-A3:

Bagaimana progress dan asynchronous assessment states harus diumumkan secara accessible?

RQ-A4:

Bagaimana media transcript, captions, dan controls sebaiknya bekerja?

RQ-A5:

Bagaimana error, validation, and recovery flows harus disampaikan?

RQ-A6:

Bagaimana responsive/reflow behavior menjaga operability pada zoom tinggi dan narrow viewport?

### Required evidence

Minimum:

- WCAG 2.2 normative requirements relevant to learner flows;
- WAI-ARIA/APG guidance where applicable;
- at least one mature learning/product experience with observable accessibility behavior if useful;
- direct validation criteria that can later become LMS acceptance tests.

### Desired output

Bukan daftar "best practices".

Output yang dibutuhkan:

~~~text
accessibility requirement
→ affected LMS workflow
→ applicable standard/evidence
→ required behavior
→ validation method
~~~

### Stop condition

Track A selesai ketika critical learner flows dapat memiliki testable accessibility contracts tanpa bergantung pada undocumented benchmark assumptions.

### Candidate sources

Primary standards sources:

- W3C WCAG 2.2;
- WAI-ARIA Authoring Practices.

Product benchmark hanya ditambahkan jika membantu menjawab interaction-specific question yang tidak diselesaikan cukup oleh standard.

**Decision state: LOCKED untuk research requirement; OPEN untuk additional product benchmark**

---

## 7. Research Track B — Assessment and Project Workflow

### Priority

**P1**

### Problem

Udacity memberi evidence kuat untuk:

- visible rubric;
- submit;
- asynchronous review;
- revision;
- pass/change-required state.

Namun CodeInteX belum memiliki evidence cukup untuk mengunci:

- exact workflow state model;
- formative versus summative assessment behavior;
- autosave/draft expectations;
- resubmission;
- feedback presentation;
- partial completion;
- human versus automated versus AI-assisted review;
- deadline/late-submission interaction.

### Research questions

RQ-B1:

Apa minimal state model yang diperlukan agar assessment workflow jelas dan recoverable?

RQ-B2:

Bagaimana criteria/rubric harus ditampilkan sebelum dan setelah submission?

RQ-B3:

Bagaimana feedback harus dihubungkan dengan criteria dan revision action?

RQ-B4:

Bagaimana draft, autosave, submit, and resubmit dibedakan?

RQ-B5:

Bagaimana long-running review state ditampilkan tanpa menciptakan uncertainty?

RQ-B6:

Bagaimana AI-assisted evaluation, jika nanti digunakan, harus dibedakan dari authoritative human/system evaluation?

### Benchmark selection requirement

Benchmark harus memiliki substantial assessment/project workflow.

Prefer benchmark yang memungkinkan observation terhadap:

- assignment brief;
- submission;
- rubric;
- feedback;
- revision;
- status lifecycle.

### Candidate benchmark classes

Candidates may include:

- mature project-based learning platforms;
- coding-learning platforms;
- higher-education LMS assessment workflows.

Tidak ada product yang dikunci sebagai benchmark sebelum research question diuji terhadap available evidence.

### Stop condition

Track B selesai ketika CodeInteX dapat mendefinisikan provisional but coherent contracts untuk:

~~~text
Assessment
ProjectSubmission
ReviewState
Feedback
Revision
FailureRecovery
~~~

tanpa mengadopsi vendor-specific workflow secara buta.

**Decision state: LOCKED untuk research requirement; OPEN untuk benchmark selection**

---

## 8. Research Track C — Mobile and Responsive Lesson Experience

### Priority

**P1**

### Problem

Udacity evidence tidak cukup untuk mengunci responsive behavior bagi:

- curriculum navigation;
- lesson player;
- assessment;
- transcript;
- progress;
- resource navigation;
- complex learning content.

### Research questions

RQ-C1:

Bagaimana learner mempertahankan orientation ketika curriculum navigation tidak dapat selalu terlihat?

RQ-C2:

Apa yang harus tetap visible versus dipindahkan ke progressive disclosure?

RQ-C3:

Bagaimana media, transcript, lesson content, dan navigation coexist pada narrow viewport?

RQ-C4:

Bagaimana large tables, code, diagrams, atau technical content harus direflow atau di-scroll?

RQ-C5:

Bagaimana progress dan next-action tetap discoverable pada mobile?

RQ-C6:

Workflow mana yang realistis digunakan di mobile dan mana yang memerlukan desktop-oriented affordance?

### Required evidence

Minimum evidence harus mencakup:

- responsive principles dari PES;
- accessibility reflow requirements;
- direct observation dari minimal satu mature learning experience dengan responsive lesson flow;
- validation against CodeInteX content types.

### Important constraint

Benchmark mobile tidak boleh otomatis menghasilkan:

~~~text
mobile version
=
desktop layout compressed
~~~

Responsive behavior harus mempertahankan:

- hierarchy;
- learner orientation;
- primary actions;
- state;
- accessibility.

### Stop condition

Track C selesai ketika LMS Experience Profile dapat mendefinisikan responsive invariants tanpa mengunci breakpoint/layout implementation.

**Decision state: LOCKED untuk research requirement; OPEN untuk benchmark selection**


---

## 9. Research Track D — Actionable Dashboard and Progress

### Priority

**P1**

### Problem

Udacity provides evidence for:

- Continue Learning;
- progress statistics;
- concepts completed;
- lessons completed;
- projects completed.

However, CodeInteX has not yet established enough evidence to determine:

- which progress information deserves prominence;
- how learner progress should drive next action;
- how blockers should appear;
- how program/course progress should relate;
- how mastery/completion differs from activity;
- when recommendations are useful versus distracting.

### Research questions

RQ-D1:

What information does a returning learner need first?

RQ-D2:

How should progress communicate:

~~~text
current position
remaining work
next action
blockers
completion evidence
~~~

without becoming a dashboard of vanity metrics?

RQ-D3:

How should progress work across:

- one course;
- multiple concurrent courses;
- program-level learning;
- optional activities;
- required assessments?

RQ-D4:

How should stalled or blocked learning be represented?

RQ-D5:

When is recommendation useful, and when does it compete with active learning?

RQ-D6:

How can the dashboard minimize time-to-resume?

### Benchmark selection requirement

Prefer mature products where learner/dashboard behavior can be observed around:

- resume;
- current work;
- progress;
- completion;
- next action.

Do not select a benchmark merely because its dashboard looks visually polished.

### Desired output

Research should support provisional contracts for:

~~~text
LearnerDashboard
ResumeLearning
LearningProgress
NextAction
BlockerVisibility
~~~

### Stop condition

Track D selesai when CodeInteX can define what the dashboard must communicate without needing to copy a benchmark layout.

**Decision state: LOCKED untuk research requirement; OPEN untuk benchmark selection**

---

## 10. Research Track E — Hosted Technical Workspace UX

### Priority

**P2 — CONDITIONAL**

### Activation condition

Track ini hanya aktif jika hosted technical workspace masuk LMS v0.1 scope.

Examples:

- browser IDE;
- notebook;
- coding sandbox;
- lab environment;
- persistent project workspace.

Jika hosted workspace tidak masuk current scope, track ini harus ditunda.

### Problem

Technical workspaces introduce additional risks:

- learner work loss;
- environment startup time;
- timeout;
- resource limits;
- reset versus recovery confusion;
- persistence uncertainty;
- execution failure;
- environment incompatibility.

### Research questions

Jika track diaktifkan:

RQ-E1:

How should workspace startup and readiness be communicated?

RQ-E2:

How should recovery differ from destructive reset?

RQ-E3:

What learner state must survive session interruption?

RQ-E4:

How should resource or execution failure be communicated?

RQ-E5:

How should autosave/persistence state be exposed?

RQ-E6:

How should workspace state integrate with lesson and assessment state?

### Stop condition

Track E selesai ketika CodeInteX dapat define minimum workspace continuity, recovery, and destructive-action contracts.

### Decision state

**OPEN / CONDITIONAL**

No research should be performed now unless hosted workspace becomes a concrete LMS requirement.

---

## 11. Explicitly Deferred Research

The following areas are not part of the current specialist benchmark milestone unless a concrete blocker emerges:

- instructor dashboard;
- enterprise administration;
- cohort management;
- CRM;
- marketing site UX;
- payment architecture;
- advanced personalization;
- community/social features;
- gamification;
- AI tutor;
- AI agent workspace;
- credential marketplace;
- advanced analytics dashboards.

### Rationale

These areas may become important later, but researching them now would broaden scope without improving current LMS foundation decisions.

### Rule

Deferred does not mean rejected.

It means:

~~~text
not required for current decision
~~~

**Decision state: LOCKED for current milestone scope**

---

## 12. Anti-Rabbit-Hole Rules

Specialist research must stop expanding when evidence is already sufficient for the decision.

### Rule 1 — Question before benchmark

Never choose a product first and invent a research question afterward.

### Rule 2 — Maximum useful benchmark set

For each research question, begin with:

- authoritative standard/evidence where applicable;
- one strong specialist benchmark.

Add a second product benchmark only if the first leaves a material unresolved conflict or gap.

A third product benchmark requires explicit justification.

### Rule 3 — Do not benchmark visual identity

Do not research:

- palette;
- shadows;
- corner radius;
- decorative motion;
- brand personality;

unless the unresolved decision is specifically about those concerns.

### Rule 4 — Stop after decision sufficiency

Do not continue collecting evidence merely because more evidence exists.

### Rule 5 — Unknown is acceptable

If a non-blocking question remains uncertain:

~~~text
mark OPEN
→ proceed
→ validate during implementation
~~~

Do not delay the entire system for low-impact certainty.

### Rule 6 — Avoid feature counting

More features do not imply better learner experience.

### Rule 7 — Preserve source distinction

Always distinguish:

~~~text
observation
inference
product decision
implementation choice
~~~

**Decision state: LOCKED**

---

## 13. Research Output Contract

Each specialist research result should record:

~~~text
Research question
Evidence source
Observation
Evidence quality
User problem
Inference
Applicability to CodeInteX
Adopt / Modify / Reject
Resulting requirement candidate
Remaining uncertainty
Decision state
~~~

Research output should be concise enough to remain auditable.

Do not reproduce entire product documentation.

---

## 14. Evidence Sufficiency Test

A research question has sufficient evidence when all of the following are true:

1. the actual user/problem concern is understood;
2. applicable standards are identified where relevant;
3. at least one credible evidence source addresses the problem;
4. known material alternatives are understood;
5. major accessibility consequences are understood;
6. major failure modes are understood;
7. the resulting requirement can be expressed without copying vendor implementation;
8. remaining uncertainty can safely be marked PROVISIONAL or OPEN.

Evidence does not need to eliminate all uncertainty.

The objective is sufficient confidence for a reversible, responsible product decision.

**Decision state: LOCKED**

---

## 15. Escalation Conditions

Additional research beyond this plan requires at least one of:

- conflicting high-quality evidence;
- critical accessibility uncertainty;
- irreversible architecture consequence;
- material security/privacy consequence;
- high migration cost if wrong;
- usability test failure;
- reference implementation failure;
- new product requirement not covered by current evidence.

Without one of these conditions, default action is:

~~~text
do not expand research scope
~~~

**Decision state: LOCKED**

---

## 16. Required Deliverables

Before drafting the normative LMS Experience Profile, required specialist outputs are:

### Required

1. Accessibility Critical Learner Workflow Evidence
2. Assessment / Project Workflow Evidence
3. Mobile / Responsive Lesson Evidence
4. Dashboard / Progress Evidence

### Conditional

5. Hosted Technical Workspace Evidence

only if Track E activation condition is met.

### Artifact strategy

These outputs may be:

- separate evidence files; or
- one consolidated specialist evidence pack;

depending on size and source overlap.

Do not split documents solely for organizational aesthetics.

**Decision state: LOCKED for required evidence; OPEN for file packaging**

---

## 17. Research Completion Gate

Specialist benchmark phase is complete when:

### Track A

Critical learner accessibility requirements are testable.

### Track B

Assessment/project workflow can be modeled coherently.

### Track C

Responsive invariants can be specified without copying layouts.

### Track D

Dashboard/progress requirements can be expressed independently of benchmark visual structure.

### Track E

Either:

- hosted workspace is out of current scope; or
- its continuity/recovery contract has enough evidence.

### Global condition

There is enough evidence to draft:

`LMS-EXPERIENCE-PROFILE-v0.1.md`

without silently inventing high-impact learner experience rules.

**Decision state: LOCKED**

---

## 18. Decision State Summary — v0.1

### LOCKED

- specialist research must be question-driven;
- evidence hierarchy;
- benchmark selection criteria;
- priority model;
- Tracks A–D required;
- Track E conditional;
- anti-rabbit-hole rules;
- evidence sufficiency test;
- escalation conditions;
- research completion gate.

### PROVISIONAL

- current priority assignment;
- candidate benchmark classes;
- exact research execution sequence.

### OPEN

- exact additional product benchmarks;
- exact specialist evidence file packaging;
- activation of hosted workspace research.

---

## 19. Immediate Execution Order

Execute research in this order:

~~~text
1. Accessibility
2. Assessment / Project Workflow
3. Mobile / Responsive Lesson Experience
4. Dashboard / Progress
5. Hosted Workspace only if activated
~~~

Accessibility is first because it is the only current P0 track.

Tracks B–D may be researched efficiently in parallel if evidence sources overlap, but conclusions must remain separate by research question.

---

## 20. Document Status

This document is a:

**PROVISIONAL RESEARCH PLAN v0.1**

Its process guardrails may be used immediately.

The selected specialist benchmarks remain subject to evidence availability and relevance.

The plan must not become a reason to delay implementation after its completion gate has been satisfied.

The next activity is specialist evidence collection, beginning with:

`Accessibility Critical Learner Workflows`
