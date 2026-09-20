# CodeInteX LMS Experience Profile v0.1

- **Project:** CodeInteX
- **Workstream:** PES / LMS
- **Artifact type:** Product Experience Profile
- **Status:** PROVISIONAL PROFILE BASELINE
- **Version:** 0.1
- **Date:** 2026-09-19
- **Canonical location:** `docs/pes/`
- **Consumes:** PES Core
- **Reference consumer:** CodeInteX LMS
- **Implementation binding:** NONE

---

## 0. Purpose

This document defines the normative learner-experience contract for the CodeInteX LMS.

It translates PES Core principles and validated LMS evidence into product-domain requirements that implementation workstreams can consume.

It answers:

~~~text
What learner experience must the CodeInteX LMS provide?
~~~

It intentionally does not answer:

~~~text
Which frontend framework implements it?
Which component library implements it?
Which CSS system implements it?
Which backend model stores it?
Which visual layout is final?
~~~

Those belong to lower implementation layers or other workstreams.

### Primary objective

The LMS Experience Profile must provide enough domain-level specificity that:

- frontend implementation can proceed without inventing learner semantics;
- back- **Version:*acts can expose the states required by the learner experience;
- AI coding agents can distinguish required behavior from implementation freedom;
- UX validation can test concrete experience outcomes;
- technology choices remain replaceable.

**Decision state: LOCKED**

---

## 1. Profile Authority and Scope

### Authority model

The authority chain is:

~~~text
PES Core
↓
LMS Experience Profile
↓
Web Implementation Profile
↓
Application implementation
~~~

This profile may specialize PES for the learning domain.

It may not contradict PES Core.

### This profile owns

The LMS Experience Profile owns domain-level learner experience contracts for:

- Learner Dashboard;
- Course Discovery;
- Course Overview;
- Enrollment-facing learning entry;
- Curriculum Navigation;
- Lesson Experience;
- Resume Learning;
- Prog
ess;
- Assessment;
- Project Submission;
- Feedback;
- Revision;
- Completion;
- Credentials;
- learner-visible learning states;
- mobile/responsive learning behavior;
- relevant learner-facing error/recovery behavior.

### This profile does not own

It does not own:

- PES experience constitution;
- global accessibility baseline;
- global semantic-token architecture;
- global theme contract;
- generic component semantics;
- implementation framework choice;
- backend persistence architecture;
- Wagtail internals;
- billing architecture;
- payment security;
- CRM;
- ERP;
- instructor/admin operational UX unless explicitly added later;
- hosted technical workspace unless Track E is activated.

### Product policy boundary

Some experience requirements depend on LMS domain policy.

Where policy is not yet established, this profile must explicitly mark it `OPEN` rather than inventing a rule.

**Decision state: LOCKED**

---

## 2. Normative So- Lesson Experienrequirements appear to conflict, use the following precedence:

~~~text
1. PES Foundation Decision Model
2. PES Consumption Contract
3. LMS Experience Profile
4. Applicable validated specialist evidence
5. Web Implementation Profile
6. Implementation-specific decisions
~~~

Evidence informs this profile.

Evidence itself does not automatically become a requirement.

### Primary evidence artifacts

This profile is informed by:

- `benchmarks/UDACITY-LEARNER-EXPERIENCE-EVIDENCE-v0.1.md`;
- `benchmarks/ACCESSIBILITY-CRITICAL-LEARNER-WORKFLOWS-EVIDENCE-v0.1.md`;
- `benchmarks/ASSESSMENT-PROJECT-WORKFLOW-EVIDENCE-v0.1.md`;
- `benchmarks/MOBILE-RESPONSIVE-LESSON-EXPERIENCE-EVIDENCE-v0.1.md`;
- `benchmarks/ACTIONABLE-DASHBOARD-PROGRESS-EVIDENCE-v0.1.md`.

### Benchmark interpretation rule

~~~text
benchmark observation
≠
CodeInteX requir
**Decision state: LOCKED**

---

## 2. Normative So- Lesson Experienrequ LMS experience contracts.

### Conflict rule

If implementation convenience conflicts with a LOCKED profile contract:

~~~text
implementation must adapt
~~~

unless the profile decision is formally revised through PES governance.

**Decision state: LOCKED**

---

## 3. LMS Experience Boundary

The LMS is a consumer of PES and a producer of learning-domain experience requirements.

### Separation of concerns

~~~text
PES Core
    owns cross-product experience rules

LMS Experience Profile
    owns learner-domain experience contracts

Backend/domain layer
    owns authoritative business rules and persistence

Frontend implementation
    renders and operates against those contracts
~~~

### Required architectural boundary

Frontend experience must not depend directly on Wagtail-specific model structure.

Preferred relationship:

~~~text
backend domain model
↓
API / domain contract
↓
frobtend adapter or view model
↓
PES-aware learner interface
~~~

### Rationale

This boundary protects:

- frontend evolvability;
- backend evolvability;
- testability;
- implementation portability;
- AI-agent comprehension;
- avoidance of CMS leakage into learner UX.

### State ownership rule

The UI may present domain state.

The UI must not silently invent authoritative domain state.

Examples include:

- enrollment eligibility;
- assessment pass/fail;
- attempt availability;
- completion;
- credential eligibility;
- submission receipt.

**Decision state: LOCKED**

---

## 4. Critical Learner Workflows

The v0.1 profile treats the following as critical learner workflows.

### Entry and continuity

~~~text
authenticate
→ learner dashboard
→ identify active learning
→ resume meaningful learning
~~~

### Course entry

~~~text
discover c
Preferred relationship:

~~~text
backendoll where eligible
→ access curriculum
~~~

### Learning consumption

~~~text
curriculum
→ lesson
→ learning activity
→ progress state
→ next meaningful action
~~~

### Assessment

~~~text
understand requirements
→ prepare work
→ validate
→ submit
→ receive confirmation
→ await evaluation
→ receive result/feedback
→ revise or complete
~~~

### Completion

~~~text
required learning complete
→ completion state established
→ credential/completion outcome available where applicable
~~~

### Recovery

Every critical workflow must define recoverable behavior for material failure states.

### Accessibility

Every critical workflow is subject to the PES WCAG 2.2 AA baseline and the Track A manual validation matrix.

**Decision state: LOCKED**

---

## 5. Global Learner Experience Invariants

The following invariants apply across→ identify actfaces.

### 5.1 State truthfulness

The interface must not claim a domain action succeeded before authoritative confirmation exists.

Examples:

~~~text
submitted
completed
passed
saved
credential earned
~~~

must correspond to the relevant authoritative state.

---

### 5.2 Learner orientation

The learner should be able to determine, where relevant:

~~~text
Where am I?
What am I doing?
What is my current state?
What should I do next?
~~~

---

### 5.3 Meaningful next action

Critical learner surfaces should expose a meaningful next action when domain state makes one available.

Optional discovery must not obscure required work.

---

### 5.4 Continuity

The LMS should minimize unnecessary reconstruction of learning context across:

- sessions;
- navigation transitions;
-
**Decision state: LOCKED**

---

## 5. Global

### 5.5 Work preservation

Learner-created work must not be discarded unnecessarily because of:

- validation failure;
- network failure;
- downstream processing failure;
- responsive state changes.

Exact persistence strategy belongs to implementation/backend architecture.

---

### 5.6 Recoverability

Material failure states should communicate:

~~~text
what happened
what was preserved
what the learner can do
what happens next
~~~

---

### 5.7 Accessibility

Accessibility is part of correctness.

It is not a post-implementation enhancement.

---

### 5.8 Responsive semantic continuity

Responsive adaptation may change presentation but must preserve:

- domain meaning;
- primary learner tasks;
- critical state;
- accessibility;
- required information.

---

### 5.9 Implementation independence

No learner requirement in this
Thofile should require one specific framework or UI library unless later evidence establishes a genuine dependency.

**Decision state: LOCKED**

---

## 6. Learner Dashboard Contract

### Primary job

The Learner Dashboard exists primarily to:

~~~text
restore learning context
→ identify priority
→ enable meaningful next action
~~~

It is not primarily:

- a marketing page;
- an analytics showcase;
- a recommendation feed;
- a certificate gallery.

### Required learner questions

A returning learner should be able to determine:

~~~text
What am I currently learning?
Where did I stop?
What should I do next?
Is anything requiring my attention?
~~~

### Priority hierarchy

The dashboard should generally prioritize:

~~~text
1. required attention / blocker
2. active learning / resume
3. next meaningful action
4. meaningful progress
5. other active learni- criticaional discovery
~~~

The exact visual order may vary when domain context justifies it.

### Resume Learning

The dashboard must provide a clear path back into meaningful active learning when resumable learning exists.

Resume logic must not be based blindly on the most recently opened page.

Potential domain signals may include:

- last meaningful learning activity;
- current incomplete lesson;
- incomplete required assessment;
- learner-selected priority;
- relevant deadline.

Exact prioritization algorithm remains OPEN.

### Multiple active courses

When several active courses exist:

- ordering should use meaningful signals;
- opaque arbitrary reordering should be avoided;
- learner agency should be preserved when the system cannot confidently select one priority.

### Blockers

Material blockers or required learner a
~~~text
1. required attent with:

- affected learning context;
- reason;
- required action;
- relevant next step.

Waiting on a reviewer/system must remain distinguishable from action required from the learner.

### Recommendations

Recommendations are secondary to active required learning unless product context explicitly establishes otherwise.

They must not obscure:

- failed assessment requiring revision;
- required incomplete work;
- blocker;
- deadline;
- learner-selected active goal.

### Progress

Dashboard progress must use explicit domain semantics.

Do not treat:

~~~text
activity
completion
proficiency
mastery
~~~

as interchangeable concepts.

### Mobile

On constrained viewports, preserve first:

- current learning;
- resume action;
- required attention;
- meaningful progress;
- next action.

Secondary dashboard content may move or collapse.

### Accessibility

Dashboard state and progress must not depend solely on:

- color;
- chart geometry
Material baphy;
- spatial position.

Meaningful textual/programmatic semantics are required.

### Validation candidates

Dashboard validation should eventually measure:

- time-to-resume;
- success identifying next action;
- blocker recognition;
- progress comprehension;
- unnecessary navigation before resuming.

Exact thresholds remain PROVISIONAL.

**Decision state: LOCKED experience contract; OPEN layout and prioritization algorithm**
