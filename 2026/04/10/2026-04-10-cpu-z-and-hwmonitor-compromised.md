# CPU-Z and HWMonitor compromised

- Score: 241 | [HN](https://news.ycombinator.com/item?id=47717847) | Link: https://www.theregister.com/2026/04/10/cpuid_site_hijacked/

### TL;DR
CPUID’s website, home to popular utilities CPU‑Z and HWMonitor, was hijacked for about six hours (April 9–10 UTC). A compromised “side API” intermittently swapped legitimate download links for malware, though the original binaries and signing keys appear untouched. The malicious HWMonitor installer used a fake CRYPTBASE.dll, fileless techniques with PowerShell and in‑memory .NET payloads, and targeted browser credentials via Chrome APIs. HN discussion focused on trust in small utility vendors, confusing ad-heavy download pages, AV false positives, and the role of package managers.

---

### Comment pulse
- Maintainer responsiveness → Sam from CPUID confirmed the breach, restored correct links, put site in read‑only, noting attackers struck while lead dev was away.
- Download UX as attack surface → Ad-heavy pages with fake “Download” buttons train users to click blindly; CLIs like winget reduce confusion—counterpoint: winget mostly wraps installers, not a strong security boundary.
- Detection and trust → AV false positives, especially around cracks, habituate users to ignore real alerts; commenters want source-based distros, reproducible builds, or reputation systems for random EXEs.

---

### LLM perspective
- View: Supply-chain attacks increasingly target web delivery layers and CDNs, not build systems, because that’s where user trust is weakest.
- Impact: Small utility authors inherit “critical software” risk without matching security budgets; users need better defaults than “download random EXE, hope AV helps.”
- Watch next: Wider package-manager coverage, stronger signing and transparency logs for Windows apps, and tools scoring reputation of arbitrary installers before execution.
