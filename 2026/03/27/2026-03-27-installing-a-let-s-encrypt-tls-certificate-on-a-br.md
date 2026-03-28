# Installing a Let's Encrypt TLS certificate on a Brother printer with Certbot

- Score: 178 | [HN](https://news.ycombinator.com/item?id=47542644) | Link: https://owltec.ca/Other/Installing+a+Let%27s+Encrypt+TLS+certificate+on+a+Brother+printer+automatically+with+Certbot+(%26+Cloudflare)

- TL;DR  
  Author automates issuing and installing a real Let’s Encrypt certificate on a Brother printer using Certbot’s Cloudflare DNS-01 plugin plus the brother-cert tool, wrapped in a bash script and scheduled with Cronicle. The script ensures RSA-2048 keys, converts to the printer’s PKCS#12 format, uploads via the printer’s web UI, and reboots it, avoiding reverse proxies or local CAs. HN discusses brother-cert’s screenscraping approach, better ways to hook into Certbot, and security of DNS API tokens and Cloudflare-centric setups.

- Comment pulse  
  - brother-cert uploads via web UI screenscraping → tool logs into printer admin, grabs CSRF token, posts cert form; ugly but only reliable vendor-independent method.  
  - Use Certbot deploy hooks instead of external scheduler → run `certbot renew` with `--deploy-hook` to copy+reload certs; in containers, rely on crond + daily script.  
  - DNS-01 tokens feel dangerous → APIs can overgrant; mitigations: per-record policies, sub-zones, DNS-alias, delegated HTTP — counterpoint: scoped tokens now common.

- LLM perspective  
  - Automating certificates for embedded devices shows ACME tooling maturing beyond web servers into general-purpose machine identity management.  
  - Biggest benefit: homelab and small IT admins who distrust vendor clouds yet want modern TLS and automated rotation for devices.  
  - Watch for standardized printer/IoT certificate APIs, narrower DNS-01 authorization schemes, and more ACME clients supporting vendor-specific deployment hooks.
