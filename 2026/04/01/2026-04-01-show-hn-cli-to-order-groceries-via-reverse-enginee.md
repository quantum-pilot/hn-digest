# Show HN: CLI to order groceries via reverse-engineered REWE API (Haskell)

- Score: 185 | [HN](https://news.ycombinator.com/item?id=47571183) | Link: https://github.com/yannick-cw/korb

### TL;DR

Korb is an unofficial Haskell CLI for REWE pickup shopping, exposing JSON commands for store selection, product and favorites search, basket editing, timeslots, checkout, order history, cancellation, receipts, and PKCE login. It targets agent workflows: a Siri-fed shopping list and prior-order template let Claude propose a basket, then a human reviews and confirms the order. Installation requires extracted REWE mTLS certificates, so API changes or enforcement could break it. Its deliberately overengineered bonus is a Lean 4 specification of the suggestion engine checked against Haskell with randomized differential tests.

### Comment pulse

- Readers wanted an official agent API or MCP endpoint, arguing explicit authentication and browser-side payment could preserve control while enabling automation.
- Publishing easier access divided commenters: it could demonstrate demand to REWE — counterpoint: it may provoke tighter restrictions on a deliberately locked-down API.
- Cross-store comparison and unit-price sorting emerged as desired extensions, with past observations of German-city price differences reaching 10–20%.

### LLM perspective

- **View:** The project’s practical value comes from converting recurring household intent into inspectable transactions, not autonomous purchasing.
- **Impact:** Formal methods become approachable when a small, bounded algorithm has an executable reference and randomized equivalence bridge.
- **Watch next:** Terms enforcement, credential handling, endpoint drift, release portability, failure recovery, and safeguards against accidental quantities.
