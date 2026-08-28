# Native ACME support comes to Nginx

- Score: 172 | [HN](https://news.ycombinator.com/item?id=45214023) | Link: https://letsencrypt.org/2025/09/11/native-acme-for-nginx

### TL;DR

NGINX introduced an official `ngx_http_acme` module, implemented in memory-safe Rust, that can obtain and renew certificates through ACME without a separately managed client. Let’s Encrypt presents this as another step toward automatic encryption, alongside native support in Caddy, Traefik, and Apache. Commenters welcomed easier secure defaults but disputed whether every service should embed certificate issuance. Advocates said the server already knows its domains and certificates; critics preferred a least-privileged standalone client, especially when certificates must cover or be distributed to several services.

### Comment pulse

- Operators contrasted seamless native renewal with the simpler auditing and troubleshooting of one centralized ACME client.
- Several commenters credited Caddy with pioneering hands-free certificate automation in a web server.

### LLM perspective

- View: Native ACME is compelling for single-server deployments, while heterogeneous systems still benefit from centralized issuance.
- Impact: Fewer manual renewal steps can improve baseline TLS reliability, provided operators understand ownership and reload behavior.
- Watch next: Module packaging, privilege boundaries, multi-service certificate workflows, renewal observability, and failure recovery.
