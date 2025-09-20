# As Android developer verification gets ready to go, a new reason to be worried

- Score: 163 | [HN](https://news.ycombinator.com/item?id=45301845) | Link: https://www.androidauthority.com/android-sideload-offline-3598988/

- TL;DR
  - Google’s upcoming Android developer verification links real identities to all apps, including sideloaded APKs. New SDK flags (e.g., DEVELOPER_VERIFICATION_FAILED_REASON_NETWORK_UNAVAILABLE, ..._DEVELOPER_BLOCKED) suggest installs may require online checks against blocklists, potentially breaking offline sideloading; ADB-based installs remain a workaround. Rollout is about a year away. HN reaction: strong concern over Google gatekeeping and loss of Android’s openness; proposals range from GrapheneOS/Lineage or Ubuntu Touch to switching to iPhone; debate spans antitrust framing and whether corporate OS users ever had real control.

- Comment pulse
  - Google as gatekeeper threatens openness → Network-required verification could block offline sideloads; control shifts to Google blocklists — counterpoint: Users never truly controlled corporate OSes.
  - Vote with devices → Flash GrapheneOS/Lineage or try Ubuntu Touch; others prefer iPhone’s polished walled garden over Google’s tightening one.
  - Antitrust lens → Android’s ‘open’ promise invites regulatory limits; Apple’s closed model evades some monopoly findings; verification likely meets economic, not user-freedom, tests.

- LLM perspective
  - View: Identity-binding plus blacklist checks; risk is network-dependent installs and centralized revocation.
  - Impact: Offline-first users, FOSS app distributors, and air‑gapped or restricted networks; ADB workflows become critical safety valves.
  - Watch next: SDK defaults, caching/expiry rules, enterprise toggles, EU DMA scrutiny, OEM deviations, and timelines for enforcement.
