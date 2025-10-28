# JetKVM – Control any computer remotely

- Score: 253 | [HN](https://news.ycombinator.com/item?id=45723159) | Link: https://jetkvm.com/

- TL;DR
  - JetKVM is a KVM‑over‑IP box promising 1080p60, 30–60 ms latency, and optional open‑source WebRTC cloud for NAT traversal. Built on Go/Linux with a React dashboard and extension ports for ATX/DC/serial, it targets hackability and low cost. HN welcomes the feature set and price versus PiKVM/TinyPilot, but questions corporate‑grade trust given sparse company provenance, notes mixed HDMI/stream reliability and H.264 quirks, and advises keeping any bare‑metal remote device off the public internet; tariffs and PoE also come up.

- Comment pulse
  - Trust requires transparency → company sites list no people or locale; YC/Estonia/Shenzhen links found elsewhere — counterpoint: likely targeting hobbyists, not audited enterprise use.
  - Reliability is mixed → HDMI incompatibilities and Loading video stream errors; some resolve by enabling H.264; one of three units failed for a buyer.
  - Alternatives trade-offs → PiKVM more open but costly; JetKVM far cheaper; other options: TinyPilot, GL.iNet Comet with Tailscale; keep KVMs off public internet.

- LLM perspective
  - View: Cheap, hackable KVM‑over‑IP is maturing, but security posture and vendor transparency lag enterprise expectations.
  - Impact: Homelabs gain BIOS‑level access affordably; enterprises stick to iDRAC/iLO until provenance, QA, and support commitments improve.
  - Watch next: Public hardware compatibility matrices, reproducible firmware builds, third‑party security audits, PoE variants, and measurable latency/quality benchmarks.
