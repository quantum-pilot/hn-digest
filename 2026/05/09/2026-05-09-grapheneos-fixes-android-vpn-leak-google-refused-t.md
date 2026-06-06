# GrapheneOS fixes Android VPN leak Google refused to patch

- Score: 261 | [HN](https://news.ycombinator.com/item?id=48075144) | Link: https://cyberinsider.com/grapheneos-fixes-android-vpn-leak-google-refused-to-patch/

### TL;DR
A researcher found that on Android 16, any ordinary app could abuse a new QUIC connection-teardown optimization so that Android’s privileged `system_server` sent arbitrary UDP packets directly over the physical network, bypassing VPN routing—even with “Always-On VPN” and “Block connections without VPN” enabled. Google labeled the issue “Won’t Fix” and not bulletin-worthy. Privacy-focused GrapheneOS responded by disabling the offending optimization for supported Pixels and shipping the change rapidly in an OS update; stock Android users only have a fragile ADB-based workaround.

---

### Comment pulse
- VPN lockdown isn’t absolute on major OSes → privileged system components on Android, iOS, and macOS can bypass VPN tunnels by design.
- Users see a pattern → limiting true network lockdown, Manifest V3, and weakened E2EE all align with data-collection business incentives.
- Classification criticized → calling a kernel-level bypass of VPN lockdown “not security bulletin class” undermines trust in Android’s security promises.

---

### LLM perspective
- View: VPN “lockdown” needs a formal, verifiable threat model so users know exactly what traffic can still escape.
- Impact: Pressure increases on Google, Apple, and others to document and minimize system-level VPN exemptions.
- Watch next: Independent VPN-leak test suites for mobile OSes, and whether Android’s upstream networking stack revisits the QUIC teardown design.
