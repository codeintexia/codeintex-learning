# Commerce Schema V1

Status: Accepted
Date: 2026-09-12

## Purpose

Define the minimum Django/PostgreSQL schema, database invariants, transaction
boundaries, and acceptance-test requirements for CodeInteX one-time Course
purchases.

This document implements the accepted architecture in:

- ADR-004: Provider-Portable Commerce Architecture
- ADR-005: Commercial Access Policy V1
- ADR-006: Commerce & Payment Integrity V1
- docs/architecture/commerce-payment-integrity-v1.md

This is a schema contract, not payment-provider implementation.

Midtrans-specific fields and behavior remain outside the core domain.

## Physical Boundary

V1 introduces one Django app:

    commerce

Learning remains in:

    learning

The physical model boundary is:

    learning/
        Course
        CourseRelease
        Module
        Lesson
        Enrollment
        LessonProgress

    commerce/
        CourseOffer
        Order
        Payment
        ProviderEvent
        FinancialAdjustment
        PaymentIntegrityCase
        CourseEntitlement

Access remains a distinct logical concern even though CourseEntitlement is
physically located in the commerce Django app for V1.

A separate access Django app is not justified by current requirements.

## Dependency Direction

Allowed:

    commerce -> settings.AUTH_USER_MODEL
    commerce -> learning.Course

Fulfillment services may use:

    learning.CourseRelease
    learning.Enrollment

Not allowed:

    learning -> commerce

The learning domain must remain usable without importing Commerce models or
services.

## Money Representation

Monetary values use integer minor units.

Examples:

    IDR 500000 -> amount_minor = 500000
    USD 19.99   -> amount_minor = 1999

Core Commerce must not use floating-point money values.

Currency is represented using an uppercase three-character currency code.

Cross-table currency equality is enforced by transactional services and tests
rather than database CHECK constraints.

## User Deletion Policy for V1

Commercial and access history must not be deleted accidentally because a user
account is hard-deleted.

V1 therefore uses PROTECT for learner references in commercial records.

This is an engineering fail-safe, not a complete privacy or legal-retention
policy.

Future account deletion must use an explicit anonymization or retention
workflow rather than cascading deletion of commercial history.

## CourseOffer

### Responsibility

CourseOffer is the server-authoritative commercial price definition for a
one-time Course purchase.

It is deliberately Course-specific.

V1 does not introduce a generic Product, SKU, PriceBook, subscription plan,
bundle, or catalog engine.

### Fields

    id
        UUID primary key

    course
        ForeignKey -> learning.Course
        on_delete = PROTECT

    amount_minor
        PositiveBigIntegerField

    currency
        CharField(max_length=3)

    is_active
        BooleanField(default=True)

    created_at
        DateTimeField(auto_now_add=True)

    updated_at
        DateTimeField(auto_now=True)

### Database Constraints

Amount must be greater than zero.

At most one ACTIVE CourseOffer may exist for:

    course + currency

This must be database-enforced with conditional uniqueness.

Historical inactive offers may remain for audit and Order references.

### Service Rules

Commercial identity fields are immutable after CourseOffer creation:

    course
    amount_minor
    currency

A price change creates a new CourseOffer and changes which offer is ACTIVE.

Historical offers remain unchanged for audit and Order references.

An Order never verifies payment against a later CourseOffer value.

## Order

### Responsibility

Order is a server-authoritative commercial purchase snapshot.

It records what CodeInteX agreed to sell to a learner at a particular price.

### States

    OPEN
    FULFILLED
    CANCELLED
    EXPIRED

### Fields

    id
        UUID primary key

    learner
        ForeignKey -> settings.AUTH_USER_MODEL
        on_delete = PROTECT

    course
        ForeignKey -> learning.Course
        on_delete = PROTECT

    offer
        ForeignKey -> CourseOffer
        on_delete = PROTECT

    status
        CharField with V1 Order states

    subtotal_amount_minor
        PositiveBigIntegerField

    discount_amount_minor
        PositiveBigIntegerField(default=0)

    total_amount_minor
        PositiveBigIntegerField

    currency
        CharField(max_length=3)

    course_title_snapshot
        CharField(max_length=255)

    created_at
        DateTimeField(auto_now_add=True)

    expires_at
        DateTimeField

    fulfilled_at
        DateTimeField(null=True, blank=True)

    cancelled_at
        DateTimeField(null=True, blank=True)

### Database Constraints

Order status must be database-constrained to:

    OPEN
    FULFILLED
    CANCELLED
    EXPIRED

Amounts must be non-negative.

Discount must not exceed subtotal.

Total must equal:

    subtotal - discount

For the V1 paid-purchase flow:

    total_amount_minor > 0

A zero-total commercial flow is intentionally unsupported until the
100%-discount policy is explicitly designed.

At most one OPEN ordinary purchase Order may exist for:

    learner + course

This must be database-enforced with conditional uniqueness.

### Immutability

Commercial snapshot fields must not be changed after Order creation:

    learner
    course
    offer
    subtotal_amount_minor
    discount_amount_minor
    total_amount_minor
    currency
    course_title_snapshot

Lifecycle fields may change through explicit service transitions.

### Service Rules

Order creation must derive commercial values from trusted server-side state.

The browser may identify a Course or submit a coupon code, but it does not
authoritatively choose:

    learner
    price
    discount amount
    currency
    entitlement target
    payment result

Until an explicit promotion/coupon persistence design is accepted, the V1
launch flow must use:

    discount_amount_minor = 0

The dormant snapshot fields do not authorize implementing ad-hoc discounts
without auditable pricing provenance.

## Payment

### Responsibility

Payment represents one provider transaction or checkout intent for an Order.

It does not necessarily represent each lower-level card, bank, QR, or
authorization attempt occurring inside a provider checkout.

### States

    CREATED
    PENDING
    SUCCEEDED
    FAILED
    CANCELLED
    EXPIRED

### Fields

    id
        UUID primary key

    order
        ForeignKey -> Order
        on_delete = PROTECT

    provider
        CharField

    status
        CharField with V1 Payment states

    operation_key
        UUIDField(unique=True)

    merchant_reference
        CharField(unique=True)

    provider_transaction_id
        CharField(null=True, blank=True)

    amount_minor
        PositiveBigIntegerField

    currency
        CharField(max_length=3)

    created_at
        DateTimeField(auto_now_add=True)

    updated_at
        DateTimeField(auto_now=True)

    succeeded_at
        DateTimeField(null=True, blank=True)

### Database Constraints

Payment status must be database-constrained to:

    CREATED
    PENDING
    SUCCEEDED
    FAILED
    CANCELLED
    EXPIRED

Payment amount must be greater than zero.

When provider_transaction_id is present, the pair:

    provider + provider_transaction_id

must be unique.

At most one externally payable nonterminal Payment may exist per Order.

For V1 the nonterminal externally payable states are:

    CREATED
    PENDING

### Identity Rules

These identities are deliberately separate:

    Order.id
    Payment.id
    Payment.operation_key
    Payment.merchant_reference
    provider_transaction_id

merchant_reference is generated by CodeInteX and remains stable for the
logical provider transaction.

### Ambiguous Provider Outcome

Payment must exist locally before a provider create-checkout call is made.

If the outbound provider call times out or its result is unknown:

    do not create a replacement Payment

The same logical operation must first be retried or reconciled.

A new Payment is allowed only after the previous provider transaction is known
not to remain externally payable.

## ProviderEvent

### Responsibility

ProviderEvent is the durable inbox record for an authenticated provider
notification.

It is integration evidence rather than learner or Course state.

### Processing States

    RECEIVED
    PROCESSING
    PROCESSED
    FAILED

### Fields

    id
        UUID primary key

    provider
        CharField

    payment
        nullable ForeignKey -> Payment
        on_delete = PROTECT

    merchant_reference
        CharField(blank=True)

    provider_event_id
        CharField(null=True, blank=True)

    provider_transaction_id
        CharField(null=True, blank=True)

    event_type
        CharField(blank=True)

    provider_status
        CharField(blank=True)

    amount_minor
        PositiveBigIntegerField(null=True, blank=True)

    currency
        CharField(max_length=3, blank=True)

    payload_digest
        CharField

    authenticity_verified_at
        DateTimeField

    authenticity_method
        CharField

    processing_status
        CharField with processing states

    occurred_at
        DateTimeField(null=True, blank=True)

    received_at
        DateTimeField(auto_now_add=True)

    processing_started_at
        DateTimeField(null=True, blank=True)

    processed_at
        DateTimeField(null=True, blank=True)

    attempt_count
        PositiveIntegerField(default=0)

    last_error_code
        CharField(blank=True)

### Database Constraints

ProviderEvent processing status must be database-constrained to:

    RECEIVED
    PROCESSING
    PROCESSED
    FAILED

Where provider_event_id is present:

    provider + provider_event_id

must be unique.

Persisting ProviderEvent means the provider-specific authenticity check has
already succeeded.

Invalid or unauthenticated webhook input does not enter the trusted
ProviderEvent inbox.

### Data Minimization

ProviderEvent does not persist arbitrary raw webhook payloads indefinitely.

Only evidence required for:

    verification
    reconciliation
    support
    audit
    incident investigation

is retained.

Any future temporary raw-event retention requires an explicit retention and
access-control policy.

### Correlation

merchant_reference exists specifically to recover this case:

    local Payment created
        ->
    provider request transmitted
        ->
    local HTTP request times out
        ->
    provider actually created transaction
        ->
    webhook arrives before provider_transaction_id was saved locally

The event can still correlate to the original Payment through the stable
CodeInteX merchant reference.

## FinancialAdjustment

### Responsibility

FinancialAdjustment records a financial fact occurring after or around a
successful acquisition without rewriting historical Payment success.

### Kinds

    REFUND
    REVERSAL
    CHARGEBACK

### States

    PENDING
    CONFIRMED
    FAILED

### Fields

    id
        UUID primary key

    payment
        ForeignKey -> Payment
        on_delete = PROTECT

    kind
        CharField with adjustment kinds

    status
        CharField with adjustment states

    amount_minor
        PositiveBigIntegerField

    currency
        CharField(max_length=3)

    operation_key
        UUIDField(null=True, blank=True)

    provider_reference
        CharField(null=True, blank=True)

    initiated_by
        nullable ForeignKey -> settings.AUTH_USER_MODEL
        on_delete = PROTECT

    initiation_reason
        TextField(blank=True)

    created_at
        DateTimeField(auto_now_add=True)

    confirmed_at
        DateTimeField(null=True, blank=True)

### Database Constraints

FinancialAdjustment kind must be database-constrained to:

    REFUND
    REVERSAL
    CHARGEBACK

FinancialAdjustment status must be database-constrained to:

    PENDING
    CONFIRMED
    FAILED

Adjustment amount must be greater than zero.

When operation_key is present, it must be unique.

When provider_reference is present, duplicate provider adjustment evidence for
the same Payment must be prevented.

### Identity Semantics

operation_key identifies a CodeInteX-initiated financial command such as a
refund.

provider_reference identifies provider-originated or provider-recorded
financial adjustment evidence when such an identity exists.

A staff-initiated refund must record initiated_by and an operational reason.

Provider-originated adjustments may leave initiated_by empty because the
provider evidence is the origin of the financial fact.

CodeInteX must not invent a fake provider identity when none is supplied.

### Aggregate Refund Rule

Full refund is an aggregate financial outcome.

It is not defined as:

    one FinancialAdjustment.amount == Payment.amount

Instead, under transaction protection:

    sum(CONFIRMED REFUND amounts)

determines the confirmed refunded amount.

Confirmed refund total must never exceed the successfully acquired Payment
amount.

When cumulative confirmed refund reaches the full acquired amount, the
affected purchase entitlement may be revoked according to Commercial Access
Policy V1.

A partial confirmed refund does not automatically revoke Course access.

## PaymentIntegrityCase

### Responsibility

PaymentIntegrityCase records an operational anomaly requiring explicit
reconciliation or authorized business resolution.

It is not Payment financial state.

### Reasons

Minimum V1 reasons:

    AMOUNT_MISMATCH
    CURRENCY_MISMATCH
    PROVIDER_IDENTITY_MISMATCH
    LATE_PAYMENT_CLOSED_ORDER
    MULTIPLE_SUCCESSFUL_PAYMENTS
    PARTIAL_CHARGEBACK
    FULFILLMENT_INCONSISTENCY

### States

    OPEN
    RESOLVED

### Fields

    id
        UUID primary key

    order
        nullable ForeignKey -> Order
        on_delete = PROTECT

    payment
        nullable ForeignKey -> Payment
        on_delete = PROTECT

    provider_event
        nullable ForeignKey -> ProviderEvent
        on_delete = PROTECT

    case_key
        CharField(unique=True)

    reason
        CharField with V1 reason values

    status
        CharField with integrity-case states

    resolution
        CharField(blank=True)

    resolution_reason
        TextField(blank=True)

    opened_at
        DateTimeField(auto_now_add=True)

    resolved_at
        DateTimeField(null=True, blank=True)

    resolved_by
        nullable ForeignKey -> settings.AUTH_USER_MODEL
        on_delete = PROTECT

### Database Constraints

PaymentIntegrityCase reason must be database-constrained to the accepted V1
reason values.

PaymentIntegrityCase status must be database-constrained to:

    OPEN
    RESOLVED

At least one correlation scope must exist:

    order
    payment
    provider_event

case_key provides stable CodeInteX-owned idempotency for anomaly creation.

Repeated detection of the same anomaly must resolve to the same logical
integrity case rather than create unbounded duplicate OPEN cases.

### Resolution Outcomes

Possible V1 business decisions may include:

    FULFILL
    REFUND
    KEEP_ACCESS
    REVOKE_PURCHASE_ACCESS
    NO_ACTION

Resolution is executed through an idempotent transactional service.

Operators must not resolve cases through destructive ad-hoc database edits.

## CourseEntitlement

### Responsibility

CourseEntitlement is an independent learner access grant for a Course.

It is not Payment state and is not Enrollment.

### Sources

    PURCHASE
    SCHOLARSHIP
    ADMIN_GRANT

### States

    ACTIVE
    REVOKED

### Fields

    id
        UUID primary key

    learner
        ForeignKey -> settings.AUTH_USER_MODEL
        on_delete = PROTECT

    course
        ForeignKey -> learning.Course
        on_delete = PROTECT

    source
        CharField with entitlement sources

    status
        CharField with entitlement states

    order
        nullable ForeignKey -> Order
        on_delete = PROTECT

    granted_at
        DateTimeField(auto_now_add=True)

    granted_by
        nullable ForeignKey -> settings.AUTH_USER_MODEL
        on_delete = PROTECT
        distinct related_name required

    grant_reason
        TextField(blank=True)

    revoked_at
        DateTimeField(null=True, blank=True)

    revoked_by
        nullable ForeignKey -> settings.AUTH_USER_MODEL
        on_delete = PROTECT
        distinct related_name required

    revocation_reason
        TextField(blank=True)

### Database Constraints

CourseEntitlement source must be database-constrained to:

    PURCHASE
    SCHOLARSHIP
    ADMIN_GRANT

CourseEntitlement status must be database-constrained to:

    ACTIVE
    REVOKED

At most one CourseEntitlement may reference a given Order.

Purchase source requires:

    order IS NOT NULL

Non-purchase sources require:

    order IS NULL

For V1, at most one ACTIVE PURCHASE entitlement may exist for:

    learner + course

This constraint does not prevent an ACTIVE SCHOLARSHIP or ADMIN_GRANT from
coexisting with purchase history.

It also permits a future repurchase after the previous purchase entitlement
has been REVOKED.

### Effective Access

Effective access exists when:

    at least one ACTIVE CourseEntitlement
    exists for learner + course

Revoking one grant must not revoke another independent ACTIVE grant.

### Exceptional Access Restoration

For V1, a reversed chargeback or similar exceptional restoration does not
mutate historical revocation away.

If access must be restored manually, an authorized audited ADMIN_GRANT may be
created through PaymentIntegrityCase resolution.

A generalized entitlement-event ledger is intentionally deferred.

## Enrollment Fulfillment

CourseEntitlement targets Course.

Enrollment continues to target CourseRelease.

Successful V1 purchase fulfillment performs:

    verified successful Payment
        ->
    Order FULFILLED
        +
    PURCHASE CourseEntitlement ACTIVE
        +
    Enrollment for current published CourseRelease

Existing Enrollment uniqueness remains owned by learning:

    learner + course_release

Publishing a new CourseRelease never silently migrates an existing Enrollment.

## Transaction Boundaries

### Create Order

Within transaction.atomic():

    lock learner row

    find any existing OPEN Order for learner + Course

    if an OPEN Order is already commercially expired:
        transition it to EXPIRED inside the same transaction

    re-check ACTIVE purchase entitlement
    re-check remaining OPEN Order
    resolve trusted ACTIVE CourseOffer
    create immutable Order snapshot

The conditional unique constraint remains the final database race barrier.

### Create Provider Payment

Within a short local transaction:

    lock Order
    verify Order is OPEN
    verify no SUCCEEDED Payment already exists for the Order
    verify no externally payable nonterminal Payment exists
    create Payment with stable operation_key and merchant_reference
    commit

Only after local commit:

    call provider

Do not hold a database transaction open while waiting on provider network I/O.

On ambiguous provider response:

    retain same Payment
    retry/reconcile same logical operation

Do not blindly create another Payment.

### Ingest Provider Event

Webhook request:

    authenticate provider request
    validate minimum structure
    persist ProviderEvent
    commit
    return provider-appropriate success promptly

Business fulfillment is not required to complete inside the webhook request.

### Process Payment Observation

Processor/reconciliation:

    identify Payment
    normalize authoritative provider observation
    enter short transaction
    lock required Payment / Order / learner scope
    apply valid state transition
    fulfill or create integrity case
    commit

The same business transition logic is used by:

    webhook processing
    reconciliation

### Fulfill Purchase

Within transaction.atomic():

    lock learner
    lock Order
    lock successful Payment as needed

    re-check:
        Order eligibility
        successful Payment
        no duplicate purchase entitlement
        current effective purchase state

    create/get purchase CourseEntitlement

    resolve current published CourseRelease

    create/get Enrollment

    transition Order -> FULFILLED

The operation must be safely retryable.

### Apply Refund

Within transaction.atomic():

    lock Payment
    lock relevant purchase entitlement / Order as needed
    verify remaining refundable amount
    create or confirm idempotent FinancialAdjustment
    recompute cumulative confirmed refund

    if cumulative refund is full:
        revoke only the affected purchase entitlement

Independent ACTIVE entitlements remain untouched.

## Database Invariant Summary

Database-enforced where feasible:

    accepted state/kind/source values for correctness-sensitive enums

    one ACTIVE CourseOffer per Course + currency

    one OPEN ordinary Order per learner + Course

    Order monetary arithmetic is internally consistent

    V1 paid Order total is greater than zero

    one nonterminal externally payable Payment per Order

    unique Payment operation_key

    unique Payment merchant_reference

    unique provider transaction identity when present

    unique provider event identity when present

    positive Payment amount

    positive FinancialAdjustment amount

    unique FinancialAdjustment operation identity when present

    no duplicate provider adjustment identity when present

    idempotent PaymentIntegrityCase identity

    PaymentIntegrityCase has at least one correlation scope

    at most one purchase CourseEntitlement per Order

    at most one ACTIVE PURCHASE entitlement per learner + Course

    purchase entitlement source/order consistency

    existing learning Enrollment uniqueness

Service-enforced:

    Order commercial values come from trusted server state

    Payment amount/currency match Order

    ProviderEvent evidence maps to the correct Payment

    sellable Course has a published CourseRelease

    CourseEntitlement learner/course match the fulfilled Order

    entitlement + Enrollment + Order fulfillment are locally atomic

    cumulative refunds do not exceed acquired amount

    full aggregate refund revokes only affected purchase entitlement

    a verified successful Payment blocks ordinary creation of another
    provider checkout for the same Order

    duplicate successful payments do not duplicate access

    staff-initiated financial adjustments retain actor/reason audit evidence

    manual integrity-case resolution is authorized and idempotent

## PostgreSQL Correctness Requirement

Production uses PostgreSQL.

Concurrency-sensitive Commerce correctness must therefore be acceptance-tested
against PostgreSQL.

SQLite remains useful for fast local and ordinary regression tests but is not
evidence that row-locking behavior is correct.

PostgreSQL-backed TransactionTestCase coverage is required for locking and
race-sensitive scenarios.

## PostgreSQL Acceptance-Test Matrix

The implementation must prove at minimum:

### Order Concurrency

Two concurrent requests for the same learner + Course:

    result:
        at most one OPEN ordinary purchase Order

### Entitlement vs Order Race

Concurrent purchase fulfillment and new Order creation:

    result:
        no accidental payable duplicate purchase

### Payment Concurrency

Two concurrent checkout-creation requests for one Order:

    result:
        at most one externally payable nonterminal Payment

### Ambiguous Checkout Creation

Provider request outcome is unknown:

    result:
        no replacement Payment is created until the original operation is
        reconciled

### Duplicate Fulfillment

Same verified successful Payment processed multiple times:

    result:
        one purchase entitlement
        one Enrollment per learner/release
        one FULFILLED Order

### Competing Success

Two valid Payment transactions unexpectedly succeed:

    result:
        financial facts preserved
        one purchase entitlement
        no duplicate Enrollment
        integrity case created

### Worker Claiming

Multiple processors compete for ProviderEvents:

    result:
        no contradictory business transition
        processing remains retryable after worker failure

### Refund Concurrency

Concurrent refund operations:

    result:
        confirmed refund aggregate never exceeds acquired amount
        duplicate refund command does not create duplicate financial movement

## Tests Before Provider Adapter

Implementation sequence:

    create commerce app
        ->
    model/constraint tests
        ->
    PostgreSQL transaction/concurrency acceptance tests
        ->
    models and migration
        ->
    provider-neutral transactional services
        ->
    regression suite
        ->
    only then payment-provider adapter

Midtrans SDK, webhook endpoint wiring, and checkout UI must not define the
domain schema.

## Explicit Non-Goals

V1 does not introduce:

    generic Product
    SKU
    Invoice
    accounting ledger
    subscription plan
    recurring billing
    bundle
    B2B seat/license
    tax engine
    wallet
    event bus
    Kafka
    RabbitMQ
    microservices
    generic entitlement framework

These require separate evidence before adoption.

## Deferred Decisions

The following do not block the V1 schema architecture:

- exact CharField lengths where no external contract requires a specific size;
- exact Django enum class names;
- exact index names;
- exact PostgreSQL lock syntax used by each service;
- exact worker runtime;
- exact reconciliation schedule/backoff;
- exact ProviderEvent retention duration;
- exact operator UI;
- exact Midtrans field/status mapping;
- future account anonymization workflow.

These implementation decisions may evolve without changing the schema
responsibilities and invariants defined here.

## Acceptance Criteria for This Proposal

This schema may move from Proposed to Accepted only if review confirms:

1. every accepted Commerce/Payment invariant has a clear persistence or
   service enforcement point;
2. no model exists solely for hypothetical future functionality;
3. no provider-specific vocabulary leaks into core Learning or Access
   semantics;
4. race-sensitive invariants have PostgreSQL-backed test plans;
5. destructive deletion cannot silently erase commercial evidence;
6. ordinary purchase, retries, duplicate events, double payment, refunds,
   grants, revocation, and new CourseRelease behavior can be represented
   without contradictory state.
