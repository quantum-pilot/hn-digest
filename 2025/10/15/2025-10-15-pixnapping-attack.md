# Pixnapping Attack

- Score: 289 | [HN](https://news.ycombinator.com/item?id=45588594) | Link: https://www.pixnapping.com/

- TL;DR
  - Researchers unveil Pixnapping, an Android attack chaining intents, window blur, VSync timing, and the GPU.zip side channel to leak on-screen pixels from other apps/websites. Demonstrated on Pixel 6–9 and Galaxy S25, it can recover Gmail content and steal Google Authenticator TOTP codes in <30s if font/layout are known. Google’s September patch limiting blur calls was bypassed; another fix is slated for December. CVE-2025-48561 assigned; GPU vendors haven’t patched GPU.zip. Users should apply updates; app-level mitigations remain unclear.

- Comment pulse
  - Require explicit Internet/background permissions → reduces stealth exfiltration — counterpoint: intents wake apps; Internet prompts harm UX per Android team.
  - App-level hardening: move/animate digits, hide when backgrounded, add noise → raises attack cost — counterpoint: degrades UX and may be bypassed; patch/workaround exist.
  - Disclosure debate: accused of rushing and equivalent to screenshot prompts → rebuttal: Feb 2025 disclosure, Sept patch bypassed; protected views need exploits, not user-approved screenshots.

- LLM perspective
  - View: Cross-app rendering effects plus timing side channels enable per-pixel exfiltration without permissions by abusing blur overlays and GPU compression.
  - Impact: Android must restrict cross-window effects and timers; GPU vendors consider compression mitigations; apps adopt dynamic, reveal-on-demand UIs for secrets.
  - Watch next: December Android patch efficacy, driver-level GPU.zip mitigations, Play Protect heuristics for blur/VSync abuse, and authenticator UX changes.
