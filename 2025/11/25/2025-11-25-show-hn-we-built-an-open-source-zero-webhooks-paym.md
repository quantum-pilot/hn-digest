# Show HN: We built an open source, zero webhooks payment processor

- Score: 199 | [HN](https://news.ycombinator.com/item?id=46048252) | Link: https://github.com/flowglad/flowglad

### TL;DR

Flowglad presents an open-source payments and billing layer designed to remove webhook handling and the mappings among product plans, prices, entitlements, provider customers, and application users. It still uses Stripe Connect for merchant accounts and acquiring, so the open code does not replace regulated payment rails. Critics questioned routing subscription-state reads through another hosted API, especially for responsive or analytical workloads; the team acknowledged this and plans merchant-side storage. Supporters saw value in changing AI-product pricing without repeatedly rebuilding billing lifecycle logic.

### Comment pulse

- The abstraction targets billing state → developers avoid maintaining price, plan, feature, and customer mappings across application and Stripe models.
- Zero webhooks does not mean zero intermediaries → Stripe Connect still supplies merchant acquiring — counterpoint: open billing logic can remain valuable.
- Remote reads may constrain product queries → caching restores responsiveness but reintroduces local state and synchronization work.

### LLM perspective

- View: This is an orchestration layer over payments, not an independent processor or self-hosted banking stack.
- Impact: Startups may iterate pricing faster while accepting another service dependency and provider constraints.
- Watch next: Self-hosting scope, merchant-side caching, query APIs, reconciliation guarantees, pricing, and support beyond Stripe Connect.
