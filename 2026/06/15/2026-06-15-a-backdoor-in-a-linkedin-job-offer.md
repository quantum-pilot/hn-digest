# A backdoor in a LinkedIn job offer

- Score: 549 | [HN](https://news.ycombinator.com/item?id=48546294) | Link: https://roman.pt/posts/linkedin-backdoor/

### TL;DR

A supposed crypto recruiter asked the author to inspect deprecated Node modules in a public GitHub repository. Instead of installing locally, he used a throwaway VPS and a read-only coding agent, which found disguised JavaScript that assembled a remote URL and executed its response. The repository’s npm prepare lifecycle loaded the payload automatically during npm install; both recruiter and commit author impersonated real people. HN readers stressed that this resembles routine interview work, criticized LinkedIn’s weak identity enforcement and npm’s install-time execution, and advocated disposable sandboxes.

### Comment pulse

- Interview pressure weakens caution → candidates want to appear responsive, making a broken repository and urgent install request unusually plausible.
- Platform identity signals are unreliable → fake recruiters can claim real employers, buy Premium, cultivate posts, and survive repeated reports.
- Enforcement faces asymmetric economics → campaigns are cheap and cross-border, while investigation and prosecution are expensive — counterpoint: IC3 accepts reports but rarely responds.

### LLM perspective

- **View:** Treat recruitment repositories as untrusted artifacts; static inspection should precede dependency resolution, builds, editor plugins, or any lifecycle hook.
- **Impact:** Job seekers face disproportionate risk because assessment speed and technical credibility are weaponized against normal professional habits.
- **Watch next:** Adopt network-denied containers, locked dependency scripts, signed commits, verified domains, and automated scanning for install-time execution.
