# Crates.io phishing attempt

- Score: 147 | [HN](https://news.ycombinator.com/item?id=45222772) | Link: https://fasterthanli.me/articles/crates-io-phishing-attempt

- TL;DR
  - Attackers targeted Rust’s crates.io maintainers with a convincing breach-notification email pushing a “temporary SSO” login; the link led to a fake GitHub sign-in on a rustfoundation-themed domain. The crates.io team acknowledged a phishing campaign; as of Sep 12 UTC, no compromised packages are known. HN focuses on verification hygiene (never act from inbound messages), real-world examples of official-looking phish (e.g., PayPal embeds attacker text), and debate over how convincing this one was versus basic tells and password-manager safeguards.

- Comment pulse
  - Treat any inbound alert as untrusted; close it, visit the site/app yourself; don’t trust phone numbers from emails or Google snippets.
  - Attackers exploit PayPal business invitations: official paypal.com mail, DKIM-signed, with attacker-written “call us” text embedded—users phone a scammer despite legit-looking links.
  - Looks polished to some; others note tells: wrong org announcing, crates.io uses GitHub auth, a real breach would be bannered—counterpoint: fatigue makes anyone slip.

- LLM perspective
  - View: Credential-phishing of maintainers is the current easiest path to supply-chain compromise; branding and subdomains outpace human heuristics.
  - Impact: Ecosystem stewards, not just users, must harden comms: no action links, org-verified banners, DMARC enforcement, takedown playbooks, mandatory hardware keys.
  - Watch next: Signal progress via: GitHub passkey adoption rates, crates.io incident postmortem, domain-typoblocking in browsers, and faster abuse-response from registries and foundations.
