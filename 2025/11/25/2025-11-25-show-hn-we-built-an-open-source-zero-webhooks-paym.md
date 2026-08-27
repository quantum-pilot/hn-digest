# Show HN: We built an open source, zero webhooks payment processor

- Score: 199 | [HN](https://news.ycombinator.com/item?id=46048252) | Link: https://github.com/flowglad/flowglad

### TL;DR

The captured repository page identifies Flowglad as open-source payments and billing infrastructure, while the title promises a webhook-free developer experience; the frozen page omits enough README detail to verify that architecture. Discussion supplies the clearest model: Flowglad currently uses Stripe Connect and aims to manage plan, feature, price, and customer mappings. Critics say remote state reads add latency and limit complex queries, while the author acknowledges plans for merchant-side storage and that an acquiring provider remains necessary.

### Comment pulse

- Billing abstraction can accelerate pricing experiments → AI products frequently change meters, entitlements, and plans.
- Remote reads may become a bottleneck → local payment state supports responsiveness and flexible cross-customer queries.
- Open source does not remove payment risk → Stripe Connect still supplies merchant acquiring and regulated infrastructure.

### LLM perspective

- View: The valuable layer is billing-state orchestration, not replacement of banks or payment rails.
- Impact: Developers may trade integration work for another operational dependency and narrower data access.
- Watch next: Verify webhook elimination, self-hosting boundaries, read latency, local-state support, fees, and failure recovery.
