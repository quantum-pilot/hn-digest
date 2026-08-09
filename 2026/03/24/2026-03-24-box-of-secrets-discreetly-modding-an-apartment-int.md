# Box of Secrets: Discreetly modding an apartment intercom to work with Apple Home

- Score: 254 | [HN](https://news.ycombinator.com/item?id=47488686) | Link: https://www.jackhogan.me/blog/box-of-secrets/

### TL;DR

After an apartment complex let its intercom’s cellular service lapse, two visitors bypassed the dead calling path and intercepted the gate solenoid wire instead. They installed a fail-through ESP32 relay in a shared junction box, wrote Rust firmware using Matter, and exposed a timed unlock in Apple Home, defaulting to ten seconds. Bluetooth runs only during provisioning to avoid memory crashes; an AC-to-DC regulator solved a mistaken power assumption. The hack restored remote guest access, but HN’s dominant concern is unauthorized modification of shared security infrastructure and unlogged access.

### Comment pulse

- Direct solenoid access made protocols irrelevant → the relay preserves normal operation when unpowered and limits each unlock to ten seconds.
- Modding shared access control is ethically and legally risky — counterpoint: physical tailgating and exposed wiring already make the gate weak.
- Owners can pursue safer equivalents → commenters describe indoor intercom boards, VoIP passcodes, commercial openers, and consent-based installations.

### LLM perspective

- **View:** The engineering is clever; permission and accountability are the project’s unresolved failures.
- **Impact:** One resident gained convenience while neighbors and management inherited new access, reliability, and liability risks.
- **Watch next:** Landlord approval, per-user authorization, event logging, fail-state testing, credential revocation, and secure enclosure.
