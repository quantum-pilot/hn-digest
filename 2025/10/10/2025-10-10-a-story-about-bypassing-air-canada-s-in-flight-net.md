# A story about bypassing air Canada's in-flight network restrictions

- Score: 170 | [HN](https://news.ycombinator.com/item?id=45536325) | Link: https://ramsayleung.github.io/en/post/2025/a_story_about_bypassing_air_canadas_in-flight_network_restrictions/

### TL;DR

On an Air Canada flight, the author found that the free messaging-only Wi-Fi blocked ordinary web traffic but allowed arbitrary TCP connections on port 53. A roommate configured an Xray VLESS/TLS proxy on that port, and a SOCKS client then reached GitHub, although bandwidth remained poor. The experiment indicates the gateway classified traffic mainly by port rather than inspecting whether it was DNS. The author did not attempt a speculative MAC-spoofing route, describing that as potentially criminal.

### Comment pulse

- Readers stressed that failed ping tests prove little unless the exact intended protocol is tested.
- Several suspected the free tier's bandwidth limit, rather than access control alone, explained the poor result.

### LLM perspective

- View: The interesting failure was simplistic port classification, not any compromise of aircraft systems.
- Impact: Messaging-tier segmentation can be porous while aggressive throttling still limits practical abuse.
- Watch next: Providers can close this gap by validating protocol behavior rather than trusting destination ports.
