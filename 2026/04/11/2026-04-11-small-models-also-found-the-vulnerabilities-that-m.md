# Small models also found the vulnerabilities that Mythos found

- Score: 749 | [HN](https://news.ycombinator.com/item?id=47732020) | Link: https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier

### TL;DR

AISLE argues Anthropic’s Mythos results do not prove exclusive frontier-model capability. Given isolated vulnerable functions and hints, eight smaller models found the showcased FreeBSD overflow; a 5.1B-active model reconstructed the OpenBSD SACK chain, while small models sometimes beat frontier systems on a trivial false-positive test. Performance reshuffled sharply by task, supporting a “jagged frontier” where orchestration, targeting, validation, cost, and maintainer trust matter more than one model. Yet most models falsely flagged patched FreeBSD code, and none reproduced Mythos’s creative multi-request exploit delivery, underscoring the need for triage and tooling.

### Comment pulse

- Critics say identifying a hinted function is verification, not repo-scale discovery. — counterpoint: supporters argue scaffolds create precisely that decomposition.
- Mythos searched roughly 1,000 times for under $20,000; readers want comparable end-to-end recall, false-positive rates, and verified exploits from open models.
- Some see cheap exhaustive per-function scans plus frontier triage as viable; others insist attackers make the missing 20% strategically decisive.

### LLM perspective

- **View:** The experiment demonstrates analysis accessibility, not equivalent autonomous discovery; both claims can coexist without diminishing either system.
- **Impact:** Defenders may combine broad cheap scanning with expensive verification, but noise management becomes the operational bottleneck.
- **Watch next:** Blind full-repository trials measuring cost, coverage, false positives, exploit validation, patch quality, and maintainer acceptance.
