# Show HN: Bor – Open-source policy management for Linux desktops

- Score: 167 | [HN](https://news.ycombinator.com/item?id=49142569) | Link: https://getbor.dev/blog/2026-08-02-bor-v080-release/

### TL;DR

Bor 0.8.0 adds managed Thunderbird, Edge, and Firewalld policies, variable-aware Polkit rules, per-action RBAC, and a redesigned PatternFly interface with routing, scalable lists, safety guards, and WCAG 2.2 AA improvements. Agents receive policies over persistent mTLS gRPC streams, enforce native locks or root-owned files, detect root-level drift with inotify, and restore changes within milliseconds. Security work tightened certificate identity, MFA, secret encryption, repository redirects, CSV export, initial credentials, and dependencies. HN saw a promising Linux fleet-management niche but asked about SSO, Cinnamon, scripts, competitors, and mTLS.

### Comment pulse

- Bor deliberately avoids arbitrary root scripts, preserving a bounded policy model, clearer audits, and enterprise compliance rather than becoming remote execution.
- It complements AD, Samba, or FreeIPA instead of managing users; LDAP and Kerberos work now, while OAuth and SAML remain future work.
- Outbound persistent streams avoid SSH credentials and inbound ports, replay missed revisions, and push policy changes immediately through NAT and firewalls.

### LLM perspective

- View: Bor’s strongest differentiator is constrained, tamper-evident enforcement rather than the broad procedural flexibility of configuration-management tools.
- Impact: Schools, nonprofits, and enterprises gain centralized Linux desktop policy without requiring Windows management or searchable SSH access.
- Watch next: Test large-fleet recovery, mixed desktop environments, external identity integration, policy conflicts, offline durability, and independent security review.
