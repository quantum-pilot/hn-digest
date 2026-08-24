# Molly: An Improved Signal App

- Score: 200 | [HN](https://news.ycombinator.com/item?id=46080916) | Link: https://molly.im/

### TL;DR

Molly is an independent Android fork of Signal offering encrypted local storage, multi-device pairing, Material You theming, automatic locking, RAM shredding, and Tor support. Its Molly-FOSS variant removes proprietary blobs and uses UnifiedPush, while a regular build retains Firebase for speed and reliability. Users praised F-Droid availability. The discussion also stressed that modified encrypted messengers enlarge the trust surface, while one longtime user reported losing registration and an unusable backup that forced a fresh Signal database.

### Comment pulse

- Privacy-conscious Android users value Molly-FOSS → UnifiedPush avoids leaking notification timing through Google infrastructure.
- Fork trust requires scrutiny → third-party changes can weaken end-to-end guarantees — counterpoint: GrapheneOS has publicly endorsed Molly.
- Reliability is not assured → a registration loss plus failed backup stranded one user for days.

### LLM perspective

- View: Platform independence is meaningful only when update discipline, protocol compatibility, and recovery paths remain dependable.
- Impact: De-Googled users gain features, but assume extra maintainer and migration risk around sensitive message history.
- Watch next: Re-registration failures, backup restores, upstream protocol changes, security reviews, and release cadence.
