# A monopoly ISP refuses to fix upstream infrastructure

- Score: 579 | [HN](https://news.ycombinator.com/item?id=46019685) | Link: https://sacbear.com/xfinity-wont-fix-internet/

### TL;DR
Over 17 months, a Sacramento Xfinity customer logs 3,300+ identical outages: ~125 seconds each, clustering at specific minute marks (:29, :44) and hours (noon, 2–3 AM). A neighbor on a different drop sees the same pattern. Modem and router are swapped, cabling is replaced, yet the outages persist and speeds drop by half. Frontline support can’t interpret logs, can’t escalate, and doesn’t care—shielded by Xfinity’s local monopoly. The article also documents insecure, often‑unlocked junction boxes and urges regulatory complaints.

---

### Comment pulse
- This is classic Comcast/DOCSIS: intermittent upstream failure, endless “inside wiring” blame, real fix only when outside plant or node is touched.  
- Likely root cause: R‑PHY node software/PNM job periodically crashing upstream; 125 s matches modem resync, not a deliberate timeout — counterpoint: commenters dislike unverified LLM-style diagnoses.  
- Reliable 6 Mbps DSL or 5G beats flaky “gigabit” cable; fiber and municipal competition instantly improve incumbent behavior, especially via mayors, commissions, and public escalation.

---

### LLM perspective
- View: The case is evidence that monopoly consumer broadband behaves like an unregulated utility with no service-quality obligation.  
- Impact: Remote work, home security, and small businesses disproportionately suffer from “tolerable” micro-outages that ISPs won’t prioritize.  
- Watch next: Municipal/open-access fiber builds, mandated reliability SLAs, and tools exposing node-level telemetry to regulators rather than only to ISPs.
