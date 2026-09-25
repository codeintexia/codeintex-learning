# CodeInteX Learning — Development State

Last updated: 2026-09-25
Project: [Yudi] CodeInteX
Repository: codeintexia/codeintex-learning
Branch: rebuild/learner-experience-v1

## Purpose

This file is the canonical handoff snapshot for continuing CodeInteX Learning development across ChatGPT sessions and human/AI contributors.

Use this file together with the ADRs under `docs/architecture/adr/` and the current Git history. If this file conflicts with newer verified repository evidence, newer evidence wins and this file should be updated.

## Current Critical Path

`learner reference slice frozen → select next product/revenue workstream`

The controlled learner reference slice:

`Learner Dashboard → Resume Learning → Curriculum Navigation → Lesson Experience`

now has repeatable Storybook coverage, Playwright browser verification, representative automated accessibility checks, controlled desktop/mobile visual review, real Django session/CSRF integration, authoritative progress-transition proof, and an unauthenticated recovery case.

The controlled learner reference slice is now frozen as the current engineering baseline. Automated responsive/reflow and keyboard/focus acceptance are complete. Representative real screen-reader validation remains OPEN as a later accessibility/release acceptance item; complete WCAG conformance is not claimed. The active critical path now returns to selecting the next product/revenue workstream from concrete requirements. Production topology, Docker/containerization, CI/CD deployment design, and other Production Readiness implementation remain PARKED until explicitly reactivated.

## Verified State

### Backend

- Django 6.1.1

- Wagtail 8.0

- Python 3.13.2

- PostgreSQL is the production canonical transactional database.

- SQLite is local development only.

- Final current-milestone default backend verification discovered **153 tests: 146 passed and 7 PostgreSQL-only tests were skipped**, with zero failures.

- After the notification-override change, the targeted Midtrans/checkout regression suite passes **36/36**, and the focused checkout + notification-override suite passes **15/15**.

- The previous dedicated commerce-wide checkpoint discovered **107 tests and passed with 7 PostgreSQL-only tests skipped**. The current full 153-test backend regression also passes after the latest Commerce changes.

- The PostgreSQL-only concurrency harness was rerun for the current milestone and passed **7/7** against PostgreSQL on 2026-09-18.

- `manage.py check`: passing at the latest backend checkpoints.

### Learner Dashboard Completion Semantics

My Learning distinguishes presentation state from progression context and does not infer authoritative course completion from lesson progress.

LOCKED for the current learner slice:

- backend `currentItemId` remains progression context and is not treated as a completion-status flag;
- lesson-completion presentation is derived from authoritative `completedItems` and `totalItems`;
- `totalItems > 0` and `completedItems == totalItems` maps to the presentation state `all-lessons-complete`;
- `all-lessons-complete` means only that every lesson in the enrolled release is complete; it does not establish authoritative course completion;
- an incomplete lesson set requires a valid current lesson and maps to `in-progress`;
- a zero-lesson course maps explicitly to `no-content`;
- courses with all lessons complete do not expose `CURRENT LESSON` or `Resume learning`;
- courses with all lessons complete retain `Course details`;
- My Learning progressbars include the course title and explicitly describe lesson progress in their accessible name.

Authoritative course completion remains an OPEN LMS domain policy. The frontend must not derive `course completed` merely from lesson counts or progress percentage.

The learner-facing view model uses a discriminated union so `all-lessons-complete`, `in-progress`, and `no-content` presentation states cannot silently share incompatible actions or imply stronger domain semantics.

Verification for the corrective milestone:

- frontend TypeScript typecheck: PASS;
- critical Playwright learner flow + representative axe checks: **3/3 PASS**;
- frontend Next.js production build: PASS;
- Storybook static production build: PASS;
- all-lessons-complete presentation renders `All lessons completed`;
- the learner UI no longer renders `Course complete` from lesson-count equality;
- `CURRENT LESSON` absent when all lessons are complete: PASS;
- `Resume learning` absent when all lessons are complete: PASS;
- `Course details` retained: PASS;
- `git diff --check`: PASS.

This was a narrow semantic correction to align implementation with the canonical PES completion contract. It does not reopen visual/layout refinement or introduce completion-policy, assessment, credential, or other new LMS architecture.

### Curriculum Navigation and Accessibility

The controlled Curriculum Navigation accessibility refinement is complete for the current learner slice.

LOCKED for the current implementation:

- curriculum items remain native buttons;
- the current curriculum item uses `aria-current="step"`;
- no locked/unavailable curriculum policy is fabricated while that LMS policy remains OPEN;
- curriculum buttons explicitly use `type="button"`;
- lesson navigation moves programmatic focus to `#lesson-content` after a real item change;
- the lesson content region remains programmatically focusable with `tabIndex={-1}`;
- lesson navigation respects `prefers-reduced-motion`;
- generic Button and Progress transitions suppress perceptible motion under reduced-motion preference;
- the generic Progress primitive exposes `role="progressbar"` plus `aria-valuemin`, `aria-valuemax`, and `aria-valuenow`.

Focused verification:

- frontend TypeScript typecheck: PASS;
- frontend Next.js production build: PASS;
- runtime progressbar semantics: PASS;
- runtime focus transfer to `#lesson-content`: PASS;
- runtime `prefers-reduced-motion` detection: PASS;
- navigation scroll behavior under reduced motion is explicitly `instant`: PASS;
- progress transition under reduced-motion emulation was effectively zero (`1e-05s` reported by browser tooling);
- temporary accessibility acceptance account was deleted after verification.

This milestone does not claim complete WCAG conformance. Representative automated accessibility coverage is now provided by the Playwright/axe learner-flow milestone below. Broader keyboard, zoom/reflow, screen-reader/assistive-technology, and responsive validation remains open where automation is insufficient.

### Storybook Verification Layer

The Storybook verification layer is established for the controlled learner reference slice.

Current implementation choices:

- Storybook is hosted by `apps/learner-web`; no separate Storybook workspace/app was created;
- Storybook uses `@storybook/nextjs-vite`;
- Storybook and `@storybook/nextjs-vite` are pinned to `10.6.0`;
- Vite is provisionally pinned to `7.3.6` for the current compatibility baseline;
- Storybook consumes the same style chain as the learner application:
  `design-tokens → ui-primitives → learning-ui → learner-web/globals.css`;
- no custom `viteFinal`, additional addon suite, visual-regression service, or topology refactor was introduced;
- generated `apps/learner-web/storybook-static/` output is ignored by Git.

Current reference-slice stories:

- Progress: empty, in-progress, complete;
- My Learning: in-progress, all-lessons-complete, mixed, no-content;
- Learning Player: initial, partially completed, deterministic authoritative-style completion transition.

Verification for this milestone:

- existing frontend direct dependency versions did not drift during Storybook installation;
- frontend TypeScript typecheck: PASS;
- Storybook static production build: PASS;
- Next.js production build after Storybook integration: PASS;
- `git diff --check`: PASS.

The Storybook build currently emits non-blocking Vite warnings for the client module directive and bundle chunk size. No workaround or bundler optimization is introduced because the workbench builds successfully and these warnings do not justify additional configuration at the current scope.

### Playwright and Automated Accessibility Verification

The repeatable browser-level verification layer for the controlled learner reference slice is established.

LOCKED for the current milestone:

- Playwright lives in the existing `apps/learner-web` tooling boundary; no separate E2E application/workspace was created;
- `@playwright/test` is pinned to `1.63.0`;
- `@axe-core/playwright` is pinned to `4.13.0`;
- the initial browser execution matrix uses Chromium only;
- Django and Next.js are orchestrated through Playwright `webServer`, while existing local servers may be reused outside CI;
- deterministic learner state is prepared by a dedicated backend fixture command under `commerce`, preserving the `learning` → commerce dependency boundary;
- the dedicated learner uses an `ADMIN_GRANT` entitlement and a real Enrollment, not fake Order/Payment records;
- authentication setup obtains a real CSRF token and establishes a real Django session through the same-origin Next.js API bridge;
- authenticated browser state is ephemeral under ignored `apps/learner-web/test-results/`;
- the critical learner test uses role/name-oriented locators where practical and does not mock the learner API;
- lesson completion asserts the real backend response and verifies that the UI consumes authoritative progress instead of independently deriving consequential progression state;
- a missing-session recovery case verifies redirects from `/my-learning` and `/learn/backend-engineering` to `/login`;
- representative axe scans are integrated into the same critical flow for My Learning and the post-completion Learning Player state.

Accessibility finding and correction:

- the initial axe run found a serious `color-contrast` violation across multiple small muted-text elements;
- the common cause was the PES semantic token `--text-muted: #758292`;
- per-selector overrides and axe exclusions were rejected;
- the semantic token was corrected to `--text-muted: #647180`;
- after the token correction, both representative automated accessibility scans pass.

Latest verification:

- Playwright setup/auth project: PASS;
- critical learner behavioral flow: PASS;
- unauthenticated recovery case: PASS;
- integrated Chromium run: **3/3 PASS**;
- representative My Learning WCAG 2.2 AA automated subset: PASS;
- representative Learning Player WCAG 2.2 AA automated subset: PASS;
- frontend TypeScript typecheck: PASS;
- Next.js production build: PASS;
- Storybook static production build: PASS;
- Django `manage.py check`: PASS;
- focused authentication + progress backend regression: **16/16 PASS**;
- `git diff --check`: PASS.

The automated checks do not establish complete WCAG conformance. Manual zoom/reflow and assistive-technology validation remain OPEN, together with any broader responsive/manual accessibility evidence required by later acceptance gates.

Decision state:

- Playwright orchestration for the reference slice: LOCKED;
- deterministic E2E learner fixture: LOCKED;
- critical learner-flow E2E: LOCKED;
- representative axe integration: LOCKED;
- unauthenticated recovery coverage: LOCKED;
- corrected muted-text semantic token for the current PES baseline: LOCKED;
- Chromium-only initial execution matrix: PROVISIONAL;
- cross-browser expansion: OPEN;
- manual zoom/reflow and assistive-technology validation: OPEN.

### Controlled PES Visual Refinement

The controlled visual refinement pass for the proven learner reference slice is complete.

Evidence and scope:

- visual review used rendered My Learning and Learning Player states at desktop (`1440×1000`) and mobile (`390px` viewport width);
- the existing information architecture and Learning Player composition were retained rather than redesigned;
- My Learning intro vertical spacing was reduced so active learning and the resume action appear earlier while preserving hierarchy and readable whitespace;
- the desktop Learning Player footer now allows the disabled `Previous` control to use intrinsic width rather than visually occupying a large portion of the footer;
- mobile curriculum disclosure, lesson typography, reading measure, curriculum grouping, active/completed state presentation, and primary action hierarchy were reviewed and intentionally left unchanged;
- the apparent mobile sticky-footer/content overlap was tested explicitly and found not to be a product defect: final lesson content retained approximately 64px clearance above the sticky footer at the tested viewport;
- temporary visual-audit Playwright specs and screenshots were not promoted into permanent visual-regression infrastructure.

Decision state:

- My Learning vertical hierarchy refinement: LOCKED;
- desktop Learning Player footer balance: LOCKED;
- Learning Player information architecture/layout: NO-CHANGE;
- mobile curriculum presentation: NO-CHANGE;
- sticky-footer occlusion concern: CLOSED / NO DEFECT;
- further visual tweaking in this slice: STOPPED to avoid diminishing-return polish.

Final regression verification after refinement:

- frontend TypeScript typecheck: PASS;
- critical Playwright learner flow + representative axe checks: **3/3 PASS**;
- Next.js production build: PASS;
- Storybook static production build: PASS;
- `git diff --check`: PASS.

This milestone does not claim complete WCAG conformance. Manual zoom/reflow and assistive-technology validation remain OPEN and form the next narrow acceptance step.

### Responsive and Keyboard Acceptance Closure

The automated acceptance closure for the controlled learner reference slice is complete.

Verified evidence:

- a `320px` CSS viewport was used as a high-reflow proxy for the critical learner flow;
- My Learning and Learning Player showed no page-level horizontal overflow;
- required progress/current-state information remained available;
- primary learner actions remained visible and operable;
- My Learning primary and secondary actions were reachable by keyboard;
- curriculum lesson controls were reachable and operable by keyboard;
- lesson navigation preserved the expected programmatic focus transition into `#lesson-content`;
- footer navigation/completion controls were reachable by keyboard with visible focus;
- the complete Playwright acceptance run passed **3/3** including authenticated setup;
- frontend TypeScript typecheck passed;
- `git diff --check` passed.

Decision state:

- responsive/reflow automated acceptance: LOCKED / PASS;
- keyboard/focus automated acceptance: LOCKED / PASS;
- current learner reference slice: FROZEN;
- representative real screen-reader validation: OPEN;
- complete WCAG conformance: NOT CLAIMED;
- further learner visual/accessibility tooling expansion: STOPPED unless activated by a concrete requirement.

The temporary acceptance Playwright spec was used only as verification evidence and is not retained as permanent test infrastructure because the current production E2E suite already protects the critical learner behavior and expanding one-off acceptance tooling would add maintenance cost without a demonstrated requirement.

### Frontend

- Next.js 16.3.3

- React 19.2.x

- TypeScript 5.9.3

- npm workspaces

- `npm run typecheck`: **passing** for the current monetization checkpoint on 2026-09-18.

- `npm run build`: **passing** for the current monetization checkpoint on 2026-09-18. The production route manifest includes `/courses/backend-engineering`, `/checkout/backend-engineering`, `/checkout/backend-engineering/return`, `/login`, `/learn/backend-engineering`, and `/my-learning`.

- The learner-facing course detail, login continuation, checkout page, and post-payment return page are implemented, verified, committed, and pushed as part of the monetization checkpoint.

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

### Build-vs-Adopt Learning Platform Strategy

- The Build-vs-Adopt Architecture Gate was completed on 2026-09-18 and is recorded in ADR-008.
- CodeInteX retains canonical ownership of Course/CourseRelease, learner-facing runtime contracts, Enrollment/progress semantics, Entitlement/Commerce semantics, and the learner-facing Product Experience.
- CodeInteX will not replatform its canonical learning core onto Open edX, Moodle, Canvas, or another full LMS without new material evidence.
- This decision does not authorize rebuilding every LMS capability internally.
- Complex non-differentiating capabilities must pass an Adopt/Integrate evaluation before custom implementation.
- `CodeInteX semantics at the core; standards at the edges` is the governing platform strategy.
- Wagtail remains a replaceable authoring implementation rather than the learner runtime contract.
- Standards and specialized engines remain requirement-driven integration choices rather than automatic platform dependencies.

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

- The Build-vs-Adopt Architecture Gate is complete. Major LMS-domain expansion must follow ADR-008: differentiated CodeInteX semantics may be owned internally, while complex non-differentiating capabilities require an Adopt/Integrate evaluation before custom implementation.

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
- Paid-course Enrollment is not exposed as a public learner-created mutation; trusted provisioning such as purchase fulfillment owns Enrollment creation.
- The former `/api/v1/courses/<slug>/enrollment/` learner endpoint has been removed and is regression-tested as unavailable, closing the direct commercial-access bypass.
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

**Implementation state:** Commerce Schema V1 provider-neutral transaction boundaries, Checkout Orchestration V1, the first Midtrans adapter, durable authenticated notification ingress, synchronous HTTP notification processing, replay idempotency, and GET Status reconciliation are implemented for the current one-time-purchase Sandbox acceptance path. Earlier real Midtrans proof established signed SHA-512 notification ingestion, durable ProviderEvent persistence, separate event processing, replay safety, and reconciliation convergence. The current local HTTP notification path now durably ingests the authenticated ProviderEvent first and then invokes `process_midtrans_event` synchronously before returning HTTP 200; processing failure therefore does not receive a false-success acknowledgement. A real learner-facing Sandbox purchase for `sandbox-checkout-buyer-3` has now converged automatically from a signed Midtrans `capture` notification to Payment `SUCCEEDED`, Order `FULFILLED`, one ACTIVE PURCHASE CourseEntitlement, and one Enrollment to CourseRelease 1. The ProviderEvent was `PROCESSED`, `attempt_count=1`, authenticated with `midtrans-sha512`, and recorded no processing error. The first buyer-3 checkout attempt had failed before provider transaction creation because the runtime Sandbox Server Key was invalid; Midtrans Status API confirmed `Transaction doesn't exist`. After the credential was corrected, CodeInteX reused the same OPEN Order and CREATED Payment, proving recovery without duplicate Order or Payment creation. The post-override targeted regression suite passes 36/36 and the focused checkout/notification-override suite passes 15/15. Final current-milestone verification also passes: the full default backend suite discovered 153 tests with 146 passed and 7 PostgreSQL-only tests skipped, and the separate PostgreSQL concurrency harness passed 7/7.

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


### Checkout Orchestration V1

- Learner checkout is exposed through `POST /api/v1/commerce/courses/<slug>/checkout/`.

- Checkout requires an authenticated Django session and remains CSRF-protected.

- Course identity is resolved server-side from the slug; the Course must be active and have a published CourseRelease before it is sellable.

- The active IDR CourseOffer, amount, and currency are resolved server-side. Client-supplied price, currency, and offer identifiers are not commercial authority.

- Checkout reuses an existing live OPEN Order and existing CREATED/PENDING Midtrans Payment instead of creating duplicate payable transactions on ordinary retries.

- `Payment.checkout_url` persists the hosted provider checkout capability so ordinary reload/retry can return the same checkout destination without another provider call.

- Midtrans Snap creation uses `Payment.operation_key` as the provider `Idempotency-Key`.

- A provider error after local Order/Payment creation leaves the same local transaction available for retry. The buyer-3 Sandbox proof exercised this recovery path after an invalid runtime Server Key caused a pre-provider checkout failure; the same Order and Payment were later reused successfully without duplicates.

- `MIDTRANS_NOTIFICATION_URL` is an optional runtime setting. When configured, the Midtrans adapter sends it through `X-Override-Notification`; when absent, the adapter preserves the previous provider behavior and does not send the override header.

- The notification override remains contained inside the Midtrans adapter boundary and does not leak provider-specific semantics into learner-facing or core Commerce contracts.

- An active PURCHASE CourseEntitlement prevents creation of a new purchase checkout for that learner and Course.

- A browser redirect remains non-authoritative for payment success; fulfillment requires trusted server-side provider observation.

- Known limitation: the narrow ambiguous-outcome window where Midtrans successfully creates checkout but CodeInteX fails before persisting `checkout_url` is not considered fully solved for recovery beyond the provider idempotency window.

### Learner Purchase Experience & Real Sandbox E2E

- Public offer discovery is exposed through `GET /api/v1/commerce/courses/<slug>/offer/`. The response exposes provider-neutral amount/currency information and does not expose Midtrans tokens, provider IDs, or commercial authority.

- The `backend-engineering` course detail page now renders persisted learning state and commercial state together: enrolled learners receive Resume; non-enrolled learners receive `Buy course · Rp10.000` from the server-authoritative offer.

- Unauthenticated purchase intent is preserved through login using a validated same-origin `next` destination; the login continuation prevents open redirects.

- `/checkout/backend-engineering` obtains the Django CSRF capability and invokes the provider-neutral CodeInteX checkout endpoint. `401` returns to login; already-entitled/succeeded conflicts return to learning; only an HTTPS checkout URL returned by the trusted backend is followed.

- `/checkout/backend-engineering/return` does not trust Midtrans browser parameters. It polls the existing authenticated progress/access read model until server-authoritative fulfillment has provisioned access.

- Development CSRF trusted origins can be extended through `CODEINTEX_DEV_CSRF_TRUSTED_ORIGINS`, allowing ephemeral HTTPS test origins without hard-coding temporary tunnel hostnames into production settings.

- Next.js `allowedDevOrigins` includes `127.0.0.1` for the local tunnel/dev topology.

- Buyer-2 proved the browser Finish Redirect path but did not prove automatic fulfillment: its Midtrans payment succeeded while the temporary backend Quick Tunnel had become DNS-unresolvable, so no provider notification reached CodeInteX. The evidence was preserved rather than manually rewritten into a successful E2E.

- Buyer-3 started from zero Orders, Payments, Entitlements, and Enrollments. Its first checkout attempt created one OPEN Order and one CREATED Payment, then returned HTTP 502 because the runtime Midtrans Sandbox Server Key was invalid. A read-only Midtrans Status check with the corrected credential confirmed that no provider transaction had been created.

- Retrying buyer-3 after correcting the credential reused the same Order and Payment. The real Sandbox payment completed and the authentic signed Midtrans `capture` notification automatically produced exactly one FULFILLED Order, one SUCCEEDED Payment with provider transaction ID, one ACTIVE PURCHASE CourseEntitlement, and one Enrollment to CourseRelease 1.

- The buyer-3 ProviderEvent was `PROCESSED`, `attempt_count=1`, `observed_payment_status=SUCCEEDED`, authenticated by `midtrans-sha512`, and had no processing error.

- Cloudflare Quick Tunnels have repeatedly expired or become DNS-unresolvable during long-running payment tests. They are useful only as ephemeral development infrastructure and are not an acceptable production webhook or redirect endpoint.

- Backend automatic fulfillment through the learner-facing purchase path is proven. A separate explicit acceptance record of the final browser transition from the return page to `/learn/backend-engineering` remains desirable if it was not captured during the successful buyer-3 run.

## PROVISIONAL

- If a learner has multiple enrollments for the same course, the newest enrollment is treated as current.

- Resume semantics are currently the first incomplete lesson, not last-visited lesson.

- The current login page is functional MVP UI, not the final Product Experience System surface.

- Reusable Django/Wagtail package extraction may be valuable later but is not a current implementation target.

- Local Next.js external rewrite is a development same-origin bridge; production routing remains to be finalized.

- Midtrans Snap is the implemented first Indonesian one-time-payment provider, but is not an architectural dependency.

- `MIDTRANS_NOTIFICATION_URL` / Midtrans `X-Override-Notification` is useful for development and deployment flexibility. Production webhook delivery must use stable infrastructure rather than ephemeral Quick Tunnels.

- The return page currently uses authenticated progress/access availability as the minimal provider-neutral fulfillment-ready signal. A dedicated purchase-status read model should be added only if richer post-payment UX or operational recovery requires it.

- Wagtail remains the current authoring implementation, but its long-term role remains provisional behind CodeInteX-owned learner/runtime contracts.

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

- Stable production payment-notification endpoint and provider-delivery topology.

- Durable retry/reconciliation scheduling for CREATED/PENDING or otherwise ambiguous provider transactions.

- Whether a provider-neutral purchase-status endpoint is needed beyond the current progress/access-ready polling.

- Graceful learner-facing handling when a Course has no active sellable CourseOffer.

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

Learning:

`Login → Django session → My Learning → Resume → Learning Player → persisted LessonProgress → refresh-safe resume`

Paid acquisition:

`Course detail → Buy → login continuation if required → CodeInteX checkout → hosted Midtrans Sandbox payment → signed server notification → Payment SUCCEEDED → Order FULFILLED → ACTIVE PURCHASE entitlement → Enrollment`

Verified behavior includes:

- Browser login succeeds through the same-origin API bridge.

- Django returns and accepts session cookies.

- Enrollment is provisioned by trusted backend workflows; there is no public learner enrollment mutation for paid access.

- Completion is idempotent.

- Progress persists across requests.

- Player restores persisted completion and current lesson after refresh.

- My Learning reflects the same persisted state.

- Release pinning prevents mixing learner progress from one release with content from another.

- Public course offer data is server-authoritative and provider-neutral.

- Browser payment return is not payment authority.

- Real signed Midtrans Sandbox notification can automatically fulfill purchase access.

- Retry after a pre-provider checkout failure can reuse the existing OPEN Order and CREATED Payment without creating duplicate commercial records.

- The buyer-3 proof produced exactly one ACTIVE PURCHASE entitlement and exactly one Enrollment.

- Final browser auto-transition from the return page to `/learn/backend-engineering` should be separately captured as UX acceptance evidence if it was not observed/documented during the buyer-3 run.

## Current Backend Test Milestones

- 17 tests: published release immutability.

- 23 tests: runtime persistence models.

- 31 tests: authenticated progress API.

- 36 tests: authentication API.

- 39 tests: My Learning read-model and latest-enrollment behavior.

- Current full default backend checkpoint: **153 tests discovered; 146 passed and 7 PostgreSQL-only tests skipped; zero failures**.

- Previous commerce-wide checkpoint: **107 tests discovered, OK with 7 PostgreSQL-only tests skipped**.

- Latest post-`X-Override-Notification` targeted Midtrans/checkout regression: **36/36 passed**.

- Latest focused checkout + notification-override regression: **15/15 passed**.

- Current PostgreSQL concurrency verification: **7/7 passed on 2026-09-18**.

- Final current-milestone full backend regression is complete and passing after the notification-override changes.

## Current Workstream Boundary

### Product Experience System

The current PES normative baseline is canonical under `docs/pes/`.

Canonical artifacts:

- `docs/pes/PES-FOUNDATION-DECISION-MODEL-v0.1.md`
- `docs/pes/PES-CONSUMPTION-CONTRACT-v0.1.md`
- `docs/pes/LMS-EXPERIENCE-PROFILE-v0.1.md`
- `docs/pes/WEB-IMPLEMENTATION-PROFILE-v0.1.md`
- `docs/pes/PES-DECISION-LOG.md`

Supporting evidence remains under `docs/pes/benchmarks/`.

Do not create a parallel LMS design foundation. The LMS consumes the PES contracts and profiles.

### Active Learner Experience Slice

The active reference implementation slice is:

`Learner Dashboard → Resume Learning → Curriculum Navigation → Lesson Experience`

The purpose is to validate the existing architecture against the canonical PES/LMS contracts without broad redesign or feature expansion.

Stable dependency direction:

`backend/domain authority → API/service contract → web data-access boundary → adapter/view model → CodeInteX-owned UI`

Physical package topology remains OPEN and should not be refactored merely for cleanliness during this slice.

### Learner Progression

Lesson-completion transitions now consume authoritative progress returned by the backend.

The client no longer independently decides consequential completion/progression state by marking the current item complete and advancing to the next array item.

Current flow:

`POST lesson completion → backend authoritative progress snapshot → web response validation → LearningProgressView → learner UI state`

The learner UI may continue to own ordinary display/navigation state, but completion state, progress percentage, and post-completion current item are derived from the authoritative server result.

Focused verification for this milestone:

- frontend TypeScript typecheck: PASS;
- frontend Next.js production build: PASS;
- `learning.test_progress_api`: 11/11 PASS;
- `git diff --check`: PASS.

### Frontend

Existing `apps/learner-web` remains the active learner application.

Existing `@codeintex/learning-ui` remains the CodeInteX-owned learner UI layer.

Next.js 16.x, App Router, React 19.x, TypeScript, Tailwind CSS 4.x, Base UI where appropriate, Storybook, Playwright, and `@axe-core/playwright` follow the canonical Web Implementation Profile.

Do not invent a second LMS token system while canonical PES token serialization remains unresolved.

### Backend

Existing Course/CourseRelease, enrollment, learner progress, authentication, entitlement, commerce, and payment correctness remain authoritative.

Wagtail remains an authoring implementation rather than the learner-facing runtime contract.

Curriculum locked/unavailable behavior remains an OPEN LMS policy and must not be fabricated in frontend code.

### Infrastructure

Production Readiness V1 remains LOCKED and valid.

Hosting topology, Docker/containerization, CI/CD deployment design, managed PostgreSQL selection, object storage, and scaling work are currently PARKED from the active learner-experience critical path.

The untracked files:

- `apps/learning-backend/Dockerfile`
- `apps/learning-backend/.dockerignore`

remain PARKED and must not be staged implicitly.

## Next Milestone

The controlled learner reference slice is frozen.

The next step is to select the next product/revenue workstream from concrete requirements rather than continuing learner-shell refinement.

Constraints:

1. do not reopen Dashboard, Curriculum, or Lesson visual refinement without a demonstrated usability, accessibility, or product defect;
2. keep representative real screen-reader validation OPEN as a release/accessibility acceptance item;
3. do not claim complete WCAG conformance from axe, Playwright, or reflow proxies alone;
4. do not expand the browser matrix without an explicit browser-support requirement;
5. do not introduce new accessibility tooling solely to close documentation gaps;
6. Production Readiness infrastructure remains PARKED until explicitly reactivated;
7. prioritize the next workstream by product value, revenue leverage, dependency order, and evidence rather than novelty.

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
