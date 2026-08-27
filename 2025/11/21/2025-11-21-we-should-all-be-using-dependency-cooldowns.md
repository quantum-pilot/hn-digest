# We should all be using dependency cooldowns

- Score: 257 | [HN](https://news.ycombinator.com/item?id=46005111) | Link: https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns

### TL;DR

The proposal is to delay adoption of newly published dependency versions by seven to fourteen days, reducing exposure during the period when many supply-chain attacks are discovered and removed. Package tooling already offers minimum-age or date-cutoff controls, and known security advisories can justify exceptions. The article’s ten-incident sample suggests cooldowns would have avoided most cases, but that selected retrospective evidence is not a universal protection rate. Slow or stealthy compromises remain possible, while compliance pressure and urgent patches complicate a blanket delay.

### Comment pulse

- Readers emphasized bypassing cooldowns for verified security fixes rather than treating every update identically.
- Others favored stable distributions, long-term support, and fewer dependencies as complementary risk reduction.

### LLM perspective

- View: A cooldown is a cheap quarantine layer, not a substitute for advisories, review, or dependency restraint.
- Impact: Separating routine freshness from urgent remediation reduces one avoidable supply-chain exposure window.
- Watch next: Tooling that applies exceptions transparently without turning every flagged vulnerability into an automatic upgrade.
