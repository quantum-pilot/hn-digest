# Email obfuscation: What works in 2026?

- Score: 334 | [HN](https://news.ycombinator.com/item?id=47609694) | Link: https://spencermortensen.com/articles/email-obfuscation/

### TL;DR

A long-running honeypot assigns a unique address to each obfuscation technique and infers failures from spam received. Among 426 plain-text harvesters, entities blocked 95%, comments 99%, and SVG, display:none decoys, JavaScript conversion, encryption, or interaction showed 100% blocking; similar link tests covered 399 harvesters. These are observed sample results, not guarantees, and some methods damage copying or accessibility. The author favors layered, usable defenses, while HN notes many addresses instead leak through breaches, contact uploads, guessed aliases, or marketing lists, and modern filters may suffice.

### Comment pulse

- Simple entities may work because many harvesters scan raw bytes around the at-sign rather than fully parsing HTML.
- Some users report negligible spam despite public addresses—counterpoint: others receive over 1,500 monthly messages after corporate publication.
- Per-recipient aliases expose leaks and permit blocking; sender whitelists offer similar control with less address management.

### LLM perspective

- **View:** Obfuscation is an inexpensive probabilistic filter, not secrecy; any browser-recoverable address remains recoverable by capable automation.
- **Impact:** Small sites can deter commodity harvesting without burdening users if they preserve selection, accessibility, and no-JavaScript fallbacks.
- **Watch next:** Larger samples, AI-enabled browser harvesters, long-term decay by technique, and measurements separating scraped spam from breached lists.
