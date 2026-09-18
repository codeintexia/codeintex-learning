# ADR-008: Build-vs-Adopt Learning Platform Strategy

Status: Accepted
Date: 2026-09-18

## Context

CodeInteX Learning has completed a working monetization slice with:

- immutable published CourseRelease semantics;
- learner Enrollment pinned to CourseRelease;
- server-authoritative LessonProgress;
- CodeInteX-owned learner-facing APIs;
- Django session authentication with same-origin browser APIs;
- provider-portable Commerce;
- CourseEntitlement separated from Enrollment and Payment;
- real Midtrans Sandbox checkout and signed-webhook fulfillment;
- PostgreSQL-backed concurrency verification.

At this point, continuing to expand LMS functionality without an explicit
Build-vs-Adopt decision would create two opposite risks:

1. replacing a proven CodeInteX domain core with a mature LMS platform and
   absorbing unnecessary migration, integration, and dual-source-of-truth
   complexity; or
2. treating "custom LMS" as permission to rebuild every mature LMS capability
   ourselves.

Representative mature LMS platforms, including Open edX, Moodle, and Canvas,
were evaluated as potential replacements or integration targets.

The decision must optimize for CodeInteX requirements, reversibility, total
cost of ownership, interoperability, maintainability, operational complexity,
migration cost, and revenue priorities rather than framework popularity.

## Decision

CodeInteX adopts the following long-term platform strategy:

> CodeInteX semantics at the core; standards and specialized capabilities at
> the edges.

CodeInteX will continue to own the product and runtime semantics that are
already differentiated, verified, and materially coupled to its product model.

CodeInteX will not adopt Open edX, Moodle, Canvas, or another full LMS as the
canonical learning core at this stage.

This is not a decision to build every LMS capability ourselves.

Complex, non-differentiating capabilities must pass an explicit
Build-vs-Adopt evaluation before custom implementation.

## CodeInteX-Owned Core

The following remain CodeInteX-owned canonical semantics:

- Course as stable product identity;
- CourseRelease as immutable published learner contract;
- learner-facing CodeInteX API contracts;
- Enrollment and release-pinning semantics;
- learner progress semantics;
- CourseEntitlement and commercial-access semantics;
- Commerce and payment-integrity semantics;
- learner-facing Product Experience implemented through the CodeInteX web
  application.

These semantics must not be silently delegated to an external LMS in a way
that creates competing sources of truth.

## Replaceable Implementations

Owning CodeInteX semantics does not require every implementation component to
remain permanent.

In particular:

- Wagtail is the current authoring implementation, not the learner runtime
  contract;
- Midtrans is one payment-provider adapter, not the Commerce domain;
- the current authentication implementation may later integrate with a wider
  SSO/OIDC architecture;
- specialized learning capabilities may be provided by external systems behind
  explicit integration boundaries.

Implementation replacement must preserve the stable CodeInteX contracts or use
an explicit migration decision.

## Adopt / Integrate Before Building

Before implementing a complex non-differentiating LMS capability, evaluate
whether an existing standard, engine, service, or interoperable product can
satisfy the requirement.

Examples include:

- advanced assessment engines;
- proctoring;
- virtual classroom systems;
- plagiarism detection;
- standards-compliant content runtimes;
- institutional roster/SIS workflows;
- external credential ecosystems;
- learning-record stores;
- specialized discussion/community systems.

Adoption is preferred when it satisfies the requirement without compromising
canonical CodeInteX semantics, product experience, security, accessibility, or
operational sustainability.

## Standards Boundary

Interoperability should be introduced when backed by concrete product or
integration requirements.

Current direction:

- LTI 1.3 / LTI Advantage: prepare for external learning-tool integration;
- QTI: prepare for assessment interchange when assessment requirements justify
  it;
- Open Badges: prepare for interoperable credentials when credential issuance
  becomes an active workstream;
- SCORM, xAPI, cmi5, Caliper, OneRoster, and similar standards remain
  requirement-driven rather than automatically adopted.

Standards are integration mechanisms, not replacements for CodeInteX domain
modeling.

## Full-LMS Adoption

A full external LMS may be reconsidered if future evidence changes the
economics or requirements materially.

Re-evaluation triggers include:

- enterprise customers require mature SIS, roster, gradebook, or institutional
  administration workflows;
- assessment requirements exceed what is economical to own;
- SCORM or another legacy content runtime becomes a material revenue
  requirement;
- instructor/admin workflow becomes substantially more complex than the
  learner/product differentiation;
- regulatory or reporting requirements demand mature capabilities that are
  expensive to reproduce safely;
- measured engineering and operational total cost of ownership exceeds the
  migration/integration cost of adopting a mature platform.

A future re-evaluation must compare concrete requirements and migration costs.
It must not replace this decision solely because another platform has more
features.

## Architecture Constraints

This decision does not authorize:

- a generic LMS abstraction layer;
- dual canonical Enrollment or progress systems;
- speculative synchronization with an external LMS;
- premature microservices;
- rebuilding mature standards or protocols without evidence;
- adding LMS bounded contexts merely to match competitor feature lists.

New domain concepts must be introduced only when CodeInteX invariants or
product requirements require them.

## Consequences

### Positive

- preserves already-proven CodeInteX domain semantics;
- avoids a premature replatforming project;
- keeps learner Product Experience under CodeInteX control;
- prevents provider/platform lock-in at the core;
- allows specialized mature capabilities to be adopted selectively;
- preserves Wagtail and other implementation choices as replaceable;
- reduces the risk of recreating a complete conventional LMS.

### Trade-offs

- CodeInteX remains responsible for its canonical runtime and commerce code;
- explicit integration boundaries must be designed when external capabilities
  are adopted;
- some capabilities available out-of-the-box in large LMS products will not be
  immediately available;
- future full-LMS adoption, if justified, will require explicit mapping and
  migration of CodeInteX-owned semantics.

## Decision State

LOCKED:

- CodeInteX-owned learning/runtime and commerce semantics remain canonical.
- No full-LMS replatforming is justified by current requirements.
- Complex non-differentiating capabilities require an Adopt/Integrate
  evaluation before custom implementation.
- "CodeInteX semantics at the core; standards at the edges" is the governing
  platform strategy.

PROVISIONAL:

- Wagtail remains the authoring implementation.
- Specific standards and external engines remain requirement-driven.

OPEN:

- future institutional LMS interoperability;
- future full-LMS adoption if re-evaluation triggers become material;
- exact implementation choices for assessment, credentials, analytics,
  classroom, SIS, and other future workstreams.

## Related Decisions

- ADR-001: Immutable Published Course Releases.
- ADR-002: Separate Wagtail Authoring from Learner Runtime State.
- ADR-003: Django Session Authentication with Same-Origin Browser APIs.
- ADR-004: Provider-Portable Commerce.
- ADR-005: Commercial Access Policy V1.
- ADR-006: Commerce & Payment Integrity V1.
- ADR-007: Commerce Schema V1.
