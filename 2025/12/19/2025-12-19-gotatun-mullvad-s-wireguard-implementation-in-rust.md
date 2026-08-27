# GotaTun – Mullvad's WireGuard Implementation in Rust

- Score: 523 | [HN](https://news.ycombinator.com/item?id=46324543) | Link: https://mullvad.net/en/blog/announcing-gotatun-the-future-of-wireguard-at-mullvad-vpn

### TL;DR

Mullvad's GotaTun is a Rust fork of Cloudflare's BoringTun, not a new VPN protocol. It adds Mullvad's DAITA and Multihop features, Android support, safe multithreading, and zero-copy techniques while removing a difficult Rust-Go FFI boundary around wireguard-go. Mullvad says wireguard-go caused over 85% of reported Android crashes; after GotaTun shipped in version 2025.10, user-perceived crash rate fell from 0.40% to 0.01%, with no crashes attributed to GotaTun. Other platforms and an external audit are planned for 2026.

### Comment pulse

- Users reported faster connections and throughput, but one Pixel owner also observed severe intermittent deep-sleep battery drain.
- Rust may improve optimization and FFI integration; commenters still considered Go adequate for most non-firmware networking.
- WireGuard intentionally leaves traffic obfuscation to an outer layer rather than hiding its protocol signature.

### LLM perspective

- View: Replacing the runtime boundary may be as important as Rust's raw performance.
- Impact: Mullvad gains clearer crash diagnostics and one implementation for Rust-heavy clients across platforms.
- Watch next: Await the audit and measure battery, throughput, latency, memory, crash attribution, and non-Android parity.
