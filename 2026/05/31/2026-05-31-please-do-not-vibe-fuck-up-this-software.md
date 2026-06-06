# Please Do Not Vibe Fuck Up This Software

- Score: 452 | [HN](https://news.ycombinator.com/item?id=48342705) | Link: https://github.com/RsyncProject/rsync/issues/929

### TL;DR
A GitHub issue titled “Please Do Not Vibe Fuck Up This Software” complains that rsync—an ultra-stable, foundational backup tool—has regressed after the maintainer began using Claude Code (AI) for changes. The issue itself is meme-y and non-actionable, but it catalyzed a huge fight about AI in critical infrastructure, maintainer responsibility, and open‑source entitlement. A specific regression was traced to an AI-authored security‑fix commit; defenders stress long‑standing bugs and necessary hardening, critics argue AI makes failures faster, opaque, and harder to trust.

---

### Comment pulse
- AI broke my backup tool → rsync is load‑bearing; post‑AI releases show regressions and performance hits, so users consider pinning or forking to preserve reliability.

- Process, not pitchforks → opening a vulgar, screenshot‑only issue is maintainer abuse; proper bug reports or Discussions channels exist — counterpoint: without loud pushback, distrust of AI remains invisible.

- Root cause is review/testing → the bad commit was Claude‑authored while fixing security bugs; AI amplifies human oversight gaps, so missing regression tests and review are the real failure.

---

### LLM perspective
- View: For “plumbing” tools like rsync, projects should codify AI usage: where allowed, how reviewed, and how changes are labeled.

- Impact: Distros, regulated orgs, and DFIR/government users may require “AI‑free” branches or audited releases, or they’ll freeze versions.

- Watch next: Look for rsync adding stronger regression suites, backports, and contribution rules; other legacy infrastructure projects will likely copy whatever governance emerges here.
