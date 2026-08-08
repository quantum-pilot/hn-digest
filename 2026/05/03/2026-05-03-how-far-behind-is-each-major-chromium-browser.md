# How far behind is each major Chromium browser?

- Score: 156 | [HN](https://news.ycombinator.com/item?id=47999006) | Link: https://chromium-drift.pages.dev/

### TL;DR

Chromium Drift is a live dashboard intended to show how many Chromium releases major derivative browsers trail. Its security premise is that lag can leave users exposed after upstream fixes become public, though the supplied snapshot was still loading and contained no browser results. Commenters said major-version distance alone is inadequate: security patches also arrive in revisions and maintained branches, vendors may fast-track critical fixes, and a single snapshot cannot show typical delay. They requested historical per-release tracking, Electron applications, additional browsers, and clearer release-cadence context.

### Comment pulse

- Electron lag may be extensive — counterpoint: many desktop apps do not execute arbitrary remote code, reducing some browser-style exploit paths.
- Accessibility feedback flagged pale low-contrast and red/green status colors; the creator said the presentation was fixed.
- Requests for Supermium and maintained-branch awareness showed that “latest major” is not a universal security baseline.

### LLM perspective

- Score exposure by missing security commits and patch age, not merely major-version count.
- Separate normal channel policy from exceptional critical-patch response, then publish median and worst-case lag.
- Track browser and Electron histories continuously with reproducible version detection and accessible non-color status labels.
