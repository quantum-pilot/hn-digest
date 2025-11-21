# Verifying your Matrix devices is becoming mandatory

- Score: 191 | [HN](https://news.ycombinator.com/item?id=45987179) | Link: https://element.io/blog/verifying-your-devices-is-becoming-mandatory-2/

### TL;DR
Element (Matrix’s main client) will, from April 2026, block unverified devices from sending or reading end‑to‑end‑encrypted messages. The goal is to eliminate confusing “untrusted device” warnings and ensure all devices are cryptographically tied to the account. Hacker News commenters broadly agree that stronger guarantees are good in theory but argue that Matrix/Element’s verification UX is brittle, often fails across devices, and risks effectively “offboarding” users. Others criticize Matrix’s metadata privacy and complexity, while a few say the policy is sound but badly communicated and sequenced.

---

### Comment pulse
- Verification UX is unreliable → devices randomly de‑verify, recovery fails, spoofed old devices persist; people waste time or give up, moving communities back to IRC/XMPP — counterpoint: some heavy users on self‑hosted servers report few issues.  
- Protocol trade‑offs worry users → content is E2E‑encrypted, but room names and social graph metadata remain visible to participating servers, making Matrix weaker than Signal for strong privacy.  
- Dev and policy maturity lag → bot authors struggled with E2EE until the Rust SDK; critics fear mandatory verification without first hardening flows, docs, and communication will accelerate churn.

---

### LLM perspective
- View: The policy is cryptographically sane but product‑risky: enforcing a flaky verification pipeline turns security hygiene into user lockout.  
- Impact: Casual and infrequent users, plus multi‑device setups, will bear the brunt; self‑hosted power users likely adapt smoothly.  
- Watch next: Clear deprecation of broken verification methods, metrics on verification success rates, and roadmap for encrypting more metadata and improving policy/moderation tools.
