# Track which Electron apps slow down macOS 26 Tahoe

- Score: 144 | [HN](https://news.ycombinator.com/item?id=45469468) | Link: https://avarayr.github.io/shamelectron/

- TL;DR
    - A community tracker (“Shamelectron”) lists Electron apps that degrade GPU performance on macOS 26 Tahoe due to Electron using a private macOS API (for window corner masks). The issue is fixed upstream; apps must bump to Electron v38.2.0, v37.6.0, or v36.9.2. Tracker shows 33 apps: 6 fixed, 27 pending. HN debates blame: Electron’s private-API use vs Apple’s QA and ecosystem priorities. Users report broader Tahoe issues (Zoom glitches, menu bar rendering, higher memory), share a script to find impacted local apps, and note Tauri is unaffected.

- Comment pulse
    - Root cause: Electron used a private Apple API, breaking compositing → framework vendors should avoid private APIs — counterpoint: Apple’s own private-API use undermines this standard.
    - Tahoe feels unstable beyond Electron → Zoom/UI bugs, higher RAM usage on 8GB machines, QA/radar frustration; many plan to delay upgrading 2–3 months.
    - Fix exists; vendors must bump Electron → author of the fix is nudging apps; script helps find your installed offenders; Tauri apps report no issues.

- LLM perspective
    - View: Public trackers plus simple upgrade targets create effective pressure for timely framework bumps.
    - Impact: macOS 26 users, Electron app teams, IT support lines, and vendors with slow release cadences.
    - Watch next: Adoption of v38.2.0/v37.6.0/v36.9.2; Apple guidance on private APIs; Slack/Zoom/1Password release timelines.
