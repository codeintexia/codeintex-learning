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
- backend/API contracts can expose the states required by the learner experience;
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
- Progress;
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

## 2. Normative Source Order

When requirements appear to conflict, use the following precedence:

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
CodeInteX requirement
~~~

Only requirements explicitly promoted into this profile become LMS experience contracts.

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
frontend adapter or view model
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
discover course
→ understand course
→ enter/enroll where eligible
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

The following invariants apply across LMS learner surfaces.

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

### 5.2 Learner orientation

The learner should be able to determine, where relevant:

~~~text
Where am I?
What am I doing?
What is my current state?
What should I do next?
~~~

### 5.3 Meaningful next action

Critical learner surfaces should expose a meaningful next action when domain state makes one available.

Optional discovery must not obscure required work.

### 5.4 Continuity

The LMS should minimize unnecessary reconstruction of learning context across:

- sessions;
- navigation transitions;
- responsive layouts;
- supported devices.

### 5.5 Work preservation

Learner-created work must not be discarded unnecessarily because of:

- validation failure;
- network failure;
- downstream processing failure;
- responsive state changes.

Exact persistence strategy belongs to implementation/backend architecture.

### 5.6 Recoverability

Material failure states should communicate:

~~~text
what happened
what was preserved
what the learner can do
what happens next
~~~

### 5.7 Accessibility

Accessibility is part of correctness.

It is not a post-implementation enhancement.

### 5.8 Responsive semantic continuity

Responsive adaptation may change presentation but must preserve:

- domain meaning;
- primary learner tasks;
- critical state;
- accessibility;
- required information.

### 5.9 Implementation independence

No learner requirement in this profile should require one specific framework or UI library unless later evidence establishes a genuine dependency.

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
5. other active learning
6. optional discovery
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

Material blockers or required learner attention should be surfaced with:

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
- chart geometry;
- iconography;
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


---

## 7. Course Discovery Contract

### Primary job

Course Discovery exists to help a learner determine:

~~~text
What learning options exist?
Which option is relevant to my goal?
What should I inspect next?
~~~

It must not be optimized only for catalog browsing volume.

### Required information

Discovery representations should expose enough information to support meaningful comparison.

Depending on course type, relevant information may include:

- course title;
- concise learning outcome;
- level or prerequisite expectation;
- estimated commitment where reliable;
- delivery format;
- credential/completion outcome where applicable;
- availability/enrollment state.

### Information quality

Discovery metadata must be semantically trustworthy.

Do not use:

- inflated level labels;
- misleading duration;
- ambiguous credential claims;
- vague outcome language;

merely to improve click-through.

### Progress-aware discovery

For already-started learning, discovery/browse surfaces may expose learner state such as:

- enrolled;
- in progress;
- completed;
- meaningful progress.

Progress must use the same semantics defined elsewhere in this profile.

### Recommendation boundary

Discovery recommendations remain secondary to required active learning in contexts where both compete.

Recommendation rationale should be explainable when it materially affects learner choice.

### Search and filtering

If catalog scale requires search or filtering, interaction should support useful criteria rather than exposing filters solely because metadata exists.

Exact:

- taxonomy;
- faceting;
- ranking;
- search engine;
- recommendation algorithm;

remain OPEN.

### Accessibility

Discovery content must remain usable through:

- semantic headings;
- accessible controls;
- keyboard interaction;
- meaningful link/button labels;
- responsive reflow.

### Anti-pattern

Do not turn discovery into a visually dense marketplace that makes learning outcomes difficult to compare.

**Decision state: LOCKED experience contract; OPEN taxonomy, ranking, and layout**

---

## 8. Course Overview Contract

### Primary job

The Course Overview exists to help the learner make an informed entry decision and understand the learning commitment.

The learner should be able to determine:

~~~text
What will I learn?
Who is this for?
What will I need?
How is the course structured?
What does completion require?
What happens if I start?
~~~

### Required semantic areas

Where relevant, Course Overview should communicate:

- learning outcomes;
- intended learner;
- prerequisite expectations;
- curriculum summary;
- assessment/project expectations;
- completion requirements;
- estimated commitment when sufficiently reliable;
- relevant credential outcome;
- enrollment/access state.

### Outcome clarity

Learning outcomes should describe capabilities or knowledge the course intends to develop.

Avoid relying only on:

- promotional slogans;
- topic lists;
- vague benefit language.

### Curriculum preview

The learner should be able to understand course structure before committing where product policy permits.

Preview may expose:

- sections/modules;
- lesson groups;
- major projects;
- assessment structure.

Exact amount of preview remains product-specific.

### Completion clarity

Where completion depends on more than content traversal, the overview should not imply that viewing all lessons alone guarantees completion.

Examples may include:

- required assessment;
- accepted project;
- required score;
- prerequisite completion.

Exact rules come from authoritative domain policy.

### Enrollment/action state

Primary action must reflect real eligibility and access state.

Examples may include:

~~~text
Start
Enroll
Continue
Resume
Unavailable
Requires prerequisite
~~~

The UI must not advertise an action that the backend/domain layer will reject under known state.

### Pricing/payment boundary

Learner-facing purchase or checkout entry may be linked from Course Overview when relevant.

However:

- pricing authority;
- discount logic;
- payment processing;
- tax;
- billing security;

belong outside this experience profile.

### Accessibility and responsive behavior

Course Overview must preserve:

- outcome clarity;
- enrollment action;
- prerequisite visibility;
- completion expectations;

across supported viewport sizes.

### Anti-pattern

Do not place critical prerequisite or completion requirements only in low-priority secondary content.

**Decision state: LOCKED experience contract; OPEN visual composition and commercial policy**

---

## 9. Curriculum Navigation Contract

### Primary job

Curriculum Navigation helps the learner understand:

~~~text
Where am I in the course?
What is available?
What is complete?
What is required?
What comes next?
~~~

### Hierarchy

Curriculum structure should preserve meaningful learning hierarchy.

Potential domain levels may include:

~~~text
course
→ module / section
→ lesson / activity
→ assessment / project
~~~

Exact taxonomy belongs to LMS domain modeling.

### Current location

The learner's current item must be distinguishable from:

- completed items;
- incomplete items;
- locked/unavailable items;
- optional items.

State must not rely solely on visual color.

### Completion semantics

Curriculum state must not silently equate:

~~~text
visited
=
completed
~~~

Completion must follow authoritative domain rules.

### Locked or unavailable content

When curriculum content is unavailable, the learner should be able to understand why when disclosure is appropriate.

Possible causes include:

- unmet prerequisite;
- release schedule;
- enrollment/access rule;
- required prior assessment.

Do not expose sensitive internal authorization detail.

### Navigation continuity

Moving between curriculum and lesson content should preserve:

- current location;
- meaningful progress;
- learner orientation.

### Next and previous navigation

Sequential navigation may be provided where curriculum semantics support it.

`Next` must not bypass an authoritative blocker or prerequisite silently.

### Narrow viewport behavior

When persistent curriculum navigation cannot remain visible, alternate presentation must preserve:

- current location;
- access to surrounding curriculum;
- route back to curriculum;
- next/previous relationship where relevant.

Exact implementation may use:

- temporary drawer;
- sheet;
- inline curriculum;
- other accessible pattern.

No specific pattern is locked here.

### Large curricula

Large curricula should avoid forcing learners to scan the entire structure for current position.

Potential techniques may include:

- section-level disclosure;
- current-section emphasis;
- localized expansion;
- searchable navigation where genuinely useful.

Exact interaction remains OPEN.

### Accessibility

Curriculum navigation must preserve:

- meaningful semantic structure;
- keyboard operability;
- focus visibility;
- understandable expanded/collapsed state;
- logical reading order.

A visual hierarchy does not automatically require an ARIA tree widget.

Use more complex interaction semantics only when the interaction genuinely requires them.

### Anti-pattern

Do not mirror backend content-tree structure mechanically if it creates a confusing learner hierarchy.

**Decision state: LOCKED experience contract; OPEN taxonomy and presentation**


---

## 10. Lesson Experience Contract

### Primary job

The Lesson Experience exists to support meaningful learning activity while preserving:

- learner orientation;
- lesson context;
- progress state;
- access to relevant support;
- clear continuation.

The learner should be able to determine:

~~~text
What am I learning?
Where is this within the course?
What do I need to do here?
What happens next?
~~~

### Primary learning activity

The lesson interface should prioritize the primary learning activity.

Depending on lesson type, this may include:

- text/content;
- video;
- audio;
- interactive exercise;
- assessment;
- project instruction;
- technical activity.

Secondary surfaces must not compete unnecessarily with the primary learning task.

### Lesson identity and context

The learner should have sufficient context to understand:

- course;
- current section/module where relevant;
- current lesson/activity;
- relationship to surrounding curriculum.

Exact visual presentation remains OPEN.

### Lesson completion

A lesson must not be marked complete merely because it was opened unless authoritative domain policy defines opening as sufficient completion.

Possible completion rules may depend on:

- explicit learner action;
- required content completion;
- assessment result;
- activity state;
- backend progression rules.

The exact rule is domain-specific and remains authoritative outside the view layer.

### Media

For media lessons, experience should provide accessible controls and preserve meaningful playback state where supported.

Relevant concerns include:

- captions where required;
- transcript where provided;
- playback controls;
- media failure recovery;
- resume position.

Transcript availability must not be falsely represented as a universal WCAG AA requirement.

### Supporting resources

Lesson resources should remain discoverable without overwhelming the primary activity.

Examples may include:

- downloadable resources;
- transcript;
- references;
- glossary;
- supplemental material.

Exact placement remains OPEN.

### Lesson navigation

Where curriculum semantics allow, learners should have clear access to:

- current curriculum context;
- previous relevant item;
- next meaningful item;
- route back to curriculum.

`Next` must not silently bypass domain blockers.

### State preservation

Opening secondary surfaces such as:

- curriculum;
- transcript;
- resources;

should not unnecessarily reset:

- media position;
- lesson position;
- learner input;
- domain progress.

### Responsive behavior

On constrained viewports:

- primary learning activity retains priority;
- curriculum context remains accessible;
- secondary resources may use progressive disclosure;
- critical actions/state remain discoverable.

### Technical content

Code, tables, diagrams, and other genuinely two-dimensional content may use localized adaptation such as scoped horizontal scrolling.

The entire lesson should not become horizontally scrollable because one content region is two-dimensional.

### Failure recovery

Material lesson failures should distinguish, where relevant:

- content unavailable;
- media failure;
- network failure;
- authorization/access failure;
- unsupported capability.

Recovery should preserve existing learner context whenever feasible.

### Accessibility

Lesson experience must preserve:

- semantic reading order;
- keyboard operation;
- visible focus;
- accessible media behavior;
- reflow/zoom;
- understandable status/error state.

**Decision state: LOCKED experience contract; OPEN lesson-type composition and completion policy**

---

## 11. Resume Learning Contract

### Primary job

Resume Learning minimizes the cost of returning to meaningful learning after interruption.

Resume is not simply:

~~~text
open most recently viewed URL
~~~

It should restore a meaningful learning context.

### Resume target

A valid resume target may depend on:

- last meaningful lesson activity;
- incomplete required lesson;
- assessment requiring action;
- project requiring revision;
- learner-selected priority;
- authoritative progression state.

Exact selection algorithm remains OPEN.

### Meaningful state

Where supported, resume may preserve:

- course;
- lesson/activity;
- media position;
- relevant assessment draft;
- project workflow state;
- progress context.

Not every transient UI state should be persisted.

### Invalid resume target

A stored resume target may become invalid because of:

- curriculum change;
- revoked access;
- expired enrollment;
- changed prerequisite;
- deleted/unpublished content;
- completion.

In that case, the learner should be redirected to the nearest meaningful valid context rather than receiving an unexplained failure.

### Cross-device continuity

Where synchronization supports it, meaningful resume state should survive supported device changes.

Exact synchronization architecture remains OPEN.

### Unsupported-device handoff

If the current device cannot complete the required activity:

- preserve context;
- explain limitation;
- identify the required environment;
- provide a continuation path.

### Resume versus next action

Resume target and next meaningful action may differ.

Example:

~~~text
last viewed lesson = Lesson 5
required action = revise failed Project 1
~~~

The product must not assume these are always identical.

### Validation

Resume experience should eventually be validated through measures such as:

- time-to-resume;
- successful return to intended activity;
- incorrect resume-target rate;
- unnecessary navigation after return.

Exact thresholds remain PROVISIONAL.

**Decision state: LOCKED continuity contract; OPEN resume selection algorithm**

---

## 12. Progress Contract

### Core semantic rule

Progress must represent an explicitly defined domain concept.

The LMS must not collapse the following into one undefined metric:

~~~text
activity
content traversal
required-item completion
assessment completion
project completion
proficiency
mastery
course completion
~~~

### Progress dimensions

A learning product may expose one or more dimensions such as:

- curriculum completion;
- required activity completion;
- assessment state;
- project state;
- demonstrated capability;
- course/program completion.

Each dimension must have defined semantics.

### Percentage rule

A percentage must communicate what its denominator represents.

For example:

~~~text
8 of 10 required items complete
~~~

is semantically stronger than:

~~~text
80%
~~~

without definition.

### Activity versus outcome

Metrics such as:

- learning time;
- sessions;
- lessons opened;
- streaks;

must not be presented as evidence of competence unless domain policy establishes that relationship.

### Visited versus completed

~~~text
visited
≠
completed
~~~

unless the authoritative domain rule explicitly defines them as equivalent.

### Completed versus mastered

~~~text
completed
≠
mastered
~~~

unless the product has a valid mastery model and evidence supporting that claim.

### Actionable progress

Where practical, progress state should connect to a meaningful next action.

Examples:

~~~text
incomplete required lesson
→ continue

assessment changes required
→ review feedback and revise

project under review
→ wait for evaluation

blocked prerequisite
→ resolve prerequisite

course complete
→ completion/credential action
~~~

### Blocked progress

Progress representation must not hide material blockers.

The learner should be able to distinguish:

~~~text
learner action required
~~~

from:

~~~text
waiting on system/reviewer
~~~

### Non-monotonic progress

If future CodeInteX products adopt proficiency or mastery models, progress may legitimately decrease after reassessment.

A monotonic-only UI must not be assumed universally.

### Aggregation

Aggregation across:

- lessons;
- assessments;
- projects;
- courses;
- programs;

requires explicit domain rules.

Frontend implementation must not invent weighting.

### Accessibility

Progress must remain understandable without reliance solely on:

- color;
- bar length;
- chart geometry;
- animation;
- icon.

Meaningful textual/programmatic representation is required.

### Responsive behavior

Mobile and desktop may visualize progress differently.

They must preserve the same underlying progress semantics.

### Validation

Progress UX should eventually test whether learners can accurately answer:

~~~text
What have I completed?
What remains?
What is blocking me?
What should I do next?
~~~

**Decision state: LOCKED semantic contract; OPEN calculation and visualization**


---

## 13. Assessment Contract

### Primary job

Assessment experience exists to help the learner:

~~~text
understand expectation
→ produce or select response
→ validate
→ submit where required
→ understand result
→ know what happens next
~~~

Assessment is a workflow, not merely a submit button.

### Assessment brief

Before consequential submission, the learner should be able to understand, where applicable:

- objective;
- task or question;
- required deliverable;
- constraints;
- evaluation criteria;
- attempt policy;
- deadline/time limit;
- submission requirements.

### Criteria visibility

Where evaluation uses explicit criteria or rubric, relevant criteria should be available before consequential submission.

The same conceptual criteria should remain traceable into later feedback where applicable.

### Draft versus submitted

Where submission creates a commitment boundary:

~~~text
draft
≠
submitted
~~~

The learner must be able to distinguish whether work is:

- still editable;
- being saved;
- ready to submit;
- being submitted;
- accepted as submitted;
- failed to submit.

Not every low-consequence practice activity requires an explicit draft/submit boundary.

### Validation

Predictable validation should happen before final submission when feasible.

Examples may include:

- required fields;
- artifact presence;
- supported format;
- file size;
- attempt eligibility.

Client-side validation may improve experience.

Authoritative validation remains a backend/domain responsibility.

### Submission confirmation

Consequential submission should provide durable confirmation rather than relying only on transient notification.

Where relevant, confirmation may expose:

- submission status;
- timestamp;
- attempt;
- submitted artifacts;
- next expected state.

### State distinction

The experience must not collapse:

~~~text
submission accepted
evaluation complete
result released
~~~

into one undifferentiated status.

These are potentially separate domain states.

### Attempts

Where multiple attempts exist, learners should understand relevant policy such as:

- current attempt;
- attempts remaining where applicable;
- whether resubmission replaces or versions prior work;
- whether feedback belongs to a specific attempt.

Exact attempt limits and grading policy remain OPEN.

### Timed assessment

When time limits exist:

- timer semantics must be clear;
- expiration behavior must be defined;
- accessibility/accommodation requirements must be considered;
- due date, hard cut-off, and attempt timer must remain distinct concepts.

Exact policy remains OPEN.

### Evaluation provenance

Where material to learner trust or action, evaluation should not misrepresent whether the result came from:

- deterministic automation;
- human review;
- AI-assisted process;
- hybrid process.

AI-generated output must not silently become authoritative assessment unless governance explicitly establishes that authority.

### Failure recovery

Assessment failures should distinguish where possible:

- validation failure;
- save failure;
- upload failure;
- submission failure;
- evaluation-processing failure;
- result retrieval failure.

The learner should be able to understand:

~~~text
What failed?
Was my work preserved?
Was submission received?
What can I do next?
~~~

### Accessibility

Assessment experience must preserve:

- keyboard operation;
- focus management;
- programmatic labels;
- accessible validation/errors;
- dynamic status communication;
- reflow/zoom;
- non-color state communication.

**Decision state: LOCKED experience contract; OPEN grading, attempt, timing, and AI-evaluation policy**

---

## 14. Project Submission Contract

### Scope

Project Submission is a specialized assessment workflow for consequential learner-created artifacts.

Possible artifacts may include:

- document;
- code;
- repository reference;
- archive;
- media;
- structured response;
- multiple related files.

Exact supported artifact types remain product-specific.

### Primary job

The learner should be able to understand:

~~~text
What must I submit?
Is my work ready?
Was it received?
What is its review state?
What happens next?
~~~

### Work preservation

Learner-created project work requires an explicit preservation strategy.

Possible mechanisms may include:

- local draft;
- server draft;
- explicit save;
- autosave;
- external artifact reference.

This profile does not lock the persistence mechanism.

### Truthful save state

The interface must not claim durable save before the authoritative persistence boundary has succeeded.

Relevant states may include:

~~~text
unsaved
saving
saved
save failed
stale
~~~

Exact vocabulary remains implementation-specific.

### Preflight

Before final submission, predictable constraints should be exposed where feasible.

Possible checks include:

- required artifact present;
- file type;
- file size;
- required metadata;
- attempt eligibility;
- deadline/cut-off;
- prerequisite completion.

### Commitment boundary

When submission:

- consumes an attempt;
- prevents further editing;
- triggers formal evaluation;
- has other significant consequence;

the interface should make that consequence clear before commitment.

Confirmation intensity should be proportional to consequence.

### Submission receipt

Successful submission should establish a durable receipt/state.

The learner should not need to infer successful receipt from disappearance of a button or page transition.

### Duplicate-submission risk

Retry behavior must not create ambiguous duplicate consequential submissions.

The exact idempotency mechanism belongs to backend/API architecture.

The learner experience requires safe and understandable retry semantics.

### Review lifecycle

Project review may conceptually include:

~~~text
submitted
→ awaiting evaluation
→ under review
→ result available
~~~

Internal grader-operational states may be richer.

They should not automatically be exposed to learners.

### Learner-facing state rule

Expose a state when it materially changes:

- learner expectation;
- available action;
- waiting condition;
- result;
- recovery path.

### Device capability

If project execution or submission requires capabilities unavailable on the current device:

- communicate limitation before substantial work where feasible;
- preserve context;
- identify supported environment;
- provide continuation path.

### Boundary

Hosted IDE, notebook, sandbox, or persistent technical workspace behavior is not defined here.

If such a workspace becomes a concrete product requirement, conditional Track E research must be activated.

**Decision state: LOCKED submission experience contract; OPEN artifact and workspace implementation**

---

## 15. Feedback and Revision Contract

### Primary job

Feedback should help the learner answer:

~~~text
What succeeded?
What did not meet expectation?
Why?
What should I do next?
~~~

A score or status alone may be insufficient.

### Feedback traceability

Where assessment uses criteria, feedback should remain traceable to the relevant:

- criterion;
- attempt;
- artifact;
- evaluation result.

### Feedback levels

Depending on assessment type, feedback may exist at:

- overall assessment level;
- criterion level;
- artifact/file level;
- inline annotation level;
- attempt level.

Not every assessment requires every feedback level.

### Result versus feedback

The interface should distinguish where necessary:

- outcome;
- score;
- feedback;
- required learner action.

Example:

~~~text
outcome = changes required
feedback = criterion-specific explanation
next action = revise and resubmit
~~~

### Evaluation complete versus released

If moderation or delayed release exists:

~~~text
evaluation complete
≠
result available to learner
~~~

The UI must represent the actual domain state truthfully.

Exact release policy remains OPEN.

### Revision

When revision is allowed, the learner should understand:

- what requires change;
- whether prior work remains available;
- whether a new attempt/version will be created;
- whether previous feedback remains accessible;
- what must happen before resubmission.

### Attempt history

Meaningful attempt history should not be silently overwritten.

Where history matters, feedback must remain associated with the attempt it evaluates.

### Changes required

A `changes required` state should connect clearly to:

- relevant feedback;
- affected criteria where applicable;
- revision path;
- resubmission action where allowed.

### Passed/completed

A successful evaluation must not automatically imply broader course completion unless authoritative completion rules establish that relationship.

### Waiting state

Learners should be able to distinguish:

~~~text
action required from me
~~~

from:

~~~text
waiting for review/system
~~~

### Appeals and review escalation

Formal appeals, moderation, and adjudication policy remain OPEN.

If activated later, their learner-facing workflow must be modeled explicitly rather than improvised in generic feedback UI.

### Accessibility

Feedback must remain understandable:

- without color alone;
- without spatial position alone;
- in logical reading order;
- with criterion/result associations preserved.

Dynamic release or status changes must follow accessible status-message principles.

**Decision state: LOCKED feedback/revision contract; OPEN appeals, moderation, and release policy**


---

## 16. Completion and Credential Contract

### Completion authority

Course or program completion is an authoritative domain state.

The frontend must not infer completion merely from:

- reaching the final lesson;
- viewing all content;
- local progress percentage;
- a successful single assessment;

unless domain policy explicitly defines those conditions as sufficient.

### Completion requirements

Where applicable, the learner should be able to understand what remains before completion.

Requirements may include:

- required lessons;
- required assessments;
- accepted project;
- required score;
- prerequisite activity;
- other explicitly defined completion conditions.

Exact completion rules remain LMS domain policy.

### Completion state

When completion is established, the experience should communicate:

- what was completed;
- completion status;
- relevant completion date where appropriate;
- next meaningful action.

### Completion versus credential

~~~text
course completed
≠
credential necessarily issued
~~~

Credential eligibility, generation, verification, or release may have additional domain rules.

These states must remain distinguishable.

### Credential availability

Where credentials exist, the learner should be able to understand:

- whether a credential is available;
- what it represents;
- whether additional action is required;
- how to access or verify it where supported.

### Claims

Credential language must not overstate what the learner has demonstrated.

Do not use terminology such as:

- certified;
- accredited;
- professional qualification;
- mastery;

unless the underlying product and policy legitimately support that claim.

### Failure and delay

If completion is established but credential generation or retrieval fails, the interface must not revert or misrepresent the authoritative completion state.

Credential-processing failure should be represented separately.

### Next action

Completion should connect to a meaningful next action where appropriate.

Possible actions may include:

- view credential;
- review completed course;
- continue program;
- return to learning dashboard.

Optional recommendations remain secondary.

### Accessibility

Completion and credential states must remain programmatically understandable and must not rely only on celebratory visual treatment.

### Celebration boundary

Celebratory motion or visual enhancement may supplement completion.

It must not:

- obscure completion information;
- block continuation;
- violate motion/accessibility requirements;
- become the only indication that completion occurred.

**Decision state: LOCKED experience contract; OPEN completion policy and credential implementation**

---

## 17. Responsive Capability Contract

### Core rule

Responsive behavior preserves learner outcome and domain semantics.

It does not require identical presentation on every device.

### Capability classification

Each critical learner workflow should eventually be classified as:

~~~text
FULL
ADAPTED
LIMITED
UNSUPPORTED-WITH-EXPLICIT-HANDOFF
~~~

### FULL

The essential learner outcome can be completed without material capability loss.

### ADAPTED

The same learner outcome remains available through a materially different responsive interaction.

### LIMITED

A useful subset remains available, but limitations must be explicit.

### UNSUPPORTED-WITH-EXPLICIT-HANDOFF

A workflow legitimately requires another supported environment.

The learner must understand:

- what is unavailable;
- what environment is required;
- whether current state is preserved;
- how to continue later.

### Default expectation

Critical ordinary LMS workflows should target FULL or ADAPTED capability unless a genuine technical, pedagogical, security, or assessment constraint prevents it.

### Responsive presentation

Responsive implementation may change:

- spatial arrangement;
- navigation presentation;
- content density;
- progressive disclosure;
- persistent versus temporary surfaces.

It must preserve:

- learner orientation;
- primary task;
- critical state;
- required information;
- accessibility.

### Orientation

Ordinary LMS workflows must not require a single device orientation unless orientation is genuinely essential.

### Reflow

Page-level horizontal scrolling should not be required for ordinary content at supported reflow conditions.

Genuinely two-dimensional content may use localized scrolling or another semantically appropriate adaptation.

### Domain state preservation

Viewport or orientation changes must not unnecessarily reset:

- learner input;
- assessment response;
- media position;
- current lesson;
- progress state.

Responsive presentation state and domain state are distinct.

### Unsupported workflow handoff

If a workflow cannot be completed on the current device, limitation should be disclosed before substantial learner work where feasible.

A useful handoff should:

~~~text
identify limitation
→ preserve context
→ explain required environment
→ provide continuation path
~~~

### Offline boundary

Offline capability is not assumed globally.

If introduced, supported offline behavior must be explicitly classified.

Potential capability semantics may include:

~~~text
AVAILABLE_OFFLINE
READ_ONLY_OFFLINE
QUEUE_FOR_SYNC
ONLINE_REQUIRED
~~~

Exact offline scope remains OPEN.

### Accessibility

Responsive transformations must preserve:

- semantic order;
- keyboard operation;
- focus behavior;
- target size;
- zoom/reflow;
- accessible disclosure state.

**Decision state: LOCKED responsive contract; OPEN per-workflow classification and implementation**

---

## 18. Learner-Facing State and Recovery Contract

### Purpose

Learner-facing state exists to help the learner understand:

~~~text
What happened?
What is happening?
Do I need to act?
What can I do next?
~~~

### State-model principle

Frontend learner state should not mechanically mirror backend operational state.

Backend state may be more detailed.

Learner-facing state should expose distinctions that materially affect:

- expectation;
- action;
- waiting;
- result;
- recovery.

### Domain-state separation

Where appropriate, separate concepts such as:

~~~text
work state
submission state
evaluation state
completion state
credential state
~~~

rather than overloading one status field.

### Example

A project may simultaneously be:

~~~text
work = saved
submission = submitted
evaluation = under_review
completion = incomplete
~~~

These dimensions are not inherently contradictory.

### Authoritative state

The UI must distinguish between:

- local/transient state;
- pending operation;
- authoritative confirmed state.

For example:

~~~text
submitting
≠
submitted
~~~

and:

~~~text
saving
≠
saved
~~~

### Waiting versus action required

The learner must be able to distinguish:

~~~text
waiting on system/reviewer
~~~

from:

~~~text
action required from learner
~~~

This distinction affects dashboard priority and next-action logic.

### Failure categories

Material failures should be represented according to their consequence rather than collapsed into a generic error.

Potential categories include:

- validation failure;
- persistence failure;
- network failure;
- submission failure;
- processing failure;
- evaluation failure;
- content retrieval failure;
- authorization/access failure;
- unsupported capability.

### Recovery contract

Where relevant, recovery should answer:

~~~text
What failed?
What state was preserved?
Did the consequential action succeed?
Can I retry safely?
What should I do next?
~~~

### Preserve before discard

Preferred recovery strategy is:

~~~text
preserve
→ explain
→ recover/retry
→ escalate when necessary
~~~

not:

~~~text
fail
→ discard
→ restart
~~~

### Retry safety

If retry can produce duplicate consequential actions, backend/API contracts must provide appropriate safety semantics.

The exact technical mechanism is outside this profile.

The learner experience requires retry behavior to be understandable and safe.

### Status communication

Dynamic states such as:

- saving;
- saved;
- upload complete;
- submission received;
- review complete;
- changes required;

must be communicated accessibly where they materially affect the learner.

### Error specificity

Error messages should be specific enough to support recovery without exposing:

- sensitive authorization internals;
- security-sensitive implementation detail;
- irrelevant system diagnostics.

### Unknown state

When authoritative state cannot be determined, the interface should not fabricate certainty.

A temporary unknown/retry state is preferable to a false success or false failure.

### Logging boundary

Observability and diagnostic logging belong to implementation/backend architecture.

Learner-facing error language should not substitute for operational telemetry.

**Decision state: LOCKED state/recovery contract; OPEN exact state vocabulary and backend representation**


---

## 19. Accessibility Validation Contract

### Baseline

The LMS inherits the PES accessibility baseline:

**WCAG 2.2 AA**

Accessibility is part of functional correctness.

Passing visual review or automated tooling alone is not sufficient.

### Critical workflow coverage

Accessibility validation must cover the critical learner workflows defined by this profile, including:

- authentication entry where applicable;
- Learner Dashboard;
- Resume Learning;
- Course Discovery;
- Course Overview;
- Curriculum Navigation;
- Lesson Experience;
- media interaction;
- Assessment;
- Project Submission;
- feedback/revision;
- completion/credential access.

### Manual validation

Manual validation must include, where applicable:

- keyboard-only operation;
- focus visibility;
- meaningful focus order;
- screen-reader interpretation;
- reflow;
- zoom/text resize;
- error identification;
- dynamic status communication;
- responsive navigation;
- media accessibility.

### Automated validation

Automated accessibility testing should be used for repeatable detection of machine-detectable failures.

It does not establish full accessibility conformity.

### Semantic integrity

Responsive or visual transformations must not destroy:

- heading structure;
- landmark structure;
- form relationships;
- accessible names;
- expanded/collapsed state;
- current-item semantics;
- error relationships;
- criterion/feedback association.

### Focus behavior

Focus management must be explicitly validated for interactions such as:

- opening/closing temporary navigation;
- dialogs where used;
- submission confirmation;
- error recovery;
- dynamic route/content transition;
- returning from secondary lesson surfaces.

### Status changes

Material asynchronous changes should be programmatically communicated where appropriate.

Examples include:

- save success/failure;
- upload completion;
- submission receipt;
- result availability;
- changes required.

### Media

Media accessibility requirements must follow actual content type and applicable standards.

Do not convert optional product enhancement into a false universal WCAG requirement.

For example, transcript support may be desirable and valuable without being represented as universally required for every prerecorded synchronized video under WCAG 2.2 AA.

### Motion

Motion should respect PES accessibility principles.

Do not assume that every reduced-motion product behavior is itself a universal WCAG 2.2 AA requirement.

### Release gate

A critical learner workflow with unresolved severe accessibility blockers must not be considered production-ready merely because the functional happy path succeeds.

Exact severity taxonomy and CI enforcement belong to the Implementation Profile.

**Decision state: LOCKED validation contract; OPEN tooling and enforcement mechanism**

---

## 20. Content and Language Contract

### Content-design principle

Learner-facing content is part of the experience contract.

Labels and messages should help the learner understand:

~~~text
state
meaning
required action
next step
~~~

### Action language

Actions should use language that communicates consequence.

Prefer meaningful labels such as:

~~~text
Submit Project
Resume Lesson
Review Feedback
Continue Assessment
~~~

over ambiguous labels such as:

~~~text
Go
OK
Process
Continue
~~~

when context does not make the consequence clear.

### State language

Learner-facing vocabulary must distinguish materially different states.

Examples:

~~~text
Draft
Submitting
Submitted
Under Review
Changes Required
Completed
~~~

Exact canonical vocabulary remains PROVISIONAL until domain/API state contracts are finalized.

### Error language

Error content should:

- identify the failed action;
- explain impact where known;
- explain preservation state where material;
- provide a recovery action when available.

Avoid exposing raw internal exceptions or implementation diagnostics.

### Empty states

Empty state content should distinguish between conditions such as:

- no enrollment yet;
- no active learning;
- no completed courses;
- no recommendations;
- data temporarily unavailable.

These states should not all use the same generic empty message.

### Time and deadline language

Where deadlines or timestamps matter, experience should avoid ambiguity about:

- date;
- time;
- timezone where relevant;
- late/cut-off consequences.

Exact formatting belongs to localization and implementation policy.

### Internationalization readiness

LMS experience contracts must not assume that English string length, grammar, pluralization, or word order are universal.

Implementation should permit localization without requiring domain-contract redesign.

### Layout implication

UI implementation must tolerate reasonable text expansion and different content lengths.

Do not make semantic meaning depend on a fixed English label fitting one exact visual width.

### Terminology governance

Domain terms such as:

- course;
- lesson;
- module;
- project;
- assessment;
- completion;
- credential;
- mastery;

must be used consistently once canonical terminology is established.

Do not introduce synonyms casually when they imply different domain states.

### Localization boundary

This profile does not lock:

- supported languages;
- translation platform;
- locale library;
- content-management workflow;
- machine-translation policy.

Those remain OPEN until product requirements activate them.

**Decision state: LOCKED content-design principles; OPEN localization implementation and canonical vocabulary details**

---

## 21. Measurement and Acceptance Contract

### Purpose

The LMS should be validated against observable learner outcomes, not visual polish alone.

### Experience-quality questions

Validation should determine whether learners can successfully answer and act on questions such as:

~~~text
Where am I?
What am I learning?
What have I completed?
What remains?
What requires my attention?
What should I do next?
Did my consequential action succeed?
~~~

### Candidate measures

Depending on workflow, useful measures may include:

- time-to-resume;
- task completion rate;
- next-action identification;
- blocker recognition;
- progress comprehension;
- submission-status comprehension;
- error recovery success;
- unnecessary navigation;
- accessibility defects;
- responsive continuity failures.

### Correctness before optimization

A workflow that is fast but produces incorrect state interpretation is not successful.

For example:

~~~text
fast submission
+
uncertain receipt
=
failed experience
~~~

### Dashboard acceptance direction

Learners should be able to:

- identify active learning;
- resume meaningful work;
- recognize required attention;
- interpret progress correctly.

### Curriculum acceptance direction

Learners should be able to:

- identify current location;
- navigate surrounding curriculum;
- understand meaningful item states;
- return to learning context.

### Assessment acceptance direction

Learners should be able to:

- understand submission requirements;
- distinguish draft from submitted state;
- determine whether submission succeeded;
- understand review/result state;
- identify revision action where required.

### Responsive acceptance direction

Critical workflows should retain their classified learner outcome at supported responsive conditions.

### Accessibility acceptance direction

Critical workflows must pass the required accessibility validation appropriate to the milestone and release stage.

### Threshold boundary

Exact quantitative thresholds remain PROVISIONAL until:

- reference implementation exists;
- representative content exists;
- usability testing provides baseline evidence.

### Anti-metric rule

Do not define LMS experience success solely through:

- page views;
- clicks;
- session duration;
- recommendation CTR;
- number of dashboard cards.

These may be operational signals but are not sufficient learner-experience acceptance criteria.

**Decision state: LOCKED acceptance model; PROVISIONAL quantitative thresholds**

---

## 22. AI and Coding-Agent Consumption Contract

### Purpose

AI coding agents are explicit consumers of the CodeInteX experience architecture.

Agents must be able to distinguish:

~~~text
LOCKED requirement
PROVISIONAL choice
OPEN decision
implementation freedom
~~~

### Normative source order

Agents working on LMS implementation must consume requirements in the established authority order.

They must not treat:

- benchmark artifacts;
- library defaults;
- generated UI;
- existing provisional implementation;

as higher authority than the normative PES/LMS contracts.

### No invented domain policy

An agent must not silently invent rules for:

- completion;
- pass/fail;
- attempt limits;
- deadline behavior;
- credential eligibility;
- progress weighting;
- mastery;
- enrollment eligibility.

When required policy is absent, the implementation must preserve the uncertainty explicitly.

### No invented learner state

Agents must not fabricate authoritative success state in client code.

Examples include locally declaring:

- submitted;
- passed;
- completed;
- credentialed;

without the relevant authoritative contract.

### PES dependency

Agents implementing LMS UI must consume PES semantics through the appropriate Implementation Profile.

They must not create a parallel local design foundation for:

- colors;
- spacing;
- typography;
- interaction semantics;
- accessibility behavior;
- generic component contracts.

### Semantic-token rule

Where PES semantic tokens exist, implementations should consume them rather than embedding arbitrary product-local visual constants.

Exact token serialization remains an Implementation Profile concern.

### UI-library boundary

Agents may use approved implementation libraries when defined by the Implementation Profile.

Library defaults do not override:

- accessibility requirements;
- component semantics;
- LMS domain contracts;
- PES interaction requirements.

### Handling unresolved decisions

When implementation reaches an unresolved requirement, agents should mark it explicitly using project conventions such as:

~~~text
PES-DEPENDENCY
PROVISIONAL-UI
OPEN-PES-DECISION
OPEN-LMS-POLICY
~~~

rather than silently locking a choice through code.

### Refactoring rule

Existing provisional UI may be replaced when it conflicts with a higher-authority contract.

Backward compatibility with an incorrect provisional UX is not automatically required.

### Generated content

AI-generated learner-facing copy must follow the Content and Language Contract and must not invent:

- credential claims;
- mastery claims;
- assessment results;
- authoritative learner state.

### Security and privacy boundary

AI agents must not expose sensitive backend/internal state merely to simplify learner-facing diagnostics.

### Auditability

Material AI-generated implementation decisions should remain reviewable through normal repository artifacts such as:

- code;
- tests;
- decision references;
- implementation documentation.

**Decision state: LOCKED agent-consumption contract**


---

## 23. Implementation Handoff Contract

### Purpose

This profile is intended to be consumed by implementation workstreams without requiring them to reinterpret benchmark evidence independently.

The next implementation-facing artifact is:

`WEB-IMPLEMENTATION-PROFILE-v0.1.md`

### Handoff principle

The Web Implementation Profile must translate this product experience profile into technology-specific implementation rules while preserving:

- learner semantics;
- accessibility requirements;
- responsive behavior;
- state truthfulness;
- domain boundaries;
- implementation replaceability.

### Required implementation inputs

Before a learner-facing implementation is considered aligned, it must consume:

- PES Foundation Decision Model;
- PES Consumption Contract;
- LMS Experience Profile;
- relevant backend/API contracts;
- Web Implementation Profile once established.

### Backend/API expectations

Implementation requires backend/API contracts capable of expressing the learner-visible states required by this profile.

Examples include, where applicable:

- enrollment/access state;
- current learning position;
- progress semantics;
- completion state;
- assessment attempt state;
- submission state;
- evaluation state;
- result/feedback state;
- credential state.

### Contract mismatch rule

If the frontend requires learner-visible semantics that the backend/API cannot represent truthfully:

~~~text
do not invent the missing state in the UI
~~~

The mismatch must be escalated to the relevant domain/backend workstream.

### Implementation freedom

Implementation remains free to choose appropriate:

- component composition;
- responsive layout;
- routing structure;
- state-management mechanism;
- rendering strategy;
- approved UI primitives;

provided those choices do not violate higher-authority contracts.

### Provisional implementation

Before the Web Implementation Profile is locked, LMS UI implementation may continue as:

~~~text
PROVISIONAL-UI
~~~

where necessary.

Such implementation must not establish a competing design or experience authority.

### Reference implementation role

The first integrated learner experience acts as a validation vehicle for:

- profile completeness;
- implementation feasibility;
- responsive behavior;
- accessibility;
- state-contract adequacy;
- real-content usability.

Reference implementation may reveal defects in this profile.

If evidence contradicts a profile decision, revise the profile through governance rather than preserving an incorrect contract for consistency.

### Testing implication

Implementation should eventually provide tests covering:

- critical state transitions;
- failure/recovery behavior;
- accessibility-sensitive interactions;
- responsive invariants;
- authoritative success states;
- domain-to-UI mapping.

Exact test framework belongs to the Web Implementation Profile.

**Decision state: LOCKED handoff contract; OPEN implementation mechanics**

---

## 24. Decision-State Register

This section summarizes major decision states established by this profile.

### LOCKED

The following are LOCKED for the v0.1 profile baseline:

1. LMS is a consumer of PES Core.
2. LMS domain experience is separated from generic PES Core semantics.
3. Backend/domain models must not leak directly into learner UI contracts.
4. Critical learner workflows require explicit recovery behavior.
5. Accessibility is part of functional correctness.
6. Responsive adaptation must preserve learner semantics and critical tasks.
7. Learner Dashboard prioritizes continuity, required attention, and meaningful next action.
8. Course Discovery must support meaningful learner comparison rather than catalog exposure alone.
9. Course Overview must clarify outcomes, requirements, structure, and entry state.
10. Curriculum Navigation must preserve learner orientation and authoritative item state.
11. Lesson Experience prioritizes the primary learning activity and preserves context.
12. Resume Learning must restore meaningful learning context rather than blindly reopen the last URL.
13. Progress requires explicit semantics and must not collapse activity, completion, proficiency, and mastery.
14. Assessment is a workflow with truthful draft/submission/evaluation distinctions.
15. Project Submission requires work-preservation and durable receipt semantics.
16. Feedback must support meaningful learner action and preserve attempt/criterion traceability where applicable.
17. Completion and credential state are distinct concepts.
18. Responsive capability may vary by workflow, but limitations require explicit handoff.
19. Learner-facing state must expose meaningful distinctions without mechanically mirroring backend operational state.
20. Critical learner workflows require manual and automated accessibility validation.
21. Learner-facing content is part of the experience contract.
22. Experience acceptance must evaluate learner understanding and task outcomes, not visual polish alone.
23. AI coding agents are explicit consumers of the normative architecture and must not invent domain policy.
24. Implementation must escalate missing domain semantics rather than fabricating authoritative state.

### PROVISIONAL

The following remain PROVISIONAL:

- quantitative UX acceptance thresholds;
- canonical learner-facing status vocabulary;
- exact dashboard prioritization signals;
- exact resume-target algorithm;
- exact responsive workflow classifications;
- some content terminology pending domain stabilization.

### OPEN

The following remain explicitly OPEN:

- final visual language;
- final dashboard layout;
- final course-discovery taxonomy;
- catalog ranking/search implementation;
- exact curriculum taxonomy;
- exact lesson-type composition;
- exact progress calculation and aggregation;
- assessment grading policy;
- attempt limits;
- late-submission policy;
- accommodation policy details;
- timed-assessment policy;
- AI evaluation authority;
- moderation and appeals;
- completion policy details;
- credential implementation;
- native app strategy;
- PWA strategy;
- offline LMS scope;
- cross-device synchronization architecture;
- hosted technical workspace;
- canonical implementation libraries until Web Implementation Profile resolves them.

### Interpretation

`OPEN` does not mean implementation may choose arbitrarily.

It means:

~~~text
decision not yet authorized at this layer
~~~

If implementation encounters an OPEN item that materially blocks progress, it must be resolved through the owning workstream.

**Decision state: LOCKED register**

---

## 25. Open Items and Activation Triggers

Open decisions should be resolved only when required by product scope or implementation evidence.

### Hosted technical workspace

Current state:

`OPEN / NOT ACTIVATED`

Activate Track E research if CodeInteX commits to a learner-facing:

- hosted IDE;
- notebook;
- coding sandbox;
- persistent lab environment;
- similar technical workspace.

Do not define its experience contract before that requirement exists.

---

### Offline learning

Current state:

`OPEN`

Activate deeper offline design when product scope requires meaningful learning without continuous connectivity.

Required decisions would include:

- offline-capable content;
- local state;
- synchronization;
- conflict handling;
- expiry;
- assessment restrictions.

---

### Native application

Current state:

`OPEN`

Do not infer a native mobile application requirement from responsive-web requirements.

Activate only from validated product/distribution needs.

---

### Mastery model

Current state:

`OPEN`

Activate only if CodeInteX intends to make learner proficiency or mastery claims beyond completion.

Required evidence would include:

- mastery definition;
- evidence model;
- reassessment;
- decay/change semantics;
- completion relationship.

---

### AI-assisted assessment

Current state:

`OPEN`

Activate explicit governance before AI output becomes consequential to:

- pass/fail;
- certification;
- credential eligibility;
- formal learner evaluation.

The governance must define authority, review, provenance, and escalation.

---

### Appeals and moderation

Current state:

`OPEN`

Activate when assessment policy requires:

- formal appeal;
- moderation;
- second review;
- adjudication;
- result-release control.

---

### Localization

Current state:

`OPEN`

Activate implementation-specific localization decisions when supported locales become product requirements.

Content and layout remain internationalization-ready meanwhile.

---

### Trigger discipline

Do not resolve an OPEN item merely because:

- a framework supports it;
- a benchmark has it;
- a library makes it easy;
- it appears sophisticated;
- it may be useful someday.

Resolve it when requirements, evidence, or implementation constraints justify the cost.

**Decision state: LOCKED activation discipline**

---

## 26. Profile Completion Gate

The LMS Experience Profile v0.1 may proceed to implementation profiling when it provides coherent contracts for the current critical learner experience.

### Required domain contracts

Current status:

~~~text
Profile authority and boundary: PASS
Critical learner workflows: PASS
Global experience invariants: PASS
Learner Dashboard: PASS
Course Discovery: PASS
Course Overview: PASS
Curriculum Navigation: PASS
Lesson Experience: PASS
Resume Learning: PASS
Progress: PASS
Assessment: PASS
Project Submission: PASS
Feedback and Revision: PASS
Completion and Credentials: PASS
Responsive Capability: PASS
Learner-facing State and Recovery: PASS
Accessibility Validation: PASS
Content and Language: PASS
Measurement and Acceptance: PASS
AI / Coding-Agent Consumption: PASS
Implementation Handoff: PASS
Decision-State Governance: PASS
~~~

### Evidence dependency

Mandatory specialist research status:

~~~text
Track A — Accessibility: PASS
Track B — Assessment / Project Workflow: PASS
Track C — Mobile / Responsive Lesson Experience: PASS
Track D — Actionable Dashboard / Progress: PASS
Track E — Hosted Workspace: NOT ACTIVATED
~~~

### Remaining uncertainty

Remaining OPEN and PROVISIONAL decisions are either:

- implementation-specific;
- product-policy-specific;
- conditional future scope;
- expected to be validated by reference implementation.

They do not currently prevent Web Implementation Profile work.

### Completion conclusion

**LMS EXPERIENCE PROFILE v0.1 COMPLETION GATE: PASS**

The profile is sufficiently specified to proceed to:

`WEB-IMPLEMENTATION-PROFILE-v0.1.md`

### Important limitation

`PASS` means:

~~~text
sufficient normative baseline for the next architecture layer
~~~

It does not mean:

- final UX;
- final visual design;
- implementation complete;
- usability proven;
- accessibility conformance certified;
- all LMS product policy resolved.

**Decision state: LOCKED for current milestone**

---

## 27. Document Status

This document is:

**PROVISIONAL PROFILE BASELINE — v0.1**

It is normative for the current CodeInteX LMS learner-experience milestone.

Its LOCKED decisions should be treated as requirements unless formally revised.

Its PROVISIONAL decisions require validation.

Its OPEN decisions must not be silently converted into implementation policy.

### Next normative artifact

`WEB-IMPLEMENTATION-PROFILE-v0.1.md`

That artifact should define how the current web implementation consumes:

- PES Core;
- LMS Experience Profile;
- semantic tokens;
- component contracts;
- interaction primitives;
- accessibility requirements;
- responsive behavior;
- framework/runtime choices.

Technology choices remain subordinate to the experience contracts defined here.

### Revalidation

This profile should be revisited when:

- reference implementation exposes a contradiction;
- usability evidence invalidates a requirement;
- accessibility testing exposes a systemic gap;
- LMS domain policy materially changes;
- new critical learner workflow enters scope;
- Track E or another conditional research track becomes activated.
