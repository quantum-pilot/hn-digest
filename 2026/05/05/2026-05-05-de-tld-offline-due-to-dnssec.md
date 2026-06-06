# .de TLD offline due to DNSSEC?

- Score: 490 | [HN](https://news.ycombinator.com/item?id=48027897) | Link: https://dnssec-analyzer.verisignlabs.com/nic.de

### TL;DR
A bad DNSSEC signature in Germany’s .de top-level domain briefly made essentially every .de domain unreachable for validating DNS resolvers. DENIC appears to have published an RRSIG over an NSEC3 record that doesn’t validate against one ZSK, so resolvers correctly treat the whole .de zone as bogus and return SERVFAIL. Non‑validating resolvers and cached answers still work, causing intermittent behavior. HN discussion focuses on how a single misstep at a TLD can disable a country’s namespace and reignites debate over DNSSEC’s fragility vs. its security benefits.

---

### Comment pulse
- Root cause is a malformed RRSIG over an NSEC3 in .de → validating resolvers SERVFAIL all .de names; anycast explains intermittent success.  
- Operational angle: DENIC staff were reportedly at a party → highlights “bus factor” and sober access for emergency rollbacks.  
- DNSSEC design debate: some see a new central failure point → others argue DNS was always hierarchical and DNSSEC mainly adds verifiable integrity, not extra centralization.

---

### LLM perspective
- View: DNSSEC’s integrity guarantees are valuable, but TLD-scale key management and rollovers remain dangerously easy to misconfigure.  
- Impact: National registries, ISPs, and enterprises depending on validating resolvers must treat DNSSEC ops like safety-critical infrastructure.  
- Watch next: DENIC’s incident report, proposed tooling for automated pre-publish validation, and safer, staged deployment patterns for TLD key rollovers.
