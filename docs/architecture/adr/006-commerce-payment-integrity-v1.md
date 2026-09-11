# ADR-006: Commerce & Payment Integrity V1

Status: Accepted
Date: 2026-09-11

## Context

CodeInteX Learning requires payment integrity that remains correct under
provider retries, duplicate or out-of-order notifications, lost responses,
concurrency, reconciliation, refunds, reversals, disputes, chargebacks, and
future payment-provider changes.

The commercial policy is defined in ADR-005.

The payment architecture must preserve that policy without coupling the LMS
domain to Midtrans or any future provider.

## Decision

CodeInteX adopts the architecture and invariants defined in:

`docs/architecture/commerce-payment-integrity-v1.md`

The specification is accepted as the V1 architecture contract for one-time
Course purchases.

Key decisions include:

- Order is a server-authoritative immutable commercial snapshot once checkout
  is created.
- Order identity and provider Payment identity are separate.
- One Order may have multiple sequential provider Payment transactions.
- CodeInteX owns business idempotency and ambiguous-outcome recovery.
- Browser callbacks are never payment authority.
- Payment success requires trusted server-side provider verification.
- Authenticated provider notifications are durably accepted before business
  processing.
- ProviderEvent processing is retryable and separate from webhook request
  handling.
- Reconciliation and webhook processing use the same payment-observation
  logic.
- Financial acquisition facts are distinct from later refund, reversal,
  dispute, and chargeback facts.
- Integrity/review workflow is distinct from Payment financial state.
- Fulfillment is locally atomic and safely retryable.
- Duplicate or competing successful payments must never create duplicate
  purchase entitlements.
- Independent CourseEntitlement grants remain independent.
- Learning history survives commercial-access revocation.
- Manual anomaly resolution must be authorized, idempotent, and auditable.

## V1 Implementation Constraint

The architecture remains a modular monolith.

PostgreSQL/Django may provide the initial durable ProviderEvent inbox and
work-claiming mechanism.

This ADR does not require:

- microservices;
- Kafka;
- RabbitMQ;
- a generic event platform;
- a universal payment framework.

Those technologies require independent evidence before adoption.

## Provider Boundary

Midtrans remains a provisional first provider for the Indonesian MVP.

Midtrans-specific transaction statuses, tokens, identifiers, retry semantics,
and webhook fields remain in the integration boundary.

They must not define Course, Enrollment, LessonProgress, entitlement, or core
Commerce semantics.

## Financial Adjustments

A successful Payment acquisition is historical evidence.

Refund, partial refund, reversal, dispute, and chargeback are subsequent
financial facts rather than reasons to erase successful acquisition history.

For Commercial Access Policy V1:

- partial refund does not automatically revoke purchase access;
- confirmed full refund may revoke the affected purchase entitlement;
- confirmed full chargeback may revoke the affected purchase entitlement;
- confirmed full provider reversal may revoke the affected purchase
  entitlement;
- another independent ACTIVE entitlement continues to provide effective
  access.

## Consequences

### Positive

- duplicate and retried provider events can be handled safely;
- provider outages and missing webhooks can be reconciled;
- payment-provider migration does not require LMS-domain redesign;
- financial history remains auditable;
- access side effects remain idempotent;
- concurrency and double-payment failure modes are explicitly addressed;
- V1 remains implementable inside the existing modular monolith.

### Trade-offs

- Commerce requires several explicit concepts rather than one Payment status;
- provider events require durable processing and operational visibility;
- reconciliation becomes a first-class operational responsibility;
- staff anomaly resolution requires authorization and audit evidence;
- implementation correctness depends on database constraints and transaction
  boundaries being designed carefully.

## Deferred Implementation Decisions

The accepted architecture intentionally does not lock:

- exact Django model and field names;
- exact PostgreSQL locking/constraint implementation;
- exact worker runtime;
- exact reconciliation cadence and retry/backoff values;
- exact ProviderEvent retention period;
- exact operator UI;
- exact Midtrans status mapping.

These must be chosen during implementation without violating the accepted
invariants.

## Related Decisions

- ADR-001: immutable published CourseRelease.
- ADR-003: Django session and same-origin authentication.
- ADR-004: provider-portable Commerce architecture.
- ADR-005: Commercial Access Policy V1.
