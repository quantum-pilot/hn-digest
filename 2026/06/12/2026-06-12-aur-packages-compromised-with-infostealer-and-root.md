# AUR packages compromised with Infostealer and Rootkit

- Score: 299 | [HN](https://news.ycombinator.com/item?id=48500447) | Link: https://discourse.ifin.network/t/400-aur-packages-compromised-with-infostealer-and-rootkit/577

### TL;DR
A malicious actor impersonated a trusted Arch User Repository (AUR) maintainer, adopted >400 orphaned packages, and injected pre-install steps that pulled an infostealer plus an eBPF-based rootkit via npm (`atomic-lockfile`) and later Bun (`js-digest`). Arch maintainers believe all malicious commits are now reverted and are tightening rules around package adoption. Users are urged to check for affected packages, rotate credentials, and consider full reinstalls if compromised. Discussion centers on AUR’s trust model, orphaned package adoption, and realistic security expectations for users.

---

### Comment pulse
- AUR is inherently untrusted user PKGBUILDs → users “must” review every PKGBUILD and update—counterpoint: this is unrealistic and doesn’t cover deep dependency chains.  
- Orphaned-package adoption is the main weak point → anyone can take over abandoned packages; proposals: disallow adoption, force new submissions, purge stale orphans, or loudly flag ownership changes.  
- Communication/UX criticized → some want front-page banners and AUR disruption; others argue AUR always warns it’s unsafe and maintainers can’t track installs or police helpers.

---

### LLM perspective
- View: This is a textbook open-source supply-chain attack exploiting weak ownership controls and transitive dependency trust.  
- Impact: Arch/AUR users now, but the pattern threatens all ecosystems built on volunteer-maintained, auto-updated packages.  
- Watch next: Stronger adoption policies, ownership-change alerts in helpers, dependency provenance/signing tools, and automated scanning for install-time network activity.
