# CodeInteX Web Implementation Profile v0.1

- **Project:** CodeInteX
- **Workstream:** PES / Web Implementation
- **Artifact type:** Implementation Profile
- **Status:** PROVISIONAL IMPLEMENTATION BASELINE
- **Version:** 0.1
- **Date:** 2026-09-19
- **Canonical location:** `docs/pes/`
- **Consumes:** PES Core + LMS Experience Profile
- **Primary target:** CodeInteX learner-facing web application
- **Repository/package topology:** OPEN

---

## 0. Purpose

This document defines the web-implementation contract used to realize CodeInteX product experience requirements.

It translates:

~~~text
PES Core
+
LMS Experience Profile
~~~

into technology-specific implementation constraints.

It answers questions such as:

~~~text
Which web runtime is used?
How are semantic tokens consumed?
Where do behavioral primitives live?
How are CodeInteX UI components owned?
How are accessibility and responsive contracts implemented and tested?
Which dependencies are allowed to define behavior?
~~~

It does not redefine learner-domain semantics.

### Authority

If an implementation choice conflicts with:

- PES Core;
- PES Consumption Contract;
- LMS Experience Profile;

the implementation choice must adapt unless the higher-authority contract is formally revised.

### Implementation principle

Technology exists to implement the experience architecture.

The experience architecture must not be redesigned around incidental framework or library defaults.

**Decision state: LOCKED**

---

## 1. Scope and Responsibility

### This profile owns

The Web Implementation Profile owns web-specific decisions for:

- framework/runtime;
- rendering boundary;
- TypeScript usage;
- styling engine;
- semantic-token consumption;
- behavioral primitive integration;
- CodeInteX-owned component implementation;
- client/server component boundary;
- responsive implementation mechanics;
- accessibility implementation mechanics;
- animation dependency policy;
- icon dependency policy;
- isolated component development/testing;
- dependency governance;
- implementation validation.

### This profile does not own

It does not own:

- PES experience constitution;
- semantic meaning of PES tokens;
- LMS learner-domain rules;
- completion policy;
- grading policy;
- credential policy;
- backend persistence;
- API business authority;
- Wagtail model structure;
- hosting/provider choice;
- repository topology unless separately decided.

### Implementation boundary

Preferred relationship:

~~~text
PES contracts
↓
Product Experience Profile
↓
Web Implementation Profile
↓
CodeInteX-owned UI implementation
↓
approved behavioral / technical dependencies
~~~

Libraries are implementation dependencies.

They are not architectural authorities.

**Decision state: LOCKED**

---

## 2. Verified Web Technology Baseline

The following baseline is verified against current official project documentation as of 2026-09-19.

### Next.js

Use the supported Next.js 16 major line.

Current support status:

~~~text
Next.js 16.x = Active LTS
Next.js 15.x = Maintenance LTS
~~~

The web profile targets:

~~~text
Next.js 16.x
App Router
~~~

The project must use a currently security-patched release within the supported 16.x line.

At this document date, official Next.js security guidance identifies `16.3.3` as the patched Active-LTS baseline for the August 2026 critical security release.

This number is a historical minimum at document time, not a permanent version pin.

### React

Use the React version supported by the selected Next.js 16 App Router release.

React 19.2 is the current stable React release verified for this baseline.

Do not independently upgrade React beyond framework compatibility merely to obtain newer APIs.

### TypeScript

TypeScript is required for learner-facing web implementation.

Implementation should use strict typing appropriate to the application and dependency ecosystem.

Exact compiler-version pinning belongs to repository dependency management.

### Tailwind CSS

Use Tailwind CSS 4.x as the primary styling implementation engine.

Tailwind is not the source of truth for CodeInteX semantic design decisions.

It consumes and exposes PES-derived semantics.

### Base UI

Use Base UI as the default behavioral primitive foundation for new CodeInteX web components where an appropriate primitive exists.

Base UI is:

- unstyled;
- React-based;
- composable;
- compatible with Tailwind;
- intended for accessible UI primitives.

### shadcn/ui

shadcn/ui may be used as a CodeInteX component bootstrap and implementation source.

For new projects, current shadcn/ui defaults to Base UI while continuing to support other primitive foundations.

Code adopted through shadcn becomes CodeInteX-owned source code.

shadcn/ui is not treated as an external runtime design-system authority.

### Current source references

- Next.js support policy:
  `https://nextjs.org/support-policy`
- Next.js App Router:
  `https://nextjs.org/docs/app`
- Next.js August 2026 security release:
  `https://nextjs.org/blog`
- React 19.2:
  `https://react.dev/blog/2025/10/01/react-19-2`
- Tailwind CSS:
  `https://tailwindcss.com/`
- shadcn/ui Base UI default:
  `https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default`
- Base UI:
  `https://base-ui.com/`

**Decision state: LOCKED baseline families; exact patch versions governed operationally**

---

## 3. Dependency Layering Contract

The UI dependency architecture should be interpreted as:

~~~text
PES semantic contracts
↓
CodeInteX semantic tokens
↓
CodeInteX-owned UI components
↓
behavioral primitives where needed
↓
browser / React runtime
~~~

### shadcn and Base UI relationship

Do not model:

~~~text
shadcn component system
+
Base UI component system
~~~

as two parallel CodeInteX UI architectures.

For the current baseline:

~~~text
CodeInteX component
    may originate from shadcn source
        ↓
    may use Base UI primitive
~~~

The CodeInteX component is the product-facing implementation boundary.

### Product code boundary

Product/domain screens should normally consume CodeInteX-owned components rather than importing low-level Base UI primitives throughout the application.

Direct primitive usage may be appropriate while constructing or extending the CodeInteX component layer.

### Library-default rule

Library default:

~~~text
≠
PES requirement
~~~

If a dependency default conflicts with:

- semantics;
- accessibility;
- responsive behavior;
- content design;
- theme contract;

the CodeInteX implementation must adapt or replace the dependency behavior.

### Replacement principle

The architecture should allow a behavioral dependency to be replaced without rewriting LMS domain semantics.

This does not require zero migration cost.

It requires that domain contracts are not coupled unnecessarily to one primitive library API.

### Dependency minimization

Do not add overlapping UI libraries merely because each provides a useful component.

New dependency introduction requires a concrete capability gap.

**Decision state: LOCKED**


---

## 4. Next.js and React Execution Model

### Default execution model

The CodeInteX learner-facing web application uses the Next.js App Router execution model.

React Server Components are the default rendering boundary unless a component requires client-side capabilities.

The default question should therefore be:

~~~text
Does this component need to execute on the client?
~~~

not:

~~~text
Can this component be made a Client Component?
~~~

### Server-first principle

Prefer Server Components for UI that primarily:

- receives domain data;
- composes content;
- renders learner state;
- produces static or request-derived markup;
- does not require browser-only APIs;
- does not require client-side interaction state.

### Client interaction principle

Use Client Components when required for behavior such as:

- event-driven interaction;
- local interactive state;
- browser APIs;
- client-side focus orchestration;
- interactive disclosure;
- drag/drop where justified;
- media controls requiring browser state;
- other behavior that cannot execute appropriately on the server.

### Network-boundary principle

`use client` establishes a client module boundary.

It should be placed deliberately rather than propagated broadly through the component tree.

### Anti-pattern

Do not mark a major application subtree as client-rendered merely because one nested control requires interactivity.

Prefer:

~~~text
Server Component
├── server-rendered content
├── server-rendered learner state
└── small Client Component interaction island
~~~

over:

~~~text
'use client'

entire learner page
└── everything executes as client bundle
~~~

unless application requirements genuinely justify the latter.

### Framework capability versus architecture

Next.js technically permits multiple data-access models.

Framework capability does not override CodeInteX architecture.

The learner-facing implementation must preserve:

~~~text
authoritative domain source
→ domain/API contract
→ web adapter/view model
→ PES-aware UI
~~~

### Rendering strategy

Rendering strategy should be selected from actual requirements.

Possible strategies may include:

- server rendering;
- static rendering;
- streaming;
- client interaction after server rendering;
- appropriate caching/revalidation.

Do not select rendering behavior solely because a Next.js feature exists.

### Cache boundary

Cache policy must preserve correctness for learner-specific and mutable state.

Data such as:

- submission state;
- assessment result;
- progress;
- access eligibility;
- completion;
- credential status;

must not be presented from caching behavior that can knowingly violate required freshness semantics.

Exact caching policy remains OPEN until backend/API characteristics are established.

**Decision state: LOCKED execution model; OPEN route-specific rendering and caching policy**

---

## 5. Server and Client Component Boundary

### Server Component default

Components are Server Components unless client execution is required.

This default helps reduce unnecessary browser JavaScript and keeps server-only capabilities outside the browser bundle.

### Client Component triggers

A component generally requires client execution when it depends on:

- React client state;
- event handlers;
- lifecycle/effect behavior;
- browser APIs;
- interactive third-party primitives requiring client runtime.

### Boundary placement

Place the client boundary as low in the component tree as practical while maintaining coherent component ownership.

Example:

~~~text
LessonPage                         [Server]
├── LessonHeader                  [Server]
├── LessonContent                 [Server]
├── ProgressSummary               [Server]
├── Transcript                    [Server where possible]
└── LessonControls                [Client]
    ├── PreviousAction
    ├── NextAction
    └── InteractiveDisclosure
~~~

The exact decomposition depends on actual behavior.

### PES component implication

A CodeInteX-owned component does not have to be universally Server or Client.

Component architecture may expose separate implementations or composition boundaries where necessary.

For example:

~~~text
AssessmentSummary                 [Server]
AssessmentForm                    [Client]
~~~

may be preferable to converting the entire assessment surface into one large Client Component.

### Behavioral primitives

Base UI primitives may require client-side execution depending on the primitive and interaction.

This requirement should remain localized to the relevant interactive component boundary.

Do not allow low-level primitive requirements to force unrelated product content into the client bundle.

### Provider discipline

Global Client Component providers increase the client execution surface.

Add a global provider only when:

- the concern genuinely spans the relevant application;
- local composition is insufficient;
- lifecycle and ownership are clear.

Potential examples require case-by-case justification.

Do not create global providers merely for convenience.

### State-placement rule

State should live at the lowest layer that legitimately owns it.

Distinguish:

~~~text
authoritative domain state
server-derived view state
client interaction state
ephemeral presentation state
~~~

These are not interchangeable.

### Authoritative state

Client state must not become the source of truth for authoritative learner facts such as:

- submitted;
- passed;
- completed;
- credentialed;
- access granted.

Client state may optimistically represent a pending operation where appropriate, but authoritative confirmation must replace or reconcile it.

### Hydration and consistency

Server-rendered and client-rendered output must avoid knowingly inconsistent learner state.

Hydration workarounds must not be used to conceal architecture errors in domain-state ownership.

### Browser-only code

Browser APIs must remain behind client-compatible boundaries.

Do not reference browser globals from server-only modules.

### Anti-patterns

Avoid:

- `'use client'` in every component;
- one giant application-wide client boundary;
- duplicate server and client sources of authoritative learner state;
- business rules implemented only inside React component state;
- low-level primitive APIs leaking throughout domain screens.

**Decision state: LOCKED boundary principles**

---

## 6. Domain Data, Adapter, and TypeScript Contract

### Architectural rule

Learner-facing components should consume web-facing domain contracts rather than raw persistence or CMS structures.

Required conceptual path:

~~~text
backend / domain authority
↓
API or service contract
↓
web data-access boundary
↓
adapter / view model
↓
CodeInteX UI component
~~~

### Wagtail boundary

Do not bind learner components directly to Wagtail-specific model shape merely because Wagtail currently provides the underlying content.

For example, product UI should prefer a semantic contract such as:

~~~text
CourseOverview
CurriculumSection
Lesson
LearnerProgress
AssessmentAttempt
SubmissionState
~~~

rather than exposing CMS implementation structure throughout React components.

### Adapter responsibility

The adapter/view-model layer may:

- normalize backend payloads;
- convert transport naming to product-domain naming;
- derive presentation-safe values;
- map operational states to learner-facing states;
- validate assumptions at a system boundary where appropriate.

It must not invent authoritative business outcomes.

### Example

Backend operational states may contain:

~~~text
marking_started
moderation_pending
ready_for_release
~~~

while a learner-facing contract may expose:

~~~text
underReview
~~~

when those distinctions do not change learner action.

That mapping should live in an explicit adapter/domain boundary rather than being rediscovered independently by multiple components.

### TypeScript rule

TypeScript types should express meaningful domain distinctions.

Prefer:

~~~text
type SubmissionState =
  | 'draft'
  | 'submitting'
  | 'submitted'
  | 'submissionFailed'
~~~

over unconstrained:

~~~text
status: string
~~~

when the state space is known.

### Separate state dimensions

Do not force unrelated domain concepts into one union solely for UI convenience.

Prefer conceptual separation such as:

~~~text
submissionState
evaluationState
completionState
credentialState
~~~

when those dimensions can vary independently.

### Transport type versus UI type

Transport/API types and UI-facing types are allowed to differ.

Example:

~~~text
API payload
↓
validated / mapped
↓
LearnerProgressView
~~~

This is intentional when it protects:

- semantic clarity;
- backend replaceability;
- UI maintainability.

### Boundary validation

TypeScript static typing does not validate untrusted runtime data by itself.

Where external or backend data can violate assumed shape, runtime validation should be considered at the appropriate boundary.

The exact validation library remains OPEN.

### Nullability

Null, absent, unknown, pending, unavailable, and zero are not automatically equivalent states.

Types should preserve meaningful distinctions where learner behavior depends on them.

### Error representation

Expected domain failures should be modeled sufficiently for learner recovery.

Do not make components parse arbitrary error strings to determine domain action.

Prefer structured error/state contracts.

### API ownership

The frontend may request improvements to API contracts when needed to represent the learner experience correctly.

It must not compensate indefinitely for missing authoritative semantics by embedding duplicated business logic in React.

### Generated types

Generated API types may be used where appropriate.

Generated types do not eliminate the need for domain adapters when transport semantics differ from learner-facing semantics.

### Type escape hatches

Use of:

- `any`;
- broad type assertions;
- unchecked casts;

at domain boundaries should be minimized and justified.

They must not become the mechanism used to suppress contract mismatches.

### Agent implication

AI coding agents should treat TypeScript errors at domain boundaries as potential contract mismatches, not merely obstacles to bypass with assertions.

**Decision state: LOCKED domain/type boundary; OPEN runtime-validation tooling and API code-generation strategy**


---

## 7. Semantic Token Consumption Contract

### Source of truth

PES semantic tokens are the authoritative source for cross-product visual semantics.

The web implementation consumes those semantics.

It must not redefine them independently inside:

- Tailwind configuration;
- component source;
- route-level CSS;
- shadcn-generated defaults;
- Base UI styling;
- product-local utility conventions.

### Conceptual flow

~~~text
PES semantic meaning
↓
serialized web token representation
↓
CSS custom properties / implementation variables
↓
Tailwind theme exposure where useful
↓
CodeInteX component styles
~~~

### Serialization boundary

The exact canonical token serialization format is still OPEN.

Possible implementation mechanisms may include:

- generated CSS custom properties;
- generated TypeScript metadata;
- build-time transforms;
- a combination of those.

This profile locks the consumption relationship, not the final serialization pipeline.

### Semantic naming

Product components should consume semantic intent rather than raw visual values where an appropriate semantic token exists.

Prefer concepts such as:

~~~text
surface
foreground
border
muted
accent
critical
success
focus
~~~

over arbitrary usage such as:

~~~text
gray-950
blue-600
#18181b
17px
~~~

when those values are representing a PES-defined semantic decision.

Exact canonical token names remain governed by PES Core.

### Raw values

Raw values may still be legitimate for:

- truly local implementation mechanics;
- calculations;
- browser workarounds;
- one-off values not representing reusable design semantics.

They should not silently become an alternate token system.

### Component ownership

CodeInteX-owned components should consume semantic tokens through a stable implementation surface.

Product/domain screens should not repeatedly reconstruct token mapping independently.

### Theme contract

Theme changes may alter permitted visual values.

Theme changes must not alter:

- component meaning;
- domain behavior;
- hierarchy;
- accessibility requirement;
- workflow logic.

### Accessibility

Semantic token implementation must preserve required contrast and focus visibility.

A token value that fails accessibility cannot be justified merely because it belongs to the configured theme.

### Agent rule

AI coding agents should prefer existing semantic tokens over introducing arbitrary raw values.

If no appropriate semantic token exists:

~~~text
do not invent a parallel token casually
~~~

Escalate or explicitly mark the gap according to PES governance.

**Decision state: LOCKED consumption architecture; OPEN serialization format and final token vocabulary**

---

## 8. Tailwind CSS Implementation Boundary

### Role

Tailwind CSS 4.x is the primary styling implementation engine for the current web baseline.

Tailwind provides:

- utility generation;
- responsive utilities;
- state variants;
- theme-variable integration;
- composition mechanisms.

Tailwind does not own CodeInteX design semantics.

### Tailwind theme variables

Tailwind 4 theme variables may expose CodeInteX semantic values to utility classes.

Conceptually:

~~~text
PES semantic token
↓
CSS variable
↓
Tailwind theme variable mapping
↓
semantic utility usage
~~~

Example architecture:

~~~css
:root {
  --cx-surface-default: ...;
  --cx-text-default: ...;
}

@theme inline {
  --color-background: var(--cx-surface-default);
  --color-foreground: var(--cx-text-default);
}
~~~

The example illustrates mapping only.

Exact variable names are not locked by this document.

### Utility semantics

Prefer semantic utility composition such as:

~~~text
bg-background
text-foreground
border-border
~~~

when those utilities map to approved semantic tokens.

Avoid spreading raw palette utilities throughout product UI when they represent product semantics.

### Arbitrary values

Tailwind arbitrary values are permitted when technically appropriate.

They must not become a routine escape hatch around:

- PES tokens;
- component contracts;
- responsive rules;
- accessibility requirements.

### Responsive utilities

Tailwind breakpoints are implementation mechanics.

PES responsive requirements are based on learner outcome and content behavior, not named breakpoint labels.

Do not encode product meaning such as:

~~~text
mobile = sm
tablet = md
desktop = lg
~~~

as an architectural assumption.

Responsive behavior should respond to actual layout/content constraints.

Exact breakpoint values remain OPEN.

### Component extraction

Repeated semantic patterns should generally converge into:

- CodeInteX-owned components;
- reusable variants;
- documented composition patterns;

rather than duplicated long utility strings across domain screens.

This does not require extracting every repeated class combination.

Avoid abstraction that provides no semantic or maintenance benefit.

### Global CSS

Global CSS should be limited to concerns that are legitimately global, such as:

- token exposure;
- base document behavior;
- typography foundations where required;
- carefully scoped browser normalization;
- global accessibility behavior.

Domain-component styling should not accumulate indiscriminately in one global stylesheet.

### Dark/theme variants

Theme switching, if activated, should operate through semantic token substitution.

Domain components should not contain parallel duplicated business-specific dark-mode implementations where token substitution is sufficient.

### Tailwind configuration authority

Tailwind configuration must reflect the approved implementation mapping.

It must not become a second source of truth for:

- brand colors;
- spacing semantics;
- typography semantics;
- component behavior.

**Decision state: LOCKED Tailwind role; OPEN breakpoint system and exact token mapping**

---

## 9. CodeInteX-Owned Component Architecture

### Ownership principle

The product-facing implementation boundary is the CodeInteX-owned component layer.

Conceptually:

~~~text
LMS screen
↓
CodeInteX domain/general UI component
↓
CodeInteX primitive composition
↓
Base UI primitive where useful
↓
React / browser
~~~

### shadcn-derived code

Components sourced or generated through shadcn/ui become CodeInteX-owned implementation code.

They may be:

- modified;
- simplified;
- extended;
- replaced;
- removed.

The project must not treat generated shadcn source as immutable vendor code.

### Base UI role

Base UI is the default behavioral primitive foundation where it provides an appropriate primitive.

It may provide lower-level behavior for concerns such as:

- dialogs;
- menus;
- popovers;
- select-like interactions;
- disclosure;
- other interactive primitives.

Exact primitive selection depends on the component requirement.

### Product-facing imports

Domain/product code should normally import CodeInteX-owned components.

Avoid widespread direct imports of Base UI primitives in learner-domain screens.

Preferred:

~~~text
Learner screen
→ CodeInteX Select
→ Base UI Select primitive
~~~

rather than:

~~~text
every learner screen
→ Base UI directly
~~~

### Why this boundary exists

This protects:

- replaceability;
- API consistency;
- styling consistency;
- accessibility review;
- agent comprehension;
- component governance.

### Component categories

The web implementation may distinguish conceptually among:

~~~text
behavioral primitives
general UI components
domain UI components
page/feature composition
~~~

These categories describe responsibilities.

They do not yet lock repository/package topology.

### General UI components

Examples may include:

- Button;
- Link treatment;
- Input;
- Select;
- Dialog;
- Tabs;
- Disclosure;
- Status;
- Progress representation.

Their semantics must remain aligned with PES Core.

### Domain UI components

Examples may include:

- ResumeLearningAction;
- CurriculumNavigator;
- LessonProgress;
- AssessmentStatus;
- SubmissionReceipt;
- FeedbackCriterion;
- CredentialStatus.

These encode LMS experience contracts rather than generic primitive behavior.

### Component API rule

Component APIs should express semantic intent.

Prefer:

~~~tsx
<SubmissionStatus state="underReview" />
~~~

over APIs that force every caller to reconstruct domain styling manually.

### Variant rule

Variants should correspond to meaningful component differences.

Do not create arbitrary variants merely to reproduce one page mockup.

### Composition over duplication

When an existing component contract can satisfy a requirement through composition, prefer composition over creating a near-duplicate component.

### Abstraction threshold

Do not prematurely create a reusable component for every fragment.

Create an abstraction when there is meaningful reuse, semantic ownership, behavioral complexity, accessibility risk, or maintenance value.

### Primitive escape hatch

Direct primitive use is permitted while implementing or extending the CodeInteX component layer.

If repeated direct primitive use appears in domain code, evaluate whether a missing CodeInteX component contract exists.

### Replacement

Replacing shadcn-derived source or Base UI primitives must not require changing authoritative LMS domain semantics.

Some component migration cost is acceptable.

Domain coupling to vendor-specific APIs should be minimized.

**Decision state: LOCKED component ownership and layering; OPEN physical package topology**


---

## 10. Responsive Implementation Contract

### Source requirement

Responsive implementation must satisfy the LMS Responsive Capability Contract.

Implementation mechanics are subordinate to learner outcome.

### CSS-first layout adaptation

Prefer CSS-native responsive behavior for layout and presentation when CSS can express the requirement correctly.

Relevant mechanisms may include:

- flexible layout;
- grid;
- wrapping;
- viewport media queries;
- container queries;
- intrinsic sizing;
- overflow management.

Do not introduce JavaScript viewport-state logic merely to reproduce behavior CSS already handles reliably.

### Viewport versus container queries

Viewport breakpoints are appropriate when behavior depends on overall available viewport space.

Container queries are appropriate when a reusable component should adapt to the space of its containing context.

Example:

~~~text
CourseProgress component
→ adapts to its available container width
→ does not assume page = mobile/tablet/desktop
~~~

This can improve component portability across:

- dashboard;
- course overview;
- side panel;
- full-width page.

### Breakpoint semantics

Breakpoint names are implementation mechanics.

Do not encode domain meaning such as:

~~~text
md = tablet
lg = desktop
~~~

into business or learner-state logic.

### Breakpoint selection

Choose breakpoint thresholds based on:

- content pressure;
- component behavior;
- readability;
- interaction usability;

rather than specific device brands or fashionable viewport sizes.

Exact breakpoint values remain OPEN.

### Mobile-first CSS

Tailwind's responsive system is mobile-first.

CodeInteX may use that implementation model where practical.

This does not mean:

~~~text
mobile UI is the canonical product
~~~

or:

~~~text
larger-screen behavior is only decoration
~~~

Every supported responsive condition must satisfy its required learner outcome.

### Container-query use

Container queries are encouraged when they improve reusable component autonomy.

Do not introduce them universally where ordinary layout composition is simpler.

### Reflow

Ordinary learner surfaces should avoid page-level horizontal scrolling under supported reflow conditions.

For genuinely two-dimensional content, localized overflow may be appropriate.

Examples include:

- code;
- wide tables;
- technical diagrams;
- data grids.

### Hidden content

Responsive hiding must distinguish:

~~~text
secondary presentation
~~~

from:

~~~text
required learner information
~~~

Do not use responsive utility classes to remove critical state or required actions without providing an accessible alternative.

### DOM and visual order

Visual reordering must not create a confusing semantic or keyboard order.

Prefer DOM order that remains meaningful across responsive states.

### State preservation

Responsive transformations must not reset authoritative or meaningful learner state.

Examples include:

- assessment answers;
- draft input;
- current lesson;
- media position;
- submission state.

### Client-side responsive state

Do not duplicate CSS responsive state into React state unless JavaScript behavior genuinely depends on it.

When client-side viewport information is necessary, implementation must account for:

- server rendering;
- hydration consistency;
- resize/change behavior;
- accessibility implications.

### Responsive component variants

A component may change composition materially across available space.

Those variants must preserve the same semantic contract unless the LMS Experience Profile explicitly permits a capability difference.

### Unsupported capability

A responsive limitation must use the LMS capability classification:

~~~text
FULL
ADAPTED
LIMITED
UNSUPPORTED-WITH-EXPLICIT-HANDOFF
~~~

It must not emerge accidentally from broken CSS.

**Decision state: LOCKED responsive implementation principles; OPEN exact breakpoint and container-query scheme**

---

## 11. Accessibility Implementation and Testing Contract

### Baseline

Implementation must satisfy:

~~~text
WCAG 2.2 AA
+
PES accessibility contracts
+
LMS Accessibility Validation Contract
~~~

Library accessibility support reduces implementation risk.

It does not transfer accessibility responsibility to the library.

### Semantic HTML first

Prefer native semantic HTML where it correctly represents the required interaction.

Examples include:

- button;
- link;
- input;
- label;
- heading;
- list;
- table;
- details where appropriate.

ARIA must supplement semantics when necessary.

It must not replace correct native semantics without reason.

### Primitive responsibility

Base UI may supply accessible interaction mechanics for appropriate complex primitives.

CodeInteX remains responsible for:

- correct primitive selection;
- accessible naming;
- content semantics;
- visual focus indication;
- contrast;
- composition;
- product workflow accessibility.

### Static analysis

The web project should use accessibility-related linting available through the approved Next.js ESLint configuration.

Static analysis may detect classes of errors such as:

- invalid ARIA usage;
- missing accessible attributes;
- some semantic mistakes.

Static analysis is not an accessibility conformance test.

### Automated runtime testing

Automated accessibility checking should be integrated at an appropriate testing layer.

Exact tooling remains OPEN.

Potential tooling may evaluate:

- DOM accessibility violations;
- accessible names;
- landmark/heading issues;
- color-independent machine-detectable rules.

Automated passing does not replace manual testing.

### Manual validation

Critical learner workflows require manual validation appropriate to the milestone.

Coverage includes, where applicable:

- keyboard-only operation;
- visible focus;
- focus sequence;
- screen-reader interpretation;
- zoom;
- reflow;
- form errors;
- status messages;
- responsive navigation;
- media interaction.

### Keyboard completeness

Every required interaction must be operable by keyboard when keyboard operation is applicable.

Custom interactions must not rely only on:

- pointer hover;
- drag;
- swipe;
- precision touch.

### Focus visibility

Interactive elements must have visible focus indication satisfying PES accessibility requirements.

Do not remove browser focus indication without providing an adequate replacement.

### Contrast

Semantic tokens and component styling must preserve required contrast.

A component-library default or approved theme token is not exempt from contrast validation.

### Forms

Form implementation must preserve programmatic relationships among:

- label;
- control;
- instruction;
- error;
- status.

Validation errors should identify:

- affected field;
- problem;
- recovery action where applicable.

### Dynamic UI

Dynamic content changes that materially affect learner understanding may require appropriate status communication.

Examples include:

- save failure;
- upload completion;
- submission receipt;
- review result availability.

### Disabled and unavailable state

Avoid using visual dimming alone to communicate unavailable interaction.

Where a learner needs to understand why an action is unavailable, expose meaningful explanation.

### Testing ownership

Accessibility tests belong alongside the implementation they protect.

Do not postpone all accessibility validation to a final audit phase.

### Release consequence

A critical workflow with severe unresolved accessibility failure is not implementation-complete even if its ordinary pointer-based happy path works.

**Decision state: LOCKED accessibility implementation contract; OPEN exact automated tooling and CI thresholds**

---

## 12. Interaction and Focus Management Contract

### Purpose

Interactive components must provide predictable behavior across:

- keyboard;
- pointer;
- touch;
- assistive technology.

### Primitive-first behavior

For complex interactive primitives, prefer established behavior from the approved primitive layer rather than rebuilding interaction mechanics casually.

Examples may include:

- dialog;
- menu;
- popover;
- select;
- disclosure;
- tabs.

### Override discipline

Do not override primitive keyboard or focus behavior merely to match visual preference.

Override only when:

- product behavior requires it;
- accessibility consequences are understood;
- behavior is tested.

### Dialog focus

Dialog-like experiences should establish deliberate:

- opening focus;
- focus containment where appropriate;
- closing behavior;
- focus return.

Base UI may provide default focus behavior and configuration mechanisms.

CodeInteX must still verify that behavior is correct for the product workflow.

### Initial focus

Initial focus should be chosen according to task semantics.

Do not automatically focus a destructive primary action merely because it is visually prominent.

### Focus return

When a temporary surface closes, focus should generally return to a meaningful originating context unless workflow semantics require another destination.

### Temporary responsive navigation

When persistent navigation becomes a temporary drawer/dialog-like surface:

- trigger state must be understandable;
- focus behavior must be predictable;
- keyboard escape/close behavior must work where appropriate;
- closing should return the learner to meaningful context.

### Menus and selection controls

Keyboard behavior should follow established interaction expectations for the selected primitive.

Do not invent application-specific arrow-key or escape semantics without strong reason.

### Route and major-context transitions

Client-side navigation can change major learner context without a traditional full-page load.

Implementation must verify that:

- page/context identity remains perceivable;
- focus does not become lost or stranded;
- important errors/status are discoverable;
- keyboard users can continue predictably.

Exact route-transition focus strategy remains PROVISIONAL and must be validated with the reference implementation.

### Focus versus scroll

Programmatic focus and scrolling should not be coupled blindly.

Moving focus solely to force a visual scroll position may create assistive-technology disruption.

Choose each deliberately.

### Error focus

After failed consequential actions, focus management should help the learner locate the error without destroying preserved input.

Possible strategies may include:

- focus error summary;
- focus first invalid field;
- preserve current focus with announced status.

The appropriate strategy depends on workflow.

### Asynchronous state

Do not move focus unexpectedly merely because asynchronous data updated.

For example:

~~~text
submission status changes
→ communicate state
≠
steal keyboard focus automatically
~~~

unless learner action requires it.

### Pointer and touch

Pointer/touch interaction must not introduce behavior unavailable to keyboard users when equivalent keyboard operation is required.

### Gesture support

Gestures may supplement interaction.

Required learner actions must not depend solely on gesture where an accessible alternative is feasible.

### Destructive and consequential actions

Interaction safeguards should be proportional to consequence.

Examples potentially requiring stronger confirmation include:

- final assessment submission;
- attempt consumption;
- destructive reset;
- irreversible learner action.

Routine reversible actions should not accumulate unnecessary confirmation dialogs.

### Focus styling ownership

Primitive libraries may manage focus movement.

CodeInteX styling owns visible focus presentation through the PES token/component system.

### Testing

Interaction components with nontrivial focus behavior should be tested at both:

- component level;
- representative workflow level.

A primitive working in isolation does not prove correct behavior when composed into an LMS workflow.

**Decision state: LOCKED interaction/focus principles; PROVISIONAL route-transition focus strategy**


---

## 13. Motion and Animation Dependency Policy

### Principle

Motion is an implementation capability.

It is not a visual-quality requirement by itself.

The web implementation should prefer the simplest mechanism that satisfies:

- interaction clarity;
- state transition;
- accessibility;
- maintainability;
- performance.

### CSS-first rule

Prefer native CSS transitions/animations when they adequately implement the required behavior.

Examples may include:

- opacity transition;
- simple color transition;
- simple transform;
- disclosure transition where appropriate;
- focus/hover state.

Do not introduce a JavaScript animation runtime for transitions that CSS can express cleanly.

### Motion library status

`Motion for React` is an approved PROVISIONAL candidate.

It is not a mandatory dependency for the baseline.

Activate it when a concrete interaction requires capabilities that are materially better served by Motion, such as:

- coordinated layout animation;
- gesture-driven interaction;
- complex shared transitions;
- animation orchestration;
- animation state requiring React integration.

### Dependency trigger

Before adding Motion, implementation should be able to identify:

~~~text
required experience behavior
→ limitation of simpler mechanism
→ capability Motion provides
~~~

Avoid:

~~~text
install animation library
→ search for places to animate
~~~

### Client-boundary consequence

Motion-based React components require client-side execution.

Animation requirements must not unnecessarily convert large server-rendered surfaces into Client Components.

Prefer isolating animation behavior to the smallest coherent interactive boundary.

### Reduced motion

If Motion is activated, implementation must respect user reduced-motion preferences.

A project-level policy should normally use the library's reduced-motion capabilities rather than requiring every individual component to rediscover preference handling.

Potential implementation may use:

~~~text
MotionConfig reducedMotion="user"
~~~

and component-specific reduced-motion behavior where required.

### Reduced-motion semantics

Reduced motion does not mean:

~~~text
remove every transition
~~~

The implementation should reduce or replace motion that may create discomfort while preserving necessary state/context communication.

### Motion meaning

Motion must not be the only method of communicating:

- state change;
- success;
- error;
- hierarchy;
- navigation destination.

### Autoplay and decorative motion

Avoid unnecessary:

- parallax;
- continuous decorative movement;
- autoplay animation;
- large transform animation;

particularly where it competes with learning content.

### Performance

Animation must not introduce material degradation to:

- input responsiveness;
- scrolling;
- lesson consumption;
- lower-capability devices.

### Governance

If Motion becomes widely used across CodeInteX, recurring patterns should be promoted into governed PES/component-level motion conventions rather than repeated as arbitrary local animation values.

### Decision

Current dependency state:

~~~text
Motion for React: PROVISIONAL / NOT REQUIRED BY DEFAULT
~~~

Activation requires a concrete capability need.

**Decision state: LOCKED dependency policy; PROVISIONAL Motion dependency**

---

## 14. Icon Implementation Policy

### Purpose

Icons support recognition and visual efficiency.

They do not replace semantic labels where a learner needs textual meaning.

### Current candidate

Lucide is the current PROVISIONAL default icon-library candidate.

Current properties supporting its candidacy include:

- SVG implementation;
- consistent icon system;
- customizable size/stroke;
- tree-shakable package usage.

### Why not LOCKED yet

The final CodeInteX visual language remains OPEN.

Iconography contributes materially to that language.

Therefore:

~~~text
approved candidate
≠
permanent architectural dependency
~~~

### Semantic rule

Icons should represent clear product meaning.

Do not select an icon only because it visually resembles a feature.

### Label rule

For consequential or ambiguous actions, prefer:

~~~text
icon + meaningful label
~~~

rather than icon-only interaction.

Examples include:

- Submit Project;
- Resume Learning;
- Review Feedback;
- Delete Attempt Draft.

### Icon-only controls

Icon-only controls may be appropriate where the meaning is conventional and space constraints justify them.

They still require an accessible name.

### Decorative icons

Purely decorative icons should not create redundant or misleading assistive-technology output.

Implementation is responsible for appropriate accessibility treatment.

### Meaningful icons

If an icon conveys information not otherwise expressed in text, that meaning must be available programmatically.

### Color

Icon meaning must not depend solely on color.

For example:

~~~text
green icon = complete
red icon = failed
~~~

requires an additional semantic indication.

### Size and touch target

Visual icon size and interactive target size are distinct concerns.

A 16px or 20px icon may sit inside a substantially larger accessible target.

Do not enlarge the SVG itself merely to satisfy target-size requirements when component padding is more appropriate.

### Styling ownership

Icon:

- color;
- size;
- stroke treatment;
- state styling;

should be governed through CodeInteX component/token conventions rather than arbitrary values scattered through feature code.

### Import discipline

If Lucide is selected, use import patterns that preserve efficient bundling.

Avoid unnecessarily importing the complete icon catalog into runtime code.

### Product-facing boundary

Domain screens may use an approved icon implementation directly for simple decorative cases.

For recurring semantic actions or statuses, prefer CodeInteX-owned components that govern icon + label + state behavior together.

### Custom icons

Custom CodeInteX icons may be introduced where the generic library cannot represent a required concept appropriately.

Do not distort the meaning of an existing icon simply to avoid creating an appropriate asset.

### Replacement

LMS domain semantics must not depend on Lucide icon names or library-specific APIs.

Replacing the icon library should not require rewriting learner-domain rules.

### Decision

Current dependency state:

~~~text
Lucide: PROVISIONAL DEFAULT CANDIDATE
~~~

Promotion to LOCKED should occur only after visual-language validation confirms fit.

**Decision state: LOCKED icon policy; PROVISIONAL Lucide dependency**

---

## 15. Storybook and Component Workbench Contract

### Decision

Storybook is the standard isolated component workbench for the current CodeInteX web implementation baseline.

Its purpose is to support:

- component development;
- state coverage;
- interaction validation;
- accessibility automation;
- responsive inspection;
- component documentation.

### Framework integration

For a standard Next.js App Router project without an incompatible custom Webpack/Babel requirement, use:

~~~text
@storybook/nextjs-vite
~~~

Current Storybook guidance recommends the Vite-based Next.js integration for most new projects.

If future repository constraints make that integration unsuitable, changing the Storybook framework adapter does not require revising PES or LMS semantics.

### Runtime boundary

Storybook is a development/testing dependency.

It is not a learner-facing production runtime dependency.

### Story source-of-truth rule

A Storybook story is:

~~~text
executable example / validation fixture
~~~

It is not the highest-authority component specification.

Authority remains:

~~~text
PES contracts
→ Product Experience Profile
→ Web Implementation Profile
→ component contract
→ story
~~~

### Story coverage

Governed reusable components should have stories covering meaningful states.

Examples may include:

~~~text
default
hover/focus where useful
disabled/unavailable
loading
error
empty
long content
responsive constraint
high-risk accessibility state
~~~

State coverage should be based on component semantics.

Do not generate meaningless story permutations merely to increase story count.

### Domain component stories

Important learner-domain components should cover relevant domain states.

Examples:

~~~text
SubmissionStatus
├── submitting
├── submitted
├── underReview
├── changesRequired
└── submissionFailed
~~~

when those states belong to the component contract.

### Interaction tests

Stories may include interaction tests for behavior such as:

- opening/closing disclosure;
- keyboard navigation;
- focus return;
- validation;
- selection;
- state transitions.

Component-level tests do not replace workflow-level integration or end-to-end testing.

### Accessibility addon

Use Storybook accessibility tooling as an automated first-line check for reusable components.

The accessibility test configuration should align with the CodeInteX WCAG 2.2 AA baseline where supported by the underlying tooling.

### Automated-testing limitation

Automated accessibility checks detect only a subset of accessibility problems.

Storybook accessibility success does not establish WCAG conformance.

Manual workflow validation remains mandatory under the LMS Accessibility Validation Contract.

### CI behavior

Accessibility/component tests should be eligible to run in CI.

For governed components, known newly introduced automated accessibility violations should normally fail validation rather than remain silently ignored.

Exact CI rollout and legacy-baseline policy remain PROVISIONAL until the repository/testing environment exists.

### Exceptions

Disabling accessibility checks for a story requires explicit justification.

Stories intentionally demonstrating an inaccessible antipattern must be clearly identified and must not be mistaken for approved component behavior.

### Responsive inspection

Storybook should include representative constrained-width states for reusable components whose composition changes with available space.

This helps validate:

- container responsiveness;
- content expansion;
- long labels;
- responsive composition.

It does not replace browser/device workflow testing.

### Theme inspection

When multiple PES-approved themes exist, reusable components should be inspectable under relevant theme conditions.

Theme stories must not fork component semantics.

### Component documentation

Storybook may expose useful implementation documentation such as:

- props;
- variants;
- state examples;
- usage constraints.

Normative semantic decisions should continue to reference canonical PES documentation rather than existing only inside Storybook.

### Visual regression

Visual regression testing may later be integrated with Storybook.

Exact tooling/provider remains OPEN.

Do not introduce a hosted visual-testing vendor before a demonstrated need justifies:

- cost;
- vendor dependency;
- workflow complexity.

### Story ownership

A reusable component change should update affected stories/tests when its meaningful contract changes.

Stale stories are implementation debt and must not be treated as trustworthy documentation.

### Decision

Current dependency state:

~~~text
Storybook: LOCKED DEVELOPMENT / TESTING CAPABILITY
Default Next.js adapter: @storybook/nextjs-vite
Exact supported package patch: operational dependency management
~~~

**Decision state: LOCKED workbench capability; OPEN visual-regression provider and CI rollout details**


---

## 16. Testing Strategy Contract

### Principle

Testing must protect authoritative contracts at the cheapest layer that can validate them reliably.

The testing architecture should not depend on one universal test type.

Use complementary layers for different failure classes.

### Required conceptual layers

The baseline distinguishes:

~~~text
static analysis
unit / domain logic tests
component / interaction tests
browser integration / E2E tests
automated accessibility checks
manual accessibility validation
~~~

Not every requirement belongs in every layer.

### Static analysis

Static validation should include, where applicable:

- TypeScript;
- linting;
- Next.js framework lint rules;
- accessibility-related lint rules;
- build-time framework checks.

Static analysis should fail on genuine contract violations rather than accumulating ignored errors indefinitely.

### Pure domain and adapter logic

Pure functions such as:

- domain-state mappings;
- view-model transformations;
- progress representation logic;
- validation helpers;
- deterministic formatting rules;

should be tested without requiring a browser where practical.

### Unit-test runner

No single unit-test runner is LOCKED yet.

Vitest or another compatible runner may be selected when repository topology and test infrastructure are established.

The testing contract is more stable than the runner choice.

### Component tests

Storybook is the primary isolated workbench for CodeInteX-owned components.

Component-level tests should cover meaningful behavior such as:

- interaction;
- variants;
- state rendering;
- accessible names;
- focus-sensitive behavior;
- error states.

### E2E baseline

Playwright is the standard browser E2E framework for the current web baseline.

Primary reasons:

- official Next.js integration guidance;
- Chromium support;
- Firefox support;
- WebKit support;
- mobile/device emulation;
- user-oriented locators;
- CI support.

### E2E scope

E2E tests should protect critical learner workflows rather than every implementation detail.

Priority workflows include:

- learner entry/dashboard;
- resume learning;
- curriculum navigation;
- lesson progression;
- assessment submission;
- project submission;
- feedback/revision;
- completion state;
- important failure/recovery paths.

### Production-like execution

Critical E2E validation should run against a production build when practical.

Conceptually:

~~~text
next build
→
production-like app server
→
Playwright
~~~

This catches failure modes that development-mode behavior may hide.

### Locator policy

Prefer locators based on user-perceivable semantics such as:

- role;
- accessible name;
- label;
- visible text where appropriate.

Avoid brittle selectors based primarily on:

- generated classes;
- DOM depth;
- implementation-specific CSS structure.

`data-testid` remains an escape hatch where no stable semantic locator exists.

### Cross-browser policy

Critical learner flows should have browser coverage sufficient to protect the supported browser baseline.

This does not imply every test must run across every browser on every local execution.

CI coverage may use an appropriate matrix.

Exact matrix remains PROVISIONAL until execution cost is measured.

### Automated accessibility in E2E

Use `@axe-core/playwright` for automated accessibility checks on representative workflow states.

This may complement Storybook accessibility checks by validating composed pages and workflow states.

### Accessibility limitation

Automated accessibility tests do not establish WCAG conformance.

Manual validation remains required under the LMS Accessibility Validation Contract.

### Failure-state testing

Tests must not cover only happy paths.

High-value failure scenarios include:

- save failure;
- submission failure;
- stale/invalid resume target;
- network/API error;
- unavailable content;
- evaluation/result retrieval failure.

### Authoritative state testing

Critical tests should verify that UI success states correspond to authoritative backend/API responses.

Avoid tests that merely confirm a local loading flag changed.

### Test ownership

Tests should live close enough to the implementation or workflow they protect that contract changes make required test updates apparent.

### Flakiness discipline

Flaky tests must not become accepted background noise.

Retries may help diagnose environmental instability.

Retries must not become a permanent mechanism for hiding deterministic defects.

### Decision

Current baseline:

~~~text
Storybook = LOCKED component workbench
Playwright = LOCKED browser E2E baseline
@axe-core/playwright = LOCKED automated E2E accessibility capability
Unit runner = OPEN / to be selected
~~~

**Decision state: LOCKED testing architecture and E2E tooling; OPEN unit runner and exact CI matrix**

---

## 17. Performance and Bundle Discipline

### Principle

Performance is part of learner usability.

The implementation should optimize real learner experience rather than framework benchmark scores in isolation.

### Server-first advantage

The Server Component default should be used to avoid unnecessary client JavaScript.

A dependency or component should not move into the browser bundle simply because client rendering is convenient.

### Client-bundle discipline

New client-side dependencies should be evaluated for:

- functionality gained;
- JavaScript cost;
- hydration cost;
- maintenance burden;
- overlap with existing dependencies.

### Dependency introduction

A significant client dependency should answer:

~~~text
What capability gap does this solve?
Can platform / CSS / existing dependency solve it?
What runtime cost does it introduce?
~~~

### Bundle analysis

Bundle analysis should be available as a diagnostic capability.

The Next.js bundle analyzer or an equivalent maintained mechanism may be used to identify:

- unexpectedly large dependencies;
- duplicate packages;
- oversized client chunks;
- regressions after dependency changes.

Bundle analysis need not run on every local edit.

It should be available for:

- performance investigation;
- major dependency introduction;
- release validation where appropriate.

### Performance budgets

Exact JavaScript, asset, or Core Web Vitals budgets are PROVISIONAL until the reference implementation provides a measured baseline.

Do not invent arbitrary budgets without representative data.

### Core Web Vitals

Production performance should eventually collect relevant field measurements rather than relying solely on laboratory simulation.

Laboratory tools such as Lighthouse are useful diagnostic instruments.

They are not the sole product-performance authority.

### Images

Use Next.js image optimization capabilities where they provide appropriate benefit.

Image implementation should avoid unnecessary:

- oversized transfers;
- layout shift;
- eager loading of offscreen content.

Image semantics and alternative text remain accessibility/content concerns, not performance concerns alone.

### Fonts

Prefer an implementation that minimizes:

- unnecessary external requests;
- layout shift;
- excessive font variants;
- excessive font payload.

`next/font` is the baseline-compatible mechanism where appropriate.

Final typography remains governed by PES visual-language decisions.

### Third-party scripts

Third-party browser scripts should be minimized.

Every third-party script adds potential:

- performance cost;
- privacy exposure;
- security risk;
- operational dependency.

Where third-party scripts are required, use an appropriate loading strategy and measure their impact.

### Streaming and loading states

Streaming may improve perceived responsiveness when it preserves correct learner semantics.

Do not fragment learner state merely to demonstrate streaming behavior.

Loading UI must distinguish:

~~~text
content pending
~~~

from authoritative product states.

### Caching

Caching should improve performance only within correctness constraints.

Learner-sensitive mutable state must not become stale enough to violate domain truthfulness.

### Prefetching

Framework prefetching may improve navigation.

It must be evaluated when:

- data is expensive;
- learner-specific;
- security-sensitive;
- network-constrained.

Do not assume more prefetching is universally better.

### Responsive performance

Mobile/responsive validation should account for:

- lower-powered devices;
- constrained networks;
- touch responsiveness;
- client bundle size.

### Performance regression

Material regressions should be investigated against learner impact rather than normalized as inevitable application growth.

**Decision state: LOCKED performance discipline; PROVISIONAL quantitative budgets**

---

## 18. Web Security Boundary

### Principle

Framework convenience must not weaken authoritative security boundaries.

The web application must treat:

~~~text
client input
route parameters
Server Action arguments
external/backend payloads
~~~

as untrusted at the appropriate boundary.

### Data-access boundary

Server-side sensitive data access should be isolated behind a deliberate data-access or service boundary.

Avoid importing:

- database clients;
- privileged backend SDKs;
- secret-bearing modules;

through arbitrary UI modules.

### Client exposure

Data passed into Client Components must be reviewed as data that can reach the browser.

Do not pass broad server/domain objects into client components merely because only one field is currently displayed.

Prefer minimal client-safe data contracts.

### Environment variables

Secret environment variables must remain server-side.

Only values intentionally safe for browser exposure may enter the public client environment.

A `NEXT_PUBLIC_`-style public variable must be considered public information.

### Authorization

Authentication and authorization are distinct.

Every consequential server-side mutation must perform appropriate authorization at the authoritative server boundary.

Do not assume that:

~~~text
button hidden in UI
=
action unauthorized
~~~

Client presentation is not an authorization control.

### Server Actions / Server Functions

If Server Actions or Server Functions are used:

- validate input;
- authenticate where required;
- authorize the operation;
- avoid trusting hidden form values as authority;
- avoid exposing sensitive closed-over data.

Framework encryption is not a substitute for proper data minimization and authorization.

### Route parameters

Dynamic route parameters are user-controlled input.

Validate them before using them in sensitive domain operations.

### Error boundary

Learner-facing errors must not expose:

- stack traces;
- database detail;
- secret values;
- internal authorization structure;
- sensitive infrastructure identifiers.

Operational diagnostics should go to controlled observability systems.

### Content Security Policy

Production deployment should implement an appropriate Content Security Policy.

Exact CSP mechanics remain OPEN because implementation depends on:

- rendering strategy;
- third-party scripts;
- hosting;
- caching requirements.

### Strict CSP trade-off

Nonce-based strict CSP can affect rendering architecture because request-specific nonces may require dynamic rendering.

Therefore:

~~~text
security requirement
≠
blindly force nonce CSP everywhere
~~~

Select the CSP strategy together with rendering/deployment architecture.

### Experimental security features

Do not make a core security architecture depend solely on experimental framework features.

Experimental features may supplement stable controls after explicit evaluation.

### Security headers

Production configuration should evaluate appropriate headers such as:

- Content-Security-Policy;
- Strict-Transport-Security where deployment conditions support it;
- X-Content-Type-Options;
- Referrer-Policy;
- Permissions-Policy;
- frame embedding policy.

Exact values depend on application and deployment requirements.

### Upload/content safety

If learner-controlled uploads or rich content enter scope, security design must explicitly address:

- content type;
- size;
- storage;
- authorization;
- serving behavior;
- malicious content risk.

Do not treat file-extension validation in the browser as sufficient security.

### Third-party dependency security

Third-party dependencies are part of the application attack surface.

Dependency governance must include security advisories and supported-version status.

### AI coding-agent rule

AI agents must not resolve security uncertainty by:

- disabling validation;
- broadening CSP indiscriminately;
- exposing secret values;
- bypassing authorization;
- inserting unsafe casts to defeat boundary checks.

Unresolved security constraints must be escalated.

**Decision state: LOCKED security boundaries; OPEN CSP details and deployment-specific headers**

---

## 19. Dependency and Version Governance

### Principle

Dependency versions are operational state.

Architecture should lock:

~~~text
supported family
role
compatibility expectation
upgrade discipline
~~~

without pretending one patch release remains correct forever.

### Framework support line

The application must remain on a supported Next.js release line.

Current baseline at this document date:

~~~text
Next.js 16.x = Active LTS
~~~

Security and critical correctness updates within the supported line must not be ignored solely to preserve an old patch number.

### Patch discipline

When an upstream security advisory identifies a safe version:

- assess applicability promptly;
- update within the supported line;
- execute relevant validation;
- record exceptional deferral when necessary.

### React compatibility

React version must remain compatible with the selected supported Next.js release.

Do not upgrade React independently merely for novelty when the framework compatibility contract does not support it.

### Exact version reproducibility

Repository dependency resolution must be reproducible.

The project should commit and maintain one authoritative package-manager lockfile for a given application/workspace.

Do not mix competing lockfiles casually.

### Package manager

Exact package-manager selection remains OPEN until repository topology is established.

Whichever package manager is selected should be standardized for the repository.

### Runtime version

The Node.js runtime must satisfy the current supported requirements of the selected Next.js release and deployment environment.

Runtime version should be declared reproducibly in repository/deployment configuration once topology is established.

### Dependency classification

Dependencies should be classified conceptually as:

~~~text
production runtime
development/testing
build/tooling
optional/capability-triggered
~~~

Do not ship development-only tooling into learner-facing runtime unnecessarily.

### New dependency acceptance

Before introducing a material dependency, evaluate:

- capability gap;
- existing overlap;
- maintenance activity;
- compatibility;
- security history/current advisories;
- bundle/runtime cost where applicable;
- license suitability;
- replacement cost.

### Overlap rule

Avoid parallel libraries that solve substantially the same problem without a documented reason.

Examples include unnecessary duplication of:

- primitive systems;
- form libraries;
- animation runtimes;
- icon systems;
- date libraries;
- validation systems.

### Transitive dependency awareness

A small direct dependency can introduce substantial transitive dependency surface.

Dependency review should consider more than direct package count.

### Automated updates

Automated dependency-update tooling may be adopted.

Exact service/tool remains OPEN.

Automation must not auto-merge high-impact framework/runtime upgrades without appropriate validation.

### Major upgrades

Major framework/library upgrades require evaluation of:

- breaking changes;
- PES/LMS contract impact;
- runtime behavior;
- accessibility;
- browser support;
- security;
- migration cost.

Do not upgrade major versions solely because they are new.

### Deprecation

A dependency should be considered for replacement when:

- unsupported;
- security-risky;
- incompatible with architecture;
- no longer maintained;
- substantially redundant;
- causing disproportionate migration/performance burden.

### Lock versus vendor lock-in

Using a library is not itself unacceptable vendor lock-in.

The goal is proportional replaceability:

~~~text
library-specific implementation may change
while
PES + LMS semantics remain stable
~~~

### Current dependency status

~~~text
Next.js 16.x supported line: LOCKED
React compatible 19.x line: LOCKED THROUGH FRAMEWORK COMPATIBILITY
TypeScript: LOCKED
Tailwind CSS 4.x: LOCKED
Base UI: LOCKED DEFAULT PRIMITIVE FOUNDATION
shadcn-derived source: APPROVED / CODE-OWNED
Storybook: LOCKED DEVELOPMENT/TESTING
Playwright: LOCKED E2E
@axe-core/playwright: LOCKED AUTOMATED E2E A11Y CAPABILITY
Motion: PROVISIONAL / CAPABILITY-TRIGGERED
Lucide: PROVISIONAL DEFAULT CANDIDATE
Unit-test runner: OPEN
Package manager: OPEN
Repository/package topology: OPEN
~~~

**Decision state: LOCKED dependency governance; individual dependency states as listed above**


---

## 20. Observability and Error Reporting Contract

### Principle

Learner-facing error handling and operational observability are related but distinct concerns.

The learner experience should answer:

~~~text
What happened?
What was preserved?
What can I do next?
~~~

Operational observability should help engineering answer:

~~~text
What failed?
Where?
For which operation?
How often?
Under what system conditions?
~~~

Neither should substitute for the other.

### Error boundaries

Next.js route-segment error boundaries should be used where they provide meaningful recovery isolation.

An unexpected error should not automatically destroy the entire learner application context when a narrower recovery boundary is appropriate.

### Error UI

Unexpected-error UI should provide:

- understandable failure language;
- meaningful retry/recovery action where possible;
- navigation escape where retry is insufficient.

It must not expose:

- stack traces;
- internal exception detail;
- secrets;
- raw infrastructure identifiers.

### Expected versus unexpected failures

Expected domain failures should normally use structured domain state rather than generic exception handling.

Examples include:

- assessment validation failure;
- unavailable attempt;
- access restriction;
- known submission rejection;
- unsupported workflow capability.

Unexpected application failures may be handled through error boundaries and operational reporting.

### `not-found` semantics

Missing resources should be distinguished from unexpected application failures when the domain can determine that a resource does not exist or is unavailable by design.

Do not use a generic server error for every absence condition.

### Retry behavior

A UI retry mechanism must respect operation semantics.

For read/render failures, re-render/retry may be sufficient.

For consequential mutations, retry safety must also consider:

- duplicate submission;
- duplicate payment-like action if such workflows later exist;
- attempt consumption;
- idempotency;
- authoritative mutation result.

### Operational correlation

Material server operations should be observable with enough correlation to trace a request or workflow across relevant services where practical.

Potential signals include:

- trace/request correlation identifier;
- route or operation name;
- service boundary;
- failure class;
- duration.

Do not place learner-sensitive data into telemetry merely because correlation is useful.

### OpenTelemetry direction

Prefer observability instrumentation that can remain vendor-neutral.

OpenTelemetry is the preferred interoperability direction for server-side:

- traces;
- metrics;
- distributed context;

where deployment/runtime support makes it appropriate.

### Important browser boundary

OpenTelemetry browser/client instrumentation is not LOCKED as the CodeInteX browser observability solution.

Current browser instrumentation maturity and product requirements do not justify that decision.

Browser-side:

- error reporting;
- Real User Monitoring;
- session diagnostics;

remain provider/tool OPEN.

### Provider neutrality

The application architecture should avoid spreading vendor-specific observability APIs through learner-domain components.

Prefer an owned observability boundary or adapter when a provider is selected.

Conceptually:

~~~text
application / server operation
↓
CodeInteX observability boundary
↓
OpenTelemetry or provider adapter
↓
observability backend
~~~

### Logging

Logs should be:

- structured where useful;
- actionable;
- environment-appropriate;
- privacy-aware.

Avoid uncontrolled application-wide `console.log` output in production paths.

### Sensitive information

Telemetry must not unnecessarily contain:

- passwords;
- authentication tokens;
- secret keys;
- private assessment responses;
- full learner submissions;
- sensitive personal data;
- raw authorization objects.

Data minimization applies to observability.

### Error identifiers

Learner-facing failures may expose a safe support/reference identifier when it materially improves support and diagnosis.

Such identifiers must not reveal sensitive infrastructure or authorization information.

### Metrics

Operational metrics may include:

- request/error rates;
- latency;
- submission-processing failures;
- dependency failures;
- availability.

Learner/product analytics are a separate concern and must not be conflated automatically with technical observability.

### Product analytics boundary

Analytics about:

- learner behavior;
- engagement;
- progression;
- educational outcomes;

requires separate product/privacy governance.

An observability platform must not silently become the learner analytics architecture.

### Web Vitals

Relevant production performance metrics may be collected through a controlled reporting boundary.

Provider choice remains OPEN.

### Alerting

Alerting should focus on actionable operational conditions.

Do not create alerts for every logged exception without considering:

- severity;
- frequency;
- learner impact;
- recoverability.

Exact alert thresholds remain OPEN until production baselines exist.

### Development telemetry

Framework-provided anonymous development telemetry is distinct from CodeInteX production observability.

Its enable/disable policy may be decided by repository/team policy.

It must not be mistaken for application monitoring.

### Current decision

~~~text
Vendor-neutral observability architecture: LOCKED
OpenTelemetry-compatible server direction: LOCKED
Specific observability backend/provider: OPEN
Browser RUM provider: OPEN
Error-reporting provider: OPEN
Product analytics platform: OUTSIDE THIS DECISION
~~~

**Decision state: LOCKED observability boundary; OPEN providers and exact telemetry stack**

---

## 21. Implementation Acceptance and Release Gate

### Purpose

Implementation completion requires more than:

~~~text
page renders
+
developer says it works
~~~

A learner-facing capability should satisfy relevant architecture, experience, accessibility, security, and testing contracts.

### Layered acceptance

A feature should be evaluated against applicable layers:

~~~text
PES Core
↓
LMS Experience Profile
↓
Web Implementation Profile
↓
domain/API contract
↓
implementation
↓
validation
~~~

### Required checks

Depending on feature scope, implementation acceptance may require:

- TypeScript/build validation;
- lint/static analysis;
- domain/adapter tests;
- component tests;
- Storybook state coverage;
- automated accessibility checks;
- Playwright workflow tests;
- manual accessibility validation;
- responsive validation;
- security review for sensitive behavior;
- performance/bundle review for material changes.

Not every small change requires every validation layer.

Risk and contract impact determine required coverage.

### Critical learner workflows

Changes affecting critical learner workflows require stronger validation.

These include:

- dashboard/resume;
- curriculum/lesson;
- assessment;
- project submission;
- feedback/revision;
- completion/credential;
- authentication/access boundaries where relevant.

### Authoritative-state gate

A feature must not be considered complete if it visually works but misrepresents authoritative state.

Examples:

~~~text
UI says Submitted
backend did not confirm submission
~~~

or:

~~~text
UI says Completed
completion policy has not been satisfied
~~~

These are correctness defects.

### Accessibility gate

A critical workflow with known severe accessibility failure is not release-ready solely because the pointer-based happy path works.

Automated accessibility success is insufficient on its own.

### Responsive gate

Critical workflows must satisfy their intended capability classification:

~~~text
FULL
ADAPTED
LIMITED
UNSUPPORTED-WITH-EXPLICIT-HANDOFF
~~~

A broken narrow layout is not equivalent to an intentionally `LIMITED` workflow.

### Error/recovery gate

Material failure states should be validated, not assumed.

Examples include:

- API unavailable;
- mutation rejected;
- submission timeout/failure;
- stale learner state;
- unavailable content;
- unauthorized operation.

### Security gate

High-risk changes should validate:

- server authorization;
- input validation;
- secret exposure;
- client data minimization;
- upload/content risk where relevant.

### Performance gate

Material client-bundle or runtime regressions should be investigated before acceptance.

Exact quantitative performance budgets remain PROVISIONAL until reference implementation baselines exist.

### Dependency gate

Introduction of a material dependency requires the Dependency and Version Governance review.

A dependency must not be accepted merely because it reduces implementation code locally.

### Visual review

Visual review is required where presentation changes.

Visual approval cannot override:

- semantic correctness;
- accessibility;
- responsive behavior;
- domain truthfulness.

### Acceptance evidence

Acceptance should leave inspectable repository evidence where appropriate:

- tests;
- stories;
- implementation code;
- review notes;
- decision references.

### Temporary exceptions

A temporary exception may be allowed only when:

- impact is understood;
- owner is clear;
- follow-up is explicit;
- exception does not silently become architecture.

Exact issue-tracking mechanism depends on repository/workflow tooling.

### Release confidence

The goal is not maximum test count.

The goal is sufficient evidence that a change preserves the contracts it can materially affect.

**Decision state: LOCKED acceptance model; PROVISIONAL quantitative thresholds and CI enforcement levels**

---

## 22. AI Coding-Agent Execution Contract

### Principle

AI coding agents may accelerate implementation.

They do not receive authority to redefine architecture or unresolved product policy.

### Mandatory context

Before making material learner-facing changes, an agent should have access to the relevant normative artifacts:

~~~text
PES Foundation Decision Model
PES Consumption Contract
LMS Experience Profile
Web Implementation Profile
relevant backend/API contract
~~~

### Authority order

An agent must interpret authority in this order:

~~~text
LOCKED normative contract
↓
PROVISIONAL project decision
↓
existing implementation
↓
library default
↓
agent preference
~~~

Existing code is not automatically authoritative.

### No silent policy creation

Agents must not invent unresolved policy for:

- grading;
- attempts;
- deadlines;
- completion;
- credentials;
- mastery;
- access;
- recommendation ranking;
- AI evaluation authority.

When required policy is missing, preserve the uncertainty explicitly.

### No silent architecture creation

Agents must not independently introduce:

- new framework;
- new primitive system;
- second styling architecture;
- alternate token system;
- new state-management framework;
- new API client architecture;
- additional testing framework;

without a demonstrated gap and dependency-governance review.

### Server/client discipline

Agents should not solve interaction issues by broadly adding:

~~~text
'use client'
~~~

to higher application layers.

They should identify the smallest coherent client boundary consistent with the execution contract.

### Data-boundary discipline

Agents must not bind learner components directly to raw Wagtail/CMS/database structures when an adapter/domain boundary is required.

### Type discipline

Agents must not routinely resolve TypeScript contract failures through:

- `any`;
- unchecked assertions;
- broad casts;
- disabling strictness.

A type mismatch at a domain boundary may indicate an architectural mismatch requiring correction.

### Token discipline

Agents should use existing PES-derived semantic tokens.

They must not introduce arbitrary raw visual constants as a substitute for missing semantic design decisions.

### Component discipline

Agents should first evaluate whether the requirement belongs to:

- existing component;
- composition of existing components;
- extension of a component contract;
- new component.

Do not create near-duplicate components merely because generating new code is easy.

### Primitive discipline

Agents should prefer approved CodeInteX-owned components in product screens.

Direct Base UI usage belongs primarily in the component implementation layer.

### Dependency discipline

Before proposing a new dependency, an agent should identify:

~~~text
capability gap
existing alternatives
runtime/build impact
maintenance impact
replacement cost
~~~

### Security discipline

Agents must never solve implementation friction by weakening:

- authorization;
- input validation;
- CSP/security controls;
- secret boundaries;
- data minimization.

### Accessibility discipline

Agents must not remove:

- labels;
- focus indicators;
- semantic HTML;
- keyboard behavior;
- status semantics;

to simplify styling or tests.

### Test discipline

Agents should update relevant tests/stories when behavior or component contracts change.

They must not:

- delete failing tests without understanding them;
- disable accessibility checks casually;
- increase retries to conceal deterministic E2E defects.

### Provisional implementation markers

When blocked by an unresolved upstream decision, use project markers where appropriate:

~~~text
PES-DEPENDENCY
PROVISIONAL-UI
OPEN-PES-DECISION
OPEN-LMS-POLICY
OPEN-WEB-IMPLEMENTATION
~~~

The exact code-comment convention may be standardized later.

### Repository discipline

Agents must respect repository-local instructions and dependency management once repository topology is established.

They must not initialize new repositories, package managers, or parallel project trees merely for convenience.

### Verification

Agent-generated code is subject to the same implementation acceptance gate as human-authored code.

Generated code is not accepted merely because it compiles.

### Decision escalation

When a requirement conflicts with a LOCKED contract, the agent should surface the conflict rather than silently implementing a workaround.

### Auditability

Material agent-generated changes should remain inspectable through normal engineering artifacts:

- diffs;
- tests;
- stories;
- commit/review history where available;
- decision references.

**Decision state: LOCKED AI-agent execution contract**


---

## 23. Implementation Decision Register

This section summarizes the major implementation decisions established by this profile.

### LOCKED

The following are LOCKED for the current web baseline:

1. Next.js 16.x supported line is the web framework baseline.
2. App Router is the routing/execution model.
3. React version follows supported Next.js compatibility.
4. TypeScript is required.
5. Server Components are the default execution boundary.
6. Client Components are introduced only where client execution is required.
7. Learner-domain semantics must remain behind explicit domain/API and adapter boundaries.
8. Raw Wagtail/CMS structure must not become the learner UI contract.
9. PES semantic tokens are authoritative over Tailwind/library styling defaults.
10. Tailwind CSS 4.x is the primary styling implementation engine.
11. Tailwind is not the design-system authority.
12. Base UI is the default behavioral primitive foundation where appropriate.
13. shadcn-derived source becomes CodeInteX-owned implementation code.
14. Product/domain screens should normally consume CodeInteX-owned components.
15. Responsive behavior must satisfy LMS capability contracts rather than device-name assumptions.
16. Accessibility implementation must satisfy WCAG 2.2 AA, PES, and LMS contracts.
17. Complex interaction behavior should prefer approved behavioral primitives rather than ad hoc recreation.
18. Storybook is the standard isolated component workbench.
19. Playwright is the standard browser E2E baseline.
20. `@axe-core/playwright` is the standard automated E2E accessibility capability.
21. Critical learner workflows require testing beyond isolated components.
22. Performance discipline includes client-bundle restraint and measurable learner impact.
23. Security authority remains server-side for consequential operations.
24. Client UI visibility is not an authorization mechanism.
25. Dependency versions follow supported release lines and security-patch discipline.
26. Observability architecture should remain provider-neutral-capable.
27. OpenTelemetry-compatible server instrumentation is the preferred interoperability direction.
28. Implementation acceptance requires evidence appropriate to contract/risk impact.
29. AI coding agents must follow the same normative and acceptance contracts as human implementation.
30. Missing authoritative domain semantics must be escalated rather than fabricated in UI code.

### PROVISIONAL

The following remain PROVISIONAL:

- route-specific rendering strategy;
- route-specific caching strategy;
- responsive breakpoint scheme;
- container-query adoption patterns;
- route-transition focus strategy;
- quantitative performance budgets;
- quantitative UX thresholds;
- exact CI execution matrix;
- Storybook accessibility CI rollout details;
- Motion adoption;
- Lucide adoption;
- exact learner-facing web state vocabulary where upstream domain vocabulary remains provisional.

### OPEN

The following remain explicitly OPEN:

- repository topology;
- package topology;
- monorepo versus alternative structure;
- package manager;
- unit-test runner;
- runtime-validation library;
- API type-generation strategy;
- canonical token serialization pipeline;
- exact breakpoint values;
- exact cache policy;
- exact CSP implementation;
- deployment/provider-specific security headers;
- visual regression provider;
- observability backend/provider;
- browser RUM provider;
- error-reporting provider;
- production product-analytics platform;
- exact performance budgets;
- automated dependency-update service;
- hosting/deployment provider.

### Dependency status

~~~text
Next.js 16.x: LOCKED
React compatible 19.x line: LOCKED THROUGH FRAMEWORK COMPATIBILITY
TypeScript: LOCKED
Tailwind CSS 4.x: LOCKED
Base UI: LOCKED DEFAULT PRIMITIVE FOUNDATION
shadcn-derived source: APPROVED / CODE-OWNED
Storybook: LOCKED
Playwright: LOCKED
@axe-core/playwright: LOCKED
Motion: PROVISIONAL / CAPABILITY-TRIGGERED
Lucide: PROVISIONAL DEFAULT CANDIDATE
Unit-test runner: OPEN
Package manager: OPEN
Repository/package topology: OPEN
~~~

### Interpretation

A LOCKED implementation decision may still evolve through formal review if stronger evidence appears.

`LOCKED` means:

~~~text
current authorized baseline
~~~

not:

~~~text
irreversible forever
~~~

An OPEN item must not be silently resolved merely through incidental implementation.

**Decision state: LOCKED register**

---

## 24. Open Items and Activation Triggers

OPEN and PROVISIONAL decisions should be resolved when concrete requirements justify them.

### Repository and package topology

Current state:

`OPEN`

Resolve before repository structure materially depends on:

- shared packages;
- multiple deployable applications;
- independent versioning;
- workspace-level tooling;
- reusable PES/component packages.

Do not create package boundaries merely to make architecture diagrams appear cleaner.

---

### Package manager

Current state:

`OPEN`

Resolve together with repository topology.

Selection should evaluate:

- workspace support;
- lockfile reproducibility;
- CI/deployment compatibility;
- developer tooling;
- dependency-management behavior.

Once selected for a repository, standardize it.

---

### Unit-test runner

Current state:

`OPEN`

Activate selection when pure domain/adapter/component logic requires a repository-level test runner.

Selection should consider:

- Next.js/React compatibility;
- TypeScript support;
- execution speed;
- ecosystem stability;
- duplication with existing tooling.

Do not add multiple unit-test runners without a concrete reason.

---

### Runtime validation

Current state:

`OPEN`

Activate a validation library when system boundaries require runtime verification beyond TypeScript static typing.

Potential triggers include:

- external API payloads;
- versioned backend contracts;
- untrusted structured input;
- webhook/external integration payloads.

Do not introduce schema tooling only for internal objects already guaranteed by a trusted typed boundary.

---

### Token serialization pipeline

Current state:

`OPEN`

Resolve when PES semantic tokens need to be emitted into implementation artifacts.

Required outcome:

~~~text
canonical PES semantics
→ reproducible generated/maintained web representation
→ Tailwind/component consumption
~~~

Avoid manually maintaining multiple independent copies of the same token values.

---

### Motion

Current state:

`PROVISIONAL / NOT REQUIRED BY DEFAULT`

Activate Motion only when a real interaction cannot be implemented sufficiently through simpler CSS/platform behavior.

Activation requires a concrete capability justification.

---

### Lucide

Current state:

`PROVISIONAL DEFAULT CANDIDATE`

Promote only after CodeInteX visual-language validation establishes that Lucide fits:

- icon semantics;
- stroke/visual language;
- accessibility usage;
- product identity.

---

### Visual regression testing

Current state:

`OPEN`

Activate when component/page visual regression risk justifies:

- baseline image maintenance;
- CI cost;
- provider/tool complexity.

Prefer repository-controlled or vendor-neutral options where fit is comparable.

---

### Observability provider

Current state:

`OPEN`

Select when deployment/runtime requirements are known.

Provider evaluation should include:

- OpenTelemetry interoperability;
- logs/traces/metrics support;
- privacy controls;
- retention;
- alerting;
- cost;
- vendor lock-in;
- operational burden.

---

### Browser error reporting and RUM

Current state:

`OPEN`

Activate when production learner traffic creates a concrete requirement for:

- client crash visibility;
- browser performance telemetry;
- field diagnostics.

Do not collect excessive learner data merely because a monitoring SDK supports it.

---

### CSP implementation

Current state:

`OPEN MECHANISM / LOCKED REQUIREMENT`

Production CSP is required.

Choose nonce-, hash-, or other appropriate strategy only after:

- rendering strategy;
- caching model;
- third-party scripts;
- hosting;

are sufficiently known.

---

### Performance budgets

Current state:

`PROVISIONAL`

Establish quantitative budgets after the reference implementation provides representative measurements.

Budgets should protect learner experience rather than arbitrary benchmark prestige.

---

### Hosting/deployment

Current state:

`OPEN`

This profile intentionally does not choose:

- Vercel;
- Cloud Run;
- container platform;
- another provider.

Hosting is a separate architecture/operations decision and must consider:

- cost;
- traffic;
- deployment model;
- security;
- observability;
- lock-in;
- operational complexity.

---

### Activation discipline

Do not resolve an OPEN item merely because:

- documentation recommends a tool;
- a dependency is popular;
- an AI agent prefers it;
- a starter template includes it;
- another company uses it;
- it may be useful in the future.

Resolve it when:

~~~text
requirement
+
evidence
+
implementation context
~~~

justify the decision.

**Decision state: LOCKED activation discipline**

---

## 25. Web Implementation Profile Completion Gate

The Web Implementation Profile v0.1 may proceed to reference implementation when it defines a coherent and testable implementation baseline without unnecessarily locking unresolved repository or operational choices.

### Required implementation contracts

Current status:

~~~text
Purpose and scope: PASS
Verified technology baseline: PASS
Dependency layering: PASS
Next.js / React execution model: PASS
Server / Client Component boundary: PASS
Domain adapter / TypeScript boundary: PASS
Semantic-token consumption: PASS
Tailwind implementation boundary: PASS
CodeInteX-owned component architecture: PASS
Responsive implementation: PASS
Accessibility implementation/testing: PASS
Interaction/focus behavior: PASS
Motion dependency policy: PASS
Icon dependency policy: PASS
Storybook workbench: PASS
Testing strategy: PASS
Performance/bundle discipline: PASS
Security boundary: PASS
Dependency/version governance: PASS
Observability/error-reporting boundary: PASS
Implementation acceptance/release gate: PASS
AI coding-agent execution contract: PASS
Decision-state governance: PASS
Open-item activation discipline: PASS
~~~

### Upstream dependency

The profile consumes:

~~~text
PES Core: AVAILABLE
PES Consumption Contract: AVAILABLE
LMS Experience Profile v0.1: PASS
Mandatory specialist research A–D: PASS
~~~

### Remaining uncertainty

Remaining OPEN and PROVISIONAL items are primarily:

- repository/tooling topology decisions;
- provider choices;
- quantitative thresholds;
- capability-triggered dependencies;
- implementation details requiring reference-implementation evidence.

They do not block beginning a controlled reference implementation.

### Reference implementation objectives

The reference implementation should validate:

- Server/Client boundaries;
- domain/API adapter adequacy;
- semantic-token consumption;
- CodeInteX component ownership;
- Base UI integration;
- Tailwind implementation;
- responsive behavior;
- accessibility;
- component/testing workflow;
- critical learner-state rendering;
- bundle/performance assumptions.

### Important constraint

Reference implementation is a validation mechanism.

It must not silently become a new source of architectural authority.

When implementation contradicts a LOCKED contract:

~~~text
investigate the contradiction
→ identify evidence
→ revise implementation or formally revise contract
~~~

Do not preserve accidental implementation merely because code already exists.

### Completion conclusion

**WEB IMPLEMENTATION PROFILE v0.1 COMPLETION GATE: PASS**

The current baseline is sufficiently specified to proceed to controlled reference implementation.

### Meaning of PASS

`PASS` means:

~~~text
sufficient implementation contract for the next execution stage
~~~

It does not mean:

- repository topology resolved;
- production deployment architecture resolved;
- final visual language complete;
- accessibility conformance certified;
- performance budgets proven;
- all dependencies permanently frozen;
- LMS implementation complete.

**Decision state: LOCKED for current milestone**

---

## 26. Document Status

This document is:

**PROVISIONAL IMPLEMENTATION BASELINE — v0.1**

Its LOCKED decisions are the authorized current web implementation baseline.

Its PROVISIONAL decisions require implementation evidence before promotion.

Its OPEN decisions must remain explicit until their activation conditions are met.

### Current implementation baseline

~~~text
Framework: Next.js 16.x / App Router
React: compatible supported React 19.x
Language: TypeScript
Styling engine: Tailwind CSS 4.x
Behavioral primitives: Base UI
Component bootstrap/source: shadcn-derived where useful
Component ownership: CodeInteX
Component workbench: Storybook
Browser E2E: Playwright
Automated E2E accessibility: @axe-core/playwright
Motion: provisional / capability-triggered
Icons: Lucide provisional candidate
~~~

### Next execution stage

The next stage is:

~~~text
controlled reference implementation
~~~

not another broad technology-selection exercise.

Reference implementation should begin with enough architecture to validate the contracts while avoiding premature repository overengineering.

### Immediate implementation priority

A suitable first vertical slice should exercise multiple contracts together, for example:

~~~text
Learner Dashboard
→ Resume Learning
→ Curriculum Navigation
→ Lesson Experience
~~~

with:

- real domain-shaped mock/API contract;
- PES semantic tokens;
- CodeInteX-owned components;
- responsive behavior;
- accessibility validation;
- Storybook coverage;
- Playwright workflow coverage.

Assessment/project flow should follow because it exercises more consequential state transitions.

### Revalidation triggers

Revisit this profile when:

- reference implementation exposes architectural contradiction;
- Next.js/React support status materially changes;
- a security advisory changes required baseline;
- Base UI/shadcn architecture materially changes;
- accessibility testing exposes systemic implementation failure;
- performance evidence invalidates client/server assumptions;
- repository topology forces a material boundary change;
- deployment architecture creates new rendering/security constraints.

### Technology-change rule

Technology may change.

The stable objective remains:

~~~text
correct
usable
accessible
secure
maintainable
testable
observable
interoperable
proportionally scalable
human- and AI-agent-usable
~~~

Implementation technology remains subordinate to those attributes and to PES/LMS contracts.
