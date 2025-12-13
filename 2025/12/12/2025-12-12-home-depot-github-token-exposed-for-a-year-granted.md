# Home Depot GitHub token exposed for a year, granted access to internal systems

- Score: 162 | [HN](https://news.ycombinator.com/item?id=46247000) | Link: https://techcrunch.com/2025/12/12/home-depot-exposed-access-to-internal-systems-for-a-year-says-researcher/

- TL;DR  
  Home Depot left a GitHub access token exposed for roughly a year, granting write access to hundreds of private repos and connected cloud systems, including order fulfillment and inventory. Researcher Ben Zimmermann responsibly disclosed the issue but was ignored; only after TechCrunch intervened did Home Depot revoke the token. The company hasn’t said whether it can tell if others abused it. HN discussion focuses on corporate legal/PR silence, GitHub’s token-scanning limits, and the real potential for financial or supply-chain abuse.

- Comment pulse  
  Legal-first response → Once media was contacted, lawyers likely ordered silence to avoid liability—counterpoint: this stonewalling further erodes trust after security lapses.  
  Detection gap → GitHub often auto-revokes exposed PATs; long-lived leak suggests self-hosted or poorly configured scanning for internal tokens.  
  Risk framing → Access to inventory and internal data could enable theft, fraud, or insider trading, not just source-code compromise.

- LLM perspective  
  View → This is a governance failure: no disclosure channel, weak secret hygiene, and unclear logging/forensics capabilities.  
  Impact → Retailers and other enterprises with GitHub-based pipelines must revisit secret management, repo access scopes, and incident-response playbooks.  
  Watch next → Look for regulators asking about logs, required VDPs, and mandatory secret scanning in supply-chain security standards.
