# GitHub is investigating unauthorized access to their internal repositories

- Score: 605 | [HN](https://news.ycombinator.com/item?id=48201316) | Link: https://twitter.com/github/status/2056884788179726685

- TL;DR  
    - GitHub reports unauthorized access to its internal repositories, with an attacker claiming about 3,800 repos exfiltrated, likely via a malicious VS Code extension. GitHub says there is no current evidence of customer organizations or hosted code being affected. Filenames in the stolen set suggest internal tools for spam handling, Copilot abuse, law-enforcement portals, and secret scanning, raising concern about exposed capabilities. HN discussion centers on how serious this is, corporate breach language, and regulatory pressure to disclose quickly.  
*Content unavailable; summarizing from title/comments.*

### Comment pulse
- Breach appears limited to GitHub-internal repos → leaked file list suggests internal systems for spam, Copilot abuse, law-enforcement portals, and secret scanning may be exposed.  
- Some see this as a major, still-unbounded incident → early disclosure without details implies serious concern—counterpoint: investors barely reacted to much larger Microsoft cloud breaches.  
- Disclosure timing → commenters argue contracts and EU rules like DORA/NIS2 force rapid notification of supplier incidents, limiting GitHub’s ability to stay quiet.

### LLM perspective
- View: GitHub’s risk is disclosure of internal security tooling and processes, which can aid future attackers even without customer code theft.  
- Impact: Incident will pressure large SaaS vendors to harden dev environments and extension ecosystems, not just production infrastructure and perimeter defenses.  
- Watch next: Key questions: scope of sensitive repos, any credential reuse to customer systems, and whether GitHub publishes remediation timelines and changes.
