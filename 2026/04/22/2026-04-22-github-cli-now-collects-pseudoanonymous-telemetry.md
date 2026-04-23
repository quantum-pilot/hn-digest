# GitHub CLI now collects pseudoanonymous telemetry

- Score: 396 | [HN](https://news.ycombinator.com/item?id=47862331) | Link: https://cli.github.com/telemetry

## TL;DR
GitHub’s gh CLI now sends pseudonymous telemetry about command usage (command, flags, OS, device ID, timestamps) to GitHub analytics by default. Users can preview payloads via a log mode and disable tracking with config or environment variables, including DO_NOT_TRACK. Hacker News debates whether telemetry is necessary insight or unnecessary spying, raises concerns about default-on behavior in CI and locked-down networks, and questions re-identification risks, prompting some developers to consider self-hosted Git hosting alternatives.

## Comment pulse
- Telemetry is framed as spying vs vital feedback: skeptics cite git’s success; supporters say git’s poor UX shows what happens without real-world usage data.  
- Default-on telemetry alarms CI users: extra outbound calls may break locked-down networks—counterpoint: others argue failed analytics uploads should be non-fatal no-ops.  
- Privacy-focused users note pseudonymous IDs plus timestamps can re-identify individuals, and either want opt-in verbose telemetry previews or migrate to self-hosted GitHub alternatives.  

## LLM perspective
- View: For a developer CLI, default-on analytics should be opt-in for new installs, opt-out for enterprises via central policy.  
- Impact: Teams must now bake GH_TELEMETRY or DO_NOT_TRACK into dotfiles, containers, and CI images to avoid surprise network traffic.  
- Watch next: Community may fork gh, add hardened privacy defaults, or pressure GitHub into prompts and clearer enterprise-wide disable switches.
