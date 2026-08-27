# Google blocks Android hack that let Pixel users enable VoLTE anywhere

- Score: 126 | [HN](https://news.ycombinator.com/item?id=45553764) | Link: https://www.androidauthority.com/pixel-ims-broken-october-update-3606444/

### TL;DR

Google's October Pixel update closed the shell-user carrier-configuration override used by Pixel IMS and Shizuku to enable VoLTE and VoWiFi on imported phones and unsupported networks. Google reportedly classified the loophole as high-severity privilege escalation CVE-2025-48617. A less accessible workaround restores VoLTE but not Wi-Fi calling without root, which can disrupt Wallet and some Gemini features. HN commenters challenged the security framing and blamed fragmented carrier certification, per-device configuration tables, regional sales limits, and inconsistent Android telephony behavior.

### Comment pulse

- The override exceeded VoLTE → users also toggled VoNR and backup calling through a second SIM's data connection.
- Vulnerability severity was disputed → commenters argued ADB access implies consent, while wireless debugging can expose shell privileges to applications.
- Carrier provisioning is structurally brittle → hardware capability does not guarantee service when whitelists and outdated configurations intervene.

### LLM perspective

- View: Patching a privilege boundary is defensible, but removing essential calling without a supported path transfers risk to users.
- Impact: Importers may lose voice features, choose root-related tradeoffs, or abandon otherwise compatible Pixel hardware.
- Watch next: Follow official regional enablement, December's bulletin, replacement-workaround safety, and standardized carrier configuration mechanisms.
