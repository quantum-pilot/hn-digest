# Installing a Let's Encrypt TLS certificate on a Brother printer with Certbot

- Score: 178 | [HN](https://news.ycombinator.com/item?id=47542644) | Link: https://owltec.ca/Other/Installing+a+Let%27s+Encrypt+TLS+certificate+on+a+Brother+printer+automatically+with+Certbot+(%26+Cloudflare)

### TL;DR

The guide automates a certificate for a LAN-only Brother DCP-L2550DW with a public domain resolved locally through NextDNS. A monthly job uses Certbot’s Cloudflare DNS-01 challenge with a scoped DNS-edit token, explicitly requests legacy-compatible RSA-2048, then `brother-cert` converts the PEM material to PKCS#12, logs into the printer’s web interface, uploads it, and reboots the device. HTTPS is attempted first, with HTTP fallback for expired certificates. HN suggested Certbot deploy hooks instead of a large wrapper and focused on protecting long-lived DNS credentials through record-level permissions, delegated challenge zones, or aliases.

### Comment pulse

- `brother-cert` exposes no device API; it scrapes a CSRF token and submits the administrator certificate-upload form.
- DNS automation need not grant whole-zone power: providers can support record-specific updates, subdomain delegation, or CNAME-based challenge aliases.
- Firmware and Wi-Fi setup remain painful on minimal printer controls; WPS can at least avoid typing long passwords.

### LLM perspective

- **View:** Issuance is straightforward; safely automating credentials and surviving vendor UI changes are the harder problems.
- **Impact:** End-to-end HTTPS protects web management and secure IPP without tying printer availability to a reverse proxy.
- **Watch next:** Tool compatibility, DNS-PERSIST-01 rollout, renewal alerts, least-privilege tokens, and post-reboot verification.
