# Reverse engineering a $1B Legal AI tool exposed 100k+ confidential files

- Score: 437 | [HN](https://news.ycombinator.com/item?id=46137514) | Link: https://alexschapiro.com/security/vulnerability/2025/12/02/filevine-api-100k

- TL;DR  
  A researcher probing Filevine, a billion‑dollar legal AI platform, found a forgotten subdomain whose JS revealed an unauthenticated AWS API. Calling it returned a fully scoped Box admin token for a law firm’s entire document store, surfacing ~100k “confidential” files before testing stopped. Filevine patched the issue after responsible disclosure. Hacker News focuses on how AI‑era vendors handle client secrets, whether naming the company is fair, slow remediation pipelines, and the need for serious bug bounties.

- Comment pulse  
  Naming the vendor is part of responsible disclosure → signals which firms take security seriously and informs customers—counterpoint: some prefer anonymity when companies respond well.  
  Patching took weeks because of org friction → routing reports, ownership confusion, overloaded teams, rigid roadmaps, and weak CI/CD often dwarf the one‑hour code fix.  
  Bug had billion‑dollar blast radius → commenters argue researcher deserved serious bounty; poor incentives push some to sell vulns privately instead of disclosing.

- LLM perspective  
  View: This is a textbook over‑privileged token leak, not an AI quirk; any SaaS centralizing sensitive docs risks identical failures.  
  Impact: Legal, medical, and finance sectors adopting AI copilots should assume compromise and demand third‑party audits, red‑teaming, and explicit token‑scoping.  
  Watch next: Expect regulators and bar associations to treat AI vendors as client‑data custodians, adding breach‑notification, security attestations, and shared liability.
