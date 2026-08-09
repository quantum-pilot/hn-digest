# My Google Workspace account suspension

- Score: 329 | [HN](https://news.ycombinator.com/item?id=47648404) | Link: https://zencapital.substack.com/p/sad-story-of-my-google-workspace

### TL;DR

While traveling from Australia to Britain, a Google Workspace administrator removed his recovery phone because Gmail kept demanding SMS despite an authenticator, passkey, backup codes, and logged-in devices. Google interpreted the change as hijacking, suspended the sole super-admin account, stopped inbound mail and forwarding, and broke Calendar, payroll, CRM, task management, and Google-based logins. DNS ownership verification and four support cases produced contradictory loops and a proposed 30-day wait; after more than 40 hours, Google employees restored access. HN blamed both brittle recovery and an unplanned dependency stack.

### Comment pulse

- Critics urged disaster planning and external backups — counterpoint: consumers also need enforceable recourse when paid providers lock them out without functional support.
- Avoiding “Login with Google” reduces correlated failure; independent credentials keep one suspended identity provider from disabling unrelated services.
- Stories about unresolved Pixel benefits, payments, search delisting, and account bans reinforced reluctance to buy Google services without internal escalation access.

### LLM perspective

- **View:** Authentication resilience needs independent recovery paths, not multiple factors terminating inside one provider’s risk engine.
- **Impact:** Single-admin Workspace tenants can lose communications and federated applications simultaneously, turning fraud protection into an operational outage.
- **Watch next:** Add secondary super-admins, offline credentials, alternate mail routing, exportable backups, tested break-glass access, and non-Google payroll authentication.
