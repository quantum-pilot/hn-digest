# iCloud+ Hide My Email addresses will remain on icloud.com

- Score: 591 | [HN](https://news.ycombinator.com/item?id=49426564) | Link: https://developer.apple.com/news/?id=1ptvdtcm

### TL;DR

Apple will move newly generated Sign in with Apple relay addresses from privaterelay.appleid.com to private.icloud.com later in 2026, while existing aliases continue forwarding without interruption. After community feedback, separate iCloud+ masking aliases will keep the main icloud.com domain. Developers must update validators, allowlists, and account systems for both Sign in with Apple domains. Commenters said mixing masked and ordinary addresses helps defeat relay blocklists and cross-site correlation, although it increases dependence on Apple and serves different goals than per-vendor aliases on personal domains.

### Comment pulse

- Shared provider domains preserve anonymity sets → sites cannot reject relay aliases without also excluding many ordinary customers.
- Personal-domain aliases expose ownership but identify leaks → users can trace spam to a vendor and retire only the compromised address.
- Apple lock-in remains real → forwarding can target another mailbox — counterpoint: losing the Apple account still disrupts every alias.

### LLM perspective

- View: Alias privacy depends as much on domain reputation as address randomness.
- Impact: Apple users gain harder-to-block aliases while accepting a larger account-recovery dependency.
- Watch next: Rollout date, rejection rates, migration failures, developer guidance, third-party relay compatibility.
