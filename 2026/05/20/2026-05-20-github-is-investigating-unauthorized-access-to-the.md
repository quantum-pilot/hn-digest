# GitHub is investigating unauthorized access to their internal repositories

- Score: 605 | [HN](https://news.ycombinator.com/item?id=48201316) | Link: https://twitter.com/github/status/2056884788179726685

### TL;DR

GitHub disclosed unauthorized access to its internal repositories, saying it had no evidence that customer enterprises, organizations, or repositories were affected and was monitoring for follow-on activity. Commenters cited a later GitHub assessment that exfiltration was limited to internal repositories and that an attacker’s claim of roughly 3,800 repositories was directionally consistent; another linked report attributed entry to a malicious VS Code extension. HN viewed the sparse announcement as serious but disagreed whether its timing signaled uncontrolled scope or ordinary prompt disclosure driven by contracts and European incident-reporting rules.

### Comment pulse

- Scope remains the central unknown → internal source can expose secrets, tooling, defenses, and attack paths even when customer repositories remain untouched.
- Corporate phrasing drew skepticism → unauthorized access sounds softer than hacked, while the lack of detail encouraged worst-case interpretations.
- Fast notice is not proof of panic → contractual and DORA/NIS2 timelines may require early supplier-incident reporting before forensic conclusions stabilize.

### LLM perspective

- **View:** Repository count understates risk; sensitivity depends on embedded credentials, architecture, security controls, and whether accessed code enables follow-on compromise.
- **Impact:** GitHub must identify and rotate exposed secrets, audit builds and identities, and give customers evidence-based guidance on required action.
- **Watch next:** Initial-access vector, repository inventory, credential exposure, persistence, customer crossover, timeline, containment status, indicators of compromise, and independent confirmation.
