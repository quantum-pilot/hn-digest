# CPU-Z and HWMonitor compromised

- Score: 241 | [HN](https://news.ycombinator.com/item?id=47717847) | Link: https://www.theregister.com/2026/04/10/cpuid_site_hijacked/

### TL;DR

Attackers compromised a secondary CPUID website API for roughly six hours across April 9–10, randomly replacing CPU-Z and 64-bit HWMonitor download links with malicious installers. CPUID says its original builds and signatures remained intact. The fake HWMonitor package used a deceptive CRYPTBASE.dll, PowerShell, in-memory execution, locally compiled .NET code, process injection, and Chrome credential-access mechanisms while fetching further payloads. The links are fixed, but entry method and victim count remain unknown. Commenters blamed confusing ad-heavy download pages and alert fatigue, while debating whether WinGet meaningfully reduces such supply-chain risk.

### Comment pulse

- A maintainer restored links and made them read-only while investigating; attackers may have timed the breach around staff availability.
- Repeated antivirus false positives train users to dismiss genuine warnings, especially when tools, cracks, or installers commonly trigger detection.
- WinGet offers hashes and familiar commands — counterpoint: shallow manifest review may not stop malicious releases after an upstream compromise.

### LLM perspective

- **View:** Signed binaries protect builds, not distribution; trustworthy delivery requires authenticated links, independent metadata, and monitoring at every redirect layer.
- **Impact:** Anyone downloading during the window faces credential theft and secondary payload risk despite visiting the legitimate site.
- **Watch next:** Indicators of compromise, victim scope, API entry point, credential rotation guidance, infrastructure hardening, and a complete incident report.
