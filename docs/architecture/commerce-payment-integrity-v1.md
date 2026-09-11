# Commerce & Payment Integrity Spec V1

Status: Accepted
Date: 2026-09-11

## Purpose

Define correctness, security, reliability, reconciliation, and audit
requirements for CodeInteX one-time course purchases before Django commerce
models or a payment-provider adapter are implemented.

This specification is provider-portable.

It defines CodeInteX invariants rather than Midtrans-specific behavior.

## Scope

V1 covers:

- one-time Course purchases;
- Order lifecycle;
- payment attempts;
- provider event ingestion;
- payment verification;
- fulfillment;
- CourseEntitlement grants;
- Enrollment provisioning;
- reconciliation;
- refund/dispute integrity principles;
- concurrency and idempotency requirements.

Subscription, bundles, B2B licensing, and international tax semantics remain
outside V1.

## Core Separation

    Commerce:
        Order

    Payments:
        Payment
        ProviderEvent
        Refund / Dispute facts

    Access:
        CourseEntitlement

    Learning:
        Enrollment
        LessonProgress

Payment is not entitlement.

Entitlement is not enrollment.

Provider state is not CodeInteX domain state.

## Invariant 1: Order Is a Server-Authoritative Immutable Commercial Snapshot

Once checkout has been created, commercially material Order fields must not be
silently recalculated from mutable catalog data.

The Order records the trusted purchase intent needed to verify and fulfill the
transaction, including at minimum:

- authenticated learner identity;
- Course identity;
- amount;
- currency;
- applicable commercial pricing snapshot;
- creation time;
- validity/expiry information.

Commercially authoritative values must be derived or validated server-side.

The browser must not be authoritative for:

- learner identity;
- price or subtotal;
- currency;
- discount amount;
- entitlement target;
- payment success.

A client may submit identifiers or inputs such as Course identity or coupon
code, but CodeInteX must resolve and validate their commercial meaning from
trusted server-side state.

Access to create, inspect, retry, cancel, or otherwise act on an Order must be
authorized against the authenticated principal and the Order owner or an
explicitly authorized staff capability.

A later change to catalog price must not change the expected amount of an
already-created Order.

## Invariant 2: Sellability Is Checked Before Checkout

A new checkout must not be created unless the Course is commercially sellable
and has a published CourseRelease that can be provisioned.

A price or catalog change after checkout creation does not invalidate an
otherwise valid Order unless an explicit commercial rule says so.

## Invariant 3: One Order May Have Multiple Provider Payment Transactions

Relationship:

    Order 1 ---- * Payment

A CodeInteX Payment represents one provider transaction or checkout intent
created for an Order.

It does not necessarily represent every lower-level authorization, bank,
card, or payment-method attempt performed inside a provider checkout.

A provider may expose multiple underlying attempts beneath one provider
checkout identity. Those observations remain provider/integration evidence
unless CodeInteX has a concrete reason to model them separately.

The CodeInteX Order identity and provider Payment identity are separate.

Each newly created provider transaction must receive a stable provider-facing
merchant reference associated with that Payment rather than reusing the
CodeInteX Order identity as though they were the same concept.

A provider may support reopening or retrying an existing checkout/token.
Such behavior remains the same CodeInteX Payment when it refers to the same
provider transaction/checkout identity.

A failed, cancelled, or expired Payment does not by itself fail the Order.

For V1, an Order must have at most one externally payable nonterminal Payment
at a time.

A new Payment may be created only after the previous provider checkout is
terminal or has been explicitly made non-payable.

## Invariant 4: Order State Represents Commercial Fulfillment

Minimum V1 Order states:

    OPEN
    FULFILLED
    CANCELLED
    EXPIRED

FULFILLED means CodeInteX has successfully applied the commercial purchase,
including the required access-side effects.

Order state must not be used as a substitute for detailed financial history.

## Invariant 5: Payment State Represents a Payment Attempt

Minimum acquisition states for V1:

    CREATED
    PENDING
    SUCCEEDED
    FAILED
    CANCELLED
    EXPIRED

CREATED exists before or during provider checkout creation so that provider
API retries can be correlated safely.

SUCCEEDED means CodeInteX has verified that the payment attempt successfully
acquired funds according to the applicable provider semantics at a point in
time.

SUCCEEDED is a historical acquisition fact, not a claim that the merchant's
net financial position can never change.

Later reversal, refund, partial refund, dispute, or chargeback facts must not
erase the historical observation that a successful acquisition was previously
verified.

A stale or lower-authority event must never blindly overwrite a more reliable
observation.

Where a provider explicitly supports later reversal of an earlier success,
that later financial fact must be retained and processed according to the
provider lifecycle and CodeInteX access policy.

The detailed representation of post-success financial adjustments remains a
separate concern from the basic Payment acquisition state.

## Invariant 6: Browser State Is Never Payment Authority

A browser redirect, success page, query parameter, JavaScript callback, or
client-supplied status must never grant CourseEntitlement.

Browser UX may report that payment is being checked.

Only trusted server-side payment verification can authorize fulfillment.

## Invariant 7: Payment Success Requires Server-Side Verification

Before a Payment becomes SUCCEEDED, CodeInteX must verify all applicable
provider and Order facts, including:

- provider authenticity;
- expected merchant/account context;
- provider transaction/reference identity;
- CodeInteX Order correlation;
- amount;
- currency;
- provider success semantics;
- applicable fraud/security result.

Mismatch must fail closed.

A mismatch must not create CourseEntitlement.

Verification or integrity anomalies are not financial Payment states.

Conditions such as amount mismatch, currency mismatch, unexpected provider
reference, late payment, and double payment must enter a separate
review/reconciliation workflow while preserving the provider financial facts.

The exact review-case schema remains an implementation decision.

## Invariant 8: Webhook Ingestion and Business Processing Are Separated

Webhook ingestion should perform only the work required to:

1. receive the request;
2. verify the provider-specific authenticity mechanism;
3. durably record the authenticated event or observation;
4. commit that record;
5. return the appropriate successful response promptly.

Complex fulfillment must not be required to complete before acknowledging a
durably accepted provider event.

If durable persistence fails, CodeInteX must not acknowledge successful
receipt merely to silence provider retries.

The execution mechanism for asynchronous processing is an implementation
choice and is not locked by this specification.

## Invariant 9: Provider Events Are Durable and Replay-Safe

Authenticated provider events must have sufficient durable identity and audit
metadata to support:

- duplicate delivery;
- retries;
- delayed delivery;
- out-of-order delivery;
- processor crashes;
- reconciliation.

Where a provider supplies a stable event ID, it should be retained.

Where no provider event ID exists, provider-specific deduplication may use an
appropriate stable identity or fingerprint.

Correctness must not depend exclusively on webhook deduplication.

Reprocessing the same business observation must itself be safe.

## Invariant 10: CodeInteX Owns Idempotency and Ambiguous-Outcome Recovery

Provider idempotency features are useful but are not the CodeInteX correctness
boundary.

CodeInteX must enforce its own idempotency using stable internal identities,
database constraints, transaction boundaries, and safe transition rules.

Outbound provider operations that can create or move money must have a stable
CodeInteX operation identity.

If a provider request has an ambiguous outcome, for example because the
request timed out after transmission, CodeInteX must not create a replacement
Payment merely because the response was lost.

The system must first retry or reconcile the same logical provider operation
using the same stable operation/provider identity where supported.

Only when the previous operation is known not to have created an externally
payable transaction may CodeInteX intentionally create a new Payment.

At minimum:

- one provider transaction must not become multiple CodeInteX Payments
  improperly;
- one Order must not generate duplicate purchase entitlement grants;
- one learner/release pair must not receive duplicate Enrollment records;
- replaying fulfillment must produce the same final business result;
- retrying an ambiguously completed outbound operation must not create an
  unintended second chargeable transaction.

## Invariant 11: Fulfillment Is Atomic Locally

For an eligible OPEN Order with a newly verified successful Payment, the local
business operation must atomically achieve the required final state:

    verified Payment
        ->
    Order FULFILLED
        +
    purchase CourseEntitlement ACTIVE
        +
    Enrollment provisioned for the applicable published CourseRelease

If the local transaction fails, partial local fulfillment must not be left as
the accepted final state.

The operation must be safely retryable.

External provider network calls should not require holding a long-running
database transaction open.

## Invariant 12: Entitlement Grants Are Independently Auditable

A learner and Course may have more than one independent entitlement grant.

Examples include:

    PURCHASE
    SCHOLARSHIP
    ADMIN_GRANT

Effective Course access exists when at least one applicable
CourseEntitlement is ACTIVE.

Revoking one grant must not revoke another independent ACTIVE grant.

A purchase entitlement must have a stable source identity so replaying the
same Order cannot generate duplicate grants.

## Invariant 13: Learning History Is Not Commercial State

Entitlement revocation must not delete:

    Enrollment
    LessonProgress
    historical learning records

Commercial access and historical learning evidence remain separate.

## Invariant 14: Late Payment Does Not Automatically Mean Fulfillment

If authoritative verification proves that money was received after an Order
was already CANCELLED or EXPIRED:

    Payment acquisition fact = SUCCEEDED

but CodeInteX must not automatically assume:

    Order = FULFILLED
    Entitlement = ACTIVE

A closed Order must not be silently reopened by a webhook.

The condition must enter explicit reconciliation/review.

Resolution may fulfill the original commercial promise when still valid and
safe, or may refund/reverse the financial receipt where fulfillment is no
longer appropriate.

The financial history must always be preserved.

## Invariant 15: Multiple Successful Payments for One Order Are an Anomaly

If one Order has already been fulfilled and another independent Payment
attempt for that same Order is later verified as SUCCEEDED:

- no second purchase entitlement is created;
- no duplicate Enrollment is created;
- the additional financial receipt is preserved;
- the condition is surfaced for reconciliation;
- any refund decision is handled explicitly.

The system must never convert a double payment into double access silently.

## Invariant 16: Reconciliation Uses the Same Business Rules

Webhook processing is the fast event path.

Provider status lookup is the reconciliation path.

Both must converge through the same payment-observation and state-transition
logic rather than implementing independent business rules.

Reconciliation must be able to recover cases such as:

    provider received money
    webhook missing/delayed
    local Payment remains PENDING

## Invariant 17: Concurrency Must Not Break Purchase or Financial Integrity

Concurrent Order creation, checkout creation, webhook delivery,
reconciliation, browser polling, or fulfillment must not create contradictory
business state.

For the V1 one-time Course purchase scope, CodeInteX must prevent more than
one ordinary externally payable OPEN purchase Order for the same learner and
Course from being created concurrently.

Order creation must re-check, under an appropriate concurrency boundary:

- whether an ACTIVE purchase entitlement already exists;
- whether another payable OPEN purchase Order already exists.

Fulfillment must also re-check purchase state under concurrency protection.

If two independently valid payments nevertheless succeed for competing
Orders before either flow observes the other:

- both successful financial facts are preserved;
- no second purchase entitlement is created;
- no duplicate Enrollment is created;
- the additional payment enters integrity/reconciliation handling.

Implementation must serialize or otherwise protect conflicting state changes
using appropriate database transactions, locking, and uniqueness mechanisms.

The exact Django/PostgreSQL mechanism remains an implementation decision.

## Invariant 18: Existing Purchase Access Prevents Accidental Repurchase

Before opening a new ordinary purchase flow, CodeInteX must check whether the
learner already has an ACTIVE purchase entitlement for the same Course.

An existing ACTIVE purchase entitlement must prevent an accidental duplicate
purchase of the same V1 course product.

A non-purchase grant such as SCHOLARSHIP or ADMIN_GRANT does not automatically
become a purchase record and does not erase the distinction between granted
and purchased access.

If a valid Order was created before another independent entitlement was
granted, a later verified payment for that Order must still be reconciled
according to the Order's commercial history rather than silently discarded.

## Invariant 19: Manual Resolution Is Authorized and Auditable

Manual resolution of a payment integrity anomaly must require explicit staff
authorization.

A manual action must record at minimum:

    actor
    action
    reason
    timestamp
    affected Order/Payment
    resulting business decision

Operators must not resolve payment anomalies by ad-hoc destructive database
editing.

The exact Django permission names and admin interface are implementation
choices.

## Operational Signals Required

The system must make the following conditions observable:

    authenticated event processing failure
    provider/local status mismatch
    amount or currency mismatch
    Payment stuck in PENDING
    verified Payment without fulfilled eligible Order
    multiple successful Payments for one Order
    failed fulfillment retry
    reconciliation backlog

Exact observability tooling is not locked by this specification.

## Failure-Mode Acceptance Matrix

The implementation must eventually prove at least these cases:

| Failure mode | Required result |
| --- | --- |
| Duplicate webhook | No duplicate financial or access side effect |
| Out-of-order webhook | No state regression; authoritative status can reconcile |
| Lost webhook | Reconciliation can recover actual payment state |
| Invalid signature/authenticity | No payment or entitlement transition |
| Browser-forged success | No entitlement |
| Amount mismatch | Fail closed; review/reconciliation |
| Currency mismatch | Fail closed; review/reconciliation |
| Processor crash after durable event | Event can be processed again safely |
| Local fulfillment transaction failure | No accepted partial fulfillment; retry safe |
| Two simultaneous success notifications | One fulfillment only |
| Two payment attempts both succeed | One entitlement; second receipt flagged |
| Payment succeeds after Order expiry | Financial success retained; no blind fulfillment |
| Catalog price changes after checkout | Existing Order verifies against its snapshot |
| Entitlement later revoked | Learning history remains intact |
| Duplicate fulfillment invocation | Same final state, no duplicate grant/enrollment |

## Security Verification Baseline

Applicable payment and commerce controls should be verified against OWASP ASVS
5.0 Level 2 as the V1 application-security baseline, with stronger controls
where threat analysis requires them.

This does not replace payment-provider requirements, PCI obligations, or
applicable law.

## Explicit Non-Goals

V1 does not introduce:

- microservices;
- Kafka;
- a generic event platform;
- a universal payment framework;
- subscription billing;
- bundle licensing;
- B2B seat allocation;
- international tax engines.

The architecture must preserve room for those future requirements without
implementing them prematurely.

## Invariant 20: ProviderEvent Is a Durable Inbox Record

An authenticated provider notification must be durably represented before
CodeInteX acknowledges successful receipt.

ProviderEvent is the V1 durable inbox concept.

It is integration evidence, not a Course, access, or learning-domain object.

A ProviderEvent must have its own CodeInteX identity and enough information
to correlate the provider observation with the relevant Payment attempt.

At minimum, durable evidence must preserve the applicable provider facts
needed for:

- provider identification;
- provider transaction/reference correlation;
- CodeInteX Payment correlation where known;
- provider transaction status or event type;
- provider occurrence time where supplied;
- CodeInteX receipt time;
- amount and currency where relevant;
- authenticity-verification evidence or method;
- a stable payload/event digest or provider event identity where useful;
- processing outcome and audit timestamps.

Exact Django field names remain an implementation decision.

Correctness must not depend on ProviderEvent deduplication alone.

The downstream payment-observation processor must remain idempotent even if
equivalent ProviderEvents are processed more than once.

## Invariant 21: Webhook Data Is Minimized

CodeInteX must not persist an entire provider webhook payload indefinitely
merely because the provider sent it.

Provider notifications may contain customer, payment-method, or other
privacy-sensitive data that is unnecessary for CodeInteX payment integrity.

V1 must persist an explicit allow-list of business and audit evidence required
for verification, reconciliation, support, and incident investigation.

Fields such as customer contact details, masked card information, provider
signatures, and other provider-specific data must not be retained unless
there is a documented operational, security, accounting, or legal need.

Where a provider requires signature verification over the original raw body,
verification occurs before transformation.

Successful verification does not by itself require indefinite raw-body
retention.

If temporary raw-event retention is later justified for incident response, it
must have explicit access control, protection, and retention/deletion policy.

The exact retention duration remains an operational/privacy decision and is
not invented by this specification.

## Invariant 22: Webhook Acknowledgement Follows Durable Acceptance

The provider webhook endpoint must not perform full commercial fulfillment
before acknowledging the notification.

The normal sequence is:

    authenticate provider notification
        ->
    validate enough structure to identify the observation
        ->
    durably persist ProviderEvent
        ->
    commit
        ->
    return provider-appropriate success response promptly

If the same authenticated notification has already been durably represented,
the endpoint may acknowledge it successfully without repeating business side
effects.

If durable persistence fails, the endpoint must not falsely acknowledge
successful durable receipt.

Invalid or unauthenticated notifications must never enter the trusted payment
processing path.

Exact HTTP status codes for invalid or failed requests are provider-adapter
behavior because provider retry semantics differ.

## Invariant 23: ProviderEvent Processing Is Separate and Retryable

Business processing occurs outside the webhook request transaction.

A processor claims durable unprocessed ProviderEvents and converts provider
facts into the same CodeInteX payment-observation logic used by
reconciliation.

The processor must be safe under:

- process crash;
- duplicate execution;
- concurrent workers;
- delayed events;
- out-of-order events;
- provider API timeout;
- transient database failure.

Processing failure must leave durable evidence that can be retried.

A successfully ingested event must not disappear merely because downstream
processing failed.

For V1, PostgreSQL/Django may provide the durable inbox and work-claiming
mechanism.

A separate broker or generic event platform is not required.

The exact worker runtime is an implementation choice. It may initially be a
supervised Django worker/management process and may later be replaced without
changing the Commerce or Access domain contracts.

## Invariant 24: Reconciliation Is Provider-Aware, Not Hard-Coded Into Domain

Reconciliation policy must account for provider lifecycle and expected
notification timing without placing provider-specific timing constants in the
Commerce domain.

Reconciliation must be possible at least when:

    a Payment remains nonterminal beyond its expected provider update window;
    CodeInteX is about to treat a Payment as locally expired or failed;
    an operator explicitly requests reconciliation;
    a learner reports that funds were deducted but access was not granted;
    an integrity anomaly requires authoritative provider status.

Provider adapters may expose or configure suitable operational timing for
their provider.

The exact cadence and retry/backoff values remain operational configuration,
not immutable domain semantics.

Reconciliation and ProviderEvent processing must converge through the same
payment-observation/state-transition service.

## Invariant 25: Processing State Is Not Financial State

ProviderEvent processing lifecycle and Payment financial lifecycle are
separate.

Conceptually, ProviderEvent processing may need states equivalent to:

    RECEIVED
    PROCESSING
    PROCESSED
    FAILED

These states describe CodeInteX processing work.

They do not describe whether money was paid.

Likewise, a payment integrity/review case describes an operational anomaly,
not a substitute Payment acquisition status.

Exact model names and processing-state representation remain implementation
choices.

## Invariant 26: Post-Success Financial Adjustments Are Separate Facts

A successful Payment acquisition must not be rewritten merely because a
subsequent financial event changes the merchant's economic position.

Post-success financial adjustments include at least the conceptual categories:

    REFUND
    REVERSAL
    CHARGEBACK

A financial adjustment belongs to a specific Payment and preserves:

- its own CodeInteX identity;
- adjustment type;
- amount;
- currency;
- provider identity/reference where available;
- provider status or confirmation evidence;
- occurrence/request/confirmation timestamps as applicable;
- reason or provider explanation where operationally necessary.

Exact Django model and field names remain implementation decisions.

Provider-specific statuses may be richer than these CodeInteX concepts and
remain available as integration evidence where needed.

## Invariant 27: Refund Operations Are Independently Idempotent

A merchant-initiated refund is a financial command distinct from the original
Payment.

Each logical refund operation must have a stable CodeInteX identity.

Retrying the same refund must reuse that logical identity and must not create
another refund merely because an API request timed out or its response was
lost.

Creating an additional refund is a new financial operation with a new
identity.

A refund must fail closed if:

- the Payment has not been verified as successfully acquired;
- currency does not match the original Payment;
- requested amount is invalid;
- the requested refund would exceed the remaining refundable amount;
- provider state does not allow the requested operation.

Provider-specific idempotency keys may implement part of this behavior but
do not replace CodeInteX-owned idempotency.

## Invariant 28: Access Effects Depend on Confirmed Economic Outcome

Financial adjustment recording and Course access are separate concerns.

For V1:

    confirmed partial refund
        -> purchase entitlement remains ACTIVE

    confirmed full refund
        -> purchase entitlement is REVOKED

    confirmed partial chargeback
        -> adjustment is recorded
        -> integrity review is required
        -> no automatic access revocation

    confirmed full chargeback
        -> purchase entitlement is REVOKED

    confirmed full provider reversal
        -> purchase entitlement is REVOKED

A provider request or provisional status alone must not trigger irreversible
access consequences when provider semantics require later confirmation.

Revocation affects only the entitlement grant produced by the affected
purchase.

Another independent ACTIVE entitlement for the same learner and Course
continues to provide effective access.

Learning history remains intact.

## Invariant 29: Financial Restoration Does Not Erase Revocation History

A later provider event may reverse an earlier chargeback or other negative
financial adjustment and restore the merchant's funds.

CodeInteX must not erase the historical adjustment or historical entitlement
revocation.

Any decision to restore purchase access must be explicit, idempotent, and
auditable.

Access restoration may create a new entitlement grant or equivalent
append-only access decision rather than mutating history to pretend the
revocation never occurred.

The exact restoration representation remains an implementation decision.

## Invariant 30: PaymentIntegrityCase Is Operational State

An integrity/review case is not a Payment financial status.

A PaymentIntegrityCase concept is used when financial facts and expected
commercial state require investigation or explicit resolution.

Minimum V1 reason categories must cover:

    AMOUNT_MISMATCH
    CURRENCY_MISMATCH
    PROVIDER_IDENTITY_MISMATCH
    LATE_PAYMENT_CLOSED_ORDER
    MULTIPLE_SUCCESSFUL_PAYMENTS
    PARTIAL_CHARGEBACK
    FULFILLMENT_INCONSISTENCY

Additional provider-specific evidence may be attached without creating
provider-specific Commerce semantics.

The minimum lifecycle is conceptually:

    OPEN
      ->
    RESOLVED

The exact internal workflow may later add states if operational evidence
requires them.

Creating an integrity case must not destroy or rewrite the underlying
Payment, ProviderEvent, Order, entitlement, or financial-adjustment facts.

## Invariant 31: Integrity Cases Fail Closed Where Access Is Not Yet Granted

When an integrity anomaly is detected before fulfillment, CodeInteX must not
grant access until the anomaly is resolved or authoritative evidence proves
the purchase valid.

Examples include:

    amount mismatch
    currency mismatch
    unexpected provider identity
    late successful payment against a closed Order

For anomalies discovered after valid fulfillment, CodeInteX preserves the
existing financial and access history and applies the explicit resolution
appropriate to that anomaly.

## Invariant 32: Manual Resolution Is an Explicit Business Decision

Resolution of a PaymentIntegrityCase must produce an auditable decision rather
than ad-hoc data mutation.

A resolution records at minimum:

- authorized actor;
- resolved case;
- decision;
- reason;
- timestamp;
- resulting financial/access action where applicable.

Possible business outcomes may include:

    FULFILL
    REFUND
    KEEP_ACCESS
    REVOKE_PURCHASE_ACCESS
    NO_ACTION

The available outcomes depend on case reason and actual provider evidence.

Resolution must be idempotent.

A repeated operator submission must not repeat fulfillment, refund, or
entitlement side effects.

## Invariant 33: Financial Adjustment History Is Reconstructable

CodeInteX must be able to reconstruct the material financial history of a
Payment from durable facts rather than a single mutable status string.

At minimum the audit trail must answer:

- whether acquisition ever succeeded;
- which refunds occurred and for what amounts;
- whether a reversal or chargeback occurred;
- which provider evidence established those facts;
- which access decisions resulted;
- which manual decisions, if any, were made.

This requirement does not imply that CodeInteX is an accounting ledger or
general-purpose financial system.

It requires only sufficient integrity and audit evidence for the commercial
operations CodeInteX actually performs.

## Deferred Implementation Decisions

The architecture is accepted.

The following remain implementation or operational decisions and may evolve
without reopening this architecture, provided the accepted invariants remain
true:

- exact ProviderEvent evidence retention period, derived from privacy,
  accounting, support, security, and applicable legal requirements;
- exact Django model and field names;
- exact PostgreSQL locking and constraint mechanisms;
- exact worker runtime and deployment topology;
- exact reconciliation intervals and retry/backoff configuration;
- exact operator UI for integrity-case resolution;
- exact provider-specific Midtrans status and event mapping.

These decisions must not weaken the accepted architecture.

In particular:

- commercially authoritative Order values remain server-controlled;
- CodeInteX Order identity and provider Payment identity remain separate;
- only one externally payable nonterminal Payment exists per Order in V1;
- ordinary duplicate payable purchase Orders for the same learner and Course
  are prevented under concurrency;
- ambiguous provider-operation outcomes are reconciled before a new
  chargeable Payment is intentionally created;
- Payment acquisition history and subsequent financial adjustments remain
  separate facts;
- review/reconciliation state remains separate from financial state;
- authenticated provider notifications enter a durable inbox before
  acknowledgement;
- webhook processing remains retryable and idempotent;
- reconciliation and webhook processing converge on the same business logic;
- independent ACTIVE entitlements remain independent;
- manual anomaly resolution remains authorized, idempotent, and auditable.

No payment-provider adapter should be implemented before the minimum Django
Commerce & Access schema, database invariants, and transition tests are
defined from this accepted specification.
