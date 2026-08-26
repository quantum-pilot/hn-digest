# Just the Browser

- Score: 464 | [HN](https://news.ycombinator.com/item?id=46645615) | Link: https://justthebrowser.com/

### TL;DR

Just the Browser supplies open-source group-policy configurations for Chrome, Edge, and Firefox that disable most generative-AI features, telemetry, sponsored content, shopping tools, prompts, and startup boost without modifying browser binaries. Users can apply the policies through automated Windows, macOS, and Linux scripts where supported or follow manual guides, then inspect active settings in each browser. HN discussion strongly questioned piping remote scripts into privileged shells for small configuration files. Defenders noted the documented manual route, while others argued useful local features such as Firefox translation should remain enabled.

### Comment pulse

- The dominant concern was supply-chain risk from executing fetched scripts with administrator privileges to install small, auditable policy files.
- Supporters emphasized that manual instructions accompany automation → counterpoint: critics still preferred screenshots and explicit, user-controlled changes.
- Readers distinguished unwanted generative features from useful local models, especially Firefox translation, which the project deliberately preserves.

### LLM perspective

- View: The policy bundle is useful, but its safest interface is transparent documentation.
- Impact: Mainstream browsers become quieter without sacrificing update cadence or switching ecosystems.
- Watch next: Signed installers, configuration completeness, policy drift, and support for Linux Chromium browsers and mobile devices.
