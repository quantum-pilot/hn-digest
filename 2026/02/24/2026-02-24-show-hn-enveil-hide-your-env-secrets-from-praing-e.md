# Show HN: enveil – hide your .env secrets from prAIng eyes

- Score: 189 | [HN](https://news.ycombinator.com/item?id=47133055) | Link: https://github.com/GreatScott/enveil

### TL;DR

Enveil is a Rust CLI intended to keep project secrets out of plaintext `.env` files and away from coding assistants’ routine file access. Templates contain `ev://` references; values live in a per-project AES-256-GCM store unlocked with an Argon2id-derived key, then enter a launched subprocess through environment variables. It offers interactive set, import, delete, rotate, and run commands but deliberately no value-printing or export command. The design limits accidental disk ingestion, not a malicious or shell-capable agent running as the same user, which can inspect the child environment.

### Comment pulse

- Same-user processes can read injected variables or alter code to print them — counterpoint: avoiding accidental file ingestion remains useful.
- Several favor surrogate credentials resolved by an inaccessible proxy, creating scoped, revocable authority without exposing real secrets to the agent.
- Critics recommend established tools such as SOPS or dotenvx and flag unzeroized strings, brute-force concerns, and overly broad security claims.

### LLM perspective

- **View:** This is encrypted secret storage, not a boundary against an agent with equivalent OS privileges.
- **Impact:** It can reduce casual leaks while leaving logs, crashes, source, and process inspection exposed.
- **Watch next:** Threat-model clarification, external audit, keychain support, and isolation or proxy integrations.
