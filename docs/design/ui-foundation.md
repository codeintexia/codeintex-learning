---
title: CodeInteX UI Foundation
version: 0.2.0
status: Active
last_reviewed: 2026-09-05
---

# CodeInteX UI Foundation

## Character

Precise. Calm. Technical. Premium. Dense but readable.

## Contract

1. Content dominates chrome.
2. Product code expresses product intent, not reusable styling recipes.
3. Semantic tokens are the visual contract.
4. Generic UI primitives do not know learning-domain concepts.
5. Learning UI may compose primitives, never the reverse.
6. Accessibility is part of component behavior.
7. Vendor/framework details do not leak into product APIs.
8. Redesigns should mostly affect token/UI layers unless the product interaction model changes.
9. New components come from real product needs, not catalog completeness.

## Layers

```text
design-tokens
  → semantic visual language

ui-primitives
  → generic interaction contracts

learning-ui
  → learning-domain composition

learner-web
  → routes, product flow, data integration
```

## Naming rules

Prefer domain nouns:

- `learner-web`
- `design-tokens`
- `ui-primitives`
- `learning-ui`
- `curriculum`
- `fixtures`

Avoid ambiguous buckets:

- `shared`
- `common`
- `core`
- `misc`
- `helpers`
- `stuff`

Do not use vendor names in architectural folder names.

## Portability rule

Theme-level changes should not require editing `apps/learner-web`.

Changes to visual language:
- color;
- typography;
- spacing;
- radius;
- shadows;
- motion;
- component skin;

belong below the application.

Changes to product interaction architecture may legitimately change application/product components.

## Non-goals

Not now:
- full Primer clone;
- multi-brand engine;
- dark mode;
- full Storybook governance;
- design-system portal;
- package publishing infrastructure.

## Stop rule

Once the Learning Player is coherent, responsive, keyboard-usable, and the current primitives are stable:

> stop foundation work and build the next learner surface.
