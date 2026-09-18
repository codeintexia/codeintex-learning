# CodeInteX Learning — Production Readiness V1

Status: LOCKED
Date: 2026-09-18

## Purpose

Define the minimum production requirements and acceptance criteria for
CodeInteX Learning before choosing or locking a hosting provider or production
topology.

This document defines requirements, not implementation choices.

## Scope

Production readiness for the currently proven monetization slice:

- learner-facing Next.js application;
- Django/Wagtail backend;
- PostgreSQL;
- Wagtail-authored course content;
- learner authentication/session;
- learner runtime state;
- CodeInteX Commerce;
- Midtrans payment integration;
- learner purchase and fulfillment flow.

## Non-Goals

This gate does not introduce:

- Kubernetes;
- microservices;
- Redis;
- Celery;
- multi-region deployment;
- autoscaling architecture;
- event streaming;
- a new LMS platform;
- new learner features;
- PES/UI redesign.

Those require separate evidence.

## LOCKED Requirements

### 1. Stable Public HTTPS

Production must provide stable HTTPS origins.

Ephemeral tunnels are not acceptable production infrastructure.

Required public behavior:

- learner web is available through a stable HTTPS hostname;
- `/api/v1/*` remains same-origin from the browser perspective;
- Midtrans has a stable HTTPS notification endpoint;
- HTTP traffic redirects to HTTPS where applicable;
- TLS termination and proxy behavior are explicit and testable.

### 2. Authentication and Browser Security

Production must preserve the existing authentication model unless a separate
architecture decision changes it.

Requirements:

- Django session authentication remains authoritative;
- CSRF remains enabled;
- session and CSRF cookies are Secure in production;
- browser auth tokens are not stored in localStorage;
- trusted origins and allowed hosts are explicit;
- wildcard trusted origins are prohibited;
- proxy Host/protocol handling must not weaken origin checks.

### 3. PostgreSQL Durability

Production transactional state must use PostgreSQL.

Requirements:

- production does not use SQLite;
- database storage is persistent;
- TLS is used for remote database connections when applicable;
- database credentials are not committed to Git;
- database backup exists;
- restore procedure is documented and tested before real payment launch.

### 4. Persistent Media

Wagtail-uploaded media must survive application restart and redeployment.

Requirements:

- production media must not depend on ephemeral application filesystem;
- media access must use stable URLs;
- backup/retention behavior must be defined;
- storage implementation must remain replaceable behind Django/Wagtail
  storage interfaces.

### 5. Static Assets

Production static assets must be deterministic and deploy-safe.

Requirements:

- `collectstatic` or equivalent production build process succeeds;
- missing static assets fail visibly during staging verification;
- application deployment does not depend on local developer files.

### 6. Secrets and Configuration

Secrets must be supplied through the deployment environment or a managed
secret mechanism.

At minimum:

- `DJANGO_SECRET_KEY`;
- database credentials;
- Midtrans Server Key;
- provider environment selection;
- stable notification URL where required.

Requirements:

- secrets are never committed;
- secrets are not printed in deployment logs;
- production startup fails closed when required configuration is absent;
- Sandbox and Production payment credentials cannot be confused silently;
- secret rotation procedures are documented for Django, database, and payment
  credentials;
- the operational consequences of rotating `DJANGO_SECRET_KEY`, including
  session invalidation or signing impact, are understood before rotation.

### 7. Environment Isolation

Staging and production must be operationally distinct environments.

Requirements:

- staging and production use separate application configuration;
- staging and production do not share PostgreSQL databases;
- staging and production do not share payment credentials;
- staging uses Sandbox payment credentials;
- production credentials are not available to ordinary staging processes;
- production personal/payment data must not be copied into staging without an
  explicit sanitization process;
- environment identity must be visible enough operationally to reduce
  accidental cross-environment actions.

### 8. Application Runtime

Production processes must use production-capable runtime commands.

Requirements:

- Django must not use `manage.py runserver`;
- Next.js must run from a production build;
- application startup behavior is deterministic;
- failed startup must be observable;
- graceful restart behavior must not corrupt transactional state.

The exact process manager/server remains an implementation choice.

### 9. Health and Readiness

The deployment platform must be able to distinguish a running process from an
application that is ready to serve traffic.

Minimum requirements:

- lightweight liveness signal;
- readiness signal that proves the application can serve its required runtime
  dependencies;
- health checks must not mutate application state;
- health endpoints must not expose secrets or sensitive system information.

Exact endpoint design remains OPEN until implementation.

### 10. Payment Notification Reliability

Production payment authority remains server-side.

Requirements:

- browser redirects are never payment authority;
- Midtrans notification signature validation remains mandatory;
- provider notification URL is stable;
- duplicate notifications remain safe;
- processing failures must not be falsely acknowledged as successfully
  fulfilled;
- notification processing remains idempotent.

### 11. Payment Recovery and Reconciliation

Production must not rely solely on a single webhook delivery.

Before accepting real production payments:

- CREATED/PENDING/ambiguous transactions must have a recovery path;
- provider reconciliation uses trusted server-to-server verification;
- retry processing must remain idempotent;
- duplicate fulfillment must remain impossible under expected races;
- reconciliation failures must be observable.

The scheduler/runtime mechanism is OPEN.

### 12. Logging and Minimum Observability

Production must provide enough evidence to diagnose failed checkout,
notification, fulfillment, authentication, and deployment operations.

Requirements:

- application errors are captured;
- HTTP 5xx failures are discoverable;
- payment integration failures are discoverable without logging secrets or
  sensitive payment data;
- deployment/restart failures are discoverable;
- logs have sufficient request/event correlation for payment diagnosis;
- cookies, session identifiers, authentication tokens, payment Server Keys,
  signatures, database credentials, and other secrets must not be logged;
- full provider payloads must not be logged by default when they may contain
  sensitive or unnecessary payment/customer data;
- retention period is explicitly defined before production launch.

A specific observability vendor is not yet selected.

### 13. Backup and Restore

Backup is not sufficient without proven restore.

Before production payment launch:

- database backup mechanism exists;
- media backup/retention is understood;
- restore procedure is documented;
- at least one staging restore test succeeds;
- recovery ownership and expected recovery time are documented.

Exact RPO/RTO targets remain OPEN until business constraints are defined.

### 14. Deployment and Rollback

Production deployment must be repeatable.

Requirements:

- deployment source is Git;
- schema migrations are explicit;
- migration failure behavior is understood;
- application version can be identified in production;
- rollback procedure is documented;
- rollback must account for database migration compatibility.

### 15. Security Baseline

Before public production launch:

- `manage.py check --deploy` is reviewed under production settings;
- DEBUG is disabled;
- HTTPS is mandatory;
- secure cookies are enabled;
- allowed hosts are explicit;
- CSRF trusted origins are explicit where needed;
- secrets are not committed;
- dependency/security scanning baseline is defined;
- privileged Django/Wagtail accounts follow explicit account hygiene;
- administrative authentication must have protection against practical
  brute-force/credential-stuffing risk;
- the Wagtail/admin surface is not unintentionally exposed through weak
  defaults;
- security headers and proxy trust settings are explicitly reviewed.

The exact privileged-access mechanism remains an implementation choice; this
requirement does not mandate a specific WAF, identity provider, or MFA product
at this stage.

### 16. External Dependency Failure Behavior

Failures of external dependencies must fail explicitly rather than producing
ambiguous success.

At minimum, production behavior must be understood for:

- PostgreSQL connection failure or timeout;
- Midtrans timeout, unavailable response, or ambiguous checkout result;
- persistent media/object-storage timeout or unavailability;
- outbound network failure.

Requirements:

- external calls use bounded timeouts where the client/library allows it;
- failure must not be converted into false payment success;
- retries must not violate idempotency;
- learner-facing failure states must terminate rather than hang indefinitely;
- operationally relevant failures must be observable.

Exact timeout values and retry policies remain implementation choices.

### 17. Operational Simplicity

Initial production infrastructure should minimize operational burden.

Prefer:

- managed infrastructure where it materially reduces failure/maintenance risk;
- one region unless evidence requires more;
- the smallest number of independently operated services consistent with
  correctness;
- reversible infrastructure choices.

Avoid:

- Kubernetes;
- unnecessary service decomposition;
- infrastructure introduced only for hypothetical future scale.

### 18. Cost Predictability

Production infrastructure must have understandable billing behavior.

Before selecting a provider:

- expected fixed monthly baseline is documented;
- major variable-cost dimensions are identified;
- spending alerts/limits are available where applicable;
- no provider is chosen primarily because of a promotional/free-tier headline.

The acceptable monthly budget ceiling is currently OPEN.

## Production Acceptance Gates

Real production payments MUST NOT be enabled until all applicable gates pass.

### Gate A — Build

- backend tests pass;
- PostgreSQL race-sensitive tests pass;
- frontend typecheck passes;
- frontend production build passes;
- static asset build passes.

### Gate B — Staging

- staging is operationally isolated from production;
- staging uses a separate database and Sandbox payment credentials;
- stable HTTPS staging origin works;
- same-origin `/api/v1/*` works;
- login/session/CSRF work;
- persistent media survives redeploy;
- database migrations succeed from a clean deployment;
- payment Sandbox checkout works;
- signed notification reaches the stable staging endpoint;
- automatic fulfillment succeeds;
- reconciliation recovery succeeds;
- representative dependency-failure behavior terminates safely without false
  payment success.

### Gate C — Recovery

- database backup exists;
- staging database restore succeeds;
- media recovery expectations are verified;
- application rollback procedure is exercised.

### Gate D — Security

- production settings review passes;
- `check --deploy` findings are reviewed and resolved or explicitly accepted;
- no concrete secrets exist in Git;
- sensitive logs are reviewed for secret/session/payment-data leakage;
- proxy/TLS/origin configuration is verified;
- privileged/admin account and access protections are reviewed;
- administrative surfaces are reviewed.

### Gate E — Operations

- application errors are observable;
- payment failures are diagnosable;
- reconciliation has an operational execution mechanism;
- deployment failure is observable;
- cost monitoring/alerts are configured.

### Gate F — Production Payment Enablement

Only after Gates A–E pass:

- production provider credentials may be configured;
- production notification URL may be registered;
- one controlled production transaction may be executed;
- post-transaction database and provider records must be reconciled;
- broader payment availability remains contingent on that controlled proof.

## Decision State

### LOCKED

- stable HTTPS is required;
- browser API remains same-origin;
- PostgreSQL is production transactional storage;
- production media is persistent;
- server-side provider observation is payment authority;
- webhook authentication and idempotency are mandatory;
- backup/restore must be proven;
- deployment/rollback must be defined;
- minimum observability is required;
- operational simplicity and cost predictability are explicit selection
  criteria;
- staging and production are operationally isolated;
- sensitive credentials/session/payment data must not leak through logs;
- external dependency failures must terminate safely without creating false
  success.

### PROVISIONAL

- one-region initial deployment;
- managed infrastructure where economically reasonable;
- minimal number of runtime components.

### OPEN

- hosting provider;
- exact production topology;
- Docker vs native build;
- production application server;
- object-storage provider;
- observability vendor;
- reconciliation scheduler mechanism;
- exact health endpoint design;
- RPO/RTO;
- monthly infrastructure budget ceiling;
- resource sizing;
- admin hostname/topology;
- privileged-access implementation mechanism;
- exact external-call timeout and retry policies;
- production log retention period.

## Next Decision

Compare viable hosting/topology options against this requirement set.

No provider or topology should be locked until it can demonstrate acceptable
fit against these requirements and the current CodeInteX architecture.
