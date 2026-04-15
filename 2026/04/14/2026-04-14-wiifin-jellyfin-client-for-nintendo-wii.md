# WiiFin – Jellyfin Client for Nintendo Wii

- Score: 239 | [HN](https://news.ycombinator.com/item?id=47759341) | Link: https://github.com/fabienmillet/WiiFin

## TL;DR

WiiFin is an experimental, GPLv3 homebrew Jellyfin client for the Nintendo Wii (and vWii). Written in C/C++ on top of GRRLIB and MPlayer CE, it offers a full 10-foot UI: account login, multiple profiles, library browsing (movies/TV/music), detail views, continue-watching/Next Up, and playback with an on-screen player overlay and Wiimote pointer. All video is server-transcoded (no direct play, stereo only, subtitles burned in). It runs on real hardware or Dolphin and builds with devkitPro.

## Comment pulse

- Jellyfin’s momentum vs Plex → TrueNAS stats and projects like this suggest a growing Jellyfin ecosystem, helped by Plex missteps on pricing and mandatory accounts.  
- Developer and UX reports → APIs are pleasant and hackable; end-user experience varies from “rock solid on TVs” to “buggy, single-instance, non-HA, logs scattered” — counterpoint: some users reverted to plain UPnP/DLNA.  
- Platform coverage jokes → Community notes a Wii client existing before solid PS5/tvOS options, though third-party tvOS apps like Streamyfin are catching up quickly.

## LLM perspective

- View: Retro-targeted clients show Jellyfin’s open API enabling niche but polished frontends beyond mainstream platforms.  
- Impact: Benefits media hoarders, homebrew communities, and users wanting ownership over media instead of SaaS lock-in.  
- Watch next: More first-class clients (consoles, tvOS), better HA and observability, and clearer security posture for self-hosters.
