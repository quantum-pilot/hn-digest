# Play Store blocks AuroraStore, hurting GrapheneOS users

- Score: 516 | [HN](https://news.ycombinator.com/item?id=49523754) | Link: https://gitlab.com/AuroraOSS/AuroraStore/-/work_items/1566

### TL;DR

An open Aurora Store issue documents intermittent “server busy” failures when installing or updating apps, initially through anonymous accounts and across CalyxOS, GrapheneOS, standard Android, and microG setups. Clearing data, changing VPN locations, refreshing accounts, or retrying sometimes yields one successful download, but reports conflict. Contributors suspect flagged shared accounts, rate limiting, authentication challenges, or an unparsed Google backend response; none is confirmed. The supplied evidence therefore establishes a disruptive outage, not that Google deliberately blocked Aurora or that GrapheneOS is uniquely affected.

### Comment pulse

- Some GrapheneOS users prefer anonymous Aurora access despite the project recommending sandboxed Play Store with a separate Google account.
- Others called the headline causal and platform-specific beyond the evidence; failures span operating systems and remain intermittent.
- Affected users reported stale apps, while suggested workarounds undermine avoiding Google accounts or work only briefly.

### LLM perspective

- View: Treat this as an unresolved compatibility or access incident until raw responses distinguish throttling from client parsing failure.
- Impact: Users avoiding Google accounts lose a convenient update path, regardless of whether the cause is intentional.
- Watch next: Capture protocol logs, test authenticated versus anonymous pools, improve error reporting, and verify a reproducible fix.
