# Internet voting is insecure and should not be used in public elections

- Score: 426 | [HN](https://news.ycombinator.com/item?id=46713924) | Link: https://blog.citp.princeton.edu/2026/01/16/internet-voting-is-insecure-and-should-not-be-used-in-public-elections/

## TL;DR
A group of 21 leading election‑security researchers argue that internet voting, including “end‑to‑end verifiable” cryptographic schemes, cannot be made safe with current or foreseeable technology. Malware on voter devices, servers, or election offices can change large numbers of votes undetectably, unlike paper systems where fraud is localized and visible. They dissect the VoteSecure mobile‑voting SDK, showing it permits vote‑selling, lacks dispute resolution, and admits unsolved endpoint‑security limits. HN comments largely favor paper ballots and emphasize trust over efficiency.

## Comment pulse
- Paper ballots → Cheating methods and countermeasures are well-known; failures are local and obvious, enabling observation, recounts, and public trust—unlike silent, large‑scale digital failure.
- Secret ballot and coercion → Systems that let you verify your vote also risk proving it to coercers, undermining receipt‑freeness and enabling vote‑buying at scale.
- Tradeoffs vs banking analogy → Banking fraud is traceable, reversible, and non‑anonymous; election fraud is anonymous, irreversible, and existential, so “online banking works” doesn’t transfer.

## LLM perspective
- View: The bottleneck isn’t cryptography; it’s hostile endpoints, coercion, and lack of credible dispute‑resolution in anonymous, remote contexts.
- Impact: High‑stakes public elections should stay paper‑based with audits; experiments belong in low‑stakes, opt‑in or organizational governance.
- Watch next: Rigorous pilot studies, formal threat models including nation‑states, and better public audit practices for existing paper‑plus‑scanner systems.
