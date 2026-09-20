# CodeInteX LMS — Accessibility Critical Learner Workflows Evidence v0.1

- **Project:** CodeInteX
- **Workstream:** PES / LMS
- **Research track:** Track A — Accessibility Critical Learner Workflows
- **Status:** EVIDENCE BASELINE — PROVISIONAL
- **Version:** 0.1
- **Date:** 2026-09-19
- **Target baseline:** WCAG 2.2 AA
- **Depends on:**
  - `../PES-FOUNDATION-DECISION-MODEL-v0.1.md`
  - `../PES-CONSUMPTION-CONTRACT-v0.1.md`
  - `LMS-SPECIALIST-BENCHMARK-PLAN-v0.1.md`
  - `UDACITY-LEARNER-EXPERIENCE-EVIDENCE-v0.1.md`

---

## 0. Purpose

Dokumen ini mengubah accessibility evidence menjadi requirement candidates yang dapat diuji untuk critical learner workflows CodeInteX LMS.

Tujuannya bukan membuat checklist WCAG generik.

Tujuannya adalah menjawab:

- bagaimana learner mengoperasikan LMS tanpa pointer;
- bagaimana hierarchy dapat dipahami assistive technology;
- bagaimana focus dipertahankan secara masuk akal;
- bagaimana system state diumumkan;
- bagaimana form dan assessment error dipulihkan;
- bagaimana learning media tetap accessible;
- bagaimana responsive/reflow mempertahankan functionality;
- bagaimana authentication tidak menciptakan cognitive barrier;
- bagaimana implementation nanti dapat diuji secara manual dan otomatis.

**Decision state: LOCKED untuk evidence interpretation process**

---

## 1. Evidence Authority

Evidence utama untuk Track A:

### A01 — WCAG 2.2

Authority:

W3C Recommendation.

Relevant criteria include:

- 1.2.1 Audio-only and Video-only (Prerecorded);
- 1.2.2 Captions (Prerecorded);
- 1.2.4 Captions (Live);
- 1.2.5 Audio Description (Prerecorded);
- 1.3.1 Info and Relationships;
- 1.3.2 Meaningful Sequence;
- 1.3.3 Sensory Characteristics;
- 1.3.4 Orientation;
- 1.4.1 Use of Color;
- 1.4.3 Contrast (Minimum);
- 1.4.4 Resize Text;
- 1.4.10 Reflow;
- 1.4.11 Non-text Contrast;
- 2.1.1 Keyboard;
- 2.1.2 No Keyboard Trap;
- 2.4.1 Bypass Blocks;
- 2.4.3 Focus Order;
- 2.4.6 Headings and Labels;
- 2.4.7 Focus Visible;
- 2.4.11 Focus Not Obscured (Minimum);
- 2.5.7 Dragging Movements;
- 2.5.8 Target Size (Minimum);
- 3.2.3 Consistent Navigation;
- 3.2.4 Consistent Identification;
- 3.2.6 Consistent Help;
- 3.3.1 Error Identification;
- 3.3.2 Labels or Instructions;
- 3.3.3 Error Suggestion;
- 3.3.4 Error Prevention (Legal, Financial, Data);
- 3.3.7 Redundant Entry;
- 3.3.8 Accessible Authentication (Minimum);
- 4.1.2 Name, Role, Value;
- 4.1.3 Status Messages.

Evidence class: AUTHORITATIVE STANDARD.

---

### A02 — WAI-ARIA Authoring Practices Guide

Relevant patterns include:

- Disclosure;
- Tree View;
- Navigation Tree View;
- Tabs;
- Dialog Modal;
- Accordion.

APG provides implementation guidance and example keyboard interaction.

APG patterns are not automatically required simply because a visual structure resembles the example.

Evidence class: AUTHORITATIVE IMPLEMENTATION GUIDANCE.

---

### A03 — WAI Forms Tutorial

Relevant guidance includes:

- labels;
- input validation;
- error identification;
- error correction;
- user notification;
- multi-step forms.

Evidence class: AUTHORITATIVE GUIDANCE.

---

### A04 — WAI Making Audio and Video Media Accessible

Relevant guidance includes:

- captions;
- transcripts;
- audio description;
- accessible media players;
- interactive transcripts.

Evidence class: AUTHORITATIVE GUIDANCE.

---

## 2. Important Standards Interpretation

### WCAG AA is the baseline, not the ceiling

CodeInteX baseline remains:

`WCAG 2.2 AA`

However, CodeInteX may adopt stronger behavior when justified.

### APG is not WCAG

APG patterns provide tested semantic and keyboard models.

They do not mean that every similar interface must use the corresponding ARIA widget.

Prefer native HTML semantics where sufficient.

### Accessibility feature does not prove accessibility

Examples:

~~~text
captions exist
≠
whole lesson is accessible

keyboard support exists
≠
focus flow is usable

ARIA exists
≠
screen-reader experience is correct
~~~

Manual critical-flow evaluation remains required.

**Decision state: LOCKED**

---

## 3. Critical Learner Workflows

Track A evaluates accessibility across these critical journeys:

### Flow A — Enter learning environment

~~~text
authenticate
→ dashboard
→ identify active learning
→ resume
~~~

### Flow B — Navigate curriculum

~~~text
understand hierarchy
→ locate current lesson
→ expand/collapse curriculum
→ select destination
→ understand new position
~~~

### Flow C — Consume lesson

~~~text
enter lesson
→ navigate content
→ operate media
→ access alternatives
→ continue
~~~

### Flow D — Progress

~~~text
inspect progress
→ understand state
→ identify remaining work
→ activate next action
~~~

### Flow E — Assessment / project

~~~text
read requirement
→ provide input/work
→ validate
→ submit
→ receive status
→ recover or continue
~~~

### Flow F — Failure recovery

~~~text
encounter failure
→ perceive failure
→ understand cause
→ locate recovery action
→ recover without unnecessary data loss
~~~

**Decision state: LOCKED**

---

## 4. Keyboard Operability Contract

### Evidence

WCAG 2.2 requires content functionality to be operable through a keyboard interface except where the function fundamentally depends on path-based movement.

Keyboard focus must also be able to leave components without trapping the user.

### LMS requirement candidate

Every critical learner action must be achievable without requiring a mouse or touch interaction.

Examples include:

- opening a course;
- resuming learning;
- curriculum navigation;
- expanding/collapsing curriculum sections;
- lesson navigation;
- media operation where supported by the player;
- opening resources;
- assessment form interaction;
- submission;
- dialogs;
- recovery actions.

### Prohibited failure modes

~~~text
click-only action
hover-only action
drag-only action when non-drag alternative is possible
keyboard trap
invisible keyboard-only functionality
custom control without keyboard behavior
~~~

### Validation

Manual:

1. disconnect or do not use pointing device;
2. complete critical workflow using keyboard;
3. verify no required action becomes unreachable;
4. verify focus can enter and leave all interactive regions.

Automated testing can support but cannot replace this test.

**Disposition: ADOPT**

**Decision state: LOCKED requirement candidate**

---

## 5. Focus Management Contract

### Evidence

Relevant WCAG requirements include:

- logical focus order;
- visible keyboard focus;
- focused component not entirely obscured by author-created content.

### LMS requirement candidate

Focus must:

- follow meaningful interaction order;
- remain visible;
- not disappear after dynamic updates;
- not move unexpectedly without interaction rationale;
- return to a meaningful trigger after temporary surfaces close where appropriate.

### Examples

Opening a modal:

~~~text
trigger
→ dialog opens
→ focus moves into dialog
→ keyboard remains within active modal interaction
→ Escape/close
→ focus returns to meaningful location
~~~

Changing lesson:

Focus behavior must be intentionally defined.

Possible valid behavior depends on interaction:

- preserve navigation focus when rapidly browsing curriculum; or
- move focus to new lesson heading when navigation represents committed page/content navigation.

Do not let framework behavior decide accidentally.

### Sticky UI risk

Sticky:

- headers;
- bottom navigation;
- media controls;
- action bars;

must not completely obscure keyboard focus.

### Validation

Test:

- forward Tab;
- reverse Shift+Tab;
- modal open/close;
- curriculum expansion;
- route/content transition;
- sticky headers/footers;
- narrow viewport;
- zoomed viewport.

**Disposition: ADOPT**

**Decision state: LOCKED requirement candidate**

---

## 6. Curriculum Hierarchy Semantics

### Evidence

WCAG requires visual information, structure, and relationships to be programmatically determinable or available in text.

APG provides both simpler Disclosure semantics and more complex Tree View semantics.

### Critical architectural conclusion

A visual curriculum hierarchy does **not** automatically require ARIA `tree`.

Potential implementations include:

~~~text
semantic headings + lists + disclosure controls
~~~

or, when interaction genuinely behaves like a desktop hierarchical widget:

~~~text
tree / treeitem semantics
~~~

### Default preference

Prefer the simplest semantic interaction model that:

- represents hierarchy correctly;
- supports keyboard interaction;
- remains understandable to screen readers;
- avoids unnecessary custom focus management.

### Disclosure contract

If curriculum sections use disclosure behavior:

- control must be keyboard operable;
- expanded/collapsed state must be programmatically exposed;
- visual state and semantic state must remain synchronized.

### Tree View escalation

Use a Tree View model only if the interaction genuinely needs tree-style composite-widget behavior.

Do not introduce arrow-key navigation and roving focus merely because nested lessons visually resemble a file tree.

### Validation

Screen-reader and keyboard testing must confirm:

- hierarchy is perceivable;
- expanded/collapsed state is perceivable;
- current item is distinguishable;
- completed/locked state is not communicated only by color;
- navigation remains usable.

**Disposition: ADOPT with implementation restraint**

**Decision state: LOCKED principle; OPEN exact curriculum widget**

---

## 7. Lesson Structure and Reading Order

### Evidence

Structure conveyed visually must also be programmatically available.

When content sequence affects meaning, reading order must preserve that meaning.

### LMS requirement candidate

Lesson content should use semantic structure appropriate to content:

- headings;
- paragraphs;
- lists;
- landmarks/regions where justified;
- native interactive controls;
- semantic tables for tabular data;
- properly associated figures/captions where relevant.

CSS layout must not create a visual reading order that conflicts materially with DOM/assistive-technology reading order.

### Responsive implication

Rearranging:

~~~text
navigation
content
resources
transcript
assessment panel
~~~

must not produce nonsensical sequential navigation order.

**Disposition: ADOPT**

**Decision state: LOCKED requirement candidate**

---

## 8. Learning Media Accessibility

### Evidence

WCAG distinguishes requirements by media type.

For prerecorded synchronized video with meaningful audio:

- captions are required at Level A;
- audio description for necessary visual information is required at Level AA.

For prerecorded audio-only content:

- an equivalent text alternative is required at Level A.

WAI recommends transcripts more broadly because they support additional user needs.

### Important distinction

For ordinary prerecorded synchronized video:

~~~text
transcript
≠
universal WCAG 2.2 AA requirement
~~~

However, transcript remains a strong CodeInteX learner-experience capability because it can improve:

- searchability;
- review;
- alternate consumption;
- accessibility beyond minimum conformance;
- navigation to specific learning content.

### LMS requirement candidate

Where applicable:

- provide required captions;
- provide required audio description or equivalent solution;
- use an accessible media player;
- do not autoplay disruptive audio;
- ensure media controls are keyboard accessible;
- expose alternatives predictably.

### Interactive transcript

Interactive transcript remains:

**PROVISIONAL PRODUCT ENHANCEMENT**

It should not be mislabeled as an AA requirement.

**Disposition: ADOPT standards; PROVISIONAL transcript enhancement**

---

## 9. Error Identification and Recovery

### Evidence

WCAG requires automatically detected input errors to be identified and described in text.

When correction suggestions are known, they should be provided unless doing so would compromise security or purpose.

WAI guidance recommends clear overall and field-level feedback.

### LMS requirement candidate

Assessment, enrollment, profile, and submission errors must communicate:

~~~text
what failed
where it failed
why, when known
how to recover
whether learner work was preserved
~~~

### Error communication must not rely only on

- red color;
- icon alone;
- toast that disappears before it can be reviewed;
- inaccessible tooltip;
- visual position only.

### Form association

Errors should be programmatically associated with relevant controls where applicable.

### Submission recovery

Where failure occurs after substantial learner effort, the experience should explicitly communicate whether work remains preserved.

**Disposition: ADOPT**

**Decision state: LOCKED requirement candidate**

---

## 10. Dynamic Status and Asynchronous Workflow

### Evidence

WCAG 2.2 requires relevant status messages to be programmatically determinable so assistive technologies can present them without requiring focus to move to the message.

### LMS relevance

Examples include:

~~~text
saving
saved
uploading
upload complete
submission received
queued
review started
review complete
progress updated
connection lost
retrying
~~~

### LMS requirement candidate

Important dynamic state changes must not depend solely on visual mutation.

The implementation must distinguish:

- information that should be announced without moving focus;
- errors requiring learner attention;
- route/context changes where focus movement is appropriate.

### Anti-pattern

Do not move keyboard focus to every status update.

Status announcement and focus movement solve different problems.

**Disposition: ADOPT**

**Decision state: LOCKED requirement candidate**


---

## 11. Reflow, Zoom, and Narrow Viewport Contract

### Evidence

WCAG 2.2 SC 1.4.10 Reflow requires content to remain usable without loss of information or functionality and, for vertically scrolling content, without requiring two-dimensional scrolling at a width equivalent to 320 CSS pixels.

Exceptions exist for content whose meaning or use genuinely requires two-dimensional layout.

WCAG 2.2 SC 1.4.4 also requires text to be resizable up to 200 percent without loss of content or functionality.

### LMS requirement candidate

Critical learner workflows must remain usable under substantial zoom and narrow viewport conditions.

Relevant LMS surfaces include:

- learner dashboard;
- curriculum navigation;
- lesson content;
- media controls;
- transcripts;
- progress;
- forms;
- assessment;
- project submission;
- dialogs;
- notifications;
- recovery actions.

### Required behavior

Responsive adaptation may:

- stack;
- collapse;
- reflow;
- move secondary controls into disclosure;
- convert persistent side navigation into temporary navigation;
- allow localized scrolling where two-dimensional structure is genuinely necessary.

Responsive adaptation must not remove:

- required content;
- primary action;
- state information;
- error information;
- accessibility semantics.

### Two-dimensional content

Examples that may legitimately require localized horizontal scrolling include:

- large data tables;
- code;
- diagrams;
- certain interactive workspaces.

The page as a whole should not require unnecessary two-dimensional scrolling merely because one region does.

### Validation

Test critical workflows at minimum for:

- 200% text resizing where applicable;
- viewport/reflow condition equivalent to 320 CSS px width;
- browser zoom;
- long translated or expanded text;
- persistent/sticky controls;
- dialogs;
- curriculum navigation.

**Disposition: ADOPT**

**Decision state: LOCKED requirement candidate**

---

## 12. Pointer Target and Alternative Interaction Contract

### Evidence

WCAG 2.2 SC 2.5.8 Target Size (Minimum) is Level AA.

The normative minimum is:

`24 × 24 CSS pixels`

with defined exceptions such as sufficient spacing, equivalent controls, and inline targets.

WCAG also addresses dragging movements.

### LMS requirement candidate

Interactive targets must be sufficiently operable for touch, mouse, stylus, and users with reduced pointing precision.

Particular attention is required for:

- lesson navigation;
- curriculum expand/collapse controls;
- media controls;
- pagination;
- tabs;
- quiz choices;
- icon buttons;
- close buttons;
- project-upload controls;
- mobile bottom/navigation actions.

### Product-quality direction

Meeting 24 × 24 CSS pixels is the conformance floor, not necessarily the preferred CodeInteX target size.

Where space permits, larger comfortable targets should be preferred.

Exact PES target-size design token remains a foundation decision and is not locked by this evidence pack.

### Dragging

If an LMS interaction uses dragging and the action does not fundamentally require path-based movement, an alternative non-drag interaction must be available.

Examples may include:

- reorder controls;
- sliders;
- matching activities;
- drag-and-drop exercises.

### Validation

Test with:

- touch;
- mouse;
- keyboard alternative;
- narrow viewport;
- adjacent small controls.

**Disposition: ADOPT**

**Decision state: LOCKED requirement candidate**

---

## 13. Contrast, Color, and Visual State Contract

### Evidence

WCAG 2.2 Level AA requires:

- normal text contrast of at least 4.5:1;
- qualifying large text contrast of at least 3:1;
- relevant non-text UI/component/state contrast of at least 3:1;
- color not to be the only visual means of conveying information where SC 1.4.1 applies.

### LMS requirement candidate

Learner state must not depend solely on color.

Examples include:

~~~text
completed
current
locked
failed
passed
warning
selected
review pending
changes required
~~~

State should use appropriate combinations of:

- text;
- iconography;
- shape/border;
- semantic label;
- programmatic state.

### Theme implication

Every supported theme must preserve accessibility semantics.

A theme is invalid if it makes required state distinctions inaccessible even when the component structure remains unchanged.

### Data visualization implication

If progress charts or analytics are introduced, meaning must not depend only on color differences.

### Validation

Validate:

- body text;
- secondary text;
- interactive controls;
- focus indicators;
- status indicators;
- error states;
- selected/current states;
- disabled-state semantics where relevant;
- both light/dark or other supported themes.

**Disposition: ADOPT**

**Decision state: LOCKED requirement candidate**

---

## 14. Accessible Authentication Contract

### Evidence

WCAG 2.2 SC 3.3.8 Accessible Authentication (Minimum) is Level AA.

Authentication must not require a cognitive-function test unless an allowed alternative or mechanism is available.

W3C guidance identifies support for password managers and copy/paste as examples that can reduce cognitive burden.

### LMS requirement candidate

Authentication flows must not unnecessarily require learners to:

- memorize credentials;
- manually transcribe information when a mechanism can assist;
- solve cognitive puzzles without an accessible alternative.

### Implementation implications

Do not intentionally block:

- password managers;
- password paste;
- relevant one-time-code assistance mechanisms where technically appropriate.

Authentication security remains a security/domain concern.

Accessibility must not weaken authentication integrity.

The correct objective is:

~~~text
secure authentication
+
accessible completion path
~~~

not choosing one instead of the other.

### Scope clarification

SC 3.3.8 principally concerns authentication of existing users.

Registration/account-creation UX should still apply similar cognitive-load principles where appropriate, but that distinction should be preserved.

**Disposition: ADOPT**

**Decision state: LOCKED requirement candidate**

---

## 15. Motion and Animation Accessibility

### PES context

PES already requires reduced-motion consideration.

### Standards interpretation

Do not describe all reduced-motion handling as a universal WCAG 2.2 AA requirement.

Different WCAG criteria address specific moving, blinking, flashing, auto-updating, or interaction-triggered content at different levels and scopes.

### CodeInteX requirement candidate

Non-essential motion should respect the user's reduced-motion preference where technically feasible.

When motion is reduced:

- information must remain available;
- state change must remain understandable;
- animation must not be required to understand navigation;
- progress/status must remain perceivable;
- interaction must remain complete.

### Examples

Potentially reducible motion:

- page transitions;
- decorative parallax;
- animated card movement;
- non-essential spring transitions;
- celebratory animation.

Potentially meaningful motion requires case-specific treatment rather than blindly disabling it.

### Product rationale

This requirement supports broader accessibility and comfort beyond minimum conformance.

**Disposition: ADOPT as PES product requirement**

**Decision state: LOCKED product requirement; not labeled as universal WCAG AA criterion**

---

## 16. Assessment and Form Accessibility Contract

### Evidence

Relevant WCAG requirements include:

- labels/instructions;
- error identification;
- error suggestion;
- programmatic name/role/value;
- keyboard operability;
- status messages.

### LMS requirement candidate

Assessment interaction must clearly communicate:

- question/instruction;
- required input;
- constraints;
- validation state;
- current answer where applicable;
- error;
- correction path;
- submission state.

### Choice-based assessment

Selection state must be available programmatically and must not depend only on color.

### Text response

Text-entry assessment must have:

- programmatically associated label/instruction;
- preserved input where feasible after recoverable failure;
- understandable validation.

### Multi-step assessment

Learners must be able to understand:

- current step;
- progress through assessment where relevant;
- whether navigation loses answers;
- whether previous answers can be reviewed.

### Timed assessment

If time limits exist, accessibility implications must be evaluated separately.

Do not introduce time pressure by default merely because the UI supports a timer.

### Submission confirmation

For consequential submissions, the experience should make the transition from editable work to submitted work clear.

Whether confirmation is required depends on reversibility and consequence.

### Validation

Test:

- keyboard-only completion;
- screen-reader interpretation;
- error correction;
- validation;
- submission;
- retry/recovery;
- narrow viewport;
- zoom.

**Disposition: ADOPT**

**Decision state: LOCKED general requirement; OPEN domain-specific assessment policy**

---

## 17. Critical Manual Accessibility Test Matrix

Automated tooling is necessary but insufficient.

The following manual matrix is required for reference implementation validation.

| Flow | Keyboard | Focus | Screen reader | Reflow/zoom | Error/recovery | Status announcement |
|---|---:|---:|---:|---:|---:|---:|
| Authentication | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED | AS APPLICABLE |
| Dashboard → Resume | REQUIRED | REQUIRED | REQUIRED | REQUIRED | AS APPLICABLE | AS APPLICABLE |
| Curriculum navigation | REQUIRED | REQUIRED | REQUIRED | REQUIRED | AS APPLICABLE | REQUIRED where dynamic |
| Lesson navigation | REQUIRED | REQUIRED | REQUIRED | REQUIRED | AS APPLICABLE | AS APPLICABLE |
| Media lesson | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED | AS APPLICABLE |
| Assessment | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| Project submission | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| Async review/status | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| Completion | REQUIRED | REQUIRED | REQUIRED | REQUIRED | AS APPLICABLE | REQUIRED where dynamic |

### Manual-test principle

A passing automated scan does not make a critical learner journey accessible.

Manual tests must evaluate the complete interaction sequence.

**Decision state: LOCKED**

---

## 18. Automated Accessibility Testing Boundary

### Automated testing is useful for

- missing accessible names;
- selected ARIA misuse;
- detectable contrast problems;
- duplicate IDs where relevant;
- selected structural violations;
- regression prevention.

### Automated testing cannot reliably prove

- logical focus order;
- understandable screen-reader flow;
- correct focus restoration;
- useful error messaging;
- sensible curriculum interaction;
- meaningful status announcements;
- cognitive clarity;
- correct reading order in all dynamic conditions;
- usable keyboard workflow.

### Implementation requirement

Web Implementation Profile should select automated accessibility tooling, but PES/LMS contracts must not depend on one vendor.

Potential implementation tools remain an Implementation Profile decision.

### CI implication

Automated accessibility checks should eventually participate in CI for stable critical components/pages.

Manual validation remains required before declaring critical flows accessible.

**Decision state: LOCKED principle; OPEN exact tooling**

---

## 19. Accessibility Requirement Candidate Summary

Track A supports promotion of the following requirements into the LMS Experience Profile.

### LOCKED candidates

1. Critical learner functionality must be keyboard operable.
2. Keyboard traps are prohibited.
3. Focus order must remain meaningful.
4. Visible focus must be preserved.
5. Sticky/overlay UI must not obscure focused controls.
6. Curriculum hierarchy must expose structure programmatically.
7. ARIA Tree View must not be used merely because curriculum is visually hierarchical.
8. Lesson DOM/semantic order must preserve meaningful reading order.
9. Required media alternatives must follow WCAG media criteria.
10. Important dynamic status must be programmatically available.
11. Errors must be identified and recoverable.
12. Critical learner workflows must satisfy reflow/zoom requirements.
13. Pointer targets must satisfy applicable WCAG 2.2 AA requirements.
14. State must not rely only on color.
15. Supported themes must preserve accessibility.
16. Authentication must satisfy accessible-authentication requirements.
17. Assessment controls and validation must be programmatically understandable.
18. Critical workflows require manual accessibility testing.

### CodeInteX requirement beyond minimum-AA interpretation

19. Non-essential motion should honor reduced-motion preference where feasible.
20. Searchable/interactive transcripts are a strong learner-experience enhancement where media architecture supports them.

### Still OPEN

- exact curriculum widget implementation;
- exact focus behavior for every lesson transition;
- preferred target size beyond WCAG minimum;
- exact automated-testing toolchain;
- exact screen-reader/browser test matrix;
- assessment-specific domain policy;
- timed-assessment policy.

---

## 20. Remaining Accessibility Evidence Gaps

Track A does not eliminate every accessibility question.

Remaining implementation-level validation includes:

- actual screen-reader behavior of chosen components;
- actual browser/framework focus behavior;
- third-party media-player accessibility;
- third-party authentication UI;
- code editor/workspace accessibility if introduced;
- chart/data-visualization accessibility if introduced;
- complex drag/drop learning activities if introduced.

These gaps should be evaluated when those implementation choices enter scope.

### Product benchmark decision

No additional LMS product benchmark is currently required for Track A.

Reason:

The high-impact accessibility requirements needed for LMS Experience Profile can be grounded directly in standards and WAI guidance.

A product benchmark may be added later only if a concrete interaction question remains unresolved.

**Decision state: LOCKED for current research milestone**

---

## 21. Track A Completion Gate

Track A completion criteria from the Specialist Benchmark Plan:

> Critical learner flows can have testable accessibility contracts without depending on undocumented benchmark assumptions.

Current evaluation:

- keyboard contract: SUFFICIENT;
- focus contract: SUFFICIENT;
- hierarchy semantics: SUFFICIENT for profile-level decision;
- media baseline: SUFFICIENT;
- forms/errors: SUFFICIENT;
- status communication: SUFFICIENT;
- reflow/zoom: SUFFICIENT;
- target-size baseline: SUFFICIENT;
- authentication baseline: SUFFICIENT;
- manual-validation strategy: SUFFICIENT.

### Conclusion

**TRACK A COMPLETION GATE: PASS**

Remaining questions are implementation-specific or domain-specific and can remain OPEN until their relevant layer is designed.

---

## 22. Source References

Authoritative sources used by this evidence pack:

### WCAG 2.2

https://www.w3.org/TR/WCAG22/

### WAI-ARIA Authoring Practices Guide

https://www.w3.org/WAI/ARIA/apg/

### WAI Forms Tutorial

https://www.w3.org/WAI/tutorials/forms/

### WAI Media Accessibility

https://www.w3.org/WAI/media/av/

### Understanding SC 1.4.10 — Reflow

https://www.w3.org/WAI/WCAG22/Understanding/reflow.html

### Understanding SC 2.5.8 — Target Size (Minimum)

https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html

### Understanding SC 3.3.8 — Accessible Authentication (Minimum)

https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html

### Understanding SC 1.4.3 — Contrast (Minimum)

https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html

### Understanding SC 1.4.11 — Non-text Contrast

https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html

---

## 23. Document Status

This document is an:

**EVIDENCE BASELINE — PROVISIONAL v0.1**

Track A research requirement is complete for the LMS Experience Profile v0.1 milestone.

The evidence is sufficient to define profile-level accessibility contracts.

Implementation-specific conformance still requires:

- reference implementation;
- automated testing;
- manual keyboard testing;
- manual screen-reader testing;
- reflow/zoom testing;
- critical-flow usability evaluation.

Passing this research gate does not mean the eventual CodeInteX LMS implementation is automatically WCAG-conformant.
