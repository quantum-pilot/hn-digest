# Shai Hulud launches second supply-chain attack

- Score: 339 | [HN](https://news.ycombinator.com/item?id=46035533) | Link: https://www.aikido.dev/blog/shai-hulud-strikes-again-hitting-zapier-ensdomains

### TL;DR

Security vendor Aikido reports a second Shai-Hulud npm worm wave affecting 492 packages with 132 million combined monthly downloads. Malicious preinstall files impersonate Bun setup, scan machines for credentials with TruffleHog, publish stolen data in public GitHub repositories, and use captured npm access to propagate; the report says failed GitHub or npm authentication can trigger home-directory deletion. Its developing count included 26,300 exposed repositories. Some packages carried only the stager, which may have limited execution.

### Comment pulse

- Sandboxing installs can reduce damage → Bubblewrap limits filesystem and process access, though it is not a complete defense.
- Incident threads were merged despite different reports → readers distinguished duplicate events from independently useful technical analysis.
- Naming caused confusion → the worm is Shai-Hulud, while its repositories deliberately use the “Sha1-Hulud” spelling.

### LLM perspective

- View: Install-time code plus durable developer credentials turns one compromised publisher into an automated trust cascade.
- Impact: Teams must treat dependency installation as untrusted execution across laptops, CI, registries, and cloud accounts.
- Watch next: Reconcile package counts, identify initial access, audit exposed secrets, and verify cleanup across affected publishers.
