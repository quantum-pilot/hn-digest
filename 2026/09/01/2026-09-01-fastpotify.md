# Fastpotify

- Score: 822 | [HN](https://news.ycombinator.com/item?id=49517448) | Link: https://fastpotify.rocks/

### TL;DR

Fastpotify is an independent, MIT-licensed Spotify client built in Rust with egui and librespot for Linux, macOS, and Windows. It promises sub-second startup, roughly 100–250 MB memory use, local gapless playback up to 320 kbps, Spotify Connect control, library search and playlist editing. Extras include themes, desktop media controls, MilkDrop visualization, and a Winamp-skinned mini-player. Discussion contrasted this focused native approach with the official client’s performance and usability problems, while raising maintainability, generated-code disclosure, and dependence on Spotify’s evolving interfaces.

### Comment pulse

- Users welcomed a lighter player after reporting high memory use, offline failures, inconsistent controls, and unwanted content in official clients.
- The author disclosed human-directed, LLM-generated code and documentation after criticism of awkward copy, emphasizing daily use and active bug fixing.
- Some feared Spotify could disrupt librespot—counterpoint: commenters pointed to an official alternative but disputed whether active blocking is underway.

### LLM perspective

- View: Fastpotify’s value is disciplined scope, but its durability depends on an external service it does not control.
- Impact: Desktop listeners gain a native alternative; maintainers inherit compatibility, credential, and trust obligations across three platforms.
- Watch next: Audit safety, measure resource claims, and track Spotify API or authentication changes affecting librespot.
