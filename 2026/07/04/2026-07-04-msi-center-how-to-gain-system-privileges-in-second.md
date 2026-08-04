# MSI Center – How to gain SYSTEM privileges in seconds

- Score: 138 | [HN](https://news.ycombinator.com/item?id=48781688) | Link: https://mrbruh.com/msicenter/

### TL;DR

MSI Center’s LocalSystem Notebook Foundation service exposed a named pipe to every authenticated user. Its custom 3DES protocol accepted arbitrary client registrations, then enabled registry and WMI changes plus execution of any program as LocalSystem; authenticated LAN users could also reach it through SMB. MSI patched the flaw within two days and shipped 2.0.70.0 on June 1; it became CVE-2026-37452. HN welcomed the response but criticized opaque remediation, a misleadingly full security mailbox, zero bounty, and dependence on fragile OEM software for fan, battery, lighting, and performance controls.

### Comment pulse

- Patch details matter → commenters report signed MSI clients and executables are now required, but the article offers no design or verification evidence.
- Users cannot simply uninstall it → battery thresholds, fan curves, GPU/CPU profiles, lighting, and sometimes updates lack convenient firmware-level alternatives.
- Unpaid research invites exploitation → multiple vendors paid $0 — counterpoint: responsible disclosure can serve public safety without direct compensation.

### LLM perspective

- **View:** The core failure was treating any authenticated user as authorized for privileged commands; obsolete encryption merely obscured it.
- **Impact:** Preinstalled control utilities can turn an ordinary compromised account into full-machine compromise across large OEM fleets.
- **Watch next:** Confirm update coverage, pipe ACLs, executable allowlists, remote SMB exposure, and whether vulnerable installers remain downloadable.
