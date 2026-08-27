# Track which Electron apps slow down macOS 26 Tahoe

- Score: 144 | [HN](https://news.ycombinator.com/item?id=45469468) | Link: https://avarayr.github.io/shamelectron/

### TL;DR

Shamelectron tracked 33 Electron applications affected by a macOS 26 Tahoe GPU-performance regression, listing six fixed and 27 awaiting upgrades at capture time. Developers were urged to move to Electron 38.2.0, 37.6.0, or 36.9.2. HN discussion traced the issue to Electron’s cosmetic use of a private Apple window API that prevented efficient rendering under Tahoe. Readers blamed both framework risk-taking and Apple’s limited compatibility testing, while noting the framework fix was already available and app vendors remained the delivery bottleneck.

### Comment pulse

- Private APIs create hidden upgrade debt → cosmetic behavior depended on an unsupported method whose rendering assumptions changed.
- Apple shares ecosystem responsibility → commenters argued beta testing could identify widespread framework breakage before release.
- Local inventory beats public shaming → a script can find installed affected apps and focus update pressure.

### LLM perspective

- View: Shared runtimes concentrate both remediation speed and delayed-distribution risk across many unrelated products.
- Impact: Tahoe users may see excess GPU or memory use until each vendor ships a newer Electron.
- Watch next: Track vendor releases, remaining app counts, Tahoe patches, energy measurements, private-API scans, and regression tests.
