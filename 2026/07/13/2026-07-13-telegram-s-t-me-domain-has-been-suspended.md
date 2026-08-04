# Telegram's t.me domain has been suspended

- Score: 225 | [HN](https://news.ycombinator.com/item?id=48897878) | Link: https://www.whois.com/whois/t.me

### TL;DR

A WHOIS snapshot for Telegram’s t.me short-link domain showed four client-prohibited statuses—delete, renew, transfer, and update—despite registration through May 2035 and Google-hosted nameservers. The supplied record does not itself prove suspension: commenters noted ICANN uses `serverHold` for that, while these locks may reflect registrar controls, a legal dispute, or simply the domain already sitting at the ten-year renewal ceiling. HN nevertheless treated the incident as a dependency warning, advocating first-party redirect links and alternate community platforms while speculating, without confirmation, about regulatory pressure and GoDaddy’s role.

### Comment pulse

- Status interpretation remained unsettled → `clientRenewProhibited` can accompany disputes, but a 2035 expiry and absent `serverHold` weaken the suspension claim.
- Link indirection paid off → one operator could replace Telegram URLs centrally rather than resend every emailed link.
- Centralized dependencies worried communities → an Indian functional-programming group had already begun moving from Telegram to Zulip.

### LLM perspective

- **View:** WHOIS locks, DNS resolution, HTTP reachability, and registry hold are separate signals; headlines should not collapse them.
- **Impact:** Broken short links can sever years of invitations, documentation, and discovery even when Telegram remains reachable.
- **Watch next:** Confirm RDAP state, DNS answers, registrar notice, registry action, restoration timeline, and whether telegram.me shares the dependency.
