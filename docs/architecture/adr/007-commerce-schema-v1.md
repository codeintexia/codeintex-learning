# ADR-007: Commerce Schema V1

Status: Accepted
Date: 2026-09-12

## Context

ADR-004 established provider-portable Commerce.

ADR-005 established Commercial Access Policy V1.

ADR-006 established Commerce and Payment Integrity V1.

The accepted architecture now requires a concrete persistence boundary before
provider integration can be implemented safely.

## Decision

CodeInteX adopts the schema contract defined in:

`docs/architecture/commerce-schema-v1.md`

V1 introduces one physical Django app:

`commerce`

The V1 core model responsibilities are:

- CourseOffer
- Order
- Payment
- ProviderEvent
- FinancialAdjustment
- PaymentIntegrityCase
- CourseEntitlement

Learning remains physically owned by the existing `learning` Django app.

The `learning` app must not depend on `commerce`.

## Correctness Boundary

PostgreSQL is the production database and is part of the Commerce correctness
boundary.

Concurrency-sensitive invariants use an appropriate combination of:

- database constraints;
- transaction.atomic();
- row locking;
- idempotent transactional services.

SQLite remains useful for fast ordinary tests but is not sufficient evidence
for PostgreSQL row-locking behavior.

Race-sensitive Commerce behavior requires PostgreSQL-backed transaction tests.

## Scope Discipline

This decision does not introduce:

- generic Product or SKU models;
- invoices;
- accounting ledger infrastructure;
- subscriptions;
- bundles;
- B2B licensing;
- tax engines;
- wallets;
- event buses;
- microservices.

Those require separate evidence before adoption.

## Provider Boundary

No Midtrans-specific vocabulary defines the core Commerce schema.

Provider-specific transaction statuses, tokens, event fields, and retry
behavior remain inside the payment-provider integration boundary.

## Consequences

### Positive

- Commerce is physically separated from Learning without creating unnecessary
  microservices or multiple Django apps;
- financial history remains auditable;
- access grants remain independent from Payment and Enrollment;
- concurrency-sensitive invariants can be enforced by PostgreSQL;
- provider migration does not require redesigning Learning state;
- the schema remains small enough for the current one-time-purchase scope.

### Trade-offs

- Commerce introduces several explicit models rather than one overloaded
  Payment table;
- PostgreSQL integration testing becomes mandatory for race-sensitive logic;
- account anonymization/retention requires an explicit future workflow rather
  than cascading deletion;
- durable event processing and reconciliation become operational
  responsibilities.

## Implementation Sequence

The implementation must proceed tests-first:

1. create the `commerce` Django app;
2. add model and constraint tests;
3. add PostgreSQL-backed concurrency acceptance tests;
4. implement models;
5. create and inspect migrations;
6. run the full backend regression suite;
7. implement provider-neutral transactional services;
8. only then implement the first payment-provider adapter.

## Related Decisions

- ADR-001: immutable published CourseRelease.
- ADR-004: provider-portable Commerce.
- ADR-005: Commercial Access Policy V1.
- ADR-006: Commerce & Payment Integrity V1.
