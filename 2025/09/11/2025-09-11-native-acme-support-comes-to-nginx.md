# Native ACME support comes to Nginx

- Score: 172 | [HN](https://news.ycombinator.com/item?id=45214023) | Link: https://letsencrypt.org/2025/09/11/native-acme-for-nginx

- TL;DR
    - Nginx now includes an official, Rust-implemented ACME module for automatic TLS certificate issuance/renewal, bringing hands-free Let’s Encrypt to one of the web’s most-used servers and proxies. It joins Caddy, Traefik, and Apache in native ACME support, pushing most sites toward seamless encryption with less operator toil. HN welcomes the move but debates architecture: embed ACME in each service vs. use a single client for all certs. Caddy’s pioneering role is noted, alongside practical setup stories and operational tradeoffs.

- Comment pulse
    - Endpoint-integrated ACME → no extra client; certs match server config; trivial for single-host setups — counterpoint: messy when multiple services share or distribute certs.
    - Central ACME client preferred → one tool, least privilege, unified logs, easier distribution and restarts across Postfix/Dovecot/RabbitMQ/Nginx.
    - Caddy pioneered hands-free certs → deserves credit; still, Nginx’s Rust ACME narrows gaps and boosts default security for a huge install base.

- LLM perspective
    - View: Native ACME in Nginx reduces toil; pick per-service vs orchestrator based on whether certificates are shared across services or hosts.
    - Impact: Ops teams, Kubernetes ingress, and homelabs simplify renewals; fewer cronjobs and glue scripts; Rust reduces attack surface for ACME handling.
    - Watch next: DNS-01 and wildcard support parity, multi-service reload hooks, security hardening, and clear guidance on when to prefer external clients.
