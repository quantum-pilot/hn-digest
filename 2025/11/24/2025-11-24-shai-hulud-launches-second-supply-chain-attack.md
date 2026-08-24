# Shai Hulud launches second supply-chain attack

- Score: 339 | [HN](https://news.ycombinator.com/item?id=46035533) | Link: https://www.aikido.dev/blog/shai-hulud-strikes-again-hitting-zapier-ensdomains

### TL;DR

A second Shai-Hulud wave compromised hundreds of npm packages associated with AsyncAPI, PostHog, Postman, Zapier, ENS, and others shortly before classic-token revocation. Malicious preinstall code installed Bun, ran a large worm payload, scanned machines for cloud and registry credentials, published stolen secrets in randomly named public repositories, then republished itself through captured npm access. This version targeted up to 100 packages per victim and threatened home-directory deletion when authentication failed. Some propagated packages omitted the payload, unintentionally limiting execution.

### Comment pulse

- Sandboxing won support → Bubblewrap can restrict install-time damage without full containers, though commenters stressed it is no complete defense.
- Thread consolidation was contested → readers argued separate reports added distinct technical detail despite covering the same campaign.
- Naming caused confusion → the worm is Shai-Hulud, while its exfiltration repositories deliberately use the SHA1-styled label.

### LLM perspective

- View: Install hooks converted trusted package updates into credential-harvesting launchers, then used stolen publisher access as the replication channel.
- Impact: Affected teams must treat developer machines, CI environments, cloud accounts, and package releases as potentially compromised.
- Watch next: Token rotation, malicious-repository cleanup, package provenance, and evidence that the initial access path has been closed.
