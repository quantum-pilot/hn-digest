# NPM debug and chalk packages compromised

- Score: 1346 | [HN](https://news.ycombinator.com/item?id=45169657) | Link: https://www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised

- TL;DR
  - On Sept 8, attackers phished a maintainer (chalk/debug), publishing new versions of 18 widely used npm packages. The payload injects into fetch/XMLHttpRequest and wallet APIs (MetaMask/Solana), silently rewriting addresses and token approvals; it even picks attacker addresses via Levenshtein similarity to the originals to defeat “first/last chars” checks. Community reacted fast, but NPM’s slow response drew criticism. Suggested fixes: delayed/multi-party publishing, code/artifact signing, stronger scanning. Short-term: pin/yank known-bad versions, reinstall, and scan for the malware’s signature (e.g., _0x112fa8).

- Comment pulse
  - Root cause → maintainer phished via realistic npm support email; affected versions listed; account recovery delays slowed yanks.
  - Payload detail → Levenshtein-based address substitution defeats eyeballing — counterpoint: it’s a familiar lookalike tactic, not unprecedented “genius.”
  - Platform fixes → mandate code signing, co-maintainer approvals, delayed publishes; others note trade-offs and human fallibility; AI can help both attack and defense.

- LLM perspective
  - View: Classic supply-chain plus runtime API hooking; mass obfuscation + simultaneous publishes were detectable with pre-publish scanning.
  - Impact: Web apps bundling tainted versions risk client-side wallet theft; CI/CD must pin exact versions and quarantine unexpected diffs.
  - Watch next: NPM policy on delayed/multi-party releases, automated obfuscation heuristics, full IoCs list, and verified “clean” republish timelines.
