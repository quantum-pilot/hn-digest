# x402 — An open protocol for internet-native payments

- Score: 198 | [HN](https://news.ycombinator.com/item?id=45347335) | Link: https://www.x402.org/

TL;DR
- Coinbase’s x402 proposes an HTTP 402–based, web-native way to gate API calls with payments: client gets 402, pays (often USDC on low‑fee L2s), retries, settles fast. Claims zero protocol fees, minimal integration, and blockchain‑agnostic micropayments for agents, storage, and content. HN likes an open alternative to Stripe-style lock‑in, but flags “no fees” marketing, Coinbase/Base dependence, and no Lightning/Bitcoin. One test saw a lost transaction and weak wallet tooling. Lightning’s L402 adds in-protocol receipts; others prefer EVMs for agent automation.

Comment pulse
- Zero-fee claim is marketing → blockchains charge gas; L2s subsidize or sub‑cent, but volatility and per-tx costs threaten micropayment economics — counterpoint: facilitators absorb gas.
- Open standard vs Coinbase stack → critics prefer Bitcoin/Lightning (L402) with macaroon auth and in-protocol receipts; x402’s out-of-band verification challenges the “one line” claim.
- Early UX concerns → a test saw a lost tx, no wallet logs, and double-pay risk; second attempt settled quickly.

LLM perspective
- View: Pay-gated APIs are useful for agents; require protocol-level receipts, idempotency, and replay protection to avoid double-charges.
- Impact: Low-friction pay-per-call could shift SaaS pricing; wallets/facilitators become core infra, not just UX.
- Watch next: Independent implementations, Lightning support, standardized proof-of-payment headers, retry semantics, and benchmarks on cost, latency, and failure modes.
