# CodeInteX LMS — Mobile and Responsive Lesson Experience Evidence v0.1

- **Project:** CodeInteX
- **Workstream:** PES / LMS
- **Research track:** Track C — Mobile / Responsive Lesson Experience
- **Status:** EVIDENCE BASELINE — PROVISIONAL
- **Version:** 0.1
- **Date:** 2026-09-19
- **Primary LMS benchmark:** Udacity
- **Specialist benchmarks:** Udemy Business Mobile Course Player; edX Mobile
- **Depends on:**
  - `../PES-FOUNDATION-DECISION-MODEL-v0.1.md`
  - `../PES-CONSUMPTION-CONTRACT-v0.1.md`
  - `LMS-SPECIALIST-BENCHMARK-PLAN-v0.1.md`
  - `UDACITY-LEARNER-EXPERIENCE-EVIDENCE-v0.1.md`
  - `ACCESSIBILITY-CRITICAL-LEARNER-WORKFLOWS-EVIDENCE-v0.1.md`

---

## 0. Purpose

Dokumen ini mengumpulkan evidence untuk mendefinisikan mobile dan responsive experience contracts CodeInteX LMS.

Research questions utama:

- bagaimana learner mempertahankan orientation pada narrow viewport;
- bagaimana curriculum navigation beradaptasi;
- bagaimana lesson content, media, transcript, dan resources coexist;
- kapan progressive disclosure diperlukan;
- bagaimana technical/two-dimensional content ditangani;
- bagaimana progress dan next action tetap discoverable;
- workflow apa yang harus usable di mobile;
- workflow apa yang secara legitimate membutuhkan larger-screen capability.

Dokumen ini tidak menentukan breakpoint CSS atau framework implementation.

**Decision state: LOCKED untuk evidence interpretation process**

---

## 1. Benchmark Selection Decision

### Existing evidence

Udacity tetap primary learner-experience benchmark.

Namun public Udacity evidence tidak cukup untuk mengunci mobile/responsive lesson behavior secara detail.

### Specialist benchmark 1

`Udemy Business Mobile Course Player`

dipilih karena current official documentation memperlihatkan mobile learner flow yang konkret:

- enter course dari My Learning;
- start/resume course;
- curriculum items tersedia dalam mobile course player;
- lesson/course items dapat dipilih;
- video controls tersedia pada mobile player;
- course resources tersedia melalui secondary `More` surface.

Ini membantu menjawab:

- curriculum visibility;
- lesson navigation;
- mobile player composition;
- progressive disclosure untuk resources.

### Specialist benchmark 2

`edX Mobile`

ditambahkan karena Udemy saja tidak cukup menjawab capability-boundary question.

Current edX documentation menunjukkan:

- most course assignments dapat dilakukan di app;
- course videos dapat dikonsumsi;
- handouts/announcements dapat dibaca;
- discussion dapat digunakan;
- video dapat di-download;
- beberapa advanced problem types mungkin memerlukan browser;
- timed/proctored exams tidak tersedia melalui app.

Ini memberikan evidence bahwa:

~~~text
mobile access
≠
every workflow must have identical capability
~~~

### Why two specialist benchmarks are justified

Benchmark kedua bukan tambahan kosmetik.

Ia menjawab unresolved question:

> Workflow mana yang realistis mobile-capable dan kapan explicit larger-screen handoff dapat diterima?

### No third benchmark

Tidak ada benchmark ketiga yang diperlukan sekarang.

**Decision state: LOCKED untuk Track C benchmark set v0.1**

---

## 2. Source Register

### C01 — Udacity Learner Experience Evidence

Internal CodeInteX artifact:

`UDACITY-LEARNER-EXPERIENCE-EVIDENCE-v0.1.md`

Relevant evidence:

- learner continuity;
- curriculum navigation;
- lesson consumption;
- Audio Slides mobile behavior;
- progress;
- resource access.

Evidence class: EXISTING PRIMARY BENCHMARK.

---

### C02 — Accessibility Critical Learner Workflows Evidence

Internal CodeInteX artifact:

`ACCESSIBILITY-CRITICAL-LEARNER-WORKFLOWS-EVIDENCE-v0.1.md`

Relevant evidence:

- reflow;
- zoom;
- orientation;
- keyboard;
- focus;
- target size;
- semantic order.

Evidence class: AUTHORITATIVE-DERIVED INTERNAL EVIDENCE.

---

### C03 — Udemy Business Mobile Course Player

Official Udemy Business support documentation.

Article:

`How to access and use the mobile course player`

Observed current behavior includes:

- My Learning entry point;
- course start;
- mobile course-player curriculum;
- scroll-and-select lesson navigation;
- video player controls;
- resource access through secondary navigation.

Evidence class: CURRENT OFFICIAL PRODUCT DOCUMENTATION.

---

### C04 — edX Mobile Capabilities

Official edX Help Center.

Article:

`What can I do on the edX app?`

Updated: 2026-09-16.

Observed behavior includes:

- enroll;
- most course assignments;
- course videos;
- handouts;
- announcements;
- discussions;
- offline video download.

Evidence class: CURRENT OFFICIAL PRODUCT DOCUMENTATION.

---

### C05 — edX Mobile Assignment Capability

Official edX Help Center.

Article:

`What types of assignments can be done in the edX app?`

Relevant evidence:

- most assignments can be attempted;
- some complex interactions require a browser;
- timed/proctored exams cannot be taken in the app.

Evidence class: OFFICIAL PRODUCT DOCUMENTATION.

---

### C06 — edX Supported Devices and Limitations

Official edX Help Center.

Article:

`What are the system requirements and supported browsers on edX?`

Updated: 2026-08-19.

Relevant evidence:

- mobile browser support;
- Android/iOS app support;
- some advanced content may not function on mobile.

Evidence class: CURRENT OFFICIAL PRODUCT DOCUMENTATION.

---

### C07 — WCAG Responsive Constraints

W3C/WAI evidence includes:

- SC 1.3.4 Orientation;
- SC 1.4.4 Resize Text;
- SC 1.4.10 Reflow;
- SC 2.5.8 Target Size (Minimum).

Evidence class: AUTHORITATIVE STANDARD.

---

## 3. Responsive Experience Principle

### Core conclusion

Responsive LMS experience is not:

~~~text
desktop layout
→ shrink width
~~~

Responsive experience is:

~~~text
preserve learner intent
+
preserve state
+
preserve hierarchy
+
adapt presentation and interaction
~~~

### Requirement candidate

At different viewport sizes, CodeInteX may change:

- spatial arrangement;
- navigation presentation;
- content density;
- disclosure strategy;
- control placement;
- persistent versus temporary surfaces.

It must preserve:

- learner orientation;
- domain semantics;
- required information;
- primary actions;
- accessibility;
- learner progress/state.

### Anti-pattern

A desktop UI that technically fits on a phone but creates:

- excessive horizontal scrolling;
- inaccessible controls;
- hidden primary actions;
- lost curriculum context;
- unreadable dense panels;

is not considered responsive success.

**Disposition: ADOPT**

**Decision state: LOCKED principle**

---

## 4. Mobile Capability Is Not Necessarily Desktop Parity

### Evidence

edX explicitly supports substantial learning activity on mobile while documenting that some advanced problem types and timed/proctored exams require another environment.

### Inference

Responsive design does not require every workflow to have identical presentation or capability on every device.

However:

~~~text
unsupported without explanation
~~~

is not acceptable.

### Requirement candidate

For each critical LMS workflow, CodeInteX should classify mobile behavior as one of:

~~~text
FULL
ADAPTED
LIMITED
UNSUPPORTED-WITH-EXPLICIT-HANDOFF
~~~

### FULL

Same essential task can be completed on mobile.

### ADAPTED

Same learner outcome is achievable through a different mobile interaction.

### LIMITED

Useful subset is available, with limitations clearly communicated.

### UNSUPPORTED-WITH-EXPLICIT-HANDOFF

Workflow legitimately requires another environment.

The learner must be told:

- what cannot be done;
- why or what environment is required;
- whether current work/state is preserved;
- how to continue later.

### Anti-pattern

Do not discover device incompatibility only after the learner has invested substantial work.

**Disposition: ADOPT**

**Decision state: LOCKED classification principle; OPEN workflow classifications**

---

## 5. Curriculum Orientation on Narrow Viewports

### Problem

Desktop learning interfaces can keep curriculum and lesson content visible simultaneously.

Narrow viewports often cannot.

Removing persistent curriculum navigation creates risk that learners lose:

- current position;
- surrounding context;
- next/previous relationship;
- course hierarchy.

### Evidence

Udemy mobile course player keeps curriculum items accessible in the lesson/player experience.

Moodle and other mature mobile learning systems also demonstrate that mobile navigation often prioritizes contextually relevant content rather than preserving full desktop chrome.

### Requirement candidate

When persistent curriculum navigation cannot remain visible, learner orientation must survive through alternate mechanisms.

Potential mechanisms include:

- compact current-location indicator;
- curriculum drawer/sheet;
- lesson list below primary content;
- previous/next navigation;
- breadcrumb-like context where useful;
- explicit return-to-curriculum action.

### Required invariant

The learner must be able to answer:

~~~text
Where am I?
What is this part of?
What comes next?
How do I return to the curriculum?
~~~

### Boundary

This requirement does not lock:

- sidebar;
- drawer;
- bottom sheet;
- accordion;
- tab;
- route structure.

Those remain Implementation Profile concerns.

**Disposition: ADOPT**

**Decision state: LOCKED orientation invariant; OPEN presentation**

---

## 6. Lesson Player Composition

### Evidence

Udemy's mobile course player combines:

- primary learning media;
- course curriculum access;
- media controls;
- secondary resources.

Resources are not necessarily kept permanently visible; they can be accessed through secondary navigation.

### Inference

On constrained screens, not every lesson-support surface deserves equal persistent visual priority.

### Requirement candidate

Lesson composition should prioritize approximately:

~~~text
primary learning activity
→ immediate lesson controls
→ current/next navigation
→ context/resources
→ secondary metadata
~~~

Exact hierarchy depends on lesson type.

### Example

For a video lesson:

~~~text
video / media
→ playback controls
→ lesson identity
→ next/current navigation
→ transcript/resources
→ secondary course information
~~~

For a text lesson, the hierarchy may differ.

### Anti-pattern

Do not force desktop multi-column composition onto mobile merely for visual consistency.

**Disposition: ADOPT**

**Decision state: LOCKED prioritization principle; OPEN exact composition**

---

## 7. Progressive Disclosure on Mobile

### Problem

Narrow viewports create competition among:

- curriculum;
- transcript;
- resources;
- notes;
- discussion;
- progress;
- lesson content.

### Requirement candidate

Secondary surfaces may use progressive disclosure when:

- they are not required continuously;
- they remain discoverable;
- opening them does not destroy learner context;
- state remains available after closing;
- accessibility is preserved.

### Candidate secondary surfaces

Depending on lesson type:

- curriculum;
- transcript;
- resources;
- notes;
- glossary;
- supporting discussion.

### Anti-pattern

Progressive disclosure must not become:

~~~text
hide everything difficult to place
~~~

Primary learner actions and critical state should not be buried simply to achieve a visually clean screen.

**Disposition: ADOPT**

**Decision state: LOCKED principle**

---

## 8. Orientation and Device Rotation

### Evidence

WCAG 2.2 SC 1.3.4 requires content not to restrict view and operation to a single display orientation unless that orientation is essential.

### LMS requirement candidate

Ordinary LMS workflows should support both portrait and landscape operation.

Examples include:

- dashboard;
- curriculum;
- lesson reading;
- quizzes;
- progress;
- ordinary media navigation.

### Exception

A specific activity may require a particular orientation only when that orientation is genuinely essential to the information or interaction.

### Anti-pattern

Do not display:

~~~text
Rotate your device to continue
~~~

as the default solution to inadequate responsive design.

### Media consideration

Video may naturally make better use of landscape, but the surrounding learning workflow must not unnecessarily require landscape orientation.

**Disposition: ADOPT**

**Decision state: LOCKED requirement**


---

## 9. Reflow and Content Density

### Evidence

Track A established WCAG reflow and resize requirements.

Responsive adaptation must preserve information and functionality under narrow viewport and substantial zoom.

### LMS problem

Learning surfaces can contain high information density:

- curriculum hierarchy;
- lesson content;
- progress;
- media;
- resources;
- assessment controls;
- navigation;
- status information.

Attempting to preserve all desktop density on a narrow viewport can create unusable interaction.

### Requirement candidate

Responsive adaptation should reduce simultaneous visual competition without removing required information.

Possible strategies include:

- stacking;
- progressive disclosure;
- temporary navigation;
- collapsible secondary information;
- shorter contextual summaries;
- localized horizontal scrolling for genuinely two-dimensional content.

### Invariant

Reducing visible density must not reduce semantic completeness.

Content may move.

Content must not silently disappear merely because viewport width is smaller.

### Anti-pattern

Do not solve narrow viewport by:

- shrinking text below readable size;
- reducing targets below accessibility requirements;
- hiding required status;
- hiding error messages;
- removing navigation with no alternative;
- requiring page-level horizontal scrolling.

**Disposition: ADOPT**

**Decision state: LOCKED**

---

## 10. Technical and Two-Dimensional Learning Content

### Problem

Technical learning may contain:

- code;
- terminal output;
- tables;
- mathematical expressions;
- diagrams;
- data grids;
- IDE/workspace surfaces.

Some content is genuinely two-dimensional.

### Evidence interpretation

WCAG reflow permits exceptions where two-dimensional presentation is necessary for meaning or use.

This does not justify making the entire lesson horizontally scrollable.

### Requirement candidate

Two-dimensional content should be isolated within an appropriate region.

Examples:

~~~text
lesson page
    ↓
responsive prose/content
    ↓
localized scrollable code/table/diagram region
~~~

### Code

Code blocks may use localized horizontal scrolling when wrapping would materially alter readability or meaning.

Where reasonable:

- preserve indentation;
- preserve copy behavior;
- provide sufficient touch/keyboard operability;
- avoid trapping page navigation.

### Tables

Responsive strategy should depend on table semantics.

Possible strategies include:

- horizontal scrolling;
- column prioritization;
- alternative compact view;
- structured transformation.

Do not convert tables into visually attractive cards when doing so destroys relationships between rows and columns.

### Workspace boundary

Full IDE/workspace behavior remains outside current Track C unless hosted workspace scope is activated.

**Disposition: ADOPT**

**Decision state: LOCKED principle; OPEN implementation patterns**

---

## 11. Media, Transcript, and Lesson Navigation

### Evidence

Udacity supports transcript/media navigation.

Udemy mobile course player keeps curriculum accessible around the primary media experience.

Mobile screen space makes simultaneous visibility of:

- media;
- transcript;
- curriculum;
- resources;

impractical in many contexts.

### Requirement candidate

Primary media must retain sufficient priority while alternate learning surfaces remain discoverable.

Potential responsive arrangement:

~~~text
primary media
→ immediate controls
→ current lesson context
→ next/previous action
→ transcript/resources/curriculum through secondary surfaces
~~~

### Transcript

Transcript access should not require abandoning the lesson context.

Potential implementation may use:

- expandable region;
- sheet/drawer;
- dedicated tab;
- inline section.

Exact pattern remains OPEN.

### State preservation

Opening and closing transcript/resources/curriculum should preserve:

- media position where appropriate;
- lesson position;
- selected context;
- learner state.

### Anti-pattern

Do not reset media or lesson context merely because a secondary mobile surface is opened.

**Disposition: ADOPT**

**Decision state: LOCKED continuity principle; OPEN presentation**

---

## 12. Touch and Mobile Interaction

### Evidence

Track A establishes WCAG 2.2 target-size and alternative-interaction requirements.

Mobile learning creates higher dependence on touch.

### Requirement candidate

Mobile controls must be usable without requiring precision interaction.

Priority controls include:

- play/pause;
- next/previous lesson;
- curriculum disclosure;
- answer selection;
- submit;
- close/back;
- resource access;
- transcript navigation.

### Interaction density

Closely packed controls require particular caution.

Do not create:

~~~text
tiny icon
tiny icon
tiny icon
tiny icon
~~~

simply to preserve desktop toolbar density.

### Gesture boundary

Gesture shortcuts may supplement interaction but should not become the only path for required actions when an accessible alternative is feasible.

Examples:

- swipe-to-next;
- drag-to-reorder;
- pinch gesture;
- scrub gesture.

### Accidental activation

High-consequence controls such as:

- assessment submit;
- destructive reset;
- delete;
- irreversible completion action;

should not be positioned or designed in ways that make accidental touch activation likely.

**Disposition: ADOPT**

**Decision state: LOCKED**

---

## 13. Offline and Connectivity-Aware Learning

### Evidence

Current Udemy mobile documentation supports downloading courses, sections, and individual lectures for offline viewing.

It also documents limitations:

- not every resource is available offline;
- some downloaded content may expire and require reconnection;
- some application behavior may still use connectivity for features or progress updates.

edX likewise supports downloaded course videos for offline consumption while not promising complete offline parity for all course interaction.

### Inference

~~~text
offline media
≠
offline LMS
~~~

Offline capability is a spectrum.

### Requirement candidate

If CodeInteX supports offline learning, every supported offline capability must have an explicit contract.

Possible categories:

~~~text
AVAILABLE_OFFLINE
READ_ONLY_OFFLINE
QUEUE_FOR_SYNC
ONLINE_REQUIRED
~~~

### Learner communication

Before connectivity disappears where feasible, the learner should be able to understand:

- what is downloaded;
- what remains online-only;
- whether progress can be recorded offline;
- whether actions will sync later;
- whether content expires.

### Sync state

If offline progress is supported, relevant states may include:

~~~text
local
pending-sync
syncing
synced
sync-failed
conflict
~~~

Exact state model remains OPEN.

### Anti-pattern

Do not display an action as fully available offline if successful completion still requires undisclosed network access.

**Disposition: ADOPT capability-contract principle**

**Decision state: LOCKED principle; OPEN offline scope**

---

## 14. Cross-Device Learning Continuity

### Problem

A learner may move between:

~~~text
phone
→ tablet
→ laptop/desktop
→ phone
~~~

The experience should not require manually reconstructing learning context every time.

### Evidence relation

Resume-learning evidence already establishes continuity as a first-class learner concern.

Mobile capability differences strengthen the need to preserve state when a learner changes environment.

### Requirement candidate

Where technically supported, cross-device continuity should preserve meaningful state such as:

- course;
- lesson;
- completion state;
- meaningful resume position;
- assessment draft state when appropriate;
- submitted assessment state;
- progress.

### Important distinction

Not every ephemeral UI state must synchronize.

Examples that may not need synchronization:

- open drawer;
- temporary tab selection;
- transient tooltip;
- scroll position with no learning meaning.

### Handoff scenario

If a workflow is unsupported on mobile:

~~~text
mobile learner
→ receives explicit limitation
→ moves to supported environment
→ resumes relevant task/context
~~~

The system should minimize reconstruction cost.

### Conflict handling

If multiple devices can modify learner state, conflict semantics belong to domain/backend architecture and must not be silently invented by the UI.

**Disposition: ADOPT**

**Decision state: LOCKED continuity principle; OPEN synchronization architecture**

---

## 15. Progress and Next Action on Mobile

### Problem

Narrow screens create pressure to hide secondary information.

Progress and next action can accidentally disappear even though they are central to learner continuity.

### Requirement candidate

Mobile learner experience should preserve access to:

- current learning position;
- meaningful progress;
- next required/recommended action;
- important blocker.

These do not all need to remain permanently visible.

They must remain readily discoverable.

### Priority principle

When screen space is constrained, prioritize:

~~~text
current task
+
next meaningful action
+
critical state
~~~

over:

~~~text
decorative metrics
+
secondary recommendation
+
nonessential dashboard density
~~~

### Dashboard implication

Mobile learner dashboard may legitimately have a different composition than desktop.

It must preserve the same core learner questions:

~~~text
Where am I?
What should I continue?
What requires attention?
What should I do next?
~~~

### Anti-pattern

Do not place the primary resume action below large amounts of low-priority dashboard content solely to preserve desktop ordering.

**Disposition: ADOPT**

**Decision state: LOCKED**


---

## 16. Responsive Capability Classification

Track C supports a standard classification for LMS workflows across device contexts.

### FULL

The essential learner outcome can be completed without material capability loss.

Example candidates:

- dashboard;
- resume learning;
- curriculum navigation;
- ordinary text lesson;
- ordinary video lesson;
- simple quiz;
- progress review.

### ADAPTED

The same learner outcome remains possible but interaction changes materially.

Examples may include:

- curriculum sidebar becoming temporary navigation;
- transcript moving from adjacent panel to disclosure surface;
- dense metadata becoming progressive disclosure.

### LIMITED

A meaningful subset is usable, but some capability is unavailable.

The limitation must be visible before substantial learner effort.

### UNSUPPORTED-WITH-EXPLICIT-HANDOFF

A workflow legitimately requires a different environment.

Potential examples may include:

- complex proctored examination;
- advanced technical workspace;
- interaction requiring capabilities unavailable on the current device.

### Requirement

Each critical workflow should eventually have an explicit responsive capability classification.

### Constraint

Classification is based on learner outcome and real technical constraints.

It must not be used to excuse poor responsive implementation.

**Decision state: LOCKED classification model; OPEN per-workflow classification**

---

## 17. Unsupported Workflow Handoff

### Problem

A learner may begin on mobile and encounter a task that cannot responsibly be completed there.

A simple message:

~~~text
Desktop only
~~~

is insufficient.

### Requirement candidate

An explicit handoff should communicate:

- what capability is unavailable;
- what environment is required;
- whether learner state is preserved;
- whether work can be started now;
- how to resume later.

### Preferred experience

~~~text
identify limitation early
→ preserve context
→ explain required environment
→ provide continuation path
~~~

### Example

A complex technical project might allow mobile users to:

- read project requirements;
- inspect rubric;
- review previous feedback;

while clearly requiring a larger supported environment for actual workspace execution.

### Anti-pattern

Do not allow substantial input and then reveal only at final submission that the workflow is unsupported.

**Disposition: ADOPT**

**Decision state: LOCKED**

---

## 18. Responsive State Preservation

### Principle

Changing viewport, orientation, or navigation presentation must not unnecessarily reset domain state.

Relevant state may include:

- current lesson;
- playback position;
- assessment draft;
- selected assessment answer;
- current curriculum location;
- learner progress;
- unsaved work warning.

### Presentation state

Some presentation state may legitimately change:

~~~text
desktop sidebar open
→
mobile sidebar closed
~~~

without changing learner domain state.

### Requirement candidate

Implementation should distinguish:

~~~text
domain state
≠
responsive presentation state
~~~

### Failure mode

A breakpoint transition must not:

- restart media unexpectedly;
- clear form input;
- change selected answer;
- reset lesson progress;
- force navigation to unrelated content.

**Disposition: ADOPT**

**Decision state: LOCKED principle**

---

## 19. Responsive Accessibility Integration

Track C consumes Track A requirements.

Responsive implementation must preserve:

- semantic reading order;
- keyboard operability;
- visible focus;
- target-size requirements;
- zoom/reflow;
- orientation support;
- non-color semantics;
- accessible errors;
- programmatic state.

### Reordering

Visual CSS reordering must not create a materially confusing assistive-technology reading sequence.

### Temporary navigation

If desktop persistent navigation becomes mobile drawer/sheet:

- trigger must be accessible;
- open/closed state must be exposed;
- focus behavior must be defined;
- close behavior must be available;
- learner must return to meaningful context.

### Progressive disclosure

Collapsed content must remain:

- discoverable;
- operable;
- semantically connected to its trigger.

**Decision state: LOCKED**

---

## 20. Track C Requirement Candidate Summary

Evidence supports the following LMS Experience Profile candidates.

### LOCKED principles

1. Responsive LMS behavior preserves learner intent, state, hierarchy, and accessibility rather than merely shrinking desktop layout.
2. Mobile capability does not require identical desktop parity.
3. Critical workflows should be classified as FULL, ADAPTED, LIMITED, or UNSUPPORTED-WITH-EXPLICIT-HANDOFF.
4. Learner orientation must survive when persistent curriculum navigation disappears.
5. Lesson composition should prioritize the primary learning activity under constrained space.
6. Progressive disclosure may move secondary surfaces but must not hide critical actions/state.
7. Ordinary LMS workflows must not unnecessarily lock device orientation.
8. Narrow layouts must reduce visual competition without removing semantic completeness.
9. Two-dimensional technical content should use localized adaptation rather than forcing page-level horizontal scrolling.
10. Transcript/resources/curriculum interactions should preserve lesson context.
11. Mobile controls must satisfy accessible touch/interaction requirements.
12. Offline capability must be explicit rather than implied as all-or-nothing LMS support.
13. Cross-device transitions should minimize learner context reconstruction.
14. Progress and next meaningful action must remain readily discoverable on mobile.
15. Unsupported workflows require explicit handoff before substantial learner effort.
16. Responsive presentation state must remain separate from domain state.
17. Responsive transformations must preserve accessibility contracts.

### PROVISIONAL

- exact mobile lesson composition;
- curriculum mobile presentation;
- transcript mobile presentation;
- offline state vocabulary;
- workflow capability classifications.

### OPEN

- exact breakpoints;
- native app requirement;
- PWA requirement;
- offline LMS scope;
- cross-device synchronization architecture;
- technical workspace mobile support;
- final mobile navigation pattern.

---

## 21. Remaining Track C Evidence Gaps

Evidence remains insufficient to lock:

- exact CodeInteX breakpoint system;
- device-specific navigation implementation;
- native application strategy;
- PWA/offline architecture;
- synchronization/conflict resolution;
- mobile code editor/workspace behavior;
- responsive complex data visualization;
- tablet-specific optimization;
- foldable/multi-window behavior.

These are implementation or future-product concerns.

They do not block LMS Experience Profile v0.1.

### Research rule

Do not add additional responsive benchmarks unless:

- reference implementation exposes a material unresolved failure;
- a new critical workflow enters scope;
- target-device requirements materially change.

**Decision state: OPEN / DEFERRED**

---

## 22. Track C Completion Gate

The Specialist Benchmark Plan defines Track C complete when:

> LMS Experience Profile can define responsive invariants without copying benchmark layouts.

Current evidence status:

- responsive principle: SUFFICIENT;
- curriculum orientation: SUFFICIENT;
- lesson composition principle: SUFFICIENT;
- progressive disclosure: SUFFICIENT;
- orientation: SUFFICIENT;
- reflow/density: SUFFICIENT;
- technical content principle: SUFFICIENT;
- media/transcript continuity: SUFFICIENT;
- touch interaction: SUFFICIENT;
- offline capability boundary: SUFFICIENT;
- cross-device continuity principle: SUFFICIENT;
- progress/next-action mobile priority: SUFFICIENT;
- unsupported-workflow handoff: SUFFICIENT;
- accessibility integration: SUFFICIENT.

Not required for current profile baseline:

- exact breakpoints;
- native/PWA architecture;
- exact responsive components;
- full offline implementation;
- exact synchronization mechanism.

### Conclusion

**TRACK C COMPLETION GATE: PASS**

No additional responsive product benchmark is required for Track C v0.1.

---

## 23. Source References

### Internal Udacity Evidence

`UDACITY-LEARNER-EXPERIENCE-EVIDENCE-v0.1.md`

### Internal Accessibility Evidence

`ACCESSIBILITY-CRITICAL-LEARNER-WORKFLOWS-EVIDENCE-v0.1.md`

### Udemy Business Mobile Course Player

Official Udemy Business support documentation:

`How to access and use the mobile course player`

### Udemy Offline Course Access

Official Udemy support documentation:

`Downloading courses for offline viewing on the Android app`

### edX Mobile Capabilities

Official edX Help Center:

`What can I do on the edX app?`

### edX Mobile Assignment Capability

Official edX Help Center:

`What types of assignments can be done in the edX app?`

### edX System Requirements

Official edX Help Center:

`What are the system requirements and supported browsers on edX?`

### WCAG 2.2

https://www.w3.org/TR/WCAG22/

### Source-use constraint

Udemy and edX are specialist evidence sources.

They are not:

- CodeInteX visual templates;
- CodeInteX navigation specifications;
- CodeInteX mobile architecture;
- CodeInteX offline architecture.

---

## 24. Document Status

This document is an:

**EVIDENCE BASELINE — PROVISIONAL v0.1**

Track C research requirement is complete for the LMS Experience Profile v0.1 milestone.

The evidence is sufficient to define mobile/responsive experience invariants without copying Udemy, edX, or Udacity layouts.

Implementation-specific responsive behavior remains subject to:

- reference implementation;
- real CodeInteX content;
- accessibility validation;
- device testing;
- usability evaluation.

Passing this research gate does not mean every future CodeInteX workflow must work identically on every device.

It means device limitations and adaptations must now be deliberate, explicit, and learner-centered.
