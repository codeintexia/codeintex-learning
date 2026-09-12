# CodeInteX Learning — Development State

Last updated: 2026-09-11
Project: [Yudi] CodeInteX
Repository: codeintexia/codeintex-learning
Branch: rebuild/learner-experience-v1

## Purpose

This file is the canonical handoff snapshot for continuing CodeInteX Learning development across ChatGPT sessions and human/AI contributors.

Use this file together with the ADRs under `docs/architecture/adr/` and the current Git history. If this file conflicts with newer verified repository evidence, newer evidence wins and this file should be updated.

## Current Critical Path

`commercial access policy → commerce/access design → payment MVP → minimum production deploy/hardening`

The learner loop is already functional and should not be expanded before monetization unless a real defect blocks the critical path.

## Verified State

### Backend

- Django 6.1.1
- Wagtail 8.0
- Python 3.13.2
- PostgreSQL is the production canonical transactional database.
- SQLite is local development only.
- Backend test suite: **39/39 passing** as of 2026-09-11.
- `manage.py check`: passing.

### Frontend

- Next.js 16.3.3
- React 19.2.x
- TypeScript 5.9.3
- npm workspaces
- `npm run typecheck`: passing at the latest verified Player/My Learning integration checkpoint.
- Production build had previously passed; rerun before any release checkpoint.

## LOCKED

### Architecture

- CodeInteX Learning is a modular monolith.
- Next.js owns learner-facing web UI.
- Django owns transactional application logic.
- Wagtail is an authoring implementation, not the learner runtime contract.
- Learner-facing APIs are owned under `/api/v1/...`.
- Runtime learner state does not live in Wagtail StreamField.
- `learning/api.py` contains public/content/read-model endpoints.
- `learning/runtime_api.py` contains authenticated transactional/runtime endpoints.
- `learning/auth_api.py` contains session authentication endpoints.
- `learning-ui` must remain backend-agnostic.

### Course Versioning

- `Course` is stable product identity.
- `CourseRelease` is the versioned learner-facing contract.
- Draft releases are editable.
- Published releases are immutable.
- Content changes after publication require a new release.
- Enrollment pins a learner to a specific `CourseRelease`.
- Player content must use the same release as the learner enrollment.
- Publishing a newer release must not silently migrate existing learners.

### Authentication and Security Foundation

- Django session authentication is the current MVP identity authority.
- CSRF remains enabled.
- Unsafe browser requests use CSRF protection.
- No fake/default learner identity.
- No auth token stored in `localStorage`.
- Browser-facing production topology targets same-origin `/api/v1/*`.
- Learner session cookies should remain scoped to the learning host unless a later SSO architecture explicitly changes this.
- Broad wildcard trusted origins and broad cookie domains are not acceptable shortcuts.

### Commerce Portability

- CodeInteX Commerce is provider-portable, not Midtrans-based.
- Payment providers are integration adapters, not domain authorities.
- Provider-specific IDs, tokens, statuses, and vocabulary must remain inside the integration/payment boundary.
- CodeInteX owns its internal Order, Payment, access, and entitlement semantics.
- Indonesian and international payment providers may coexist.
- Historical payments retain their original provider identity; historical records are not rewritten when providers change.
- Learner-facing product code must not depend on a provider-specific checkout component or status model.

### Learner Runtime

- `Enrollment` is authoritative for learner access to a specific release.
- `LessonProgress` is authoritative for completed lessons.
- Progress percentage is derived.
- Lesson completion is idempotent.
- Player persistence is server-authoritative.
- Refresh restores persisted completion/current state.
- My Learning reads real `Enrollment` + `LessonProgress`, not fixtures.
- My Learning keeps one course entry when multiple enrollments exist for the same course, using the latest enrollment.

### Product / Delivery Discipline

- Do not add speculative frameworks, generic `shared/common/core` layers, or public plugin packaging on the current revenue critical path.
- Do not fabricate courses, pricing, testimonials, reviews, or learner personas.
- Prefer simple, reversible implementation choices that preserve stable architectural boundaries.
- Docker files remain parked until production deployment assumptions are locked.

### Commercial Access Policy V1

- One-time purchase grants indefinite access to the purchased Course, unless the entitlement is later revoked.
- CourseEntitlement targets Course rather than a specific CourseRelease.
- Normal future CourseRelease revisions remain available to entitled learners.
- Materially different scope or value proposition is modeled as a new Course/product rather than a disguised revision.
- Enrollment remains pinned to a specific CourseRelease.
- Publishing a new CourseRelease never silently migrates an existing Enrollment.
- Learning history and LessonProgress survive entitlement revocation.
- Free preview does not create a CourseEntitlement.
- Scholarship and administrative grants create real entitlements without fake Payment records.
- Coupons and discounts affect commerce calculations, not learning-access semantics.
- In V1, granting an entitlement provisions an Enrollment to the current published CourseRelease.
- Refund or confirmed chargeback may revoke entitlement without deleting Enrollment or learning progress.

### Commerce & Payment Integrity V1

- Order is a server-authoritative immutable commercial snapshot once checkout is created.
- CodeInteX Order identity and provider Payment identity are separate.
- One Order may have multiple sequential provider Payment transactions.
- Only one externally payable nonterminal Payment may exist per Order in V1.
- Ordinary duplicate payable purchase Orders for the same learner and Course must be prevented under concurrency.
- Browser redirects/callbacks are never payment authority.
- Payment success requires trusted server-side provider verification.
- CodeInteX owns business idempotency and ambiguous-outcome recovery.
- Authenticated provider notifications enter a durable database-backed ProviderEvent inbox before acknowledgement.
- Webhook ingestion is separated from retryable business processing.
- Webhook processing and reconciliation converge through the same payment-observation logic.
- Financial acquisition history is separate from refund, reversal, dispute, and chargeback facts.
- Payment integrity/review workflow is separate from Payment financial state.
- Partial refund does not automatically revoke Course access.
- Confirmed full refund, full chargeback, or full reversal may revoke only the affected purchase entitlement.
- Independent ACTIVE entitlements continue to provide effective Course access.
- Learning history survives commercial-access revocation.
- Manual payment-anomaly resolution must be authorized, idempotent, and auditable.

### Commerce Schema V1

**Implementation state:** Commerce Schema V1 provider-neutral transaction boundaries plus the first Midtrans adapter/workflow bridge are implemented locally. Midtrans coverage includes Snap checkout creation, notification authentication, durable ProviderEvent ingestion, separate event processing, status normalization, reconciliation through the existing observation engine, cumulative refund handling, reversal handling, and partial-chargeback integrity review. The current full default backend suite reports 134 tests: OK, with 7 PostgreSQL-only concurrency tests skipped; all 7 pass separately on PostgreSQL 18.6. Real Midtrans sandbox compatibility remains to be proven.

- V1 introduces one physical Django app: `commerce`.
- `learning` does not depend on `commerce`.
- V1 core models are CourseOffer, Order, Payment, ProviderEvent, FinancialAdjustment, PaymentIntegrityCase, and CourseEntitlement.
- CourseOffer owns server-authoritative Course pricing.
- Order is an immutable commercial snapshot after creation.
- Payment represents a provider transaction / checkout intent.
- ProviderEvent is the durable authenticated notification inbox.
- FinancialAdjustment preserves refund, reversal, and chargeback facts without rewriting Payment acquisition history.
- PaymentIntegrityCase owns payment anomaly/reconciliation workflow.
- CourseEntitlement is independent from Payment and Enrollment.
- PostgreSQL database constraints and transactional services are correctness boundaries for concurrency-sensitive Commerce behavior.
- PostgreSQL-backed TransactionTestCase coverage is required for locking and race-sensitive behavior.
- Production financial/commercial learner references use fail-safe deletion protection in V1; account anonymization/retention workflow remains a separate policy concern.

## PROVISIONAL

- If a learner has multiple enrollments for the same course, the newest enrollment is treated as current.
- Resume semantics are currently the first incomplete lesson, not last-visited lesson.
- The current login page is functional MVP UI, not the final Product Experience System surface.
- Reusable Django/Wagtail package extraction may be valuable later but is not a current implementation target.
- Local Next.js external rewrite is a development same-origin bridge; production routing remains to be finalized.

- Midtrans Snap is the current strong MVP candidate for Indonesian one-time checkout, but is not an architectural dependency.

## OPEN

### Commercial Access Policy V1 — Open Decisions

- Exact refund eligibility and refund window.
- Detailed fraud policy.
- UX and policy for moving from CourseRelease N to N+1.
- Whether multiple release enrollments may be active simultaneously.
- Commercial handling of 100%-discount orders.
- Subscription semantics.
- Bundle semantics.
- B2B seat and license semantics.
- International tax policy.

- Production hosting and reverse-proxy topology.
- Production TLS/proxy trust configuration.
- SSO/OIDC architecture for the wider CodeInteX ecosystem.
- Formal threat model and ASVS-based verification scope.
- Observability and audit-event strategy.
- Backup/restore and disaster recovery verification.
- Accessibility conformance verification.
- Load/performance verification.
- CI/CD and security scanning baseline.
- Public package/open-source/framework extraction.

- Global expansion payment strategy: global PSP vs Merchant of Record vs multi-provider routing.

## PARKED

- `apps/learning-backend/.dockerignore`
- `apps/learning-backend/Dockerfile`
- AI/agent features
- Assessments
- Certificates
- Analytics
- Public Wagtail/Django package extraction
- SWC/RAM worker investigation
- Final login UX polish

## Proven Learner Flow

`Login → Django session → My Learning → Resume → Learning Player → persisted LessonProgress → refresh-safe resume`

Verified behavior includes:

- Browser login succeeds through the same-origin API bridge.
- Django returns and accepts session cookies.
- Enrollment is idempotent.
- Completion is idempotent.
- Progress persists across requests.
- Player restores persisted completion and current lesson after refresh.
- My Learning reflects the same persisted state.
- Release pinning prevents mixing learner progress from one release with content from another.

## Current Backend Test Milestones

- 17 tests: published release immutability.
- 23 tests: runtime persistence models.
- 31 tests: authenticated progress API.
- 36 tests: authentication API.
- 39 tests: My Learning read-model and latest-enrollment behavior.

## Current Workstream Boundary

### Strategy

Revenue first. Avoid non-blocking feature expansion.

### Architecture

Keep domain boundaries stable and implementation choices replaceable.

### Backend

Next milestone: payment/entitlement integration without coupling payment-provider concepts directly into learning-domain core.

### Frontend

Learner loop is sufficient for MVP continuation. Avoid polish unless it blocks conversion, accessibility, or correctness.

### Security

Essential controls must be completed before production payment acceptance; deeper assurance should follow measurable verification criteria rather than labels.

## Next Milestone

Prove the implemented Midtrans adapter against the real Midtrans sandbox: create a checkout using sandbox credentials, complete a controlled payment, verify authenticated notification ingestion and separate processing, and confirm GET Status reconciliation converges to the same local state. Do not enable production payments until the end-to-end learner purchase flow and production launch gate pass.

## Session Handoff Procedure

When starting a new ChatGPT session:

1. Stay inside project `[Yudi] CodeInteX`.
2. State that development continues from branch `rebuild/learner-experience-v1`.
3. Treat this file and ADRs as repository continuity context.
4. Inspect current Git status and recent commits before changing code.
5. Prefer newer repository evidence over this snapshot if they conflict.
6. Update this file when a milestone materially changes decision state.

Suggested opening message:

> Continue CodeInteX Learning from branch `rebuild/learner-experience-v1`. Use `docs/development/STATE.md` and `docs/architecture/adr/` as continuity sources. Inspect current Git status and recent commits before changing anything. Preserve the locked decisions and continue from the current critical path.

## Update Rule

Update this file when any of the following changes:

- critical path;
- a PROVISIONAL decision becomes LOCKED or DEPRECATED;
- an architecture boundary changes;
- a major milestone is proven;
- test baseline changes materially;
- production/deployment assumptions become locked;
- a workstream becomes active or parked.
