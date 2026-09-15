# Microsoft patches Windows and Excel – breaks audio, remote access, and paste

- Score: 240 | [HN](https://news.ycombinator.com/item?id=49699297) | Link: https://www.theregister.com/os-platforms/2026/09/14/microsoft-patches-windows-and-excel-breaks-audio-remote-access-and-paste/5296085

### TL;DR

Microsoft acknowledged that September security updates disrupted Remote Desktop Services across several Windows versions, broke some USB Audio Class 1.0 devices, and caused silent paste failures in Excel 2016 through 2024. RDS failures could hang servers and related tools; restarting virtual machines offered only temporary relief. Switching audio to two-channel mode helped some users. Removing the Office update may restore paste but also removes security fixes. Microsoft was developing fixes, with no universal safe workaround reported in the article.

### Comment pulse

- QA should catch basic regressions → Remote access, paste, audio, and management-tool failures affect routine workflows immediately.
- Silent failure is especially harmful → Excel leaves source selected and destination unchanged without warning users.
- Alternatives have tradeoffs → Frustrated users considered Linux while others described its own hardware and desktop reliability problems.

### LLM perspective

- View: Security patches create an operational trap when regressions compete directly with vulnerabilities they remediate.
- Impact: Administrators must test wider application behavior and preserve rollback paths before deploying urgent updates.
- Watch next: Out-of-band fixes, root-cause reports, regression-test expansion, affected-device lists, and enterprise deployment guidance.
