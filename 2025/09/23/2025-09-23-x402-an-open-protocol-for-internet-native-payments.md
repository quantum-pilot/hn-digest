# x402 — An open protocol for internet-native payments

- Score: 198 | [HN](https://news.ycombinator.com/item?id=45347335) | Link: https://www.x402.org/

### TL;DR

x402 uses HTTP 402 responses and headers to let clients pay for APIs or content without accounts, email, OAuth, or elaborate signatures. The site presents it as blockchain-agnostic, instant, fee-free at the protocol layer, and suitable for agents, storage, creators, and micropayments; its example charges USDC per request through middleware. Commenters welcomed an open alternative to proprietary payment APIs but challenged the framing: underlying networks may charge fees, Coinbase sponsors the protocol and promotes Base, and one test produced an ambiguous transaction that risked duplicate payment.

### Comment pulse

- HTTP-native payment can simplify machine commerce → agents could pay per request without account provisioning.
- Protocol neutrality is disputed → nominal chain agnosticism coexists with Coinbase sponsorship and a Base-centered ecosystem.
- Payment reliability needs stronger semantics → pending transactions, retries, receipts, refunds, and duplicate prevention remain practical concerns.

### LLM perspective

- View: Standardizing the challenge-response flow solves integration, not settlement trust or consumer protection.
- Impact: APIs could monetize small requests while shifting wallet and network complexity to clients and facilitators.
- Watch next: Test idempotency, multi-chain support, privacy, disputes, fee disclosure, facilitator portability, and failure recovery.
