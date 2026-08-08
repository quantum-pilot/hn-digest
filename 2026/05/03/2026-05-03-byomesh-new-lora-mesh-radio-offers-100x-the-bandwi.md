# BYOMesh – New LoRa mesh radio offers 100x the bandwidth

- Score: 222 | [HN](https://news.ycombinator.com/item?id=47999636) | Link: https://partyon.xyz/@nullagent/116499715071759135

### TL;DR

BYOMesh combines an SX1276 for familiar sub-1 GHz LoRa bands with an SX1281 for faster 2.4 GHz LoRa on one compact companion board. Its creator targets MeshCore, Meshtastic, MeshTNC, BLE capture, and especially line-of-sight backhaul between elevated nodes, claiming up to 100× more aggregate bandwidth without Wi-Fi HaLow’s power, complexity, or licensing jump. Commenters liked the dual-band flexibility but demanded legal, reproducible throughput and range tests: 2.4 GHz sacrifices propagation, LoRa remains far slower than HaLow, and airtime congestion constrains larger meshes.

### Comment pulse

- Range depends on modulation, link budget, antenna height, and obstruction — counterpoint: higher frequency still incurs materially greater free-space loss.
- Proposed uses included hilltop backhaul, campus sensors, packet-radio bridges, and mobile nodes; commenters doubted reliable military-scale drone meshes.
- Regulatory concerns centered on whether claimed bandwidth fits FCC limits, with disagreement about which MeshCore violations actually apply.

### LLM perspective

- Publish packet size, spreading factor, coding rate, power, duty cycle, antennas, distance, and loss for every benchmark.
- Dual radios could reserve sub-GHz for resilient reach and 2.4 GHz for opportunistic high-rate hops.
- Watch firmware support, antenna configuration, payload aggregation, collision behavior, and region-specific compliance.
