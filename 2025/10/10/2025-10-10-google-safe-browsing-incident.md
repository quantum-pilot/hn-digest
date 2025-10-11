# Google Safe Browsing incident

- Score: 186 | [HN](https://news.ycombinator.com/item?id=45538760) | Link: https://www.statichost.eu/blog/google-safe-browsing/

- TL;DR
  Statichost.eu was briefly flagged by Google Safe Browsing after phishing sites appeared on user subdomains, triggering deceptive‑site warnings across browsers that consume Google’s list (“5B+ devices”). The owner removed offenders, requested review, and was unblocked in ~6 hours, then criticized Google’s outsized gatekeeping and telemetry. HN replies: Safe Browsing behaved correctly; hosts should segregate user content on a separate domain and use the Public Suffix List; PSL can be obscure/slow; commenters also note wider, non‑Google blocking risks.

- Comment pulse
  - Safe Browsing worked; separate domain + Public Suffix List → signals unrelated tenants, avoids collateral blocks — counterpoint: PSL is obscure and approvals unpredictable.
  - It’s not just Google → ISPs, AV, DPI, and small operators can silently block; add NEL logging and probe paths with RIPE Atlas.
  - Hygiene for UGC hosts → moderate fast, isolate cookies, prefer __Host- cookies to prevent clobbering; expect blacklist cascades across browsers.

- LLM perspective
  - View: The blast radius comes from shared domains; treat user content like untrusted tenants and enforce automated, minute-level abuse triage.
  - Impact: Early detection reduces time-on-list; every hour multiplies downstream blocks via AVs, DNS resolvers, and Safe Browsing consumers.
  - Watch next: Statichost.page PSL submission; publish abuse-handling metrics; integrate Safe Browsing Lookup API and AV feedback loops for preemptive flags.
