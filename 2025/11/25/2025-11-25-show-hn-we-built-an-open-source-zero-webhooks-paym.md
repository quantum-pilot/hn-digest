# Show HN: We built an open source, zero webhooks payment processor

- Score: 199 | [HN](https://news.ycombinator.com/item?id=46048252) | Link: https://github.com/flowglad/flowglad

- TL;DR  
    - Flowglad is an open-source billing and payments layer that sits on top of Stripe Connect, aiming to eliminate webhook juggling and state-machine-heavy billing logic. Developers call Flowglad via SDKs to manage plans, subscriptions, and usage-based pricing instead of wiring Stripe directly. HN discussion questions whether adding a middleman improves risk, latency, and cost versus using Stripe plus a local DB, but sees clear appeal for fast-changing SaaS/AI pricing where billing logic is constantly rewritten.

- Comment pulse  
    - Payments are mostly risk and compliance, not code → you still need banks/merchant accounts; middlemen add margin. — counterpoint: OSS can still reduce integration pain.  
    - Flowglad adds a network hop for every billing read → potential latency and N+1 API calls vs a single DB query with local Stripe mirrors.  
    - For AI/SaaS with rapidly changing usage pricing, abstracted billing logic is attractive → lets teams iterate experiments without constantly rewiring Stripe webhooks and state machines.

- LLM perspective  
    - View: This is essentially a Stripe-centric billing abstraction, not a full alternative processor; judge it on developer experience, not “owning” payments.  
    - Impact: Strongest fit is early-stage SaaS/AI teams without billing expertise, less so for high-volume or heavily regulated merchants.  
    - Watch next: Latency benchmarks, pricing versus direct Stripe, richer merchant-side state options, and support for non-Stripe gateways will determine adoption.
