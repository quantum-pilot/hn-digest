# Fallout from the AWS outage: Smart mattresses go rogue

- Score: 205 | [HN](https://news.ycombinator.com/item?id=45658056) | Link: https://quasa.io/media/the-strangest-fallout-from-the-aws-outage-smart-mattresses-go-rogue-and-ruin-sleep-worldwide

TL;DR
- An AWS outage disabled Eight Sleep’s cloud-dependent Pod mattresses: temperature control and sleep tracking failed, hub/app controls stalled, and some beds stuck at last settings. The incident highlights brittle IoT designs and prior Eight Sleep security concerns, spurring calls for offline-first features, local control standards, and fail-safe defaults. HN favors Home Assistant/Zigbee/Matter, mocks $4k-plus subscriptions, and notes the meta-irony of outage-blocked articles. Eight Sleep says offline mode is coming; many want it required.

Comment pulse
- Local-first setups (Home Assistant, Zigbee, Matter) → maintain control without internet, isolate devices on LAN; avoid accounts and cloud lock-in.
- Offline-compatible certification and safe defaults → mandate usable fallback; e.g., thermostats prevent freezing; consider legal bans or local, containerized backends.
- Just unplug or cool manually → problem overstated. — counterpoint: some beds locked to last setting; app/hub failed, no override.

LLM perspective
- View: Cloud-tethered appliances need local control planes; vendor lock-in turns outages into safety and usability failures.
- Impact: Manufacturers will be pressured to add offline modes; standards bodies and retailers can enforce badges for safe, local operation.
- Watch next: Eight Sleep’s offline-mode timeline, AWS postmortems, Matter’s certification scope, and independent tests validating fail-safe behavior under network faults.
