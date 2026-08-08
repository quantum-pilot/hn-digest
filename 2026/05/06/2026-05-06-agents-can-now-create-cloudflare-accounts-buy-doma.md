# Agents can now create Cloudflare accounts, buy domains, and deploy

- Score: 618 | [HN](https://news.ycombinator.com/item?id=48031684) | Link: https://blog.cloudflare.com/agents-stripe-projects/

### TL;DR

Cloudflare and Stripe introduced an open-beta provisioning flow that lets coding agents discover services, create or link a Cloudflare account, receive API credentials, register a domain, start paid products, and deploy an application through Stripe Projects. Stripe attests the signed-in user’s identity and supplies tokenized payment; agents never see card details, while humans approve permissions and accept terms. A default $100 monthly cap applies per provider. Commenters saw a missing last mile for app-building platforms, but worried about fraud automation, runaway purchases, cross-vendor lock-in, and weak recovery paths.

### Comment pulse

- Supporters framed this as production plumbing for app builders — counterpoint: rare domain purchases may deserve careful manual setup.
- Security fears focused on tailored scam sites, domain squatting, and bots receiving privileges once reserved for verified humans.
- Past bundled accounts raised portability concerns: inaccessible provider accounts can make migration, ownership transfer, or incident recovery painful.

### LLM perspective

- Provisioning moves the agent boundary from code generation into legal, financial, and operational commitments.
- Controls need per-action approval, domain allowlists, irreversible-action delays, complete audit trails, and immediate revocation.
- Watch the promised specification, additional orchestrators, dispute handling, ownership transfer, and legitimate production adoption.
