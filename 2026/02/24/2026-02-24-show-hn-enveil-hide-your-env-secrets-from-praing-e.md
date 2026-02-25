# Show HN: enveil – hide your .env secrets from prAIng eyes

- Score: 189 | [HN](https://news.ycombinator.com/item?id=47133055) | Link: https://github.com/GreatScott/enveil

- TL;DR  
  - enveil is a Rust CLI that replaces plaintext .env secrets with ev:// placeholders, storing real values in an encrypted per-project vault and injecting them only at process launch. It’s aimed at stopping AI coding tools from casually reading secrets from project directories. HN agrees this mitigates one common footgun but stresses it doesn’t protect secrets once loaded into a running process, and questions rolling custom crypto for such a narrow threat model.

- Comment pulse  
  - Narrow win: prevents AI assistants from accidentally ingesting .env files → but environment variables remain readable to any same-user process, including agent shells and debug tools.  
  - Broader threat: secrets leak via logs, traces, hardcoded keys; static analyzers and pipeline hygiene help most — counterpoint: .env is still a frequent failure.  
  - Many prefer sops/dotenvx or credential-injecting proxies (Airut, OrcaBot) over new env tools; cryptography reviewers criticize enveil’s design and advise avoiding rolled-by-hand schemes.

- LLM perspective  
  - View: enveil is pragmatic for solo devs using local AI assistants, but not a comprehensive secret-management or agent-safety solution.  
  - Impact: cuts low-effort leaks from AI file reads; serious teams still need Vault/KMS, log scrubbing, and hardened agent sandboxes.  
  - Watch next: patterns combining local secret stores, surrogate credentials, and MCP-like brokers that keep raw secrets outside any LLM process.
