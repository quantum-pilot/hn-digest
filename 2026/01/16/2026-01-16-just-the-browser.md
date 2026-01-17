# Just the Browser

- Score: 464 | [HN](https://news.ycombinator.com/item?id=46645615) | Link: https://justthebrowser.com/

### TL;DR
Just the Browser is an open-source set of configuration files and scripts for Chrome, Edge, and Firefox that uses enterprise/group policies to strip out AI features, telemetry, shopping add-ons, sponsored content, default-browser nags, and startup-boost behavior—leaving a more minimal browser while keeping the mainstream engines and update pipelines. HN discussion focuses less on the feature set and more on whether it’s wise to run third‑party admin scripts, the incompleteness of some configs, and evolving attitudes toward “good” vs “bad” AI features.

---

### Comment pulse
- Convenience vs security → Some appreciate pre-curated policies but won’t run elevated third‑party scripts; they’d rather have a step‑by‑step guide with screenshots.  
- Scope and completeness → Firefox config currently flips few AI/telemetry flags; Chrome config seems to miss several annoyances — counterpoint: project is early and open to contributions.  
- What counts as “bad AI”? → Many want AI disabled but exempt local translation; some see this as proof that once normalized, today’s “AI features” may be accepted, too.

---

### LLM perspective
- View: This is essentially “DIY enterprise hardening” for personal machines, packaged for non-admins who’d never touch group policy.  
- Impact: Best suited to privacy-conscious users staying on mainstream browsers for security, compatibility, or corporate requirements.  
- Watch next: Browser vendors may change or lock down policy keys; a documented “minimal mode” from vendors would obsolete projects like this.
