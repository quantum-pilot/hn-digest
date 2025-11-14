# Launch HN: Tweeks (YC W25) – Browser extension to deshittify the web

- Score: 152 | [HN](https://news.ycombinator.com/item?id=45916525) | Link: https://www.tweeks.io/onboarding

- TL;DR
    - Tweeks is a Chrome extension that uses an LLM to generate Greasemonkey-like “tweeks” from natural-language prompts, letting users hide clutter, reshape feeds, or restyle sites. Scripts persist via domain patterns and run locally; an LLM is called only when generating or updating, based on a captured page. HN asked about privacy, brittleness, cost, and business model. The founder says eval is manual, updates are planned, local models aren’t ready, Firefox is on the roadmap, and monetization/open source remain TBD.

- Comment pulse
    - Userscript-style scope and persistence → scripts use domain patterns; LLM only for generation; maintenance done manually now, with planned update propagation and eventual self-healing.
    - Privacy risk during generation → page snapshot sent to LLM; scripts run locally; costs scale with page complexity, not per visit — counterpoint: signup timing felt dark-patterny.
    - Monetization and openness unclear → founder weighs trust and SOC2 vs open-sourcing risk; local models not ready; Firefox support requested and prioritized.

- LLM perspective
    - View: AI-assisted userscripts pragmatically empower user-side UI changes without full agent browsing; Greasemonkey UX with natural-language authoring.
    - Impact: Likely adoption by power users, accessibility tweakers, and teams fixing internal tools; potential friction with ad-driven sites remains.
    - Watch next: Firefox port, script update/marketplace mechanics, selector-robustness benchmarks, and on-device LLMs enabling dynamic per-load filtering without server calls.
