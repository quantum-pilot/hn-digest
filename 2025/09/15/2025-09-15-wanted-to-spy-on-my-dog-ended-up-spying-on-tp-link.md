# Wanted to spy on my dog, ended up spying on TP-Link

- Score: 418 | [HN](https://news.ycombinator.com/item?id=45251690) | Link: https://kennedn.com/blog/posts/tapo/

### TL;DR

Trying to configure a Tapo camera without its cloud-dependent app, Joshua Kennedy intercepted onboarding traffic with Frida and mitmproxy, decompiled the APK, found a hard-coded default password, derived session keys, and decrypted the device’s “securePassthrough” calls. The analysis reduced onboarding to Wi-Fi scanning, account enablement, password replacement, and network joining, which Kennedy reproduced in a Bash script that also enables RTSP/ONVIF. The write-up criticizes inconsistent cryptography and password handling, while commenters broadened the concern to unaudited consumer IoT firmware.

### Comment pulse

- The author of the Frida interception scripts praised the project as a practical use of the tooling.
- Commenters discussed tradeoffs among cloud convenience, local control, proprietary audio, ONVIF, and neglected router security.

### LLM perspective

- View: The project shows how cloud onboarding can conceal a small local protocol behind brittle security machinery.
- Impact: Reproducible local provisioning restores ownership but exposes embedded credentials and inconsistent cryptographic design.
- Watch next: Track firmware changes, credential reuse across models, vendor remediation, and whether local onboarding remains possible.
