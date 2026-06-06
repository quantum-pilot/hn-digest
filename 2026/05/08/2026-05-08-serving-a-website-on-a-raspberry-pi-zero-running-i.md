# Serving a website on a Raspberry Pi Zero running in RAM

- Score: 183 | [HN](https://news.ycombinator.com/item?id=48064312) | Link: https://btxx.org/posts/memory/

## TL;DR
A personal site is hosted on a Raspberry Pi Zero v1.3 running Alpine Linux entirely from RAM: the SD card is only for boot and storing config via Alpine’s `lbu`. The Pi runs a tiny HTTP server (`darkhttpd` or `nginx`) serving static files, while a $4/year Alpine VPS handles TLS termination and forwards plain HTTP back home using `socat`, fronted by TierHive’s HAProxy. The post details setup, port-forwarding, dynamic DNS, and dead-simple full-card backups with `dd`.

---

## Comment pulse
- Offloading TLS to a VPS diminishes the claim that the Pi “serves the site” → TLS, routing, and possibly caching happen in the cloud — counterpoint: this mirrors common 2026 reverse-proxy practice and keeps the Pi minimal.  
- Pi Zero is easily capable of more than a static site → people run email, Pi-hole, CI, SDR, and long-lived homelabs; performance rivals old enterprise servers.  
- Diskless Alpine-in-RAM is genuinely useful → survives power cuts, allows hot-removal of SD, simplifies full-image backups, and can reduce SD wear.

---

## LLM perspective
- View: This is a neat, reproducible recipe for an ultra-minimal, RAM-only edge node fronted by a tiny TLS proxy.  
- Impact: Appeals to hobbyists wanting hands-on self-hosting, backup discipline, and understanding of proxies/NAT/VPS on real hardware.  
- Watch next: Benchmark Pi-handled TLS vs VPS-offloaded TLS; quantify RAM/CPU tradeoffs; document failure modes and recovery playbooks for home-hosted setups.
