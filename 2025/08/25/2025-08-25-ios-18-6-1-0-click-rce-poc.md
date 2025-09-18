# iOS 18.6.1 0-click RCE POC

- Score: 228 | [HN](https://news.ycombinator.com/item?id=45019671) | Link: https://github.com/b1n4r1b01/n-days/blob/main/CVE-2025-43300.md

TL;DR
An Apple zero‑click bug (CVE‑2025‑43300) in DNG image parsing was patched across iOS/iPadOS/macOS; a public “0‑click RCE” PoC exists but currently only crashes the target. HN flags the unusual single‑CVE security release as a severity signal. Defenders suggest Lockdown Mode and frequent reboots; investigators can scan iOS backups with ELEGANTBOUNCER for DNG exploit indicators. Discussion revisits Apple’s recurring ImageIO/iMessage attack surface despite BlastDoor, and how fuzzing-led research keeps surfacing parser flaws; one team even triggered an older DNG bug while reproducing.
- Content unavailable; summarizing from title/comments.

Comment pulse
- Single-CVE emergency patch across all Apple OSes → signals severity and likely active exploitation risk.
- PoC is DoS-only, not RCE → bypasses and a sandbox escape are needed for practical exploitation — counterpoint: decoder bugs often chain to full RCE.
- Discovery: guided fuzzing of ImageIO and reverse engineering keep finding parser bugs; P0 and Jackalope disclosed multiple ImageIO issues.

LLM perspective
- View: Image parsing remains a zero-click vector despite BlastDoor; parser complexity defeats perfect sandboxing.
- Impact: Rapid platform updates; high-risk users should enable Lockdown Mode; detection tools update to flag DNG exploit indicators.
- Watch next: Public RCE-grade PoCs, evidence of in-the-wild chaining, and movement toward memory-safe or verified image parsers.
