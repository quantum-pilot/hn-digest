# Indoor Wi-Fi Roaming with OpenWRT

- Score: 199 | [HN](https://news.ycombinator.com/item?id=48282180) | Link: https://taoofmac.com/space/blog/2026/05/26/1730

### TL;DR

On four wired OpenWrt access points, the author kept separate 2.4 GHz/WPA2 and 5 GHz/WPA3 SSIDs, then addressed sticky roaming by adding usteer and static, band-specific 802.11k neighbor reports that hostapd had failed to populate. One later sample showed no 2.4 GHz miracle but eliminated roughly −90 dBm associations and redistributed 5 GHz clients more plausibly; one Fast Transition error appeared. HN emphasized that roaming stays client-dependent, debating Apple thresholds, 802.11r compatibility, channel/power tuning, and whether split SSIDs simplify legacy support or create unnecessary complexity.

### Comment pulse

- Roaming is client-specific → Apple prioritizes stability with documented thresholds, while Android behavior varies by vendor and traffic type.
- Tuning remains contentious → reduced-power, same-channel deployments reportedly switch quickly — counterpoint: nearby co-channel APs can interfere, and disabling 802.11r helped some homes.
- SSID separation is a policy choice → legacy encryption, band preference, VLANs, and firewall rules may justify it, but extra networks increase complexity.

### LLM perspective

- **View:** Apparent improvement came from restoring missing topology information, not changing coverage; steering still depends on clients accepting hints.
- **Impact:** OpenWrt users gain inspectable, cloud-free roaming, but must own RF tuning, compatibility testing, and long-term telemetry.
- **Watch next:** Collect multi-week roam events, SNR distributions, handoff latency, disconnects, FT errors, and results by device, band, and firmware.
