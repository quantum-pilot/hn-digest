# I found 10k GitHub repositories distributing Trojan malware

- Score: 634 | [HN](https://news.ycombinator.com/item?id=48583928) | Link: https://orchidfiles.com/github-repositories-distributing-malware/

### TL;DR
An individual discovered a large, ongoing malware campaign on GitHub: ~10,000 non-fork repos that clone legitimate projects’ full commit history and contributors, then repeatedly rewrite the latest commit as “Update README.md” to insert a link to a Trojan-containing zip. Using gharchive plus GitHub’s API, they filtered for high-frequency updates where only the README changed and found 25% of such repos matched the pattern. GitHub was slow to react but began mass-deleting once the issue and detection script were publicized; similar activity was documented by security researchers and on Reddit over a year ago.

---

### Comment pulse
- Goal is likely automation abuse → fake repos target AI/“agent” systems that auto-pick dependencies, seeding worm-like account stealers at scale—counterpoint: simple SEO/“Last Updated” gaming might already suffice.  
- Developers report identity hijacking → their names and projects are cloned into “skills”/tool marketplaces with added malicious URLs and sketchy “verifying your browser” gates.  
- Real-world damage is documented → a Disney engineer’s GitHub plugin Trojan yielded months of full-account access, reinforcing advice to separate MFA from password managers and self-compile code.

---

### LLM perspective
- View: This shows how low-friction cloning plus weak repo vetting enables industrial-scale malware that looks “community-trusted” at a glance.  
- Impact: GitHub, security vendors, and corporate DevOps will need automated, behavioral detection of repo-level abuse, not just file-level scanning.  
- Watch next: GitHub’s policy/technical response, AV signatures for this family, and whether package registries/agent platforms start enforcing stronger provenance checks.
