# Imgur Geo-Blocked the UK, So I Geo-Unblocked My Network

- Score: 238 | [HN](https://news.ycombinator.com/item?id=46081188) | Link: https://blog.tymscar.com/posts/imgurukproxy/

### TL;DR

After Imgur blocked UK access, the author restored old embedded images across every home device without tunneling unrelated traffic. Pi-hole resolves `i.imgur.com` to Traefik, which uses TLS passthrough to an Nginx proxy sharing Gluetun's VPN network; credentials remain encrypted in a declarative NixOS setup. The result adds little image-loading latency and requires no client configuration. Commenters suggested simpler router-level policy routing, while noting that domain routing and IPv6 bypass can complicate otherwise straightforward WireGuard rules.

### Comment pulse

- Router policy routing may replace several containers → OpenWrt and UniFi can send selected domains through WireGuard.
- DNS-based proxying suits hostname selection → ordinary IP routes struggle when shared or changing addresses underlie a domain.
- IPv6 needs separate attention → unsupported VPN routing can let traffic bypass the intended tunnel.

### LLM perspective

- View: The design trades infrastructure complexity for transparent, domain-specific behavior across unmanaged devices.
- Impact: Households can preserve access to legacy embeds without sacrificing bandwidth or configuring every client.
- Watch next: Test IPv6, DNS changes, certificate behavior, VPN failure modes, and additional blocked hostnames.
