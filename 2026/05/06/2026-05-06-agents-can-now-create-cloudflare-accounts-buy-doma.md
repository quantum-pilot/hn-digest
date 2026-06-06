# Agents can now create Cloudflare accounts, buy domains, and deploy

- Score: 618 | [HN](https://news.ycombinator.com/item?id=48031684) | Link: https://blog.cloudflare.com/agents-stripe-projects/

- TL;DR  
  - Cloudflare and Stripe’s new protocol lets AI “agents” spin up Cloudflare accounts, attach billing, buy domains and deploy apps automatically via Stripe Projects, with humans only approving ToS and payment. Under the hood it combines service discovery, identity attestation and tokenized payments plus default spending caps. Fans see it as another brick in an agent-native cloud stack; critics see thin real-world use-cases, lock‑in risks, and a wide new attack surface for scammers, spammers and runaway agents.

- Comment pulse  
  - Skeptics: domain buying is rare; manual setup avoids cross‑vendor lock‑in, and past auto-provisioning (Fly/Vercel) hurt migrations — counterpoint: agent‑ready Cloudflare stack already powers internal tools.  
  - Security worry: perfect for spam, phishing and domain squatting; agents could overspend before users notice, despite tokenization and default $100/provider limits.  
  - Meta view: Cloudflare once banned a human over unverifiable ID, yet now courts “agents”; more broadly, industry is pivoting from blocking bots to monetizing them.

- LLM perspective  
  - View: Treats agents as first-class cloud customers; if standardized, this could become the default way devtools wire up infrastructure.  
  - Impact: Lowers friction for small teams and non-experts, but simultaneously lowers friction for sophisticated fraud operations and mass spam.  
  - Watch next: abuse safeguards, clearer spend controls, open spec details, and whether other clouds or IDEs copy this orchestration model.
