# Udacity Learner Experience — Benchmark Evidence Pack v0.1

- **Project:** CodeInteX
- **Workstream:** Product Experience System / LMS
- **Benchmark:** Udacity
- **Benchmark role:** PRIMARY learner-experience benchmark
- **Status:** EVIDENCE BASELINE — PROVISIONAL
- **Version:** 0.1
- **Research snapshot:** 2026-09-19
- **Evidence scope:** Publicly observable and officially documented learner experience
- **Depends on:**
  - `../PES-FOUNDATION-DECISION-MODEL-v0.1.md`
  - `../PES-CONSUMPTION-CONTRACT-v0.1.md`
  - `../PES-DECISION-LOG.md`

---

## 0. Purpose

Dokumen ini merekam evidence dari Udacity yang relevan terhadap learner experience CodeInteX LMS.

Tujuannya bukan untuk menyalin Udacity.

Tujuannya adalah:

- mengidentifikasi learner problems yang telah ditangani oleh produk matang;
- memisahkan observation dari inference;
- mengevaluasi pattern mana yang layak diadopsi, dimodifikasi, atau ditolak;
- menghasilkan candidate patterns untuk LMS Experience Profile;
- mengurangi keputusan UI berdasarkan selera;
- menyediakan evidence yang auditable bagi manusia dan AI coding agents.

Udacity tetap merupakan benchmark, bukan specification.

---

## 1. Benchmark Policy

Canonical evidence flow:

~~~text
Observation
    ↓
User Problem
    ↓
Evidence / Rationale
    ↓
Adopt / Modify / Reject
    ↓
Pattern Candidate
    ↓
CodeInteX Validation
~~~

Tidak diperbolehkan:

~~~text
Udacity looks good
→ copy interface
~~~

Benchmark tidak memberi authority atas:

- CodeInteX visual identity;
- PES architecture;
- accessibility baseline;
- implementation stack;
- backend architecture;
- final component taxonomy.

---

## 2. Evidence Classification

### E1 — Direct official current evidence

Official Udacity documentation atau product page yang masih aktif dan cukup relevan untuk menggambarkan current behavior.

### E2 — Direct official historical evidence

Official material yang menjelaskan design rationale atau historical behavior, tetapi current implementation harus diverifikasi sebelum dianggap masih berlaku.

### E3 — Inference

Kesimpulan CodeInteX yang diturunkan dari evidence.

Inference bukan fakta tentang Udacity.

### E4 — Unknown

Behavior tidak dapat diverifikasi secara cukup dari public evidence.

Unknown tidak boleh diisi dengan asumsi.

---

## 3. Source Register

### S01 — 2024 Learner Experience Redesign

Official Udacity Enterprise Help Center.

Source:

https://udacityenterprise.zendesk.com/hc/en-us/articles/28797777385357-2024-Learner-Experience-Redesign

Observed documentation includes:

- redesigned Dashboard;
- redesigned Classroom;
- course selector;
- expandable/collapsible lessons;
- Resources tab;
- redesigned Enrollment Page.

Evidence class: E1.

### S02 — Dashboard

Official Udacity Enterprise Help Center.

Source:

https://udacityenterprise.zendesk.com/hc/en-us/articles/43450585898253-Dashboard

Observed documentation includes:

- Continue Learning;
- learning statistics;
- concepts completed;
- lessons completed;
- projects completed;
- enrollment management;
- certificate access;
- search/filter/sort for enrollments;
- recommendations and career resources.

Evidence class: E1.

### S03 — Classroom Access

Official Udacity Enterprise Help Center.

Source:

https://udacityenterprise.zendesk.com/hc/en-us/articles/360040430812-How-do-I-access-my-Classroom

Observed documentation includes:

- currently-learning programs;
- completed programs;
- program tiles;
- search;
- help access;
- account access.

Evidence class: E1.

### S04 — Classroom Navigation

Official Udacity Support.

Source:

https://support.udacity.com/hc/en-us/articles/360013816732-How-do-I-access-my-Classroom

Observed documentation includes:

- left-side navigation;
- lesson navigation;
- syllabus view;
- multi-program access.

Evidence class: E1.

### S05 — Learning Reminders

Official Udacity Enterprise Help Center.

Source:

https://udacityenterprise.zendesk.com/hc/en-us/articles/47594468814733-Can-I-schedule-learning-reminders

Observed documentation includes:

- learner-defined learning schedule;
- `.ics` export;
- personal-calendar integration;
- calendar event linking back to learning dashboard.

Evidence class: E1.


### S06 — Audio Slides

Official Udacity Enterprise Help Center.

Source:

https://udacityenterprise.zendesk.com/hc/en-us/articles/45190164601997-How-do-I-Use-Audio-Slides

Observed documentation includes:

- synchronized audio and slides;
- playback controls;
- adjustable speed;
- timeline navigation;
- direct slide navigation;
- transcript access;
- optional synchronization;
- mobile captions.

Evidence class: E1.

### S07 — Video Transcripts

Official Udacity Enterprise Help Center.

Source:

https://udacityenterprise.zendesk.com/hc/en-us/articles/29297779386253-Video-Transcripts

Observed documentation includes:

- real-time transcript;
- transcript search;
- transcript-to-video timestamp navigation;
- show/hide transcript.

Evidence class: E1.

### S08 — Course Structure

Official Udacity Enterprise Help Center.

Source:

https://udacityenterprise.zendesk.com/hc/en-us/articles/360040227772-What-is-a-Udacity-course-like

Observed documentation includes:

- short videos;
- quizzes;
- exercises;
- problem sets;
- projects.

Evidence class: E1.

### S09 — Project Grading

Official Udacity Support.

Source:

https://support.udacity.com/hc/en-us/articles/208403736-How-does-grading-work-at-Udacity

Observed documentation includes:

- rubric available before submission;
- same rubric used during review;
- `Meets Specifications`;
- `Requires Changes`;
- resubmission after corrections.

Evidence class: E1.

### S10 — Project Review Timeline

Official Udacity Support.

Source:

https://support.udacity.com/hc/en-us/articles/211532546-Project-review-timeline

Observed documentation includes:

- asynchronous project review;
- review completion is not instantaneous.

Evidence class: E1.

### S11 — Submission Failure Guidance

Official Udacity Support.

Source:

https://support.udacity.com/hc/en-us/articles/213037623-Guide-on-submission-error-message

Observed documentation includes:

- submission-failed recovery;
- file-size constraints;
- wrong-file-type handling;
- already-passed project state;
- support escalation.

Evidence class: E1.

### S12 — Learner Support

Official Udacity Enterprise Help Center.

Source:

https://udacityenterprise.zendesk.com/hc/en-us/articles/360040916891-How-can-I-find-support

Observed documentation includes:

- Knowledge Q&A;
- mentor/community support;
- program/project filtering;
- Help Center;
- support tickets.

Evidence class: E1.


### S13 — Classroom Content Feedback

Official Udacity Enterprise Help Center.

Source:

https://udacityenterprise.zendesk.com/hc/en-us/articles/360040862511-How-do-I-report-a-bug-or-an-issue-in-the-classroom-content-I-E-quizzes-lessons-etc

Observed documentation includes:

- contextual lesson feedback;
- issue reporting from learning content.

Evidence class: E1.

### S14 — Media Failure Recovery

Official Udacity Enterprise Help Center.

Source:

https://udacityenterprise.zendesk.com/hc/en-us/articles/360040483292-I-m-not-able-to-access-the-course-videos

Observed documentation includes:

- alternative downloadable video;
- downloadable transcript;
- compatibility checks;
- support escalation.

Evidence class: E1.

### S15 — Workspace Functionality

Official Udacity Enterprise Help Center.

Source:

https://udacityenterprise.zendesk.com/hc/en-us/articles/36266147832973-Workspace-functionalities

Observed documentation includes:

- persistent workspace files;
- refresh;
- destructive reset;
- re-authentication;
- timeout;
- workspace shutdown;
- resource constraints.

Evidence class: E1.

### S16 — Certificate

Official Udacity Support.

Source:

https://support.udacity.com/hc/en-us/articles/209923923-Receiving-a-certificate

Observed documentation includes:

- post-completion graduation steps;
- certificate access;
- print/share capability.

Evidence class: E1.

### S17 — Credential Requirements

Official Udacity Support.

Source:

https://support.udacity.com/hc/en-us/articles/207694906-How-are-your-Udacity-credentials-awarded

Observed documentation includes:

- required program components;
- project completion;
- graduation process;
- identity verification.

Evidence class: E1.

### S18 — Current Catalog

Official Udacity website.

Source:

https://www.udacity.com/catalog

Observed documentation includes:

- program-type filtering;
- skill filtering/search;
- level filtering;
- duration filtering;
- sorting;
- program cards.

Evidence class: E1.

### S19 — Current Program Detail Example

Official Udacity website.

Source:

https://www.udacity.com/course/generative-ai--nd608

Research snapshot exposed:

- program type;
- level;
- duration;
- rating;
- update date;
- skills;
- prerequisites;
- program outline;
- course count;
- lesson count;
- project count;
- reviews;
- enrollment options.

Evidence class: E1.


---

## 4. Learner Dashboard

### Observation

Udacity documents a centralized learner dashboard with:

- Continue Learning;
- recently accessed learning ordered for resumption;
- progress statistics;
- enrollments;
- certificates;
- recommendations;
- career resources.

Evidence: S02, S03.

### User problem

Returning learners need to answer quickly:

~~~text
Where was I?
What should I do next?
How far have I progressed?
What else requires my attention?
~~~

### Inference

A learner dashboard is most valuable when it reduces restart cost.

The strongest behavior is not the existence of dashboard cards.

The stronger experience principle is:

~~~text
return
→ recognize current context
→ resume with minimal navigation
~~~

### CodeInteX disposition

**ADOPT — principle**

Resume learning should be a primary learner-dashboard action.

**MODIFY — progress**

Do not treat raw learning activity as sufficient progress.

Metrics such as:

- hours spent;
- concepts visited;
- lesson count;

may provide context but can become vanity metrics.

CodeInteX should emphasize:

- meaningful completion;
- current position;
- remaining work;
- blockers;
- recommended next learner action.

### Candidate patterns

- `LearnerDashboard`
- `ResumeLearning`

Status: PROVISIONAL PATTERN CANDIDATES.

---

## 5. Course Discovery and Enrollment Decision

### Observation

Current Udacity catalog exposes discovery controls such as:

- program/content type;
- skill;
- level;
- duration;
- sorting.

Current program detail pages expose information including:

- level;
- estimated duration;
- skills;
- prerequisites;
- curriculum outline;
- lessons/projects;
- recency/update information;
- reviews;
- enrollment options.

Evidence: S18, S19.

### User problem

Before committing time or money, a learner needs to determine:

~~~text
Is this for me?
Am I prepared?
What will I learn?
How much work is involved?
What will I produce?
How current is it?
~~~

### Inference

Course discovery should optimize decision quality, not only conversion.

The system should reduce uncertainty before enrollment.

### CodeInteX disposition

**ADOPT — information completeness**

Course/program detail should expose enough information for informed enrollment.

**MODIFY — information hierarchy**

CodeInteX should not copy Udacity's commercial hierarchy or exact marketing presentation.

Priority should follow CodeInteX learner needs and product constraints.

### Candidate patterns

- `CourseDiscovery`
- `CourseOverview`
- `EnrollmentDecisionSupport`

Status: PROVISIONAL PATTERN CANDIDATES.

---

## 6. Program, Course, and Lesson Hierarchy

### Observation

Udacity exposes hierarchical learning navigation across structures comparable to:

~~~text
Program
→ Course
→ Lesson
→ Learning content
~~~

Documented classroom behavior includes:

- course selector;
- expandable/collapsible lesson titles;
- syllabus navigation;
- left-side navigation.

Evidence: S01, S04.

### User problem

Large learning programs create orientation problems:

~~~text
Where am I in the program?
What belongs to this course?
What is complete?
What comes next?
How do I move elsewhere without losing context?
~~~

### Inference

Curriculum hierarchy must be:

- navigable;
- understandable;
- resumable;
- progress-aware.

Hierarchy is an experience contract, not merely a sidebar layout.

### CodeInteX disposition

**ADOPT — hierarchical orientation**

Learners must be able to understand current position and surrounding curriculum.

**MODIFY — navigation implementation**

A permanent left navigation is not intrinsically correct.

Its suitability depends on:

- viewport;
- curriculum depth;
- content density;
- lesson context;
- input modality.

### Candidate patterns

- `CurriculumTree`
- `CurriculumNavigator`
- `CourseSelector`
- `LessonNavigator`

Status: PROVISIONAL PATTERN CANDIDATES.


---

## 7. Lesson Consumption

### Observation

Udacity documents multiple learning modalities including:

- video;
- text;
- quizzes;
- exercises;
- problem sets;
- projects;
- interactive workspaces;
- audio/slide experiences;
- transcripts.

Evidence: S06, S07, S08, S15.

### Observation — media control

Audio Slides documentation exposes learner controls including:

- play/pause;
- previous/next navigation;
- adjustable playback speed;
- volume;
- timeline navigation;
- direct slide navigation;
- transcript access.

Evidence: S06.

### Observation — transcript interaction

Video transcript documentation supports:

- reading alongside media;
- transcript search;
- direct navigation from transcript text to video timestamp;
- show/hide transcript.

Evidence: S07.

### User problem

Learners need different ways to:

- consume learning material;
- revisit material;
- scan for relevant information;
- search within content;
- navigate efficiently;
- control learning pace.

### Inference

Lesson experience should not assume one strictly linear consumption mode.

Learner control is especially important for:

- review;
- accessibility;
- interrupted learning;
- variable prior knowledge;
- different learning speeds.

### CodeInteX disposition

**ADOPT — learner control**

Learners should control reasonable aspects of pacing and navigation.

**ADOPT — transcript-driven navigation**

Where video/audio is used, searchable transcript navigation is a strong candidate capability.

**ADOPT — multimodal representation where useful**

Multiple representations should be supported when they solve a pedagogical or accessibility problem.

**REJECT — modality for novelty**

Audio, animation, interactive slides, AI, or other modalities must not be introduced merely because they are technically possible.

### Candidate patterns

- `LessonExperience`
- `MediaLesson`
- `TranscriptNavigator`
- `InteractiveLesson`

Status: PROVISIONAL PATTERN CANDIDATES.

---

## 8. Resume Learning and Learning Continuity

### Observation

Udacity explicitly documents `Continue Learning` behavior for returning learners.

Learning reminders can also route learners back toward their learning environment.

Evidence: S02, S05.

### User problem

Learning commonly occurs across interrupted sessions.

After returning, learners may otherwise need to reconstruct:

~~~text
What was I studying?
Where did I stop?
What have I completed?
What should I do next?
~~~

### Inference

Resume learning is not merely a button.

It is a continuity contract involving preservation or reconstruction of meaningful learning context.

Potential context includes:

- current course;
- current lesson;
- meaningful last position;
- completion state;
- unfinished assessment;
- unfinished project;
- recommended next action.

### CodeInteX disposition

**ADOPT — resume-first continuity**

The LMS should minimize the cognitive and navigational cost of returning to learning.

### Open questions

Exact semantics still require LMS-domain decisions:

- What counts as the last meaningful position?
- Should simple page visits update resume state?
- How is completed content handled?
- How are multiple concurrent courses prioritized?
- How is stale resume state handled?
- What happens when curriculum structure changes?

### Candidate pattern

`ResumeLearning`

Status: PROVISIONAL PATTERN CANDIDATE.

---

## 9. Learning Progress

### Observation

Udacity dashboard documentation exposes progress-related information including:

- learning activity/time;
- concepts completed;
- lessons completed;
- projects completed.

Evidence: S02.

### User problem

Learners need to understand whether they are moving toward meaningful learning outcomes.

A percentage alone may not answer:

~~~text
Where am I?
What remains?
What should I do next?
Am I blocked?
Have I demonstrated the required capability?
~~~

### Inference

Different metrics represent different concepts.

~~~text
time spent
→ activity

content completed
→ curriculum traversal

assessment/project completion
→ evidence of demonstrated performance
~~~

These should not automatically be treated as equivalent measures of learning.

### CodeInteX disposition

**MODIFY — progress model**

CodeInteX should avoid a progress model dominated by vanity metrics.

Preferred conceptual hierarchy:

~~~text
Current learner position
→ Next meaningful action
→ Required remaining work
→ Blockers or unmet requirements
→ Evidence of mastery/completion
→ Supplemental activity metrics
~~~

Progress should be actionable rather than merely decorative.

### Candidate pattern

`LearningProgress`

### Open questions

The LMS Experience Profile still needs to define:

- progress calculation semantics;
- optional versus required learning items;
- assessment weighting;
- project completion semantics;
- prerequisite effects;
- course versus program progress;
- recalculation after curriculum changes.

Status: PROVISIONAL PATTERN CANDIDATE.


---

## 10. Assessment and Project Workflow

### Observation

Udacity project workflow exposes evaluation criteria before project submission.

Documented behavior includes:

- rubric visible before submission;
- the same rubric used during review;
- result states including `Meets Specifications`;
- result states including `Requires Changes`;
- revision and resubmission after unmet criteria.

Evidence: S09.

### User problem

Learners need to understand:

~~~text
What am I expected to produce?
What counts as acceptable?
How will my work be evaluated?
What happens after submission?
What should I fix if I do not pass?
~~~

### Inference

Assessment is more usable and pedagogically transparent when acceptance criteria are visible before submission.

A rubric can support:

- expectation setting;
- self-review;
- evaluation consistency;
- actionable revision.

### CodeInteX disposition

**ADOPT — transparent criteria**

Learners should know relevant assessment criteria before submitting work.

**ADOPT — actionable evaluation result**

Assessment result should communicate what passed, what did not, and what action remains.

**ADOPT — revision loop where pedagogically appropriate**

Failure should not automatically terminate the learning workflow if revision is part of the intended pedagogy.

### Candidate patterns

- `Assessment`
- `ProjectBrief`
- `ProjectSubmission`
- `ProjectReview`
- `RevisionWorkflow`

Status: PROVISIONAL PATTERN CANDIDATES.

---

## 11. Asynchronous Review State

### Observation

Udacity documents project review as an asynchronous process rather than an immediate result.

Evidence: S10.

### User problem

Long-running evaluation creates uncertainty.

After submission, a learner may need to know:

~~~text
Did my submission succeed?
Is it waiting for review?
Is it currently being reviewed?
Am I blocked?
Can I continue learning?
What happens when review completes?
~~~

### Inference

Asynchronous review should be represented as explicit workflow state.

It should not be modeled as an indefinite generic loading state.

Potential domain states may include:

~~~text
draft
ready-to-submit
uploading
submitted
queued
under-review
changes-required
passed
submission-failed
cancelled
~~~

This is a candidate state model, not yet a locked LMS domain contract.

### CodeInteX disposition

**ADOPT — visible asynchronous workflow**

The learner should be able to distinguish submission success from review completion.

The interface should communicate whether the learner can continue other work while review is pending.

### Candidate pattern

`AssessmentReviewState`

### Open questions

The LMS Experience Profile must still determine:

- canonical review states;
- whether review is human, automated, AI-assisted, or hybrid;
- whether review blocks course progression;
- retry/resubmission rules;
- notification behavior;
- review-history visibility.

Status: PROVISIONAL PATTERN CANDIDATE.

---

## 12. Submission Failure and Recovery

### Observation

Udacity support documentation identifies submission failure conditions including:

- submission/upload failure;
- file-size constraints;
- unsupported file types;
- already-passed project state;
- workflow issues requiring support escalation.

Evidence: S11.

### User problem

Submission is often a high-cost learner action.

A failure may involve:

- lost time;
- uncertainty about whether work was received;
- deadline anxiety;
- repeated uploads;
- risk of losing learner work.

### Inference

Known submission constraints should be communicated before failure whenever feasible.

Recovery should preserve learner context and provide a specific next action.

### CodeInteX disposition

**ADOPT — pre-submit validation**

Where feasible, validate predictable requirements before network submission.

Examples:

- allowed file types;
- size limits;
- required files;
- required fields;
- submission eligibility.

**ADOPT — visible submission state**

The interface should distinguish states such as:

~~~text
ready
validating
uploading
processing
submitted
failed
~~~

Exact domain vocabulary remains OPEN.

**MODIFY — avoid external-help dependency**

A critical submission failure should not require a learner to discover basic recovery instructions in a separate help center.

Primary UI should communicate:

- failure cause;
- preserved work state;
- retry path;
- corrective action;
- escalation path when self-recovery is impossible.

### Candidate pattern

`SubmissionFailureRecovery`

### Risk note

Client-side validation must not replace authoritative backend validation.

Frontend validation improves experience; backend validation remains authoritative for business rules and integrity.

Status: PROVISIONAL PATTERN CANDIDATE.


---

## 13. Resources and Search

### Observation

Udacity consolidates learning resources within a dedicated Resources area.

Public documentation also describes classroom search and Knowledge search.

Evidence: S01, S03, S12.

### User problem

As learning content grows, learners need to relocate material without manually traversing the entire curriculum.

They may need to find:

- a prior lesson;
- a reference;
- project guidance;
- supporting material;
- help related to the current topic.

### Inference

Resources should be retrievable by purpose and context, not merely stored.

Search becomes more valuable as curriculum depth and content volume increase.

### CodeInteX disposition

**ADOPT — consolidated learning resources**

Relevant learning resources should have a predictable access model.

**ADOPT — search when scale justifies it**

Search should not be added as decoration.

It becomes justified when manual navigation no longer provides efficient retrieval.

### Candidate patterns

- `LearningResources`
- `CurriculumSearch`

### Open questions

The LMS Experience Profile must still determine:

- search scope;
- ranking;
- filtering;
- whether transcripts are searchable;
- whether project resources are indexed;
- permission-aware search behavior;
- empty/no-result behavior.

Status: PROVISIONAL PATTERN CANDIDATES.

---

## 14. Graceful Media Degradation

### Observation

Udacity documents alternative access when primary video playback fails, including:

- downloadable video;
- downloadable transcript;
- compatibility troubleshooting;
- support escalation.

Evidence: S14.

### User problem

Media delivery can fail because of:

- network restrictions;
- browser incompatibility;
- device limitations;
- service/provider failure;
- geographic/network policy;
- temporary connectivity issues.

A single fragile media path can block learning entirely.

### Inference

Critical learning content should avoid unnecessary single points of failure where practical.

Alternative representations may preserve learning continuity even when the preferred medium fails.

### CodeInteX disposition

**ADOPT — graceful degradation principle**

Media failure should not automatically mean learning failure.

Possible recovery paths may include:

- alternate media source;
- transcript;
- downloadable material;
- retry;
- compatibility guidance;
- support escalation.

Exact implementation depends on CodeInteX media architecture.

### Candidate pattern

`LearningMediaFallback`

Status: PROVISIONAL PATTERN CANDIDATE.

---

## 15. Learning Schedule and Reminders

### Observation

Udacity allows learners to define a learning schedule and export calendar events through `.ics`.

Documented calendar entries can route the learner back toward the learning environment.

Evidence: S05.

### User problem

Self-paced learning competes with:

- work;
- study;
- family;
- other commitments.

A learner may understand what to do but fail to reserve time to do it.

### Inference

Learning planning can bridge:

~~~text
intention
→ scheduled commitment
→ return to learning
~~~

The underlying problem is continuity and habit support, not calendar integration itself.

### CodeInteX disposition

**ADOPT — problem**

Support for learning planning is worth evaluating.

**MODIFY — implementation**

`.ics` export is one possible implementation and is not a PES requirement.

Potential solutions may include:

- calendar export;
- internal reminders;
- notification integration;
- recurring learning plans;
- learner-defined targets.

### Candidate pattern

`LearningPlan`

### Risk note

Reminder systems can become noisy or manipulative.

Any future implementation should preserve:

- learner control;
- notification preferences;
- easy opt-out;
- appropriate frequency.

Status: PROVISIONAL PATTERN CANDIDATE.

---

## 16. Support and Contextual Feedback

### Observation

Udacity documents multiple support mechanisms including:

- Knowledge Q&A;
- mentor/community pathways;
- Help Center;
- support escalation;
- contextual reporting of learning-content issues.

Evidence: S12, S13.

### User problem

Learner problems are not all the same.

Examples include:

~~~text
content misunderstanding
technical failure
platform failure
content defect
account problem
assessment question
~~~

A single generic support path may lose useful context.

### Inference

Support is more effective when problem context is preserved and the request is routed appropriately.

A content defect should not necessarily follow the same path as an account-access problem.

### CodeInteX disposition

**ADOPT — contextual support principle**

Support entry points should preserve useful context where feasible.

**MODIFY — support architecture**

Exact channels should depend on CodeInteX operational capacity.

The system should not promise mentor, community, or human-support capability unless CodeInteX can actually operate it reliably.

### Candidate patterns

- `ContextualHelp`
- `ContentFeedback`
- `SupportEscalation`

### Operational risk

Every visible support channel creates an operational obligation.

Product design must account for:

- ownership;
- response expectations;
- escalation;
- abuse handling;
- privacy;
- staffing or automation boundaries.

Status: PROVISIONAL PATTERN CANDIDATES.


---

## 17. Workspace Continuity and Destructive Operations

### Observation

Udacity workspace documentation distinguishes operations including:

- refresh workspace;
- reset workspace;
- re-authenticate;
- shutdown;
- timeout configuration.

Reset can remove previous learner work, whereas refresh is intended to restore or recover workspace files.

Evidence: S15.

### User problem

Technical-learning environments may contain learner-created work whose accidental loss is costly.

The learner must be able to distinguish between:

~~~text
recover environment
and
destroy/reset learner state
~~~

### Inference

Destructive workspace operations require stronger communication and confirmation than routine recovery actions.

### CodeInteX disposition

**ADOPT — risk-proportionate destructive-action semantics**

The UI must clearly communicate:

- what will be changed;
- whether learner work will be deleted;
- whether the action is reversible;
- what recovery options remain.

This is consistent with PES Experience Constitution.

### Candidate pattern

`LearningWorkspaceRecovery`

### Applicability

This pattern is relevant only if CodeInteX provides hosted or persistent learning workspaces.

Status: PROVISIONAL PATTERN CANDIDATE.

---

## 18. Completion and Credentials

### Observation

Udacity documents graduation requirements and certificate access after required program completion.

Credential eligibility may depend on completion of required program components and graduation steps.

Evidence: S16, S17.

### User problem

Learners need an unambiguous answer to:

~~~text
Am I finished?
What requirement remains?
What did I earn?
How can I access it?
How can I share or verify it?
~~~

### Inference

Completion should be represented as an explicit domain state transition rather than inferred only from a progress percentage.

Credential issuance is related to, but distinct from, learning progress.

### CodeInteX disposition

**ADOPT — explicit completion criteria**

Learners should be able to understand remaining requirements before completion.

**ADOPT — durable credential access where applicable**

If CodeInteX issues credentials, learners should retain a predictable way to access them.

### Candidate patterns

- `Completion`
- `Credential`
- `Certificate`

### Open questions

The LMS Experience Profile must still determine:

- exact completion rules;
- optional versus mandatory activities;
- credential eligibility;
- revocation or correction;
- verification mechanism;
- expiration where relevant.

Status: PROVISIONAL PATTERN CANDIDATES.

---

## 19. Responsive and Mobile Evidence

### Verified observation

Udacity Audio Slides documentation explicitly describes mobile behavior including:

- simplified controls;
- slide navigation;
- captions during playback.

Evidence: S06.

### Evidence limitation

The public evidence collected in this benchmark is insufficient to establish current Udacity behavior across:

- all breakpoints;
- landscape mode;
- tablets;
- touch-target sizing;
- complex curriculum reflow;
- workspace usability on mobile;
- project submission on mobile.

### Inference

Limited mobile evidence must not be generalized into a complete responsive model.

### CodeInteX disposition

**DO NOT INFER**

Responsive architecture must be validated independently against CodeInteX target devices, content, workflows, and accessibility requirements.

### Benchmark state

Unverified responsive behavior is classified as:

`E4 — Unknown`.

---

## 20. Accessibility Evidence

### Vendor statement

Udacity states that its learner-experience redesign was intended to improve accessibility.

Evidence: S01.

This is a vendor statement, not independent conformance evidence.

### Verified accessibility-supporting capabilities

Public documentation confirms capabilities that may support accessible or alternative consumption, including:

- transcripts;
- captions in documented Audio Slides mobile behavior;
- adjustable playback speed;
- alternative learning-media access in selected failure scenarios.

Evidence: S06, S07, S14.

### Not verified

This benchmark does not establish conformance for:

~~~text
WCAG 2.2 AA
keyboard accessibility
screen-reader semantics
focus management
contrast requirements
zoom and reflow
accessible authentication
touch-target requirements
error identification
status announcements
~~~

### Inference

Presence of accessibility-supporting features does not prove overall product accessibility.

### CodeInteX disposition

**REJECT — vendor accessibility claim as proof**

CodeInteX retains its independent:

- WCAG 2.2 AA baseline;
- keyboard evaluation;
- screen-reader evaluation;
- focus evaluation;
- zoom/reflow evaluation;
- contrast validation;
- critical-workflow manual testing.

Accessibility evidence from a benchmark can inform design, but cannot replace CodeInteX validation.

---

## 21. Empty, Error, Partial, Offline, and Permission States

### Verified evidence

Public Udacity documentation provides evidence for selected failure and recovery scenarios including:

- project submission failure;
- video-access failure;
- workspace re-authentication/recovery;
- support escalation.

Evidence: S11, S14, S15.

### Evidence gaps

Current public evidence is insufficient for systematic evaluation of:

- empty learner dashboard;
- no-enrollment state;
- no-certificate state;
- partial dashboard loading;
- dashboard network errors;
- offline lesson behavior;
- permission-denied UI;
- stale learner data;
- interrupted save behavior;
- failed progress synchronization.

### Inference

Happy-path evidence must not be treated as evidence of robust state handling.

### CodeInteX disposition

These states remain benchmark gaps.

CodeInteX must define and validate them independently.

### PES implication

Relevant product workflows should explicitly evaluate:

~~~text
loading
empty
partial
error
permission-denied
stale
offline
success
~~~

according to context.

Unobserved Udacity behavior remains:

`E4 — Unknown`.


---

## 22. Adopt / Modify / Reject Summary

### ADOPT

Principles currently supported strongly enough to become LMS design inputs:

- resume-first learner continuity;
- explicit curriculum hierarchy;
- transparent course prerequisites and expectations;
- visible and actionable learning progress;
- searchable/filterable discovery when content scale justifies it;
- learner-controlled media consumption;
- transcript-driven media navigation;
- transparent assessment criteria;
- explicit asynchronous review state;
- contextual submission failure recovery;
- consolidated learning resources;
- contextual learner support;
- explicit completion requirements.

These are experience inputs.

They are not yet final UI components or implementation choices.

### MODIFY

Patterns worth carrying forward but requiring CodeInteX-specific interpretation:

- dashboard composition;
- progress metrics;
- left-navigation model;
- course recommendations;
- learning reminders;
- certificate prominence;
- support-channel architecture;
- calendar integration;
- workspace recovery;
- catalog filtering.

### REJECT

The following must not be imported from the benchmark:

- Udacity visual identity;
- pixel-level layouts;
- branding;
- Udacity-specific terminology where CodeInteX domain language differs;
- vendor-specific infrastructure assumptions;
- activity metrics treated automatically as learning outcomes;
- recommendation systems without demonstrated user value;
- accessibility claims without independent validation;
- external-help dependency for failures that should be recoverable in-context.

---

## 23. Pattern Candidates for LMS Experience Profile

Evidence collected in this benchmark currently supports investigation of the following working taxonomy.

### Learner orientation and continuity

~~~text
LearnerDashboard
ResumeLearning
LearningPlan
~~~

### Discovery and enrollment

~~~text
CourseDiscovery
CourseOverview
EnrollmentDecisionSupport
~~~

### Curriculum navigation

~~~text
CurriculumTree
CurriculumNavigator
CourseSelector
LessonNavigator
~~~

### Lesson experience

~~~text
LessonExperience
MediaLesson
TranscriptNavigator
InteractiveLesson
LearningMediaFallback
~~~

### Progress

~~~text
LearningProgress
~~~

### Assessment and projects

~~~text
Assessment
ProjectBrief
ProjectSubmission
ProjectReview
RevisionWorkflow
AssessmentReviewState
SubmissionFailureRecovery
~~~

### Resources and support

~~~text
LearningResources
CurriculumSearch
ContextualHelp
ContentFeedback
SupportEscalation
~~~

### Technical learning environment

~~~text
LearningWorkspaceRecovery
~~~

### Completion and credentials

~~~text
Completion
Credential
Certificate
~~~

### Decision state

This taxonomy is:

**OPEN / PROVISIONAL**

Names and boundaries are not yet locked.

A future LMS Experience Profile may:

- merge candidates;
- split candidates;
- rename candidates;
- reject candidates;
- add missing patterns.

---

## 24. Cross-Benchmark Requirements

Udacity alone is insufficient evidence for final LMS experience decisions.

Specialist evidence is still required for areas where Udacity public evidence is incomplete or where another product class offers stronger evidence.

Priority areas include:

- accessibility;
- assessment/project workflow;
- technical-learning workspace UX;
- mobile learning;
- instructor experience;
- administration;
- community/discussion;
- analytics;
- personalization;
- AI-assisted learning.

Canonical benchmark strategy remains:

~~~text
Primary learner benchmark
+
Specialist benchmarks
+
HCI / accessibility evidence
+
CodeInteX product evidence
+
Usability validation
~~~

### Benchmark-selection rule

A specialist benchmark should only be added when it answers a concrete unresolved question.

Do not accumulate benchmark products merely to create a large comparison set.

---

## 25. Key Inferences for CodeInteX LMS

The following are CodeInteX inferences derived from the evidence.

They are not observations about Udacity.

### I01 — Resume cost should be minimized

A returning learner should not reconstruct context manually after every interruption.

### I02 — Progress should drive action

Progress should answer:

~~~text
Where am I?
What remains?
What should I do next?
Is anything blocking me?
~~~

### I03 — Curriculum hierarchy is experience infrastructure

Curriculum hierarchy should not be modeled only as one page-specific sidebar implementation.

It is a domain-level navigation and orientation concern.

### I04 — Assessment is a workflow

Assessment should be modeled approximately as:

~~~text
understand requirements
→ perform work
→ self-check
→ submit
→ wait / review
→ receive result
→ revise or complete
~~~

Exact states remain domain-specific.

### I05 — Media requires learner control

Media experience should support reasonable control over:

- pacing;
- navigation;
- revisiting;
- alternate representation;
- recovery.

### I06 — Failure states should preserve continuity

Failure should avoid unnecessary loss of:

- learner work;
- progress;
- context;
- current position;
- next action.

### I07 — Completion is not merely percentage

Completion requires explicit domain rules and should communicate whether required outcomes have actually been met.

### I08 — Domain state must be explicit

Important learner workflows should not hide domain states behind generic UI states such as:

~~~text
loading
done
error
~~~

Where the domain distinguishes:

~~~text
submitted
queued
under-review
changes-required
passed
~~~

the experience may need to preserve those distinctions.

### I09 — Support design creates operational obligations

A support surface is not only UI.

It creates expectations around:

- ownership;
- response;
- escalation;
- privacy;
- moderation;
- reliability.

---

## 26. Risks of Misusing This Benchmark

### Risk 1 — Visual imitation

Failure mode:

~~~text
Udacity is the primary benchmark
→
CodeInteX should look like Udacity
~~~

This conclusion is invalid.

### Risk 2 — Cargo-cult metrics

Metrics such as:

- hours studied;
- lessons completed;
- content viewed;

can become misleading if interpreted as learning outcomes without stronger evidence.

### Risk 3 — Legacy-pattern inheritance

A mature product may contain interaction patterns caused by:

- historical architecture;
- organizational constraints;
- legacy systems;
- existing customer expectations.

CodeInteX should not inherit those constraints automatically.

### Risk 4 — Enterprise versus individual learner divergence

Some evidence comes from Udacity Enterprise documentation.

Enterprise learners may have different:

- enrollment behavior;
- permissions;
- reporting;
- support;
- program assignment;

than direct consumer learners.

### Risk 5 — Public-observation limitation

Public documentation does not expose every authenticated state.

Absence of public evidence is not evidence that a behavior does not exist.

### Risk 6 — Benchmark authority inflation

Presence of a pattern in Udacity does not prove:

- optimality;
- accessibility;
- usability;
- suitability for CodeInteX;
- architectural correctness.

### Risk 7 — Overfitting one benchmark

If CodeInteX uses Udacity as the answer to every LMS question, it will reduce independent product reasoning.

Udacity should remain a primary evidence source, not the sole source of truth.


---

## 27. Evidence Gaps

The following areas remain insufficiently verified through the current public-source benchmark:

- complete authenticated learner journey;
- detailed keyboard navigation;
- screen-reader behavior;
- focus order;
- focus restoration;
- exact responsive behavior;
- touch-target behavior;
- loading-state behavior;
- empty-state behavior;
- offline behavior;
- permission-denied behavior;
- stale-data handling;
- interrupted-save behavior;
- exact progress calculation;
- assessment accessibility;
- detailed project-upload interaction;
- credential accessibility;
- learner notification center;
- personalization controls;
- recommendation controls;
- privacy behavior around personalization;
- current learner community experience.

### Evidence rule

These gaps must remain explicit.

Do not convert:

~~~text
not observed
~~~

into:

~~~text
does not exist
~~~

and do not convert:

~~~text
likely behavior
~~~

into:

~~~text
verified behavior
~~~

### Decision state

Evidence gaps remain **OPEN** until supported by sufficient evidence.

---

## 28. Implications for the LMS Experience Profile

The benchmark evidence supports development of an initial LMS Experience Profile around at least the following experience domains:

- learner orientation;
- resume learning;
- course discovery;
- course overview;
- enrollment decision support;
- curriculum hierarchy;
- lesson navigation;
- lesson consumption;
- learning progress;
- assessment;
- project submission;
- asynchronous review;
- revision;
- learning resources;
- contextual support;
- completion;
- credentials.

### Each domain contract should eventually define

- user intent;
- domain semantics;
- information requirements;
- workflow;
- states;
- actions;
- failure modes;
- recovery;
- accessibility;
- responsive behavior;
- content requirements;
- relevant analytics signals;
- dependencies on PES Core.

### Boundary

The LMS Experience Profile should describe domain experience contracts.

It should not redefine:

- global tokens;
- typography foundations;
- spacing foundations;
- global component semantics;
- accessibility baseline;
- theme architecture.

Exact LMS component taxonomy remains OPEN.

---

## 29. What This Evidence Does Not Yet Justify

This benchmark does not provide sufficient evidence to lock:

- final CodeInteX visual language;
- final typography;
- final color palette;
- final spacing scale;
- final radius system;
- final elevation system;
- final density system;
- exact learner-dashboard layout;
- exact navigation layout;
- exact responsive breakpoints;
- exact mobile navigation;
- final animation language;
- final iconography implementation;
- shadcn/ui component selection;
- Base UI primitive selection;
- Tailwind implementation details;
- data-visualization library;
- AI-agent UI framework;
- LMS repository topology;
- final LMS domain-component taxonomy.

### Principle

Benchmark evidence should lock a decision only when the evidence actually addresses that decision.

Do not use learner-workflow evidence to justify unrelated visual or technical choices.

---

## 30. Benchmark Decision State

### LOCKED

Existing benchmark governance:

- Udacity is the PRIMARY learner-experience benchmark for CodeInteX LMS.
- Udacity is not a visual template.
- Benchmark observations must remain distinguishable from CodeInteX inference.
- Benchmark presence does not prove optimality.
- Accessibility requires independent CodeInteX validation.
- Product implementation must not copy benchmark identity.

### PROVISIONAL

The following remain provisional outputs of this evidence pack:

- pattern candidates;
- CodeInteX LMS inferences;
- Adopt / Modify / Reject dispositions;
- initial LMS experience-domain grouping.

These must be tested against:

- product requirements;
- specialist evidence;
- accessibility;
- implementation constraints;
- usability evidence.

### OPEN

Still open:

- final LMS pattern taxonomy;
- exact progress semantics;
- exact assessment state model;
- specialist benchmark set;
- responsive strategy;
- learner-support operating model;
- credential model;
- personalization model;
- AI-learning interaction model.

---

## 31. Recommended Next Step

Do not immediately convert every pattern candidate into implementation components.

The next decision activity should be:

~~~text
Evidence-gap review
        ↓
Select specialist benchmarks only where needed
        ↓
Resolve high-risk gaps
        ↓
Draft LMS Experience Profile v0.1
        ↓
Reference implementation
        ↓
Accessibility and usability validation
        ↓
Promote, revise, or reject provisional patterns
~~~

### Highest-priority evidence gaps

Initial priority:

1. accessibility of critical learner workflows;
2. assessment and project workflow;
3. mobile/responsive lesson experience;
4. actionable progress and learner dashboard;
5. technical-learning workspace UX if hosted workspaces enter scope.

### Constraint

Specialist benchmark research must be problem-driven.

Do not create a large benchmark matrix unless it materially improves a decision.

---

## 32. Document Status

This document is an:

**EVIDENCE BASELINE — PROVISIONAL v0.1**

It is not a normative LMS specification.

The following distinctions must be preserved:

~~~text
Udacity observation
≠
CodeInteX inference

CodeInteX inference
≠
LOCKED requirement

pattern candidate
≠
implementation component
~~~

Observed benchmark behavior may inform CodeInteX decisions.

It does not automatically determine them.

Any future normative LMS decision derived from this evidence must be recorded in the relevant specification and, when material, reflected in the PES Decision Log.
