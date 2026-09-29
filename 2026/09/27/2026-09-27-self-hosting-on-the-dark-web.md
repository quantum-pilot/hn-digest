# Self-Hosting on the Dark Web

- Score: 350 | [HN](https://news.ycombinator.com/item?id=49870295) | Link: https://david.alvarezrosa.com/posts/self-hosting-on-the-dark-web/

### TL;DR

The author mirrors a static Hugo site as a Tor onion service by configuring Tor to forward its generated address to nginx on localhost, then building a second copy with the onion base URL so absolute links stay inside Tor. Tor stores service keys in its own protected directory and supplies end-to-end onion encryption, so the local nginx endpoint needs no TLS. Commenters added operational advice: advertise the mirror with `Onion-Location`, isolate bindings or sockets, minimize request chattiness, and plan for Tor-specific abuse.

### Comment pulse

- Onion hosting works behind NAT → the service initiates Tor connectivity while concealing the origin address from visitors.
- Performance rewards fewer requests → commenters recommended server rendering, compact assets, minimal JavaScript, and less connection chattiness.
- Isolation prevents accidental exposure or correlation → dedicated loopback addresses, ports, or Unix sockets reduce cross-service configuration mistakes.

### LLM perspective

- View: Publishing a static mirror is mechanically simple; operating a trustworthy, resilient onion service is the harder layer.
- Impact: Personal publishers can offer censorship-resistant access without exposing a public origin IP or managing onion TLS certificates.
- Watch next: Add address discovery, verify link isolation, monitor availability, and test behavior under Tor latency and abuse.
