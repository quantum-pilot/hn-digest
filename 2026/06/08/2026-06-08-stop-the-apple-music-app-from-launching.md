# Stop the Apple Music app from launching

- Score: 559 | [HN](https://news.ycombinator.com/item?id=48447935) | Link: https://lowtechguys.com/musicdecoy/

### TL;DR

Music Decoy prevents macOS from opening Music when an idle Play command arrives. It simply stays running under Music’s bundle identifier, causing the Remote Control Daemon to believe the system app is already open; version 1.1 can instead launch a configured player such as Spotify. The workaround preserves media-key controls, unlike disabling the daemon, and avoids continuously killing Music. HN admired the zero-work bundle-ID collision, shared remapping alternatives and a live-performance failure case, but split over whether Apple’s default is hostile promotion or reasonable Play-button behavior.

### Comment pulse

- Elegant mechanism → Matching com.apple.Music exploits rcd’s process check without polling, illustrating how deep system knowledge can remove code rather than add it.
- Operational risk → Unconfigurable Bluetooth Play events can route unexpected music through live-performance audio systems, making this more than a minor annoyance.
- Intent debate → Critics see forced Music launches as anticompetitive — counterpoint: others expect an idle Play key to open the bundled player.

### LLM perspective

- **View:** The best workaround intercepts the narrow dispatch assumption while preserving unrelated media controls.
- **Impact:** Users gain control without daemon changes; the duplicate identifier may still depend on undocumented behavior.
- **Watch next:** Test macOS updates, code-signing conflicts, Bluetooth call transitions, alternate-player launching, quit discoverability, and resource use.
