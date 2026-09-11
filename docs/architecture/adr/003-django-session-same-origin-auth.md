# ADR-003: Django Session Authentication with Same-Origin Browser APIs

Status: Accepted
Date: 2026-09-11

## Context

CodeInteX Learning needs secure learner authentication quickly, with minimal infrastructure and without introducing a premature third-party auth dependency or browser token-storage scheme.

The learner web application is Next.js while Django is the application/runtime authority.

## Decision

For the current MVP:

- Django session authentication is the learner identity authority.
- Browser API traffic targets same-origin `/api/v1/*`.
- CSRF protection remains enabled for unsafe requests.
- Session cookies are HttpOnly and should remain scoped to the learning host.
- No bearer token is stored in browser `localStorage`.
- Local development uses a Next.js rewrite to Django.
- Server-side Next.js reads may forward the Django session cookie to the backend when needed.
- Production reverse-proxy routing will preserve the same browser-origin model.

## Consequences

Positive:

- simple threat model relative to custom browser token handling;
- Django's mature session and CSRF machinery remains authoritative;
- no duplicate identity store is introduced;
- frontend remains thin around authentication state.

Trade-offs:

- production proxy Host/proto handling must be configured correctly;
- CSRF trusted-origin behavior must be verified for each environment;
- future central SSO/OIDC will require an explicit migration/integration design.

## Security Constraints

- do not disable CSRF to simplify integration;
- do not use wildcard trusted origins;
- do not broaden cookie scope to `.codeintex.com` without an explicit cross-product authentication decision;
- verify secure cookie, TLS, proxy headers, and production security settings before accepting production traffic.
