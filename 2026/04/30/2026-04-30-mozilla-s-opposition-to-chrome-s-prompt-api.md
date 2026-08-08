# Mozilla's opposition to Chrome's Prompt API

- Score: 575 | [HN](https://news.ycombinator.com/item?id=47959463) | Link: https://github.com/mozilla/standards-positions/issues/1213#issuecomment-4347988313

### TL;DR

Mozilla opposes Chrome’s proposed Prompt API because websites inevitably tune prompts to a model’s quirks, risking Chrome/Gemini-only behavior and making competing or upgraded models break sites. It also objects that Chrome use requires acknowledging Google-specific prohibited-use terms and says evidence for developer support is thin. Mozilla favors extension-based experimentation with developer-selected models before standardizing. Hacker News split: supporters argue local inference improves privacy, cost, and web competitiveness, while critics add memory, CPU, fingerprinting, and browser-monopoly concerns. Chromium participants acknowledge calcification risk but prefer shipping, measuring compatibility failures, and correcting quirks.

### Comment pulse

- Supporters compare model variation with speech or geolocation APIs; opponents say nondeterministic prompt behavior is qualitatively harder to test.
- Model fingerprinting could create trusted-browser checks and second-class browsers — counterpoint: disabling the API may suffice if sites degrade gracefully.
- Local models avoid server cost and data transfer, but impose downloads, RAM, CPU, permissions, and platform-specific policy terms.

### LLM perspective

- **View:** Standardizing transport is easier than semantics; site behavior still depends on opaque, changing model output.
- **Impact:** An early dominant model could become the compatibility target regardless of specification neutrality.
- **Watch next:** Cross-model breakage, permissions, fingerprint resistance, update strategy, extension results, and multi-engine consensus.
