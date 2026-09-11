# ADR-005: Commercial Access Policy V1

Status: Accepted
Date: 2026-09-11

## Context

CodeInteX Learning needs a clear commercial-access contract before Order,
Payment, entitlement, and payment-provider integration are implemented.

Without that contract, implementation choices could accidentally define
customer rights, couple access to payment-provider state, or damage learning
history when commercial state changes.

The V1 commercial model prioritizes a simple one-time course purchase while
preserving the ability to evolve commerce independently from the learning
domain.

## Decision

### One-Time Purchase

A successful one-time purchase grants indefinite access to the purchased
Course unless the entitlement is later revoked.

The commercial entitlement targets Course, not a particular CourseRelease.

Normal future CourseRelease revisions of that Course are included for
entitled learners.

A materially different scope, value proposition, credential, or learning
product is modeled as a new Course/product rather than being hidden inside a
revision.

### Release and Enrollment Semantics

Enrollment remains pinned to a specific CourseRelease.

Publishing a newer CourseRelease does not silently migrate existing
Enrollments.

For V1, granting an entitlement provisions an Enrollment to the current
published CourseRelease.

The exact learner experience for moving to a newer release remains an open
decision.

### Revocation and Learning History

Refund or confirmed chargeback may revoke commercial access.

Revocation does not delete Enrollment, LessonProgress, or historical learning
records.

Commercial access state and learning history are separate concerns.

### Free and Granted Access

Free preview does not create a CourseEntitlement.

Scholarship and administrative grants create real CourseEntitlement records
without fabricating Order or Payment records.

### Discounts

Coupons and discounts affect commerce calculations.

They do not change the semantics of the resulting course entitlement.

## Consequences

### Positive

- the customer promise is explicit before payment implementation;
- entitlement remains independent from payment-provider vocabulary;
- normal course revisions do not require repeat purchases;
- existing learner progress cannot be corrupted by silent release migration;
- refund and chargeback handling does not destroy learning history;
- scholarship and administrative access do not pollute financial records;
- the V1 model remains small enough for the current one-time-purchase scope.

### Trade-offs

- CodeInteX must define what constitutes a normal revision versus a materially
  new product;
- entitlement and enrollment remain separate models even though V1 provisions
  them together;
- future subscription, bundle, and B2B models may require additional access
  concepts rather than overloading CourseEntitlement.

## Open Decisions

- exact refund eligibility and refund window;
- detailed fraud policy;
- UX and policy for moving from CourseRelease N to N+1;
- whether multiple release enrollments may be active simultaneously;
- commercial handling of 100%-discount orders;
- subscription semantics;
- bundle semantics;
- B2B seat and license semantics;
- international tax policy.

## Related Decisions

- ADR-001: published CourseRelease records are immutable.
- ADR-004: CodeInteX Commerce is provider-portable.
- Payment, entitlement, and enrollment are separate concepts.
- Learning progress survives loss of commercial access.
