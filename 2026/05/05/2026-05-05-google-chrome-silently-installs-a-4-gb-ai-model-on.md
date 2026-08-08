# Google Chrome silently installs a 4 GB AI model on your device without consent

- Score: 1205 | [HN](https://news.ycombinator.com/item?id=48019219) | Link: https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/

### TL;DR

Alexander Hanff reports that an untouched Chrome profile downloaded Gemini Nano weights into `OptGuideOnDeviceModel`: roughly 4 GB, installed in the background, with deletion followed by re-download unless AI flags or policy disable it. Filesystem events, Chrome state, feature flags, and updater logs form his evidence chain. He argues the default violates European consent and transparency rules and estimates one global rollout could emit 6,000–60,000 tonnes CO2e, depending on eligible devices. His remedy is explicit opt-in, download-on-first-use, visible model management, persistent removal, and published deployment impact.

### Comment pulse

- Critics saw unrequested 4 GB as materially different from routine browser updates — counterpoint: installing Chrome and accepting updates may cover bundled features.
- Sysadmins highlighted per-user storage amplification: thousands of profiles can turn one model into terabytes and repeated lab downloads.
- Others noted metered connections, while some users could not find the file, suggesting rollout or eligibility differences.

### LLM perspective

- Verify actual deployment counts and transfer energy before treating the emissions bands as measured impact.
- A system-wide cache could reduce institutional duplication, but explicit controls should govern download, removal, and webpage access.
- Separate local-model settings from cloud AI surfaces; shared branding can obscure where prompts are processed.
