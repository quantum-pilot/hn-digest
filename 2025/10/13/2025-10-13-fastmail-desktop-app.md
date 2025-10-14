# Fastmail desktop app

- Score: 141 | [HN](https://news.ycombinator.com/item?id=45564619) | Link: https://www.fastmail.com/blog/desktop-app/

TL;DR
Fastmail released a desktop app for macOS, Windows, and Linux: a standalone wrapper of its web client with offline access, native notifications, and default mailto handling. HN readers largely infer it’s Electron/WebView, debating “native” wording and reporting heavy memory use (~700MB). Supporters value convenience, offline mode, and integrated mail/contacts/calendar; skeptics prefer browser tabs or existing clients (e.g., Thunderbird) and question duplication. Others argue an official download reduces setup friction for non-technical users while keeping open-standards choices intact.

Comment pulse
- It’s an Electron wrapper, not “native” → higher RAM/CPU; web client remains primary; benefits mostly notifications and windowing.
- Official app reduces setup friction → non-technical users won’t configure Thunderbird; one download, login, mailto works — counterpoint: browser tab/PWA already covers most needs.
- Offline support is the differentiator → read/compose without connectivity; still, install size and Flatpak/Electron dependency put some off; Safari “Add to Dock” suffices for others.

LLM perspective
- View: A packaged web app prioritizes reach and speed over platform-native fidelity.
- Impact: Lowers churn for new users; adds offline and handler features without fragmenting codebases.
- Watch next: Clarify “native” messaging; measure memory/CPU vs browser and Thunderbird; consider PWA install, mailto registration, and resource budgets.
