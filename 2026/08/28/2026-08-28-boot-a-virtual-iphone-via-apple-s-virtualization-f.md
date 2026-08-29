# Boot a Virtual iPhone via Apple's Virtualization.framework

- Score: 239 | [HN](https://news.ycombinator.com/item?id=49485267) | Link: https://github.com/Lakr233/vphone-cli

### TL;DR

vphone-cli boots a full virtual iPhone image on Apple Silicon through Apple’s Virtualization.framework and PCC research-VM infrastructure. It requires macOS 15 or newer, Xcode, numerous build dependencies, and relaxed SIP and AMFI protections for private entitlements and unsigned code. Unlike Apple’s iOS Simulator, which runs specially compiled userspace components on macOS, this approach runs a separate iPhone kernel and userspace image. Commenters see uses in security research, testing, automation, and jailbroken environments, though hardware capabilities remain uncertain.

### Comment pulse

- Readers distinguished full-system virtualization from Simulator builds, citing different SDK targets, dependencies, kernels, and debugging possibilities.
- Questions remained about GPU access, localhost browser testing, virtual baseband support, and region-specific setup failures.
- Commenters attributed Japan and EU restrictions to regional entitlements, alternative marketplaces, location checks, side-button access, or possibly FeliCa.

### LLM perspective

- View: The project fills a research gap between lightweight Simulator compatibility and scarce, constrained physical test devices.
- Impact: Researchers can inspect current iOS behavior reproducibly, but host security must be deliberately weakened.
- Watch next: Document device services, networking, GPU behavior, snapshots, regional checks, and safe isolation of relaxed host protections.
