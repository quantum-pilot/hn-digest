# An iroh powered smart fan

- Score: 161 | [HN](https://news.ycombinator.com/item?id=48817539) | Link: https://www.iroh.computer/blog/an-iroh-powered-smart-fan

### TL;DR

The project turns an ESP32, DHT22, and 5V fan into a Rust controller reachable without an app-specific cloud. Iroh supplies encrypted device-to-device networking over local connections or optional relays; irpc exposes temperature, humidity, status, and threshold methods; a WebAssembly page connects by endpoint ticket; and hysteresis prevents rapid fan toggling. The finished build adds a printed enclosure and separate QR codes for read-only and authenticated control. HN liked endpoint encryption but questioned 4 MiB PSRAM, the simple secret, and DIY complexity versus cheap hubs, while asking about Matter interoperability.

### Comment pulse

- Endpoint encryption improves IoT’s baseline → direct identities reduce bespoke cloud trust — counterpoint: full relay support consuming 4 MiB PSRAM limits embedded practicality.
- Smart control is not smarter mechanics → automatic thresholds add behavior, while commenters argued airflow, acoustics, and blade design determine fan quality.
- DIY autonomy competes with convenience → inexpensive infrared hubs already integrate with voice ecosystems, motivating requests for Matter and Home Assistant compatibility.

### LLM perspective

- **View:** The compelling architecture separates device identity from application infrastructure: browsers dial hardware directly, while optional generic relays solve reachability.
- **Impact:** Open peer-to-peer networking can reduce vendor lock-in, but memory footprint, provisioning, recovery, and authorization remain product-level engineering work.
- **Watch next:** Smaller QUIC stacks, key rotation, Wi-Fi recovery, schema evolution, self-hosted relays, and Matter or Home Assistant bridges.
