# ADR-004: Provider-Portable Commerce Architecture

Status: Accepted
Date: 2026-09-11

## Context

CodeInteX will initially sell primarily in Indonesia but is intended to support international expansion.

A payment provider selected for the Indonesian MVP may not remain the best provider for other countries, currencies, payment methods, subscriptions, tax requirements, or future commercial models.

Coupling learning or access models directly to a provider such as Midtrans would create unnecessary migration cost and vendor lock-in.

## Decision

CodeInteX Commerce will be provider-portable.

Payment providers are integration adapters rather than domain authorities.

The CodeInteX domain owns its own commercial state and terminology.

Provider-specific concepts such as:

- Midtrans Snap tokens;
- Midtrans transaction statuses;
- Stripe Checkout Session IDs;
- Stripe PaymentIntent IDs;
- provider webhook event identifiers;

must not become fields or semantics of:

- Course;
- CourseRelease;
- Enrollment;
- LessonProgress;
- CourseEntitlement.

Provider adapters may translate provider-specific behavior into CodeInteX-owned Order and Payment state.

Indonesian and international providers may coexist.

Historical payments retain the provider through which they were originally processed.

Changing the provider used for new transactions must not require rewriting historical payment records or learner progress.

## Architectural Boundary

Conceptually:

    CodeInteX Commerce
            |
            v
    Payment Provider Port
            |
            +-- Midtrans Adapter
            |
            +-- Global PSP Adapter
            |
            +-- Merchant of Record Adapter
                (if selected later)

The product/frontend layer should request a checkout capability from CodeInteX rather than depend directly on a provider-specific component.

For example:

    POST /orders/{id}/checkout/
            |
            v
    CodeInteX selects provider
            |
            v
    checkout response

The browser should not need to understand internal provider-selection policy.

## Consequences

### Positive

- lower provider switching cost for future one-time transactions;
- Indonesian and global payment providers can coexist;
- learning-domain integrity is preserved;
- provider pricing changes do not force LMS-domain redesign;
- historical payment evidence remains auditable;
- future routing by market or currency remains possible.

### Trade-offs

- a small provider abstraction/integration boundary must be maintained;
- provider capabilities cannot always be normalized perfectly;
- refunds, recurring billing, disputes, and reconciliation may require provider-specific handling behind the boundary;
- provider portability does not imply that migration is cost-free.

## Constraints

The abstraction must remain capability-driven and minimal.

Do not create a large universal payment framework in anticipation of hypothetical providers.

Only abstract capabilities CodeInteX actually uses.

Provider-specific functionality may exist behind an adapter when normalization would destroy important semantics.

## Current Provider State

PROVISIONAL:

- Midtrans Snap is the current strong candidate for Indonesian MVP one-time checkout.

OPEN:

- global PSP selection;
- Merchant of Record evaluation;
- recurring-billing provider;
- international tax/compliance model;
- multi-provider routing policy.

## Related Decisions

- Payment, entitlement, and enrollment remain separate concepts.
- Learning progress is independent from commercial-access state.
- Provider webhook processing must be authenticated and idempotent.
