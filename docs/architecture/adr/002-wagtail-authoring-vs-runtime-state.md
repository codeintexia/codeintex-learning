# ADR-002: Separate Wagtail Authoring from Learner Runtime State

Status: Accepted
Date: 2026-09-11

## Context

Wagtail is useful for structured authoring, but learner progress, enrollment, payment entitlement, attempts, and other transactional state have different integrity, lifecycle, and security requirements.

Placing runtime learner state inside CMS content structures would couple the learner contract to Wagtail internals and make transactional behavior harder to reason about, test, secure, and migrate.

## Decision

- Wagtail is the current authoring implementation.
- Learner-facing contracts are owned by CodeInteX APIs under `/api/v1/...`.
- Public/content read models are separated from authenticated runtime APIs.
- Enrollment and lesson progress are first-class Django transactional models.
- Runtime learner state does not live in Wagtail StreamField.
- `learning-ui` remains unaware of Wagtail and Django transport details.

## Consequences

Positive:

- authoring implementation can evolve without redefining learner runtime contracts;
- transactional integrity is handled by normal Django models/database constraints;
- frontend and future clients depend on CodeInteX contracts rather than Wagtail internals;
- future package extraction remains possible without forcing it now.

Trade-offs:

- explicit mapping from authoring models to learner API payloads is required;
- some information exists in both authoring/domain read models and runtime composition layers;
- boundaries require discipline to avoid accidental leakage.

## Non-goal

This ADR does not commit CodeInteX to publishing a reusable Wagtail plugin or framework. Extraction remains optional downstream value.
