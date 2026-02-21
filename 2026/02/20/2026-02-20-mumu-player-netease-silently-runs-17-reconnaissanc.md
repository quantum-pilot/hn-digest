# MuMu Player (NetEase) silently runs 17 reconnaissance commands every 30 minutes

- Score: 308 | [HN](https://news.ycombinator.com/item?id=47082496) | Link: https://gist.github.com/interpiduser5/547d8a7baec436f24b7cce89dd4ae1ea

TL;DR  
MuMu Player Pro, a macOS Android emulator from NetEase, silently runs 17 system commands every 30 minutes, logging processes, installed apps, network topology, DNS, hosts file, and kernel parameters. These logs are tied to the Mac’s serial number via Chinese analytics provider SensorsData, yet none of this collection is disclosed in the privacy policy or needed for emulation. HN discussion focuses on Chinese software as a security risk, mitigation via sandboxing/VLANs, and comparisons to Western data-harvesting practices.

Comment pulse  
- Chinese games/emulators seen as threats → Hidden telemetry plus kernel anticheat could enable lateral movement; some isolate gaming rigs on VLANs — counterpoint: still leaves box online.  
- Sandbox everything, not just Chinese apps → Users run risky software in VMs or mobile sandboxes, restrict file access, and firewall LAN to limit unavoidable analytics.  
- Debate over singling out China → Some say all tech firms abuse data, others argue Chinese-state ties and weak ethics justify suspicion and potential platform bans.

LLM perspective  
- View: This behavior fits enterprise-grade endpoint surveillance patterns, not consumer gaming; regulators will view it as undisclosed spyware.  
- Impact: Apple may strengthen notarization checks, process-list access policies, or silently revoke certificates for similar high-volume recon tools.  
- Watch next: independent packet captures, reverse-engineering of upload behavior, and eventual inclusion in threat intel feeds or antivirus signatures.
