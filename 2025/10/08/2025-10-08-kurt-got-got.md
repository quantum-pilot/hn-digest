# Kurt Got Got

- Score: 238 | [HN](https://news.ycombinator.com/item?id=45520615) | Link: https://fly.io/blog/kurt-got-got/

- TL;DR
  - Fly.io’s CEO fell for a plausible “X content violation” phish, entering shared Twitter creds on members-x.com. Attackers changed email/2FA, posted a crypto airdrop scam, and locked the team out for ~15 hours; no infrastructure or customer data were touched. The post argues training can’t stop clicks; use phishing‑resistant auth (U2F/FIDO2/Passkeys) and put everything behind an IdP/SSO. Twitter was a legacy shared password; now it’s passkeys. Lesson: any account outside phishing‑resistant MFA will eventually get phished.

- Comment pulse
  - Phishing succeeds despite training → pentest stories: USB bait still gets executed; internal tests show ~10% click rate, which is catastrophic at large scale.
  - Use phishing‑resistant MFA like Passkeys/U2F → blocks credential proxying; wallets/passkeys prevented scams — counterpoint: some say passkeys are confusing, little gain over strong password managers.
  - Email filtering is failing on “X content violation” lures → wording constantly changes; some teams replaced providers after misses; one cited Check Point catching all.

- LLM perspective
  - View: Treat social accounts as first-class assets: enforce IdP SSO with phishing-resistant MFA; eliminate shared vault passwords and browser-only logins.
  - Impact: Marketing, comms, contractors need managed access; adopt delegated access tools, rotate tokens; fewer emergency recoveries after 2FA takeovers.
  - Watch next: Platforms enabling enterprise SSO/passkeys for brand accounts; better audit logs for social tooling; phishing-resistance benchmarks across email security vendors.
