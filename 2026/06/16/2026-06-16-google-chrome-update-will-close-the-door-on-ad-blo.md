# Google Chrome update will close the door on ad blockers

- Score: 262 | [HN](https://news.ycombinator.com/item?id=48555244) | Link: https://9to5google.com/2026/06/15/google-chromes-next-update-will-mark-the-end-of-popular-ad-blockers/

### TL;DR

Chrome 150 will remove the hidden flag that still let power users run Manifest V2 extensions, and Chrome 151 is expected to delete the remaining legacy flags. That effectively ends original uBlock Origin support in Chrome, though Manifest V3 blockers such as uBlock Origin Lite still function with reduced block coverage, extension-bound updates, and no dynamic filtering. Google cites maintenance debt, complexity, and security bugs. HN treated the cutoff as another reason to adopt Firefox or browsers with built-in blocking, while debating whether Chromium forks can sustainably preserve independent protections.

### Comment pulse

- Browser-engine diversity is strategic → Firefox’s imperfections matter less than preventing Google’s Chromium decisions from becoming de facto web policy.
- Forks offer partial escape → Brave hosts four MV2 extensions itself, while Vivaldi embeds blocking — counterpoint: upstream dependence still creates maintenance risk.
- Lite’s adequacy depends on threat model → users report no ads, but it lacks dynamic filtering, element picking, custom lists, and independent ruleset updates.

### LLM perspective

- **View:** Extension APIs are governance infrastructure; capability limits determine whether users or publishers control page behavior.
- **Impact:** Power users migrate or lose granular controls; ordinary users may notice little until advertisers adapt around static rules.
- **Watch next:** Track Chrome 150/151 rollout, Lite bypass rates, Firefox share, fork maintenance commitments, and built-in blocker performance.
