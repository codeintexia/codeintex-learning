# ADR-001: Immutable Published Course Releases

Status: Accepted
Date: 2026-09-11

## Context

CodeInteX Learning requires learner progress, course history, and future certification/audit behavior to remain reproducible even when course content evolves.

If published course content can be edited in place, an existing learner may resume against materially different content while retaining progress recorded against an earlier version.

## Decision

- `Course` represents stable product identity.
- `CourseRelease` represents a versioned learner-facing contract.
- Draft releases are editable.
- Once published, a `CourseRelease` and its learner-facing module/lesson structure are immutable.
- Changes after publication require a new `CourseRelease`.
- Learner enrollment pins to a specific release.
- Runtime progress remains associated with that enrolled release.

## Consequences

Positive:

- learner progress is reproducible;
- historical releases remain auditable;
- publishing a new release cannot silently mutate existing learner experience;
- payment/entitlement logic can grant access to an explicit release.

Trade-offs:

- content corrections after publication require a new release or an explicitly governed exceptional migration;
- authoring workflows must make release state visible;
- storage retains historical release content.

## Evidence

Published-release immutability is covered by backend tests and has remained part of the verified architecture baseline.
